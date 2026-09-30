# Policy System (Persistent, Versioned Policy)

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-12 · **Category:** shared infrastructure · **Roadmap stage:** **not mapped by §95** (CF-06) · **Sources:** §29, §30 (also §02 items 5–6)
>
> Canonical location for policy per §98 (`docs/systems/policy/`). §98 also names `docs/product/trading-policy.md`; that file has not been created because its purpose is unclear (CF-08, OQ-15).

Canonical definition of how user rules are stored, versioned, and changed. The policy system is the policy **authority**. The [Natural Language Policy Interface](natural-language-policy-interface.md) is only a way into it (NLP-003).

## Policy is not AI memory

- **POL-001** User rules outside AI context · CONSTRAINT · §29 — Important user rules must not exist only inside an AI model's context or memory.
- **POL-002** Structured, persistent, versioned policy · CONFIRMED REQUIREMENT · §29 — They must be stored persistently in structured, versioned policy. This protects against: context loss; model drift; session changes; accidental omission; ambiguity; unauthorized changes.

## Versioning and change control

- **POL-003** Every meaningful change is a new version · CONFIRMED REQUIREMENT · §30 — Meaningful policy changes must create a new version (example: Policy v1.0, Policy v1.1, Policy v2.0).
- **POL-004** Change process · CONFIRMED REQUIREMENT · §30 — Important changes should follow: new instruction → interpretation → difference analysis → conflict check → risk analysis → simulation if required → confirmation if required → activation.

## How instructions become enforceable policy

Summary of the documents that define each step. No new rules are added here.

1. The user states objectives and restrictions in ordinary language (NLP-001, NLP-002).
2. The instruction is interpreted into structured policy, validated, and checked for conflicts and ambiguity. Ambiguity is surfaced, and interpretation is never silently made more permissive (NLP-004 to NLP-006).
3. The accepted change becomes a new policy version (POL-003, POL-004).
4. Deterministic systems enforce it. The [Risk Engine](../../risk/risk-engine.md) enforces user hard constraints second only to system safety (RSK-004). The [Global Capital Authority](../capital-management.md) applies user policy to allocation and reinvestment (CAP-006, CAP-011).

## Boundary (§92)

- **Owns:** the authoritative, versioned user policy.
- **Used by:** Risk Engine, Global Capital Authority, Recovery ("validate policy", REC-002), Trading Director ("policy" input, AGT-004), audit ("policy version", AUD-002).
- **Must not:** be replaced by AI memory (POL-001, MEM-004).
- **Not yet specified in Part 1:** the policy schema, which changes count as "important", when simulation or confirmation is "required" (OQ-17), who confirms, interfaces, tests.

## Findings

- CF-06: the Risk Engine (CORE TRADING FOUNDATION) depends on user hard constraints, but §95 maps policy only through the NL interface in the later AI INTELLIGENCE stage.
- CF-08 and OQ-15: §98 gives two canonical locations for policy.
- DUP-22: AI memory also lists "policy history" (MEM-002).
