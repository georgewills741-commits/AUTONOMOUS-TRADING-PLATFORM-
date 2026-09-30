# Monitoring and Observability

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-28 (also owns alerting and reporting, [DEC-017](../decisions/DEC-017-reporting-alerting-and-performance-targets.md)) · **Category:** operations · **Roadmap stage:** OPERATIONALIZATION ("Monitoring") · **Sources:** §88 (also §02 item 20)

Canonical definition of **operational** monitoring: whether the platform itself is functioning correctly. Market monitoring is a separate concern owned by the [Opportunity Detection Engine](../systems/opportunity-detection.md) (ARCH-005). The "Trading" signals below observe the platform's own trading activity, not the market.

## Requirements

- **MON-001** Trading signals · SYSTEM REQUIREMENT · §88 — Trading: trades; P&L; exposure; strategy performance; opportunity activity.
- **MON-002** Infrastructure signals · SYSTEM REQUIREMENT · §88 — Infrastructure: CPU; memory; latency; queue depth; database health; API health.
- **MON-003** Exchange signals · SYSTEM REQUIREMENT · §88 — Exchanges: connectivity; rate limits; errors; order failures; market-data health.
- **MON-004** AI signals · SYSTEM REQUIREMENT · §88 — AI: calls; latency; cost; errors; confidence; validation failures.
- **MON-005** Risk signals · SYSTEM REQUIREMENT · §88 — Risk: rejections; exposure; limits; kill switches; safe mode.
- **MON-006** Recovery signals · SYSTEM REQUIREMENT · §88 — Recovery: reconciliation; state mismatches; recovery events.

## Decisions applied (2026-09-30)

- **MON-007** Alerting · CONFIRMED REQUIREMENT · DEC-017 — Alerts have severities INFO, WARNING, CRITICAL, and EMERGENCY, and are delivered to at least one operator-configured channel. CRITICAL and EMERGENCY alerts require acknowledgement.
- **MON-008** Reporting · CONFIRMED REQUIREMENT · DEC-017 — The platform produces daily and on-demand reports of P&L, exposure, strategy performance, expected vs actual, AI cost, and incidents, as read-only views over the ledger, portfolio, audit trail, and Performance Controller.
- **MON-009** Operational logs · SYSTEM REQUIREMENT · DEC-017 — Structured operational logs are kept here and rotated after 90 days. They are separate from the audit trail (AUD-006).

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

Monitoring collects the performance measurements in PERF-010, and raises an alert or incident when recovery fails (REC-012) or a safety level escalates (RSK-015). No new requirement is created here.

## Not yet specified

Specific alert channels (operator configuration), dashboard layouts, and tests. How monitoring feeds platform state is HLT-010.
