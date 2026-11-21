"""The Slippage Engine: a taker order walked through a book snapshot, exact (QNT-006, QNT-007;
the Stage 2 plan's U7)."""

from __future__ import annotations

from decimal import Decimal
from typing import Final

from atp.marketdata import BookSnapshot, TakerSide, Validated, item_time_ns
from atp.numeric import Rounding, amount, divide
from atp.quant._common import (
    CalculationRefused,
    RefusalCause,
    calculation_id,
    check_amount,
    require_eligible,
    unsigned,
)
from atp.quant._contracts import SlippageEstimate

SLIPPAGE_CALCULATION: Final = "atp.quant.slippage"
SLIPPAGE_VERSION: Final = "1.0"
"""The version of `walk_book`'s definition; a change to it is a new version."""


def walk_book(
    data: Validated[BookSnapshot],
    side: TakerSide,
    quantity: Decimal,
    increment: Decimal,
    limit_price: Decimal | None = None,
) -> SlippageEstimate:
    """Walk a taker order of `quantity`, in the base asset, through a book snapshot.

    A buy takes the asks and a sell the bids, best first, each level up to its quantity, until
    the order is filled, the side ends, or the next level is worse than `limit_price` where one
    is given (above it for a buy, below it for a sell). Every sum and product is exact; the
    average price, the value filled divided by the quantity filled, is rounded against the
    taker to a multiple of `increment` (`atp.numeric.divide`: up for a buy, down for a sell), so
    it is never better than the exact one, which is never better than the best price. Slippage
    against the best price and impact against the mid are exact. A side without levels is
    refused (MISSING_INPUT), as is a snapshot that was not VALID when assessed; an order that
    fills nothing has no average or worst price.
    """
    book = require_eligible(data, "book snapshot")
    if type(book) is not BookSnapshot:
        msg = "a size is walked through a book snapshot"
        raise TypeError(msg)
    if type(side) is not TakerSide:
        msg = "the side is a TakerSide"
        raise TypeError(msg)
    check_amount(quantity, "quantity")
    check_amount(increment, "increment")
    if quantity <= 0:
        msg = "the quantity is above zero"
        raise ValueError(msg)
    if limit_price is not None:
        check_amount(limit_price, "limit price")
        if limit_price <= 0:
            msg = "the limit price is above zero"
            raise ValueError(msg)
    buy = side is TakerSide.BUY
    levels = book.asks if buy else book.bids
    if not levels:
        raise CalculationRefused(
            RefusalCause.MISSING_INPUT,
            f"the book has no {'asks' if buy else 'bids'} to walk",
        )
    best = levels[0].price
    remaining = quantity
    filled = notional = amount(0)
    reached = 0
    worst: Decimal | None = None
    for level in levels:
        if remaining <= 0:
            break
        if limit_price is not None and (
            level.price > limit_price if buy else level.price < limit_price
        ):
            break
        taken = min(level.quantity, remaining)
        filled += taken
        notional += taken * level.price
        remaining -= taken
        reached += 1
        worst = level.price
    average = (
        None
        if filled <= 0
        else divide(
            notional,
            filled,
            increment,
            Rounding.TOWARD_POSITIVE_INFINITY
            if buy
            else Rounding.TOWARD_NEGATIVE_INFINITY,
        )
    )
    mid = (
        (book.bids[0].price + book.asks[0].price) / 2
        if book.bids and book.asks
        else None
    )
    sign = 1 if buy else -1
    inputs = (book.evidence_id,)
    parameters = [
        ("side", side.value),
        ("quantity", str(quantity)),
        ("increment", str(increment)),
        ("limit_price", "none" if limit_price is None else str(limit_price)),
    ]
    return SlippageEstimate(
        market=book.market,
        side=side,
        quantity=quantity,
        limit_price=limit_price,
        filled=filled,
        complete=remaining <= 0,
        levels=reached,
        best=best,
        worst=worst,
        notional=notional,
        average_price=average,
        increment=increment,
        slippage=unsigned(sign * (notional - filled * best)),
        mid=mid,
        impact=None if mid is None else unsigned(sign * (notional - filled * mid)),
        time_ns=item_time_ns(book),
        inputs=inputs,
        calculation_version=SLIPPAGE_VERSION,
        evidence_id=calculation_id(
            SLIPPAGE_CALCULATION, SLIPPAGE_VERSION, parameters, inputs
        ),
    )
