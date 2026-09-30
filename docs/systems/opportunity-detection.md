# Opportunity Detection Engine (Whole-Universe Market Monitoring)

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-05 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION ("Market universe", "Opportunity monitoring") · **Sources:** §08, §09

Canonical definition of how the platform watches its whole authorized trading universe and finds candidate opportunities. This is **market monitoring**. It is separate from operational monitoring (ARCH-005).

## Whole-universe monitoring

- **OPP-001** Monitor the whole configured universe · CONFIRMED REQUIREMENT · §08 — The platform must continuously monitor the configured trading universe, not merely a small manually selected list.
- **OPP-002** Scan dimensions · SYSTEM REQUIREMENT · §08 — The opportunity-monitoring architecture should be capable of scanning relevant supported markets across: exchanges; assets; trading pairs; directional conditions; cross-exchange relationships; triangular routes; liquidity conditions; volatility; funding; market regimes; significant events.
- **OPP-003** Discover within the authorized universe · CONFIRMED REQUIREMENT · §08 — The purpose is to allow the system to discover opportunities wherever they exist within the authorized universe.
- **OPP-004** Not everything through AI · CONSTRAINT · §08 — This does not mean blindly processing every possible market event through AI.
- **OPP-005** Monitoring pipeline · CONFIRMED ARCHITECTURAL PRINCIPLE · §08 — Whole market universe → deterministic market data → quantitative processing → opportunity scanning → filtering → significant / executable opportunity → strategy / risk / capital → AI only when justified.

## Opportunity detection

- **OPP-006** Shared detection capability · CONFIRMED ARCHITECTURAL PRINCIPLE · §09 — The platform requires a shared opportunity-detection capability.
- **OPP-007** Detection scope · SYSTEM REQUIREMENT · §09 — It should identify: directional opportunities; cross-exchange arbitrage; triangular arbitrage; market-regime changes; significant anomalies; liquidity changes; strategy conditions; relevant market events.
- **OPP-008** Deterministic screening, selective AI · CONFIRMED ARCHITECTURAL PRINCIPLE · §09 — Deterministic systems perform high-volume screening. AI is activated only when its reasoning adds meaningful value.

## Decisions applied (2026-09-30)

- **OPP-009** Trading universe · CONFIRMED REQUIREMENT · DEC-008 — The authorized trading universe is every market of an enabled instrument type on an enabled venue, minus exclusions set in the Policy System. It updates automatically as venues list and delist markets.
- **OPP-010** Single owner of market monitoring · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This engine is the only owner of market monitoring (§08 and §09 describe one system). Exchange health belongs to operational monitoring (SYS-28).
- **OPP-011** Detection, not allocation ranking · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This engine detects and filters candidates. Economic quality comes from the True Net-Profit Engine (TNP-021), and ranking for capital is done by the Global Capital Authority (CAP-017).
- **OPP-012** Tiered monitoring · SYSTEM REQUIREMENT · DEC-017 — Every market in the universe is monitored at ticker level. Full order-book depth is subscribed for markets the scanner flags as candidates, within venue rate limits.

## Boundary (§92)

- **Owns:** scanning of the configured universe and production of candidate opportunities.
- **Consumes:** [market data](market-data.md), [quantitative](quantitative-engine.md) outputs, and [regime](market-regime-engine.md) state.
- **Hands off to:** trading systems, then capital and risk. Economic evaluation belongs to the [True Net-Profit Engine](true-net-profit-engine.md).
- **Not yet specified:** filtering criteria, what counts as a "significant" event, interfaces, tests. The universe is defined by OPP-009.

## Findings (all resolved)

DUP-05 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (OPP-010). DUP-10 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (OPP-011). CF-02 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (AI, when used, sits before the capital and risk steps). OQ-03 → [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md) (OPP-009).
