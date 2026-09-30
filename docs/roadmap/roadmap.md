# Master Roadmap

> **Status:** ACTIVE — stage classification from Handoff Part 1 (§95). Sequence and placement decided in [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md); items from the owner's correction placed by [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md). Per-stage entry and exit criteria are expected from Part 2's "implementation-stage mapping" and "verification architecture".
>
> **Implementation has not started and is not authorized.** Current position: FOUNDATION; Part 1 documented and every open item resolved; waiting for Part 2 (see [project state](../project-state.md)).

## Stage classification and sequence

- **RMP-001** Minimum stage classes · CONFIRMED REQUIREMENT · §95 — At minimum: FOUNDATION; DATA FOUNDATION; CORE TRADING FOUNDATION; DIRECTIONAL TRADING; ARBITRAGE; AI INTELLIGENCE; OPERATIONALIZATION. Exact sequencing must be finalized in the master roadmap after dependency analysis.
- **RMP-002** Sequential stages · CONFIRMED REQUIREMENT · DEC-016 — Stages run sequentially in the order of RMP-001. Every system and capability belongs to exactly one build stage (listed below), and no live trading happens before OPERATIONALIZATION's canary and live-operation items.

## Stages

"Items (§95)" are the handoff's own lists, verbatim. "Added by DEC-016" lists items §95 did not map, or mapped ambiguously. Constitution Rule 140 fields (objective, scope, tests, verification, completion criteria) will be completed per stage after Part 2.

| # | Stage | Items (§95) | Added by DEC-016 | Systems | Status |
|---|---|---|---|---|---|
| 1 | FOUNDATION | Repository; Documentation; Requirements; Architecture; Interfaces; Configuration; Security foundation; Testing foundation; Traceability | Technology stack decision (DEC-009) | Documentation set; SYS-31 (foundation) | **IN PROGRESS**: Part 1 documented, open items resolved, stack decided. Interfaces await Part 2. Configuration and testing foundations wait for implementation approval |
| 2 | DATA FOUNDATION | Exchange adapters; Market-data ingestion; Validation; Normalization; Storage; Market universe; Quantitative engine; Regime engine; Opportunity monitoring | Performance measurement framework (PERF-008 to PERF-010) and measured baselines for hard limits (V-08, V-17) | SYS-01, SYS-02, SYS-03, SYS-04, SYS-05 | NOT STARTED |
| 3 | CORE TRADING FOUNDATION | Portfolio; Capital Authority; Capital reservation; Risk; Opportunity economics; Execution; Reconciliation | Policy System (structured, versioned) incl. autonomy boundaries (POL-011); operating modes; audit and event history; system health; safety levels and emergency controller (RSK-015 to RSK-020); automatic recovery with execution lease (REC-010 to REC-013) and staged restart recovery (REC-014 to REC-018); cause-based kill-switch recovery (RSK-021 to RSK-025); trading ledger | SYS-06, SYS-07, SYS-08, SYS-09, SYS-10, SYS-11, SYS-12, SYS-29, SYS-30, SYS-33 | NOT STARTED |
| 4 | DIRECTIONAL TRADING | Directional strategies; Signals; Entry/exit; Position management; Strategy lifecycle; Backtesting; Paper trading | Strategy lifecycle, backtesting, and paper trading built as shared infrastructure; readiness-driven canary framework with the Governance and Readiness Engine (STR-013 to STR-022) | SYS-17, SYS-14, SYS-15, SYS-16 | NOT STARTED |
| 5 | ARBITRAGE | Cross-exchange; Triangular; Liquidity intelligence; True net-profit calculation; Opportunity database; Rebalancing; Capital reserve; Accumulation; Arbitrage risk; Performance controller | Arbitrage cost components and latency decay (TNP-023) added to the one True Net-Profit Engine; Performance Controller built platform-wide; autonomous rebalancing with transfer execution and transfer authority (CAP-023 to CAP-025, EXE-009, EXA-010, SEC-006, SEC-007, AUD-007) | SYS-18, SYS-19, SYS-20, SYS-21 | NOT STARTED |
| 6 | AI INTELLIGENCE | AI gateway; Natural Language Policy Interface; Model router; Agents; Trading Director; Devil's Advocate; Hallucination Firewall; Multi-agent validation; AI cost management; AI memory/knowledge | Model evaluation; structured AI output contract; confidence calibration | SYS-22, SYS-13, SYS-23, SYS-24, SYS-25, SYS-26, SYS-27 | NOT STARTED |
| 7 | OPERATIONALIZATION | Monitoring; Recovery; Reconciliation; Reporting; Performance engineering; Deployment; Canary; Live operation | Hardening of reconciliation and system health; alerting; 24/7 supervision (OPS-006, TEC-013); automatic performance-degradation handling (PERF-011) | SYS-28; SYS-11 and SYS-29 hardening; PERF; OPS | NOT STARTED |

**Cross-cutting in every stage:** numerical precision (ARCH-010, ARCH-011, TEC-003), security (SEC), and each instrument type being gated by its risk controls (PLT-012).

**Not in any stage:** platform account / custody (SYS-32), which is FUTURE ([DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md)).

The stage-level dependency diagram is in the [dependency map](../architecture/dependency-map.md).

## What remains for Part 2

Per the handoff's closing note: remaining detailed requirements, deeper subsystem specifications, interfaces and contracts, complete dependency mapping, implementation-stage mapping, verification architecture, and remaining production requirements. After Part 2 arrives, each stage gets its objective, scope, entry and exit criteria, tests, and verification (constitution Rule 140). Every decision in DEC-006 to DEC-018 is re-checked against Part 2; any conflict is recorded as a new finding, never changed silently.
