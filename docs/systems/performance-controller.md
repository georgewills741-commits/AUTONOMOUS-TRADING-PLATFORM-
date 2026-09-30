# Performance Controller (Expected vs Actual)

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-21 · **Category:** shared infrastructure (§49 is platform-wide) · **Roadmap stage:** ARBITRAGE ("Performance controller"), although it serves all strategies (CF-05) · **Sources:** §48–§50

Canonical definition of comparing expected with actual results, detecting deterioration, and keeping model health separate from strategy health.

## Expected vs actual

- **PFC-001** Expected-vs-actual comparison · CONFIRMED REQUIREMENT · §48 — Compare expected versus actual: profitability; fees; slippage; execution price; latency; fill rate; liquidity; rebalancing cost; strategy performance. This is particularly important for arbitrage.

## Performance controller

- **PFC-002** Continuous comparison · SYSTEM REQUIREMENT · §49 — The platform should continuously compare actual results against expected behavior.
- **PFC-003** What it detects · SYSTEM REQUIREMENT · §49 — It should detect: strategy deterioration; execution degradation; unexpected fees; increasing slippage; reduced liquidity; opportunity-quality deterioration; model degradation; exchange degradation; infrastructure degradation.
- **PFC-004** Only policy-permitted actions · CONSTRAINT · §49 — The controller should recommend or trigger only actions permitted by deterministic policy.

## Model health vs strategy health

- **PFC-005** Two separate kinds of health · CONFIRMED ARCHITECTURAL PRINCIPLE · §50 — These are separate. Model health: AI model reliability, cost, latency, calibration, hallucination rate, and task performance. Strategy health: trading strategy effectiveness under market conditions. A healthy model does not imply a healthy strategy. A healthy strategy does not imply a healthy AI model.

Model health is measured by [Model Evaluation](../ai/model-management.md) (MEV-001). Strategy health feeds [Strategy Management](strategy/strategy-management.md)'s controlled improvement path (STR-009).

## Decisions applied (2026-09-30)

- **PFC-006** One platform-wide controller · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This is the single performance controller for every strategy. Arbitrage systems supply expected values and the opportunity database.
- **PFC-007** Detection here, interpretation by the analyst · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-013 — Deterministic detection happens here. The Performance Analyst agent interprets results and attributes causes (AGT-015).
- **PFC-008** Permitted actions · CONFIRMED REQUIREMENT · DEC-012 — Under deterministic policy, the controller may raise alerts, propose suspending a strategy, activate a kill switch when a configured rule fires (RSK-009), and trigger recalibration of cost estimates (TNP-022). It cannot change strategies, limits, or policy.

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

The controller's detection scope (PFC-003) includes the performance and latency degradation of PERF-011. The reference to RSK-009 in PFC-008 now resolves to RSK-021 to RSK-025 ([DEC-021](../decisions/DEC-021-kill-switch-recovery.md)); a kill switch this controller activates follows their recovery rules. The resulting restrictions are applied by the Risk Engine's safety levels (RSK-015), within PFC-004 and PFC-008.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **PFC-009** Strategy drift · SYSTEM REQUIREMENT · P2§42 — The platform should monitor whether production behavior is diverging from validated strategy behavior. Possible dimensions: win/loss distribution; execution quality; slippage; opportunity frequency; regime distribution; latency; P&L distribution; risk behavior. Significant drift should trigger review or controlled suspension.
- **PFC-010** Paper expected-vs-observed · SYSTEM REQUIREMENT · P2§63 — The platform should compare expected vs observed paper results. Examples: expected fill price vs observed simulated fill; expected vs observed slippage; expected profitability vs realized paper profitability; expected vs observed opportunity frequency; expected vs observed execution latency; expected vs observed strategy behavior.
- **PFC-011** Expected values, variance, and cause · CONFIRMED REQUIREMENT · P2§74 — The platform should retain expected values before execution where possible, then compare: expected → actual → variance → cause. Potential causes: slippage; latency; liquidity; fee changes; market movement; strategy assumptions; data quality; execution failure.
- **PFC-012** Missed-opportunity analysis · SYSTEM REQUIREMENT · P2§75 — The platform should preserve opportunities that were not executed when measurable. Reasons may include: risk rejection; capital unavailable; policy restriction; insufficient net profit; liquidity; latency; exchange degradation; AI uncertainty; execution uncertainty. Later analysis may determine whether the rejection was appropriate.
- **PFC-013** False-opportunity analysis · SYSTEM REQUIREMENT · P2§76 — The system should analyze opportunities that appeared attractive but failed to produce expected economics, to detect: poor models; bad assumptions; data problems; slippage underestimation; liquidity errors; strategy degradation.
- **PFC-014** Arbitrage performance tracking · SYSTEM REQUIREMENT · P2§95, P2§224 — For arbitrage, track: expected opportunities; executed opportunities; net profitability; failed opportunities; slippage; execution latency; rebalancing costs; inventory efficiency; expected vs actual. Deterioration may trigger throttling, suspension, review, or recalibration, not uncontrolled live strategy rewriting.
- **PFC-015** Four-way arbitrage comparison · SYSTEM REQUIREMENT · P2§98 — The arbitrage subsystem should compare: theoretical vs expected executable vs paper observed vs live observed. This helps detect unrealistic arbitrage assumptions.

Notes:

- **Actions.** The controller still acts only through PFC-008: it raises alerts, proposes suspension, trips a configured kill switch, and triggers recalibration. Throttling (PFC-014) and controlled suspension (PFC-009) are applied by the Risk Engine through safety levels (RSK-015) or by Strategy Management, never by rewriting a live strategy (STR-010).
- **Preserved opportunities** (PFC-012) are records in the Opportunity Database (OPP-014, OPP-015). Interpreting causes is the Performance Analyst's work (AGT-015, AGT-021).
- **Stage (CF-16).** Paper evidence and the Readiness System, both built in DIRECTIONAL TRADING, need the expected-vs-actual comparison. That core (PFC-001 to PFC-003, PFC-009 to PFC-013) is therefore built in DIRECTIONAL TRADING. The arbitrage-specific tracking (PFC-014, PFC-015) stays in ARBITRAGE ([DEC-024](../decisions/DEC-024-part-2-reconciliation.md)).

## Boundary (§92)

- **Owns:** the comparison of expected against actual results, and deterioration detection (PFC-002, PFC-003).
- **Consumes:** expected values (e.g. from the [True Net-Profit Engine](true-net-profit-engine.md)), actual outcomes (execution, portfolio), and the [arbitrage opportunity database](arbitrage/arbitrage-intelligence.md) (ARB-004).
- **Must not:** take actions outside deterministic policy (PFC-004).
- **Not yet specified:** detection thresholds (operator policy), interfaces, tests. Permitted actions are PFC-008.

## Findings (all resolved)

DUP-03 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (PFC-006). DUP-14 → [DEC-013](../decisions/DEC-013-ai-organization.md) (PFC-007). CF-05 → [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md) (built in ARBITRAGE, platform-wide, before any live operation).
