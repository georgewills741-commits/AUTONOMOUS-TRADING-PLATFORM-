# Master Roadmap

> **Status:** ACTIVE — stage classification from Handoff Part 1 (§95). **Sequencing is PROPOSED.** §95 says exact sequencing must be finalized after dependency analysis, and Part 2 promises "implementation-stage mapping".
>
> **Implementation has not started and is not authorized.** Current position: FOUNDATION, documentation of Part 1 complete; waiting for Part 2 (see [project state](../project-state.md)).

## Stage classification

- **RMP-001** Minimum stage classes · CONFIRMED REQUIREMENT · §95 — At minimum: FOUNDATION; DATA FOUNDATION; CORE TRADING FOUNDATION; DIRECTIONAL TRADING; ARBITRAGE; AI INTELLIGENCE; OPERATIONALIZATION. Exact sequencing must be finalized in the master roadmap after dependency analysis.

## Stages

"Items (§95)" are the handoff's own lists, verbatim. "Systems" link items to the [system registry](../architecture/system-registry.md). Entry and exit criteria, tests, and verification per stage (constitution Rule 140) are not defined yet. They are expected from Part 2's "verification architecture".

| # | Stage | Items (§95) | Systems | Status |
|---|---|---|---|---|
| 1 | FOUNDATION | Repository; Documentation; Requirements; Architecture; Interfaces; Configuration; Security foundation; Testing foundation; Traceability | Documentation set; SYS-31 (foundation) | **IN PROGRESS**: documentation of Part 1 done; interfaces await Part 2; configuration and testing foundations not started (they need implementation approval and a technology stack, OQ-16) |
| 2 | DATA FOUNDATION | Exchange adapters; Market-data ingestion; Validation; Normalization; Storage; Market universe; Quantitative engine; Regime engine; Opportunity monitoring | SYS-01, SYS-02, SYS-03, SYS-04, SYS-05 | NOT STARTED |
| 3 | CORE TRADING FOUNDATION | Portfolio; Capital Authority; Capital reservation; Risk; Opportunity economics; Execution; Reconciliation | SYS-06, SYS-07, SYS-08, SYS-09, SYS-10, SYS-11 | NOT STARTED |
| 4 | DIRECTIONAL TRADING | Directional strategies; Signals; Entry/exit; Position management; Strategy lifecycle; Backtesting; Paper trading | SYS-17, SYS-14, SYS-15, SYS-16 | NOT STARTED |
| 5 | ARBITRAGE | Cross-exchange; Triangular; Liquidity intelligence; True net-profit calculation; Opportunity database; Rebalancing; Capital reserve; Accumulation; Arbitrage risk; Performance controller | SYS-18, SYS-19, SYS-20, SYS-21 (with SYS-06, SYS-07, SYS-09) | NOT STARTED |
| 6 | AI INTELLIGENCE | AI gateway; Natural Language Policy Interface; Model router; Agents; Trading Director; Devil's Advocate; Hallucination Firewall; Multi-agent validation; AI cost management; AI memory/knowledge | SYS-22, SYS-13, SYS-24, SYS-23, SYS-25, SYS-27 | NOT STARTED |
| 7 | OPERATIONALIZATION | Monitoring; Recovery; Reconciliation; Reporting; Performance engineering; Deployment; Canary; Live operation | SYS-28, SYS-11, PERF, OPS | NOT STARTED |

The numbering follows §95's listing order. The PROPOSED dependency order (the two trading stages can run in parallel, and AI INTELLIGENCE follows CORE) is in the [dependency map](../architecture/dependency-map.md).

## Mapping findings

Tracked as CF-05 and CF-06 in the [findings register](../conflicts/register.md).

### Not mapped to any stage by §95, with a proposed placement (RECOMMENDED — NOT YET APPROVED)

| Item | Proposed stage | Why |
|---|---|---|
| Policy System: persistent, versioned policy (SYS-12) | CORE TRADING FOUNDATION, at the latest | The Risk Engine enforces user hard constraints (CF-06) |
| Operating modes (MODE) | CORE TRADING FOUNDATION | Paper vs live separation must exist before any trading system runs |
| Auditability / event history (SYS-30) | CORE TRADING FOUNDATION | Core systems produce the events that must be recorded (AUD-003) |
| System health state machine (SYS-29) | CORE TRADING FOUNDATION, formalized; extended in OPERATIONALIZATION | Safe mode and trading halt are needed as soon as trading exists |
| Numerical precision (ARCH-010, ARCH-011) | Every stage, from DATA FOUNDATION on | Cross-cutting |
| Model evaluation (SYS-26); structured AI output and calibration (AIV-004 to AIV-012) | AI INTELLIGENCE | Needed before any AI output is used |
| Custody / ledger (SYS-32, SYS-33) | None until OQ-01 and OQ-02 are answered | Unconfirmed |
| Security beyond the foundation (SEC) | Every stage | Cross-cutting (constitution Rule 151) |

### Mapped to more than one stage, or to a stage narrower than their use

| Item | §95 mapping | Observation |
|---|---|---|
| Reconciliation | CORE and OPERATIONALIZATION | Probably core reconciliation first and operational hardening later; needs confirmation |
| Opportunity economics / true net-profit calculation | CORE and ARBITRAGE | One engine (DUP-01); arbitrage adds cost components such as transfer and multi-leg costs |
| Strategy lifecycle, backtesting, paper trading | DIRECTIONAL | Also required by arbitrage (PAP-002) |
| Performance controller | ARBITRAGE | Platform-wide (PFC-002) |

## What remains for Part 2

Per the handoff's closing note: remaining detailed requirements, deeper subsystem specifications, interfaces and contracts, complete dependency mapping, implementation-stage mapping, verification architecture, and remaining production requirements. After Part 2, this roadmap gets per-stage objectives, scope, entry and exit criteria, tests, and verification (constitution Rule 140), and the open questions are re-checked.
