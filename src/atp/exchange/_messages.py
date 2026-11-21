"""A venue's message: its size limit and its exact decoding (the Stage 2 plan's U4 and D5).

Every message is checked against a size limit before anything reads it. A JSON message is
decoded so that each number keeps the text the venue wrote, as a `JsonNumber`: an amount is
built only from a venue's text (D5; the numerical policy, N1), and a decoder that turned numbers
into floats would lose it. A message that is too large or cannot be decoded is reported with
its cause as untranslatable input for SYS-02 (EXA-013), never dropped silently.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass

from atp.marketdata import Lineage, Stream, UntranslatableCause, UntranslatableInput


class JsonNumber(str):
    """A JSON number's text, exactly as the venue wrote it."""

    __slots__ = ()


type JsonValue = None | bool | str | list[JsonValue] | dict[str, JsonValue]
"""A decoded JSON value; each number is a `JsonNumber`, which is a `str`."""


@dataclass(frozen=True, slots=True)
class Decoded:
    """A message decoded."""

    value: JsonValue


def _refuse_constant(name: str) -> None:
    # NaN, Infinity, and -Infinity are not JSON, though Python's decoder accepts them.
    msg = f"not a JSON number: {name}"
    raise ValueError(msg)


def _object(pairs: list[tuple[str, JsonValue]]) -> dict[str, JsonValue]:
    # A name given twice would leave the value to the decoder's choice of the last one.
    value = dict(pairs)
    if len(value) != len(pairs):
        msg = "a name is given twice in one object"
        raise ValueError(msg)
    return value


def decode_json(content: bytes, *, max_bytes: int) -> Decoded | UntranslatableCause:
    """Decode a message of at most `max_bytes` bytes of UTF-8 JSON, each number kept as its
    text; OVERSIZED when it is larger, before any of it is read, and MALFORMED when it is not
    such JSON, a name given twice in one object or nesting too deep for the decoder included."""
    if type(max_bytes) is not int or max_bytes <= 0:
        msg = "a message's size limit is a whole number of bytes above zero"
        raise ValueError(msg)
    if type(content) is not bytes:
        msg = "a message is bytes"
        raise TypeError(msg)
    if len(content) > max_bytes:
        return UntranslatableCause.OVERSIZED
    try:
        value: JsonValue = json.loads(
            content.decode("utf-8"),
            parse_float=JsonNumber,
            parse_int=JsonNumber,
            parse_constant=_refuse_constant,
            object_pairs_hook=_object,
        )
    except (UnicodeDecodeError, ValueError, RecursionError):
        return UntranslatableCause.MALFORMED
    return Decoded(value)


def untranslatable(
    *,
    venue: str,
    stream: Stream,
    lineage: Lineage,
    receive_time_ns: int,
    cause: UntranslatableCause,
    content: bytes,
) -> UntranslatableInput:
    """The record of a venue's input that could not be translated, for SYS-02 (EXA-013): the
    content's SHA-256 digest and length, never the content itself."""
    return UntranslatableInput(
        venue=venue,
        stream=stream,
        lineage=lineage,
        receive_time_ns=receive_time_ns,
        cause=cause,
        content_sha256=hashlib.sha256(content).hexdigest(),
        content_length=len(content),
    )
