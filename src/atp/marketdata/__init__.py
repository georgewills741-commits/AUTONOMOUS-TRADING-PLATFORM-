"""SYS-02 Market-Data Infrastructure: the canonical market-data contracts and evidence identifiers.

Requirements: ARCH-025, EXA-013, MKD-005, MKD-010, HLT-014. The contracts are the canonical
objects adapters (SYS-01, `atp.exchange`) translate venue data into (EXA-013), defined before the
adapters (ARCH-025); each item carries an evidence identifier (MKD-005), its lineage (MKD-010),
and its event and receipt times, kept exact to the venue's resolution (HLT-014). The conventions
the contracts follow are in docs/architecture/contracts.md.

Validation, deduplication, ordering, quality scoring, and quarantine are this system's work,
done once (MKD-011): `MarketDataValidator` checks each item under the limits of
`ValidationLimits` and returns it as `Validated`, the only form in which consumers accept market
data, or holds it back with a `QuarantineRecord` (MKD-008, MKD-009, MKD-013; the Stage 2 plan's
U5 and D3).
"""

from atp.marketdata._contracts import (
    ASSET_PATTERN,
    EVIDENCE_ID_PATTERN,
    VENUE_PATTERN,
    VERSION_PATTERN,
    BookLevel,
    BookSnapshot,
    BookUpdate,
    Freshness,
    FundingRate,
    InstrumentType,
    Lineage,
    MarketMetadata,
    MarketRef,
    MarketStatus,
    OhlcvBar,
    QualityAssessment,
    QuarantineCause,
    QuarantineRecord,
    Stream,
    TakerSide,
    Ticker,
    TimeResolution,
    Trade,
    UnavailableCause,
    UntranslatableCause,
    UntranslatableInput,
    VenueState,
    VenueStatus,
)
from atp.marketdata._evidence import EVIDENCE_FORM, evidence_id
from atp.marketdata._items import MarketItem
from atp.marketdata._limits import StreamLimits, ValidationLimits
from atp.marketdata._quality import (
    QUALITY_RULE_VERSION,
    assess,
    freshness,
    quality_score,
)
from atp.marketdata._validation import (
    VALIDATION_RULE_VERSION,
    MarketDataValidator,
    StreamFreshness,
    Validated,
    deduplicate,
    in_order,
)

__all__ = [
    "ASSET_PATTERN",
    "EVIDENCE_FORM",
    "EVIDENCE_ID_PATTERN",
    "QUALITY_RULE_VERSION",
    "VALIDATION_RULE_VERSION",
    "VENUE_PATTERN",
    "VERSION_PATTERN",
    "BookLevel",
    "BookSnapshot",
    "BookUpdate",
    "Freshness",
    "FundingRate",
    "InstrumentType",
    "Lineage",
    "MarketDataValidator",
    "MarketItem",
    "MarketMetadata",
    "MarketRef",
    "MarketStatus",
    "OhlcvBar",
    "QualityAssessment",
    "QuarantineCause",
    "QuarantineRecord",
    "Stream",
    "StreamFreshness",
    "StreamLimits",
    "TakerSide",
    "Ticker",
    "TimeResolution",
    "Trade",
    "UnavailableCause",
    "UntranslatableCause",
    "UntranslatableInput",
    "Validated",
    "ValidationLimits",
    "VenueState",
    "VenueStatus",
    "assess",
    "deduplicate",
    "evidence_id",
    "freshness",
    "in_order",
    "quality_score",
]
