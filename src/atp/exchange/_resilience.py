"""Connection resilience (EXA-015, EXA-007; the Stage 2 plan's U4).

A venue's connections keep their health in a `VenueHealth`: a `CircuitBreaker` stops requests to
a venue that keeps failing, then lets one trial through at a time, whose success closes it
again; a trial the venue refuses, or whose outcome never comes, lets another through once it
has run for the circuit's open time, so only a region refusal ends the venue's use for good,
and no other route is tried (EXA-007). The
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
    and while it runs the circuit is half-open and refuses the others. A success closes the
    circuit, and a failure while a trial runs opens it again; a trial that ends as neither,
    refused by the venue or never reported (its caller may have stopped), lets another request
    through once it has run for `open_ns`. Outcomes are not tied to requests: a success or a
    failure recorded while a trial runs is taken as the trial's."""

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
        self._trial_ns: int | None = None

    def _trial_runs(self, now_ns: int) -> bool:
        return self._trial_ns is not None and now_ns - self._trial_ns < self._open_ns

    def state(self, now_ns: int) -> CircuitState:
        """The state now."""
        if self._opened_ns is None:
            return CircuitState.CLOSED
        if self._trial_runs(now_ns):
            return CircuitState.HALF_OPEN
        return CircuitState.OPEN

    def allows(self, now_ns: int) -> bool:
        """Whether a request may be sent now; while the circuit is open, the first allowed is
        its trial."""
        if self._opened_ns is None:
            return True
        if self._trial_runs(now_ns):
            return False
        if self._trial_ns is None and now_ns - self._opened_ns < self._open_ns:
            return False
        self._trial_ns = now_ns
        return True

    def opens_ns(self, now_ns: int) -> int:
        """How long until a trial may be let through: zero when the circuit is closed, or when
        a trial may be let through now."""
        if self._opened_ns is None:
            return 0
        start = self._opened_ns if self._trial_ns is None else self._trial_ns
        return max(0, start + self._open_ns - now_ns)

    def succeeded(self) -> None:
        """A request succeeded: the circuit closes."""
        self._failures = 0
        self._opened_ns = None
        self._trial_ns = None

    def failed(self, now_ns: int) -> None:
        """A request failed: a trial's failure opens the circuit again, and so does the
        failure that makes `threshold` in a row."""
        if self._trial_ns is not None:
            self._trial_ns = None
            self._opened_ns = now_ns
            return
        self._failures += 1
        if self._opened_ns is None and self._failures >= self._threshold:
            self._opened_ns = now_ns


class VenueHealth:
    """A venue's state as its connections observe it: UNAVAILABLE with REGION_REFUSED for good
    once the venue refuses the region, after which no request is allowed and no other route is
    tried (EXA-007); otherwise UNAVAILABLE with RATE_LIMITED while a rate-limit refusal is the
    last outcome recorded, and UNAVAILABLE with the cause of the last failure while the circuit
    is not closed; otherwise AVAILABLE once a request has succeeded, and UNKNOWN before. A
    timeout, an UNKNOWN, and a connection that failed are failures of the venue, counted toward
    the circuit; a rate-limit refusal and a venue's refusal of one request, as it was sent, are
    neither a success nor a failure of the venue."""

    def __init__(self, limits: ResilienceLimits) -> None:
        self._circuit = CircuitBreaker(limits.failure_threshold, limits.open_ns)
        self._region_refused = False
        self._rate_limited = False
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
        """How long until the circuit lets a trial through: above zero whenever `allows`
        refuses a request, unless the venue refused the region."""
        return self._circuit.opens_ns(now_ns)

    def record(self, outcome: Outcome[object, RequestFailure], now_ns: int) -> None:
        """Record a request's outcome."""

        def failure(cause: UnavailableCause) -> None:
            self._circuit.failed(now_ns)
            self._cause = cause
            self._rate_limited = False

        def refused(error: RequestFailure) -> None:
            if error.cause is UnavailableCause.REGION_REFUSED:
                self._region_refused = True
            elif error.cause is UnavailableCause.CONNECTION_FAILED:
                failure(UnavailableCause.CONNECTION_FAILED)
            else:
                # The venue answered, refusing the request for its rate limit or as it was
                # sent (VENUE_ERROR): neither a success nor a failure of the venue, so the
                # circuit, and a trial it runs, are left as they are.
                self._rate_limited = error.cause is UnavailableCause.RATE_LIMITED

        def succeeded(_: object) -> None:
            self._circuit.succeeded()
            self._status = VenueStatus.AVAILABLE
            self._rate_limited = False

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
        if self._rate_limited:
            return VenueStatus.UNAVAILABLE, UnavailableCause.RATE_LIMITED
        if self._circuit.state(now_ns) is not CircuitState.CLOSED:
            return VenueStatus.UNAVAILABLE, self._cause
        return self._status, None


class ConnectionClosed(Exception):
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
    connection and connect again, after the backoff of the failures in a row, or the wait the
    venue asked for when it refused a connection and that is longer. A connection is
    opened only when the venue's health allows it. A failed attempt, a stale feed (a timeout),
    and a drop (a connection that failed) are failures, recorded in it; a connection counts as
    a success, and ends the run of failures, only when its first message arrives, so a venue
    whose connections open but deliver nothing still backs off and opens its circuit."""
    failures = 0
    while True:
        now = now_ns()
        if not health.allows(now):
            if health.region_refused:
                return
            # The circuit is open, or its trial runs elsewhere.
            await sleep_ns(health.wait_ns(now))
            continue
        outcome = await connect()
        connection = outcome.fold(
            on_success=lambda opened: opened,
            on_failure=lambda _: None,
            on_timeout=lambda: None,
            on_unknown=lambda: None,
        )
        if connection is None:
            health.record(outcome, now_ns())
            if health.region_refused:
                return
            failures += 1
            asked = outcome.fold(
                on_success=lambda _: None,
                on_failure=lambda failure: failure.retry_after_ns,
                on_timeout=lambda: None,
                on_unknown=lambda: None,
            )
            delay = limits.backoff.delay_ns(failures)
            await sleep_ns(delay if asked is None else max(delay, asked))
            continue
        report(FeedEvent.CONNECTED)
        delivered = False
        try:
            while True:
                message = await connection.receive(limits.heartbeat_timeout_ns)
                if message is None:
                    report(FeedEvent.STALE)
                    health.record(Outcome.timeout(), now_ns())
                    break
                if not delivered:
                    delivered = True
                    failures = 0
                    health.record(Outcome.success(None), now_ns())
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
