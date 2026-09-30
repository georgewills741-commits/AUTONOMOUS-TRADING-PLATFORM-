# Paper Trading

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-16 · **Category:** shared infrastructure · **Roadmap stage:** DIRECTIONAL TRADING, although it covers arbitrage too (PAP-002, CF-05) · **Sources:** §32; Part 2 P2§58–P2§64, P2§97, P2§162, P2§234, P2§350

Canonical definition of paper trading. PAPER is both a platform [operating mode](../../product/operating-modes.md) (MODE-001) and a [strategy lifecycle](strategy-management.md) stage (STR-001). This document defines the paper-trading capability used by both.

## Requirements

- **PAP-001** Production architecture, realistically · CONFIRMED REQUIREMENT · §32 — Paper trading should use the production architecture as realistically as practical.
- **PAP-002** What paper trading accounts for · SYSTEM REQUIREMENT · §32 — It should account for: fees; spread; slippage; liquidity; latency; partial fills; rejections; position management; risk; capital reservation; portfolio interaction; opportunity competition; directional trading; cross-exchange arbitrage; triangular arbitrage.

## Paper trading architecture (Handoff Part 2)

New requirements from [Handoff Part 2](../../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Where each Part 2 section went: [Part 2 reconciliation](../../traceability/part-2-reconciliation.md).

- **PAP-004** Paper is a real operating mode · CONFIRMED REQUIREMENT · P2§58 — Paper/demo trading must not be treated as merely a toy simulator. The platform should support continuous real-time paper operation: live market data → deterministic processing → strategies → risk → paper capital → paper execution → paper positions → paper P&L → performance → readiness analysis.
- **PAP-005** Continuous operation and records · SYSTEM REQUIREMENT · P2§59 — The paper system should be capable of operating continuously against real market data, accumulating evidence over time. It should record: opportunities; decisions; simulated orders; simulated fills; slippage assumptions; fees; P&L; drawdown; exposure; risk events; rejected trades; missed opportunities; strategy behavior; model behavior; incidents.
- **PAP-006** Paper/live architectural parity · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§60, P2§234 — Paper trading should use the same logical architecture as live trading where practical: strategy → risk → capital → execution interface, with a paper executor or a live executor behind the execution interface. The difference should primarily be the execution environment.
- **PAP-007** Simulated capital · SYSTEM REQUIREMENT · P2§61 — Paper mode must have explicit simulated capital. The system should track: starting capital; current simulated capital; reserved capital; available capital; P&L; fees; exposure; drawdown. Simulated capital must not be confused with real exchange capital.
- **PAP-008** No perfect-fill assumption · CONSTRAINT · P2§62 — The paper executor should model relevant execution conditions rather than assuming signal → perfect fill. In addition to PAP-002, where possible it simulates order types and market movement.
- **PAP-009** Versioned evidence · SYSTEM REQUIREMENT · P2§64 — Paper mode should accumulate evidence rather than producing only a single score. Evidence should be versioned by: strategy; strategy version; policy; policy version; model; model version; market; regime; time period.
- **PAP-010** Paper arbitrage · SYSTEM REQUIREMENT · P2§97 — Arbitrage must also be testable in paper mode. The simulator should account for: multi-leg execution; liquidity; slippage; fees; partial fills; timing; venue failure; inventory; rebalancing.
- **PAP-011** Paper never touches live accounts · CONSTRAINT · P2§162 — Paper mode must never accidentally execute against live accounts. Environment and credentials must be independently controlled.
- **PAP-012** Paper results are evidence, not authorization · CONSTRAINT · P2§350 — Paper trading is a continuous evidence-generation environment, and progression toward live execution must be determined through a canonical readiness process rather than a single arbitrary performance number. No paper result should automatically become production authorization (Part 2, final non-negotiables).

### How the pieces fit

```text
live market data (SYS-02) → quant / regime / opportunity (SYS-03..05)
  → strategy (SYS-17, later SYS-18/19) → Risk Engine (SYS-09)
  → Global Capital Authority with simulated capital (SYS-07, PAP-007)
  → execution interface (SYS-10) → paper executor (this system, PAP-008)
  → paper positions and P&L → Performance Controller (SYS-21, PFC-010)
  → versioned evidence (PAP-009) → Readiness System (SYS-34, RDY-002)
```

| Concern | Owner | Requirements |
|---|---|---|
| Paper executor and its fill, latency, and partial-fill model | This system (SYS-16) | PAP-002, PAP-008, PAP-010 |
| Execution interface shared by paper and live executors | SYS-10 Execution Engine | PAP-006 |
| Simulated capital state | SYS-07 Global Capital Authority, running with simulated balances in the paper environment | PAP-007, PAP-013 |
| Expected-vs-observed comparison of paper results | SYS-21 Performance Controller | PFC-010, PFC-015 |
| Paper evidence records | This system, with events in the audit trail (SYS-30) | PAP-005, PAP-009 |
| Readiness verdict from paper evidence | SYS-34 Readiness System | RDY-001, RDY-002, PAP-012 |
| Separation from live accounts | This system, with SYS-31 Security and the environments of OPS-004 | PAP-011, MODE-006, SEC-004 |

**Where PAPER-mode strategies run (OQ-25, decided by the owner).** From [DEC-027](../../decisions/DEC-027-part-2-open-questions.md) ([owner decisions 3](../../handoffs/owner-decisions-03-part-2-findings.md), Q2):

- **PAP-013** PAPER mode runs in the paper environment · CONSTRAINT · DEC-027 — A strategy in PAPER mode runs in a separate paper setup that sees live prices but holds no real exchange keys, so it cannot touch real accounts. This is the paper environment of OPS-004, with its own simulated capital and database.

Its evidence reaches the Readiness System one way, read-only (RDY-002). Production accepts paper evidence and never accepts commands from the paper environment. A version that passes readiness is deployed to production for canary unchanged (STR-025).

## Boundary (§92)

- **Uses:** the production Risk Engine, Global Capital Authority, Portfolio, and Execution paths with simulated capital (PAP-001, MODE-001).
- **Specified by Part 2:** the paper architecture above (PAP-004 to PAP-012).
- **Not yet specified:** the fill, latency, and partial-fill models; interfaces; tests. PAP-003 refers to the canary rule STR-011, which is replaced; the canary that must confirm live costs is now STR-013 to STR-020.

## Decisions applied (2026-09-30)

- **PAP-003** Paper does not validate small margins · CONSTRAINT · DEC-014 — Paper results alone do not validate small-margin strategies. Their canary (STR-011) must confirm live expected-vs-actual costs.

## Findings

All resolved. OQ-25 → [DEC-027](../../decisions/DEC-027-part-2-open-questions.md) (PAP-013).

TC-04 → [DEC-014](../../decisions/DEC-014-net-profit-formula-and-uncertainty-margin.md) (PAP-003, TNP-022). OQ-08 → [DEC-015](../../decisions/DEC-015-modes-canary-and-policy-governance.md) (operating modes owned by the Policy System).
