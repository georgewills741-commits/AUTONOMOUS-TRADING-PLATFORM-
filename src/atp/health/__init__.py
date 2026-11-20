"""SYS-29 System Health: clock-drift detection.

Requirements: HLT-013, HLT-014. The monitor compares venues' server and event times with the
local clock, tells a local drift from one venue's, and gives the response of the Stage 2 plan's D3:
a drifting venue's data quarantined with the cause CLOCK_PROBLEM by `atp.marketdata`'s validation,
cross-system delays marked unreliable when the local clock drifts or cannot be told, and DATA
DEGRADED kept for SYS-29's health state, which CORE TRADING FOUNDATION builds (SR-14). Host clock
synchronization as code is OPERATIONALIZATION's (OPS-014).
"""

from atp.health._clock import (
    ClockLimits,
    ClockMonitor,
    ClockSample,
    ClockVerdict,
    LocalClock,
)

__all__ = [
    "ClockLimits",
    "ClockMonitor",
    "ClockSample",
    "ClockVerdict",
    "LocalClock",
]
