"""SYS-01 Exchange Adapter Layer: what venue access needs that no single venue owns.

Requirements: EXA-001, EXA-004, EXA-006, EXA-007, EXA-011, EXA-013, EXA-014, EXA-015. One
adapter per enabled venue implements `VenueAdapter` (EXA-001, EXA-004), and a venue is added by
its adapter and configuration alone (EXA-006, EXA-011); the adapters come venue by venue, each
after its verification (the Stage 2 plan's D1; OQ-34). Here: a message's size limit and exact
decoding, each number kept as the venue's text, and the record of untranslatable input
(EXA-013; D5); each request's result as an outcome; the rate-limit manager (EXA-014); and
connection resilience, with a region refusal ending the venue's use, no other route tried
(EXA-015, EXA-007). CCXT (TEC-005) may be imported only inside this package, and is never given
a credential, and nothing in `src/` turns TLS verification off: the structure test checks both.
"""

from atp.exchange._backoff import Backoff
from atp.exchange._interface import ServerTime, Translation, VenueAdapter
from atp.exchange._messages import (
    Decoded,
    JsonNumber,
    JsonValue,
    decode_json,
    untranslatable,
)
from atp.exchange._ratelimit import (
    Priority,
    RateLimit,
    RateLimiter,
    RequestQueue,
    retry_read,
)
from atp.exchange._requests import (
    RATE_LIMIT_STATUSES,
    REGION_REFUSAL_STATUS,
    Answered,
    Interrupted,
    NoAnswerInTime,
    NotSent,
    RequestFailure,
    TransportResult,
    request_outcome,
)
from atp.exchange._resilience import (
    CircuitBreaker,
    CircuitState,
    Connection,
    ConnectionClosed,
    FeedEvent,
    ResilienceLimits,
    VenueHealth,
    maintain_connection,
)

__all__ = [
    "RATE_LIMIT_STATUSES",
    "REGION_REFUSAL_STATUS",
    "Answered",
    "Backoff",
    "CircuitBreaker",
    "CircuitState",
    "Connection",
    "ConnectionClosed",
    "Decoded",
    "FeedEvent",
    "Interrupted",
    "JsonNumber",
    "JsonValue",
    "NoAnswerInTime",
    "NotSent",
    "Priority",
    "RateLimit",
    "RateLimiter",
    "RequestFailure",
    "RequestQueue",
    "ResilienceLimits",
    "ServerTime",
    "TransportResult",
    "Translation",
    "VenueAdapter",
    "VenueHealth",
    "decode_json",
    "maintain_connection",
    "request_outcome",
    "retry_read",
    "untranslatable",
]
