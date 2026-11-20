"""Freshness and quality (MKD-006, MKD-008, MKD-012; the Stage 2 plan's D3).

An item's age is the time from what it describes (the venue's time for it, else its local
receipt) to the assessment; against its stream's limits it is VALID, then STALE, then INVALID.
Its quality score, from 0 to 100, follows deterministically from its freshness and from whether
the venue gave its time, under the version of the rule written here. Each stream's freshness
from its latest validated item is `StreamFreshness`, beside the validation that makes items
validated.
"""

from __future__ import annotations

from typing import Final

from atp.marketdata._contracts import Freshness, QualityAssessment
from atp.marketdata._items import MarketItem, item_time_ns, stream_of, venue_time_ns
from atp.marketdata._limits import StreamLimits, ValidationLimits

QUALITY_RULE_VERSION: Final = "1.0"
"""The version of the quality score's rule below; a change to the rule is a new version."""

_FRESHNESS_SCORE: Final = {
    Freshness.VALID: 100,
    Freshness.STALE: 50,
    Freshness.INVALID: 0,
}
_NO_VENUE_TIME_PENALTY: Final = 10


def age_ns(item: MarketItem, now_ns: int) -> int:
    """How old `item` is at `now_ns`, from the time it describes; an item whose time is after
    `now_ns`, within the clock skew validation allows, is of age zero."""
    return max(now_ns - item_time_ns(item), 0)


def freshness(age: int, limits: StreamLimits) -> Freshness:
    """VALID up to the stale limit, STALE up to the invalid limit, then INVALID."""
    if age <= limits.stale_after_ns:
        return Freshness.VALID
    if age <= limits.invalid_after_ns:
        return Freshness.STALE
    return Freshness.INVALID


def quality_score(state: Freshness, *, venue_timed: bool) -> int:
    """The quality score under rule 1.0: 100 for VALID, 50 for STALE, 0 for INVALID; 10 less
    when the venue gave no time for the item, so its age is measured from the local receipt;
    never below 0."""
    score = _FRESHNESS_SCORE[state]
    if not venue_timed:
        score -= _NO_VENUE_TIME_PENALTY
    return max(score, 0)


def assess(
    item: MarketItem, now_ns: int, limits: ValidationLimits
) -> QualityAssessment:
    """The quality assessment of `item` at `now_ns`."""
    age = age_ns(item, now_ns)
    state = freshness(age, limits.for_stream(stream_of(item)))
    return QualityAssessment(
        evidence_id=item.evidence_id,
        assessed_time_ns=now_ns,
        freshness=state,
        age_ns=age,
        score=quality_score(state, venue_timed=venue_time_ns(item) is not None),
        rule_version=QUALITY_RULE_VERSION,
    )
