# Readiness System (Governance and Readiness Engine)

> **Status:** DOCUMENTED (Handoff Parts 2 and 3, DEC-023, DEC-024, DEC-031) — not implemented · **System:** SYS-34 · **Category:** shared infrastructure (deterministic) · **Roadmap stage:** DIRECTIONAL TRADING · **Sources:** P2§65–P2§68, P2§70, P2§184, P2§339, P2§350; P3§352–P3§357, P3§378–P3§385, P3§411–P3§414, P3§478–P3§486, P3§527; [DEC-023](../decisions/DEC-023-autonomous-canary-approval.md); [DEC-024](../decisions/DEC-024-part-2-reconciliation.md); [DEC-031](../decisions/DEC-031-part-3-reconciliation.md)
>
> Canonical definition of the one authority that decides whether a strategy or a system change is ready to progress, and which capabilities are currently available. It is the platform's **capability and readiness model** (P3§541 item 13). Requirement line format: [`docs/requirements/README.md`](../requirements/README.md).

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

## Owner decisions applied (Part 2 findings, 2026-09-30)

- **RDY-008** Capability eligibility · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-028 — This system decides when a capital-intensive capability becomes eligible under progressive capability activation (CAP-032). It uses the Global Capital Authority's capital figures and the evidence of RDY-002. Eligibility never exceeds the operator's authorizations (MODE-003, POL-011).

The owner kept this system as its own system (DEC-024, confirmed in [DEC-027](../decisions/DEC-027-part-2-open-questions.md)).

## Handoff Part 3 applied (2026-09-30)

New requirements from [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), cited as P3§N. Part 3 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 3 reconciliation](../traceability/part-3-reconciliation.md). Placement, duplicate, and conflict resolutions: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md).

### Capital-scaled capability

- **RDY-009** Capital-scaled capability · CONFIRMED REQUIREMENT · P3§352 — The platform must intelligently adapt its available capabilities to the actual resources and operating conditions of the account. The system must not treat $100 exactly the same operationally as $1,000, $10,000, or $100,000+ while pretending that the same execution opportunities, liquidity requirements, diversification, infrastructure capacity, or risk capacity exist. Instead, the system must understand capital + liquidity + risk capacity + market conditions + execution capacity + operational readiness + strategy requirements, and determine which capabilities are currently appropriate. This is a capability-scaling system.
- **RDY-010** Small capital is a first-class operating mode · CONFIRMED REQUIREMENT · P3§353 — A small account must not be treated as an inferior or broken version of the system. For example, $100 must still receive: opportunity scanning; risk controls; deterministic calculations; portfolio management; performance tracking; strategy evaluation; AI intelligence where economically justified; reconciliation; monitoring; security; auditability; capital protection. However, features requiring more capital should not be activated merely because the software technically supports them. The system should understand what is economically executable.
- **RDY-011** Feature and strategy requirements · SYSTEM REQUIREMENT · P3§354 — Each feature or strategy should define its requirements. Possible requirements include: minimum capital; maximum capital; minimum liquidity; minimum expected edge; minimum capital efficiency; required diversification; required reserve; required infrastructure; required venue access; required execution quality; required risk capacity; required operational readiness; required historical validation; required strategy maturity. The system evaluates: current state → feature requirements → eligibility engine → available capabilities. A feature may be: ENABLED; LIMITED; DEGRADED; DEFERRED; UNAVAILABLE; or REQUIRES REVIEW.
- **RDY-012** Automatic capability unlocking · CONFIRMED REQUIREMENT · P3§355 — As the account grows and operational conditions improve, the platform should automatically recognize when previously unavailable capabilities become viable. Example: $100 → small-capital strategies; $500 → additional strategies become economically viable; $1,000 → broader opportunity participation; $5,000 → additional diversification/capital allocation possibilities; $10,000+ → larger strategy universe where requirements permit. These are examples only; they are NOT hard-coded universal thresholds. The actual thresholds must be determined by: strategy economics; fees; slippage; liquidity; risk; capital requirements; market conditions; execution quality; policy; validation history. The system must not simply unlock features because a numerical balance crossed a fixed arbitrary threshold.
- **RDY-013** Capability scaling is multi-dimensional · CONSTRAINT · P3§356 — Capital alone must not determine system capability. The system should consider: capital; liquidity; risk capacity; market conditions; strategy readiness; execution quality; venue health; data quality; infrastructure capacity; AI resource capacity; operational readiness; policy permissions; compliance / account restrictions where applicable. More money does not automatically mean more risk. Instead: more resources + sufficient readiness + validated capability + authorized policy = possible capability expansion.
- **RDY-014** No artificial feature locking · CONFIRMED REQUIREMENT · P3§357 — The platform should not unnecessarily disable useful functionality simply because the account is small. If a feature can safely operate with small capital, it should remain available. The system should distinguish: technically available; economically useful; risk-appropriate; authorized; operationally ready.

