# System and Capability Registry

> **Status:** ACTIVE — derived from Handoff Part 1, updated 2026-09-30 with decisions DEC-006 to DEC-031 and Handoff Parts 2 and 3, and on 2026-10-02 with DEC-035 (the future feature registry row); two "since replaced" pointers added by the [master knowledge-base audit](../traceability/master-knowledge-base-audit-2026-10-02.md). No system is implemented.
>
> The single list of every system and capability named in Parts 1, 2, and 3: what it is, which document is canonical for it, which requirement IDs it owns, and which §95 roadmap stage it belongs to. Names are the handoff's own. No system has been invented; capabilities that a handoff names without an owning system are marked. Part 2 added one system (SYS-34) and no other: every other Part 2 name was assigned to an existing owner (table at the end, [DEC-024](../decisions/DEC-024-part-2-reconciliation.md)). Every entry must meet the §92 boundary fields (ARCH-012). Each specification records the fields Part 1 supplies.

## Registry

| ID | Name (as in handoff) | Category | Canonical document | Req. prefix | §95 stage | Classification |
|---|---|---|---|---|---|---|
| SYS-01 | Exchange Adapter Layer | Shared infrastructure | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | EXA | DATA FOUNDATION | Confirmed; venues Binance, OKX, Coinbase, Bybit, KuCoin ([DEC-008](../decisions/DEC-008-venues-and-trading-universe.md)) |
| SYS-02 | Market-Data Infrastructure | Shared infrastructure | [systems/market-data.md](../systems/market-data.md) | MKD | DATA FOUNDATION | Confirmed |
| SYS-03 | Quantitative Engine (incl. Fee Engine, Slippage Engine) | Shared infrastructure | [systems/quantitative-engine.md](../systems/quantitative-engine.md) | QNT | DATA FOUNDATION | Confirmed; Fee and Slippage Engines are its components (QNT-007, [DEC-024](../decisions/DEC-024-part-2-reconciliation.md)) |
| SYS-04 | Market Regime Engine | Shared infrastructure | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | RGM | DATA FOUNDATION | Confirmed; deterministic (RGM-005, [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md)) |
| SYS-05 | Opportunity Detection Engine (incl. whole-universe monitoring, Opportunity Filter, Opportunity Database) | Shared infrastructure | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | OPP | DATA FOUNDATION; Opportunity Database in CORE TRADING FOUNDATION | Confirmed; §08 and §09 are one system (OPP-010, [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md)); owns the one Opportunity Database (OPP-016, [DEC-024](../decisions/DEC-024-part-2-reconciliation.md)) |
| SYS-06 | True Net-Profit Engine | Shared infrastructure | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | TNP | CORE TRADING FOUNDATION (ARBITRAGE adds cost components, [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-07 | Global Capital Authority | Shared infrastructure | [systems/capital-management.md](../systems/capital-management.md) | CAP | CORE TRADING FOUNDATION | Confirmed |
| SYS-08 | Portfolio Management | Shared infrastructure | [systems/portfolio-management.md](../systems/portfolio-management.md) | PRT | CORE TRADING FOUNDATION | Confirmed |
| SYS-09 | Deterministic Risk Engine (incl. risk hierarchy, no-trade outcomes) | Shared infrastructure | [risk/risk-engine.md](../risk/risk-engine.md) | RSK | CORE TRADING FOUNDATION | Confirmed; owns kill switches (RSK-008, [DEC-012](../decisions/DEC-012-safety-architecture.md)); owns safety levels and the emergency controller (RSK-015, RSK-020, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)); cause-based kill-switch recovery (RSK-021 to RSK-025, [DEC-021](../decisions/DEC-021-kill-switch-recovery.md)) |
| SYS-10 | Execution Engine | Shared infrastructure | [systems/execution-engine.md](../systems/execution-engine.md) | EXE | CORE TRADING FOUNDATION | Confirmed; also executes rebalancing transfers (EXE-009, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)) |
| SYS-11 | Recovery and Reconciliation (incl. active-instance and split-brain protection) | Shared infrastructure | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | REC | CORE TRADING FOUNDATION; hardened in OPERATIONALIZATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed; automatic 24/7 recovery and execution lease (REC-010 to REC-013, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)); staged restart recovery (REC-014 to REC-018, [DEC-022](../decisions/DEC-022-restart-recovery-sequence.md)); split-brain protection across hosts and high availability (REC-019 to REC-024; [DEC-030](../decisions/DEC-030-high-availability-and-single-active-copy.md)) |
| SYS-12 | Policy System | Shared infrastructure | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | POL | CORE TRADING FOUNDATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-13 | Natural Language Policy Interface | AI-assisted interface into SYS-12 | [systems/policy/natural-language-policy-interface.md](../systems/policy/natural-language-policy-interface.md) | NLP | AI INTELLIGENCE | Confirmed |
| SYS-14 | Strategy Management (Strategy Factory, lifecycle, versioning, Strategy Registry) | Shared infrastructure | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | STR | DIRECTIONAL TRADING, shared; ARBITRAGE depends on it ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed; its APPROVAL stage is performed by SYS-34 (STR-019 to STR-022, [DEC-023](../decisions/DEC-023-autonomous-canary-approval.md), [DEC-024](../decisions/DEC-024-part-2-reconciliation.md)) |
| SYS-15 | Backtesting | Shared infrastructure | [systems/strategy/backtesting.md](../systems/strategy/backtesting.md) | BKT | DIRECTIONAL TRADING, shared; ARBITRAGE depends on it ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-16 | Paper Trading | Shared infrastructure | [systems/strategy/paper-trading.md](../systems/strategy/paper-trading.md) | PAP | DIRECTIONAL TRADING, shared; ARBITRAGE depends on it ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-17 | Directional Trading System | Trading system | [systems/directional-trading.md](../systems/directional-trading.md) | DIR | DIRECTIONAL TRADING | Confirmed |
| SYS-18 | Cross-Exchange Arbitrage System | Trading system | [systems/arbitrage/cross-exchange-arbitrage.md](../systems/arbitrage/cross-exchange-arbitrage.md) | XAR | ARBITRAGE | Confirmed |
| SYS-19 | Triangular Arbitrage System | Trading system | [systems/arbitrage/triangular-arbitrage.md](../systems/arbitrage/triangular-arbitrage.md) | TAR | ARBITRAGE | Confirmed |
| SYS-20 | Arbitrage Intelligence | Arbitrage-shared capabilities | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARB | ARBITRAGE | Confirmed; several capabilities overlap platform systems (see document) |
| SYS-21 | Performance Controller | Shared infrastructure | [systems/performance-controller.md](../systems/performance-controller.md) | PFC | DIRECTIONAL TRADING (core); ARBITRAGE (arbitrage tracking) ([DEC-024](../decisions/DEC-024-part-2-reconciliation.md), CF-16) | Confirmed |
| SYS-22 | AI Intelligence Layer (incl. Hallucination Firewall, output contract, multi-agent validation, calibration) | AI | [ai/ai-architecture.md](../ai/ai-architecture.md), [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AIL, AIV | AI INTELLIGENCE | Confirmed; AI gateway defined (AIL-006, [DEC-013](../decisions/DEC-013-ai-organization.md)); AI Resource & Decision Governor is the gateway's admission component (AIL-009, [DEC-024](../decisions/DEC-024-part-2-reconciliation.md)) |
| SYS-23 | AI Agents | AI | [ai/agents.md](../ai/agents.md) | AGT | AI INTELLIGENCE | Confirmed; five agents (AGT-016, [DEC-013](../decisions/DEC-013-ai-organization.md)) |
| SYS-24 | Model Router | AI | [ai/model-management.md](../ai/model-management.md) | RTR | AI INTELLIGENCE | Confirmed; deterministic (RTR-003, [DEC-013](../decisions/DEC-013-ai-organization.md)) |
| SYS-25 | AI Cost Manager | AI support service (deterministic; listed as an agent in §54) | [ai/model-management.md](../ai/model-management.md) | COST | AI INTELLIGENCE | Confirmed; deterministic service (COST-002, [DEC-013](../decisions/DEC-013-ai-organization.md)) |
| SYS-26 | Model Evaluation (Model Evaluation Agent in §54) | AI support service (deterministic; listed as an agent in §54) | [ai/model-management.md](../ai/model-management.md) | MEV | AI INTELLIGENCE ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed; deterministic service (MEV-003, [DEC-013](../decisions/DEC-013-ai-organization.md)) |
| SYS-27 | AI Memory / Project Knowledge | AI | [ai/ai-memory.md](../ai/ai-memory.md) | MEM | AI INTELLIGENCE | Confirmed |
| SYS-28 | Monitoring and Observability (incl. alerting, reporting, Daily System Intelligence Dashboard, Incident Management) | Operations | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md), [operations/daily-system-intelligence.md](../operations/daily-system-intelligence.md), [operations/incident-management.md](../operations/incident-management.md) | MON, DSI, INC | OPERATIONALIZATION | Confirmed; owns alerting and reporting ([DEC-017](../decisions/DEC-017-reporting-alerting-and-performance-targets.md)); dashboard and incidents added by Part 2 (DSI-006, INC-003, [DEC-024](../decisions/DEC-024-part-2-reconciliation.md)) |
| SYS-29 | System Health State Machine (incl. failure handling, controlled degradation) | Operations | [operations/system-health.md](../operations/system-health.md) | HLT | CORE TRADING FOUNDATION; hardened in OPERATIONALIZATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed; state machine formalized (HLT-007 to HLT-009, [DEC-012](../decisions/DEC-012-safety-architecture.md); since replaced by HLT-011, HLT-012, and RSK-015 to RSK-017 and RSK-020, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)) |
| SYS-30 | Auditability / Event and Decision History | Capability — implementing system not named | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | AUD | CORE TRADING FOUNDATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed |
| SYS-31 | Security Architecture | Cross-cutting | [security/security-architecture.md](../security/security-architecture.md) | SEC | FOUNDATION ("Security foundation") | Confirmed |
| SYS-32 | Platform Account / Custody | Conditional | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | CUS | None — FUTURE | **FUTURE**: not built; single operator ([DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md)) |
| SYS-33 | Ledger / Accounting Foundation (internal trading ledger) | Shared infrastructure | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | LED | CORE TRADING FOUNDATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) | Confirmed (LED-004 to LED-007, [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md)) |
| SYS-34 | Readiness System (Governance and Readiness Engine) | Shared infrastructure (deterministic) | [systems/readiness-system.md](../systems/readiness-system.md) | RDY | DIRECTIONAL TRADING | Confirmed; one system under two names (DUP-24); performs the APPROVAL stage (STR-019 to STR-022); registered by [DEC-024](../decisions/DEC-024-part-2-reconciliation.md). Since Part 3 also holds the capability registry, capability availability, and the readiness matrix (RDY-020 to RDY-026; DUP-33) |

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
| MIG | Hosting, portability, backup, migration, disaster recovery | [operations/hosting-and-migration.md](../operations/hosting-and-migration.md) |
| VER | Platform verification: performance, load, and chaos testing; map of all verification requirements | [architecture/verification-architecture.md](verification-architecture.md) |
| GOV | Architecture governance: feature integration gate, duplicate and conflict detection, compatibility, removal, deprecation, ADRs, complexity budget | [architecture/architecture-governance.md](architecture-governance.md) |

