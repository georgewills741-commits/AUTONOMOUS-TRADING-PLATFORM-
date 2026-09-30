# Model Routing, Model Evaluation and AI Cost

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **Systems:** SYS-24 Model Router, SYS-25 AI Cost Manager, SYS-26 Model Evaluation · **Roadmap stage:** AI INTELLIGENCE ("Model router", "AI cost management"); model evaluation is not listed in §95 (CF-05) · **Sources:** §61–§63

Canonical definition of how the platform chooses whether and which AI to use, how it evaluates models, and how it tracks AI cost. In the §54 roster, "Model Evaluation Agent" and "AI Cost Manager" appear as AI agents. Whether they should be AI at all is TC-02.

## Model evaluation

- **MEV-001** Evaluation dimensions · SYSTEM REQUIREMENT · §61 — Evaluate: accuracy; reliability; calibration; cost; latency; failure patterns; hallucination frequency; task suitability.
- **MEV-002** Model performance is not profitability · CONSTRAINT · §61 — Do not confuse model performance with trading profitability.

This is the measurement of "model health" as defined in PFC-005.

## AI cost management

- **COST-001** What the AI Cost Manager monitors · SYSTEM REQUIREMENT · §62 — Monitor: API usage; cost per task; cost per model; cost per event; budget utilization; model routing; excessive calls; repeated calls; unnecessary premium-model usage.

## Model routing

- **RTR-001** Routing tiers · SYSTEM REQUIREMENT · §63 — The Model Router determines whether a task requires: no AI, low-cost AI, or premium AI.
- **RTR-002** Routing factors · SYSTEM REQUIREMENT · §63 — Consider: task difficulty; financial consequence; context complexity; reliability; current model performance; cost; latency; budget; expected value.

## Boundary (§92)

- **Model Router uses:** model evaluation results ("current model performance") and cost and budget data (inferred from RTR-002).
- **Not yet specified in Part 1:** AI providers and models (OQ-16), budgets, routing rules, interfaces, tests.

## Findings

- TC-02: model evaluation and cost monitoring are measurement and accounting that deterministic software can do. Making them AI agents would conflict with QNT-003 and constitution Rules 87 and 201. The Model Router is in the same position.
- DUP-15: cost appears in MEV-001, COST-001, and RTR-002; model performance appears in MEV-001 and RTR-002; routing appears in COST-001 and RTR-001.
