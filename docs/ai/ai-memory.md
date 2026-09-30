# AI Memory / Project Knowledge

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-27 · **Category:** AI · **Roadmap stage:** AI INTELLIGENCE ("AI memory/knowledge") · **Sources:** §68

Canonical definition of the platform's runtime knowledge/memory architecture for AI. This is about the running platform. It is separate from this repository, which is the *builder's* project memory under the constitution.

## Requirements

- **MEM-001** Knowledge not only in AI context · CONSTRAINT · §68 — Important persistent project knowledge must not depend solely on temporary AI context.
- **MEM-002** Knowledge/memory architecture · SYSTEM REQUIREMENT · §68 — The platform should have a clearly defined knowledge/memory architecture where required for: strategy history; model evaluations; research findings; previous decisions; policy history; system state; important lessons; validated constraints.
- **MEM-003** Memory properties · CONFIRMED REQUIREMENT · §68 — Memory must be: persistent; traceable; versioned where appropriate; scoped; auditable; protected against accidental contamination.
- **MEM-004** Not a second source of truth · CONSTRAINT · §68 — Memory must not become an uncontrolled second source of truth. Authoritative requirements remain in the appropriate canonical repository/system.

## Decisions applied (2026-09-30)

- **MEM-005** Reference, never copy · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — Memory entries about policy, strategies, model evaluations, or system state reference the owning system's versioned records instead of copying them.

## Findings (all resolved)

DUP-22 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (MEM-005).