## Named in Part 1 but not defined — how each was resolved

None of these became a new system (§00 item 21). Each was assigned to an existing owner.

| Name | Where it appears | Resolution |
|---|---|---|
| Reporting and alerts | §01, §02 item 22, §95 | SYS-28 Monitoring and Observability (MON-007, MON-008, [DEC-017](../decisions/DEC-017-reporting-alerting-and-performance-targets.md)) |
| AI gateway | §95 | Component of SYS-22 (AIL-006, [DEC-013](../decisions/DEC-013-ai-organization.md)) |
| Global safety architecture | §47 | Risk Engine + System Health (RSK-008, HLT-010, [DEC-012](../decisions/DEC-012-safety-architecture.md)) |
| Storage | §03, §04, §10, §95, §97 | PostgreSQL / TimescaleDB / Parquet ([technology stack](technology-stack.md), [DEC-009](../decisions/DEC-009-technology-stack.md)); each system owns its own data |
| Logging | §04 | SYS-28 operational logs (MON-009), separate from audit (AUD-006) |
| Canary | §34, §38, §95 | SYS-14 (STR-011, [DEC-015](../decisions/DEC-015-modes-canary-and-policy-governance.md); since replaced by STR-013 to STR-018, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)) |
| Market universe | §08, §95 | SYS-05 (OPP-009, [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md)) with exclusions from SYS-12 |

