"""Amounts in contracts: strings in JSON, `Decimal` in Python (ARCH-010, TEC-003; the numerical policy)."""

from __future__ import annotations

from decimal import Decimal
from typing import Annotated, Any, Final

from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import PydanticCustomError, core_schema

from atp.contracts._errors import register_kernel_messages
from atp.numeric import AMOUNT_PATTERN, AMOUNT_REFUSALS, AmountError, amount

_AMOUNT_TYPE: Final = (
    "an amount is given as a decimal string (or as a Decimal from Python code)"
)
register_kernel_messages("amount_type", [_AMOUNT_TYPE])
register_kernel_messages("amount_invalid", AMOUNT_REFUSALS)


def _validate(value: object) -> Decimal:
    # Each refusal has its own error type; the constructor's messages never contain the value.
    if type(value) is not str and type(value) is not Decimal:
        raise PydanticCustomError("amount_type", _AMOUNT_TYPE)
    try:
        return amount(value)
    except AmountError as error:
        raise PydanticCustomError("amount_invalid", str(error)) from None


class AmountSchema:
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        # The amount is built first, then handed to Pydantic's decimal schema. `Amount` is a type
        # alias, so Pydantic applies a field's bounds (gt, le, multiple_of, max_digits,
        # decimal_places) with its own validators around this schema, in either spelling; a
        # field's `strict=True` goes into the decimal schema, the one place it can apply.
        return core_schema.no_info_before_validator_function(
            _validate,
            handler(source),
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
            "pattern": AMOUNT_PATTERN,
            "description": (
                "A decimal amount written as a string. A JSON number is refused. At most 34 "
                "significant digits; no NaN or infinity."
            ),
        }


# A `type` statement, not an assignment: an alias made by assignment could be called, and
# `Amount("NaN")` would build a `Decimal` outside `atp.numeric` without the amount's checks.
type Amount = Annotated[Decimal, AmountSchema]
"""A contract field holding an amount, built with `atp.numeric.amount`."""
