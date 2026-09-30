# Auditability and Event and Decision History

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-30 (named in the handoff as capabilities, "Auditability" and "Event and Decision History"; no implementing system is named) · **Roadmap stage:** CORE TRADING FOUNDATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) · **Sources:** §86, §87 (also §02 item 21)

Canonical definition of what must be traceable and which events must be preserved.

## Requirements

- **AUD-001** Traceable actions · CONFIRMED REQUIREMENT · §86 — Important actions must be traceable.
- **AUD-002** Audit record contents · SYSTEM REQUIREMENT · §86 — Record where applicable: what happened; when; which system acted; strategy; strategy version; policy version; model/agent; evidence; risk checks; capital reservation; execution; external venue confirmation; final outcome.
- **AUD-003** Events to preserve · SYSTEM REQUIREMENT · §87 — Preserve meaningful events: opportunity detected; opportunity rejected; trade proposed; risk rejection; capital unavailable; order submitted; order filled; partial fill; cancellation; exchange failure; recovery; strategy suspension; strategy promotion; strategy retirement; policy change; model change; AI disagreement; kill-switch activation.

## Decisions applied (2026-09-30)

- **AUD-004** Append-only and permanent · CONSTRAINT · DEC-009 — Audit records and event history are append-only and are never deleted.
- **AUD-005** Authoritative event record · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — The event and decision history is the authoritative record of what happened. The arbitrage opportunity database is derived from it (ARB-014).
- **AUD-006** Separate from operational logs · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-017 — Operational logs (MON-009) are separate from the audit trail. Logs may be rotated; audit records may not.

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

- **AUD-007** Transfer record · CONFIRMED REQUIREMENT · DEC-019 — For every transfer the system must record: why the transfer was initiated; source; destination; asset; amount; expected benefit; transfer cost; policy version; authorization boundary; execution result; reconciliation result.

## Boundary (§92)

- **Owns:** the audit trail and the event and decision history.
- **Fed by:** every acting system ("which system acted", AUD-002).
- **Protected by:** [security](../security/security-architecture.md) ("audit records", SEC-001).
- **Not yet specified:** event schemas, interfaces, tests. Storage is TEC-006; retention and immutability AUD-004; logging AUD-006.

## Findings (all resolved)

DUP-21 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (AUD-005, ARB-014). CF-05 → [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md) (CORE TRADING FOUNDATION).
