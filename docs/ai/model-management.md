# Model Routing, Model Evaluation and AI Cost

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **Systems:** SYS-24 Model Router, SYS-25 AI Cost Manager, SYS-26 Model Evaluation · **Roadmap stage:** AI INTELLIGENCE ("Model router", "AI cost management"; model evaluation placed there by [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) · **Sources:** §61–§63

Canonical definition of how the platform chooses whether and which AI to use, how it evaluates models, and how it tracks AI cost. In the §54 roster, "Model Evaluation Agent" and "AI Cost Manager" appear as AI agents. They are implemented as deterministic services, not agents (TC-02, [DEC-013](../decisions/DEC-013-ai-organization.md)).

## Model evaluation

- **MEV-001** Evaluation dimensions · SYSTEM REQUIREMENT · §61 — Evaluate: accuracy; reliability; calibration; cost; latency; failure patterns; hallucination frequency; task suitability.
- **MEV-002** Model performance is not profitability · CONSTRAINT · §61 — Do not confuse model performance with trading profitability.

This is the measurement of "model health" as defined in PFC-005.

## AI cost management

- **COST-001** What the AI Cost Manager monitors · SYSTEM REQUIREMENT · §62 — Monitor: API usage; cost per task; cost per model; cost per event; budget utilization; model routing; excessive calls; repeated calls; unnecessary premium-model usage.

## Model routing

- **RTR-001** Routing tiers · SYSTEM REQUIREMENT · §63 — The Model Router determines whether a task requires: no AI, low-cost AI, or premium AI.
- **RTR-002** Routing factors · SYSTEM REQUIREMENT · §63 — Consider: task difficulty; financial consequence; context complexity; reliability; current model performance; cost; latency; budget; expected value.

## Decisions applied (2026-09-30)

- **MEV-003** Model Evaluation is deterministic · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-013 — Model Evaluation is a deterministic measurement service, not an AI agent.
- **COST-002** AI Cost Manager is deterministic · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-013 — The AI Cost Manager is a deterministic service. It sets the budgets and limits that the AI gateway enforces (AIL-006).
- **RTR-003** Deterministic routing · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-013 — The Model Router is deterministic: it applies rules over the RTR-002 factors and never calls an LLM to decide a route.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **RTR-004** Additional routing factors · SYSTEM REQUIREMENT · P2§13, P2§206 — In addition to the factors in RTR-002, the Model Router considers: quality requirement; availability; historical performance. The architecture must support multiple providers and models and must not hard-code one model throughout the system.
- **RTR-005** Task-specific, auditable selection · CONFIRMED REQUIREMENT · P2§14, P2§207 — Selection proceeds: task → classification → quality requirement → risk / consequence → available models → quality / cost / latency / reliability → model selection. The routing decision must be deterministic and auditable. Simple tasks should not automatically consume premium models.
- **MEV-004** Additional evaluation metrics and history · SYSTEM REQUIREMENT · P2§15, P2§208 — Models must be measured rather than trusted based solely on reputation. In addition to the dimensions in MEV-001, possible metrics include: validation success; structured-output compliance; useful contribution; evidence compliance. Historical results should be retained.

Part 2 lists "Model Evaluation Agent" and "AI Cost Manager" among the AI roles (P2§6). They stay deterministic services (MEV-003, COST-002; [DEC-013](../decisions/DEC-013-ai-organization.md)), and the "AI analysis" of model evaluation in P2§339 is done by the Performance Analyst (AGT-014). See the role mapping in [agents](agents.md#roles-and-who-performs-them-handoff-part-2).

## Boundary (§92)

- **Model Router uses:** model evaluation results ("current model performance") and cost and budget data from the AI Cost Manager ([DEC-013](../decisions/DEC-013-ai-organization.md)).
- **Not yet specified:** providers and models (AIL-007), budget values (operator policy), routing rule details, interfaces, tests.

## Findings (all resolved)

TC-02 → [DEC-013](../decisions/DEC-013-ai-organization.md) (MEV-003, COST-002, RTR-003). DUP-15 → [DEC-013](../decisions/DEC-013-ai-organization.md): evaluation and cost are measurement services that feed the router.
