"""Validation errors rendered without input (TEC-004, SEC-005; docs/architecture/contracts.md).

A Pydantic validation error carries the refused input in its structured forms and, for an
unknown field, the field's name in its location; some messages quote input too. Errors are
therefore rendered and logged only through `validation_error_details`, which leaves the input
out, redacts every part of a location that is not a name the contracts themselves declare, and
keeps a message only for error types whose messages never quote input, and only if the message
is that type's own: Pydantic's, or the kernel's fixed text. A validator that raised one of those
types with a message of its own gets the generic message.
"""

from __future__ import annotations

import json
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any, Final, Literal

from pydantic import ValidationError
from pydantic_core import InitErrorDetails

REDACTED: Final = "<redacted>"
"""Shown in place of a location part that came from the input."""

GENERIC_MESSAGE: Final = "invalid value"
"""Shown in place of a message that could quote the input."""

# Error types whose messages are fixed text or name only schema facts (expected types,
# patterns, limits, allowed values). A type not listed gets the generic message: among them
# `value_error`, whose message is whatever a validator wrote, which could quote the input.
_SAFE_MESSAGE_TYPES: Final = frozenset(
    {
        "amount_invalid",
        "amount_type",
        "bool_type",
        "contract_value_type",
        "dataclass_type",
        "decimal_type",
        "dict_type",
        "enum",
        "extra_forbidden",
        "frozen_field",
        "frozen_instance",
        "idempotency_key_invalid",
        "idempotency_key_type",
        "int_type",
        "is_instance_of",
        "json_invalid",
        "json_type",
        "literal_error",
        "missing",
        "model_attributes_type",
        "model_type",
        "none_required",
        "string_pattern_mismatch",
        "string_too_long",
        "string_too_short",
        "string_type",
        "tuple_type",
        "union_tag_not_found",
    }
)

# Error types whose last location part is a key from the input.
_INPUT_KEY_TYPES: Final = frozenset({"extra_forbidden", "invalid_key"})

# Pydantic words some messages differently for JSON input ("a valid array", not "a valid tuple").
_INPUT_TYPES: Final[tuple[Literal["python", "json"], ...]] = ("python", "json")

_known_names: set[str] = set()

# The kernel's own (error type, message) pairs, registered by the modules that raise them.
_kernel_messages: set[tuple[str, str]] = set()


def register_kernel_messages(kind: str, messages: Iterable[str]) -> None:
    """Record the fixed messages the kernel raises with one of its own error types."""
    _kernel_messages.update((kind, message) for message in messages)


def register_known_names(names: Iterable[str]) -> None:
    """Record names a contract declares (fields, aliases, tags); only they appear in locations."""
    _known_names.update(names)


@dataclass(frozen=True, slots=True)
class ErrorDetail:
    """One refusal, with no input in it."""

    location: tuple[str | int, ...]
    type: str
    message: str

    def as_dict(self) -> dict[str, object]:
        return {
            "location": list(self.location),
            "type": self.type,
            "message": self.message,
        }


def validation_error_details(error: ValidationError) -> tuple[ErrorDetail, ...]:
    """The one way to render a validation error: no input, no input-derived names or messages."""
    details: list[ErrorDetail] = []
    # The context is read only to recognize Pydantic's own messages; it is never shown.
    for item in error.errors(
        include_url=False, include_context=True, include_input=False
    ):
        kind = item["type"]
        parts = list(item["loc"])
        if kind in _INPUT_KEY_TYPES and parts:
            # The last part is a key taken from the input: an unknown field's name, or a
            # mapping key that is not a string (which a position check would let through).
            parts[-1] = REDACTED
        location = tuple(
            part if isinstance(part, int) or part in _known_names else REDACTED
            for part in parts
        )
        message = item["msg"]
        if not _is_own_message(kind, message, item.get("ctx")):
            message = GENERIC_MESSAGE
        details.append(ErrorDetail(location, kind, message))
    return tuple(details)


def _is_own_message(kind: str, message: str, context: dict[str, Any] | None) -> bool:
    """Whether a message may be kept: its type is listed, and the message is the type's own,
    the kernel's fixed text or the one Pydantic gives for that type and context. A validator
    that raised a listed type with a message of its own (which could quote the input) fails."""
    if kind not in _SAFE_MESSAGE_TYPES:
        return False
    if (kind, message) in _kernel_messages:
        return True
    line: InitErrorDetails = {"type": kind, "loc": (), "input": None}
    if context is not None:
        line["ctx"] = context
    for input_type in _INPUT_TYPES:
        try:
            rendered = ValidationError.from_exception_data(
                "refusal", [line], input_type=input_type
            )
        except (KeyError, TypeError, ValueError):
            return False  # not one of Pydantic's types, or a context it does not take
        if rendered.errors(include_url=False)[0]["msg"] == message:
            return True
    return False


class ContractError(ValueError):
    """Input refused by a contract. It holds only redacted details, never the input."""

    def __init__(self, contract_id: str, details: tuple[ErrorDetail, ...]) -> None:
        self.contract_id = contract_id
        self.details = details
        super().__init__(self._render())

    def __reduce__(
        self,
    ) -> tuple[type[ContractError], tuple[str, tuple[ErrorDetail, ...]]]:
        return (ContractError, (self.contract_id, self.details))

    def _render(self) -> str:
        lines = [f"input refused by contract {self.contract_id}:"]
        for detail in self.details:
            where = ".".join(str(part) for part in detail.location) or "(input)"
            lines.append(f"  {where}: {detail.message} [{detail.type}]")
        return "\n".join(lines)

    def to_json(self) -> str:
        """The refusal as JSON, for structured logs."""
        return json.dumps(
            {
                "contract": self.contract_id,
                "errors": [detail.as_dict() for detail in self.details],
            },
            sort_keys=True,
        )
