"""A venue's rate-limit manager (EXA-014; the Stage 2 plan's U4).

Rate limits are deterministic infrastructure. Each of a venue's limits, REST or WebSocket, for
the whole venue or one endpoint, is a `RateLimit` with a name: at most so much weight in any
window, a sliding one. A request names the limits it counts against, with its weight in each,
and is sent only when every one of them has room (`RateLimiter`), so no request goes over a
limit, also when many wait at once: `RequestQueue` admits waiting requests one at a time, in
priority order, and records each request's weight as it admits it; should it fail, each
request waiting is given its failure, so none waits for good. A rate-limit refusal pauses the
venue for its backoff, or longer when the venue asks for longer, the pause doubling with each
refusal in a row until a request is accepted. Reads are retried by `retry_read`, after a
backoff, or the wait the venue asked for when that is longer, only where a retry may change
the outcome; a retry rule for financial actions, which must never be repeated by a retry,
comes with them in CORE TRADING FOUNDATION (EXE-008).

Times are a monotonic clock's whole nanoseconds; the clock and the wait are given by the code
that runs the path, so that tests run without waiting.
"""

from __future__ import annotations

import asyncio
import enum
import heapq
import itertools
from collections import deque
from collections.abc import Awaitable, Callable, Iterable, Mapping
from typing import Final

from pydantic import Field

from atp.contracts import Contract, ContractVersion, Outcome
from atp.exchange._backoff import Backoff
from atp.exchange._requests import RequestFailure
from atp.marketdata import UnavailableCause

_INT64_MAX: Final = 2**63 - 1
_IDENTIFIER: Final = r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$"


class RateLimit(Contract):
    """One of a venue's limits on requests or messages, under the name its adapter gives it: at
    most `capacity` units of weight in any `window_ns` nanoseconds, a sliding window."""

    contract_id = "atp.exchange.rate-limit"
    contract_version = ContractVersion(1, 0)

    name: str = Field(pattern=_IDENTIFIER)
    capacity: int = Field(gt=0, le=_INT64_MAX)
    window_ns: int = Field(gt=0, le=_INT64_MAX)


class Priority(enum.Enum):
    """Which waiting request is admitted first: HIGH, then NORMAL, then LOW; within one
    priority, in the order they came."""

    HIGH = "high"
    NORMAL = "normal"
    LOW = "low"


_RANK: Final = {Priority.HIGH: 0, Priority.NORMAL: 1, Priority.LOW: 2}


class RateLimiter:
    """What each of a venue's limits has used in its window, and whether a request fits."""

    def __init__(self, limits: Iterable[RateLimit], backoff: Backoff) -> None:
        self._limits: dict[str, RateLimit] = {}
        for limit in limits:
            if limit.name in self._limits:
                msg = f"the limit {limit.name} is given twice"
                raise ValueError(msg)
            self._limits[limit.name] = limit
        self._used: dict[str, deque[tuple[int, int]]] = {
            name: deque() for name in self._limits
        }
        self._backoff = backoff
        self._paused_until_ns: int | None = None
        self._refusals = 0
        self._last_ns: int | None = None

    def check(self, costs: Mapping[str, int]) -> None:
        """Refuse costs that name no limit, an unknown one, or a weight that is not a whole
        number above zero, or above its limit's capacity, which no wait could make fit."""
        if not costs:
            msg = "a request counts against one limit or more"
            raise ValueError(msg)
        for name, weight in costs.items():
            limit = self._limits.get(name)
            if limit is None:
                msg = f"no limit is named {name}"
                raise ValueError(msg)
            if type(weight) is not int or not 0 < weight <= limit.capacity:
                msg = f"a weight in {name} is a whole number from 1 to its capacity"
                raise ValueError(msg)

    def _now(self, now_ns: int) -> None:
        if type(now_ns) is not int or now_ns < 0:
            msg = "a time is a monotonic clock's whole nanoseconds"
            raise ValueError(msg)
        if self._last_ns is not None and now_ns < self._last_ns:
            msg = "a monotonic clock never goes back"
            raise ValueError(msg)
        self._last_ns = now_ns

    def wait_ns(self, costs: Mapping[str, int], now_ns: int) -> int:
        """How long until a request with these costs may be sent: zero when it may now."""
        self.check(costs)
        self._now(now_ns)
        wait = 0
        if self._paused_until_ns is not None:
            wait = max(wait, self._paused_until_ns - now_ns)
        for name, weight in costs.items():
            window = self._limits[name].window_ns
            used = self._used[name]
            while used and used[0][0] + window <= now_ns:
                used.popleft()
            excess = (
                sum(taken for _, taken in used) + weight - self._limits[name].capacity
            )
            for time, taken in used:
                if excess <= 0:
                    break
                excess -= taken
                if excess <= 0:
                    wait = max(wait, time + window - now_ns)
        return wait

    def take(self, costs: Mapping[str, int], now_ns: int) -> None:
        """Record a request sent now; refused when it does not fit now."""
        if self.wait_ns(costs, now_ns) != 0:
            msg = "a request goes over a limit, or the venue's pause, now"
            raise ValueError(msg)
        for name, weight in costs.items():
            self._used[name].append((now_ns, weight))

    def refused(self, now_ns: int, retry_after_ns: int | None) -> int:
        """Record a rate-limit refusal received now, and pause every request for the backoff
        of the refusals in a row, or for `retry_after_ns` when the venue asked for longer;
        returns the pause."""
        self._now(now_ns)
        self._refusals += 1
        pause = self._backoff.delay_ns(self._refusals)
        if retry_after_ns is not None:
            pause = max(pause, retry_after_ns)
        until = now_ns + pause
        if self._paused_until_ns is None or until > self._paused_until_ns:
            self._paused_until_ns = until
        return pause

    def accepted(self) -> None:
        """Record a request the venue accepted: the next refusal is the first in a row."""
        self._refusals = 0