### Canary readiness

- **RDY-015** Canary readiness factors · SYSTEM REQUIREMENT · P3§378, P3§379 — Canary deployment should be automatically eligible when the system determines that sufficient conditions exist. It must not simply activate because "there is enough money"; capital is one factor. In addition to the conditions of STR-013 and the evidence of RDY-002, canary readiness should consider: risk capacity; rollback readiness; venue health; deployment health. Conceptually: candidate version → validation → paper → readiness assessment → capital capacity → risk capacity → infrastructure health → rollback readiness → policy authorization → canary eligibility; only then canary.
- **RDY-016** Canary eligibility is not canary activation · CONSTRAINT · P3§381, P3§527 — The platform should be able to automatically recognize when a strategy/version becomes eligible for canary. However, eligibility is not identical to execution: a strategy can become eligible for canary, and activation still requires all required controls. The final transition must satisfy the approved deployment-control policy.

### Readiness states, blockers, and explanations

- **RDY-017** Component readiness states · SYSTEM REQUIREMENT · P3§383 — The platform should distinguish readiness from simple availability. A component can be: NOT_READY; READY_FOR_RESEARCH; READY_FOR_BACKTEST; READY_FOR_PAPER; READY_FOR_CANARY; READY_FOR_PRODUCTION; BLOCKED; SUSPENDED; DEGRADED; REQUIRES_REVIEW. The exact final state model must be established during architecture.
- **RDY-018** Blockers have reasons and are actionable · CONFIRMED REQUIREMENT · P3§384, P3§481 — BLOCKED should mean: a required condition prevents the system from safely proceeding. Examples: insufficient capital; missing dependency; failed validation; policy restriction; data quality failure; risk restriction; security issue; infrastructure failure; missing required approval; failed reconciliation; unsupported venue; insufficient liquidity. A blocker must have a reason. The system should never simply display BLOCKED without explaining: what; why; since when; which requirement; what dependency; what would remove the blocker. A blocker should identify what is missing. Examples: CANARY BLOCKED — reason: insufficient out-of-sample validation; required: complete required validation stage. ARBITRAGE BLOCKED — reason: Exchange B liquidity below strategy requirement; required: improved liquidity or strategy adjustment.
- **RDY-019** Readiness is explainable · CONFIRMED REQUIREMENT · P3§385 — For every major capability, the system should be able to answer "Why is this capability enabled?" or "Why is this capability blocked?". This should reference: policy; capital; risk; strategy; validation; dependencies; environment; infrastructure; security.

### Capability registry and self-awareness

- **RDY-020** Capability registry · SYSTEM REQUIREMENT · P3§411, P3§412 — The platform should maintain an internal understanding of: what features exist; what versions exist; what strategies exist; what policies exist; what dependencies exist; what services are active; what services are degraded; what capabilities are available; what capabilities are blocked; what requires review. This becomes the foundation for autonomous orchestration. The platform should maintain a canonical registry of system capabilities. Each capability may include: capability ID; version; owner; dependencies; requirements; capital requirements; risk requirements; environment requirements; status; readiness; permissions; feature flags; validation status.
- **RDY-021** Knowing what it can and cannot do · CONFIRMED REQUIREMENT · P3§413, P3§414 — The system should be able to determine: "I can execute this." "I can analyze this but cannot execute it." "I cannot safely execute this yet." "This requires more capital." "This requires better liquidity." "This requires additional validation." "This is blocked by policy." "This capability is currently degraded." This prevents false autonomy. Autonomy should include the ability to recognize: newly available opportunities; newly available strategies; newly available capital; newly available venues; newly available infrastructure; newly validated capabilities; and determine whether they can safely be used.

### Production readiness across dimensions

- **RDY-022** Readiness is not one boolean · CONFIRMED REQUIREMENT · P3§478, P3§479 — Production readiness must be evaluated across multiple dimensions. Examples: functional readiness; security readiness; data readiness; risk readiness; capital readiness; execution readiness; operational readiness; monitoring readiness; recovery readiness; deployment readiness; rollback readiness; documentation readiness; testing readiness. Avoid simplistic READY = TRUE/FALSE for the whole system. A platform may be trading READY but new strategy NOT READY; paper READY but production NOT READY; research READY but live execution BLOCKED.
- **RDY-023** Readiness matrix · SYSTEM REQUIREMENT · P3§480 — The platform should eventually expose a structured readiness matrix showing: system; capability; current state; blockers; dependencies; required action; owner; last validated; validation version.
- **RDY-024** Automatic readiness re-evaluation · CONFIRMED REQUIREMENT · P3§482 — Readiness should be recalculated when relevant conditions change. Examples: capital increases; liquidity improves; strategy validation completes; infrastructure recovers; an exchange returns; policy changes; data quality improves; risk limits change. The system should not require the user to manually rediscover eligibility.
- **RDY-025** Stable capability transitions · CONSTRAINT · P3§485, P3§486 — Capability scaling should not constantly oscillate because of tiny balance changes. The architecture should consider: hysteresis; stability windows; minimum meaningful changes; reservation state; pending settlements. The system should avoid ENABLE → DISABLE → ENABLE → DISABLE because of minor fluctuations. Capability transitions should be stable and explainable.

