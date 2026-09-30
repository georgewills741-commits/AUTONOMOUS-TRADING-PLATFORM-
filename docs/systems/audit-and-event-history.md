# Auditability and Event and Decision History

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-30 (named in the handoff as capabilities, "Auditability" and "Event and Decision History"; no implementing system is named) · **Roadmap stage:** **not mapped by §95** (CF-05) · **Sources:** §86, §87 (also §02 item 21)

Canonical definition of what must be traceable and which events must be preserved.

## Requirements

- **AUD-001** Traceable actions · CONFIRMED REQUIREMENT · §86 — Important actions must be traceable.
- **AUD-002** Audit record contents · SYSTEM REQUIREMENT · §86 — Record where applicable: what happened; when; which system acted; strategy; strategy version; policy version; model/agent; evidence; risk checks; capital reservation; execution; external venue confirmation; final outcome.
- **AUD-003** Events to preserve · SYSTEM REQUIREMENT · §87 — Preserve meaningful events: opportunity detected; opportunity rejected; trade proposed; risk rejection; capital unavailable; order submitted; order filled; partial fill; cancellation; exchange failure; recovery; strategy suspension; strategy promotion; strategy retirement; policy change; model change; AI disagreement; kill-switch activation.

## Boundary (§92)

- **Owns:** the audit trail and the event and decision history.
- **Fed by:** every acting system ("which system acted", AUD-002).
- **Protected by:** [security](../security/security-architecture.md) ("audit records", SEC-001).
- **Not yet specified in Part 1:** storage, retention, immutability, the relationship to "logging" (§04), interfaces, tests.

## Findings

- DUP-21: the arbitrage opportunity database (ARB-003) also records detected and rejected opportunities.
- CF-05: auditability is not mapped to any roadmap stage, yet the core trading systems produce the events it must record.