## Named in Part 3 — how each was resolved

Part 3 adds no system. Every name it uses is a component or alias of an existing owner ([DEC-031](../decisions/DEC-031-part-3-reconciliation.md)).

| Name in Part 3 | Where it appears | Resolution |
|---|---|---|
| Eligibility Engine | P3§354 | Component of SYS-34 (RDY-011, RDY-026; DUP-33) |
| Canary Readiness Engine | P3§379 | Component of SYS-34 (RDY-015, RDY-026; DUP-33) |
| Capability registry | P3§411, §412, §535 | Component of SYS-34 (RDY-020, RDY-026; DUP-33) |
| Readiness matrix | P3§480 | Produced by SYS-34 (RDY-023), shown through SYS-28's daily report (DSI-002) |
| Rebalancing Engine | P3§361 to §366 | Rebalancing-decision component of SYS-07 using SYS-20's evaluation (CAP-037 to CAP-042; DUP-34) |
| Capital Authority | P3§359, §366, §400, §442 | SYS-07 Global Capital Authority |
| AI Resource Governor | P3§449, §535 | Component of the AI gateway in SYS-22 (AIL-008, AIL-009, AIL-021) |
| Global controller | P3§515 | ARCH-035: SYS-12, SYS-09's emergency controller, and SYS-29 together |
| Policy compiler | P3§515, §535 | As for Part 2: NLP-004 in SYS-13, deterministic compilation in SYS-12 |
| Liquidity Engine, Market Quality Engine, Liquidity Manager | P3§403 (examples in the duplicate-detection rule) | Not systems. Liquidity evaluation is SYS-06's (TNP-024) with SYS-03 metrics; market-data quality is SYS-02's (MKD-008, MKD-012) |
| System Rules Register | P3§468, §537 | Documentation: [requirements/system-rules-register.md](../requirements/system-rules-register.md) (ARCH-038) |
| Future feature registry | P3§509 | GOV-018, replaced by GOV-024 (the canonical feature lifecycle, DEC-035); where feature statuses are kept is decided when Stage 1 is planned; no separate registry created |
| Emergency state model | P3§372 | Mapped onto SYS-09's safety levels and SYS-29's health states without merging meanings; mapping in the [Risk Engine](../risk/risk-engine.md) (DUP-35) |
| Strategy Optimizer, Model Evaluation Agent, Quant Research Agent, Strategy Research Agent | P3§535 | Mapped to DEC-013's agents and services as for Part 2 (AGT-017; [agents](../ai/agents.md)) |
| Execution state authority, financial ledger authority | P3§467 | SYS-10 (EXE-002) and SYS-33 (LED-004, LED-006); ARCH-037 |

