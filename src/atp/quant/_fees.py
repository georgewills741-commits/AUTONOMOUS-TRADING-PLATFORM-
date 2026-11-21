"""The Fee Engine: fees at a venue's published schedule, and funding payments, exact (QNT-005,
QNT-007; the Stage 2 plan's U7 and D8)."""

from __future__ import annotations

from collections.abc import Sequence
from decimal import Decimal
from typing import Final

from atp.config import VenueSettings
from atp.marketdata import (
    FundingRate,
    MarketRef,
    Validated,
    ValidationLimits,
    item_time_ns,
)
from atp.quant._common import (
    CalculationRefused,
    RefusalCause,
    calculation_id,
    check_amount,
    require_current,
    unsigned,
)
from atp.quant._contracts import (
    FeeEstimate,
    FundingEstimate,
    LiquidityRole,
    PositionSide,
)

FEE_CALCULATION: Final = "atp.quant.fee"
FEE_VERSION: Final = "1.0"
"""The version of `estimate_fee`'s definition; a change to it is a new version."""
FUNDING_CALCULATION: Final = "atp.quant.funding"
FUNDING_VERSION: Final = "1.0"
"""The version of `estimate_funding`'s definition; a change to it is a new version."""


def _check_notional(notional: Decimal) -> None:
    check_amount(notional, "notional")
    if notional < 0:
        msg = "the notional is zero or above"
        raise ValueError(msg)


def estimate_fee(
    venue: VenueSettings,
    market: MarketRef,
    role: LiquidityRole,
    notional: Decimal,
    inputs: Sequence[str] = (),
) -> FeeEstimate:
    """The fee for an order of `notional`, in the quote asset, in `market`, as `role`.

    The rate is the maker or taker rate of the venue's published schedule for the market's
    instrument type, at its base tier, as the venue's configuration holds it with its source and
    date (the Stage 2 plan's D8; the account's own tier and rates come with CORE TRADING
    FOUNDATION); the fee is the notional times the rate, exactly, so it grows with the notional
    at a rate of zero or above. A market of another venue raises `ValueError`. A venue with no
    schedule for the market's type is refused (MISSING_INPUT): an unknown fee is never taken as
    zero. `inputs` names, by their evidence identifiers, the results the notional came from.
    """
    if type(venue) is not VenueSettings or type(market) is not MarketRef:
        msg = "a fee is estimated from a venue's settings and one of its markets"
        raise TypeError(msg)
    if market.venue != venue.venue:
        msg = "the market is not of the venue whose settings were given"
        raise ValueError(msg)
    if type(role) is not LiquidityRole:
        msg = "the role is a LiquidityRole"
        raise TypeError(msg)
    _check_notional(notional)
    named = tuple(inputs)
    schedule = next(
        (fees for fees in venue.fees if fees.instrument_type is market.instrument_type),
        None,
    )
    if schedule is None:
        raise CalculationRefused(
            RefusalCause.MISSING_INPUT,
            f"no fee schedule is configured for {venue.venue}'s "
            f"{market.instrument_type.value} markets",
        )
    rate = schedule.maker if role is LiquidityRole.MAKER else schedule.taker
    parameters = [
        ("venue", market.venue),
        ("market", market.symbol()),
        ("instrument_type", market.instrument_type.value),
        ("role", role.value),
        ("tier", "base"),
        ("rate", str(rate)),
        ("source", schedule.source),
        ("as_of", schedule.as_of),
        ("notional", str(notional)),
    ]
    return FeeEstimate(
        market=market,
        role=role,
        tier="base",
        schedule=schedule,
        notional=notional,
        rate=rate,
        fee=unsigned(notional * rate),
        inputs=named,
        calculation_version=FEE_VERSION,
        evidence_id=calculation_id(FEE_CALCULATION, FEE_VERSION, parameters, named),
    )


def estimate_funding(
    data: Validated[FundingRate],
    side: PositionSide,
    notional: Decimal,
    *,
    now_ns: int,
    limits: ValidationLimits,
) -> FundingEstimate:
    """The funding payment of a perpetual position of `notional`, in the quote asset, for one
    funding interval at a published funding rate.

    The payment is the notional times the rate, exactly. When the rate is above zero a long
    position pays it and a short one receives it, and the reverse when it is below, as perpetual
    funding works; `cost` is what the position pays, below zero when it receives. A rate not
    VALID when validated or at `now_ns`, the time of use, under `limits` is refused.
    """
    item = require_current(data, "funding rate", now_ns, limits)
    if type(item) is not FundingRate:
        msg = "funding is estimated from a funding rate"
        raise TypeError(msg)
    if type(side) is not PositionSide:
        msg = "the side is a PositionSide"
        raise TypeError(msg)
    _check_notional(notional)
    payment = notional * item.rate
    inputs = (item.evidence_id,)
    parameters = [("side", side.value), ("notional", str(notional))]
    return FundingEstimate(
        market=item.market,
        side=side,
        notional=notional,
        rate=item.rate,
        cost=unsigned(payment if side is PositionSide.LONG else -payment),
        funding_time_ns=item.funding_time_ns,
        interval_seconds=item.interval_seconds,
        time_ns=item_time_ns(item),
        inputs=inputs,
        calculation_version=FUNDING_VERSION,
        evidence_id=calculation_id(
            FUNDING_CALCULATION, FUNDING_VERSION, parameters, inputs
        ),
    )
