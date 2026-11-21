"""The engine's results (MKD-005, MKD-010). Each names what it describes and holds its values,
the time it describes, its inputs' evidence identifiers, the version of its calculation, and its
own evidence identifier (`calculation_id`). Spreads, liquidity, fees, funding, and slippage are
amounts (TEC-003); an indicator's value is a float, which no amount is made from (the Stage 2
plan's D5).
"""

from __future__ import annotations

import enum
from typing import Annotated, Final, Literal

from pydantic import Field

from atp.config import FeeSchedule
from atp.contracts import Amount, Contract, ContractVersion
from atp.marketdata import EVIDENCE_ID_PATTERN, VERSION_PATTERN, MarketRef, TakerSide

_INT64_MAX: Final = 2**63 - 1

# Nanoseconds since the Unix epoch, UTC.
_Nanoseconds = Annotated[int, Field(ge=0, le=_INT64_MAX)]
# A whole number of bars or seconds.
_Count = Annotated[int, Field(gt=0, le=_INT64_MAX)]
_EvidenceId = Annotated[str, Field(pattern=EVIDENCE_ID_PATTERN)]


class LiquidityRole(enum.Enum):
    """Whether an order adds liquidity to a book (maker) or takes it (taker)."""

    MAKER = "maker"
    TAKER = "taker"


class PositionSide(enum.Enum):
    """The side of a perpetual position: a long gains as the price rises, a short as it falls."""

    LONG = "long"
    SHORT = "short"


class IndicatorKind(enum.Enum):
    """An indicator this engine computes; its definition is the function of the same name."""

    SMA = "sma"
    EMA = "ema"
    RSI = "rsi"
    MACD_LINE = "macd-line"
    MACD_SIGNAL = "macd-signal"
    MACD_HISTOGRAM = "macd-histogram"
    ATR = "atr"
    SIMPLE_RETURN = "simple-return"
    LOG_RETURN = "log-return"
    VOLATILITY = "volatility"


class SpreadMetrics(Contract):
    """A market's best bid and ask, from a ticker or a book snapshot, their mid, the spread, and
    the spread relative to the mid, rounded up to a multiple of `increment`, so never
    understated."""

    contract_id = "atp.quant.spread"
    contract_version = ContractVersion(1, 0)
    market: MarketRef
    bid: Amount
    ask: Amount
    mid: Amount
    spread: Amount
    relative_spread: Amount
    increment: Amount
    time_ns: _Nanoseconds
    inputs: tuple[_EvidenceId, ...] = Field(min_length=1)
    calculation_version: str = Field(pattern=VERSION_PATTERN)
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)


class DepthMetrics(Contract):
    """The liquidity a book snapshot shows within a band around its mid, the band a fraction of
    the mid (0.01 is 1%): the quantity, in the base asset, and its value, in the quote asset, of
    the bids at or above the mid less the band, and of the asks at or below the mid plus the
    band. A side is complete when the snapshot shows one of its levels beyond the band, so it
    shows all that side's depth within the band; otherwise that depth is at least what it
    shows."""

    contract_id = "atp.quant.depth"
    contract_version = ContractVersion(1, 0)
    market: MarketRef
    band: Amount
    mid: Amount
    bid_bound: Amount
    ask_bound: Amount
    bid_quantity: Amount
    bid_notional: Amount
    bid_complete: bool
    ask_quantity: Amount
    ask_notional: Amount
    ask_complete: bool
    time_ns: _Nanoseconds
    inputs: tuple[_EvidenceId, ...] = Field(min_length=1)
    calculation_version: str = Field(pattern=VERSION_PATTERN)
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)


