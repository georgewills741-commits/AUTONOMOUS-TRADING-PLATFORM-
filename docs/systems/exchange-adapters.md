# Exchange Adapter Layer

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-01 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION · **Sources:** §42 (also §02 item 16)

Canonical definition of how the platform connects to trading venues.

## Requirements

- **EXA-001** Standardized adapters · CONFIRMED ARCHITECTURAL PRINCIPLE · §42 — Use standardized exchange adapters.
- **EXA-002** Candidate venues · DEPRECATED / REPLACED · §42 — Previously discussed examples include: Binance; OKX; Coinbase.
- **EXA-003** Adapter responsibilities · SYSTEM REQUIREMENT · §42 — Adapters should handle: authentication; market data; account data; orders; fills; balances; positions; precision; rate limits; errors; connectivity; exchange-specific capabilities.
- **EXA-004** Standardized interfaces for the rest of the platform · CONFIRMED ARCHITECTURAL PRINCIPLE · §42 — The rest of the platform should use standardized interfaces.

## Decisions applied (2026-09-30)

EXA-002 is replaced by EXA-005 (owner decision, [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md)).

- **EXA-005** Initial venues · CONFIRMED REQUIREMENT · DEC-008 — The initial supported venues are Binance, OKX, Coinbase, Bybit, and KuCoin.
- **EXA-006** New venues without platform changes · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-008 — Adding a venue requires only a new adapter and its configuration; no other system changes.
- **EXA-007** Legitimate access only · CONSTRAINT · DEC-008 — A venue is enabled only where the operator's account is permitted to use it. The platform never circumvents a venue's geographic or eligibility restrictions.
- **EXA-008** Order-state query is mandatory · CONSTRAINT · DEC-008 — An adapter must support client-assigned order IDs and querying order state after a timeout. A venue lacking either cannot be used for automated trading.
- **EXA-009** Instrument support per venue · SYSTEM REQUIREMENT · DEC-007 — Adapters expose which instrument types (spot, perpetual futures, margin) each venue supports, and handle their venue-specific settings: leverage, margin mode, position mode, funding, and borrow data.

## Boundary (§92)

- **Owns:** all venue-specific behavior (EXA-003). No other system talks to a venue directly (EXA-004).
- **Used by:** Market Data (raw data, §10), Execution Engine (orders, §02 item 16), Recovery and Reconciliation (balances, positions, open orders, fills, §71). Full list: [dependency map](../architecture/dependency-map.md).
- **Not yet specified in Part 1:** the standardized interface itself, per-venue failure behavior, credential handling (see [security](../security/security-architecture.md)), tests.

## Findings (all resolved)

OQ-03 → [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md) (EXA-005; trading universe in OPP-009). OQ-04 → [DEC-007](../decisions/DEC-007-instrument-scope.md) (EXA-009). TC-05 → [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md) (EXA-008).
