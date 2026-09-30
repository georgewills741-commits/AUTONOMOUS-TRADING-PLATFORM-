# AI Memory / Project Knowledge

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-27 · **Category:** AI · **Roadmap stage:** AI INTELLIGENCE ("AI memory/knowledge") · **Sources:** §68

Canonical definition of the platform's runtime knowledge/memory architecture for AI. This is about the running platform. It is separate from this repository, which is the *builder's* project memory under the constitution.

## Requirements

- **MEM-001** Knowledge not only in AI context · CONSTRAINT · §68 — Important persistent project knowledge must not depend solely on temporary AI context.
- **MEM-002** Knowledge/memory architecture · SYSTEM REQUIREMENT · §68 — The platform should have a clearly defined knowledge/memory architecture where required for: strategy history; model evaluations; research findings; previous decisions; policy history; system state; important lessons; validated constraints.
- **MEM-003** Memory properties · CONFIRMED REQUIREMENT · §68 — Memory must be: persistent; traceable; versioned where appropriate; scoped; auditable; protected against accidental contamination.
- **MEM-004** Not a second source of truth · CONSTRAINT · §68 — Memory must not become an uncontrolled second source of truth. Authoritative requirements remain in the appropriate canonical repository/system.

## Findings

- DUP-22: MEM-002 lists policy history, strategy history, model evaluations, and system state. Each already has a canonical owner: the Policy System (POL-003), Strategy Management (STR-005), Model Evaluation (MEV-001), and System Health / Portfolio. Under MEM-004, memory may reference them but must not become their authority.
