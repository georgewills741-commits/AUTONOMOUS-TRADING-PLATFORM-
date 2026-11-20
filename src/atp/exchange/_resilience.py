"""Connection resilience (EXA-015, EXA-007; the Stage 2 plan's U4).

A venue's connections keep their health in a `VenueHealth`: a `CircuitBreaker` stops requests to
a venue that keeps failing, then lets one trial through, whose success closes it again; a
region refusal makes the venue unavailable for good, and no other route is tried (EXA-007). The
venue's state is U2's `VenueStatus`, with its `UnavailableCause`: states of their own, not the
platform's. `maintain_connection` keeps a stream connected: it reconnects after a drop, and
after a missed heartbeat, which marks the feed stale, with a backoff between failed attempts.

Times are a monotonic clock's whole nanoseconds; the clock and the wait are given by the code
that runs the path.
"""

from __future__ import annotations

import enum
from collections.abc import Awaitable, Callable
from typing import Final, Protocol

from pydantic import Field

from atp.contracts import Contract, ContractVersion, Outcome
from atp.exchange._backoff import Backoff
from atp.exchange._requests import RequestFailure
from atp.marketdata import UnavailableCause, VenueStatus

_INT64_MAX: Final = 2**63 - 1


class ResilienceLimits(Contract):
    """A venue connection's resilience limits, IMPLEMENTATION CHOICE values given with its
    adapter: the backoff between failed attempts; how many failures in a row open the circuit,
    and how long it stays open before a trial; and how long a stream may stay silent, heartbeat
    answers included, before its feed is stale."""

    contract_id = "atp.exchange.resilience-limits"
    contract_version = ContractVersion(1, 0)

    backoff: Backoff
    failure_threshold: int = Field(gt=0, le=_INT64_MAX)
    open_ns: int = Field(gt=0, le=_INT64_MAX)
    heartbeat_timeout_ns: int = Field(gt=0, le=_INT64_MAX)


class CircuitState(enum.Enum):
    """A circuit breaker's state."""

    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half-open"


class CircuitBreaker:
    """Stops requests to a venue that keeps failing: `threshold` failures in a row open the
    circuit, which refuses every request for `open_ns`; then one trial request is let through,
    and while it runs the circuit is half-open and refuses the others; the trial's success
    closes the circuit, and its failure opens it again."""

    def __init__(self, threshold: int, open_ns: int) -> None:
        if type(threshold) is not int or threshold < 1:
            msg = "a circuit opens after one failure or more"
            raise ValueError(msg)
        if type(open_ns) is not int or open_ns < 1:
            msg = "a circuit stays open for whole nanoseconds above zero"
            raise ValueError(msg)
        self._threshold = threshold
        self._open_ns = open_ns
        self._failures = 0
        self._opened_ns: int | None = None
        self._trial = False

    def state(self, now_ns: int) -> CircuitState:
        """The state now."""
        if self._trial:
            return CircuitState.HALF_OPEN
        if self._opened_ns is None:
            return CircuitState.CLOSED
        return CircuitState.OPEN

    def allows(self, now_ns: int) -> bool:
        """Whether a request may be sent now; the first allowed once the circuit has been open
        for `open_ns` is its trial."""
        if self._trial:
            return False
        if self._opened_ns is None:
            return True
        if now_ns - self._opened_ns < self._open_ns:
            return False
        self._trial = True
        return True

    def opens_ns(self, now_ns: int) -> int:
        """How long until a trial may be sent: zero when the circuit is closed or its open time
        is over."""
        if self._opened_ns is None:
            return 0
        return max(0, self._opened_ns + self._open_ns - now_ns)

    def succeeded(self) -> None:
        """A request succeeded: the circuit closes."""
        self._failures = 0
        self._opened_ns = None
        self._trial = False

    def failed(self, now_ns: int) -> None:
        """A request failed: a trial's failure opens the circuit again, and so does the
        failure that makes `threshold` in a row."""
        if self._trial:
            self._trial = False
            self._opened_ns = now_ns
            return
        self._failures += 1
        if self._opened_ns is None and self._failures >= self._threshold:
            self._opened_ns = now_ns


