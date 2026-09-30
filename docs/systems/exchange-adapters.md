# Exchange Adapter Layer

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-01 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION · **Sources:** §42 (also §02 item 16)

Canonical definition of how the platform connects to trading venues.

## Requirements

- **EXA-001** Standardized adapters · CONFIRMED ARCHITECTURAL PRINCIPLE · §42 — Use standardized exchange adapters.
- **EXA-002** Candidate venues · PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION · §42 — Previously discussed examples include: Binance; OKX; Coinbase.
- **EXA-003** Adapter responsibilities · SYSTEM REQUIREMENT · §42 — Adapters should handle: authentication; market data; account data; orders; fills; balances; positions; precision; rate limits; errors; connectivity; exchange-specific capabilities.
- **EXA-004** Standardized interfaces for the rest of the platform · CONFIRMED ARCHITECTURAL PRINCIPLE · §42 — The rest of the platform should use standardized interfaces.

## Boundary (§92)

- **Owns:** all venue-specific behavior (EXA-003). No other system talks to a venue directly (EXA-004).
- **Used by:** Market Data (raw data, §10), Execution Engine (orders, §02 item 16), Recovery and Reconciliation (balances, positions, open orders, fills, §71). Full list: [dependency map](../architecture/dependency-map.md).
- **Not yet specified in Part 1:** the standardized interface itself, per-venue failure behavior, credential handling (see [security](../security/security-architecture.md)), tests.

## Findings

- OQ-03: which venues and which trading universe are in scope. EXA-002 lists previously discussed venues only.
- OQ-04: instrument scope (spot, margin, derivatives). "Positions" and funding rates imply more than spot, but Part 1 does not say.
- TC-05: idempotent execution (EXE-006) needs every adapter to support querying order state after a timeout.
