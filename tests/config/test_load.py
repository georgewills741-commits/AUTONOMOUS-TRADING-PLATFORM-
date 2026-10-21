"""Loading the configuration: TOML in its JSON form, fail closed, no value in any error (MIG-004,
MIG-010, MIG-027, OPS-004, SEC-005; constitution Rules 108 to 111)."""

from __future__ import annotations

import decimal
import enum
import threading
from decimal import Decimal
from pathlib import Path

import pytest

from atp.config import (
    REDACTED,
    Configuration,
    ConfigurationError,
    Environment,
    ProcessEnvironment,
    SecretKind,
    configure_process,
    environment_named,
    load_configuration,
    read_toml,
    summary,
)
from atp.contracts import Amount, Contract, ContractVersion
from atp.numeric import decimal_context_is_configured

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = REPOSITORY_ROOT / "config" / "examples"
EXAMPLE_VARIABLE = "ATP_EXAMPLE_SERVER_CREDENTIAL"

# Assembled at run time so that no file holds a credential-shaped sample.
SECRET = "sk" + "_live_" + "Q7x9Z2" + "secretvalue"


class Side(enum.Enum):
    BUY = "buy"
    SELL = "sell"


class Limit(Contract):
    contract_id = "test.config.limit"
    contract_version = ContractVersion(1, 0)
    size: Amount
    count: int = 0


class Book(Contract):
    contract_id = "test.config.book"
    contract_version = ContractVersion(1, 0)
    sides: tuple[Side, ...]
    limits: tuple[Limit, ...] = ()
    enabled: bool = False


def _directory(tmp_path: Path, portable: str, environments: dict[str, str]) -> Path:
    (tmp_path / "platform.toml").write_text(portable, encoding="utf-8")
    (tmp_path / "environments").mkdir()
    for name, text in environments.items():
        (tmp_path / "environments" / f"{name}.toml").write_text(text, encoding="utf-8")
    return tmp_path


def _specific(name: str, secrets: str = "") -> str:
    return f'environment = "{name}"\nenvironment_id = "example-{name}"\n{secrets}'


SERVER_DECLARATION = '[[secrets]]\nname = "ATP_DB"\nkind = "server"\n'


def _refusal(directory: Path, name: str, variables: dict[str, str]) -> list[str]:
    with pytest.raises(ConfigurationError) as error:
        load_configuration(directory, name, ProcessEnvironment(variables))
    return list(error.value.lines)


# Reading TOML documents (the stage record's question for U4: how a TOML document reaches a
# contract, and how an amount setting written as a TOML integer is read).


def test_a_toml_document_is_read_in_its_json_form() -> None:
    book = read_toml(
        Book,
        'sides = ["buy", "sell"]\nenabled = true\n'
        '[[limits]]\nsize = "1.50"\ncount = 2\n',
        "book.toml",
    )
    assert book.sides == (Side.BUY, Side.SELL)
    assert book.limits == (Limit(size=Decimal("1.50"), count=2),)
    assert type(book.limits[0].size) is Decimal
    assert book.enabled is True


@pytest.mark.parametrize("size", ["3", "-3", "0"])
def test_an_amount_written_as_a_toml_integer_is_refused(size: str) -> None:
    with pytest.raises(ConfigurationError) as error:
        read_toml(Limit, f"size = {size}\n", "limit.toml")
    assert error.value.lines[0] == (
        "limit.toml: input refused by contract test.config.limit:"
    )
    assert "[amount_type]" in error.value.lines[1]


@pytest.mark.parametrize("number", ["1.5", "1e3", "1.0", "-0.0", "1_000.5"])
def test_a_toml_number_with_a_fraction_or_an_exponent_is_refused(number: str) -> None:
    with pytest.raises(ConfigurationError) as error:
        read_toml(Limit, f'size = "1"\ncount = {number}\n', "limit.toml")
    assert error.value.lines == (
        (
            "limit.toml: a number with a fraction or an exponent is not a setting value; "
            "an amount is written as a string"
        ),
    )


@pytest.mark.parametrize("number", ["inf", "-inf", "nan", "+nan"])
def test_a_toml_infinity_or_nan_is_refused(number: str) -> None:
    with pytest.raises(ConfigurationError) as error:
        read_toml(Limit, f"size = {number}\n", "limit.toml")
    assert error.value.lines == (
        (
            "limit.toml: a number is refused: "
            "an amount must be a decimal number in the accepted text form"
        ),
    )


@pytest.mark.parametrize(
    "value",
    ["2026-10-21", "2026-10-21T04:00:00Z", "2026-10-21T04:00:00", "04:00:00"],
)
def test_a_toml_date_or_time_is_refused(value: str) -> None:
    with pytest.raises(ConfigurationError) as error:
        read_toml(Limit, f'size = "1"\n[when]\nat = {value}\n', "limit.toml")
    assert error.value.lines == ("limit.toml: a date or a time is not a setting value",)


