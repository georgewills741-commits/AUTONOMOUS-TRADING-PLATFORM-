"""The `atp` command (D1 of the Stage 1 plan). Its one command checks a configuration.

    atp config check --env <environment> --config-dir <directory>

It loads the configuration of that environment from the directory (`atp.config`), reading the
declared secrets from the process environment, and prints a summary in which every secret's
value is `<redacted>`. Exit status: 0 when the configuration is valid; 1 when it is refused,
with the reasons on standard error; 2 when the command is used wrongly. This module imports only
`atp.config`, and no module imports it.

Requirements: MIG-004 (the configuration directory is always given: the command has no default
for it), SEC-005 (the secrets come from the process environment, and are printed only as
`<redacted>`).
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from atp.config import (
    ConfigurationError,
    ProcessEnvironment,
    configure_process,
    load_configuration,
    summary,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="atp", description="The autonomous trading platform's command."
    )
    commands = parser.add_subparsers(dest="command", required=True)
    config = commands.add_parser("config", help="work with the configuration")
    config_commands = config.add_subparsers(dest="config_command", required=True)
    check = config_commands.add_parser(
        "check", help="validate one environment's configuration"
    )
    check.add_argument(
        "--env", required=True, help="the environment, one of OPS-004's six"
    )
    check.add_argument(
        "--config-dir",
        required=True,
        type=Path,
        help="the directory holding platform.toml and environments/<env>.toml",
    )
    return parser


def main(arguments: Sequence[str] | None = None) -> int:
    """Run the command; return its exit status."""
    options = _parser().parse_args(arguments)
    configure_process()
    try:
        configuration = load_configuration(
            options.config_dir, options.env, ProcessEnvironment()
        )
    except ConfigurationError as error:
        print("configuration refused:", file=sys.stderr)
        for line in error.lines:
            print(f"  {line}", file=sys.stderr)
        return 1
    print("configuration valid:")
    for line in summary(configuration):
        print(f"  {line}")
    return 0


def run() -> None:
    """The installed `atp` command's entry point."""
    sys.exit(main())
