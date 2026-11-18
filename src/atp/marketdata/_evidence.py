"""Evidence identifiers (MKD-005; the Stage 2 plan's D5).

An item's identifier is derived from what identifies it at its venue, never drawn at random, so
the same item received twice, or replayed, gets the same identifier, and a duplicate is found by
it (MKD-004).
"""

from __future__ import annotations

import hashlib
import json
from typing import Final

from atp.marketdata._contracts import MarketRef, Stream

EVIDENCE_FORM: Final = "atp.evidence/1"
"""The name and version of the form hashed below; a change to the form is a new version."""


def evidence_id(
    *,
    venue: str,
    stream: Stream,
    market: MarketRef | None,
    venue_key: str | None = None,
    event_time_ns: int | None = None,
    content: str | None = None,
) -> str:
    """An item's evidence identifier: a SHA-256 digest, in lowercase hexadecimal.

    It digests the form's name, the venue, the stream, the market (its instrument type and
    assets) and, after them, the venue's own identifier or sequence number of the item
    (`venue_key`) where the venue gives one; otherwise the item's event time, where the venue
    gives one, and a SHA-256 digest of its content as the venue sent it (`content`). Exactly
    one of `venue_key` and `content` is given, and `venue_key` is not empty; anything else
    raises `ValueError`.
    """
    if venue_key is not None and content is None:
        if not venue_key:
            msg = "a venue's key is not empty"
            raise ValueError(msg)
        key: list[object] = ["key", venue_key]
    elif venue_key is None and content is not None:
        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
        key = ["content", event_time_ns, digest]
    else:
        msg = "exactly one of a venue's key and the content is given"
        raise ValueError(msg)
    market_part = (
        None
        if market is None
        else [market.instrument_type.value, market.base, market.quote, market.settle]
    )
    form = json.dumps(
        [EVIDENCE_FORM, venue, stream.value, market_part, *key],
        ensure_ascii=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(form.encode("ascii")).hexdigest()
