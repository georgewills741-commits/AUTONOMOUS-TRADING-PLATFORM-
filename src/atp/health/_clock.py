"""Clock-drift detection (HLT-013, HLT-014; SR-14; the Stage 2 plan's D3).

Each sample compares one venue's clock with the local wall clock. A venue's server time, read by
a request, was the venue's time at some moment between the request's sending and its answer's
receipt, so the venue's offset from the local clock lies between its time minus the receipt and
its time minus the sending. Wholly beyond the drift limit, the venue is drifting, ahead or
behind; wholly within it, the venue is in time; across it, the round trip was too long to tell.
An item's event time comes before its receipt, so it bounds the offset from below only: it can
show a venue ahead, never one behind or in time. The monitor keeps each venue's latest sample of
each kind, server time and event time, and counts those no older than the sample age limit.

The monitor tells a local drift from a venue's (D3). When some venue is in time, so is the local
clock, and each drifting venue's data gets the quarantine cause CLOCK_PROBLEM. When no venue is
in time and the drifting venues, at least `minimum_venues` of them, all drift in the same
direction, they agree with each other and the local clock is the one drifting: cross-system
delays are unreliable, and no venue's data is quarantined. Otherwise the local clock is
UNDETERMINED: delays are not reliable, and each drifting venue's data is quarantined. A drift
found raises DATA DEGRADED for SYS-29's health state (CORE); alerts come with SYS-28 (SR-14).
Where no drift is found, nothing is quarantined or degraded, even when the local clock is
UNDETERMINED for want of a sample.
"""

from __future__ import annotations

import enum
import re
from dataclasses import dataclass
from typing import Final

from pydantic import Field

from atp.contracts import Contract, ContractVersion
from atp.marketdata import VENUE_PATTERN

_INT64_MAX: Final = 2**63 - 1


class ClockLimits(Contract):
    """The limits of drift detection, IMPLEMENTATION CHOICE values set from the first live
    measurements (D3): the drift limit; how old a sample may be and still count; and how many
    venues must agree before the local clock is found drifting."""

    contract_id = "atp.health.clock-limits"
    contract_version = ContractVersion(1, 0)

    drift_limit_ns: int = Field(gt=0, le=_INT64_MAX)
    sample_max_age_ns: int = Field(gt=0, le=_INT64_MAX)
    minimum_venues: int = Field(ge=2, le=_INT64_MAX)


@dataclass(frozen=True, slots=True)
class ClockSample:
    """One comparison of `venue`'s clock with the local wall clock: the venue's time, the local
    time the request was sent (none for an item's event time), and the local receipt time, all
    in nanoseconds since the Unix epoch, UTC."""

    venue: str
    venue_time_ns: int
    sent_ns: int | None
    received_ns: int

    def __post_init__(self) -> None:
        if (
            type(self.venue) is not str
            or re.fullmatch(VENUE_PATTERN, self.venue) is None
        ):
            msg = "a clock sample names a venue"
            raise ValueError(msg)
        times = [self.venue_time_ns, self.received_ns]
        if self.sent_ns is not None:
            times.append(self.sent_ns)
        if any(type(time) is not int or not 0 <= time <= _INT64_MAX for time in times):
            msg = "a clock sample's times are whole nanoseconds since the epoch"
            raise ValueError(msg)
        if self.sent_ns is not None and self.sent_ns > self.received_ns:
            msg = "a request is sent before its answer is received"
            raise ValueError(msg)

    def ahead_by_more_than(self, limit_ns: int) -> bool:
        """Whether the venue's clock is surely ahead of the local one by more than `limit_ns`."""
        return self.venue_time_ns - self.received_ns > limit_ns

    def behind_by_more_than(self, limit_ns: int) -> bool:
        """Whether the venue's clock is surely behind the local one by more than `limit_ns`;
        never for an event time, which bounds the offset from below only."""
        return self.sent_ns is not None and self.sent_ns - self.venue_time_ns > limit_ns

    def within(self, limit_ns: int) -> bool:
        """Whether the venue's clock is surely within `limit_ns` of the local one; never for an
        event time."""
        return (
            self.sent_ns is not None
            and self.received_ns - self.venue_time_ns <= limit_ns
            and self.venue_time_ns - self.sent_ns <= limit_ns
        )


class LocalClock(enum.Enum):
    """What the samples show of the local clock."""

    IN_SYNC = "in-sync"
    DRIFTING = "drifting"
    UNDETERMINED = "undetermined"


@dataclass(frozen=True, slots=True)
class ClockVerdict:
    """The monitor's finding at one time: the venues whose data gets the quarantine cause
    CLOCK_PROBLEM, and the local clock's state."""

    assessed_time_ns: int
    drifting_venues: frozenset[str]
    local_clock: LocalClock

    @property
    def data_degraded(self) -> bool:
        """Whether a drift was found: DATA DEGRADED, for SYS-29's health state (HLT-011)."""
        return bool(self.drifting_venues) or self.local_clock is LocalClock.DRIFTING

    @property
    def delays_reliable(self) -> bool:
        """Whether cross-system delays, from a venue's time to a local one, can be trusted."""
        return self.local_clock is LocalClock.IN_SYNC


class ClockMonitor:
    """Each venue's latest clock sample of each kind, and the verdict they give."""

    def __init__(self, limits: ClockLimits) -> None:
        self._limits = limits
        self._latest: dict[tuple[str, bool], ClockSample] = {}

    def observe(self, sample: ClockSample) -> None:
        """Keep `sample` if it is the venue's latest of its kind: a server time, or an event
        time, so that event times, which come often, never hide a server time's finding."""
        key = (sample.venue, sample.sent_ns is not None)
        known = self._latest.get(key)
        if known is None or sample.received_ns >= known.received_ns:
            self._latest[key] = sample

    def verdict(self, now_ns: int) -> ClockVerdict:
        """The verdict at `now_ns` from the samples no older than the limit."""
        limits = self._limits
        limit = limits.drift_limit_ns
        recent = [
            sample
            for sample in self._latest.values()
            if now_ns - sample.received_ns <= limits.sample_max_age_ns
        ]
        ahead = frozenset(
            sample.venue for sample in recent if sample.ahead_by_more_than(limit)
        )
        behind = frozenset(
            sample.venue for sample in recent if sample.behind_by_more_than(limit)
        )
        drifting = ahead | behind
        in_time = (
            frozenset(sample.venue for sample in recent if sample.within(limit))
            - drifting
        )
        if in_time:
            return ClockVerdict(now_ns, drifting, LocalClock.IN_SYNC)
        one_direction = not ahead or not behind
        if drifting and one_direction and len(drifting) >= limits.minimum_venues:
            return ClockVerdict(now_ns, frozenset(), LocalClock.DRIFTING)
        return ClockVerdict(now_ns, drifting, LocalClock.UNDETERMINED)
