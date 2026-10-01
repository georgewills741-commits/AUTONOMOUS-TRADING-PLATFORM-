# Incident Management

> **Status:** DOCUMENTED (Handoff Parts 2 and 3) — not implemented · **Owner:** SYS-28 Monitoring and Observability (component) · **Roadmap stage:** OPERATIONALIZATION (production hardening, RMP-010) · **Sources:** P2§77, P2§160, P2§194; [DEC-024](../decisions/DEC-024-part-2-reconciliation.md); Part 3: P3§499–P3§500
>
> Canonical definition of how production incidents are recorded. Requirement line format: [`docs/requirements/README.md`](../requirements/README.md).

## Requirements

- **INC-001** Structured incident management · CONFIRMED REQUIREMENT · P2§77 — Production operations require structured incident management.
- **INC-002** Incident record · SYSTEM REQUIREMENT · P2§77 — Incidents should record: incident ID; time; environment; system; severity; detection method; symptoms; root cause; impact; actions; recovery; follow-up; related changes.
- **INC-003** Owner of incident records · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-024 — Incident records are owned by Monitoring and Observability (SYS-28), which already raises alerts (MON-007, MON-011) and receives recovery escalations (REC-012). Security incidents use the same record (SEC-009).

## Handoff Part 3 applied (2026-09-30)

New requirements from [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), cited as P3§N. Part 3 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 3 reconciliation](../traceability/part-3-reconciliation.md). Placement, duplicate, and conflict resolutions: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md).

- **INC-004** Incident lifecycle · SYSTEM REQUIREMENT · P3§499 — The system should support the incident lifecycle: detect → classify → contain → protect → investigate → recover → reconcile → verify → close → learn.
- **INC-005** Post-incident learning · CONFIRMED REQUIREMENT · P3§500 — Important incidents should produce structured lessons. Possible outputs: new test; new alert; new rule; architecture change; strategy change; risk change; documentation change; monitoring improvement. Production behavior must not be changed merely because an incident occurred.

INC-005's outputs are proposals that go through their owners' change processes: a strategy change through the lifecycle (STR-009), a risk or policy change through POL-005 to POL-007, an architecture change through GOV-016. Lessons are learning evidence (STR-027).

## How incidents connect to the rest of the platform

- **Detection:** alerts (MON-007, MON-011), recovery escalation (REC-012, RSK-024), and kill-switch trips (RSK-008).
- **Response:** containment by the owning systems: the Risk Engine's safety levels (RSK-015) and recovery (REC-015). An incident record never takes a trading action itself.
- **Human involvement:** only where PLT-014 reserves the condition for a human, for example security events or an unknown financial state.
- **Evidence:** incidents count against readiness (RDY-002) and appear in the daily report (DSI-002).
- **Audit:** the incident record references the audit events it concerns (AUD-003); it does not replace them.

## Not yet specified

Severity scale (the alert severities of MON-007 are the starting point), the state machine for INC-004's lifecycle, follow-up tracking, retention, interfaces, tests.
