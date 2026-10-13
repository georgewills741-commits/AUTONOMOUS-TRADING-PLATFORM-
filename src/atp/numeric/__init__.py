"""Exact amounts: the one way to build and round financial amounts.

Requirements: ARCH-010 (numerical precision), TEC-003 (exact decimal arithmetic), ARCH-011
(rounding to an exchange's increments; the increments themselves come in DATA FOUNDATION).
The rules are in docs/architecture/numerical-policy.md.

Call `configure_decimal_context()` once at process start. Build every amount with `amount()`,
never with `Decimal(...)` outside this package; round only with `quantize()`, which names its
direction. Any other operation whose exact result does not fit the precision raises.
"""

from atp.numeric._amount import (
    AMOUNT_PATTERN,
    AMOUNT_REFUSALS,
    AmountError,
    amount,
    amount_from_toml,
)
from atp.numeric._context import (
    PRECISION,
    TRAPPED_SIGNALS,
    DecimalContextError,
    configure_decimal_context,
    decimal_context_is_configured,
)
from atp.numeric._rounding import Rounding, quantize

__all__ = [
    "AMOUNT_PATTERN",
    "AMOUNT_REFUSALS",
    "PRECISION",
    "TRAPPED_SIGNALS",
    "AmountError",
    "DecimalContextError",
    "Rounding",
    "amount",
    "amount_from_toml",
    "configure_decimal_context",
    "decimal_context_is_configured",
    "quantize",
]
