# Stage 2 — DATA FOUNDATION: Plan

> **Status:** APPROVED — by the owner on 2026-11-17, with changes to D1 and D2, which section 10 states ([DEC-073](../decisions/DEC-073-stage-2-plan-approved-with-changes.md); [owner decisions 40](../handoffs/owner-decisions-40-approval-of-stage-2-plan-with-changes.md)). Stage 2's implementation is authorized, checkpoint by checkpoint in section 11's order, once the change that records the approval has passed its three gates. The approval covers Stage 2 only, not later architecture changes (constitution Rules 134–136), and does not authorize bypassing an unresolved entry condition, buying infrastructure without the owner's approval, or weakening a technical requirement. Stage 2's features are APPROVED, and DESIGNED as this plan designs them ([DEC-040](../decisions/DEC-040-later-stage-features-proposed.md)).
>
> The fields of constitution Rule 140 for the second stage of the [master roadmap](roadmap.md), in the form of the approved [Stage 1 plan](stage-01-foundation-plan.md) ([DEC-038](../decisions/DEC-038-stage-1-plan-approved.md)). Every choice not already a requirement or decision is listed in section 10, dependencies included (Rules 99–101), and was decided by the owner on 2026-11-17 (DEC-073). No requirement is added, removed, or reworded; each new value is classified in the [values register](../requirements/values-register.md) before use, set from measurement, never invented (ARCH-018; PERF-006). What the repository cannot confirm is marked unknown or "to be confirmed".

## 1. Objective

Build the data foundation from public, read-only market data, without any trading capability:

- adapters for the venues D1 enables, the only code that talks to a venue, with rate limits, resilience, and exact increments (EXA, ARCH-011);
- one market-data system that validates, normalizes once, scores, quarantines, marks freshness, keeps lineage, stores, and archives (MKD), with clock-drift detection (HLT-013);
- the Quantitative Engine with its Fee and Slippage Engines, the Market Regime Engine, and continuous, bounded whole-universe monitoring that produces candidates only (QNT, RGM, OPP);
- measurement, and the first baselines from which V-08 and V-17 can later be set (PERF-008 to PERF-010, PERF-018 to PERF-020, as the [roadmap](roadmap.md) places them).

Systems affected: SYS-01 to SYS-05 (roadmap); from the roadmap's additions, SYS-29's clock-drift detection and the cross-cutting performance, configuration (MIG-034), and security (SEC-010) sets.

At the end of Stage 2 the platform watches markets and measures itself, but holds no credential, reads no account, and cannot place an order (RMP-002, RMP-011). Nothing for execution is built, the approved maker-versus-taker selection included (EXE-012; DEC-067, decision 4: "This approval does not authorize immediate execution-system implementation during Stage 2 Data Foundation").

## 2. Entry gate (master execution constitution §12)

| Condition | Status | Evidence |
|---|---|---|
| Prerequisite stages complete | Yes: Stage 1 COMPLETE on 2026-11-10 | DEC-067; [Stage 1 exit verification](../traceability/stage-01-exit-verification.md) |
| Required architecture exists | Yes: SYS-01 to SYS-05 specified, with dependencies D-01 to D-05 | [System registry](../architecture/system-registry.md), [dependency map](../architecture/dependency-map.md) |
| Required contracts exist | The kernel exists (Stage 1, U3); U2 writes SYS-02's contracts, and U7 to U9 those of SYS-03 to SYS-05's outputs, each before any code uses them (ARCH-025; audit finding A-05) | [Contract conventions](../architecture/contracts.md) |
| Required dependencies exist | Decided: TEC-005, TEC-006, TEC-009, TEC-010 ([DEC-009](../decisions/DEC-009-technology-stack.md)); the packages Stage 2 adds are in D12 | [Technology stack](../architecture/technology-stack.md) |
| Required decisions approved | Yes: section 10's, by the owner on 2026-11-17 | [DEC-073](../decisions/DEC-073-stage-2-plan-approved-with-changes.md) |
| Required documentation exists | Yes; what the specifications leave to "when DATA FOUNDATION is planned" (schemas, failure behaviour, regime rules, promotion, thresholds, budgets, filters, the drift response, how stored data names its contract) is decided here as rules and conventions (D3, D5, D6, D9, D10; U4 and U5 for failure behaviour) and completed by the unit that builds it: the schemas at U2 and U7 to U9, the regime rules at U8, thresholds and budgets from measurement | The specifications of SYS-01 to SYS-05 and SYS-29 |
| Required environment available | **Not yet verified.** The builder found this cloud environment's network policy unrestricted (2026-11-17); no exchange endpoint has been contacted; whether each venue's public API answers from its region is unknown. Observed read-only on 2026-11-17: a Docker client but no running daemon; PostgreSQL 16 server programs, no TimescaleDB; uv 0.11.32 on the path, not the required 0.12.23 | U1's readiness check, before any work that depends on infrastructure (D2); its result is in the [Stage 2 record](../traceability/stage-02-data-foundation.md) |

## 3. Requirements and their disposition in Stage 2

Below, once each: the 67 requirements whose registry default stage is DATA FOUNDATION (EXA-001 to EXA-015, MKD-001 to MKD-013, QNT-001 to QNT-007, RGM-001 to RGM-008, OPP-001 to OPP-024); those the roadmap's DATA FOUNDATION rows name (HLT-013, HLT-014, PERF-008 to PERF-010, PERF-018 to PERF-020, MIG-034, SEC-010), with the V-08 and V-17 baselines; and what the Stage 1 plan left to this stage or to the first running or deployable service (ARCH-011; TEC-005 to TEC-007, TEC-009's testcontainers, TEC-010 to TEC-012; OPS-010). The roadmap is authoritative where it places a requirement elsewhere than the [registry](../requirements/registry.md)'s default stage. "CORE" is CORE TRADING FOUNDATION.

### 3.1 Delivered by Stage 2 code

