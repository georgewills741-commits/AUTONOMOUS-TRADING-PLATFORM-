# DEC-009 — Technology stack, storage, and deployment

- **Status:** ACCEPTED
- **Later changes:** Among the requirements, the retention values below are stated only in TEC-012; MKD-007 and MON-009 point to it instead of repeating them ([DEC-036](DEC-036-owner-decisions-audit-findings.md), DUP-40). The text below is kept as written.
- **Date:** 2026-09-30
- **Decided by:** builder, under the owner's explicit delegation ("choose the best combination that suits my system"). The owner may override.
- **Resolves:** OQ-16, OQ-22
- **Canonical detail:** [technology stack](../architecture/technology-stack.md) (TEC requirements)
- **Does not authorize implementation.** It fixes what will be used once implementation is approved.

## Context

Constitution Rule 104 forbids choosing a stack silently, and PERF-006 requires technology choices to follow measured requirements. No measurements exist yet, so the choice must be sound for the known requirements and leave room to optimize measured bottlenecks. The known requirements are:

- five or more venues; spot, perpetuals, and margin
- whole-universe scanning; triangular and cross-exchange arbitrage; directional strategies
- exact financial arithmetic
- backtesting and quantitative research
- an AI layer
- a single operator

## Decision

| Concern | Choice | Why |
|---|---|---|
| Primary language | Python 3.12+, asyncio, fully typed (mypy strict) | Best ecosystem for exchange APIs, quantitative work, backtesting, and AI SDKs; asyncio handles many concurrent venue connections; one language across live and research keeps behavior identical in backtest, paper, and live (PAP-001) |
| Measured hot paths | Rust extension modules (PyO3), **only after measurement** shows a bottleneck (e.g. order-book maintenance, triangular route search) | Meets PERF-006; avoids building for speed before it is needed |
| Financial arithmetic | `decimal.Decimal` for every price, quantity, fee, balance, P&L, and reservation; floats only for indicators, signals, and research | ARCH-010 requires deterministic, precise financial calculations |
| Contracts and validation | Pydantic v2 models for inter-system contracts, configuration, and AI outputs | ARCH-012 interfaces, AIV-004 machine validation, constitution Rule 108 |
| Exchange connectivity | CCXT (REST and WebSocket, MIT license) behind the platform's own adapter interface; native venue clients where CCXT falls short, per measurement | Covers all five venues and 100+ more (EXA-006); the platform's own interface keeps CCXT replaceable (EXA-004) |
| Authoritative state | PostgreSQL 16 | ACID transactions for capital reservations, ledger, orders, policy and strategy versions, audit |
| Market-data time series | TimescaleDB extension on PostgreSQL | One database engine; efficient time-series retention |
| Research and backtesting data | Parquet files queried with DuckDB / Polars | Fast columnar analysis on permanent historical archives |
| Inter-process messaging | NATS JetStream | Low-latency fan-out of market data and order/fill events, with backpressure (PERF-005); single small binary |
| Architecture style | Modular monolith: one codebase, each system a module with explicit interfaces, run as a few processes | Right size for one operator; avoids premature microservices; systems can be split later if measurement requires |
| Tooling | uv with a committed lockfile; ruff; mypy; pytest with Hypothesis (property tests for numerics) and testcontainers | Reproducible dependencies (Rule 102); tests against real PostgreSQL |
| Observability | OpenTelemetry, Prometheus, Grafana; structured JSON logs | Covers MON-001 to MON-009 |
| Deployment | Docker images; initially one host with Docker Compose; rollback by redeploying the previous image | OPS-003 controlled deployment and rollback |
| Secrets | Never in the repository; injected at runtime from environment or a secret manager | SEC-001, constitution Rule 110 |
| AI providers | Provider-agnostic AI gateway; providers and models are configuration, chosen by the Model Router from Model Evaluation results | AIL-007; model choice is made in the AI INTELLIGENCE stage with measurements |

**Retention (OQ-22):**
- Ledger, audit trail, event history, policy versions, and strategy versions: permanent and append-only.
- Market data: 30 days in TimescaleDB, then permanent compressed Parquet archives of OHLCV, trades, and order-book snapshots for backtesting.
- Operational logs: 90 days.
- Historical data sources: the platform's own collection from venues from day one; external vendors are FUTURE.

## Alternatives considered

- **Rust core with Python research:** faster execution path, but two languages across live and research, slower delivery, and harder backtest/live parity. Rust stays available for measured hot paths.
- **Go:** good concurrency, but a weaker quantitative and AI ecosystem.
- **Microservices from day one:** operational cost with no measured need.
- **Redis instead of NATS:** viable. NATS was chosen because the use is pure messaging with fan-out and backpressure; caching needs are covered in process.

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). The alternatives above were written with this record; the one below is named in this record's "Retention" paragraph, in answer to OQ-22._

- **External historical-data vendors** (OQ-22 asked for the historical data sources): deferred as FUTURE; the platform collects its own data from venues from day one ("Retention" above).

## Consequences

Python is now an approved project language, which also clears the way to commit documentation-consistency tooling. Licenses must be rechecked when each dependency is added (constitution Rule 99). TimescaleDB community features are under the Timescale License, which permits self-hosted use.