### Placement

- **RDY-026** Part 3's engines are parts of this system · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-031 — The Eligibility Engine (P3§354), the Canary Readiness Engine (P3§379), the capability registry (P3§412), and the readiness matrix (P3§480) are components of this system, not new systems. The capability registry references the Strategy Registry, the Policy System, System Health, and deployment records by identifier instead of copying their state. Eligibility and availability never exceed the operator's authorizations (RDY-008, PLT-023).

## Capability and readiness model (Part 3)

This section explains how the requirements above fit together. It adds no requirement.

**Four kinds of status, kept apart (DUP-32).** Part 3 and Part 2 use several status lists. They answer different questions, so they are not merged; one owner holds each.

| Question | Status set | Applies to | Owner |
|---|---|---|---|
| May this strategy version progress to its next lifecycle step? | RDY-004 readiness states (NOT_READY … PRODUCTION_ACTIVE, SUSPENDED, REJECTED) | Strategy versions | This system |
| Is this component ready for a given use? | RDY-017 component readiness (NOT_READY, READY_FOR_RESEARCH … READY_FOR_PRODUCTION, BLOCKED, SUSPENDED, DEGRADED, REQUIRES_REVIEW) | Components and capabilities, including system changes | This system |
| Is this capability available right now, and how much of it? | RDY-011 availability (ENABLED, LIMITED, DEGRADED, DEFERRED, UNAVAILABLE, REQUIRES REVIEW) | Capabilities in the capability registry | This system |
| Where is this feature in the repository's life? | The canonical feature lifecycle GOV-024 (IDEA … RETIRED, which replaced GOV-018) and GOV-009's deprecation statuses (ACTIVE … REPLACED) | Documented features | [Architecture governance](../architecture/architecture-governance.md) (documentation, not runtime) |

The lifecycle stage of a strategy version (STR-024) stays in the Strategy Registry (RDY-007). The final state models are fixed when DIRECTIONAL TRADING is planned, as RDY-004 and RDY-017 both allow.

**How a capability becomes available.**

```text
capital / conditions change (CAP-046) or any readiness input changes (RDY-024)
  → feature requirements (RDY-011, V-39)
  → multi-dimensional evaluation (RDY-013): capital, liquidity, risk capacity, market,
    strategy readiness, execution quality, venue health, data quality, infrastructure,
    AI capacity, operational readiness, policy permissions, account restrictions
  → stability check: hysteresis, windows, minimum change (RDY-025, V-37)
  → availability status (RDY-011) + blocker with reason and required action (RDY-018)
  → capability registry and readiness matrix (RDY-020, RDY-023)
```

**What never changes with capital.** Capital alone never unlocks a capability (RDY-013), never creates authorization (PLT-023), and never raises exposure limits on its own (CAP-034, CF-18). Eligibility is not activation (RDY-016): activating a canary or a live capability still needs the deployment-control policy (STR-014, STR-019 to STR-022) and the operator's maximum mode (MODE-003).

**Where the evidence comes from.** Part 3 adds venue health (Exchange Adapter Layer, EXA-015), deployment health and rollback readiness (Deployment and operational readiness, OPS-005, OPS-012), and capital states (Global Capital Authority, CAP-044) to the sources listed below. This system reads them; it recomputes none of them (RDY-006).

**The platform-level production-readiness model** (P3§541 item 23) uses RDY-022's dimensions and is described in [Deployment and operational readiness](../operations/deployment-and-operational-readiness.md).

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

- **Owns:** readiness states, the aggregation of readiness evidence, blocking conditions, and the automatic APPROVAL decision of STR-019; since Part 3, also the capability registry, capability availability, and the readiness matrix (RDY-020, RDY-023, RDY-026).
- **Consumes:** the evidence above, read-only; the eligibility policy and the human-controlled gates (V-28) from the Policy System.
- **Produces:** readiness verdicts, canary authorization (STR-013, STR-019), and readiness reporting (RDY-005) for the [daily report](../operations/daily-system-intelligence.md).
- **Must not:** be bypassed by AI or a human (STR-022); take AI output as a verdict (AI may provide analysis only, ARCH-022); recompute evidence that another system owns (RDY-006); authorize production from paper results alone (PAP-012).
- **Failure behavior:** missing or stale evidence means NOT_READY, never READY (RDY-003, PLT-018).
- **Not yet specified:** evidence thresholds per transition (policy values, V-33 in the [values register](../requirements/values-register.md), plus V-02 to V-05 for canary); per-feature requirements (V-39) and stability controls (V-37); the final state models (RDY-004, RDY-017); interfaces; tests.
