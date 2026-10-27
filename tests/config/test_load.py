"""Loading the configuration: TOML in its JSON form, fail closed, no value in any error (MIG-004,
MIG-010, MIG-027, OPS-004, SEC-005; constitution Rules 108 to 111)."""

from __future__ import annotations

import decimal
import enum
import os
import threading
import tracemalloc
from decimal import Decimal
from pathlib import Path
from typing import Self

import pytest
from hypothesis import event, given
from hypothesis import strategies as st

from atp.config import (
    MAXIMUM_DOCUMENT_SIZE,
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


@pytest.mark.parametrize(
    ("text", "refusal"),
    [
        (
            "sides = [1.5]\n",
            "a number with a fraction or an exponent is not a setting value",
        ),
        ("sides = [2026-10-21]\n", "a date or a time is not a setting value"),
        (
            'sides = ["buy"]\n[[limits]]\nsize = "1"\ncount = 1e3\n',
            "a number with a fraction",
        ),
        (
            'sides = ["buy"]\n[[limits]]\nsize = "1"\nat = 04:00:00\n',
            "a date or a time",
        ),
    ],
)
def test_a_value_inside_an_array_is_checked_too(text: str, refusal: str) -> None:
    with pytest.raises(ConfigurationError) as error:
        read_toml(Book, text, "book.toml")
    (line,) = error.value.lines
    assert line.startswith(f"book.toml: {refusal}")


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


TOO_LONG = (
    f"limit.toml: longer than {MAXIMUM_DOCUMENT_SIZE} characters, the most a configuration "
    "document may hold"
)


def test_the_limit_on_a_document_is_v_41() -> None:
    # V-41 in the values register records this value and its reason; a change changes both.
    assert MAXIMUM_DOCUMENT_SIZE == 8192


def test_a_document_at_the_limit_is_read() -> None:
    document = 'size = "7"\n#'
    text = document + "x" * (MAXIMUM_DOCUMENT_SIZE - len(document))
    assert len(text) == MAXIMUM_DOCUMENT_SIZE
    assert read_toml(Limit, text, "limit.toml").size == Decimal(7)


@pytest.mark.parametrize("last", ["#", "="], ids=["valid", "not TOML"])
def test_a_document_longer_than_the_limit_is_refused_unread(last: str) -> None:
    # One character more, valid TOML or not: refused for its length, before it is parsed.
    document = 'size = "7"\n#'
    text = document + "x" * (MAXIMUM_DOCUMENT_SIZE - len(document) - 1) + "\n" + last
    assert len(text) == MAXIMUM_DOCUMENT_SIZE + 1
    with pytest.raises(ConfigurationError) as error:
        read_toml(Limit, text, "limit.toml")
    assert error.value.lines == (TOO_LONG,)


def test_the_reading_of_the_worst_document_within_the_limit_is_bounded() -> None:
    # The reader's memory grows with the square of a dotted key's parts; the longest key a
    # document within the limit can hold is the worst case found (V-41): about 65 MiB.
    text = ".".join(["a"] * ((MAXIMUM_DOCUMENT_SIZE - 2) // 2)) + "=1"
    assert len(text) <= MAXIMUM_DOCUMENT_SIZE
    tracemalloc.start()
    try:
        with pytest.raises(ConfigurationError) as error:
            read_toml(Limit, text, "limit.toml")
        peak = tracemalloc.get_traced_memory()[1]
    finally:
        tracemalloc.stop()
    assert error.value.lines == ("limit.toml: nested too deeply to read",)
    assert peak < 80 * 2**20


@pytest.mark.parametrize(
    ("text", "refusal"),
    [
        # The reader refuses an integer too long to convert with an error of another class.
        ("count = 1" + "0" * 5000 + "\n", "limit.toml: not valid TOML"),
        (
            "x = " + "[" * 2000 + "]" * 2000 + "\n",
            "limit.toml: nested too deeply to read",
        ),
        (
            "x = " + "{a = " * 600 + "1" + "}" * 600 + "\n",
            "limit.toml: nested too deeply to read",
        ),
        # The reader converts these bases without the limit; the JSON form then cannot.
        ("count = 0x" + "f" * 4000 + "\n", "limit.toml: not valid TOML"),
        ("count = 0o" + "7" * 5000 + "\n", "limit.toml: not valid TOML"),
        # A binary integer the JSON form cannot convert is longer than any document read.
        ("count = 0b" + "1" * 15000 + "\n", TOO_LONG),
        ("sides = [0x" + "f" * 4000 + "]\n", "limit.toml: not valid TOML"),
        # Tables nested by their headers, which the reader takes without recursion.
        (
            "[" + ".".join(["a"] * 4000) + "]\n",
            "limit.toml: nested too deeply to read",
        ),
    ],
    ids=[
        "integer too long",
        "arrays too deep",
        "inline tables too deep",
        "hexadecimal integer too long",
        "octal integer too long",
        "binary integer too long",
        "integer too long in an array",
        "tables too deep",
    ],
)
def test_a_document_the_reader_cannot_take_is_refused(text: str, refusal: str) -> None:
    with pytest.raises(ConfigurationError) as error:
        read_toml(Limit, text, "limit.toml")
    assert error.value.lines == (refusal,)


# Documents the property below tries: the settings of `Book` and `Limit`, each with values of
# its own, a setting `x`, and perhaps `y` in a limit, whose value fails one step of the reading
# (the length, the reader, the amount constructor, the JSON form, the conversion to JSON, or
# validation), or none; the last line may be another table, a header nested too deeply, or not
# TOML.
_SIDES = ['["buy"]', '["buy", "sell"]', '["hold"]', "[]", '"buy"']
_ENABLED = ["true", "false", '"yes"']
_SIZES = ['"1.5"', '"-0"', '"x"', "1", "{}"]
_COUNTS = ["0", "-0", "0x1f", "0o7", "0b1", '"1"']
_OTHER = [
    "",
    "1.5",
    "1e3",
    "inf",
    "nan",
    "1979-05-27",
    "07:32:00",
    "1979-05-27T07:32:00Z",
    "0x" + "f" * 4000,
    "0o" + "7" * 5000,
    # Longer than any document read, as a binary integer the conversion cannot take must be.
    "0b" + "1" * 15000,
    "1" + "0" * 5000,
    "[" * 3000 + "]" * 3000,
    "{a = " * 1000 + "1" + "}" * 1000,
    '"\\u00e9"',
    "'lit'",
    "[]",
]
# A header 3,000 deep, within the length of a document: deeper than the JSON form's recursion
# goes, also while Hypothesis raises the recursion limit for a test (to about 2,000).
_LAST_LINES = ["", "[t]", "[" + ".".join(["a"] * 3000) + "]", "=", 'x = "']


def _toml_document(top: dict[str, str], limits: list[dict[str, str]], last: str) -> str:
    lines = [f"{key} = {value}" for key, value in top.items() if value]
    for table in limits:
        lines.append("[[limits]]")
        lines.extend(f"{key} = {value}" for key, value in table.items() if value)
    lines.append(last)
    return "\n".join(lines) + "\n"


_TOML_DOCUMENTS = st.builds(
    _toml_document,
    st.fixed_dictionaries(
        {"x": st.sampled_from(_OTHER)},
        optional={
            "sides": st.sampled_from(_SIDES),
            "enabled": st.sampled_from(_ENABLED),
        },
    ),
    st.lists(
        st.fixed_dictionaries(
            {},
            optional={
                "size": st.sampled_from(_SIZES),
                "count": st.sampled_from(_COUNTS),
                "y": st.sampled_from(_OTHER),
            },
        ),
        max_size=2,
    ),
    st.sampled_from(_LAST_LINES),
)


def _step(refusal: str) -> str:
    """The step a refusal's first line names, for the property's statistics."""
    for text, step in (
        ("longer than", "the length"),
        ("not valid TOML (", "the reader: not valid TOML"),
        ("a number is refused", "the amount constructor"),
        ("is not a setting value", "the JSON form"),
        ("nested too deeply to read", "any step: nested too deeply"),
        ("not valid TOML", "the reader or the conversion: an integer too long"),
        ("input refused by contract", "validation"),
    ):
        if text in refusal:
            return step
    return "other"


@given(_TOML_DOCUMENTS | st.text(max_size=60))
def test_any_text_is_read_or_refused(text: str) -> None:
    # The reader's boundary: whatever the document, a contract or `ConfigurationError`.
    try:
        read_toml(Book, text, "book.toml")
    except ConfigurationError as error:
        # A refusal names its file on its first line; a contract's details follow.
        assert error.lines[0].startswith("book.toml: ")
        event(_step(error.lines[0]))
    else:
        event("read")


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


def test_a_file_whose_status_cannot_be_read_is_refused(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    directory = _directory(
        tmp_path, 'platform_id = "atp"\n', {"paper": _specific("paper")}
    )
    portable = directory / "platform.toml"
    stat = Path.stat

    def refuse(path: Path, *, follow_symlinks: bool = True) -> os.stat_result:
        if path == portable:
            raise PermissionError(13, "Permission denied", str(path))
        return stat(path, follow_symlinks=follow_symlinks)

    monkeypatch.setattr(Path, "stat", refuse)
    assert _refusal(directory, "paper", {}) == [
        "platform.toml: cannot be read (Permission denied)"
    ]


def test_a_configuration_directory_whose_name_is_too_long_is_refused(
    tmp_path: Path,
) -> None:
    assert _refusal(tmp_path / ("d" * 300), "paper", {}) == [
        "platform.toml: cannot be read (File name too long)"
    ]


class _FailingFile:
    """An open file whose reading fails."""

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *details: object) -> None:
        return None

    def read(self, size: int = -1) -> bytes:
        raise OSError(5, "Input/output error")


@pytest.mark.parametrize(
    ("failing", "reason"),
    [("opening", "Permission denied"), ("reading", "Input/output error")],
)
def test_a_file_that_cannot_be_read_is_refused(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, failing: str, reason: str
) -> None:
    directory = _directory(
        tmp_path, 'platform_id = "atp"\n', {"paper": _specific("paper")}
    )
    portable = directory / "platform.toml"

    def opened(path: Path, mode: str = "r") -> _FailingFile:
        assert (path, mode) == (portable, "rb")
        if failing == "opening":
            raise PermissionError(13, "Permission denied", str(path))
        return _FailingFile()

    monkeypatch.setattr(Path, "open", opened)
    assert _refusal(directory, "paper", {}) == [
        f"platform.toml: cannot be read ({reason})"
    ]


def _too_large(relative: str) -> list[str]:
    return [
        (
            f"{relative}: larger than {MAXIMUM_DOCUMENT_SIZE} bytes, the most a "
            "configuration file may hold"
        )
    ]


@pytest.mark.parametrize("relative", ["platform.toml", "environments/paper.toml"])
def test_a_file_at_the_limit_loads_and_a_larger_one_is_refused(
    tmp_path: Path, relative: str
) -> None:
    directory = _directory(
        tmp_path, 'platform_id = "atp"\n', {"paper": _specific("paper")}
    )
    path = directory / relative
    content = path.read_bytes() + b"#"
    end = "\u00e9".encode()  # one character of two bytes
    at_limit = content + b"x" * (MAXIMUM_DOCUMENT_SIZE - len(content) - len(end)) + end
    assert len(at_limit) == MAXIMUM_DOCUMENT_SIZE
    path.write_bytes(at_limit)
    configuration = load_configuration(directory, "paper", ProcessEnvironment({}))
    assert configuration.portable.platform_id == "atp"
    # Larger by one character of two bytes, which a read of one byte more than the limit cuts:
    # refused for its size, before it is decoded, and not as text that is not UTF-8.
    path.write_bytes(at_limit[: -len(end)] + b"xx" + end)
    assert _refusal(directory, "paper", {}) == _too_large(relative)


def test_a_file_larger_than_the_limit_is_refused_before_anything_else(
    tmp_path: Path,
) -> None:
    # Not TOML, and holding a declared secret's value: neither is looked at, and the refusal
    # holds nothing from the file.
    directory = _directory(
        tmp_path,
        f"platform_id = \n# {SECRET}\n" + "x" * MAXIMUM_DOCUMENT_SIZE,
        {"paper": _specific("paper", SERVER_DECLARATION)},
    )
    lines = _refusal(directory, "paper", {"ATP_DB": SECRET})
    assert lines == _too_large("platform.toml")
    assert SECRET not in "\n".join(lines)


def test_a_file_larger_than_the_limit_is_not_read_in_full(tmp_path: Path) -> None:
    # A sparse file of 64 MiB, which takes no space on disk: read in full, it would take 64 MiB
    # of memory.
    directory = _directory(tmp_path, "", {"paper": _specific("paper")})
    with (directory / "platform.toml").open("wb") as file:
        file.truncate(64 * 2**20)
    tracemalloc.start()
    try:
        lines = _refusal(directory, "paper", {})
        peak = tracemalloc.get_traced_memory()[1]
    finally:
        tracemalloc.stop()
    assert lines == _too_large("platform.toml")
    assert peak < 2**20


def test_a_refused_load_leaves_nothing_behind(tmp_path: Path) -> None:
    # Loading keeps no state: after refusals, a valid directory loads as it does the first time.
    directory = _directory(
        tmp_path,
        'platform_id = "atp"\n',
        {"paper": _specific("paper", SERVER_DECLARATION)},
    )
    variables = {"ATP_DB": SECRET}
    source = ProcessEnvironment(variables)
    expected = summary(load_configuration(directory, "paper", source))
    portable = directory / "platform.toml"
    valid = portable.read_bytes()
    for broken in (valid + b"#" * MAXIMUM_DOCUMENT_SIZE, b"platform_id = ", b"\xff"):
        portable.write_bytes(broken)
        _refusal(directory, "paper", variables)
    portable.write_bytes(valid)
    assert summary(load_configuration(directory, "paper", source)) == expected


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
        # The same, written with a TOML escape: found as read.
        (
            'platform_id = "atp\\u002dshared"\n',
            SERVER_DECLARATION,
            "atp-shared",
            "platform.toml",
        ),
        # As read, in a nested setting: another declaration's name, written with an escape.
        (
            'platform_id = "atp"\n',
            SERVER_DECLARATION + '[[secrets]]\nname = "ATP\\u005fOTHER"\nkind = "ai"\n',
            "ATP_OTHER",
            "environments/paper.toml",
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