| Requirements | What Stage 2 delivers | Unit |
|---|---|---|
| EXA-001, EXA-004, EXA-006, EXA-011, TEC-005 | One exchange abstraction, CCXT behind it, one adapter per enabled venue; nothing else talks to a venue or imports CCXT; a venue is added by its adapter and configuration alone | U4 |
| EXA-014 (its retry rule for financial actions: CORE, with EXE-008) | Per-endpoint and per-venue limits for REST and WebSocket, priority, backoff, retries for reads only | U4 |
| EXA-015 | Connection health, reconnect, heartbeats, stale-feed detection, backoff, circuit breaking, venue states of their own type | U4 |
| ARCH-011 (completed) | Each market's tick and step sizes and minimums from public metadata, exact, applied through `atp.numeric`'s quantization | U4 |
| MKD-001, MKD-003, MKD-011 | One market-data system; the pipeline in its stated order; normalization in one place | U5 |
| MKD-005 | A stable evidence identifier, source, and timestamp on every stored item and calculation output | U2, U5, U7 |
| MKD-008, MKD-009, MKD-013 | Validation before use, deterministic quality scores, quarantine for each listed cause | U5 |
| MKD-007, TEC-009 (testcontainers) | TimescaleDB storage with V-18's retention, then the Parquet archive; tests on a real PostgreSQL with TimescaleDB | U6 |
| HLT-013 | Clock-drift detection, with D3's response | U5 |
| QNT-004, QNT-007 | Primitive metrics only, one Fee Engine and one Slippage Engine; combining costs stays with the True Net-Profit Engine (TNP-017) | U7 |
| RGM-001, RGM-002, RGM-003, RGM-005, RGM-006, RGM-007 | Deterministic, versioned classification in D9's taxonomy, with UNCERTAIN, UNKNOWN, ABNORMAL; SYS-04 the only owner of regime state | U8 |
| OPP-001, OPP-003, OPP-006, OPP-010, OPP-012 | One detection engine monitors the whole configured universe continuously: every market at ticker level, full depth for candidates within rate limits | U9 |
| OPP-021, OPP-022, OPP-023 | Scanning never stops at a find; search order is a preference, never a floor, quota, stopping condition, or universe restriction; several tiers at once | U9 |
| PERF-020; MIG-034; SEC-010 (each later stage for its own) | Storage latency, error rate, backpressure measured; a record per new setting; each new control traced to monitoring, no informal exception | U3, U10; U2; U11 |

### 3.2 Started in Stage 2, completed in a later stage

