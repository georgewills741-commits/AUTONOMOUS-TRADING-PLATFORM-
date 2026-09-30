# Performance, Latency and Continuous Operation

> **Status:** DOCUMENTED (Handoff Part 1) — no measurements exist yet · **Owner:** cross-cutting · **Roadmap stage:** OPERATIONALIZATION ("Performance engineering", §95), but §76 requires it from architecture design onward · **Sources:** §75–§78

## Requirements

- **PERF-001** Continuous operation · CONFIRMED REQUIREMENT · §75 — The production system must support long-running operation under: high event volumes; large trade histories; increasing strategy count; increasing market universe; AI provider failures; exchange rate limits; network failures; component restarts.
- **PERF-002** Performance is first-class · CONFIRMED REQUIREMENT · §76 — Performance must be considered from architecture design. The platform should be: fast where latency matters; efficient; correct under concurrency; stable under load; scalable; resource-conscious; resistant to bottlenecks.
- **PERF-003** Latency-sensitive path · CONFIRMED ARCHITECTURAL PRINCIPLE · §77 — Market event → data validation → feature/signal processing → opportunity detection → strategy evaluation → risk check → execution validation → exchange order.
- **PERF-004** AI off the latency path · CONSTRAINT · §77 — AI should not unnecessarily block latency-sensitive execution.
- **PERF-005** Performance engineering techniques · CONFIRMED ARCHITECTURAL PRINCIPLE · §78 — Where justified: event-driven processing; async processing; parallel processing; efficient data structures; caching; batching; precomputation; incremental calculations; connection reuse; concurrency controls; efficient persistence; backpressure; queues; work prioritization; resource isolation.
- **PERF-006** Measured technology choices · CONSTRAINT · §78 — Technology choices must be based on measured requirements.

## Findings

- CF-03: the latency-sensitive path (PERF-003) has no capital-reservation step, but CAP-004 requires reservation before capital is committed.
- OQ-19: Part 1 gives no latency budgets, throughput targets, or universe size, so PERF-006 cannot be applied yet.

See the [findings register](../conflicts/register.md) and the [open-question register](../open-questions/register.md).
