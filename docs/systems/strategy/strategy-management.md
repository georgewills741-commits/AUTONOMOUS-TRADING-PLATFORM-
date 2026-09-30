# Strategy Management (Lifecycle, Strategy Factory, Versioning)

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-14 · **Category:** shared infrastructure ("Strategy lifecycle", §04) · **Roadmap stage:** DIRECTIONAL TRADING ("Strategy lifecycle"), although it serves all trading systems (CF-05) · **Sources:** §34–§38

Canonical definition of how strategies are researched, validated, promoted, versioned, improved, and retired, and of what research may and may not touch.

## Lifecycle and promotion

- **STR-001** Strategy lifecycle · CONFIRMED REQUIREMENT · §34 — Research → strategy specification → backtest → validation → out-of-sample / walk-forward → stress / robustness → paper → approval → canary → production.
- **STR-002** No AI shortcut through stages · CONSTRAINT · §34 — No strategy bypasses required stages because an AI recommends it.

## Strategy Factory

- **STR-003** Strategy Factory responsibilities · SYSTEM REQUIREMENT · §35 — Research; hypothesis generation; candidate creation; backtesting; validation; robustness; paper testing; comparison; versioning; promotion; retirement.
- **STR-004** Factory cannot touch live trading · CONSTRAINT · §35 — It must not directly modify live trading.

## Versioning

- **STR-005** Every meaningful change is a new version · CONFIRMED REQUIREMENT · §36 — Every meaningful strategy change creates a new version (examples: Directional Trend v1.0, v1.1, v2.0).
- **STR-006** No silent production changes · CONSTRAINT · §36 — Active production strategies must never be silently modified.

## Research / production separation

- **STR-007** What research may do · CONFIRMED ARCHITECTURAL PRINCIPLE · §37 — Research may: analyze history; generate hypotheses; create candidate strategies; backtest; stress-test; paper-test.
- **STR-008** What research must not touch · CONSTRAINT · §37 — Research must not directly modify: live strategies; production risk limits; exchange credentials; execution logic; user hard constraints; kill switches.

## Controlled improvement

- **STR-009** Improvement path · CONFIRMED REQUIREMENT · §38 — When a strategy deteriorates: performance deterioration → investigation → research → hypothesis → new strategy version → backtest → out-of-sample → robustness → paper → approval → canary → production.
- **STR-010** Forbidden reaction to losses · CONSTRAINT · §38 — Never: loss → AI changes live strategy → risk increases.

## Decisions applied (2026-09-30)

- **STR-011** Canary · DEPRECATED / REPLACED · DEC-015 — In canary, a newly approved strategy version trades live with a capped capital allocation and tightened risk limits, for a minimum period and trade count. Promotion to production requires expected-vs-actual results within tolerance and no safety incidents. A breach suspends the version or rolls back to the previous one. Initial operator-configurable defaults: capital cap of 5% of the strategy's target allocation; minimum 14 days and 50 trades.
- **STR-012** The Strategy Factory owns the research process · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — The Strategy Factory owns and coordinates the research process, including "research coordination" (§51). AI agents assist inside it.

## Owner correction applied (OC-1, [DEC-019](../../decisions/DEC-019-company-grade-autonomous-operating-model.md))

STR-011 (canary: 5% for 14 days and 50 trades) is replaced by STR-013 to STR-018. Its values are withdrawn (V-01 to V-03 in the [values register](../../requirements/values-register.md)).

- **STR-013** Evidence-based canary readiness · CONFIRMED REQUIREMENT · DEC-019 — A candidate strategy version becomes eligible for canary only when the system verifies: backtest; out-of-sample; walk-forward; stress test; robustness; paper trading; risk validation; policy validation; operational validation; capital availability; liquidity availability; market/regime compatibility; system health; then canary authorization. Capital availability is one condition, not the only one.
- **STR-014** Automatic canary entry · CONFIRMED REQUIREMENT · DEC-019 — When all readiness conditions are verified, the platform automatically enters canary operation, without waiting for manual activation, unless policy designates that gate as human-controlled (PLT-014).
- **STR-015** Dynamic canary allocation · CONFIRMED REQUIREMENT · DEC-019 — The initial canary allocation is determined within policy-defined limits, based on factors such as: available capital; target capital; strategy risk; portfolio exposure; liquidity; expected opportunity frequency; historical validation quality; strategy confidence; market regime; capital efficiency; existing portfolio correlation; current system risk. It must always remain within hard risk limits. No universal fixed percentage is used.
- **STR-016** Gradual scaling · CONSTRAINT · DEC-019 — A successful canary progresses through controlled allocation stages: small initial allocation → observe → validate live performance → check expected vs actual → check risk → check execution → check slippage → check drawdown → check stability → increase allocation → revalidate → next allocation stage → full authorized deployment. The allocation never jumps from canary to full capital without passing the required gates.
- **STR-017** Automatic canary stop · CONFIRMED REQUIREMENT · DEC-019 — If a canary deteriorates, the platform automatically: stops allocation increases; reduces exposure where policy requires; suspends the strategy; rolls back the strategy version; returns capital to the appropriate reserve; records the event; analyses expected vs actual performance. This must not require an AI agent to improvise the response.
- **STR-018** Evidence, not time alone · CONSTRAINT · DEC-019 — Readiness is evidence-based and risk-based. A strategy does not become production-ready merely because time has passed, and is not rejected merely for not reaching an arbitrary number of days when all required evidence is otherwise sufficient. Time and trade count may be used as evidence requirements.