class VenueHealth:
    """A venue's state as its connections observe it: UNKNOWN until an outcome is recorded;
    AVAILABLE after a success; UNAVAILABLE while the circuit is not closed, with the cause of
    the last failure, and while a rate-limit refusal is the last outcome, with RATE_LIMITED; and
    UNAVAILABLE with REGION_REFUSED for good once the venue refuses the region, after which no
    request is allowed and no other route is tried (EXA-007). A timeout, an UNKNOWN, and a
    connection that failed count as failures toward the circuit; a venue's refusal of one
    request, as it was sent, does not."""

    def __init__(self, limits: ResilienceLimits) -> None:
        self._circuit = CircuitBreaker(limits.failure_threshold, limits.open_ns)
        self._region_refused = False
        self._status = VenueStatus.UNKNOWN
        self._cause: UnavailableCause | None = None

    @property
    def region_refused(self) -> bool:
        """Whether the venue refused the region: it stays unavailable."""
        return self._region_refused

    def allows(self, now_ns: int) -> bool:
        """Whether a request may be sent now."""
        return not self._region_refused and self._circuit.allows(now_ns)

    def wait_ns(self, now_ns: int) -> int:
        """How long until the circuit lets a trial through."""
        return self._circuit.opens_ns(now_ns)

    def record(self, outcome: Outcome[object, RequestFailure], now_ns: int) -> None:
        """Record a request's outcome."""

        def failure(cause: UnavailableCause) -> None:
            self._circuit.failed(now_ns)
            self._cause = cause

        def refused(error: RequestFailure) -> None:
            if error.cause is UnavailableCause.REGION_REFUSED:
                self._region_refused = True
            elif error.cause is UnavailableCause.RATE_LIMITED:
                self._cause = UnavailableCause.RATE_LIMITED
            elif error.cause is UnavailableCause.CONNECTION_FAILED:
                failure(UnavailableCause.CONNECTION_FAILED)

        def succeeded(_: object) -> None:
            self._circuit.succeeded()
            self._status = VenueStatus.AVAILABLE
            self._cause = None

        outcome.fold(
            on_success=succeeded,
            on_failure=refused,
            on_timeout=lambda: failure(UnavailableCause.TIMEOUT),
            on_unknown=lambda: failure(UnavailableCause.VENUE_ERROR),
        )

    def status(self, now_ns: int) -> tuple[VenueStatus, UnavailableCause | None]:
        """The venue's state now, and why it is unavailable when it is."""
        if self._region_refused:
            return VenueStatus.UNAVAILABLE, UnavailableCause.REGION_REFUSED
        if self._circuit.state(now_ns) is not CircuitState.CLOSED:
            return VenueStatus.UNAVAILABLE, self._cause
        if self._cause is UnavailableCause.RATE_LIMITED:
            return VenueStatus.UNAVAILABLE, UnavailableCause.RATE_LIMITED
        return self._status, None


class ConnectionClosed(Exception):  # noqa: N818 - what a stream reports, not a mistake of ours
    """A stream's connection was closed or dropped."""


class Connection(Protocol):
    """A stream's open connection, as its transport gives it."""

    async def receive(self, timeout_ns: int) -> bytes | None:
        """The next message, or None when none came within `timeout_ns`; raises
        `ConnectionClosed` when the connection is closed or dropped."""
        ...

    async def close(self) -> None:
        """Close the connection."""
        ...


class FeedEvent(enum.Enum):
    """What happened to a stream's feed: connected, and subscribed; stale, after a missed
    heartbeat; or dropped."""

    CONNECTED = "connected"
    STALE = "stale"
    DROPPED = "dropped"


async def maintain_connection(
    connect: Callable[[], Awaitable[Outcome[Connection, RequestFailure]]],
    deliver: Callable[[bytes], Awaitable[None]],
    report: Callable[[FeedEvent], None],
    *,
    health: VenueHealth,
    limits: ResilienceLimits,
    now_ns: Callable[[], int],
    sleep_ns: Callable[[int], Awaitable[None]],
) -> None:
    """Keep a stream connected until the venue refuses the region, or the task is cancelled:
    connect (`connect` opens the connection and subscribes), deliver each message, and, after a
    drop or a silence longer than the heartbeat timeout, which marks the feed stale, close the
    connection and connect again, after the backoff of the failures in a row. A connection is
    opened only when the venue's health allows it; each attempt's outcome, a stale feed (a
    timeout), and a drop (a connection that failed) are recorded in it."""
    failures = 0
    while True:
        now = now_ns()
        if not health.allows(now):
            if health.region_refused:
                return
            # The circuit is open, or its trial runs elsewhere.
            wait = health.wait_ns(now)
            await sleep_ns(wait if wait > 0 else limits.backoff.initial_ns)
            continue
        outcome = await connect()
        health.record(outcome, now_ns())
        if health.region_refused:
            return
        connection = outcome.fold(
            on_success=lambda opened: opened,
            on_failure=lambda _: None,
            on_timeout=lambda: None,
            on_unknown=lambda: None,
        )
        if connection is None:
            failures += 1
            await sleep_ns(limits.backoff.delay_ns(failures))
            continue
        failures = 0
        report(FeedEvent.CONNECTED)
        try:
            while True:
                message = await connection.receive(limits.heartbeat_timeout_ns)
                if message is None:
                    report(FeedEvent.STALE)
                    health.record(Outcome.timeout(), now_ns())
                    break
                await deliver(message)
        except ConnectionClosed:
            report(FeedEvent.DROPPED)
            health.record(
                Outcome.failure(RequestFailure(UnavailableCause.CONNECTION_FAILED)),
                now_ns(),
            )
        finally:
            await connection.close()
        failures += 1
        await sleep_ns(limits.backoff.delay_ns(failures))