## Named in Part 2 — how each was resolved

Part 2 names many components. Only the Readiness System became a registered system, and only because it was already a named engine ([DEC-023](../decisions/DEC-023-autonomous-canary-approval.md)). The rest are components or aliases of existing owners ([DEC-024](../decisions/DEC-024-part-2-reconciliation.md)).

| Name in Part 2 | Where it appears | Resolution |
|---|---|---|
| Readiness System | P2§65–§67, §184 | SYS-34, the same system as the Governance and Readiness Engine (DUP-24) |
| AI Resource & Decision Governor | P2§12, §315, §339 | Component of the AI gateway in SYS-22 (AIL-008, AIL-009; DUP-25) |
| Fee Engine, Slippage Engine | P2§30, §31, §184, §191 | Components of SYS-03 (QNT-005 to QNT-007; DUP-27) |
| Opportunity Database / Opportunity Registry | P2§27, §184, §214 | Component of SYS-05 (OPP-014 to OPP-016; DUP-26) |
| Opportunity Filter | P2§25, §274, §314 | Component of SYS-05 (OPP-005, OPP-008) |
| Strategy Registry | P2§20, §184, §210 | Component of SYS-14 (STR-023, STR-024) |
| Strategy Factory | P2§19, §209 | Component of SYS-14 (STR-003, STR-012), as in Part 1 |
| Market-data normalization layer | P2§2, §184 | SYS-02 (MKD-011; DUP-28) |
| Exchange abstraction | P2§44, §184 | SYS-01 (EXA-011) |
| Policy Authority | P2§184 | SYS-12 Policy System |
| Policy compiler | P2§102, §193, §314 | Two steps: natural language → structured policy in SYS-13 (NLP-004); structured policy → enforceable rules in SYS-12 ([glossary](../glossary.md)) |
| Global platform controller / global controller | P2§193, §314, §349 | SYS-12, SYS-09's emergency controller, and SYS-29 together; no new system (ARCH-035, decided by the owner in [DEC-027](../decisions/DEC-027-part-2-open-questions.md)) |
| Rebalancing Engine | P2§91 | ARB-006 evaluation (SYS-20) with the CAP-018 decision (SYS-07) |
| Arbitrage Risk Engine | P2§93, §222 | Rule sets in SYS-09 (RSK-012, RSK-033) |
| Arbitrage Performance Controller | P2§95, §224 | SYS-21's arbitrage tracking (PFC-014) |
| Paper executor, live executor | P2§60 | Paper executor in SYS-16; the execution interface in SYS-10 (PAP-006) |
| Readiness dashboard | P2§190 | The readiness section of the Daily System Intelligence report (DSI-002) reading SYS-34 |
| Daily System Intelligence Dashboard / Report | P2§69–§72 | Component of SYS-28 (DSI; DUP-30) |
| Incident management | P2§77, §194 | Component of SYS-28 (INC) |
| Configuration compiler / environment adapter | P2§137, §246 | MIG-011, in the hosting, backup, and migration set; implementing module assigned when OPERATIONALIZATION is planned |
| Consistency system | P2§173, §294 | ARCH-032; first increment is the documentation checker in `tools/docs/` ([DEC-025](../decisions/DEC-025-documentation-tooling-in-repository.md)) |
| Domain command language | P2§176, §297 | ARCH-034, PROPOSED |
| Global project constitution | P2§174, §295 | "Platform principles" index in the [platform overview](../product/platform-overview.md) (ARCH-028) |
| Capital Allocation & Treasury Engine | Owner decisions 3 (Q6) | SYS-07 Global Capital Authority ([DEC-028](../decisions/DEC-028-capital-buckets-and-progressive-activation.md)) |
