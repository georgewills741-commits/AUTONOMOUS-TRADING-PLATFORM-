"""Connection resilience (EXA-015, EXA-007; the Stage 2 plan's U4): the circuit breaker opens and
closes; a venue's state; reconnection after a drop; a missed heartbeat marks the feed stale; a
region refusal makes the venue unavailable, no other route tried. Waits run on a fake clock."""

from __future__ import annotations

import asyncio

import pytest

from atp.contracts import ContractError, Outcome
from atp.exchange import (
    Backoff,
    CircuitBreaker,
    CircuitState,
    Connection,
    ConnectionClosed,
    FeedEvent,
    RequestFailure,
    ResilienceLimits,
    VenueHealth,
    maintain_connection,
)
from atp.marketdata import UnavailableCause, VenueStatus

LIMITS = ResilienceLimits(
    backoff=Backoff(initial_ns=100, maximum_ns=1_000),
    failure_threshold=3,
    open_ns=10_000,
    heartbeat_timeout_ns=500,
)


def refusal(cause: UnavailableCause) -> Outcome[object, RequestFailure]:
    return Outcome.failure(RequestFailure(cause))


@pytest.mark.req("EXA-015")
def test_the_circuit_opens_after_failures_in_a_row_and_lets_one_trial_through() -> None:
    circuit = CircuitBreaker(3, 1_000)
    for now in (0, 1, 2):
        assert circuit.allows(now)
        assert circuit.state(now) is CircuitState.CLOSED
        circuit.failed(now)
    assert circuit.state(2) is CircuitState.OPEN
    assert not circuit.allows(3)
    assert circuit.opens_ns(3) == 999
    assert not circuit.allows(1_001)
    # Its open time over, the first request is the trial; the others wait for it.
    assert circuit.allows(1_002)
    assert circuit.state(1_002) is CircuitState.HALF_OPEN
    assert not circuit.allows(1_002)
    circuit.succeeded()
    assert circuit.state(1_003) is CircuitState.CLOSED
    assert circuit.allows(1_003)
    assert circuit.opens_ns(1_003) == 0


@pytest.mark.req("EXA-015")
def test_a_failed_trial_opens_the_circuit_again() -> None:
    circuit = CircuitBreaker(1, 1_000)
    circuit.failed(0)
    assert circuit.allows(1_000)
    circuit.failed(1_000)
    assert circuit.state(1_000) is CircuitState.OPEN
    assert not circuit.allows(1_999)
    assert circuit.allows(2_000)


@pytest.mark.req("EXA-015")
def test_a_success_ends_a_run_of_failures() -> None:
    circuit = CircuitBreaker(2, 1_000)
    circuit.failed(0)
    circuit.succeeded()
    circuit.failed(1)
    assert circuit.state(1) is CircuitState.CLOSED
    circuit.failed(2)
    assert circuit.state(2) is CircuitState.OPEN


@pytest.mark.parametrize(
    ("threshold", "open_ns"), [(0, 1), (True, 1), (1, 0), (1, 1.5)]
)
def test_a_circuit_s_limits_are_whole_numbers_above_zero(
    threshold: object, open_ns: object
) -> None:
    with pytest.raises(ValueError, match="above zero|or more"):
        CircuitBreaker(threshold, open_ns)  # type: ignore[arg-type]


@pytest.mark.req("EXA-015")
def test_a_venue_is_unknown_until_an_outcome_then_available_after_a_success() -> None:
    health = VenueHealth(LIMITS)
    assert health.status(0) == (VenueStatus.UNKNOWN, None)
    health.record(Outcome.timeout(), 0)
    assert health.status(0) == (VenueStatus.UNKNOWN, None)
    health.record(Outcome.success(b""), 1)
    assert health.status(1) == (VenueStatus.AVAILABLE, None)


@pytest.mark.req("EXA-015")
@pytest.mark.parametrize(
    ("failure", "cause"),
    [
        (Outcome.timeout(), UnavailableCause.TIMEOUT),
        (Outcome.unknown(), UnavailableCause.VENUE_ERROR),
        (
            refusal(UnavailableCause.CONNECTION_FAILED),
            UnavailableCause.CONNECTION_FAILED,
        ),
    ],
)
def test_failures_in_a_row_make_the_venue_unavailable_with_their_cause(
    failure: Outcome[object, RequestFailure], cause: UnavailableCause
) -> None:
    health = VenueHealth(LIMITS)
    health.record(Outcome.success(b""), 0)
    for now in (1, 2):
        health.record(failure, now)
        assert health.status(now) == (VenueStatus.AVAILABLE, None)
    health.record(failure, 3)
    assert health.status(3) == (VenueStatus.UNAVAILABLE, cause)
    assert not health.allows(4)
    assert health.wait_ns(4) == 9_999
    # The trial succeeds: the venue is available again.
    assert health.allows(10_003)
    health.record(Outcome.success(b""), 10_004)
    assert health.status(10_004) == (VenueStatus.AVAILABLE, None)