def test_an_integer_stays_an_integer_and_text_stays_text() -> None:
    assert read_toml(Limit, 'size = "7"\ncount = 7\n', "x").count == 7
    with pytest.raises(ConfigurationError):
        read_toml(Limit, 'size = "7"\ncount = "7"\n', "x")
    with pytest.raises(ConfigurationError):
        read_toml(Book, 'sides = ["buy"]\nenabled = 1\n', "x")


@pytest.mark.parametrize(
    "text",
    [
        "size = ",
        'size = "1"\nsize = "2"\n',
        "[secret_table]\n[secret_table]\n",
        'size = "unterminated',
        "= 3",
    ],
)
def test_invalid_toml_is_refused_with_its_position_only(text: str) -> None:
    with pytest.raises(ConfigurationError) as error:
        read_toml(Limit, text, "limit.toml")
    (line,) = error.value.lines
    assert line.startswith("limit.toml: not valid TOML (at ")
    assert "secret_table" not in line


def test_a_refused_toml_value_is_not_in_the_error() -> None:
    with pytest.raises(ConfigurationError) as error:
        read_toml(Limit, f'size = "{SECRET}"\n', "limit.toml")
    assert SECRET not in str(error.value)
    with pytest.raises(ConfigurationError) as error:
        read_toml(Limit, f'size = "1"\n{SECRET} = 1\n', "limit.toml")
    assert SECRET not in str(error.value)


# Loading a configuration directory.


def test_a_configuration_loads_with_its_secrets(tmp_path: Path) -> None:
    directory = _directory(
        tmp_path,
        'platform_id = "atp"\n',
        {"paper": _specific("paper", SERVER_DECLARATION)},
    )
    configuration = load_configuration(
        directory, "paper", ProcessEnvironment({"ATP_DB": SECRET})
    )
    assert configuration.portable.platform_id == "atp"
    assert configuration.environment.environment is Environment.PAPER
    assert configuration.environment.environment_id == "example-paper"
    ((declaration, secret),) = configuration.secrets
    assert declaration.name == "ATP_DB"
    assert declaration.kind is SecretKind.SERVER
    assert secret.reveal() == SECRET


def test_an_unknown_environment_is_refused(tmp_path: Path) -> None:
    directory = _directory(
        tmp_path, 'platform_id = "atp"\n', {"prod": _specific("paper")}
    )
    assert _refusal(directory, "prod", {}) == [
        (
            "unknown environment: the environments are development, testing, research, "
            "paper, staging, production"
        )
    ]
    with pytest.raises(ConfigurationError):
        environment_named("Paper")
    assert environment_named("paper") is Environment.PAPER


def test_the_environment_must_be_the_one_the_file_declares(tmp_path: Path) -> None:
    directory = _directory(
        tmp_path, 'platform_id = "atp"\n', {"paper": _specific("production")}
    )
    assert _refusal(directory, "paper", {}) == [
        "environments/paper.toml: declares the environment production, not paper"
    ]


@pytest.mark.parametrize("missing", ["platform.toml", "environments/paper.toml"])
def test_a_missing_file_is_refused(tmp_path: Path, missing: str) -> None:
    directory = _directory(
        tmp_path, 'platform_id = "atp"\n', {"paper": _specific("paper")}
    )
    (directory / missing).unlink()
    assert _refusal(directory, "paper", {}) == [
        f"{missing}: no such file in the configuration directory"
    ]


def test_a_directory_in_place_of_a_file_is_refused(tmp_path: Path) -> None:
    directory = _directory(tmp_path, 'platform_id = "atp"\n', {})
    (directory / "environments" / "paper.toml").mkdir()
    assert _refusal(directory, "paper", {}) == [
        "environments/paper.toml: no such file in the configuration directory"
    ]


def test_a_file_that_is_not_utf_8_is_refused(tmp_path: Path) -> None:
    directory = _directory(tmp_path, "", {"paper": _specific("paper")})
    (directory / "platform.toml").write_bytes(b'platform_id = "\xff"\n')
    assert _refusal(directory, "paper", {}) == ["platform.toml: not UTF-8 text"]


@pytest.mark.parametrize(
    ("portable", "first_line"),
    [
        ("", "platform.toml: input refused by contract atp.config.portable:"),
        (
            'platform_id = "Atp"\n',
            "platform.toml: input refused by contract atp.config.portable:",
        ),
        (
            'platform_id = "atp"\nhost = "h"\n',
            "platform.toml: input refused by contract atp.config.portable:",
        ),
        ("platform_id = ", "platform.toml: not valid TOML (at end of document)"),
    ],
)
def test_a_missing_unknown_or_malformed_setting_stops_the_load(
    tmp_path: Path, portable: str, first_line: str
) -> None:
    directory = _directory(tmp_path, portable, {"paper": _specific("paper")})
    assert _refusal(directory, "paper", {})[0] == first_line


