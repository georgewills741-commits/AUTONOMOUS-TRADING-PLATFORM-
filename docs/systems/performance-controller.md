# Performance Controller (Expected vs Actual)

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-21 · **Category:** shared infrastructure (§49 is platform-wide) · **Roadmap stage:** ARBITRAGE ("Performance controller"), although it serves all strategies (CF-05) · **Sources:** §48–§50

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

## Boundary (§92)

- **Owns:** the comparison of expected against actual results, and deterioration detection (PFC-002, PFC-003).
- **Consumes:** expected values (e.g. from the [True Net-Profit Engine](true-net-profit-engine.md)), actual outcomes (execution, portfolio), and the [arbitrage opportunity database](arbitrage/arbitrage-intelligence.md) (ARB-004).
- **Must not:** take actions outside deterministic policy (PFC-004).
- **Not yet specified:** detection thresholds (operator policy), interfaces, tests. Permitted actions are PFC-008.

## Findings (all resolved)

DUP-03 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (PFC-006). DUP-14 → [DEC-013](../decisions/DEC-013-ai-organization.md) (PFC-007). CF-05 → [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md) (built in ARBITRAGE, platform-wide, before any live operation).
