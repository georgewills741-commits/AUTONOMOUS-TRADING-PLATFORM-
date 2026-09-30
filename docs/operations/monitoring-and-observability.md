# Monitoring and Observability

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-28 · **Category:** operations · **Roadmap stage:** OPERATIONALIZATION ("Monitoring") · **Sources:** §88 (also §02 item 20)

Canonical definition of **operational** monitoring: whether the platform itself is functioning correctly. Market monitoring is a separate concern owned by the [Opportunity Detection Engine](../systems/opportunity-detection.md) (ARCH-005). The "Trading" signals below observe the platform's own trading activity, not the market.

## Requirements

- **MON-001** Trading signals · SYSTEM REQUIREMENT · §88 — Trading: trades; P&L; exposure; strategy performance; opportunity activity.
- **MON-002** Infrastructure signals · SYSTEM REQUIREMENT · §88 — Infrastructure: CPU; memory; latency; queue depth; database health; API health.
- **MON-003** Exchange signals · SYSTEM REQUIREMENT · §88 — Exchanges: connectivity; rate limits; errors; order failures; market-data health.
- **MON-004** AI signals · SYSTEM REQUIREMENT · §88 — AI: calls; latency; cost; errors; confidence; validation failures.
- **MON-005** Risk signals · SYSTEM REQUIREMENT · §88 — Risk: rejections; exposure; limits; kill switches; safe mode.
- **MON-006** Recovery signals · SYSTEM REQUIREMENT · §88 — Recovery: reconciliation; state mismatches; recovery events.

## Not yet specified in Part 1

Alerting and reporting (named in §01, §02 item 22, and §95 but never defined, OQ-13), dashboards, retention, how monitoring feeds the [system health](system-health.md) state, and tests.
