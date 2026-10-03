# Arbitrage Intelligence (Shared Arbitrage Capabilities)

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-20 · **Category:** arbitrage-shared capabilities · **Roadmap stage:** ARBITRAGE ("Liquidity intelligence", "Opportunity database", "Rebalancing", "Capital reserve", "Arbitrage risk") · **Sources:** §43–§47

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
| Opportunity discovery; opportunity ranking | [Opportunity Detection Engine](../opportunity-detection.md); ranking for capital by the Global Capital Authority (CAP-017) | DUP-10 |
| True net-profit calculation | [True Net-Profit Engine](../true-net-profit-engine.md) | DUP-01 |
| Arbitrage-specific risk | [Risk Engine](../../risk/risk-engine.md) | DUP-09 |
| Capital reserve; dynamic capital allocation | [Global Capital Authority](../capital-management.md) | DUP-07 |
| Rebalancing intelligence | Global Capital Authority, per ARB-007 | DUP-06 |
| Kill switch | [Risk Engine](../../risk/risk-engine.md) rule set (RSK-008) | DUP-04, OQ-06 |
| Performance controller; expected-vs-actual analysis | [Performance Controller](../performance-controller.md) | DUP-03 |
| Opportunity database | Overlaps [event and decision history](../audit-and-event-history.md) | DUP-21 |
| Liquidity intelligence | Not defined elsewhere; stays here | — |

Every overlap above is resolved: DUP-04 by [DEC-012](../../decisions/DEC-012-safety-architecture.md), all others by [DEC-011](../../decisions/DEC-011-ownership-of-shared-responsibilities.md).

## Decisions applied (2026-09-30)

- **ARB-012** Arbitrage systems use shared owners · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — The cross-exchange and triangular arbitrage systems supply leg and route definitions, sizes, and expected values. They take fee, slippage, and net-profit calculation from the True Net-Profit Engine; capital, reserve, allocation, and rebalancing decisions from the Global Capital Authority; risk rules from the Risk Engine; exchange health from operational monitoring; and expected-vs-actual analysis from the Performance Controller.
- **ARB-013** Deterministic arbitrage · CONSTRAINT · DEC-013 — Arbitrage decisions are fully deterministic. AI may analyse arbitrage performance but never proposes or approves an arbitrage trade.
- **ARB-014** Opportunity database is derived from events · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — The arbitrage opportunity database is an analytical store linked to the event and decision history by event identifiers, and can be rebuilt from it. It never diverges from the event history.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../../decisions/DEC-024-part-2-reconciliation.md).

- **ARB-015** Quality tiers are analytical only · CONSTRAINT · P2§96, P2§225 — Previously discussed analytical categories are: Tier 1, approximately ≥1% true net; Tier 2, approximately 0.5–1%; Tier 3, approximately 0.2–0.5%; Tier 4, below approximately 0.2%. These are analytical categories only, not unconditional execution rules.

### Arbitrage architecture after Part 2

Every Part 2 arbitrage item has one owner. Arbitrage systems reuse the shared owners (ARB-002, ARB-012) and add no parallel authority.

| Part 2 item | Owner | Requirements |
|---|---|---|
| Cross-exchange economics (P2§87) | SYS-18, economics from SYS-06 | XAR-002, XAR-004, TNP-018 |
| Triangular route discovery and execution risk (P2§88, §89) | SYS-19, risk rules in SYS-09 | TAR-003, TAR-004, RSK-033 |
| Capital pre-positioning (P2§90) | SYS-18 uses it; capital held by SYS-07 | XAR-005, CAP-002 |
| Intelligent rebalancing, the "Rebalancing Engine" (P2§91) | Evaluation here, decision by SYS-07 | ARB-005, ARB-006, CAP-018, CAP-023, CAP-024 |
| Arbitrage capital reserves (P2§92) | SYS-07 | ARB-008, ARB-009, CAP-029 to CAP-033 (confirmed by the owner, DEC-028) |
| Arbitrage risk engine (P2§93) | SYS-09 rule sets | RSK-012, RSK-033 |
| Arbitrage kill switch (P2§94) | SYS-09 | RSK-008, ARB-010 |
| Arbitrage performance controller (P2§95) | SYS-21 | PFC-014 |
| Quality tiers (P2§96) | Analytical categories here | ARB-015 (values register V-32) |
| Paper arbitrage (P2§97) | SYS-16 | PAP-010 |
| Four-way expected-vs-actual (P2§98) | SYS-21 | PFC-015 |
| Opportunity database (§44) | Now the arbitrage view of the platform-wide Opportunity Database in SYS-05 | ARB-003, ARB-014, OPP-016 |

ARB-015 is consistent with TNP-005 and TNP-016: the tiers never gate execution. The arbitrage build order is RMP-007.

## Boundary (§92)

- **Owns (uncontested):** liquidity intelligence and rebalancing *evaluation*. The arbitrage opportunity database is the arbitrage view of the platform-wide Opportunity Database, which the Opportunity Detection Engine owns (OPP-016; DUP-26, [DEC-024](../../decisions/DEC-024-part-2-reconciliation.md)).
- **Must not:** hold capital state outside the Global Capital Authority (ARB-009), or override global safety (ARB-011).
- **Not yet specified in Part 1:** kill-switch reset rules, database retention, interfaces, tests. Since specified: kill-switch reset and recovery (RSK-021 to RSK-025, [DEC-021](../../decisions/DEC-021-kill-switch-recovery.md)); the arbitrage kill switch is a Risk Engine rule set (RSK-008). Still open: retention of the arbitrage records, interfaces, tests.
