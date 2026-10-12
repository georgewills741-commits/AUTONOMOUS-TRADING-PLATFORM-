"""The idempotency key every financially significant request will carry (ARCH-041)."""

from __future__ import annotations

import re
import secrets
from typing import Any, ClassVar, Final, final

from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import PydanticCustomError, core_schema

from atp.contracts._errors import register_kernel_messages

_PATTERN: Final = "[0-9a-f]{32}"
_RE: Final = re.compile(_PATTERN, flags=re.ASCII)


@final
class IdempotencyKey:
    """A request's identity: retrying with the same key must not repeat the operation.

    32 lowercase hexadecimal characters (128 bits). `new()` draws one from the operating
    system's secure random source. Using the key to make an operation idempotent is the
    operation's own contract, written in its stage (CORE TRADING FOUNDATION and later).
    """

    PATTERN: ClassVar[str] = f"^{_PATTERN}$"
    __slots__ = ("_text",)
    _text: str

    def __init__(self, text: str) -> None:
        if type(text) is not str or _RE.fullmatch(text) is None:
            msg = "an idempotency key is 32 lowercase hexadecimal characters"
            raise ValueError(msg)
        object.__setattr__(self, "_text", text)

    def __init_subclass__(cls, **kwargs: object) -> None:
        msg = "IdempotencyKey cannot be subclassed"
        raise TypeError(msg)

    def __reduce__(self) -> tuple[type[IdempotencyKey], tuple[str]]:
        return (IdempotencyKey, (self._text,))

    @classmethod
    def new(cls) -> IdempotencyKey:
        """A new random key."""
        return cls(secrets.token_hex(16))

    def __setattr__(self, name: str, value: object) -> None:
        msg = "an idempotency key is immutable"
        raise AttributeError(msg)

    def __delattr__(self, name: str) -> None:
        msg = "an idempotency key is immutable"
        raise AttributeError(msg)

    def __str__(self) -> str:
        return self._text

    def __repr__(self) -> str:
        return f"IdempotencyKey('{self._text}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, IdempotencyKey):
            return NotImplemented
        return str(other) == self._text

    def __hash__(self) -> int:
        return hash(self._text)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_plain_validator_function(
            _validate,
            serialization=core_schema.plain_serializer_function_ser_schema(
                str, return_schema=core_schema.str_schema(), when_used="json"
            ),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return {
            "type": "string",
            "pattern": cls.PATTERN,
            "description": "An idempotency key: 32 lowercase hexadecimal characters.",
        }


_KEY_TYPE: Final = "an idempotency key is given as a string"
_KEY_INVALID: Final = "an idempotency key is 32 lowercase hexadecimal characters"
register_kernel_messages("idempotency_key_type", [_KEY_TYPE])
register_kernel_messages("idempotency_key_invalid", [_KEY_INVALID])


def _validate(value: object) -> IdempotencyKey:
    # Each refusal has its own error type with fixed text, so it is reported without input.
    if isinstance(value, IdempotencyKey):
        return value
    if type(value) is not str:
        raise PydanticCustomError("idempotency_key_type", _KEY_TYPE)
    try:
        return IdempotencyKey(value)
    except ValueError:
        raise PydanticCustomError("idempotency_key_invalid", _KEY_INVALID) from None
