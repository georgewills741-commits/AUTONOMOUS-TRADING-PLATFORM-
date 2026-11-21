"""The rate-limit manager (EXA-014; the Stage 2 plan's U4): no request over a limit, also under
concurrency; priority; backoff after a rate-limit refusal; retries for reads only where a retry
may change the outcome. Waits run on a fake clock."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable

import pytest
from pydantic import ValidationError

from atp.contracts import Outcome
from atp.exchange import (
    Backoff,
    Priority,
    RateLimit,
    RateLimiter,
    RequestFailure,
    RequestQueue,
    retry_read,
)
from atp.marketdata import UnavailableCause

BACKOFF = Backoff(initial_ns=100, maximum_ns=1_000)


class FakeClock:
    """A monotonic clock that a wait moves forward, so tests do not wait."""

    def __init__(self, now: int = 1_000) -> None:
        self.now = now
        self.waits: list[int] = []

    def __call__(self) -> int:
        return self.now

    async def sleep(self, ns: int) -> None:
        # What was due runs first, at the time it was due; then the time passes.
        assert ns > 0
        self.waits.append(ns)
        await asyncio.sleep(0)
        self.now += ns


def limiter(*limits: tuple[str, int, int]) -> RateLimiter:
    return RateLimiter(
        [RateLimit(name=name, capacity=c, window_ns=w) for name, c, w in limits],
        BACKOFF,
    )


@pytest.mark.req("EXA-014")
def test_the_backoff_doubles_up_to_its_maximum() -> None:
    assert [BACKOFF.delay_ns(n) for n in range(1, 7)] == [
        100,
        200,
        400,
        800,
        1_000,
        1_000,
    ]
    assert BACKOFF.delay_ns(10**9) == 1_000
    assert Backoff(initial_ns=300, maximum_ns=500).delay_ns(2) == 500
    assert Backoff(initial_ns=5, maximum_ns=5).delay_ns(3) == 5


@pytest.mark.parametrize("failures", [0, -1, True, 1.0])
def test_a_backoff_follows_a_failure(failures: object) -> None:
    with pytest.raises(ValueError, match="one failure or more"):
        BACKOFF.delay_ns(failures)  # type: ignore[arg-type]


def test_a_backoff_s_longest_wait_is_at_least_its_first() -> None:
    with pytest.raises(ValidationError, match="at least the first"):
        Backoff(initial_ns=10, maximum_ns=9)
    with pytest.raises(ValidationError):
        Backoff(initial_ns=0, maximum_ns=9)


def test_a_backoff_s_waits_are_64_bit_nanoseconds() -> None:
    largest = 2**63 - 1
    assert Backoff(initial_ns=largest, maximum_ns=largest).delay_ns(2) == largest
    for initial, maximum in ((1, 2**63), (2**63, largest)):
        with pytest.raises(ValidationError):
            Backoff(initial_ns=initial, maximum_ns=maximum)


@pytest.mark.req("EXA-014")
def test_a_request_fits_while_its_window_has_room() -> None:
    rate = limiter(("rest", 3, 1_000))
    for now in (0, 10, 20):
        assert rate.wait_ns({"rest": 1}, now) == 0
        rate.take({"rest": 1}, now)
    # Full until the first request leaves the window at 0 + 1,000.
    assert rate.wait_ns({"rest": 1}, 500) == 500
    with pytest.raises(ValueError, match="over a limit"):
        rate.take({"rest": 1}, 999)
    assert rate.wait_ns({"rest": 1}, 1_000) == 0
    # A weight of two waits for the second request to leave too.
    assert rate.wait_ns({"rest": 2}, 1_000) == 10


@pytest.mark.req("EXA-014")
def test_weights_count_and_the_oldest_leave_first() -> None:
    rate = limiter(("rest", 10, 100))
    rate.take({"rest": 4}, 0)
    rate.take({"rest": 5}, 50)
    assert rate.wait_ns({"rest": 1}, 60) == 0
    # Five more need the 4 of time 0 to leave, at 100.
    assert rate.wait_ns({"rest": 5}, 60) == 40
    # Six need the 5 of time 50 to leave too, at 150; so do ten.
    assert rate.wait_ns({"rest": 6}, 60) == 90
    assert rate.wait_ns({"rest": 10}, 60) == 90


@pytest.mark.req("EXA-014")
def test_a_request_must_fit_every_limit_it_names() -> None:
    rate = limiter(("rest", 100, 1_000), ("book", 1, 200))
    rate.take({"rest": 1, "book": 1}, 0)
    assert rate.wait_ns({"rest": 1}, 10) == 0
    assert rate.wait_ns({"rest": 1, "book": 1}, 10) == 190
    with pytest.raises(ValueError, match="over a limit"):
        rate.take({"rest": 1, "book": 1}, 10)
    # A refused take records nothing.
    assert rate.wait_ns({"rest": 100}, 999) == 1


@pytest.mark.req("EXA-014")
def test_a_rate_limit_refusal_pauses_every_request_with_a_doubling_backoff() -> None:
    rate = limiter(("rest", 100, 1_000))
    assert rate.refused(0, None) == 100
    assert rate.wait_ns({"rest": 1}, 50) == 50
    assert rate.wait_ns({"rest": 1}, 100) == 0
    assert rate.refused(100, None) == 200
    assert rate.refused(300, None) == 400
    assert rate.wait_ns({"rest": 1}, 300) == 400
    rate.accepted()
    assert rate.refused(1_000, None) == 100


@pytest.mark.req("EXA-014")
def test_a_refusal_waits_as_long_as_the_venue_asks_when_that_is_longer() -> None:
    rate = limiter(("rest", 100, 1_000))
    assert rate.refused(0, 5_000) == 5_000
    assert rate.wait_ns({"rest": 1}, 1) == 4_999
    # A shorter request never shortens a pause already set.
    assert rate.refused(10, 0) == 200
    assert rate.wait_ns({"rest": 1}, 10) == 4_990


@pytest.mark.parametrize(
    ("costs", "message"),
    [
        ({}, "one limit or more"),
        ({"other": 1}, "no limit is named"),
        ({"rest": 0}, "from 1 to its capacity"),
        ({"rest": 4}, "from 1 to its capacity"),
        ({"rest": True}, "from 1 to its capacity"),
        ({"rest": 1.0}, "from 1 to its capacity"),
    ],
)
def test_costs_are_checked(costs: dict[str, object], message: str) -> None:
    with pytest.raises(ValueError, match=message):
        limiter(("rest", 3, 10)).wait_ns(costs, 0)  # type: ignore[arg-type]


def test_a_limit_is_named_once_and_times_never_go_back() -> None:
    with pytest.raises(ValueError, match="given twice"):
        limiter(("rest", 3, 10), ("rest", 4, 10))
    rate = limiter(("rest", 3, 10))
    rate.wait_ns({"rest": 1}, 5)
    with pytest.raises(ValueError, match="never goes back"):
        rate.wait_ns({"rest": 1}, 4)
    with pytest.raises(ValueError, match="never goes back"):
        rate.refused(4, None)
    with pytest.raises(ValueError, match="whole nanoseconds"):
        rate.wait_ns({"rest": 1}, -1)


def test_a_rate_limit_is_a_contract() -> None:
    with pytest.raises(ValidationError):
        RateLimit(name="Rest", capacity=1, window_ns=1)
    with pytest.raises(ValidationError):
        RateLimit(name="rest", capacity=0, window_ns=1)
    with pytest.raises(ValidationError):
        RateLimit(name="rest", capacity=1, window_ns=0)
    largest = 2**63 - 1
    limit = RateLimit(name="rest", capacity=largest, window_ns=largest)
    assert (limit.capacity, limit.window_ns) == (largest, largest)
    with pytest.raises(ValidationError):
        RateLimit(name="rest", capacity=2**63, window_ns=1)
    with pytest.raises(ValidationError):
        RateLimit(name="rest", capacity=1, window_ns=2**63)


def run_queue(
    queue_of: Callable[[FakeClock], RequestQueue],
    body: Callable[[RequestQueue, FakeClock], Awaitable[None]],
) -> FakeClock:
    clock = FakeClock()

    async def main() -> None:
        await body(queue_of(clock), clock)

    # Within five seconds of real time: a queue that stopped admitting fails the test.
    asyncio.run(asyncio.wait_for(main(), 5))
    return clock


@pytest.mark.req("EXA-014")
def test_no_request_goes_over_a_limit_under_concurrency() -> None:
    admitted: list[int] = []
    rate = limiter(("rest", 3, 1_000))

    async def body(queue: RequestQueue, clock: FakeClock) -> None:
        async def request() -> None:
            await queue.admit({"rest": 1}, Priority.NORMAL)
            admitted.append(clock())

        await asyncio.gather(*(request() for _ in range(10)))

    run_queue(
        lambda clock: RequestQueue(rate, now_ns=clock, sleep_ns=clock.sleep), body
    )
    assert len(admitted) == 10
    for start in admitted:
        assert sum(start <= time < start + 1_000 for time in admitted) <= 3
    assert admitted == sorted(admitted)
    assert admitted[3] - admitted[0] == 1_000


@pytest.mark.req("EXA-014")
def test_waiting_requests_are_admitted_in_priority_order() -> None:
    order: list[str] = []
    rate = limiter(("rest", 1, 100))

    async def body(queue: RequestQueue, clock: FakeClock) -> None:
        rate.take({"rest": 1}, clock())

        async def request(name: str, priority: Priority) -> None:
            await queue.admit({"rest": 1}, priority)
            order.append(name)

        await asyncio.gather(
            request("low", Priority.LOW),
            request("normal 1", Priority.NORMAL),
            request("high", Priority.HIGH),
            request("normal 2", Priority.NORMAL),
        )

    run_queue(
        lambda clock: RequestQueue(rate, now_ns=clock, sleep_ns=clock.sleep), body
    )
    assert order == ["high", "normal 1", "normal 2", "low"]


def test_a_request_whose_caller_stops_waiting_takes_no_room() -> None:
    admitted: list[str] = []
    rate = limiter(("rest", 1, 100))

    async def body(queue: RequestQueue, clock: FakeClock) -> None:
        rate.take({"rest": 1}, clock())
        first = asyncio.ensure_future(queue.admit({"rest": 1}, Priority.HIGH))
        await asyncio.sleep(0)
        first.cancel()
        await queue.admit({"rest": 1}, Priority.LOW)
        admitted.append("second")

    clock = run_queue(
        lambda clock: RequestQueue(rate, now_ns=clock, sleep_ns=clock.sleep), body
    )
    assert admitted == ["second"]
    # The second was admitted when the first take left the window, not a window later.
    assert clock.now == 1_100


@pytest.mark.req("EXA-014")
def test_a_later_request_starts_the_queue_again() -> None:
    admitted: list[int] = []
    rate = limiter(("rest", 1, 100))

    async def body(queue: RequestQueue, clock: FakeClock) -> None:
        await queue.admit({"rest": 1}, Priority.NORMAL)
        admitted.append(clock())
        await clock.sleep(1_000)
        await queue.admit({"rest": 1}, Priority.NORMAL)
        admitted.append(clock())

    run_queue(
        lambda clock: RequestQueue(rate, now_ns=clock, sleep_ns=clock.sleep), body
    )
    assert admitted == [1_000, 2_000]


def test_a_failure_of_the_queue_is_given_to_every_waiting_request() -> None:
    failures: list[str] = []
    admitted: list[int] = []
    rate = limiter(("rest", 1, 100))

    async def body(queue: RequestQueue, clock: FakeClock) -> None:
        rate.take({"rest": 1}, clock())

        async def request() -> None:
            try:
                await queue.admit({"rest": 1}, Priority.NORMAL)
            except ValueError as error:
                failures.append(str(error))

        # The clock goes back: the queue cannot admit, and no request waits for good.
        clock.now -= 1
        await asyncio.gather(request(), request())
        # The clock right again, the queue admits again.
        clock.now += 101
        await queue.admit({"rest": 1}, Priority.NORMAL)
        admitted.append(clock())

    run_queue(
        lambda clock: RequestQueue(rate, now_ns=clock, sleep_ns=clock.sleep), body
    )
    assert failures == ["a monotonic clock never goes back"] * 2
    assert admitted == [1_100]


def test_a_failure_of_the_queue_skips_requests_whose_callers_stopped_waiting() -> None:
    rate = limiter(("rest", 1, 100))

    async def body(queue: RequestQueue, clock: FakeClock) -> None:
        rate.take({"rest": 1}, clock())
        clock.now -= 1
        stopped = asyncio.ensure_future(queue.admit({"rest": 1}, Priority.NORMAL))
        waiting = [
            asyncio.ensure_future(queue.admit({"rest": 1}, priority))
            for priority in (Priority.LOW, Priority.HIGH, Priority.LOW)
        ]
        await asyncio.sleep(0)
        stopped.cancel()
        # The queue fails with the stopped request among those waiting; each other request
        # is still given the failure.
        for request in waiting:
            with pytest.raises(ValueError, match="never goes back"):
                await request

    run_queue(
        lambda clock: RequestQueue(rate, now_ns=clock, sleep_ns=clock.sleep), body
    )


def test_the_queue_checks_costs_before_waiting() -> None:
    async def body(queue: RequestQueue, clock: FakeClock) -> None:
        with pytest.raises(ValueError, match="no limit is named"):
            await queue.admit({"other": 1}, Priority.NORMAL)

    run_queue(
        lambda clock: RequestQueue(
            limiter(("rest", 1, 100)), now_ns=clock, sleep_ns=clock.sleep
        ),
        body,
    )


def scripted(
    *outcomes: Outcome[str, RequestFailure],
) -> tuple[Callable[[], Awaitable[Outcome[str, RequestFailure]]], list[int]]:
    sent: list[int] = []
    remaining = list(outcomes)

    async def send() -> Outcome[str, RequestFailure]:
        sent.append(len(sent) + 1)
        return remaining.pop(0)

    return send, sent


def result(outcome: Outcome[str, RequestFailure]) -> str:
    return outcome.fold(
        on_success=lambda value: value,
        on_failure=lambda failure: failure.cause.value,
        on_timeout=lambda: "timeout",
        on_unknown=lambda: "unknown",
    )


RATE_LIMITED = Outcome.failure(RequestFailure(UnavailableCause.RATE_LIMITED, 429))
CONNECTION_FAILED = Outcome.failure(RequestFailure(UnavailableCause.CONNECTION_FAILED))
REGION_REFUSED = Outcome.failure(RequestFailure(UnavailableCause.REGION_REFUSED, 451))
VENUE_ERROR = Outcome.failure(RequestFailure(UnavailableCause.VENUE_ERROR, 400))


@pytest.mark.req("EXA-014")
def test_a_read_is_retried_with_backoff_while_a_retry_may_help() -> None:
    send, sent = scripted(
        Outcome.timeout(),
        Outcome.unknown(),
        RATE_LIMITED,
        CONNECTION_FAILED,
        Outcome.success("data"),
    )
    clock = FakeClock()

    async def main() -> Outcome[str, RequestFailure]:
        return await retry_read(send, attempts=5, backoff=BACKOFF, sleep_ns=clock.sleep)

    assert result(asyncio.run(main())) == "data"
    assert sent == [1, 2, 3, 4, 5]
    assert clock.waits == [100, 200, 400, 800]


@pytest.mark.req("EXA-014")
def test_a_retry_waits_as_long_as_the_venue_asks_when_that_is_longer() -> None:
    send, sent = scripted(
        Outcome.failure(RequestFailure(UnavailableCause.RATE_LIMITED, 429, 700)),
        Outcome.failure(RequestFailure(UnavailableCause.RATE_LIMITED, 429, 50)),
        Outcome.success("data"),
    )
    clock = FakeClock()

    async def main() -> Outcome[str, RequestFailure]:
        return await retry_read(send, attempts=3, backoff=BACKOFF, sleep_ns=clock.sleep)

    assert result(asyncio.run(main())) == "data"
    assert sent == [1, 2, 3]
    assert clock.waits == [700, 200]


@pytest.mark.req("EXA-014")
@pytest.mark.parametrize(("asked", "sent_times"), [(1_001, [1]), (1_000, [1, 2])])
def test_a_read_is_not_retried_when_the_venue_asks_for_longer_than_its_backoff_allows(
    asked: int, sent_times: list[int]
) -> None:
    send, sent = scripted(
        Outcome.failure(RequestFailure(UnavailableCause.RATE_LIMITED, 418, asked)),
        Outcome.success("data"),
    )
    clock = FakeClock()

    async def main() -> Outcome[str, RequestFailure]:
        return await retry_read(send, attempts=3, backoff=BACKOFF, sleep_ns=clock.sleep)

    assert result(asyncio.run(main())) == ("rate-limited" if asked > 1_000 else "data")
    assert sent == sent_times
    assert clock.waits == ([] if asked > 1_000 else [asked])


@pytest.mark.req("EXA-007", "EXA-014")
@pytest.mark.parametrize(
    ("first", "expected"),
    [
        (Outcome.success("data"), "data"),
        (REGION_REFUSED, "region-refused"),
        (VENUE_ERROR, "venue-error"),
    ],
)
def test_a_read_is_not_retried_when_a_retry_cannot_help(
    first: Outcome[str, RequestFailure], expected: str
) -> None:
    send, sent = scripted(first, Outcome.success("again"))
    clock = FakeClock()

    async def main() -> Outcome[str, RequestFailure]:
        return await retry_read(send, attempts=3, backoff=BACKOFF, sleep_ns=clock.sleep)

    assert result(asyncio.run(main())) == expected
    assert sent == [1]
    assert clock.waits == []


@pytest.mark.req("EXA-014")
def test_a_read_is_sent_at_most_its_attempts() -> None:
    send, sent = scripted(Outcome.timeout(), Outcome.timeout(), Outcome.success("late"))
    clock = FakeClock()

    async def main() -> Outcome[str, RequestFailure]:
        return await retry_read(send, attempts=2, backoff=BACKOFF, sleep_ns=clock.sleep)

    assert result(asyncio.run(main())) == "timeout"
    assert sent == [1, 2]
    assert clock.waits == [100]


@pytest.mark.parametrize("attempts", [0, -1, True])
def test_a_read_is_sent_once_or_more(attempts: object) -> None:
    send, _ = scripted(Outcome.success("data"))

    async def main() -> None:
        await retry_read(
            send,
            attempts=attempts,  # type: ignore[arg-type]
            backoff=BACKOFF,
            sleep_ns=FakeClock().sleep,
        )

    with pytest.raises(ValueError, match="once or more"):
        asyncio.run(main())


def test_a_read_of_one_attempt_is_sent_once() -> None:
    send, sent = scripted(Outcome.timeout(), Outcome.success("late"))
    clock = FakeClock()

    async def main() -> Outcome[str, RequestFailure]:
        return await retry_read(send, attempts=1, backoff=BACKOFF, sleep_ns=clock.sleep)

    assert result(asyncio.run(main())) == "timeout"
    assert sent == [1]
    assert clock.waits == []