class RequestQueue:
    """Admits a venue's waiting requests one at a time, in priority order, each when every
    limit it counts against has room."""

    def __init__(
        self,
        limiter: RateLimiter,
        *,
        now_ns: Callable[[], int],
        sleep_ns: Callable[[int], Awaitable[None]],
    ) -> None:
        self._limiter = limiter
        self._now_ns = now_ns
        self._sleep_ns = sleep_ns
        self._waiting: list[tuple[int, int, asyncio.Future[None], dict[str, int]]] = []
        self._arrivals = itertools.count()
        self._runner: asyncio.Task[None] | None = None

    async def admit(self, costs: Mapping[str, int], priority: Priority) -> None:
        """Wait until the request may be sent; its weights are recorded as it is admitted."""
        self._limiter.check(costs)
        loop = asyncio.get_running_loop()
        admitted: asyncio.Future[None] = loop.create_future()
        heapq.heappush(
            self._waiting,
            (_RANK[priority], next(self._arrivals), admitted, dict(costs)),
        )
        if self._runner is None or self._runner.done():
            self._runner = loop.create_task(self._admit_waiting())
        await admitted

    async def _admit_waiting(self) -> None:
        try:
            while self._waiting:
                _, _, admitted, costs = self._waiting[0]
                if admitted.done():
                    # Its caller stopped waiting.
                    heapq.heappop(self._waiting)
                    continue
                now = self._now_ns()
                wait = self._limiter.wait_ns(costs, now)
                if wait == 0:
                    heapq.heappop(self._waiting)
                    self._limiter.take(costs, now)
                    admitted.set_result(None)
                    continue
                await self._sleep_ns(wait)
        except Exception as error:
            # The clock or the wait failed: each request waiting is given the failure, so
            # none waits for an admission that would never come.
            waiting, self._waiting = self._waiting, []
            for _, _, admitted, _ in waiting:
                if not admitted.done():
                    admitted.set_exception(error)


_RETRIED: Final = frozenset(
    {UnavailableCause.RATE_LIMITED, UnavailableCause.CONNECTION_FAILED}
)
"""The failures a read is retried after. A region refusal is never retried, and no other route
is tried (EXA-007); a venue's refusal of a request as it was sent would be repeated."""


async def retry_read[T](
    send: Callable[[], Awaitable[Outcome[T, RequestFailure]]],
    *,
    attempts: int,
    backoff: Backoff,
    sleep_ns: Callable[[int], Awaitable[None]],
) -> Outcome[T, RequestFailure]:
    """Send a read, and send it again, after the backoff of the attempts so far or the wait
    the venue asked for, whichever is longer, while its outcome is a TIMEOUT, an UNKNOWN, or a
    failure in `_RETRIED`, at most `attempts` times in all; the last outcome is returned."""
    if type(attempts) is not int or attempts < 1:
        msg = "a read is sent once or more"
        raise ValueError(msg)
    attempt = 1
    while True:
        outcome = await send()
        retried = outcome.fold(
            on_success=lambda _: False,
            on_failure=lambda failure: failure.cause in _RETRIED,
            on_timeout=lambda: True,
            on_unknown=lambda: True,
        )
        if not retried or attempt == attempts:
            return outcome
        asked = outcome.fold(
            on_success=lambda _: None,
            on_failure=lambda failure: failure.retry_after_ns,
            on_timeout=lambda: None,
            on_unknown=lambda: None,
        )
        delay = backoff.delay_ns(attempt)
        await sleep_ns(delay if asked is None else max(delay, asked))
        attempt += 1
