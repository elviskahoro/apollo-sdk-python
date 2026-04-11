"""Dagger pipeline for Apollo SDK generation via Stainless."""
from __future__ import annotations

import os
import sys
import asyncio
import argparse

import dagger

# Install the stl CLI inside the build container.
#
# Spike findings (Task 1) should confirm the working install sequence on
# python:3.13-slim before this pipeline runs in CI.  The commands below
# follow the documented install path; update if the spike reveals a
# different binary location or install mechanism (e.g. direct GitHub
# release download).
STL_INSTALL_CMDS: list[list[str]] = [
    ["apt-get", "update", "-qq"],
    ["apt-get", "install", "-y", "--no-install-recommends", "curl", "ca-certificates"],
    ["sh", "-c", "curl -fsSL https://stainless.com/install.sh | sh"],
]


async def generate(force: bool) -> None:
    """Trigger a Stainless cloud build and pull the generated SDK files."""
    async with dagger.Connection(
        dagger.Config(log_output=sys.stderr),
    ) as client:
        # Mount the entire repo so stl can read .stainless/ config and spec.
        source = client.host().directory(".")

        stainless_key = client.set_secret(
            "stainless-api-key",
            os.environ["STAINLESS_API_KEY"],
        )

        # Lightweight base — stl is a self-contained binary.
        ctr = client.container().from_("python:3.13-slim")

        for cmd in STL_INSTALL_CMDS:
            ctr = ctr.with_exec(cmd)

        # Build the stl invocation.  --pull writes generated files back into
        # the repo directory relative to the working directory.
        args = [
            "stl",
            "builds",
            "create",
            "--project",
            "apollo-sdk",
            "--target",
            "python",
            "--wait",
            "all",
            "--pull",
        ]
        if force:
            # --allow-empty forces regeneration even when no config/spec diff
            # exists.  Spike (Task 1.3) must confirm this flag is supported.
            args.append("--allow-empty")

        ctr = (
            ctr.with_directory("/repo", source)
            .with_workdir("/repo")
            .with_secret_variable("STAINLESS_API_KEY", stainless_key)
            .with_exec(args)
        )

        output = await ctr.stdout()
        sys.stdout.write(output)

        # Export the generated SDK files back to the host working directory.
        # --pull writes into src/ relative to /repo; mirror that back.
        await ctr.directory("/repo/src").export("./src")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apollo SDK generation pipeline")
    parser.add_argument("command", choices=["generate"])
    parser.add_argument(
        "--force",
        default="false",
        help="Pass 'true' to force regeneration with --allow-empty",
    )
    args = parser.parse_args()
    asyncio.run(generate(force=args.force.lower() == "true"))