@pytest.mark.req("EXA-015")
def test_a_venue_s_refusal_of_one_request_is_not_a_failure_of_the_venue() -> None:
    health = VenueHealth(LIMITS)
    health.record(Outcome.success(b""), 0)
    for now in range(1, 10):
        health.record(refusal(UnavailableCause.VENUE_ERROR), now)
    assert health.status(10) == (VenueStatus.AVAILABLE, None)
    assert health.allows(10)


@pytest.mark.req("EXA-014", "EXA-015")
def test_a_rate_limit_refusal_makes_the_venue_unavailable_until_a_success() -> None:
    health = VenueHealth(LIMITS)
    health.record(Outcome.success(b""), 0)
    health.record(refusal(UnavailableCause.RATE_LIMITED), 1)
    assert health.status(1) == (VenueStatus.UNAVAILABLE, UnavailableCause.RATE_LIMITED)
    # The rate limiter paces the requests; the circuit stays closed.
    assert health.allows(2)
    health.record(Outcome.success(b""), 3)
    assert health.status(3) == (VenueStatus.AVAILABLE, None)


@pytest.mark.req("EXA-007", "EXA-015")
def test_a_region_refusal_makes_the_venue_unavailable_for_good() -> None:
    health = VenueHealth(LIMITS)
    health.record(Outcome.success(b""), 0)
    health.record(refusal(UnavailableCause.REGION_REFUSED), 1)
    assert health.region_refused
    assert health.status(1) == (
        VenueStatus.UNAVAILABLE,
        UnavailableCause.REGION_REFUSED,
    )
    assert not health.allows(10**12)
    health.record(Outcome.success(b""), 2)
    assert health.status(2) == (
        VenueStatus.UNAVAILABLE,
        UnavailableCause.REGION_REFUSED,
    )
    assert not health.allows(10**12)


def test_resilience_limits_are_a_contract() -> None:
    backoff = {"initial_ns": 1, "maximum_ns": 2}
    good = {
        "backoff": backoff,
        "failure_threshold": 1,
        "open_ns": 1,
        "heartbeat_timeout_ns": 1,
    }
    assert ResilienceLimits.from_python(good).failure_threshold == 1
    for name in ("failure_threshold", "open_ns", "heartbeat_timeout_ns"):
        with pytest.raises(ContractError):
            ResilienceLimits.from_python({**good, name: 0})


class FakeClock:
    def __init__(self) -> None:
        self.now = 1_000
        self.waits: list[int] = []

    def __call__(self) -> int:
        return self.now

    async def sleep(self, ns: int) -> None:
        assert ns > 0
        self.waits.append(ns)
        await asyncio.sleep(0)
        self.now += ns


class FakeConnection:
    """Gives its script in order: a message, None for a silence, or a drop."""

    def __init__(
        self, clock: FakeClock, *script: bytes | None | type[ConnectionClosed]
    ):
        self.clock = clock
        self.script = list(script)
        self.closed = False
        self.timeouts: list[int] = []

    async def receive(self, timeout_ns: int) -> bytes | None:
        self.timeouts.append(timeout_ns)
        step = self.script.pop(0)
        if step is ConnectionClosed:
            raise ConnectionClosed
        if step is None:
            self.clock.now += timeout_ns
            return None
        assert isinstance(step, bytes)
        return step

    async def close(self) -> None:
        self.closed = True


def run(
    clock: FakeClock,
    *attempts: Outcome[Connection, RequestFailure],
    health: VenueHealth | None = None,
) -> tuple[list[str], VenueHealth, int]:
    """Run `maintain_connection` over these connection attempts, the last of which must end
    it, within five seconds of real time; returns what happened, in order, the venue's health,
    and how many attempts were made."""
    events: list[str] = []
    health = VenueHealth(LIMITS) if health is None else health
    remaining = list(attempts)
    made = 0

    async def connect() -> Outcome[Connection, RequestFailure]:
        nonlocal made
        made += 1
        events.append(f"connect at {clock.now}")
        return remaining.pop(0)

    async def deliver(message: bytes) -> None:
        events.append(message.decode())

    def report(event: FeedEvent) -> None:
        events.append(event.value)

    asyncio.run(
        asyncio.wait_for(
            maintain_connection(
                connect,
                deliver,
                report,
                health=health,
                limits=LIMITS,
                now_ns=clock,
                sleep_ns=clock.sleep,
            ),
            5,
        )
    )
    return events, health, made


REGION_REFUSED: Outcome[Connection, RequestFailure] = Outcome.failure(
    RequestFailure(UnavailableCause.REGION_REFUSED, 451)
)


@pytest.mark.req("EXA-015")
def test_a_stream_reconnects_after_a_drop() -> None:
    clock = FakeClock()
    first = FakeConnection(clock, b"one", b"two", ConnectionClosed)
    second = FakeConnection(clock, b"three", ConnectionClosed)
    events, _, made = run(
        clock, Outcome.success(first), Outcome.success(second), REGION_REFUSED
    )
    assert events == [
        "connect at 1000",
        "connected",
        "one",
        "two",
        "dropped",
        "connect at 1100",
        "connected",
        "three",
        "dropped",
        "connect at 1200",
    ]
    assert made == 3
    assert first.closed and second.closed
    assert first.timeouts == [500, 500, 500]


