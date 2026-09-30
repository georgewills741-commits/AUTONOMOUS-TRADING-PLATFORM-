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

## Boundary (§92)

- **Owns:** the comparison of expected against actual results, and deterioration detection (PFC-002, PFC-003).
- **Consumes:** expected values (e.g. from the [True Net-Profit Engine](true-net-profit-engine.md)), actual outcomes (execution, portfolio), and the [arbitrage opportunity database](arbitrage/arbitrage-intelligence.md) (ARB-004).
- **Must not:** take actions outside deterministic policy (PFC-004).
- **Not yet specified in Part 1:** detection thresholds, the list of permitted actions, interfaces, tests.

## Findings

- DUP-03: Arbitrage Intelligence (ARB-001) and both arbitrage systems also list the performance controller and expected-vs-actual analysis.
- DUP-14: the Performance Analyst agent (AGT-014) also evaluates deterioration and expected-vs-actual results. The PROPOSED split is deterministic detection here and AI interpretation in the agent.
- CF-05: mapped to the ARBITRAGE stage but platform-wide.
