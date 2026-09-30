# Readiness System (Governance and Readiness Engine)

> **Status:** DOCUMENTED (Handoff Part 2, DEC-023, DEC-024) — not implemented · **System:** SYS-34 · **Category:** shared infrastructure (deterministic) · **Roadmap stage:** DIRECTIONAL TRADING · **Sources:** P2§65–P2§68, P2§70, P2§184, P2§339, P2§350; [DEC-023](../decisions/DEC-023-autonomous-canary-approval.md); [DEC-024](../decisions/DEC-024-part-2-reconciliation.md)
>
> Canonical definition of the one authority that decides whether a strategy or a system change is ready to progress. Requirement line format: [`docs/requirements/README.md`](../requirements/README.md).

## One system, two names

The owner named this system the **Governance and Readiness Engine** when deciding CF-13 ([DEC-023](../decisions/DEC-023-autonomous-canary-approval.md)). Handoff Part 2 calls the same responsibility the **Readiness System**. They are the same system (DUP-24). It was first placed as a component of Strategy Management. [DEC-024](../decisions/DEC-024-part-2-reconciliation.md) registers it as its own system, SYS-34, for three reasons:

- Part 2 lists it as a canonical authority next to, and separate from, the Strategy Registry (ARCH-027).
- It aggregates evidence from at least nine owners (RDY-002).
- It judges system changes as well as strategies (P2§65, OPS-011).

The owner's rules for the approval it performs stay where they are, in [Strategy Management](strategy/strategy-management.md) (STR-019 to STR-022): they govern that lifecycle's APPROVAL stage.

## Requirements

- **RDY-001** One canonical readiness system · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§65, P2§67 — The platform should have a canonical Readiness System for determining whether a strategy/system is ready to progress. There must not be several independent systems each claiming whether a strategy is "ready".
- **RDY-002** Readiness evidence · SYSTEM REQUIREMENT · P2§65, P2§67 — Readiness should consider: data quality; strategy stability; out-of-sample behavior; risk behavior; drawdown; execution quality; slippage; liquidity; reliability; error rates; operational incidents; policy compliance; reconciliation health; paper evidence; model behavior where applicable; monitoring health; recovery capability. The Readiness System aggregates evidence from: validation; risk; performance; execution; data quality; reliability; incidents; policy; paper trading.
- **RDY-003** Not a single number · CONSTRAINT · P2§65 — Readiness must not be a single arbitrary profitability number.
- **RDY-004** Explicit readiness states · SYSTEM REQUIREMENT · P2§66 — Readiness must be explicit. Possible readiness states: NOT_READY; RESEARCH; VALIDATING; PAPER_REQUIRED; PAPER_ACTIVE; READINESS_REVIEW; READY_FOR_CANARY; CANARY_ACTIVE; PRODUCTION_APPROVED; PRODUCTION_ACTIVE; SUSPENDED; REJECTED. Exact states may be refined during architecture.
- **RDY-005** Readiness reporting · SYSTEM REQUIREMENT · P2§70 — Readiness is reported with: current readiness; evidence accumulated; missing evidence; blocking conditions.
- **RDY-006** Same system as the Governance and Readiness Engine · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-024 — The Readiness System of Part 2 and the Governance and Readiness Engine of DEC-023 are one system, SYS-34. It performs the lifecycle APPROVAL stage ("READINESS REVIEW" in P2§68) under STR-019 to STR-022. It consumes evidence from the systems that own it and does not recompute that evidence.
- **RDY-007** Readiness verdict vs lifecycle stage · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-024 — The Strategy Registry (STR-023, STR-024) records which lifecycle stage a strategy version is in. This system records whether the evidence allows it to progress: its readiness state, evidence, and blocking conditions. Neither system changes the other's state.

## How readiness states relate to lifecycle stages

P2§66 says the states "may be refined during architecture". This mapping is the initial refinement ([DEC-024](../decisions/DEC-024-part-2-reconciliation.md)). It is finalized when DIRECTIONAL TRADING is planned.

| Readiness state (RDY-004) | Meaning | Lifecycle stage in the Strategy Registry (STR-024) |
|---|---|---|
| NOT_READY | Evidence is missing or failing for the next step | Any |
| RESEARCH | Hypothesis and definition work | DRAFT, RESEARCH |
| VALIDATING | Backtest, out-of-sample, walk-forward, stress, robustness | BACKTESTED, VALIDATING |
| PAPER_REQUIRED | Validation passed; paper evidence needed | VALIDATING |
| PAPER_ACTIVE | Accumulating paper evidence | PAPER |
| READINESS_REVIEW | Evidence being judged at the APPROVAL stage | PAPER |
| READY_FOR_CANARY | Every mandatory gate passed (STR-019) | APPROVED |
| CANARY_ACTIVE | Live with limited exposure | CANARY |
| PRODUCTION_APPROVED | Canary passed its promotion criteria | CANARY |
| PRODUCTION_ACTIVE | Full production | PRODUCTION |
| SUSPENDED | Stopped by a gate, a drift finding, or an operator | SUSPENDED |
| REJECTED | Blocked / readiness-failed (STR-022) | RETIRED, or back to RESEARCH as a new version |

## Evidence sources

| Evidence (RDY-002) | Owner | Requirements |
|---|---|---|
| Validation, out-of-sample, walk-forward, stress, robustness | SYS-15 Backtesting, SYS-14 Strategy Factory | STR-001, BKT-006 to BKT-009 |
| Paper evidence | SYS-16 Paper Trading | PAP-005, PAP-009 |
| Expected vs observed, drift, missed and false opportunities | SYS-21 Performance Controller | PFC-001, PFC-009 to PFC-013 |
| Risk behavior, drawdown | SYS-09 Risk Engine, SYS-08 Portfolio | RSK-002, PRT-002 |
| Capital availability | SYS-07 Global Capital Authority | STR-019 |
| Execution quality, slippage, liquidity | SYS-10 Execution Engine, SYS-21 | PFC-001 |
| Data quality | SYS-02 Market-Data Infrastructure | MKD-008 |
| Reliability, error rates, monitoring health | SYS-28 Monitoring, SYS-29 System Health | MON-010, HLT-011 |
| Operational incidents | SYS-28 Incident Management | INC-002 |
| Policy compliance | SYS-12 Policy System | POL-013 |
| Reconciliation health, recovery capability | SYS-11 Recovery and Reconciliation | REC-016 |
| Model behavior | SYS-26 Model Evaluation | MEV-004 |

## Boundary (§92)

- **Owns:** readiness states, the aggregation of readiness evidence, blocking conditions, and the automatic APPROVAL decision of STR-019.
- **Consumes:** the evidence above, read-only; the eligibility policy and the human-controlled gates (V-28) from the Policy System.
- **Produces:** readiness verdicts, canary authorization (STR-013, STR-019), and readiness reporting (RDY-005) for the [daily report](../operations/daily-system-intelligence.md).
- **Must not:** be bypassed by AI or a human (STR-022); take AI output as a verdict (AI may provide analysis only, ARCH-022); recompute evidence that another system owns (RDY-006); authorize production from paper results alone (PAP-012).
- **Failure behavior:** missing or stale evidence means NOT_READY, never READY (RDY-003, PLT-018).
- **Not yet specified:** evidence thresholds per transition (policy values, V-33 in the [values register](../requirements/values-register.md), plus V-02 to V-05 for canary); interfaces; tests.
