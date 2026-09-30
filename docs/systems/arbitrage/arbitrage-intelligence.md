# Arbitrage Intelligence (Shared Arbitrage Capabilities)

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-20 · **Category:** arbitrage-shared capabilities · **Roadmap stage:** ARBITRAGE ("Liquidity intelligence", "Opportunity database", "Rebalancing", "Capital reserve", "Arbitrage risk") · **Sources:** §43–§47

Canonical definition of capabilities used by both arbitrage systems: the opportunity database, rebalancing, the arbitrage capital reserve, and the arbitrage kill switch. Many §43 capabilities overlap platform-wide systems; each overlap is recorded below rather than resolved silently.

## Arbitrage-specific capabilities

- **ARB-001** Capability list · SYSTEM REQUIREMENT · §43 — Arbitrage-specific capabilities include: opportunity discovery; true net-profit calculation; liquidity intelligence; opportunity ranking; arbitrage-specific risk; opportunity database; capital reserve; dynamic capital allocation; rebalancing intelligence; kill switch; performance controller; expected-vs-actual analysis.
- **ARB-002** Reuse shared infrastructure · CONSTRAINT · §43 — It must reuse shared infrastructure.

## Arbitrage opportunity database

- **ARB-003** What the database records · SYSTEM REQUIREMENT · §44 — Record: detected opportunities; executed opportunities; rejected opportunities; rejection reasons; expected profitability; actual profitability; fees; slippage; liquidity; execution latency; capital used; capital unavailable; rebalancing costs; failure reasons.
- **ARB-004** Purpose of the database · CONFIRMED REQUIREMENT · §44 — This supports learning and expected-vs-actual analysis.

## Intelligent rebalancing

- **ARB-005** No automatic transfer after every trade · CONSTRAINT · §45 — The system must not automatically transfer assets after every arbitrage trade.
- **ARB-006** Rebalancing evaluation · SYSTEM REQUIREMENT · §45 — It should evaluate: current balances; future opportunities; transfer costs; network fees; transfer time; exchange liquidity; capital efficiency; expected opportunities; reserve requirements; risk.
- **ARB-007** Rebalancing is a capital-management decision · CONFIRMED ARCHITECTURAL PRINCIPLE · §45 — Rebalancing is a capital-management decision.

## Arbitrage capital reserve

- **ARB-008** Sufficient reserves · CONFIRMED REQUIREMENT · §46 — Arbitrage must maintain sufficient reserves where required to execute necessary legs and manage existing commitments.
- **ARB-009** Reserve lives in the Global Capital Authority · CONSTRAINT · §46 — The reserve must integrate with the Global Capital Authority. No hidden arbitrage capital state is permitted.

## Arbitrage kill switch

- **ARB-010** Kill-switch triggers · SYSTEM REQUIREMENT · §47 — Possible triggers: exchange instability; abnormal execution failures; liquidity collapse; unexpected spreads; repeated losses; reconciliation problems; API instability; market anomalies; capital inconsistency.
- **ARB-011** Global safety stays authoritative · CONSTRAINT · §47 — The global safety architecture remains authoritative.

## Overlap with platform-wide systems

| ARB-001 capability | Platform-wide owner | Finding |
|---|---|---|
| Opportunity discovery; opportunity ranking | [Opportunity Detection Engine](../opportunity-detection.md); ranking owner unresolved | DUP-10 |
| True net-profit calculation | [True Net-Profit Engine](../true-net-profit-engine.md) | DUP-01 |
| Arbitrage-specific risk | [Risk Engine](../../risk/risk-engine.md) | DUP-09 |
| Capital reserve; dynamic capital allocation | [Global Capital Authority](../capital-management.md) | DUP-07 |
| Rebalancing intelligence | Global Capital Authority, per ARB-007 | DUP-06 |
| Kill switch | undefined "global safety architecture" | DUP-04, OQ-06 |
| Performance controller; expected-vs-actual analysis | [Performance Controller](../performance-controller.md) | DUP-03 |
| Opportunity database | Overlaps [event and decision history](../audit-and-event-history.md) | DUP-21 |
| Liquidity intelligence | Not defined elsewhere; stays here | — |

## Boundary (§92)

- **Owns (uncontested):** the arbitrage opportunity database, liquidity intelligence, and rebalancing *evaluation*.
- **Must not:** hold capital state outside the Global Capital Authority (ARB-009), or override global safety (ARB-011).
- **Not yet specified in Part 1:** kill-switch reset rules, database retention, interfaces, tests.
