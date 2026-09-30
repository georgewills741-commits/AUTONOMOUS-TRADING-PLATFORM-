# Performance, Latency and Continuous Operation

> **Status:** DOCUMENTED (Handoff Part 1) — no measurements exist yet · **Owner:** cross-cutting · **Roadmap stage:** OPERATIONALIZATION ("Performance engineering", §95), but §76 requires it from architecture design onward · **Sources:** §75–§78

## Requirements

- **PERF-001** Continuous operation · CONFIRMED REQUIREMENT · §75 — The production system must support long-running operation under: high event volumes; large trade histories; increasing strategy count; increasing market universe; AI provider failures; exchange rate limits; network failures; component restarts.
- **PERF-002** Performance is first-class · CONFIRMED REQUIREMENT · §76 — Performance must be considered from architecture design. The platform should be: fast where latency matters; efficient; correct under concurrency; stable under load; scalable; resource-conscious; resistant to bottlenecks.
- **PERF-003** Latency-sensitive path · CONFIRMED ARCHITECTURAL PRINCIPLE · §77 — Market event → data validation → feature/signal processing → opportunity detection → strategy evaluation → risk check → execution validation → exchange order.
- **PERF-004** AI off the latency path · CONSTRAINT · §77 — AI should not unnecessarily block latency-sensitive execution.
- **PERF-005** Performance engineering techniques · CONFIRMED ARCHITECTURAL PRINCIPLE · §78 — Where justified: event-driven processing; async processing; parallel processing; efficient data structures; caching; batching; precomputation; incremental calculations; connection reuse; concurrency controls; efficient persistence; backpressure; queues; work prioritization; resource isolation.
- **PERF-006** Measured technology choices · CONSTRAINT · §78 — Technology choices must be based on measured requirements.

## Decisions applied (2026-09-30)

- **PERF-007** Initial design targets · DEPRECATED / REPLACED · DEC-017 — Until measurements replace them (PERF-006), the design targets are: internal decision latency, from market event received to order submitted and excluding venue network time, p99 ≤ 50 ms on arbitrage paths and ≤ 500 ms on directional paths.

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

PERF-007 is replaced by PERF-008 to PERF-012. Its 50 ms / 500 ms figures remain only as initial DESIGN TARGETS (V-06, V-07 in the [values register](../requirements/values-register.md)).

- **PERF-008** Latency decomposition · CONFIRMED REQUIREMENT · DEC-019 — The system should distinguish: market-data latency; internal processing latency; opportunity-detection latency; decision latency; risk-validation latency; capital-reservation latency; order-submission latency; exchange round-trip latency; fill latency; end-to-end execution latency.
- **PERF-009** Path-specific latency budgets · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-019 — Latency budgets are path-specific: the arbitrage path has ultra-low-latency requirements; the directional path has strategy-dependent requirements; the research path is generally less critical; the AI research path's budget is determined by task; the monitoring path has an independent budget. The architecture should not force one latency target onto every subsystem.
- **PERF-010** Continuous measurement · CONFIRMED REQUIREMENT · DEC-019 — The platform should continuously collect performance measurements, including where relevant: p50, p95, p99, and p99.9 latency; maximum observed latency; jitter; exchange round-trip time; queue delay; processing delay; network delay; order acknowledgement delay; fill delay; missed-opportunity latency; data freshness. Performance targets are established from: measured baseline → market requirements → strategy requirements → risk requirements → hard performance limits → SLO / SLA-like internal targets.
- **PERF-011** Automatic degradation handling · CONFIRMED REQUIREMENT · DEC-019 — Performance degradation is detected, classified, assessed for opportunity impact, and adapted to. Possible actions: reduce opportunity eligibility; reduce trading frequency; disable the affected strategy; disable the affected venue; reduce capital; increase safety restrictions; switch infrastructure path; enter degraded mode. The system should not continue behaving as though its performance characteristics remain normal.
- **PERF-012** Hard limits, soft targets, observed measurements · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-019 — Performance values are distinguished as hard limits (crossing them may make execution unsafe), soft targets (optimization goals), or observed measurements (what the system actually experiences). Design numbers are never mistaken for guaranteed real-world performance.

Placement (builder): the Performance Controller detects degradation (PFC-003); the Risk Engine applies the PERF-011 restrictions through safety levels (RSK-015). How latency enters opportunity economics is TNP-023.

## Findings (all resolved)

CF-03 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (capital reservation is on the latency-sensitive path, CAP-021). OQ-19 → [DEC-017](../decisions/DEC-017-reporting-alerting-and-performance-targets.md), superseded by [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md) (PERF-008 to PERF-012; data freshness limits in MKD-006).
