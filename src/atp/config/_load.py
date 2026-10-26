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

_TOO_DEEP: Final = "nested too deeply to read"


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

    `where` names the document in errors. Every refusal raises `ConfigurationError`, whose
    lines hold no value from the document; a document nested too deeply to read is refused
    too.
    """
    return _read_toml(contract, text, where)[0]


def _read_toml[C: Contract](
    contract: type[C], text: str, where: str
) -> tuple[C, object]:
    """`read_toml`, with the document's JSON form, which the loader searches for secrets.

    Every step of the reading (parsing, the JSON form, validation) is inside one boundary: a
    failure of any of them, of a class the document can cause, becomes `ConfigurationError`.
    """
    try:
        form = _json_form(_parse_toml(text, where), where)
        return contract.from_json(json.dumps(form)), form
    except ConfigurationError:
        raise
    except ContractError as error:
        first, *details = str(error).splitlines()
        raise ConfigurationError([f"{where}: {first}", *details]) from None
    except RecursionError:
        raise ConfigurationError([f"{where}: {_TOO_DEEP}"]) from None
    except ValueError:
        # Any other refusal of a step: an integer too long to convert, in the reader (decimal)
        # or in the JSON form (hexadecimal, octal, or binary), which TOML's 64-bit integers
        # exclude anyway. Its text can quote the document, so none of it is kept.
        raise ConfigurationError([f"{where}: not valid TOML"]) from None


def _parse_toml(text: str, where: str) -> dict[str, object]:
    try:
        return tomllib.loads(text, parse_float=amount_from_toml)
    except tomllib.TOMLDecodeError as error:
        position = _TOML_POSITION.search(str(error))
        suffix = f" ({position.group(1)})" if position else ""
        raise ConfigurationError([f"{where}: not valid TOML{suffix}"]) from None
    except AmountError as error:
        # Its message is fixed text, never the number (`atp.numeric.AMOUNT_REFUSALS`).
        raise ConfigurationError([f"{where}: a number is refused: {error}"]) from None


def _read_file(directory: Path, relative: str) -> str:
    """A file's text. Looking at the file and reading it are inside one boundary: an
    operating-system error of either becomes `ConfigurationError`."""
    path = directory / relative
    try:
        if not path.is_file():
            raise ConfigurationError(
                [f"{relative}: no such file in the configuration directory"]
            )
        return path.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        raise ConfigurationError([f"{relative}: not UTF-8 text"]) from None
    except OSError as error:
        reason = f" ({error.strerror})" if error.strerror else ""
        raise ConfigurationError([f"{relative}: cannot be read{reason}"]) from None


def _setting_texts(form: object) -> list[str]:
    """Every text value of a document in its JSON form, nested ones included."""
    texts: list[str] = []
    pending: list[object] = [form]
    while pending:
        value = pending.pop()
        if isinstance(value, str):
            texts.append(value)
        elif isinstance(value, list):
            pending.extend(value)
        elif isinstance(value, dict):
            pending.extend(value.values())
    return texts


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
    secret that is not set or is empty, or whose value appears in either file or in a setting's
    value as read, stops the load. Every refusal raises `ConfigurationError`.
    """
    environment = environment_named(environment_name)
    environment_file = f"{ENVIRONMENTS_DIRECTORY}/{environment.value}.toml"
    portable_text = _read_file(directory, PORTABLE_FILE)
    environment_text = _read_file(directory, environment_file)
    portable, portable_form = _read_toml(
        PortableConfiguration, portable_text, PORTABLE_FILE
    )
    specific, specific_form = _read_toml(
        EnvironmentConfiguration, environment_text, environment_file
    )
    if specific.environment is not environment:
        msg = (
            f"{environment_file}: declares the environment {specific.environment.value}, "
            f"not {environment.value}"
        )
        raise ConfigurationError([msg])
    searched = (
        (PORTABLE_FILE, portable_text, _setting_texts(portable_form)),
        (environment_file, environment_text, _setting_texts(specific_form)),
    )
    secrets: list[tuple[SecretDeclaration, Secret]] = []
    for declaration in specific.secrets:
        value = source.secret_value(declaration.name)
        if not value:
            msg = (
                f"the secret {declaration.name} is not set, or is empty, in the process "
                "environment"
            )
            raise ConfigurationError([msg])
        for relative, text, settings in searched:
            # As written, comments included, and as read, where a TOML escape is undone.
            if value in text or any(value in setting for setting in settings):
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
