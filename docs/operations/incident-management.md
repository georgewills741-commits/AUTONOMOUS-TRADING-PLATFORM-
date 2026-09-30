# Incident Management

> **Status:** DOCUMENTED (Handoff Part 2) — not implemented · **Owner:** SYS-28 Monitoring and Observability (component) · **Roadmap stage:** OPERATIONALIZATION (production hardening, RMP-010) · **Sources:** P2§77, P2§160, P2§194; [DEC-024](../decisions/DEC-024-part-2-reconciliation.md)
>
> Canonical definition of how production incidents are recorded. Requirement line format: [`docs/requirements/README.md`](../requirements/README.md).

## Requirements

- **INC-001** Structured incident management · CONFIRMED REQUIREMENT · P2§77 — Production operations require structured incident management.
- **INC-002** Incident record · SYSTEM REQUIREMENT · P2§77 — Incidents should record: incident ID; time; environment; system; severity; detection method; symptoms; root cause; impact; actions; recovery; follow-up; related changes.
- **INC-003** Owner of incident records · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-024 — Incident records are owned by Monitoring and Observability (SYS-28), which already raises alerts (MON-007, MON-011) and receives recovery escalations (REC-012). Security incidents use the same record (SEC-009).

## How incidents connect to the rest of the platform

- **Detection:** alerts (MON-007, MON-011), recovery escalation (REC-012, RSK-024), and kill-switch trips (RSK-008).
- **Response:** containment by the owning systems: the Risk Engine's safety levels (RSK-015) and recovery (REC-015). An incident record never takes a trading action itself.
- **Human involvement:** only where PLT-014 reserves the condition for a human, for example security events or an unknown financial state.
- **Evidence:** incidents count against readiness (RDY-002) and appear in the daily report (DSI-002).
- **Audit:** the incident record references the audit events it concerns (AUD-003); it does not replace them.

## Not yet specified

Severity scale (the alert severities of MON-007 are the starting point), incident lifecycle states, follow-up tracking, retention, interfaces, tests.
