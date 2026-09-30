# Technology Stack

> **Status:** DECIDED — [DEC-009](../decisions/DEC-009-technology-stack.md) (builder choice under the owner's explicit delegation, 2026-09-30). Nothing is implemented, and choosing the stack does not authorize implementation.
>
> Canonical definition of the languages, libraries, storage, messaging, tooling, and deployment the platform will use. The reasons and alternatives are in DEC-009. Adding a dependency not listed here requires a decision record (constitution Rules 99–101).

## Requirements

- **TEC-001** Primary language · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-009 — The platform is written in Python 3.12 or later, using asyncio for concurrency, and is fully type-checked (mypy strict).
- **TEC-002** Rust only for measured hot paths · CONSTRAINT · DEC-009 — Rust extension modules (PyO3) may be added only where measurement shows a Python bottleneck, such as order-book maintenance or triangular route search (PERF-006).
- **TEC-003** Exact decimal arithmetic · CONSTRAINT · DEC-009 — Every price, quantity, fee, balance, P&L amount, and reservation uses exact decimal arithmetic (`decimal.Decimal`). Floating point is allowed only for indicators, signals, and research, never for capital, ledger, economics, or orders (ARCH-010).
- **TEC-004** Validated contracts · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-009 — Inter-system contracts, configuration, and AI outputs are defined as Pydantic v2 models and validated at every boundary.
- **TEC-005** Exchange connectivity library · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-009 — Venue access uses CCXT (REST and WebSocket) behind the platform's own adapter interface; native venue clients are used where measurement shows CCXT is insufficient. No system outside the adapter layer depends on CCXT.
- **TEC-006** Storage · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-009 — PostgreSQL 16 holds authoritative transactional state (capital and reservations, ledger, orders, policy and strategy versions, audit and event history). The TimescaleDB extension holds market-data time series. Parquet files, queried with DuckDB or Polars, hold historical research and backtesting data.
- **TEC-007** Messaging · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-009 — Inter-process events (market-data fan-out, order and fill events) use NATS JetStream, with backpressure.
- **TEC-008** Modular monolith · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-009 — One codebase; each system is a module with explicit interfaces, run as a small number of processes. A system is split into its own service only when measurement requires it.
- **TEC-009** Reproducible tooling · CONFIRMED REQUIREMENT · DEC-009 — Dependencies are managed with uv and a committed lockfile. Code is linted and formatted with ruff and type-checked with mypy. Tests use pytest, with Hypothesis property tests for numerical code and testcontainers for tests against real PostgreSQL.
- **TEC-010** Observability stack · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-009 — OpenTelemetry for traces and metrics, Prometheus for metric storage, Grafana for dashboards, and structured JSON logs.
- **TEC-011** Deployment · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-009 — Services ship as Docker images. The initial deployment is a single host running Docker Compose. Rollback means redeploying the previous image version.
- **TEC-012** Data retention · CONFIRMED REQUIREMENT · DEC-009 — The ledger, audit trail, event history, and policy and strategy versions are kept permanently and are append-only. Market data is kept 30 days in TimescaleDB, then permanently in compressed Parquet archives (OHLCV, trades, order-book snapshots). Operational logs are kept 90 days.

## Not yet decided

Specific versions of each library (fixed in the lockfile when implementation starts), the AI providers and models (chosen in the AI INTELLIGENCE stage from Model Evaluation results, AIL-007), and hosting location. The hosting location should minimise network latency to the enabled venues, and is to be chosen with measurements.
