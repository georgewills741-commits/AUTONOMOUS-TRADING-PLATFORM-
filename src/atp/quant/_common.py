"""What the engine's calculations share: their refusals, the check of the market data they are
given, and the evidence identifier of a result (MKD-005, MKD-010, MKD-012)."""

from __future__ import annotations

import enum
import hashlib
import json
import re
from collections.abc import Sequence
from decimal import Decimal
from typing import Final

from atp.marketdata import (
    EVIDENCE_ID_PATTERN,
    Freshness,
    MarketItem,
    Validated,
    ValidationLimits,
    assess,
)

CALCULATION_FORM: Final = "atp.calculation/1"
"""The name and version of the form a result's evidence identifier digests; a change to the form
is a new version."""


class RefusalCause(enum.Enum):
    """Why a calculation has no result for the data it was given."""

    INELIGIBLE_INPUT = "ineligible-input"
    """Market data that was not VALID when validated, or is not VALID at the time of use, or
    a time of use before the data was validated (MKD-012)."""
    MISSING_INPUT = "missing-input"
    """A price, a side of a book, or a fee schedule the calculation needs is absent."""
    INSUFFICIENT_DATA = "insufficient-data"
    """Fewer bars than the calculation's periods need."""
    GAP = "gap"
    """Bars missing between two that were given."""
    UNDEFINED = "undefined"
    """The calculation's definition gives no value for this data, as for the RSI of prices that
    never moved, or a value a float cannot hold."""


class CalculationRefused(Exception):
    """A calculation that has no result for the data it was given. Its consumer treats the result
    as unknown, never as zero (master execution constitution §168)."""

    def __init__(self, cause: RefusalCause, detail: str) -> None:
        super().__init__(f"{cause.value}: {detail}")
        self.cause = cause


def require_validated[ItemT: MarketItem](
    data: Validated[ItemT], what: str, now_ns: int
) -> ItemT:
    """The item of `data`, which must be validated market data that was VALID when it was
    validated (MKD-012), and validated no later than `now_ns`, the time of use: before its
    validation nothing shows the item VALID, and its age at a time before it would read as zero
    (`atp.marketdata.age_ns`). This is the check of history, such as a series' earlier bars,
    older than a freshness limit by nature; `require_current` checks data used as current.
    Anything that is not `Validated`, and a time that is not a whole number of nanoseconds,
    raise `TypeError`; data not VALID when validated, or validated after the time of use, is
    refused."""
    given: object = data  # typed code cannot pass anything else; other code can
    if type(given) is not Validated:
        msg = f"the {what} reaches a calculation only as atp.marketdata's Validated"
        raise TypeError(msg)
    if type(now_ns) is not int:
        msg = "the time of use is a whole number of nanoseconds"
        raise TypeError(msg)
    if not data.eligible:
        raise CalculationRefused(
            RefusalCause.INELIGIBLE_INPUT, f"the {what} was not VALID when validated"
        )
    if now_ns < data.assessment.assessed_time_ns:
        raise CalculationRefused(
            RefusalCause.INELIGIBLE_INPUT,
            f"the time of use is before the {what} was validated",
        )
    return data.item


def require_current[ItemT: MarketItem](
    data: Validated[ItemT], what: str, now_ns: int, limits: ValidationLimits
) -> ItemT:
    """The item of `data`, which must pass `require_validated` and be VALID again at `now_ns`,
    the time of use, under `limits` (MKD-012): `eligible` keeps the assessment made when the
    item was validated, so the item is assessed again here (`atp.marketdata.assess`). Limits
    that are not `ValidationLimits` raise `TypeError`; data not VALID at the time of use is
    refused."""
    if type(limits) is not ValidationLimits:
        msg = "the freshness limits are atp.marketdata's ValidationLimits"
        raise TypeError(msg)
    item = require_validated(data, what, now_ns)
    if assess(item, now_ns, limits).freshness is not Freshness.VALID:
        raise CalculationRefused(
            RefusalCause.INELIGIBLE_INPUT, f"the {what} is not VALID at the time of use"
        )
    return item


def check_amount(value: Decimal, what: str) -> None:
    """Refuse a parameter that is not a finite amount."""
    if type(value) is not Decimal:
        msg = f"the {what} is an amount built with atp.numeric.amount"
        raise TypeError(msg)
    if not value.is_finite():
        msg = f"the {what} is finite"
        raise ValueError(msg)


def unsigned(value: Decimal) -> Decimal:
    """`value`, with a zero's sign removed, so that a result never reads -0."""
    return value.copy_abs() if value.is_zero() else value


def calculation_id(
    calculation: str,
    version: str,
    parameters: Sequence[tuple[str, str]],
    inputs: Sequence[str],
) -> str:
    """A result's evidence identifier: a SHA-256 digest, in lowercase hexadecimal.

    It digests the form's name, the calculation's name and version, its parameters, each as a
    name and its text, and its inputs' evidence identifiers, in their order. The same calculation
    of the same inputs with the same parameters gets the same identifier, on any platform: the
    results, which in floats can differ between platforms, are not digested. An input that is
    not an evidence identifier raises `ValueError`.
    """
    for identifier in inputs:
        if type(identifier) is not str or not re.fullmatch(
            EVIDENCE_ID_PATTERN, identifier
        ):
            msg = "an input is named by its evidence identifier"
            raise ValueError(msg)
    form = json.dumps(
        [
            CALCULATION_FORM,
            calculation,
            version,
            [[name, text] for name, text in parameters],
            list(inputs),
        ],
        ensure_ascii=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(form.encode("ascii")).hexdigest()
