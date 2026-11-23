"""SYS-03 Quantitative Engine: the platform's deterministic calculations, with the Fee Engine and
the Slippage Engine.

Requirements: QNT-001, QNT-002, QNT-003, QNT-004, QNT-005, QNT-006, QNT-007 (Stage 2's parts: the
Stage 2 plan, section 3), TEC-003, MKD-005, MKD-010, MKD-012. No calculation asks an LLM or any AI (QNT-001, QNT-003). The engine computes
primitive metrics only (QNT-004): spreads, and the liquidity a book shows around its mid
(`spread_metrics`, `depth_metrics`); the Fee Engine's fees at a venue's published schedule and
funding payments (`estimate_fee`, `estimate_funding`); the Slippage Engine's walk of a taker
order through a book (`walk_book`); and indicators of a market's bars (`sma`, `ema`, `rsi`,
`macd`, `atr`, `simple_return`, `log_return`, `volatility`, `correlation`). Combining costs into
a net result belongs to the True Net-Profit Engine (TNP-017). The definitions are in
docs/systems/quantitative-engine.md.

Market data reaches a calculation only as `atp.marketdata`'s `Validated` (SYS-03 consumes
validated, normalized market data), and only if it was VALID when validated and is VALID again
at the time of use, which each calculation is given with the freshness limits (`now_ns`,
`limits`; MKD-012). A calculation that has no result for its data (data not VALID, a missing
price or fee schedule, too few bars, a gap, a definition that gives no value) raises
`CalculationRefused`, with its `RefusalCause`, so its consumer reads the result as unknown,
never as zero. Wrong arguments raise `TypeError` or `ValueError`.

Spreads, liquidity, fees, funding, and slippage are exact amounts (TEC-003); a quotient that
must be rounded is rounded by `atp.numeric.divide`, in the direction that never understates a
cost. Indicators are floats (TEC-003 allows them for indicators; the Stage 2 plan's D5), made
only in `_indicators`, which builds no amount. Each result is a contract that carries the time
it describes, its inputs' evidence identifiers, the version of its calculation, and its own
evidence identifier (`calculation_id`; MKD-005, MKD-010).
"""

from atp.quant._common import (
    CALCULATION_FORM,
    CalculationRefused,
    RefusalCause,
    calculation_id,
)
from atp.quant._contracts import (
    Correlation,
    DepthMetrics,
    FeeEstimate,
    FundingEstimate,
    IndicatorKind,
    IndicatorValue,
    LiquidityRole,
    PositionSide,
    SlippageEstimate,
    SpreadMetrics,
)
from atp.quant._fees import (
    FEE_CALCULATION,
    FEE_VERSION,
    FUNDING_CALCULATION,
    FUNDING_VERSION,
    estimate_fee,
    estimate_funding,
)
from atp.quant._indicators import (
    CORRELATION_CALCULATION,
    INDICATOR_CALCULATION,
    INDICATOR_VERSION,
    atr,
    correlation,
    ema,
    log_return,
    macd,
    rsi,
    simple_return,
    sma,
    volatility,
)
from atp.quant._slippage import SLIPPAGE_CALCULATION, SLIPPAGE_VERSION, walk_book
from atp.quant._spread import (
    DEPTH_CALCULATION,
    DEPTH_VERSION,
    SPREAD_CALCULATION,
    SPREAD_VERSION,
    depth_metrics,
    spread_metrics,
)

__all__ = [
    "CALCULATION_FORM",
    "CORRELATION_CALCULATION",
    "DEPTH_CALCULATION",
    "DEPTH_VERSION",
    "FEE_CALCULATION",
    "FEE_VERSION",
    "FUNDING_CALCULATION",
    "FUNDING_VERSION",
    "INDICATOR_CALCULATION",
    "INDICATOR_VERSION",
    "SLIPPAGE_CALCULATION",
    "SLIPPAGE_VERSION",
    "SPREAD_CALCULATION",
    "SPREAD_VERSION",
    "CalculationRefused",
    "Correlation",
    "DepthMetrics",
    "FeeEstimate",
    "FundingEstimate",
    "IndicatorKind",
    "IndicatorValue",
    "LiquidityRole",
    "PositionSide",
    "RefusalCause",
    "SlippageEstimate",
    "SpreadMetrics",
    "atr",
    "calculation_id",
    "correlation",
    "depth_metrics",
    "ema",
    "estimate_fee",
    "estimate_funding",
    "log_return",
    "macd",
    "rsi",
    "simple_return",
    "sma",
    "spread_metrics",
    "volatility",
    "walk_book",
]
