# Natural Language Policy Interface

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-13 (an interface into SYS-12 Policy System) · **Category:** AI-assisted interface · **Roadmap stage:** AI INTELLIGENCE · **Sources:** §28

Canonical definition of how the user expresses objectives, restrictions and preferences in ordinary language, and how those statements become structured policy.

## Requirements

- **NLP-001** Built-in natural-language interface · CONFIRMED REQUIREMENT · §28 — The platform should provide a built-in Natural Language Policy Interface through which the user can express trading objectives, restrictions, preferences, and instructions in ordinary language.
- **NLP-002** Instruction categories · SYSTEM REQUIREMENT · §28 — Example categories: Objectives ("What am I trying to achieve?"); Restrictions ("What must the system never do?"); Capital authorization ("How much capital may the system use?"); Venue authorization ("Which exchanges may be used?"); Risk preferences ("What level of exposure is permitted?"); Operating preferences ("How should the system behave within those boundaries?").
- **NLP-003** Interface, not authority · CONFIRMED ARCHITECTURAL PRINCIPLE · §28 — The Natural Language Policy Interface is an interface into the policy system, not the policy authority itself.
- **NLP-004** Interpretation pipeline · CONFIRMED ARCHITECTURAL PRINCIPLE · §28 — User natural language → policy interpretation → structured policy → validation → conflict / ambiguity check → policy version → deterministic enforcement.
- **NLP-005** Never silently more permissive · CONSTRAINT · §28 — The LLM must never silently reinterpret an important instruction into a more permissive policy.
- **NLP-006** Surface ambiguity · CONFIRMED REQUIREMENT · §28 — Ambiguous instructions must be surfaced.

## Boundary (§92)

- **Owns:** turning natural language into a *proposed* structured policy change.
- **Hands off to:** the [Policy System](policy-system.md), which versions and activates the change (POL-003, POL-004).
- **Must not:** activate policy by itself (NLP-003) or widen permissions without surfacing it (NLP-005).
- **AI controls that apply:** the [AI hard-safety boundary](../../ai/ai-architecture.md) and [structured, validated output](../../ai/ai-output-validation.md).
- **Not yet specified in Part 1:** the user-facing channel, confirmation flow, how to fall back when the LLM is unavailable (HLT-005), interfaces, tests.
