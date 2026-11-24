"""Spread and liquidity metrics, exact (QNT-002; the Stage 2 plan's U7)."""

from __future__ import annotations

from decimal import Decimal
from itertools import takewhile
from typing import Final

from atp.marketdata import (
    BookSnapshot,
    Ticker,
    Validated,
    ValidationLimits,
    item_time_ns,
)
from atp.numeric import Rounding, amount, divide
from atp.quant._common import (
    CalculationRefused,
    RefusalCause,
    calculation_id,
    check_amount,
    require_current,
)
from atp.quant._contracts import DepthMetrics, SpreadMetrics

SPREAD_CALCULATION: Final = "atp.quant.spread"
SPREAD_VERSION: Final = "1.0"
"""The version of `spread_metrics`'s definition; a change to it is a new version."""
DEPTH_CALCULATION: Final = "atp.quant.depth"
DEPTH_VERSION: Final = "1.0"
"""The version of `depth_metrics`'s definition; a change to it is a new version."""


def _best(item: Ticker | BookSnapshot) -> tuple[Decimal | None, Decimal | None]:
    if type(item) is Ticker:
        return item.bid, item.ask
    if type(item) is BookSnapshot:
        bid = item.bids[0].price if item.bids else None
        ask = item.asks[0].price if item.asks else None
        return bid, ask
    msg = "a spread is computed from a ticker or a book snapshot"
    raise TypeError(msg)


def spread_metrics(
    data: Validated[Ticker | BookSnapshot],
    increment: Decimal,
    *,
    now_ns: int,
    limits: ValidationLimits,
) -> SpreadMetrics:
    """The spread of a ticker's or a book snapshot's best bid and ask.

    The mid is (bid + ask) / 2 and the spread ask - bid, both exact; the relative spread is the
    spread divided by the mid, rounded up to a multiple of `increment`, above zero
    (`atp.numeric.divide`), so it is never understated. Data without a best bid or a best ask
    is refused (MISSING_INPUT), as is data not VALID when validated or at `now_ns`, the time of
    use, under `limits`.
    """
    item = require_current(data, "ticker or book snapshot", now_ns, limits)
    bid, ask = _best(item)
    check_amount(increment, "increment")
    if increment <= 0:
        msg = "the increment is above zero"
        raise ValueError(msg)
    if bid is None or ask is None:
        raise CalculationRefused(
            RefusalCause.MISSING_INPUT, "a spread needs a best bid and a best ask"
        )
    mid = (bid + ask) / 2
    spread = ask - bid
    relative = divide(spread, mid, increment, Rounding.TOWARD_POSITIVE_INFINITY)
    inputs = (item.evidence_id,)
    return SpreadMetrics(
        market=item.market,
        bid=bid,
        ask=ask,
        mid=mid,
        spread=spread,
        relative_spread=relative,
        increment=increment,
        time_ns=item_time_ns(item),
        inputs=inputs,
        calculation_version=SPREAD_VERSION,
        evidence_id=calculation_id(
            SPREAD_CALCULATION, SPREAD_VERSION, [("increment", str(increment))], inputs
        ),
    )


def depth_metrics(
    data: Validated[BookSnapshot],
    band: Decimal,
    *,
    now_ns: int,
    limits: ValidationLimits,
) -> DepthMetrics:
    """The depth a book snapshot shows within `band` of its mid, a fraction above zero and
    below one (0.01 is 1%).

    The bounds are mid × (1 - band) for the bids and mid × (1 + band) for the asks, exact. Each
    side counts its levels from the best while they are within its bound: their quantities, and
    the sum of each price times its quantity, both exact. A side is complete when a level beyond
    the bound follows. A snapshot without a bid or an ask is refused (MISSING_INPUT), as is one
    not VALID when validated or at `now_ns`, the time of use, under `limits`.
    """
    book = require_current(data, "book snapshot", now_ns, limits)
    if type(book) is not BookSnapshot:
        msg = "depth is computed from a book snapshot"
        raise TypeError(msg)
    check_amount(band, "band")
    if not 0 < band < 1:
        msg = "the band is a fraction of the mid, above zero and below one"
        raise ValueError(msg)
    if not book.bids or not book.asks:
        raise CalculationRefused(
            RefusalCause.MISSING_INPUT, "depth around the mid needs a bid and an ask"
        )
    mid = (book.bids[0].price + book.asks[0].price) / 2
    bid_bound = mid * (1 - band)
    ask_bound = mid * (1 + band)
    bids = list(takewhile(lambda level: level.price >= bid_bound, book.bids))
    asks = list(takewhile(lambda level: level.price <= ask_bound, book.asks))
    zero = amount(0)
    inputs = (book.evidence_id,)
    return DepthMetrics(
        market=book.market,
        band=band,
        mid=mid,
        bid_bound=bid_bound,
        ask_bound=ask_bound,
        bid_quantity=sum((level.quantity for level in bids), zero),
        bid_notional=sum((level.price * level.quantity for level in bids), zero),
        bid_complete=len(bids) < len(book.bids),
        ask_quantity=sum((level.quantity for level in asks), zero),
        ask_notional=sum((level.price * level.quantity for level in asks), zero),
        ask_complete=len(asks) < len(book.asks),
        time_ns=item_time_ns(book),
        inputs=inputs,
        calculation_version=DEPTH_VERSION,
        evidence_id=calculation_id(
            DEPTH_CALCULATION, DEPTH_VERSION, [("band", str(band))], inputs
        ),
    )
