"""SYS-02 Market-Data Infrastructure: the canonical market-data contracts and evidence identifiers.

Requirements: ARCH-025, EXA-013, MKD-005, MKD-010, HLT-014. The contracts are the canonical
objects adapters (SYS-01, `atp.exchange`) translate venue data into (EXA-013), defined before the
adapters (ARCH-025); each item carries an evidence identifier (MKD-005), its lineage (MKD-010),
and its event and receipt times, kept exact to the venue's resolution (HLT-014). Validation,
deduplication, ordering, quality scoring, and quarantine are this system's work (MKD-011), built
at the Stage 2 plan's checkpoint B. The conventions the contracts follow are in
docs/architecture/contracts.md.
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

__all__ = [
    "ASSET_PATTERN",
    "EVIDENCE_FORM",
    "EVIDENCE_ID_PATTERN",
    "VENUE_PATTERN",
    "VERSION_PATTERN",
    "BookLevel",
    "BookSnapshot",
    "BookUpdate",
    "Freshness",
    "FundingRate",
    "InstrumentType",
    "Lineage",
    "MarketMetadata",
    "MarketRef",
    "MarketStatus",
    "OhlcvBar",
    "QualityAssessment",
    "QuarantineCause",
    "QuarantineRecord",
    "Stream",
    "TakerSide",
    "Ticker",
    "TimeResolution",
    "Trade",
    "UnavailableCause",
    "UntranslatableCause",
    "UntranslatableInput",
    "VenueState",
    "VenueStatus",
    "evidence_id",
]