| Requirement | Stage 2 | Completed in |
|---|---|---|
| EXA-003 | Market data, precision, rate limits, errors, connectivity, public capabilities | CORE: authentication, account data, orders, fills, balances, positions |
| EXA-005 | Adapters of the venues whose public market data D1's verification permits | Each other initial venue once D1's verification permits its public market data; no stage fixed |
| EXA-007 | A venue's public market data used only where D1's verification finds credential-free, read-only access to it permitted by applicable law and the venue's terms and answering from the environment without a workaround; otherwise the venue stays disabled for it, its status recorded, never reached another way | CORE and later: the account's eligibility, supported instruments, and jurisdiction, and every applicable risk and readiness gate, verified before any trading activation (D1) |
| EXA-009 | Instrument types per venue; public funding data | CORE: leverage, margin and position modes; account borrow data |
| EXA-012, EXA-013 | Subscriptions, symbol mapping, fee metadata (D8), WebSocket state, connection management; canonical symbols, timestamps, precision, errors, rate limits | CORE: order cancellation and querying; orders, fills, positions |
| MKD-002 | Every listed item a venue publishes without credentials, increments and minimums included | CORE: the account's own execution data |
| MKD-004 | Timestamps, duplicates, gaps, ordering, corruption, symbol mappings, precision; receive times and delisted markets kept | DIRECTIONAL TRADING: backtest biases (BKT-002, BKT-004, BKT-005) |
| MKD-006 | Freshness marking per stream against D3's provisional limits | CORE: the limits as hard limits in policy; no trading on stale data (RSK-010, RSK-034) |
| MKD-010 | Source, timestamp, dataset, data, processing, and feature versions | CORE: policy version, decision lineage (AUD-012); DIRECTIONAL TRADING: strategy version |
| MKD-012 | Freshness and quality per data type; Stage 2's consumers take eligible data only | DIRECTIONAL TRADING: strategy-specific thresholds; CORE: decision eligibility in risk |
| QNT-002 | Indicators, volatility, spread, returns, correlation, liquidity metrics, fee and slippage estimates | CORE: drawdown, exposure, sizing, risk/reward; CORE, ARBITRAGE: arbitrage economics (True Net-Profit Engine) |
| QNT-005 | Venue, instrument, maker or taker, schedule and tier as D8 provides, funding rates | CORE: the account's actual tier and rates; ARBITRAGE: transfer costs |
| QNT-006 | Depth, size, liquidity, volatility, spread, execution type, market impact | DIRECTIONAL TRADING and CORE: historical execution behaviour |
| RGM-008 | No regime is inferred; UNKNOWN reaches consumers as UNKNOWN | CORE, DIRECTIONAL TRADING: the responses (no trade, wait, reduced exposure, validation) |
| OPP-002, OPP-007 | Scanning and detection across venues, assets, pairs, liquidity, volatility, funding, regimes, anomalies, events, observed cross-venue prices | DIRECTIONAL TRADING: directional and strategy conditions and opportunities; ARBITRAGE: cross-exchange and triangular arbitrage, triangular routes scanned once SYS-19 discovers them (TAR-002, TAR-003) |
| OPP-005, OPP-018 | Universe → data → quant → scanning → filtering → candidates, continuously | CORE: economics, risk, capital, execution eligibility; DIRECTIONAL TRADING: strategies; AI INTELLIGENCE: AI when justified |
| OPP-008 | Deterministic high-volume screening | AI INTELLIGENCE: selective AI activation |
| OPP-009 | Every market of the enabled types on the enabled venues, following listings and delistings (D1) | CORE: the Policy System's exclusions (D-44) |
| OPP-013 | Bounds from data quality, liquidity, venue availability, resources, eligibility; the universe-selection architecture completed (D10) | CORE: bounds from risk policy |
| OPP-017, OPP-020 | Breadth, depth, speed, continuity, cross-market and cross-venue comparison; markets, venues, and depth scaled within budgets | DIRECTIONAL TRADING: strategy diversity and count; ARBITRAGE: arbitrage routes |
| OPP-024 | Adaptive frequency, depth, expansion, and analysis depth within budgets and rate limits, never re-analysing unchanged inputs (D10) | DIRECTIONAL TRADING: priority by demonstrated quality (PFC-012, PFC-013, from CORE's Opportunity Database); concurrent strategy evaluations |
| HLT-014 | UTC event times, monotonic durations, venue server times compared (D5) | OPERATIONALIZATION: host clock synchronization as code (OPS-014) |
| PERF-008 | Market-data, processing, and detection latency; public requests' round trip | CORE: decision, risk, reservation, submission, order round-trip, fill, end-to-end latency |
| PERF-010 | The framework; first baselines | CORE: acknowledgement and fill delays; DIRECTIONAL TRADING: missed-opportunity latency; OPERATIONALIZATION: internal targets |
| PERF-018 | Normalization and database-write latencies; DESIGN TARGET values proposed from them | CORE: reconciliation; AI INTELLIGENCE: AI activation; OPERATIONALIZATION: monitoring |
| V-08, V-17 (measured baselines) | What Stage 2's paths allow: staleness and its parts per stream; market-data, normalization, storage, detection latency (D2) | CORE: the values set as HARD LIMITs in policy by RSK-039's human-controlled change; decision-latency baselines, which need CORE's path |
| TEC-006, TEC-012 | TimescaleDB for market data, its retention, the Parquet archive | CORE and later: transactional state, permanent records; OPERATIONALIZATION: logs (V-19) |
| TEC-010 | OpenTelemetry metrics; JSON logs (D7) | OPERATIONALIZATION: traces, Prometheus, Grafana (SYS-28) |
| TEC-011, OPS-010 | Compose for the development backing services, at the deployment definition's one location (D7) | OPERATIONALIZATION: images and deployment (OPS-007, OPS-008, OPS-011 to OPS-017) |

### 3.3 Applied as design rules to Stage 2's own work, verified in Gate 2

QNT-001, QNT-003, OPP-004 (no LLM, no AI); OPP-011 (detection, not ranking for capital); OPP-019, SR-04 (a candidate reaches nothing that acts); PERF-009 (each measurement belongs to a path); PERF-019 (cold work off the hot path); PERF-014, PERF-015, PERF-017, PERF-021, PERF-023, SR-42 (backpressure, priority, overhead, bounded queues, no unsafe fast path); ARCH-010, TEC-003 (floats only as D5 allows); ARCH-018; ARCH-025, ARCH-026, ARCH-041, ARCH-042, GOV-006, GOV-007, TEC-004 (contracts on the kernel; each venue request's result an outcome, UNKNOWN never SUCCESS); GOV-014; GOV-017; MIG-004, MIG-010; MIG-012 (a schema version from the first table); PLT-012 (D1); PLT-022; PLT-029; SEC-004, SEC-005 (no venue credential; the database credential a `server` secret); TNP-005, TNP-016, TNP-031, SR-48 (no percentage floor; a gross observation is no net profit); V-44 with PFC-021 and SR-19 (nothing reads the daily benchmark: DEC-067, decision 3; [DEC-068](../decisions/DEC-068-universal-opportunity-directive-mapped.md); [DEC-070](../decisions/DEC-070-permanent-trading-rules-mapped.md) found the owner's trading rules already canonical); RMP-011. TC-10 stays open: regime, venue, and freshness states each have their own type, so their UNKNOWN, UNCERTAIN, or DEGRADED cannot be confused with the outcome's or the health states', as Stage 1 did with its names.

### 3.4 Decided, applied in later stages (not built in Stage 2)

| Requirement | Applied in |
|---|---|
| EXA-008 | CORE, with EXE-008 |
| EXA-010 | ARBITRAGE (roadmap) |
| RGM-004 | DIRECTIONAL TRADING, from the regime state Stage 2 provides |
| OPP-014, OPP-015, OPP-016 | CORE: the one Opportunity Database, derived from the event history (roadmap; D-58). Stage 2 stores no candidates |
| TEC-007 | When a second process needs market-data fan-out, at the latest with CORE's order and fill events (D7) |

### 3.5 Not built

EXA-002 (DEPRECATED / REPLACED by DEC-008's venue list).

## 4. In scope: work units

Each unit is a coherent, recoverable piece of work (master execution constitution §08). The units form five checkpoints; each passes the three gates before its commit (DEC-032, DEC-033).

### U1 — Environment readiness, dependencies, venue verification (checkpoint A)

- **Requirements:** EXA-007; the packages and services of TEC-005, TEC-006, TEC-009, TEC-010 (constitution Rules 99–102, 105).
- **Content:** first, D2's readiness check, before any work that depends on infrastructure: what the environment provides and lacks for Stage 2 (uv 0.12.23, a Docker daemon, PostgreSQL 16 with TimescaleDB, the TimescaleDB image pinned by digest, Docker on the machine checks' runners), and the smallest compliant way to provide what is missing with the approved stack and the infrastructure already available; where it cannot be provided, the report D2 requires goes to the owner, the work that needs it waits, and the configuration is not attempted again. D12's packages added; the lockfile reviewed against published advisories and licenses (a scanner run once, not added); strict mypy and `filterwarnings = error` checked, any exception confined to `atp.exchange` and recorded. Then D1's verification, venue by venue: its published terms and restrictions, and applicable law, on access to its public market data, checked against the environment's location, the owner being asked where they turn on the operator's jurisdiction; where they permit it, one documented public request (server time or market list), without credentials, shows whether it answers from here; a venue whose terms forbid that access, or whose answer refuses it, stays disabled for public market data, its status recorded, and is never reached another way (no proxy, no other region). On those responses: whether the locked CCXT gives amounts as the venue's own text, and which streams it supports (D5).
- **Acceptance:** the stage record holds the readiness check and its result, the venue table (venue; terms checked; endpoint, date, result; status for public market data; trading eligibility, not established), the dependency review, and the CCXT findings; every Stage 1 check passes on the new lockfile; nothing else was contacted.

### U2 — Data contracts and configuration (checkpoint A)

- **Requirements:** ARCH-025, GOV-006, GOV-007, TEC-004; EXA-013; MKD-005, MKD-010; HLT-014; MIG-010, MIG-034; SEC-005; GOV-014.
- **Content:** SYS-02's canonical contracts on the kernel, with committed schemas: market metadata (increments, minimums, status), ticker, trade, book snapshot and sequenced update, OHLCV bar, funding rate, venue state, quality and freshness, quarantine record, untranslatable input; each with event and receive times, venue, market, evidence identifier, lineage (D5). `atp.config` gains portable settings (enabled venues and types, D1; fee schedules with source and date, D8; universe bounds and budgets, D10; regime timeframes, D9) and environment-specific ones (database address, its `server` credential's name, archive directory), each with MIG-034's record in the [developer guide](../development.md)'s "Configuration". Examples may name a venue once its adapter exists (Stage 1's named none, GOV-017).
- **Acceptance:** contract tests refuse unknown fields, floats and JSON numbers for amounts, bad times, malformed identifiers; schema snapshots; a negative test per new configuration rule; `atp config check` passes on every example.

### U3 — Measurement framework (checkpoint A)

- **Requirements:** PERF-008, PERF-009, PERF-010, PERF-018, PERF-020 (Stage 2's parts); TEC-010 (D7); SR-41.
- **Content:** `atp.measurement`, first, so later units are measured as built: named points tagged with path (market data; the detection part of the arbitrage and directional paths; monitoring) and component; durations from the monotonic clock; event-to-receipt delays from wall-clock times, marked unreliable beyond D3's drift limit; OpenTelemetry histograms; counters for errors, queue depth and delay, shed work. In baseline runs the samples also go to the cold-path archive, so p50, p95, p99, p99.9, maximum, and jitter are exact; a percentile is reported only with enough samples (p99.9: at least 1,000). Recording never blocks the hot path: a bounded buffer, drops counted. No target is set.
- **Acceptance:** with injected clocks and known samples the statistics are exact; too few samples report "insufficient"; the drift flag works; a full buffer drops and counts, never blocks.

### U4 — Exchange Adapter Layer, SYS-01 (checkpoint B)

- **Requirements:** EXA-001, EXA-003 to EXA-007, EXA-009, EXA-011 to EXA-015 (Stage 2's parts, section 3); ARCH-011; TEC-005; MKD-002.
- **Content:** `atp.exchange`: the adapter interface (markets and metadata; ticker, trade, book, OHLCV, funding, status streams; snapshots; server time); one adapter per enabled venue, without credentials, refusing private endpoints; symbol mapping; increments read exactly and applied through `atp.numeric.quantize`; amounts only from venue text (D5); each request's result an outcome (TIMEOUT for a timeout, UNKNOWN for an ambiguous answer); the rate-limit manager and connection resilience; a size limit on every message; TLS verification never off; untranslatable input passed to SYS-02 with its cause.
- **Acceptance:** per venue, on recorded responses replayed through the real adapter (D11): mapping, increments, exact amounts (a float or JSON number refused); no request over a limit under concurrency; backoff after a rate-limit refusal; reconnect after a drop; a missed heartbeat marks the feed stale; the circuit breaker opens and closes; a region refusal makes the venue unavailable, no other route tried. Structure test: CCXT only in `atp.exchange`, never given a credential; nothing in `src/` turns TLS verification off. Each enabled venue's opt-in live check recorded.

### U5 — Validation, normalization, quality, quarantine, freshness, lineage, clock drift (checkpoint B)

- **Requirements:** MKD-001, MKD-003 to MKD-006, MKD-008 to MKD-013 (Stage 2's parts); HLT-013, HLT-014; SR-12, SR-13, SR-14.
- **Content:** `atp.marketdata`: the checks of MKD-004, MKD-008, and MKD-013 (timestamps, fields, impossible prices, duplicates by evidence identifier, ordering, sequence gaps resolved by a fresh snapshot, consistency across sources and venues, outliers, clock problems); a deterministic, versioned quality score; freshness states per stream (D3); quarantine with cause and evidence, never passed on; lineage fields; a validated type only this module can create, the only input consumers accept. `atp.health` (SYS-29) compares venue server and event times with the local clock, tells a local drift from one venue's, and applies D3, its DATA DEGRADED signal kept for SYS-29's health state (CORE).
- **Acceptance:** a test per quarantine cause, freshness transition, and injected drift case; properties: deduplication idempotent, ordering stable, quality score repeatable for the same input and version; no quarantined or stale item reaches a consumer as eligible; structure test: only `atp.marketdata` creates validated data.

### U6 — Storage and retention (checkpoint C)

- **Requirements:** MKD-007; TEC-006, TEC-012 (market data); TEC-009; MKD-005, MKD-010; MIG-012 (rule).
- **Content:** `atp.storage`: connections with the `server` secret through `atp.config`'s secret source, the migration runner, the schema version. SYS-02's tables and migrations in `atp.marketdata` (D6): hypertables, `NUMERIC` amounts validated again when read, each table's contract identity and version recorded; writes batched off the hot path through a bounded queue, a failed or shed write recorded as a data gap, never silent. After V-18's period, data goes to Parquet with DuckDB, verified before the database copy is dropped.
- **Acceptance:** with testcontainers: migrations from empty and from each earlier version, a rerun a no-op; exact round trips through database and archive; a `NaN` in a `NUMERIC` column refused when read; a database outage gives FAILURE, TIMEOUT, or UNKNOWN and a recorded gap while the hot path runs on; archive failure keeps the rows.

### U7 — Quantitative Engine with the Fee and Slippage Engines, SYS-03 (checkpoint C)

- **Requirements:** QNT-001 to QNT-007 (Stage 2's parts); TEC-003; MKD-005; master execution constitution §30.
- **Content:** `atp.quant`: indicators (RSI, MACD, ATR, moving averages, volatility, returns, correlation), incremental where measurement shows a gain (PERF-005), floats allowed only here and in `atp.regime` (D5); spread, liquidity metrics, the Fee Engine (each result names its source, D8), and the Slippage Engine (a size walked through the book; market impact), in exact amounts; `atp.numeric` gains division with a named direction under N4 and N5 of the [numerical policy](../architecture/numerical-policy.md); each output carries an evidence identifier, its inputs' identifiers, and the calculation's version.
- **Acceptance:** each calculation against hand-worked values from its published definition; properties: fees grow with notional, a walked taker price is never better than the best, results exact and repeatable; structure test: floats only in D5's modules, none reaching an amount; division's property tests.

### U8 — Market Regime Engine, SYS-04 (checkpoint D)

- **Requirements:** RGM-001 to RGM-003, RGM-005 to RGM-008 (RGM-008: Stage 2's part).
- **Content:** `atp.regime`: D9's taxonomy; a versioned rule set over SYS-03's features with explicit thresholds; eligible data only (MKD-012); missing, stale, or quarantined input gives UNKNOWN, conflicting or low-confidence rules UNCERTAIN, never a guess; each result carries its rule version and inputs' identifiers; regime changes published for SYS-05.
- **Acceptance:** each state from constructed inputs, UNKNOWN and UNCERTAIN included; same inputs and version, same result; a new state is a new minor contract version (RGM-007).

### U9 — Opportunity Detection Engine, SYS-05 (checkpoint D)

- **Requirements:** OPP-001 to OPP-013, OPP-017 to OPP-024 (Stage 2's parts, section 3); PLT-022; SR-04, SR-48.
- **Content:** `atp.opportunity`: the universe from D1's venues and types, following listings and delistings; every market at ticker level; the Opportunity Filter and promotion to depth (D10); detectors for regime changes, anomalies, liquidity changes, and cross-venue price differences; candidates as contracts holding gross observations and evidence identifiers, no profit claim (TNP-031), not stored (OPP-016), consumed by nothing that acts; adaptive intensity within budgets and rate limits; several tiers at once.
- **Acceptance:** the universe follows listings and delistings; every market stays at ticker level; a large candidate neither stops scanning nor delays a smaller one; a small candidate waiting for depth keeps its place, never dropped; adaptive intensity stays within budgets and rate limits, changes nothing outside SYS-05, skips unchanged inputs; structure test: SYS-05 imports nothing that can act; nothing reads V-44.

### U10 — The process end to end, and the measured baselines (checkpoint E)

- **Requirements:** PERF-008, PERF-010, PERF-018, PERF-020; V-08, V-17 (baselines); PERF-019, PERF-021 (rules); EXA-015 live; TEC-010, TEC-011, OPS-010 (D7).
- **Content:** `atp.runtime` builds one process from the modules' public interfaces: bounded queues, market data ahead of cold-path work, shed work counted; `atp data run --env <name> --config-dir <dir>` starts and stops it cleanly; after a restart it resubscribes, takes new snapshots, and records the interval as a gap, assuming nothing about what venues did meanwhile (constitution Rule 157); backing services from D7's Compose definition. D2's baseline runs and report: per path, venue, and stream, what PERF-008, PERF-010, PERF-018, and PERF-020 allow here, with environment, host, region, period, and sample counts; proposed DESIGN TARGET values and V-08 and V-17 figures, labelled OBSERVED or PROPOSED, adopting nothing.
- **Acceptance:** a deterministic end-to-end replay in the tests; injected faults handled and measured as designed (disconnect, rate-limit refusal, malformed and float-number payloads, sequence gap, clock drift, database outage, overload); live runs and report recorded, each figure traceable to its samples.

### U11 — Traceability, security, stage record, closure (checkpoint E)

- **Requirements:** SEC-010; ARCH-030, ARCH-031, ARCH-040; GOV-024; master execution constitution §142 to §144, §152.
- **Content:** the stage record (section 6), created at the start of checkpoint A, updated at each checkpoint; requirement markers and the verification matrix; the [threat model](../security/threat-model.md)'s new trust boundaries (venues' public endpoints as untrusted input; the database) and Stage 2's security traceability table; interface sections in the specifications; the numerical policy, contract conventions, developer guide, architecture-to-repository map, values register (V-08 and V-17 "Not set" unless the owner sets them), feature-status rows, roadmap, project state; the §152 checklist, the company-grade order report ([owner decisions 14](../handoffs/owner-decisions-14-company-grade-order-and-traceability.md), §40) and the stage-transition audit ([owner decisions 15](../handoffs/owner-decisions-15-stage-transition-persistence-and-commit-integrity.md)), as at Stage 1's exit; the completion certificate, whose "approved to proceed" is the owner's.
- **Acceptance:** section 9.

## 5. Out of scope

Everything that belongs to a later stage, even where Stage 2 prepares for it (RMP-011; GOV-017):

- venue credentials and private endpoints (balances, orders, fills, positions, account fees and borrow data); orders of any kind; capital, risk, execution, reconciliation, portfolio, policy, audit and event history, the ledger (CORE and later); the maker-versus-taker selection (EXE-012; DEC-067, decision 4);
- the Opportunity Database or any candidate store, economic evaluation, net profit, ranking for capital (CORE); strategies, backtesting, paper trading (DIRECTIONAL TRADING); routes and transfers (ARBITRAGE); AI; Rust (TEC-002);
- NATS (D7), traces, Prometheus, Grafana, alerting, platform images, deployment, the configuration compiler, infrastructure as code beyond D7's file, host clock synchronization (OPERATIONALIZATION);
- setting any HARD LIMIT (V-08, V-17), or replacing V-06 and V-07, whose decision latency needs CORE's path; TC-09 and TC-10; venues whose public market data D1's verification does not permit (D1).

## 6. Outputs

| Output | Location | Kind |
|---|---|---|
| `atp.exchange`, `atp.marketdata`, `atp.quant`, `atp.regime`, `atp.opportunity`, `atp.health`, `atp.measurement`, `atp.storage`, `atp.runtime`; division in `atp.numeric`; `atp data run` | `src/atp/` (D4) | Implementation |
| Tests, recorded venue fixtures, opt-in live checks | `tests/` (D4, D11) | Tests |
| Committed schemas; migrations | `contracts/`; the owning module (D6) | Contracts; storage |
| Configuration examples with the new settings | `config/examples/` | Configuration |
| Development backing services | `infrastructure/development/` (D7) | Deployment definition (its start) |
| Baseline report; stage record and certificate | `docs/traceability/stage-02-baselines.md`, `docs/traceability/stage-02-data-foundation.md` | Verification evidence |
| The documents U11 updates | Their existing locations | Documentation |

Each new directory is created at the checkpoint that first puts a real artifact in it (constitution Rules 9–12).

## 7. Tests

| Level | What | Tool |
|---|---|---|
| Unit and contract | Each unit's rules; strictness, schema snapshots, amounts as text, time fields | pytest |
| Property | Exactness and division; deduplication and ordering; repeatable results; fee and slippage bounds; no candidate dropped for its size | Hypothesis |
| Type | Strict typing; CCXT confined | mypy |
| Replay | Recorded venue data through the real adapters and the whole process, deterministically | pytest |
| Integration | Storage, migrations, archive on PostgreSQL with TimescaleDB | pytest, testcontainers |
| Negative path, faults, concurrency | Every refusal and fault of U2 to U10; rate limits and bounded queues under load; the decimal context in every task | pytest |
| Structure | D4's import directions; CCXT, credentials, private endpoints, TLS; floats only where D5 allows; validated data only from `atp.marketdata`; V-44 read nowhere | pytest (`ast`) |
| Mutation (check 7) | Each enforced rule has a test that fails without it ([DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md), decision 6) | `tools/mutation/` |
| Live (opt-in) | Enabled venues' public endpoints and streams; baseline runs | Recorded in the stage record |
| Documentation; machine checks | The documentation checker, requirement comparison, and self-test; the developer guide's checks but `uv build`, on every pull request and on every push but one to a temporary backup or archive branch ([DEC-064](../decisions/DEC-064-retired-branches-kept-and-backup-commits-skip-checks.md), decision 2) | `tools/docs/`; the workflow |

No coverage figure is invented; every public function of the new modules has a test, checked in Gate 2 against the matrix.

## 8. Verification (the three gates, applied to Stage 2)

At every checkpoint, and for the whole stage before closure, as DEC-045 and [DEC-069](../decisions/DEC-069-owner-questions-and-efficiency-directive.md) apply them:

- **Gate 1 — technical:** lint, format, strict typing, all tests (database tests through testcontainers), the replay run, the package build, the documentation checker and requirement comparison, the matrix current; check 7 on changed rules, in full on each checkpoint's final tree.
- **Gate 2 — architecture and consistency:** one owner per module, imports one way (D4, structure test); one normalization layer, market-data store, configuration source, and measurement mechanism; no candidate store (OPP-016); no float in an amount, no credential, private endpoint, AI, or future-stage work; new values classified, new settings recorded (MIG-034); section 3.1 traced; documentation, roadmap, feature status, and project state agree with what was built.
- **Gate 3 — independent end-to-end and failure audit:** a reviewer briefed with the approved baseline (DEC-045, decision 1) works from a fresh clone: installs, runs every check and the replay, injects U10's faults, and tries to get a float into an amount, a stale or quarantined item to a consumer as eligible, a candidate to anything that acts, a credential read, scanning stopped by a large find, or a small candidate dropped; checks the baseline figures against their samples, none presented as a limit; checks that each marked test proves its requirement and that a fresh session could continue from the repository alone (master execution constitution §88). Findings are recorded with provenance (DEC-045, decision 2; [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 4).

## 9. Completion criteria

1. U1 to U11 meet their acceptance criteria.
2. The three gates pass for the whole stage, after every fix (DEC-032).
3. Section 3.1 is traced to implementation and tests in the matrix; sections 3.2 to 3.5 keep their dispositions, with no gap unexplained.
4. No secret, credential, private-endpoint call, or local path is in the repository; the secret test passes; U1's dependency review is recorded; U11's documentation is updated.
5. The baseline report is written, its figures traceable and labelled with their environment, its V-08 and V-17 proposals put to the owner.
6. The §152 checklist is complete; the company-grade order report and the stage-transition audit are made; the completion certificate is written.
7. Every checkpoint is committed, verified, and pushed.
8. The owner approves proceeding to Stage 3 planning (§143, §156).

## 10. Decisions this plan asks for

The owner decided them on 2026-11-17 ([DEC-073](../decisions/DEC-073-stage-2-plan-approved-with-changes.md)): D3 to D12 as recommended, subject to the existing canonical requirements and the owner's conditions (DEC-073); D1 and D2 as the owner decided them, stated in place of their recommendations.

| # | Decision | Recommendation | Alternatives | Why |
|---|---|---|---|---|
| D1 | Venues and instrument types for public market data | Decided by the owner (DEC-073): the five initial venues (EXA-005) stay the candidate market-data sources, the architecture open to more (EXA-006), none assumed available. A venue's support, lawful access to its public market data, the account's eligibility, and trading authorization are kept apart. A venue's public market data is monitored only where U1 verifies that credential-free, read-only access to it is permitted by applicable law and the venue's terms and answers from the environment without any workaround; a venue whose access or eligibility is unresolved stays disabled for that operation, its status recorded; public access is never taken as permission to trade; before any later trading activation, the account's eligibility, supported instruments, and jurisdiction, and every applicable risk and readiness gate, are verified. As the plan recommended, the plan's reading of OPP-009 within the overall technical direction the owner approved (DEC-073, decision 3): monitoring covers PLT-011's three types (spot, perpetual futures, margin) where the venue publishes them (OPP-009), and PLT-012 keeps gating live trading | The owner confirming which venues the account may use (the plan's recommendation); all five, checked on documented examples only; spot only | Access depends on the operator's jurisdiction and the venue's terms (EXA-007; [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md)), and access to public data and eligibility to trade are different questions; an adapter never run against its venue is unverified (Rule 128) |
| D2 | Where the live work runs; what its baselines are for | Decided by the owner (DEC-073): before any work that depends on infrastructure, a focused environment-readiness check at U1 determines the smallest compliant solution with the approved technology stack and the infrastructure already available; where the environment needed cannot be provided, the builder reports the exact limitation, the safest viable alternative, the dependencies, and any decision or expense needing the owner's approval, does not attempt again a configuration known to be unavailable, and buys no infrastructure without the owner's approval. As the plan stated and the requirements set: each baseline is labelled with its environment, host, region, period, and sample counts and is a first baseline only; V-08 and V-17 stay "Not set" until the owner sets them as HARD LIMITs in policy by RSK-039's human-controlled change, once CORE builds the Policy System; production's come from the production host (OPERATIONALIZATION; hosting location undecided) | This cloud environment as observed, without a readiness check (the plan's recommendation); an environment the owner provides (MIG-004 allows it); V-08 and V-17 set from these baselines | Targets come from evidence measured where they apply (PERF-006, PERF-018, SR-41); hard limits are the safety floor (RSK-034); no cycle is spent on a configuration known to be unavailable |
| D3 | Data-quality limits before V-17; the drift response | Provisional STALE and INVALID ages per data type and a drift limit, IMPLEMENTATION CHOICE values set from the first live measurements (U4, U5), used only to mark data in Stage 2 and never presented as V-17. A drifting venue clock gives its data the quarantine cause "clock problems" (MKD-013); a drifting local clock marks cross-system delays unreliable; both raise DATA DEGRADED for SYS-29 (CORE); alerts come with SYS-28 (SR-14) | Ages only until V-17 exists; V-17 set now, unmeasured | MKD-006 and MKD-012 need a limit to mark data; nothing trades in Stage 2; HLT-013's specification leaves the response to this plan |
| D4 | Locations and module boundaries | Section 6's modules, one per system, SYS-29's drift detection in `atp.health`; `atp.measurement` the performance set's (owner of PERF-008 to PERF-010; SYS-28 later collects from it, D-52); `atp.storage` and `atp.runtime` platform architecture's; tests in `tests/<module>/`, fixtures in `tests/fixtures/venues/`, live checks in `tests/live/`, not collected by default. Imports one way: SYS-01 imports SYS-02's contracts, never the reverse; quant → marketdata; regime → quant, marketdata; opportunity → marketdata, quant, regime; only `atp.runtime` joins them, and only `atp.cli` imports it (beside `atp.config`) | One `atp.data` package; a separate contracts package | Visible ownership (Rules 11, 15; TEC-008); venue code isolated (EXA-011) without import cycles; database access shared on purpose (Rule 82) |
| D5 | Contracts: time, identifiers, amounts, floats | Event times as integer nanoseconds since the Unix epoch, UTC, the venue's resolution recorded; durations from the monotonic clock; evidence identifiers derived from venue, stream, market, and the venue's event identifier or sequence (else time and content digest), so a duplicate keeps its identifier; amounts only from venue text through `atp.numeric` (where CCXT cannot give it, TEC-005's native-client exception, recorded); stored data names its contract and version per table and per archive file, which the contract conventions left to "the first messaging and storage"; floats only in `atp.quant`'s indicators and `atp.regime` (TEC-003) | Datetimes (microseconds only); random identifiers; CCXT's numbers; identity on every row | Lossless times; repeatable deduplication; exactness (numerical policy, N1); less storage |
| D6 | Storage, migrations, archive | As U6 describes: hypertables, `NUMERIC` amounts revalidated on read; forward-only, versioned SQL migrations run by one runner in `atp.storage`, with the rollback strategy §59 requires (a restorable backup before any migration that rewrites stored rows, MIG-012's restore); after V-18, Parquet through DuckDB (one of TEC-006's two), amounts as text, as N6 has them in JSON | Alembic with SQLAlchemy; Polars; fixed-scale decimals in Parquet | No migration framework to add; exact at any scale; SQL over Parquet without a data-frame layer |
| D7 | One process; messaging, observability, deployment | One process (TEC-008), its parts linked by bounded in-process queues, not a message bus; NATS JetStream (TEC-007) when a second process needs fan-out; OpenTelemetry metrics (TEC-010) and standard-library JSON logs, without secrets, refused input, or a refusal's frame variables; no traces, Prometheus, Grafana, or platform image yet; a Compose file for the development backing services (PostgreSQL 16 with TimescaleDB, image by digest, password from the environment) at `infrastructure/development/`, the start of OPS-010's one definition | NATS now; the whole TEC-010 stack now; the database started by hand | No message pathway before it is needed (master execution constitution §28, §68); the approved stack, not a home-made one; Compose is TEC-011's tool; OPS-010 wants the definition in the repository |
| D8 | Fee data in Stage 2 | Each venue's published schedule (base tier, maker and taker per type) as that venue's configuration with source and date, or a public endpoint where one exists (unknown per venue); each fee result names its source; the account's own rates come with CORE | No Fee Engine until CORE; a library's built-in figures | QNT-005 needs a schedule now; a configured one is traceable (MIG-034); a library's figure is not the venue's statement |
| D9 | Regime taxonomy | The union of RGM-002's and RGM-007's lists, "panic/stress" one state: TRENDING, RANGING, HIGH_VOLATILITY, LOW_VOLATILITY, PANIC_STRESS, ABNORMAL, UNCERTAIN, UNKNOWN; per market and configured timeframe, one trend state and one volatility state, PANIC_STRESS and ABNORMAL overriding both; thresholds IMPLEMENTATION CHOICE values from measured distributions | One label per market; PANIC and STRESS apart; thresholds in policy | The specification finalizes the taxonomy in this stage; one label would force combined conditions into one class (RGM-003) |
| D10 | Opportunity monitoring rules | Promotion to depth by deterministic, versioned filter rules over price and spread changes, cross-venue relationships, liquidity, volatility, and regime changes, ordered by observed gross size and quality as a preference only, no candidate dropped for being small (SR-48); "significant" means beyond a detector's threshold relative to the market's own measured distribution; thresholds, tier limits, and budgets (depth subscriptions per venue within its limits, scan frequency) are IMPLEMENTATION CHOICE values from measurement; adaptive intensity moves only frequency, depth allocation, and analysis depth within them | Depth for every market (beyond venue limits); a minimum gross spread for promotion (a floor OPP-022 forbids) | The specification leaves these to this plan; they keep OPP-021 to OPP-024 testable |
| D11 | How venue code is tested | Recorded public responses and streams, captured where D1's verification permits, labelled (venue, endpoint, date), small, scanned by the secret test, replayed through the real adapters; live checks opt-in, outside the machine checks, results recorded; database tests through testcontainers, locally and in the machine checks (Docker on the runners to be confirmed) | Live venue calls in the machine checks; hand-written fixtures only | Machine checks stay deterministic and independent of venue reachability (GOV-023); recorded data tests real formats |
| D12 | Dependencies Stage 2 adds | Runtime: CCXT (TEC-005); psycopg 3, a PostgreSQL driver the stack does not name (typed and asynchronous, to be confirmed on the locked version); DuckDB (TEC-006); OpenTelemetry API and SDK (TEC-010). Development: testcontainers (TEC-009). Service: PostgreSQL 16 (V-22) with TimescaleDB. No asynchronous test plugin (`asyncio.run` in ordinary tests); no NATS client (D7). Versions fixed at checkpoint A, the image by digest, each reviewed for advisories and licenses. If the locked CCXT fails strict mypy or `filterwarnings = error`, the exception is confined to `atp.exchange` and recorded with its reason in the stage record | asyncpg; Alembic; pytest-asyncio | A dependency the stack does not list needs a decision record (Rules 99–101); fewer packages to review |

## 11. Sequence and checkpoints

| Checkpoint | Units | Depends on |
|---|---|---|
| A | U1 readiness, dependencies, and venue verification; U2 contracts and configuration; U3 measurement | The owner's approval of this plan (DEC-073); U1's readiness check before any work that depends on infrastructure (D2); D1's verification of a venue before its data is used |
| B | U4 adapters; U5 validation and clock drift | A (live checks: U1's venue verification) |
| C | U6 storage; U7 quantitative engine | B |
| D | U8 regime; U9 opportunity detection | C |
| E | U10 the process and baselines; U11 closure | A to D (U10's runs: D2's environment) |

**Order changed** on 2026-11-21 by [DEC-080](../decisions/DEC-080-checkpoint-c-before-the-venue-adapters.md), at the owner's request: checkpoint C (U7, then U6) is built before checkpoint B's venue adapters, which follow once a venue is verified and a server approved; checkpoint B stays open until they pass their gates.

Each checkpoint: work → three gates → commit → push (DEC-032); a failed gate stops the sequence until fixed and re-verified (master execution constitution §19). Uncommitted work is backed up as [DEC-057](../decisions/DEC-057-progress-continuity-no-loss-and-recovery.md) (decision 4), [DEC-064](../decisions/DEC-064-retired-branches-kept-and-backup-commits-skip-checks.md) (decision 2), and [DEC-071](../decisions/DEC-071-one-reusable-backup-branch.md) provide; convergence is classified from this plan's approval (DEC-057, decision 3). On approval, the feature-status table gets one row per feature of U2 to U10.

## 12. Risks and limits

| Risk | Effect | Handling |
|---|---|---|
| A venue's terms or region refuse access to its public market data here, or that access turns on information not yet available | That venue cannot be used; fewer venues to compare | It stays disabled for public market data, its status recorded (EXA-007, D1); never worked around; the owner is asked only for genuinely missing owner-level information |
| No Docker daemon or TimescaleDB here (observed 2026-11-17) | No storage, database tests, or baseline runs here | U1's readiness check finds the smallest compliant solution with what is available; where none exists, the report D2 requires goes to the owner, the work that needs it waits at its last verified checkpoint, and the configuration is not attempted again (Rules 94, 209) |
| CCXT gives amounts as floats, or its typing or warnings fail strict mypy or `filterwarnings = error` (to be confirmed at U1) | Lost exactness; failed checks | Amounts only from venue text (D5), else the native-client exception; exceptions confined to `atp.exchange`, each recorded |
| Development baselines differ from production | Limits from the wrong evidence | Labelled per environment; production's from the production host; V-08 and V-17 set only by the owner (D2) |
| A usage or background-run limit cuts a run short | Short baseline periods | Runs recorded per period, nothing claimed beyond the samples; if the environment D2 needs cannot be provided here, the report D2 requires goes to the owner |
| V-08's decision latency needs CORE's path | V-08 incomplete after Stage 2 | Stated in section 3.2; no figure invented |
| Whole-universe monitoring meets venue rate limits | Refusals or bans | Rate-limit manager and budgets (EXA-014, D10), measured |
| Storage grows faster than expected | Disk pressure (Rule 150) | V-18's retention, the archive, storage measured (PERF-020) |
| Float indicators differ across platforms | A regime threshold could flip | Repeatability claimed per platform; floats kept to indicators (D5) |
| A venue changes its API | An adapter breaks | Fixtures and live checks find it; the fix is a new checkpoint |
| Scope creep toward CORE (account endpoints, a candidate store, net profit) | Future work in Stage 2 (RMP-011) | Section 5; Gate 2 |