## Owner decisions applied (CF-11 to CF-13, 2026-09-30)

- **STR-019** Autonomous approval by the Governance and Readiness Engine · CONFIRMED REQUIREMENT · DEC-023 — The lifecycle APPROVAL stage (STR-001, STR-009) is performed automatically by the platform's deterministic Governance and Readiness Engine when all mandatory readiness, risk, validation, capital, data-integrity, liquidity, execution, and operational checks pass. A strategy may enter canary automatically only when it satisfies the defined eligibility policy and sufficient capital is available.
- **STR-020** Deterministic canary controls · CONFIRMED REQUIREMENT · DEC-023 — The canary allocation, exposure limits, duration, and promotion criteria are enforced by deterministic controls.
- **STR-021** Human approval only where policy requires · CONFIRMED REQUIREMENT · DEC-023 — Human approval is required only when policy explicitly marks a deployment as requiring human authorization, such as a brand-new strategy class, a material risk-model change, an exceptional capital increase, a security-sensitive change, or any unresolved governance exception.
- **STR-022** Gates cannot be bypassed · CONSTRAINT · DEC-023 — No AI agent or human may bypass the deterministic safety gates. Failure of any mandatory gate prevents canary deployment and places the strategy into a blocked / readiness-failed state until the required conditions are satisfied.

The Governance and Readiness Engine is a component of this system (SYS-14), not a separate system ([DEC-023](../../decisions/DEC-023-autonomous-canary-approval.md)). It issues the "canary authorization" named in STR-013.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../../decisions/DEC-024-part-2-reconciliation.md).

- **STR-023** Strategy Registry · SYSTEM REQUIREMENT · P2§20, P2§210 — Every strategy should have a canonical identity in the Strategy Registry. At minimum: strategy ID; version; description; objective; applicable markets; applicable regimes; risk profile; parameters; dependencies; validation history; status; creation timestamp; approval status; retirement status.
- **STR-024** Lifecycle states · SYSTEM REQUIREMENT · P2§20 — The lifecycle may include the states: DRAFT; RESEARCH; BACKTESTED; VALIDATING; PAPER; APPROVED; CANARY; PRODUCTION; SUSPENDED; RETIRED.
- **STR-025** Strategy version immutability · CONSTRAINT · P2§21, P2§211 — Once used for important production decisions, a strategy version must remain reconstructable. Parameter changes must create a new version. Historical versions must not be silently rewritten.
- **STR-026** Experiment reproducibility · CONFIRMED REQUIREMENT · P2§119 — Experiments should record: dataset version; code version; strategy version; parameters; model/version; configuration; random seeds where applicable; environment; results. A historical experiment should be reproducible as closely as technically possible.

Notes:

- **One lifecycle.** Part 2 describes the lifecycle in five places (P2§19 Strategy Factory, §68 paper → readiness → canary → production, §107 controlled self-improvement, §209, §317). Each is a view of STR-001 and STR-009 at a different level of detail, not a second lifecycle (DUP-29). Part 2's "READINESS REVIEW" is the APPROVAL stage of STR-001.
- **Governance and Readiness Engine.** It is now registered as its own system, SYS-34 [Readiness System](../readiness-system.md), because Part 2 makes it a canonical authority that aggregates evidence from many systems and covers system changes as well as strategies ([DEC-024](../../decisions/DEC-024-part-2-reconciliation.md), DUP-24). STR-019 to STR-022 stay here: they govern this lifecycle's APPROVAL stage, which that system performs.
- **Lifecycle state vs readiness.** This system's Strategy Registry records which lifecycle stage a strategy version is in (STR-024). The Readiness System records whether the evidence allows it to progress (RDY-004, RDY-007).
- The Strategy Registry is the canonical registry of ARCH-027.

## Boundary (§92)

- **Owns:** strategy versions, lifecycle state, promotion, and retirement.
- **Uses:** [Backtesting](backtesting.md) and [Paper Trading](paper-trading.md) as lifecycle stages; AI research agents as assistants ([agents](../../ai/agents.md), AGT-012, AGT-013).
- **Must not:** modify live trading directly (STR-004), or let research change protected production controls (STR-008).
- **Not yet specified:** validation thresholds for each lifecycle stage (expected with Part 2 verification architecture), interfaces, tests. The operator approves promotions; canary is STR-011.

## Findings

All resolved. DUP-18 → DEC-011 (STR-012). DUP-20 → DEC-011 (DIR-004). OQ-09 → DEC-015 (STR-011, since replaced). CF-05 → DEC-016. CF-13 → [DEC-023](../../decisions/DEC-023-autonomous-canary-approval.md) (STR-019 to STR-022).
