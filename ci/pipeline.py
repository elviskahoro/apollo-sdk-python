"""Dagger pipeline for Apollo SDK generation via Stainless."""

import argparse
import asyncio
import os
import sys

import dagger
from dagger import dag

STL_VERSION = "0.1.0-alpha.88"
STL_URL = (
    f"https://github.com/stainless-api/stainless-api-cli/releases/download/"
    f"v{STL_VERSION}/stl_{STL_VERSION}_linux_amd64.tar.gz"
)

# Install stl CLI from GitHub releases — the old install script URL 404s.
STL_INSTALL_CMDS = [
    ["apt-get", "update"],
    ["apt-get", "install", "-y", "curl"],
    ["sh", "-c", f"curl -fsSL {STL_URL} | tar xz -C /usr/local/bin stl"],
]


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

        # Lightweight base — stl is a static Go binary
        ctr = dag.container().from_("python:3.13-slim")

        # Install stl CLI
        for cmd in STL_INSTALL_CMDS:
            ctr = ctr.with_exec(cmd)

        # Build stl command
        args = [
            "stl", "builds", "create",
            "--project", "apollo",
            "--target", "python",
            "--branch", "main",
            "--wait", "all",
            "--pull",
        ]
        if force:
            args.append("--allow-empty")

        ctr = (
            ctr
            .with_directory("/repo", source)
            .with_workdir("/repo")
            .with_secret_variable("STAINLESS_API_KEY", stainless_key)
            .with_exec(args)
        )

        output = await ctr.stdout()
        print(output)

        # Export generated SDK files back to host
        await ctr.directory("/repo/src").export("./src")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apollo SDK generation pipeline")
    parser.add_argument("command", choices=["generate"])
    parser.add_argument("--force", default="false")
    args = parser.parse_args()
    asyncio.run(generate(force=args.force == "true"))
