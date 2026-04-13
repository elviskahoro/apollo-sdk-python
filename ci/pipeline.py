"""Dagger pipeline for Apollo SDK generation via Stainless.

stl exits non-zero when any build target has a failing conclusion (e.g.
upstream test failures in stainless-sdks/apollo-python), even though the
build itself completed and --pull wrote generated files. We capture the
output and exit code separately so the pipeline succeeds when the commit
target completed, regardless of upstream test status.
"""

import os
import sys
import json
import asyncio
import logging
import argparse

import dagger
from dagger import dag

logger = logging.getLogger(__name__)

STL_VERSION = "0.1.0-alpha.88"
STL_URL = (
    f"https://github.com/stainless-api/stainless-api-cli/releases/download/"
    f"v{STL_VERSION}/stl_{STL_VERSION}_linux_amd64.tar.gz"
)

STL_INSTALL_CMDS = [
    ["apt-get", "update"],
    ["apt-get", "install", "-y", "curl"],
    ["sh", "-c", f"curl -fsSL {STL_URL} | tar xz -C /usr/local/bin stl"],
]


def check_build_result(raw_output: str) -> None:
    """Parse stl JSON output and fail only if the commit target didn't complete."""
    # stl can print multiple JSON objects (status + build result). Parse all
    # and use the last one that has a "targets" key (the build object).
    decoder = json.JSONDecoder()
    build = None
    pos = 0
    while pos < len(raw_output):
        idx = raw_output.find("{", pos)
        if idx == -1:
            break
        try:
            obj, end = decoder.raw_decode(raw_output, idx)
            if "targets" in obj or "error" in obj:
                build = obj
            pos = end
        except json.JSONDecodeError:
            pos = idx + 1

    if build is None:
        logger.error(raw_output)
        raise SystemExit("stl produced no parseable build output")
    logger.info(json.dumps(build, indent=2))

    # "No changes to commit" — stl returns an error object, not a build object
    if build.get("error") == "bad request" and "no changes" in build.get("message", "").lower():
        logger.info("No changes to commit — nothing to generate")
        return

    python_target = build.get("targets", {}).get("python", {})
    commit_status = python_target.get("commit", {}).get("status")
    commit_conclusion = (
        python_target.get("commit", {}).get("completed", {}).get("conclusion")
    )
    test_conclusion = (
        python_target.get("test", {}).get("completed", {}).get("conclusion")
    )

    if commit_status != "completed":
        raise SystemExit(
            f"SDK commit target did not complete (status: {commit_status})"
        )

    if commit_conclusion not in ("success",):
        raise SystemExit(
            f"SDK commit target concluded with '{commit_conclusion}'"
        )

    if test_conclusion and test_conclusion != "success":
        raise SystemExit(
            f"Upstream tests concluded with '{test_conclusion}'"
        )

    logger.info("Build completed (commit: %s, tests: %s)", commit_conclusion, test_conclusion)


async def generate(force: bool) -> None:
    """Trigger a Stainless cloud build and pull generated SDK files."""
    async with dagger.connection(
        config=dagger.Config(log_output=sys.stderr),
    ):
        source = dag.host().directory(".")
        stainless_key = dag.set_secret(
            "stainless-api-key",
            os.environ["STAINLESS_API_KEY"],
        )

        ctr = dag.container().from_("python:3.13-slim")

        for cmd in STL_INSTALL_CMDS:
            ctr = ctr.with_exec(cmd)

        # stl command — wrapped in sh to capture exit code without failing
        # the container. All args are static, no user input.
        stl_args = [
            "stl", "builds", "create",
            "--project", "apollo",
            "--target", "python",
            "--branch", "main",
            "--wait", "all",
            "--pull",
        ]
        if force:
            stl_args.append("--allow-empty")

        stl_cmd = " ".join(stl_args)
        wrapper = f"{stl_cmd} > /tmp/stl-output.txt 2>&1; echo $? > /tmp/stl-exit-code"

        ctr = (
            ctr
            .with_directory("/repo", source)
            .with_workdir("/repo")
            .with_secret_variable("STAINLESS_API_KEY", stainless_key)
            .with_exec(["sh", "-c", wrapper])
        )

        exit_code = (await ctr.file("/tmp/stl-exit-code").contents()).strip()
        output = (await ctr.file("/tmp/stl-output.txt").contents()).strip()

        if exit_code == "0":
            logger.info(output)
        else:
            check_build_result(output)

        await ctr.directory("/repo/src").export("./src")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description="Apollo SDK generation pipeline")
    parser.add_argument("command", choices=["generate"])
    parser.add_argument("--force", default="false")
    args = parser.parse_args()
    asyncio.run(generate(force=args.force == "true"))
