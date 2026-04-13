"""Dagger pipeline for Apollo SDK generation via Stainless."""
from __future__ import annotations

import os
import sys
import asyncio
import logging
import argparse

import dagger

logger = logging.getLogger(__name__)

# Install the stl CLI inside the build container.
#
# Download the latest pre-built binary from GitHub releases rather than using
# the install script which may not work in all environments.
STL_INSTALL_CMDS: list[list[str]] = [
    ["apt-get", "update", "-qq"],
    ["apt-get", "install", "-y", "--no-install-recommends", "curl", "ca-certificates"],
    [
        "sh",
        "-c",
        "curl -fsSL https://github.com/stainless-api/stainless-api-cli/releases/download/v0.1.0-alpha.79/stl_0.1.0-alpha.79_linux_amd64.tar.gz | tar -xz -C /usr/local/bin",
    ],
]


async def generate(force: bool) -> None:
    """Trigger a Stainless cloud build and pull the generated SDK files."""
    # Validate that the API key is set before proceeding
    if "STAINLESS_API_KEY" not in os.environ:
        raise ValueError(
            "STAINLESS_API_KEY environment variable is not set. "
            "Please set this variable with your Stainless API credentials."
        )

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

        # Verify stl was installed correctly
        ctr = ctr.with_exec(["stl", "--version"])

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

        # Capture both stdout and stderr to aid debugging
        try:
            output = await ctr.stdout()
            logger.info(output)
        except dagger.ExecError as e:
            # If the command failed, also log stderr for debugging
            stderr = await ctr.stderr()
            logger.error(f"Stainless CLI error (exit code {e.exit_code}):")
            logger.error(f"STDERR: {stderr}")
            logger.error(
                "\nCommon causes:\n"
                "  - Invalid or expired STAINLESS_API_KEY\n"
                "  - Project 'apollo-sdk' not found or not accessible\n"
                "  - Network or API server issues"
            )
            raise

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
