# Market Data Infrastructure

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-02 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION ("Market-data ingestion", "Validation", "Normalization", "Storage") · **Sources:** §10

Canonical definition of market-data ingestion, validation, normalization, and quality.

## Requirements

- **MKD-001** Foundational shared infrastructure · CONFIRMED ARCHITECTURAL PRINCIPLE · §10 — Market data is foundational shared infrastructure.
- **MKD-002** Data coverage · SYSTEM REQUIREMENT · §10 — Where supported, it should include: OHLCV; tick/trade data; order books; bid/ask; spread; volume; funding rates; exchange metadata; trading-pair metadata; timestamps; market status; execution-related information.
- **MKD-003** Market-data pipeline · CONFIRMED ARCHITECTURAL PRINCIPLE · §10 — Exchange → adapter → raw data → validation → normalization → quality checks → storage → quantitative engine → strategies / opportunity engine.
- **MKD-004** Data integrity protections · CONFIRMED REQUIREMENT · §10 — Protect against: invalid timestamps; duplicate events; missing data; out-of-order data; corruption; look-ahead bias; training/validation contamination; survivorship bias; incorrect symbol mappings; precision errors.

## Boundary (§92)

- **Owns:** raw, validated, normalized, and stored market data (MKD-003).
- **Consumes:** raw data from the [Exchange Adapter Layer](exchange-adapters.md).
- **Used by:** Quantitative Engine, Opportunity Detection Engine, trading systems, Backtesting (historical data, §33).
- **Not yet specified in Part 1:** storage technology and retention, data schemas, latency targets, failure behavior when data is degraded (the DATA DEGRADED health state exists in §74 but is not defined), tests.

## Findings

- OQ-22: storage architecture and retention. "Storage" is named as shared infrastructure (§03, §04, §10, §95, §97) but no section defines it.
- TC-06: the Hallucination Firewall (AIV-001) needs market data to carry source and timestamp identifiers that AI claims can cite.
