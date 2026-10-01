# Performance, Latency and Continuous Operation

> **Status:** DOCUMENTED (Handoff Parts 1, 2, and 3) — no measurements exist yet · **Owner:** cross-cutting · **Roadmap stage:** OPERATIONALIZATION ("Performance engineering", §95), but §76 requires it from architecture design onward · **Sources:** §75–§78; Part 3: P3§395–P3§399

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

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **PERF-013** Concurrency-safe financial state · CONSTRAINT · P2§122 — The platform must account for concurrent: market events; opportunities; strategies; capital reservations; orders; fills; reconciliation; AI requests. Financial state transitions must be atomic or otherwise concurrency-safe.
- **PERF-014** Backpressure · CONFIRMED REQUIREMENT · P2§123 — The platform must prevent downstream overload. Possible controls: queues; rate limits; priorities; dropping non-critical work; degradation; resource budgets. Safety-critical processing must have higher priority than research.
- **PERF-015** Resource priority · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§124, P2§272 — Conceptual priority, highest first: emergency safety; risk; capital integrity; execution; market data; reconciliation; monitoring; live AI; research; background analytics. Exact implementation is an architecture decision.
- **PERF-016** Research compute isolation · CONSTRAINT · P2§125, P2§271 — Heavy research workloads must not consume resources required by: risk; execution; market-data processing; reconciliation; monitoring. Research workloads should be isolated or resource-limited.
- **PERF-017** Overhead to minimize · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§344 — Latency-sensitive paths should remain deterministic wherever possible. Minimize: internal computation overhead; unnecessary AI calls; unnecessary network calls; repeated calculations; database bottlenecks; queue congestion; lock contention. Measure performance rather than assuming it.

Atomic capital reservation specifically is CAP-027. Performance, load, and chaos testing (P2§168 to §170) are in the [verification architecture](verification-architecture.md).

## Handoff Part 3 applied (2026-09-30)

New requirements from [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), cited as P3§N. Part 3 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 3 reconciliation](../traceability/part-3-reconciliation.md). Placement, duplicate, and conflict resolutions: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md).

- **PERF-018** Service-specific latency targets · CONFIRMED REQUIREMENT · P3§395 — The platform should be designed for low-latency deterministic processing. However, Claude must not invent arbitrary universal latency guarantees before benchmarking the architecture and infrastructure. The correct principle is: minimize latency; measure latency; set service-specific targets; validate targets under realistic load. In addition to the latencies of PERF-008, latency targets should be defined separately for: normalization; reconciliation; AI activation; database writes; monitoring.
- **PERF-019** Hot path and cold path · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§396 — The architecture should distinguish the hot path from the cold path. The hot path may include: market data → normalization → quant → opportunity → risk → capital → execution. The cold path may include: research; historical analysis; reports; model evaluation; strategy discovery; long-running simulations. Heavy cold-path work must not block latency-sensitive execution.
- **PERF-020** Additional performance measurements · SYSTEM REQUIREMENT · P3§397 — In addition to the measurements of PERF-010 and VER-001, the system must measure: storage latency; error rate; backpressure. Performance optimization must be evidence-driven.
- **PERF-021** Bounded queues; critical state never discarded · CONSTRAINT · P3§398 — If incoming events exceed processing capacity, the system must not simply allow queues to grow without limit. In addition to the controls of PERF-014, it should implement where appropriate: sampling where safe; aggregation where safe; dropping of non-critical derived events; scaling; load shedding. Critical financial state must not be silently discarded.
- **PERF-022** What concurrency must not create · CONSTRAINT · P3§399 — In addition to PERF-013, concurrent opportunities must not create: double capital allocation; duplicate orders; conflicting strategy decisions; race conditions; incorrect position state. Capital reservation and other critical state transitions should be atomic where required.

PERF-019's hot path is PERF-003's latency-sensitive path in Part 3's words; PERF-016 already isolates research. PERF-018's targets become DESIGN TARGET values per service (like V-06 and V-07), replaced by measured baselines (PERF-010, PERF-012). PERF-022 lists what concurrency must not create; the mechanisms are CAP-027 (atomic reservation), EXE-008 and REC-017 (no duplicate orders), and CAP-017 (one allocator, so strategies cannot make conflicting allocation decisions). P3§400 is CAP-027.

## Decisions applied (2026-10-01)

From the master execution constitution ([DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md)). PERF-023 (§43) says for performance work what RSK-034 (the safety floor), REC-018 (recovery), and STR-022 (canary gates) say for their areas; it is indexed as SR-47 in the [System Rules Register](../requirements/system-rules-register.md).

- **PERF-023** No unsafe fast path · CONSTRAINT · DEC-033 — Performance optimization must never bypass: risk; capital; execution validation; authorization; reconciliation; audit. There is no "fast path" that is allowed to become an unsafe path.

## Findings (all resolved)

CF-03 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (capital reservation is on the latency-sensitive path, CAP-021). OQ-19 → [DEC-017](../decisions/DEC-017-reporting-alerting-and-performance-targets.md), superseded by [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md) (PERF-008 to PERF-012; data freshness limits in MKD-006).
