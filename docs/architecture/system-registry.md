# System and Capability Registry

> **Status:** ACTIVE — derived from Handoff Part 1, updated 2026-09-30 with decisions DEC-006 to DEC-020. No system is implemented.
>
> The single list of every system and capability named in Part 1: what it is, which document is canonical for it, which requirement IDs it owns, and which §95 roadmap stage it belongs to. Names are the handoff's own. No system has been invented; capabilities that Part 1 names without an owning system are marked. Every entry must meet the §92 boundary fields (ARCH-012). Each specification records the fields Part 1 supplies.

## Registry

| ID | Name (as in handoff) | Category | Canonical document | Req. prefix | §95 stage | Classification |
|---|---|---|---|---|---|---|
| SYS-01 | Exchange Adapter Layer | Shared infrastructure | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | EXA | DATA FOUNDATION | Confirmed; venues Binance, OKX, Coinbase, Bybit, KuCoin ([DEC-008](../decisions/DEC-008-venues-and-trading-universe.md)) |
| SYS-02 | Market-Data Infrastructure | Shared infrastructure | [systems/market-data.md](../systems/market-data.md) | MKD | DATA FOUNDATION | Confirmed |
| SYS-03 | Quantitative Engine | Shared infrastructure | [systems/quantitative-engine.md](../systems/quantitative-engine.md) | QNT | DATA FOUNDATION | Confirmed |
| SYS-04 | Market Regime Engine | Shared infrastructure | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | RGM | DATA FOUNDATION | Confirmed; deterministic (RGM-005, [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md)) |
| SYS-05 | Opportunity Detection Engine (incl. whole-universe monitoring) | Shared infrastructure | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | OPP | DATA FOUNDATION | Confirmed; §08 and §09 are one system (OPP-010, [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md)) |
| SYS-06 | True Net-Profit Engine | Shared infrastructure | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | TNP | CORE TRADING FOUNDATION (ARBITRAGE adds cost components, [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-07 | Global Capital Authority | Shared infrastructure | [systems/capital-management.md](../systems/capital-management.md) | CAP | CORE TRADING FOUNDATION | Confirmed |
| SYS-08 | Portfolio Management | Shared infrastructure | [systems/portfolio-management.md](../systems/portfolio-management.md) | PRT | CORE TRADING FOUNDATION | Confirmed |
| SYS-09 | Deterministic Risk Engine (incl. risk hierarchy, no-trade outcomes) | Shared infrastructure | [risk/risk-engine.md](../risk/risk-engine.md) | RSK | CORE TRADING FOUNDATION | Confirmed; owns kill switches (RSK-008, [DEC-012](../decisions/DEC-012-safety-architecture.md)); owns safety levels and the emergency controller (RSK-015, RSK-020, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)) |
| SYS-10 | Execution Engine | Shared infrastructure | [systems/execution-engine.md](../systems/execution-engine.md) | EXE | CORE TRADING FOUNDATION | Confirmed; also executes rebalancing transfers (EXE-009, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)) |
| SYS-11 | Recovery and Reconciliation | Shared infrastructure | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | REC | CORE TRADING FOUNDATION; hardened in OPERATIONALIZATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed; automatic 24/7 recovery and execution lease (REC-010 to REC-013, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)) |
| SYS-12 | Policy System | Shared infrastructure | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | POL | CORE TRADING FOUNDATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-13 | Natural Language Policy Interface | AI-assisted interface into SYS-12 | [systems/policy/natural-language-policy-interface.md](../systems/policy/natural-language-policy-interface.md) | NLP | AI INTELLIGENCE | Confirmed |
| SYS-14 | Strategy Management (Strategy Factory, lifecycle, versioning) | Shared infrastructure | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | STR | DIRECTIONAL TRADING, shared; ARBITRAGE depends on it ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-15 | Backtesting | Shared infrastructure | [systems/strategy/backtesting.md](../systems/strategy/backtesting.md) | BKT | DIRECTIONAL TRADING, shared; ARBITRAGE depends on it ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-16 | Paper Trading | Shared infrastructure | [systems/strategy/paper-trading.md](../systems/strategy/paper-trading.md) | PAP | DIRECTIONAL TRADING, shared; ARBITRAGE depends on it ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-17 | Directional Trading System | Trading system | [systems/directional-trading.md](../systems/directional-trading.md) | DIR | DIRECTIONAL TRADING | Confirmed |
| SYS-18 | Cross-Exchange Arbitrage System | Trading system | [systems/arbitrage/cross-exchange-arbitrage.md](../systems/arbitrage/cross-exchange-arbitrage.md) | XAR | ARBITRAGE | Confirmed |
| SYS-19 | Triangular Arbitrage System | Trading system | [systems/arbitrage/triangular-arbitrage.md](../systems/arbitrage/triangular-arbitrage.md) | TAR | ARBITRAGE | Confirmed |
| SYS-20 | Arbitrage Intelligence | Arbitrage-shared capabilities | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARB | ARBITRAGE | Confirmed; several capabilities overlap platform systems (see document) |
| SYS-21 | Performance Controller | Shared infrastructure | [systems/performance-controller.md](../systems/performance-controller.md) | PFC | ARBITRAGE, platform-wide ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-22 | AI Intelligence Layer (incl. Hallucination Firewall, output contract, multi-agent validation, calibration) | AI | [ai/ai-architecture.md](../ai/ai-architecture.md), [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AIL, AIV | AI INTELLIGENCE | Confirmed; AI gateway defined (AIL-006, [DEC-013](../decisions/DEC-013-ai-organization.md)) |
| SYS-23 | AI Agents | AI | [ai/agents.md](../ai/agents.md) | AGT | AI INTELLIGENCE | Confirmed; five agents (AGT-016, [DEC-013](../decisions/DEC-013-ai-organization.md)) |
| SYS-24 | Model Router | AI | [ai/model-management.md](../ai/model-management.md) | RTR | AI INTELLIGENCE | Confirmed; deterministic (RTR-003, [DEC-013](../decisions/DEC-013-ai-organization.md)) |
| SYS-25 | AI Cost Manager | AI support service (deterministic; listed as an agent in §54) | [ai/model-management.md](../ai/model-management.md) | COST | AI INTELLIGENCE | Confirmed; deterministic service (COST-002, [DEC-013](../decisions/DEC-013-ai-organization.md)) |
| SYS-26 | Model Evaluation (Model Evaluation Agent in §54) | AI support service (deterministic; listed as an agent in §54) | [ai/model-management.md](../ai/model-management.md) | MEV | AI INTELLIGENCE ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed; deterministic service (MEV-003, [DEC-013](../decisions/DEC-013-ai-organization.md)) |
| SYS-27 | AI Memory / Project Knowledge | AI | [ai/ai-memory.md](../ai/ai-memory.md) | MEM | AI INTELLIGENCE | Confirmed |
| SYS-28 | Monitoring and Observability (incl. alerting and reporting) | Operations | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | MON | OPERATIONALIZATION | Confirmed; owns alerting and reporting ([DEC-017](../decisions/DEC-017-reporting-alerting-and-performance-targets.md)) |
| SYS-29 | System Health State Machine (incl. failure handling, controlled degradation) | Operations | [operations/system-health.md](../operations/system-health.md) | HLT | CORE TRADING FOUNDATION; hardened in OPERATIONALIZATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed; state machine formalized (HLT-007 to HLT-009, [DEC-012](../decisions/DEC-012-safety-architecture.md)) |
| SYS-30 | Auditability / Event and Decision History | Capability — implementing system not named | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | AUD | CORE TRADING FOUNDATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-31 | Security Architecture | Cross-cutting | [security/security-architecture.md](../security/security-architecture.md) | SEC | FOUNDATION ("Security foundation") | Confirmed |
| SYS-32 | Platform Account / Custody | Conditional | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | CUS | None — FUTURE | **FUTURE**: not built; single operator ([DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md)) |
| SYS-33 | Ledger / Accounting Foundation (internal trading ledger) | Shared infrastructure | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | LED | CORE TRADING FOUNDATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed (LED-004 to LED-007, [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md)) |

## Cross-cutting requirement sets (not systems)

| Prefix | Scope | Canonical document |
|---|---|---|
| PLT | Platform identity, objective, priority order, return expectations | [product/platform-overview.md](../product/platform-overview.md) |
| MODE | Operating modes (owned by the Policy System, POL-008) | [product/operating-modes.md](../product/operating-modes.md) |
| ARCH | Structural principles, precision, ownership and traceability rules | [architecture/overview.md](overview.md) |
| PERF | Performance, latency, continuous operation | [architecture/performance-and-latency.md](performance-and-latency.md) |
| OPS | Operational readiness, development while online | [operations/deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) |
| RMP | Roadmap stage classification and sequence | [roadmap/roadmap.md](../roadmap/roadmap.md) |
| TEC | Technology stack | [architecture/technology-stack.md](technology-stack.md) |

## Named in Part 1 but not defined — how each was resolved

None of these became a new system (§00 item 21). Each was assigned to an existing owner.

| Name | Where it appears | Resolution |
|---|---|---|
| Reporting and alerts | §01, §02 item 22, §95 | SYS-28 Monitoring and Observability (MON-007, MON-008, [DEC-017](../decisions/DEC-017-reporting-alerting-and-performance-targets.md)) |
| AI gateway | §95 | Component of SYS-22 (AIL-006, [DEC-013](../decisions/DEC-013-ai-organization.md)) |
| Global safety architecture | §47 | Risk Engine + System Health (RSK-008, HLT-010, [DEC-012](../decisions/DEC-012-safety-architecture.md)) |
| Storage | §03, §04, §10, §95, §97 | PostgreSQL / TimescaleDB / Parquet ([technology stack](technology-stack.md), [DEC-009](../decisions/DEC-009-technology-stack.md)); each system owns its own data |
| Logging | §04 | SYS-28 operational logs (MON-009), separate from audit (AUD-006) |
| Canary | §34, §38, §95 | SYS-14 (STR-011, [DEC-015](../decisions/DEC-015-modes-canary-and-policy-governance.md)) |
| Market universe | §08, §95 | SYS-05 (OPP-009, [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md)) with exclusions from SYS-12 |