@pytest.mark.req("EXA-015")
def test_a_missed_heartbeat_marks_the_feed_stale_and_the_stream_reconnects() -> None:
    clock = FakeClock()
    silent = FakeConnection(clock, b"one", None)
    events, health, _ = run(
        clock,
        Outcome.success(silent),
        Outcome.success(FakeConnection(clock, ConnectionClosed)),
        REGION_REFUSED,
    )
    assert events[:5] == [
        "connect at 1000",
        "connected",
        "one",
        "stale",
        "connect at 1600",
    ]
    assert silent.closed
    assert health.region_refused


@pytest.mark.req("EXA-015")
def test_failed_connections_back_off_and_open_the_circuit() -> None:
    clock = FakeClock()
    failed = Outcome.failure(RequestFailure(UnavailableCause.CONNECTION_FAILED))
    events, _, made = run(
        clock, failed, Outcome.timeout(), Outcome.unknown(), failed, REGION_REFUSED
    )
    # 100, 200, then 400 after the third failure, which opens the circuit: its trial waits for
    # the open time, 10,000 from the third failure at 1,300; the trial fails at 11,300, and the
    # next trial waits 10,000 more.
    assert events == [
        "connect at 1000",
        "connect at 1100",
        "connect at 1300",
        "connect at 11300",
        "connect at 21300",
    ]
    assert made == 5
    assert clock.waits == [100, 200, 400, 9_600, 800, 9_200]


@pytest.mark.req("EXA-015")
def test_connections_that_go_stale_or_drop_before_any_message_open_the_circuit() -> (
    None
):
    clock = FakeClock()
    events, _, _ = run(
        clock,
        Outcome.success(FakeConnection(clock, None)),
        Outcome.success(FakeConnection(clock, ConnectionClosed)),
        Outcome.success(FakeConnection(clock, None)),
        REGION_REFUSED,
    )
    assert events == [
        "connect at 1000",
        "connected",
        "stale",
        "connect at 1600",
        "connected",
        "dropped",
        "connect at 1800",
        "connected",
        "stale",
        "connect at 12300",
    ]
    assert clock.waits == [100, 200, 400, 9_600]


@pytest.mark.req("EXA-007", "EXA-015")
def test_a_venue_that_refused_the_region_is_never_connected() -> None:
    health = VenueHealth(LIMITS)
    health.record(
        Outcome.failure(RequestFailure(UnavailableCause.REGION_REFUSED, 451)), 0
    )
    clock = FakeClock()
    events, _, made = run(clock, health=health)
    assert events == []
    assert made == 0
    assert clock.waits == []


@pytest.mark.req("EXA-007", "EXA-015")
def test_a_region_refusal_ends_the_stream_and_no_other_route_is_tried() -> None:
    clock = FakeClock()
    events, health, made = run(clock, REGION_REFUSED)
    assert events == ["connect at 1000"]
    assert made == 1
    assert clock.waits == []
    assert health.status(clock.now) == (
        VenueStatus.UNAVAILABLE,
        UnavailableCause.REGION_REFUSED,
    )


@pytest.mark.req("EXA-015")
def test_a_venue_is_available_once_a_message_arrives() -> None:
    clock = FakeClock()
    health = VenueHealth(LIMITS)
    seen: list[tuple[VenueStatus, UnavailableCause | None]] = []
    attempts: list[Outcome[Connection, RequestFailure]] = [
        Outcome.success(FakeConnection(clock, b"one", ConnectionClosed)),
        REGION_REFUSED,
    ]

    async def connect() -> Outcome[Connection, RequestFailure]:
        seen.append(health.status(clock.now))
        return attempts.pop(0)

    async def deliver(message: bytes) -> None:
        seen.append(health.status(clock.now))

    asyncio.run(
        asyncio.wait_for(
            maintain_connection(
                connect,
                deliver,
                lambda event: None,
                health=health,
                limits=LIMITS,
                now_ns=clock,
                sleep_ns=clock.sleep,
            ),
            5,
        )
    )
    # Unknown when it connects; available at its first message, and still after one drop.
    assert seen == [
        (VenueStatus.UNKNOWN, None),
        (VenueStatus.AVAILABLE, None),
        (VenueStatus.AVAILABLE, None),
    ]


@pytest.mark.req("EXA-015")
def test_the_connection_is_closed_when_delivery_fails() -> None:
    clock = FakeClock()
    connection = FakeConnection(clock, b"one")
    health = VenueHealth(LIMITS)

    async def connect() -> Outcome[Connection, RequestFailure]:
        return Outcome.success(connection)

    async def deliver(message: bytes) -> None:
        raise RuntimeError(message.decode())

    async def main() -> None:
        await maintain_connection(
            connect,
            deliver,
            lambda event: None,
            health=health,
            limits=LIMITS,
            now_ns=clock,
            sleep_ns=clock.sleep,
        )

    with pytest.raises(RuntimeError, match="one"):
        asyncio.run(main())
    assert connection.closed
