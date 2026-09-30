# AI Output Validation (Hallucination Firewall, Output Contract, Multi-Agent Validation, Calibration)

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-22 (components of the AI Intelligence Layer) · **Roadmap stage:** AI INTELLIGENCE ("Hallucination Firewall", "Multi-agent validation"); structured output and confidence calibration placed there by [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md) · **Sources:** §64–§67

Canonical definition of how AI output is checked before anything deterministic acts on it.

## Hallucination Firewall

- **AIV-001** Evidence references · CONFIRMED REQUIREMENT · §64 — Important AI claims should reference: data source; timestamp; dataset; calculation; event; evidence identifier.
- **AIV-002** Mark unverifiable claims · CONFIRMED REQUIREMENT · §64 — If evidence cannot be verified, the claim is marked UNVERIFIED.
- **AIV-003** Unverified claims are not evidence · CONSTRAINT · §64 — Unverified claims cannot become factual trading evidence.

## Structured AI output contract

- **AIV-004** Machine-validated output · CONFIRMED REQUIREMENT · §65 — AI output must be machine-validated.
- **AIV-005** Conceptual output schema · SYSTEM REQUIREMENT · §65 — Decision: BUY / SELL / HOLD / NO_TRADE; Confidence: 0–100; Evidence: []; Invalidation: []; RiskObservations: []; Strategy: ID + VERSION; Reasoning: structured explanation.
- **AIV-006** Reject malformed output · CONSTRAINT · §65 — Malformed or incomplete output must be rejected.

## Multi-agent validation

- **AIV-007** Validation chain for important decisions · CONFIRMED ARCHITECTURAL PRINCIPLE · §66 — For important decisions: market analysis → quantitative analysis → Trading Director → Devil's Advocate → deterministic Risk Engine.
- **AIV-008** Validation policy options · SYSTEM REQUIREMENT · §66 — Possible policies: single-agent analysis; multi-agent agreement; mandatory Devil's Advocate; premium confirmation; no trade on unresolved disagreement.
- **AIV-009** Risk remains authoritative · CONSTRAINT · §66 — Risk remains authoritative.

## Confidence calibration

- **AIV-010** Confidence is not probability · CONSTRAINT · §67 — AI confidence must not automatically be interpreted as probability.
- **AIV-011** Compare confidence with outcomes · CONFIRMED REQUIREMENT · §67 — Compare AI confidence against observed outcomes.
- **AIV-012** Responses to overconfidence · SYSTEM REQUIREMENT · §67 — If systematic overconfidence occurs, the system may: require stronger evidence; require additional validation; route to another model; reduce the model's role; suspend the model for that task.

## Decisions applied (2026-09-30)

- **AIV-013** Decision values · CONFIRMED REQUIREMENT · DEC-013 — The Decision field allows BUY, SELL, HOLD, NO_TRADE, WAIT, UNCERTAIN, and INSUFFICIENT_EVIDENCE. AI may also recommend REDUCE_RISK or SUSPEND_STRATEGY, as proposals for deterministic systems to evaluate.
- **AIV-014** Validation policy · CONFIRMED REQUIREMENT · DEC-013 — Every AI-originated trade proposal gets a mandatory Devil's Advocate review, and unresolved disagreement means NO TRADE. Premium-model confirmation is required when the proposal's capital at risk exceeds an operator-configured threshold.
- **AIV-015** Important decisions · CONFIRMED REQUIREMENT · DEC-013 — The important decisions of AIV-007 are: every AI-originated trade proposal; every AI-proposed strategy change; every AI interpretation of policy that would loosen a constraint.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **AIV-016** Deterministic validation chain for AI proposals · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§5, P2§199 — The fundamental interaction is: AI → proposal → structured output → schema validation → policy validation → risk validation → capital validation → execution validation → deterministic decision. AI cannot skip deterministic validation.
- **AIV-017** Claim types kept distinct · CONSTRAINT · P2§8, P2§202 — Material AI claims should be evidence-backed. The system must distinguish observed fact, AI interpretation, AI hypothesis, and decision proposal. These must never be represented as equivalent.
- **AIV-018** Additional evidence fields · CONFIRMED REQUIREMENT · P2§8 — In addition to the references in AIV-001, material claims should reference, where applicable, the market, the venue, and the dataset version.
- **AIV-019** Handling unsupported material claims · SYSTEM REQUIREMENT · P2§9, P2§203 — For material claims: claim → evidence → source → timestamp → validation. If evidence cannot be established where evidence is required: mark the claim unsupported; reject it where necessary; request more evidence; enter WAIT / NO TRADE where appropriate.
- **AIV-020** Disagreement is a supported state · CONSTRAINT · P2§11, P2§205 — AI disagreement must be a supported state: disagreement increases uncertainty and leads to additional validation or WAIT / NO TRADE. Artificial consensus must not be manufactured merely to generate a trade.

Part 2's "unsupported" claim is the UNVERIFIED claim of AIV-002; the name UNVERIFIED is kept ([glossary](../glossary.md)). P2§10 (multi-agent validation; "AI agreement cannot override deterministic safety") is already AIV-007, AIV-008, AIV-009, and AIV-014. AIV-016's order (schema → policy → risk → capital → execution) is consistent with the runtime order of [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md), in which the Risk Engine authorizes before capital is reserved.

## Findings (all resolved)

CF-04 and OQ-12 → [DEC-013](../decisions/DEC-013-ai-organization.md) (AIV-013, RSK-014; arbitrage never uses AI proposals, ARB-013). OQ-18 → [DEC-013](../decisions/DEC-013-ai-organization.md) (AIV-014, AIV-015). TC-06 → [DEC-013](../decisions/DEC-013-ai-organization.md) (MKD-005).