def test_a_trading_credential_outside_production_stops_the_load(tmp_path: Path) -> None:
    trading = '[[secrets]]\nname = "ATP_T"\nkind = "trading"\n'
    directory = _directory(
        tmp_path, 'platform_id = "atp"\n', {"staging": _specific("staging", trading)}
    )
    assert _refusal(directory, "staging", {"ATP_T": SECRET}) == [
        "environments/staging.toml: input refused by contract atp.config.environment:",
        "  secrets: invalid value [trading_credential_outside_production]",
    ]


@pytest.mark.parametrize("variables", [{}, {"ATP_DB": ""}])
def test_a_secret_that_is_not_set_or_empty_stops_the_load(
    tmp_path: Path, variables: dict[str, str]
) -> None:
    directory = _directory(
        tmp_path,
        'platform_id = "atp"\n',
        {"paper": _specific("paper", SERVER_DECLARATION)},
    )
    assert _refusal(directory, "paper", variables) == [
        "the secret ATP_DB is not set, or is empty, in the process environment"
    ]


@pytest.mark.parametrize(
    ("portable", "secrets", "value", "file"),
    [
        (
            f'platform_id = "atp"\n# {SECRET}\n',
            SERVER_DECLARATION,
            SECRET,
            "platform.toml",
        ),
        (
            'platform_id = "atp"\n',
            SERVER_DECLARATION + f"# {SECRET}\n",
            SECRET,
            "environments/paper.toml",
        ),
        # A valid setting whose value is the secret's.
        (
            'platform_id = "atp-shared"\n',
            SERVER_DECLARATION,
            "atp-shared",
            "platform.toml",
        ),
    ],
)
def test_a_secret_value_in_a_configuration_file_stops_the_load(
    tmp_path: Path, portable: str, secrets: str, value: str, file: str
) -> None:
    directory = _directory(tmp_path, portable, {"paper": _specific("paper", secrets)})
    lines = _refusal(directory, "paper", {"ATP_DB": value})
    assert lines == [f"{file}: holds the value of the secret ATP_DB"]


def test_the_summary_shows_no_secret_value(tmp_path: Path) -> None:
    directory = _directory(
        tmp_path,
        'platform_id = "atp"\n',
        {"paper": _specific("paper", SERVER_DECLARATION)},
    )
    configuration = load_configuration(
        directory, "paper", ProcessEnvironment({"ATP_DB": SECRET})
    )
    assert summary(configuration) == [
        "platform_id: atp",
        "environment: paper",
        "environment_id: example-paper",
        f"secret ATP_DB (server): {REDACTED}",
    ]
    assert SECRET not in repr(configuration)


def test_the_summary_says_when_no_secret_is_declared(tmp_path: Path) -> None:
    directory = _directory(
        tmp_path, 'platform_id = "atp"\n', {"paper": _specific("paper")}
    )
    configuration = load_configuration(directory, "paper", ProcessEnvironment({}))
    assert summary(configuration)[-1] == "secrets: none declared"


def test_a_configuration_is_immutable(tmp_path: Path) -> None:
    directory = _directory(
        tmp_path, 'platform_id = "atp"\n', {"paper": _specific("paper")}
    )
    configuration = load_configuration(directory, "paper", ProcessEnvironment({}))
    assert isinstance(configuration, Configuration)
    with pytest.raises(AttributeError):
        configuration.secrets = ()  # type: ignore[misc]


def test_configure_process_sets_the_decimal_context() -> None:
    seen: list[bool] = []

    def in_a_thread() -> None:
        decimal.getcontext().prec = 10
        seen.append(decimal_context_is_configured())
        configure_process()
        seen.append(decimal_context_is_configured())

    worker = threading.Thread(target=in_a_thread)
    worker.start()
    worker.join()
    assert seen == [False, True]


# The example configuration (config/examples/), one file per environment.


@pytest.mark.parametrize("environment", [e.value for e in Environment])
def test_every_example_environment_loads(environment: str) -> None:
    configuration = load_configuration(
        EXAMPLES, environment, ProcessEnvironment({EXAMPLE_VARIABLE: SECRET})
    )
    assert configuration.environment.environment.value == environment
    assert configuration.environment.environment_id == f"example-{environment}"
    assert all(
        declaration.kind is not SecretKind.TRADING
        for declaration, _secret in configuration.secrets
    )
    assert summary(configuration)[-1] == (
        f"secret {EXAMPLE_VARIABLE} (server): {REDACTED}"
    )


def test_the_examples_are_the_six_environments_and_the_portable_part() -> None:
    files = sorted(
        path.relative_to(EXAMPLES).as_posix()
        for path in EXAMPLES.rglob("*")
        if path.is_file()
    )
    assert files == sorted(
        ["platform.toml", *(f"environments/{e.value}.toml" for e in Environment)]
    )
