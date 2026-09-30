# AI Intelligence Layer

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-22 · **Category:** AI · **Roadmap stage:** AI INTELLIGENCE · **Sources:** §51–§53
>
> Canonical location for AI per §98 (`docs/ai/`).

Canonical definition of what AI is for, the hard boundary it may never cross, and when it is activated.

| Topic | Document |
|---|---|
| Responsibilities, hard-safety boundary, activation | this document |
| Hallucination Firewall, structured output, multi-agent validation, confidence calibration | [AI output validation](ai-output-validation.md) |
| Model routing, model evaluation, AI cost | [Model management](model-management.md) |
| Agent roster and overlap analysis | [Agents](agents.md) |
| AI memory / knowledge | [AI memory](ai-memory.md) |
| Model health vs strategy health | [Performance Controller](../systems/performance-controller.md) (PFC-005) |

## Role of AI

- **AIL-001** AI responsibilities · SYSTEM REQUIREMENT · §51 — AI responsibilities may include: market interpretation; research; strategy discovery; hypothesis generation; backtest interpretation; news analysis; sentiment; complex reasoning; strategy improvement proposals; failure investigation; performance interpretation; research coordination.
- **AIL-002** AI proposes, deterministic infrastructure enforces · CONFIRMED ARCHITECTURAL PRINCIPLE · §51 — AI proposes and analyzes. Deterministic infrastructure enforces.

## Hard-safety boundary

- **AIL-003** What AI must never do · CONSTRAINT · §52 — AI must not: bypass risk; increase authorized risk; disable kill switches; override user hard restrictions; submit unrestricted arbitrary orders; deploy unvalidated strategies; modify protected test boundaries; assume unsupported claims are facts; assume execution succeeded; receive unrestricted secrets.

The same boundary appears elsewhere as system-level rules: RSK-003 (AI cannot bypass risk), EXE-003 (never trust an AI claim of order success), STR-002 (no AI shortcut through the lifecycle), SEC-002 (no unrestricted credentials for AI agents). These statements agree with each other.

## Event-driven activation

- **AIL-004** No per-tick AI · CONSTRAINT · §53 — AI must not inspect every market tick unnecessarily.
- **AIL-005** Event-driven activation · CONFIRMED ARCHITECTURAL PRINCIPLE · §53 — Preferred architecture: high-volume market events → deterministic processing → filtering → significant event → AI reasoning if justified.

Consistent with OPP-008 (AI activated only when its reasoning adds meaningful value) and PERF-004 (AI should not unnecessarily block latency-sensitive execution).

## Boundary (§92)

- **Owns:** AI reasoning, research, and proposals, always as *input* to deterministic systems.
- **Must not:** anything in AIL-003.
- **Failure behavior (§91 example):** if AI is unavailable, deterministic capabilities continue where safe (HLT-005).
- **Not yet specified in Part 1:** the "AI gateway" listed in §95 (OQ-14), AI providers and models (OQ-16), interfaces, tests.
