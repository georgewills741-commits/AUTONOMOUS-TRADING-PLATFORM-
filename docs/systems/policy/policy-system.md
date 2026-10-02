# Policy System (Persistent, Versioned Policy)

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-12 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ([DEC-016](../../decisions/DEC-016-roadmap-stage-placement.md)) · **Sources:** §29, §30 (also §02 items 5–6)
>
> Canonical location for policy per §98 (`docs/systems/policy/`). §98 also names `docs/product/trading-policy.md`. It is deliberately not created: the operator's policy exists only in this system's runtime store (POL-009, [DEC-015](../../decisions/DEC-015-modes-canary-and-policy-governance.md)).

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
4. Deterministic systems enforce it. The [Risk Engine](../../risk/risk-engine.md) enforces user hard constraints below system safety and security (RSK-004, RSK-049: the owner ranked security controls above the user's hard policy, [DEC-035](../../decisions/DEC-035-owner-decisions-part-3-findings.md)). The [Global Capital Authority](../capital-management.md) applies user policy to allocation and reinvestment (CAP-006, CAP-011).

## Decisions applied (2026-09-30)

- **POL-005** Important changes need confirmation · CONFIRMED REQUIREMENT · DEC-015 — A policy change is important if it loosens a limit or restriction; increases authorized capital, leverage, or venues; moves a strategy to a more permissive operating mode; or changes a hard constraint. An important change requires the operator's explicit confirmation after seeing the difference, the conflict check, and the risk analysis.
- **POL-006** Simulation before loosening · CONFIRMED REQUIREMENT · DEC-015 — Simulation (a replay over recent market data, or a paper run) is required before activating a change that loosens risk limits or increases capital or leverage.
- **POL-007** Tightening changes activate immediately · CONFIRMED REQUIREMENT · DEC-015 — Changes that only reduce risk may activate immediately without confirmation; they are still versioned and audited.
- **POL-008** Operating mode is policy · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-015 — This system owns the platform-wide maximum operating mode and each strategy's mode. A mode change is a policy change.
- **POL-009** Single location of policy · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-015 — The operator's actual policy exists only in this system's versioned store. No repository document holds policy content.
- **POL-010** Structured editing before the NL interface · CONFIRMED REQUIREMENT · DEC-015 — Until the Natural Language Policy Interface exists, the operator edits structured policy directly through a validated operator interface, under the same versioning and change rules.

## Owner correction applied (OC-1, [DEC-019](../../decisions/DEC-019-company-grade-autonomous-operating-model.md))

- **POL-011** Autonomy boundaries are policy · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-019 — The Policy System holds the boundaries within which the platform acts autonomously: rebalancing controls (CAP-025); safety policy and emergency-type rules (RSK-016); position-protection policy (RSK-017); canary allocation limits and evidence requirements (STR-015, STR-018); performance hard limits (PERF-012); which gates are human-controlled (PLT-014). Their values are recorded in the values register (ARCH-018). An unset boundary means the autonomous action it governs is outside authorization.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../../decisions/DEC-024-part-2-reconciliation.md).

- **POL-012** Machine-readable policy fields · SYSTEM REQUIREMENT · P2§102, P2§280 — Natural-language policy should eventually compile into machine-readable policy. Potential fields: policy ID; version; objective; hard constraints; soft preferences; risk limits; capital limits; allowed markets; restricted markets; allowed strategies; forbidden conditions; emergency rules; effective time; expiration; change history.
- **POL-013** Policy traceability · CONFIRMED REQUIREMENT · P2§103, P2§281 — Important decisions should reference the active policy version. The system should answer: which policy permitted or restricted this decision?
- **POL-014** Policy history is immutable · CONSTRAINT · P2§104, P2§282 — A policy change creates a new version. Historical decisions remain associated with the policy that governed them.
- **POL-015** Policy simulation · CONFIRMED REQUIREMENT · P2§105, P2§283 — Material policy changes should be testable before activation. The system should compare current policy vs proposed policy and identify meaningful behavioral differences.

Notes:

- **Already covered.** Objectives translated into structured policy (P2§100) is NLP-001, NLP-002, NLP-004, and POL-002.
- **"Policy compiler".** Part 2 uses the term for two steps. Natural language → structured policy is the interpretation pipeline of the [Natural Language Policy Interface](natural-language-policy-interface.md) (NLP-004). Structured policy → enforceable rules, recompiled on every policy change (ARCH-023), is deterministic and belongs to this system. See the [glossary](../../glossary.md).
- **POL-015 with POL-006 and POL-007.** Every material change can be simulated. Simulation is mandatory before a loosening change (POL-006). A change that only tightens may still activate immediately (POL-007).
- **CF-14 (decided).** The owner chose an immutable safety floor ([DEC-026](../../decisions/DEC-026-safety-floor-and-layered-control.md)):
  - Changing a safety invariant or a HARD LIMIT value needs a formal, versioned, audited, human-controlled policy change (RSK-039).
  - Operational limits adapt automatically inside the bounds set here (RSK-035, RSK-036). Those adjustments are operating decisions, not policy changes needing confirmation.
  - POL-005 to POL-007 still govern changes to the bounds and authorizations themselves.

## Boundary (§92)

- **Owns:** the authoritative, versioned user policy.
- **Used by:** Risk Engine, Global Capital Authority, Recovery ("validate policy", REC-002), Trading Director ("policy" input, AGT-004), audit ("policy version", AUD-002).
- **Must not:** be replaced by AI memory (POL-001, MEM-004).
- **Not yet specified:** the final policy schema (POL-012 lists its potential fields), interfaces, tests. Change governance is POL-005 to POL-007; the operator confirms.

## Findings

All resolved. CF-14 → [DEC-026](../../decisions/DEC-026-safety-floor-and-layered-control.md).

CF-06 → [DEC-016](../../decisions/DEC-016-roadmap-stage-placement.md) (this system is in CORE TRADING FOUNDATION). CF-08 and OQ-15 → [DEC-015](../../decisions/DEC-015-modes-canary-and-policy-governance.md) (POL-009). OQ-17 → [DEC-015](../../decisions/DEC-015-modes-canary-and-policy-governance.md) (POL-005 to POL-007). OQ-08 → [DEC-015](../../decisions/DEC-015-modes-canary-and-policy-governance.md) (POL-008). DUP-22 → [DEC-011](../../decisions/DEC-011-ownership-of-shared-responsibilities.md) (MEM-005).
