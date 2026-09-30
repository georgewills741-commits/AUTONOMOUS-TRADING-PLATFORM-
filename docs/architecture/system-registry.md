# System and Capability Registry

> **Status:** ACTIVE — derived from Handoff Part 1 on 2026-09-30. No system is implemented.
>
> The single list of every system and capability named in Part 1: what it is, which document is canonical for it, which requirement IDs it owns, and which §95 roadmap stage it belongs to. Names are the handoff's own. No system has been invented; capabilities that Part 1 names without an owning system are marked. Every entry must meet the §92 boundary fields (ARCH-012). Each specification records the fields Part 1 supplies.

## Registry

| ID | Name (as in handoff) | Category | Canonical document | Req. prefix | §95 stage | Classification |
|---|---|---|---|---|---|---|
| SYS-01 | Exchange Adapter Layer | Shared infrastructure | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | EXA | DATA FOUNDATION | Confirmed; venue list requires confirmation |
| SYS-02 | Market-Data Infrastructure | Shared infrastructure | [systems/market-data.md](../systems/market-data.md) | MKD | DATA FOUNDATION | Confirmed |
| SYS-03 | Quantitative Engine | Shared infrastructure | [systems/quantitative-engine.md](../systems/quantitative-engine.md) | QNT | DATA FOUNDATION | Confirmed |
| SYS-04 | Market Regime Engine | Shared infrastructure | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | RGM | DATA FOUNDATION | Confirmed; method open (OQ-10) |
| SYS-05 | Opportunity Detection Engine (incl. whole-universe monitoring) | Shared infrastructure | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | OPP | DATA FOUNDATION | Confirmed; merging §08 and §09 into one system is PROPOSED (DUP-05) |
| SYS-06 | True Net-Profit Engine | Shared infrastructure | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | TNP | CORE TRADING FOUNDATION (also ARBITRAGE, CF-05) | Confirmed |
| SYS-07 | Global Capital Authority | Shared infrastructure | [systems/capital-management.md](../systems/capital-management.md) | CAP | CORE TRADING FOUNDATION | Confirmed |
| SYS-08 | Portfolio Management | Shared infrastructure | [systems/portfolio-management.md](../systems/portfolio-management.md) | PRT | CORE TRADING FOUNDATION | Confirmed |
| SYS-09 | Deterministic Risk Engine (incl. risk hierarchy, no-trade outcomes) | Shared infrastructure | [risk/risk-engine.md](../risk/risk-engine.md) | RSK | CORE TRADING FOUNDATION | Confirmed; placing §27 here is PROPOSED |
| SYS-10 | Execution Engine | Shared infrastructure | [systems/execution-engine.md](../systems/execution-engine.md) | EXE | CORE TRADING FOUNDATION | Confirmed |
| SYS-11 | Recovery and Reconciliation | Shared infrastructure | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | REC | CORE TRADING FOUNDATION and OPERATIONALIZATION (CF-05) | Confirmed |
| SYS-12 | Policy System | Shared infrastructure | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | POL | **Not mapped** (CF-06) | Confirmed |
| SYS-13 | Natural Language Policy Interface | AI-assisted interface into SYS-12 | [systems/policy/natural-language-policy-interface.md](../systems/policy/natural-language-policy-interface.md) | NLP | AI INTELLIGENCE | Confirmed |
| SYS-14 | Strategy Management (Strategy Factory, lifecycle, versioning) | Shared infrastructure | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | STR | DIRECTIONAL TRADING (CF-05) | Confirmed |
| SYS-15 | Backtesting | Shared infrastructure | [systems/strategy/backtesting.md](../systems/strategy/backtesting.md) | BKT | DIRECTIONAL TRADING (CF-05) | Confirmed |
| SYS-16 | Paper Trading | Shared infrastructure | [systems/strategy/paper-trading.md](../systems/strategy/paper-trading.md) | PAP | DIRECTIONAL TRADING (CF-05) | Confirmed |
| SYS-17 | Directional Trading System | Trading system | [systems/directional-trading.md](../systems/directional-trading.md) | DIR | DIRECTIONAL TRADING | Confirmed |
| SYS-18 | Cross-Exchange Arbitrage System | Trading system | [systems/arbitrage/cross-exchange-arbitrage.md](../systems/arbitrage/cross-exchange-arbitrage.md) | XAR | ARBITRAGE | Confirmed |
| SYS-19 | Triangular Arbitrage System | Trading system | [systems/arbitrage/triangular-arbitrage.md](../systems/arbitrage/triangular-arbitrage.md) | TAR | ARBITRAGE | Confirmed |
| SYS-20 | Arbitrage Intelligence | Arbitrage-shared capabilities | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARB | ARBITRAGE | Confirmed; several capabilities overlap platform systems (see document) |
| SYS-21 | Performance Controller | Shared infrastructure | [systems/performance-controller.md](../systems/performance-controller.md) | PFC | ARBITRAGE (CF-05) | Confirmed |
| SYS-22 | AI Intelligence Layer (incl. Hallucination Firewall, output contract, multi-agent validation, calibration) | AI | [ai/ai-architecture.md](../ai/ai-architecture.md), [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AIL, AIV | AI INTELLIGENCE | Confirmed; "AI gateway" undefined (OQ-14) |
| SYS-23 | AI Agents | AI | [ai/agents.md](../ai/agents.md) | AGT | AI INTELLIGENCE | **Roster PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION** (OQ-11) |
| SYS-24 | Model Router | AI | [ai/model-management.md](../ai/model-management.md) | RTR | AI INTELLIGENCE | Confirmed; deterministic implementation recommended (TC-02) |
| SYS-25 | AI Cost Manager | AI (listed as an agent in §54) | [ai/model-management.md](../ai/model-management.md) | COST | AI INTELLIGENCE | Confirmed; agent vs deterministic service open (TC-02) |
| SYS-26 | Model Evaluation (Model Evaluation Agent in §54) | AI (listed as an agent in §54) | [ai/model-management.md](../ai/model-management.md) | MEV | **Not mapped** (CF-05) | Confirmed; agent vs deterministic service open (TC-02) |
| SYS-27 | AI Memory / Project Knowledge | AI | [ai/ai-memory.md](../ai/ai-memory.md) | MEM | AI INTELLIGENCE | Confirmed |
| SYS-28 | Monitoring and Observability | Operations | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | MON | OPERATIONALIZATION | Confirmed |
| SYS-29 | System Health State Machine (incl. failure handling, controlled degradation) | Operations | [operations/system-health.md](../operations/system-health.md) | HLT | **Not mapped** (CF-05) | Confirmed; final state machine open (OQ-07) |
| SYS-30 | Auditability / Event and Decision History | Capability — implementing system not named | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | AUD | **Not mapped** (CF-05) | Confirmed |
| SYS-31 | Security Architecture | Cross-cutting | [security/security-architecture.md](../security/security-architecture.md) | SEC | FOUNDATION ("Security foundation") | Confirmed |
| SYS-32 | Platform Account / Custody | Conditional | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | CUS | **Not mapped** | **PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION** (OQ-01) |
| SYS-33 | Ledger / Accounting Foundation | Conditional | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | LED | **Not mapped** | Conditional on OQ-01 / OQ-02 |

## Cross-cutting requirement sets (not systems)

| Prefix | Scope | Canonical document |
|---|---|---|
| PLT | Platform identity, objective, priority order, return expectations | [product/platform-overview.md](../product/platform-overview.md) |
| MODE | Operating modes (owner not assigned, OQ-08) | [product/operating-modes.md](../product/operating-modes.md) |
| ARCH | Structural principles, precision, ownership and traceability rules | [architecture/overview.md](overview.md) |
| PERF | Performance, latency, continuous operation | [architecture/performance-and-latency.md](performance-and-latency.md) |
| OPS | Operational readiness, development while online | [operations/deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) |
| RMP | Roadmap stage classification | [roadmap/roadmap.md](../roadmap/roadmap.md) |

## Named in Part 1 but not defined

Recorded so that none of them disappears. None of them is registered as a system, because that would invent one (§00 item 21).

| Name | Where it appears | Tracking |
|---|---|---|
| Reporting and alerts | §01, §02 item 22, §95 | OQ-13 |
| AI gateway | §95 | OQ-14 |
| Global safety architecture | §47 | OQ-06, DUP-04 |
| Storage | §03, §04, §10, §95, §97 | OQ-22 |
| Logging | §04 | OQ-22 |
| Canary | §34, §38, §95 | OQ-09 |
| Market universe (definition and configuration) | §08, §95 | OQ-03 |
