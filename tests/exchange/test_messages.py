"""A venue's message: the size limit, exact decoding, and untranslatable input (EXA-013; the
Stage 2 plan's U4 and D5)."""

from __future__ import annotations

import hashlib

import pytest
from pydantic import ValidationError

from atp.exchange import Decoded, JsonNumber, decode_json, untranslatable
from atp.marketdata import Lineage, Stream, UntranslatableCause

LINEAGE = Lineage(
    source="venue answer", adapter="atp.exchange.sample", adapter_version="1.0"
)


def decoded(content: bytes, max_bytes: int = 1024) -> object:
    result = decode_json(content, max_bytes=max_bytes)
    assert isinstance(result, Decoded), result
    return result.value


@pytest.mark.req("EXA-013")
def test_each_number_keeps_the_venue_s_text() -> None:
    value = decoded(b'{"price": 0.1000, "size": 3, "e": 1.5e-7, "n": -0, "s": "2.50"}')
    assert value == {
        "price": "0.1000",
        "size": "3",
        "e": "1.5e-7",
        "n": "-0",
        "s": "2.50",
    }
    assert isinstance(value, dict)
    for name in ("price", "size", "e", "n"):
        assert type(value[name]) is JsonNumber
    assert type(value["s"]) is str


@pytest.mark.req("EXA-013")
def test_a_long_number_is_not_rounded() -> None:
    text = "12345678901234567890.123456789012345678901234567890"
    assert decoded(f"[{text}]".encode()) == [text]


@pytest.mark.req("EXA-013")
def test_a_message_over_the_limit_is_oversized_before_it_is_read() -> None:
    assert decode_json(b"[1]", max_bytes=3) == Decoded([JsonNumber("1")])
    assert decode_json(b"[12]", max_bytes=3) is UntranslatableCause.OVERSIZED
    # Not JSON at all: the size is checked first.
    assert decode_json(b"\xff" * 4, max_bytes=3) is UntranslatableCause.OVERSIZED


@pytest.mark.req("EXA-013")
@pytest.mark.parametrize(
    "content",
    [
        b"",
        b"{",
        b'{"a": 1} x',
        b"[NaN]",
        b"[Infinity]",
        b"[-Infinity]",
        b'{"a": 1, "a": 2}',
        b"\xff\xfe",
        b'"\xe2\x82"',
        "﻿[1]".encode(),
        b"[" * 100_000 + b"]" * 100_000,
    ],
    ids=[
        "empty",
        "unfinished",
        "trailing text",
        "nan",
        "infinity",
        "minus infinity",
        "a name twice",
        "not utf-8",
        "cut utf-8",
        "byte order mark",
        "nested too deep",
    ],
)
def test_what_is_not_json_is_malformed(content: bytes) -> None:
    assert decode_json(content, max_bytes=1_000_000) is UntranslatableCause.MALFORMED


def test_a_name_given_twice_in_different_objects_is_allowed() -> None:
    assert decoded(b'[{"a": 1}, {"a": 2}]') == [{"a": "1"}, {"a": "2"}]


@pytest.mark.parametrize("limit", [0, -1, True, 1.0, "10"])
def test_the_size_limit_is_a_whole_number_above_zero(limit: object) -> None:
    with pytest.raises(ValueError, match="size limit"):
        decode_json(b"[]", max_bytes=limit)  # type: ignore[arg-type]


@pytest.mark.parametrize("content", ["[]", bytearray(b"[]"), memoryview(b"[]")])
def test_a_message_is_bytes(content: object) -> None:
    with pytest.raises(TypeError, match="bytes"):
        decode_json(content, max_bytes=10)  # type: ignore[arg-type]


@pytest.mark.req("EXA-013")
def test_untranslatable_input_keeps_the_digest_and_length_not_the_content() -> None:
    content = b'{"price": "secret-looking text"}'
    record = untranslatable(
        venue="sample",
        stream=Stream.TICKER,
        lineage=LINEAGE,
        receive_time_ns=1_763_600_000_000_000_000,
        cause=UntranslatableCause.MISSING_FIELD,
        content=content,
    )
    assert record.content_sha256 == hashlib.sha256(content).hexdigest()
    assert record.content_length == len(content)
    assert record.cause is UntranslatableCause.MISSING_FIELD
    assert record.stream is Stream.TICKER
    assert "secret-looking" not in record.to_json()


def test_untranslatable_input_is_validated_as_its_contract() -> None:
    with pytest.raises(ValidationError):
        untranslatable(
            venue="Not A Venue",
            stream=Stream.TICKER,
            lineage=LINEAGE,
            receive_time_ns=0,
            cause=UntranslatableCause.MALFORMED,
            content=b"",
        )
