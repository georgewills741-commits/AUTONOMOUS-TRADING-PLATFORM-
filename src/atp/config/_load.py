"""Loading the configuration: fail closed, report without input (MIG-010, SEC-005; Rule 108).

A configuration directory holds the portable part, `platform.toml`, and one environment-specific
file per environment, `environments/<environment>.toml`. Each file is read with the standard
library's TOML reader, its floats through the amount constructor (`parse_float`), and is then
validated in its JSON form by its contract's `from_json`: tables become objects, arrays become
arrays, and a TOML file is read exactly as the same settings written in JSON would be. So an
amount is written as a string; a TOML date, time, or number with a fraction or an exponent is
refused, since no setting takes one.
"""

from __future__ import annotations

import datetime
import json
import re
import tomllib
from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Final

from atp.config._secrets import REDACTED, Secret, SecretSource
from atp.config._settings import (
    Environment,
    EnvironmentConfiguration,
    PortableConfiguration,
    SecretDeclaration,
)
from atp.contracts import Contract, ContractError
from atp.numeric import AmountError, amount_from_toml, configure_decimal_context

PORTABLE_FILE: Final = "platform.toml"
"""The portable part, in the configuration directory."""

ENVIRONMENTS_DIRECTORY: Final = "environments"
"""The directory, inside the configuration directory, of the environment-specific files."""

# Where a TOML error is: the reader's messages can quote a key from the file, so only this
# suffix of them is kept.
_TOML_POSITION: Final = re.compile(
    r"\((at line [0-9]+, column [0-9]+|at end of document)\)$"
)


class ConfigurationError(ValueError):
    """A configuration was refused. Its lines name files, settings, and secrets, and never hold
    a secret's value or a refused value."""

    def __init__(self, lines: Sequence[str]) -> None:
        self.lines = tuple(lines)
        super().__init__("\n".join(self.lines))


@dataclass(frozen=True, slots=True)
class Configuration:
    """A loaded configuration: both parts, and each declared secret's value."""

    portable: PortableConfiguration
    environment: EnvironmentConfiguration
    secrets: tuple[tuple[SecretDeclaration, Secret], ...]


def configure_process() -> None:
    """What a platform process sets up at start, before it reads its configuration: the
    decimal context (`atp.numeric`), so that TOML floats are read as amounts."""
    configure_decimal_context()


def _json_form(value: object, where: str) -> object:
    """A parsed TOML value in its JSON form: tables, arrays, text, integers, and booleans.

    A date or a time, and a number with a fraction or an exponent (which `parse_float` reads
    as an amount), are refused: no setting takes one.
    """
    if isinstance(value, dict):
        return {key: _json_form(item, where) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_form(item, where) for item in value]
    if isinstance(value, datetime.date | datetime.time):
        msg = f"{where}: a date or a time is not a setting value"
        raise ConfigurationError([msg])
    if type(value) is Decimal:
        msg = (
            f"{where}: a number with a fraction or an exponent is not a setting value; "
            "an amount is written as a string"
        )
        raise ConfigurationError([msg])
    return value


def read_toml[C: Contract](contract: type[C], text: str, where: str) -> C:
    """Read a TOML document as the given contract, in its JSON form (see the module docstring).

    `where` names the document in errors. Raises `ConfigurationError`, whose lines hold no
    value from the document.
    """
    try:
        document = tomllib.loads(text, parse_float=amount_from_toml)
    except tomllib.TOMLDecodeError as error:
        position = _TOML_POSITION.search(str(error))
        suffix = f" ({position.group(1)})" if position else ""
        raise ConfigurationError([f"{where}: not valid TOML{suffix}"]) from None
    except AmountError as error:
        # Its message is fixed text, never the number (`atp.numeric.AMOUNT_REFUSALS`).
        raise ConfigurationError([f"{where}: a number is refused: {error}"]) from None
    try:
        return contract.from_json(json.dumps(_json_form(document, where)))
    except ContractError as error:
        first, *details = str(error).splitlines()
        raise ConfigurationError([f"{where}: {first}", *details]) from None


def _read_file(directory: Path, relative: str) -> str:
    path = directory / relative
    if not path.is_file():
        raise ConfigurationError(
            [f"{relative}: no such file in the configuration directory"]
        )
    try:
        return path.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        raise ConfigurationError([f"{relative}: not UTF-8 text"]) from None


def environment_named(name: str) -> Environment:
    """The environment with this name, or `ConfigurationError` if there is none."""
    for environment in Environment:
        if environment.value == name:
            return environment
    names = ", ".join(environment.value for environment in Environment)
    raise ConfigurationError([f"unknown environment: the environments are {names}"])


def load_configuration(
    directory: Path, environment_name: str, source: SecretSource
) -> Configuration:
    """Load the configuration of one environment from a configuration directory.

    The environment-specific file is `environments/<environment_name>.toml`, and the
    environment it declares must be that one. Each declared secret is read from `source`; a
    secret that is not set or is empty, or whose value appears in either file, stops the load.
    Every refusal raises `ConfigurationError`.
    """
    environment = environment_named(environment_name)
    environment_file = f"{ENVIRONMENTS_DIRECTORY}/{environment.value}.toml"
    portable_text = _read_file(directory, PORTABLE_FILE)
    environment_text = _read_file(directory, environment_file)
    portable = read_toml(PortableConfiguration, portable_text, PORTABLE_FILE)
    specific = read_toml(EnvironmentConfiguration, environment_text, environment_file)
    if specific.environment is not environment:
        msg = (
            f"{environment_file}: declares the environment {specific.environment.value}, "
            f"not {environment.value}"
        )
        raise ConfigurationError([msg])
    secrets: list[tuple[SecretDeclaration, Secret]] = []
    for declaration in specific.secrets:
        value = source.secret_value(declaration.name)
        if not value:
            msg = (
                f"the secret {declaration.name} is not set, or is empty, in the process "
                "environment"
            )
            raise ConfigurationError([msg])
        for relative, text in (
            (PORTABLE_FILE, portable_text),
            (environment_file, environment_text),
        ):
            if value in text:
                msg = f"{relative}: holds the value of the secret {declaration.name}"
                raise ConfigurationError([msg])
        secrets.append((declaration, Secret(value)))
    return Configuration(portable, specific, tuple(secrets))


def summary(configuration: Configuration) -> list[str]:
    """The configuration as lines of text, each secret's value shown as `<redacted>`."""
    lines = [
        f"platform_id: {configuration.portable.platform_id}",
        f"environment: {configuration.environment.environment.value}",
        f"environment_id: {configuration.environment.environment_id}",
    ]
    if not configuration.secrets:
        lines.append("secrets: none declared")
    for declaration, _secret in configuration.secrets:
        lines.append(
            f"secret {declaration.name} ({declaration.kind.value}): {REDACTED}"
        )
    return lines