class SlippageEstimate(Contract):
    """The Slippage Engine's estimate for a taker order of `quantity`, in the base asset, walked
    through one side of a book snapshot, best level first: the asks for a buy, the bids for a
    sell, up to `limit_price` where one is given, as for a limit order that takes liquidity.

    It gives how much fills (`filled`, `complete` when all of it), the levels it reaches, the
    best price and the worst it reaches, the value filled (`notional`, in the quote asset), and
    the average price, rounded against the taker to a multiple of `increment`: up for a buy,
    down for a sell. `slippage` is what the walk costs beyond the best price, and `impact` what
    it costs beyond the mid, which also counts half the spread; both are exact, in the quote
    asset, and never below zero. Without a level on the other side there is no mid, and no
    impact.
    """

    contract_id = "atp.quant.slippage"
    contract_version = ContractVersion(1, 0)
    market: MarketRef
    side: TakerSide
    quantity: Amount
    limit_price: Amount | None
    filled: Amount
    complete: bool
    levels: int = Field(ge=0, le=_INT64_MAX)
    best: Amount
    worst: Amount | None
    notional: Amount
    average_price: Amount | None
    increment: Amount
    slippage: Amount
    mid: Amount | None
    impact: Amount | None
    time_ns: _Nanoseconds
    inputs: tuple[_EvidenceId, ...] = Field(min_length=1)
    calculation_version: str = Field(pattern=VERSION_PATTERN)
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)


class FeeEstimate(Contract):
    """The Fee Engine's fee for an order of `notional`, in the quote asset, in a market of a
    venue, at the venue's published schedule for the market's instrument type, at its base tier
    (the Stage 2 plan's D8): the notional times the role's rate, exactly; a fee below zero is a
    rebate. It holds the schedule, which names its source and date, and the evidence
    identifiers of the inputs the notional came from, where it came from any."""

    contract_id = "atp.quant.fee"
    contract_version = ContractVersion(1, 0)
    market: MarketRef
    role: LiquidityRole
    tier: Literal["base"]
    schedule: FeeSchedule
    notional: Amount
    rate: Amount
    fee: Amount
    inputs: tuple[_EvidenceId, ...]
    calculation_version: str = Field(pattern=VERSION_PATTERN)
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)


class FundingEstimate(Contract):
    """The Fee Engine's funding payment for a perpetual position of `notional`, in the quote
    asset, for one funding interval at a published funding rate: the notional times the rate,
    exactly. When the rate is above zero a long position pays it and a short one receives it,
    and the reverse when it is below; `cost` is what the position pays, below zero when it
    receives. The funding time and interval are the venue's, where it gives them."""

    contract_id = "atp.quant.funding"
    contract_version = ContractVersion(1, 0)
    market: MarketRef
    side: PositionSide
    notional: Amount
    rate: Amount
    cost: Amount
    funding_time_ns: _Nanoseconds | None
    interval_seconds: _Count | None
    time_ns: _Nanoseconds
    inputs: tuple[_EvidenceId, ...] = Field(min_length=1)
    calculation_version: str = Field(pattern=VERSION_PATTERN)
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)


class IndicatorValue(Contract):
    """An indicator of a market's closed bars of one interval: its kind, its periods, and its
    value, a float (TEC-003; the Stage 2 plan's D5), at the end of the last bar it reads."""

    contract_id = "atp.quant.indicator"
    contract_version = ContractVersion(1, 0)
    market: MarketRef
    interval_seconds: _Count
    indicator: IndicatorKind
    periods: tuple[_Count, ...] = Field(min_length=1)
    value: float
    time_ns: _Nanoseconds
    inputs: tuple[_EvidenceId, ...] = Field(min_length=1)
    calculation_version: str = Field(pattern=VERSION_PATTERN)
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)


class Correlation(Contract):
    """The correlation of two markets' one-bar log returns over `period` returns of closed bars
    of one interval ending at the same time: Pearson's coefficient, a float from -1 to 1."""

    contract_id = "atp.quant.correlation"
    contract_version = ContractVersion(1, 0)
    market: MarketRef
    other: MarketRef
    interval_seconds: _Count
    period: _Count
    value: float = Field(ge=-1, le=1)
    time_ns: _Nanoseconds
    inputs: tuple[_EvidenceId, ...] = Field(min_length=2)
    calculation_version: str = Field(pattern=VERSION_PATTERN)
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)
