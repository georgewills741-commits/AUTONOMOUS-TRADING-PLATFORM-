# Exchange Adapter Layer

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-01 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION · **Sources:** §42 (also §02 item 16)

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

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

- **EXA-010** Transfer support · SYSTEM REQUIREMENT · DEC-019 — Adapters for venues used in rebalancing support transfers to allowlisted addresses of the operator's own venue accounts, using the separate transfer credential (SEC-006), and support transfer-status queries. For on-chain transfers, status can also be confirmed on the blockchain.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **EXA-011** Venue behavior stays in adapters · CONSTRAINT · P2§44, P2§231 — The architecture is: trading engine → exchange abstraction → venue adapter → exchange. Exchange-specific behavior must not be scattered throughout the trading engine. Other venues may be added through the same abstraction.
- **EXA-012** Additional adapter responsibilities · SYSTEM REQUIREMENT · P2§45, P2§232 — In addition to EXA-003, adapters may handle: market-data subscriptions; symbol mapping; fee metadata; order cancellation; order querying; WebSocket state; connection management. Shared trading logic remains outside adapters where possible.
- **EXA-013** Normalization into canonical objects · SYSTEM REQUIREMENT · P2§46, P2§233 — Exchanges differ in symbols, orders, fills, fees, positions, timestamps, precision, errors, and rate limits. The adapter layer must normalize these into canonical platform objects.
- **EXA-014** Rate-limit management · SYSTEM REQUIREMENT · P2§47 — Rate limits must be treated as deterministic infrastructure. The system should understand: per-endpoint limits; venue limits; backoff; retry policy; priority; WebSocket limits; REST limits. Retries must not create duplicate financial actions.
- **EXA-015** Connection resilience · SYSTEM REQUIREMENT · P2§48 — Connections should be resilient. The platform should support: connection health; reconnect; heartbeats; stale-feed detection; backoff; circuit breaking; venue degradation states.

P2§44 names Binance, OKX, and Coinbase; the initial venues also include Bybit and KuCoin (EXA-005, [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md)), which Part 2 allows ("other venues may be added through the same abstraction"). **Two normalizers? No (DUP-28).** Adapters translate venue formats into canonical objects (EXA-013). The single market-data normalization layer of ARCH-027 is [Market-Data Infrastructure](market-data.md) (MKD-011), which validates, deduplicates, orders, and scores the adapters' output once. Retry safety (EXA-014) relies on client order IDs (EXE-008, EXA-008).

## Boundary (§92)

- **Owns:** all venue-specific behavior (EXA-003). No other system talks to a venue directly (EXA-004).
- **Used by:** Market Data (raw data, §10), Execution Engine (orders, §02 item 16), Recovery and Reconciliation (balances, positions, open orders, fills, §71). Full list: [dependency map](../architecture/dependency-map.md).
- **Not yet specified in Part 1:** the standardized interface itself, per-venue failure behavior, credential handling (see [security](../security/security-architecture.md)), tests.

## Findings

**Resolved:** OQ-28 → [DEC-036](../decisions/DEC-036-owner-decisions-audit-findings.md): the owner confirmed the instrument scope of PLT-011 ([DEC-007](../decisions/DEC-007-instrument-scope.md)): spot, perpetual futures, and margin, no other derivatives ([open-question register](../open-questions/register.md); raised by the [master knowledge-base audit](../traceability/master-knowledge-base-audit-2026-10-02.md)). EXA-009 exposes the instrument types per venue.

Resolved:

OQ-03 → [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md) (EXA-005; trading universe in OPP-009). OQ-04 → [DEC-007](../decisions/DEC-007-instrument-scope.md) (EXA-009). TC-05 → [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md) (EXA-008).
