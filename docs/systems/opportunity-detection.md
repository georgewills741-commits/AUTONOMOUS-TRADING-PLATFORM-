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

## Boundary (§92)

- **Owns:** scanning of the configured universe and production of candidate opportunities.
- **Consumes:** [market data](market-data.md), [quantitative](quantitative-engine.md) outputs, and [regime](market-regime-engine.md) state.
- **Hands off to:** trading systems, then capital and risk. Economic evaluation belongs to the [True Net-Profit Engine](true-net-profit-engine.md).
- **Not yet specified in Part 1:** how the "configured" or "authorized" universe is defined and by whom, filtering criteria, what counts as a "significant" event, interfaces, tests.

## Findings

- DUP-05: §08 (whole-universe monitoring) and §09 (Opportunity Detection Engine) describe overlapping capabilities. This document treats them as one system; that grouping is PROPOSED.
- DUP-10: "opportunity discovery" and "opportunity ranking" are also listed by Arbitrage Intelligence (ARB-001) and Cross-Exchange Arbitrage (XAR-003).
- CF-02: §08 places AI after strategy/risk/capital; §70 places AI before capital/risk.
- OQ-03: how the trading universe is authorized and configured.
