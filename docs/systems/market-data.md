# Market Data Infrastructure

> **Status:** DOCUMENTED (Handoff Parts 1, 2, and 3) — not implemented · **System:** SYS-02 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION ("Market-data ingestion", "Validation", "Normalization", "Storage") · **Sources:** §10; Part 3: P3§425–P3§427

Canonical definition of market-data ingestion, validation, normalization, and quality.

## Requirements

- **MKD-001** Foundational shared infrastructure · CONFIRMED ARCHITECTURAL PRINCIPLE · §10 — Market data is foundational shared infrastructure.
- **MKD-002** Data coverage · SYSTEM REQUIREMENT · §10 — Where supported, it should include: OHLCV; tick/trade data; order books; bid/ask; spread; volume; funding rates; exchange metadata; trading-pair metadata; timestamps; market status; execution-related information.
- **MKD-003** Market-data pipeline · CONFIRMED ARCHITECTURAL PRINCIPLE · §10 — Exchange → adapter → raw data → validation → normalization → quality checks → storage → quantitative engine → strategies / opportunity engine.
- **MKD-004** Data integrity protections · CONFIRMED REQUIREMENT · §10 — Protect against: invalid timestamps; duplicate events; missing data; out-of-order data; corruption; look-ahead bias; training/validation contamination; survivorship bias; incorrect symbol mappings; precision errors.

## Decisions applied (2026-09-30)

- **MKD-005** Evidence identifiers · CONFIRMED REQUIREMENT · DEC-013 — Every stored data item and calculation output carries a stable identifier, its source, and its timestamp, so that AI claims can cite it (AIV-001).
- **MKD-006** Freshness limits · CONSTRAINT · DEC-012 — Each market-data stream has a freshness limit. Data older than its limit is marked stale, and nothing may trade on stale data.
- **MKD-007** Storage and retention · SYSTEM REQUIREMENT · DEC-009 — Market data is kept in TimescaleDB for 30 days and permanently in compressed Parquet archives (OHLCV, trades, order-book snapshots) for backtesting (TEC-006, TEC-012).

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **MKD-008** Validation before authority · CONFIRMED REQUIREMENT · P2§49, P2§2 — Market data must be validated before being treated as authoritative, and data-quality scoring is deterministic. In addition to MKD-004, checks may include: sequence continuity; impossible prices; stale data; cross-source inconsistencies.
- **MKD-009** Data quarantine · CONFIRMED REQUIREMENT · P2§49 — Invalid data may enter DATA QUARANTINE rather than contaminating the trading path.
- **MKD-010** Data lineage · CONFIRMED REQUIREMENT · P2§50 — Important calculations and decisions should be traceable to: source; timestamp; dataset; data version; processing version; feature version; strategy version; policy version.
- **MKD-011** Single market-data normalization layer · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-024 — This system is the one market-data normalization layer of ARCH-027. Adapters translate venue formats into canonical objects (EXA-013); validation, deduplication, ordering, quality scoring, and quarantine happen here, once.

Decision lineage from market event to result is AUD-012; MKD-010 is its data side and extends the evidence identifiers of MKD-005. Clock-drift detection (P2§51) is HLT-013.

## Handoff Part 3 applied (2026-09-30)

New requirements from [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), cited as P3§N. Part 3 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 3 reconciliation](../traceability/part-3-reconciliation.md). Placement, duplicate, and conflict resolutions: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md).

- **MKD-012** Freshness states; data quality precedes decisions · SYSTEM REQUIREMENT · P3§425, P3§426 — Stale data is not fresh data: data must carry freshness information. If data exceeds acceptable age, STABLE/VALID may become STALE and eventually INVALID/QUARANTINED. The exact thresholds must be strategy- and data-type-specific. The system must not make high-confidence decisions from low-quality data. Conceptually: data quality → decision eligibility.
- **MKD-013** Quarantine causes · SYSTEM REQUIREMENT · P3§427 — Suspicious or corrupted data should be quarantined rather than silently incorporated into trading decisions. Possible causes: invalid timestamps; missing fields; impossible prices; duplicate events; sequence gaps; exchange inconsistency; outlier corruption; clock problems.

MKD-012 keeps MKD-006: each stream's freshness limit is the platform-wide hard limit (V-08; part of the safety floor, RSK-034). A strategy may require fresher data than that limit, never staler. MKD-013 lists causes for the quarantine of MKD-009. P3§428 (time synchronization) is HLT-013 and HLT-014. P3§447 (data lineage) is MKD-010.

## Boundary (§92)

- **Owns:** raw, validated, normalized, and stored market data (MKD-003).
- **Consumes:** raw data from the [Exchange Adapter Layer](exchange-adapters.md).
- **Used by:** Quantitative Engine, Opportunity Detection Engine, trading systems, Backtesting (historical data, §33).
- **Not yet specified in Part 1:** storage technology and retention, data schemas, latency targets, failure behavior when data is degraded (the DATA DEGRADED health state exists in §74 but is not defined), tests.

## Findings (all resolved)

OQ-22 → [DEC-009](../decisions/DEC-009-technology-stack.md) (storage and retention, MKD-007; the operational meaning of "logging" is MON-009). TC-06 → [DEC-013](../decisions/DEC-013-ai-organization.md) (MKD-005).
