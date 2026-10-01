# Platform Overview

> **Status:** DOCUMENTED (Handoff Parts 1, 2, and 3) — not implemented · **Owner:** platform-wide (product level) · **Sources:** §01, §02, §82, §83; Part 3: P3§389, P3§415–P3§416, P3§457, P3§501–P3§503, P3§522, P3§525, P3§529–P3§530, P3§533–P3§534, P3§542, P3§544–P3§547
>
> Canonical definition of what the platform is, what it must be capable of, and the priority order that governs every trade-off. Requirement line format: [`docs/requirements/README.md`](../requirements/README.md).

## Identity

- **PLT-001** Platform identity · CONFIRMED REQUIREMENT · §01 — The project is a professional autonomous cryptocurrency trading platform. It is not merely an AI trading bot.
- **PLT-002** Platform capability scope · CONFIRMED REQUIREMENT · §01 — The platform combines: autonomous trading; directional trading; cross-exchange arbitrage; triangular arbitrage; quantitative analysis; market-data infrastructure; whole-universe opportunity monitoring; portfolio management; capital management; risk management; strategy management; backtesting; paper trading; live trading; exchange connectivity; AI-assisted research; AI reasoning; natural-language policy control; model routing; AI cost management; strategy improvement; monitoring; recovery; reconciliation; security; auditability; reporting; controlled deployment; continuous development.
- **PLT-003** Long-lived production platform · CONFIRMED ARCHITECTURAL PRINCIPLE · §01 — The architecture must be designed as a long-lived production platform rather than a collection of independent scripts or bots.

## Core objective

- **PLT-004** Controlled autonomous trading environment · CONFIRMED REQUIREMENT · §02 — The platform should provide a controlled autonomous trading environment capable of the 24 capabilities listed in the table below.
- **PLT-005** No assumed profit · CONSTRAINT · §02 — The system must never assume that automation, AI, arbitrage, or a strategy guarantees profit.

The table maps each §02 capability to the system that owns it. The mapping is analysis, not handoff text; where ownership is unclear the table says so.

| # | Capability (§02, verbatim) | Owning system (see [system registry](../architecture/system-registry.md)) |
|---|---|---|
| 1 | Connecting to supported trading venues. | SYS-01 Exchange Adapter Layer |
| 2 | Establishing authorized capital. | SYS-12 Policy System (capital authorization) with SYS-07 Global Capital Authority; no custody: single operator ([DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md)) |
| 3 | Receiving user objectives and restrictions. | SYS-13 Natural Language Policy Interface |
| 4 | Understanding those instructions through a controlled policy interface. | SYS-13 Natural Language Policy Interface |
| 5 | Representing them as structured, persistent policy. | SYS-12 Policy System |
| 6 | Enforcing applicable hard constraints deterministically. | SYS-09 Risk Engine, using SYS-12 Policy System |
| 7 | Monitoring the configured market universe continuously. | SYS-05 Opportunity Detection Engine, on SYS-02 Market Data |
| 8 | Detecting potential opportunities. | SYS-05 Opportunity Detection Engine |
| 9 | Evaluating opportunities deterministically. | SYS-06 True Net-Profit Engine |
| 10 | Selecting appropriate validated strategies. | SYS-17 Directional selects among validated versions owned by SYS-14 Strategy Management ([DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md)) |
| 11 | Performing quantitative analysis. | SYS-03 Quantitative Engine |
| 12 | Using AI selectively for reasoning and research. | SYS-22 AI Intelligence Layer with SYS-24 Model Router |
| 13 | Applying deterministic risk controls. | SYS-09 Risk Engine |
| 14 | Managing capital competition between strategies. | SYS-07 Global Capital Authority |
| 15 | Validating execution conditions. | SYS-10 Execution Engine |
| 16 | Executing through controlled exchange adapters. | SYS-10 Execution Engine via SYS-01 |
| 17 | Managing positions. | Shared: trading systems manage their positions; SYS-08 Portfolio holds position state |
| 18 | Reconciling internal and external state. | SYS-11 Recovery and Reconciliation |
| 19 | Recovering after interruptions. | SYS-11 Recovery and Reconciliation |
| 20 | Monitoring strategy and platform health. | SYS-21 Performance Controller (strategy); SYS-28 Monitoring and SYS-29 System Health (platform) |
| 21 | Recording decisions and events. | SYS-30 Auditability / Event and Decision History |
| 22 | Generating reports and alerts. | SYS-28 Monitoring and Observability ([DEC-017](../decisions/DEC-017-reporting-alerting-and-performance-targets.md)) |
| 23 | Improving strategies through controlled research. | SYS-14 Strategy Management |
| 24 | Preventing unvalidated AI reasoning from directly controlling protected trading infrastructure. | SYS-22 AI Intelligence Layer (hard-safety boundary) with SYS-09 Risk Engine |

## Priorities and return expectations

- **PLT-006** Platform safety priority · CONFIRMED ARCHITECTURAL PRINCIPLE · §82 — The project's conceptual hierarchy is: 1. Capital Preservation; 2. Risk Control; 3. Execution Safety; 4. Positive Net Profitability; 5. Capital Efficiency; 6. Compounding / Growth; 7. Opportunity Targets. Higher priorities cannot be overridden by lower ones.
- **PLT-007** No guaranteed returns · CONSTRAINT · §83 — The platform must never assume: fixed profit per trade; fixed daily return; guaranteed arbitrage profit; guaranteed strategy performance; guaranteed AI accuracy.
- **PLT-008** No fixed daily percentage · CONSTRAINT · §83 — The system is not constrained to a fixed daily percentage either.
- **PLT-009** Platform objective · CONFIRMED REQUIREMENT · §83 — Its objective is: maximize risk-adjusted, executable, net profitability while preserving capital and avoiding unnecessary exposure.

How these principles apply to individual opportunities (positive-net execution, small-profit accumulation, no profit ceiling) is defined in the [True Net-Profit Engine](../systems/true-net-profit-engine.md). How realized results are reinvested is defined in [Global Capital Authority](../systems/capital-management.md).

## Decisions applied (2026-09-30)

- **PLT-010** Single-operator platform · CONFIRMED REQUIREMENT · DEC-006 — The platform trades for one operator, using the operator's own accounts at supported venues through API keys. It does not take custody of funds and has no deposit, withdrawal, or multi-user account functions.
- **PLT-011** Instrument scope · CONFIRMED REQUIREMENT · DEC-007 — The platform trades spot, perpetual futures, and margin products.
- **PLT-012** Instrument types gated by their risk controls · CONSTRAINT · DEC-007 — No instrument type is enabled for live trading until the risk controls specific to it (RSK-013) are implemented and verified.

Sources: [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md) (owner decision), [DEC-007](../decisions/DEC-007-instrument-scope.md) (owner decision).

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

- **PLT-013** Company-grade autonomy · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-019 — The operating model is autonomous, policy-bounded, risk-bounded, capital-bounded, evidence-driven, self-monitoring, self-recovering, and reconciliation-aware. The system should require human intervention when necessary, but human absence must not itself cause normal 24/7 operation to stop.
- **PLT-014** Human intervention by exception · CONFIRMED REQUIREMENT · DEC-019 — Human intervention should primarily be required for: policy changes requiring approval; security events; unrecoverable state; unknown financial state; unauthorized conditions; custody/security events; infrastructure failure beyond automated recovery; architecture changes; production approval gates explicitly designated as human-controlled. Routine operation should remain autonomous.
- **PLT-015** Operating decision rule · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-019 — The system operates autonomously when it has sufficient authority, capital, information, infrastructure health, and state certainty to do so safely. When it can act safely, it acts autonomously; when it needs more information, it waits and validates; when it is outside authorization, it does not act; when external state is uncertain, it reconciles or enters SAFE MODE; when a condition is recoverable, it recovers automatically; when a strategy is ready, it enters canary automatically; when performance deteriorates, it adapts, throttles, or suspends; when an emergency occurs, it enters the appropriate safety state. The system must be autonomous without being uncontrolled.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **PLT-016** Deterministic-first identity · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§1 — The project is a deterministic-first autonomous financial software platform with an AI intelligence layer. The foundational principle is: AI provides intelligence; deterministic infrastructure provides authority.
- **PLT-017** Capabilities added by Part 2 · CONFIRMED REQUIREMENT · P2§1, P2§338 — In addition to PLT-002, the platform is intended to combine: market-regime detection; execution; AI market interpretation; performance analysis; incident management; backup/restore; deployment portability; local hosting; server/cloud hosting; migration; failover/standby where approved; production change control.
- **PLT-018** Safe-state principle · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§1, P2§350 — If the system does not know enough to act safely, it must be able to choose NO TRADE, WAIT, SAFE MODE, or another explicitly defined safe state.
- **PLT-019** What the objective is not · CONSTRAINT · P2§313, P2§35 — The objective (PLT-009) is not: maximum trades; maximum AI activity; maximum leverage; maximum percentage per trade; fixed daily return. The architecture should optimize for quality, executability, risk-adjusted economics, and capital efficiency, not artificial trade-count targets.
- **PLT-020** Autonomy is bounded · CONSTRAINT · P2§106, P2§278, P2§343 — Autonomous operation means the system can act within authorized boundaries. It does not mean: unlimited capital; unlimited leverage; unlimited strategy changes; unlimited AI authority; unlimited withdrawals; unlimited deployment access. The user provides high-level objectives and boundaries, the platform translates them into structured policies, deterministic infrastructure enforces them, and AI provides intelligence inside those boundaries. The system must never invent authorization.

Part 2 §312 (capital-preservation hierarchy) is PLT-006 and §313's objective is PLT-009, both unchanged. "Failover/standby where approved" in PLT-017 stays conditional: failover is FUTURE until high availability is approved (REC-021).

- **PLT-021** Maximum autonomy inside a deterministic safety envelope · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-026 — The objective is maximum autonomy inside a deterministic safety envelope: the system should be capable of operating 24/7 and recovering intelligently without sacrificing the fundamental safety guarantees of the platform.

PLT-021 comes from the owner's answer to CF-14 ([DEC-026](../decisions/DEC-026-safety-floor-and-layered-control.md)).

### Non-negotiable platform principles (P2§174, P2§295; ARCH-028)

Part 2 asks for a central statement of the platform's non-negotiable principles and leaves the name to architecture. This index is that statement. It is called "platform principles", not "constitution", so it is never confused with the [builder constitution](../builder/claude-code-builder-constitution.md), which governs how Claude builds, not how the platform behaves ([DEC-024](../decisions/DEC-024-part-2-reconciliation.md)). Each principle is defined once, in the requirements listed; this table only points to them.

| Principle (P2§174) | Canonical requirements |
|---|---|
| Deterministic core | PLT-016, ARCH-019, ARCH-021, QNT-003, RSK-001, EXE-001 |
| AI boundary | ARCH-020, ARCH-022, AIL-002, AIL-003, AIV-016 |
| Capital preservation | PLT-006 |
| Risk precedence and the safety floor | RSK-004, RSK-005, RSK-034, RSK-039, AIV-009 (CF-14 decided by the owner, [DEC-026](../decisions/DEC-026-safety-floor-and-layered-control.md)) |
| No fixed returns | PLT-005, PLT-007, PLT-008, TNP-014, ARB-015 |
| True net profitability | TNP-001, TNP-004, TNP-018, TNP-020 |
| Unknown-state safety | PLT-018, RSK-014, RGM-008, REC-014, REC-016, DSI-004 |
| Controlled self-improvement | STR-002, STR-009, STR-010, AGT-013, RDY-001 |
| Auditability | AUD-001, AUD-010, AUD-012 |
| Reconciliation | REC-008, REC-015, LED-009, MIG-018 |
| No duplicate authorities | ARCH-016, ARCH-027 |
| Bounded autonomy | PLT-013, PLT-015, PLT-020, PLT-021, RSK-035, RSK-036 |
| No deadlock by safety | RSK-037, RSK-038 |

## Handoff Part 3 applied (2026-09-30)

New requirements from [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), cited as P3§N. Part 3 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 3 reconciliation](../traceability/part-3-reconciliation.md). Placement, duplicate, and conflict resolutions: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md).

- **PLT-022** Search aggressively, act conservatively · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§389, P3§416, P3§522, P3§544 — This is a core operating principle and one of the central behavioral principles. The platform should: search broadly; filter intelligently; validate rigorously; execute selectively (P3§416). It must aggressively SEARCH and selectively EXECUTE; these are different: search broadly, filter strictly, execute disciplinedly (P3§389). SEARCH: broadly, continuously, quickly, across approved opportunities. ACT: only when economics, liquidity, risk, capital, policy, execution, data, and system state are sufficiently validated (P3§522). Search broadly; filter strictly; validate rigorously; execute selectively; monitor continuously; recover safely (P3§544).
- **PLT-023** Capital enables capability, not permission · CONSTRAINT · P3§415, P3§525, P3§545 — Capital should enable capability. Capital should not automatically create risk. As capital grows, the system becomes capable of evaluating more opportunities and capabilities where justified by: economics; risk; liquidity; infrastructure; validation; authorization. The system must never infer "We have more capital, therefore we have permission to do anything." Capital growth does not create authorization, and having sufficient money does not automatically authorize a feature. Authorization comes from: user policy + system policy + risk + capital + validation + security + approved deployment state.
- **PLT-024** One intelligent operating system · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§457, P3§530, P3§546 — The platform should behave as one intelligent operating system for autonomous trading. It continuously observes, understands, evaluates, allocates, executes, reconciles, monitors, recovers, learns, and improves, but only within explicit authority and controlled validation. The platform may operate autonomously inside explicit boundaries: autonomy means observe → analyze → decide → act → verify → learn; it does not mean act without authority. The user defines: objectives; boundaries; policy; authority. The system determines how, when, where, and whether, within those boundaries.
- **PLT-025** Knowing when not to act · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§529, P3§547 — The system must know when not to act. In addition to the valid outcomes of RSK-006, correct outcomes include: REBALANCE; DO NOT REBALANCE; DEGRADE; RECOVER; REQUIRE REVIEW. In addition to the safe states of PLT-018, RECONCILE is a correct response when the system does not know enough to act safely. Never invent certainty.
- **PLT-026** Scale without rebuilding, and without losing control · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§502, P3§503, P3§533 — As the platform grows ($100 → $1,000 → $10,000 → $100,000+ → larger capital environments), the architecture should not need to be fundamentally rewritten merely because capital increased. Instead the system should scale, according to actual requirements: capital allocation; execution capacity; strategy universe; opportunity processing; infrastructure; monitoring; data; risk management. The platform must scale intelligently with capital, markets, venues, strategies, data, compute, AI workload, users/accounts if applicable, and operational complexity. Scaling must preserve: safety; correctness; auditability; performance; reconciliation; control. Larger capital should result in more control, more validation, more observability, and more risk management, not simply more trades.
- **PLT-027** Company-grade engineering · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§501, P3§534 — The platform should behave like a serious financial technology system rather than a collection of trading scripts, and be engineered as a production financial infrastructure company would engineer a serious autonomous system. That means: central authorities; clear contracts; controlled state; auditability; reconciliation; observability; security; recovery; testability; versioning; dependency management; change control; documentation; traceability. And: no shortcuts around financial authority; no hidden state; no uncontrolled AI; no duplicate authorities; no silent assumptions; no undocumented production changes; no unvalidated self-improvement; no unsafe migration; no uncontrolled failover; no forced trading; no fixed-return assumptions; no artificial daily profit ceiling; no assumption that more capital means more risk; no assumption that a restart means the system is safe to resume.
- **PLT-028** Final master objective · CONFIRMED REQUIREMENT · P3§542 — The final platform objective is: build a deterministic-first, AI-enhanced, autonomous, capital-aware, opportunity-aggressive, risk-controlled, 24/7, self-monitoring, self-recovering, controlled-self-improving, production-grade cryptocurrency trading platform. The system should: search aggressively; think intelligently; calculate deterministically; allocate capital intelligently; execute disciplinedly; reconcile constantly; recover automatically where safe; scale with capital; activate capabilities when ready; adapt to changing conditions; learn from results; and never sacrifice safety for activity.

How these fit what already exists:

- **PLT-028 and PLT-009.** PLT-009 remains the trading objective (maximize risk-adjusted, executable, net profitability while preserving capital). PLT-028 describes the platform to be built. "Opportunity-aggressive" means aggressive search as defined in OPP-017, never aggressive risk-taking.
- **PLT-022.** Part 3 states the same principle four times with small wording differences; each wording is kept in the one requirement and attributed to its section. The opportunity engine's side of it is OPP-017 to OPP-019.
- **PLT-023.** The authorization list extends PLT-020 ("the system must never invent authorization"). How capital growth may change limits is reconciled in CF-18 ([DEC-031](../decisions/DEC-031-part-3-reconciliation.md)).
- **PLT-024.** The user/system split restates PLT-020 and PLT-015 in Part 3's words.
- **PLT-025.** P3§531 (the final master safety principle) is PLT-015 with three additions that live with their owners: stop feature integration on conflict (GOV-004), reassess capability when capital changes (CAP-046), validate strategy changes before production (STR-002, STR-009).
- **PLT-027.** Each "no ..." item is enforced by the requirements listed for it in the [System Rules Register](../requirements/system-rules-register.md).
- P3§421 (protect capital before optimizing growth) is PLT-006 unchanged. P3§543 (AI provides intelligence; deterministic infrastructure provides authority) is PLT-016 unchanged.

The principles index above gains no new rows: Part 3's system rules are indexed in the [System Rules Register](../requirements/system-rules-register.md), which points to each canonical requirement (ARCH-038).

## Decisions applied (2026-10-01)

From the owner's directive on verification and platform independence ([DEC-034](../decisions/DEC-034-verification-and-platform-independence.md)).

- **PLT-029** Platform independent of Claude Code · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-034 — The production platform must exist independently of Claude Code. Claude Code is the engineering agent responsible for building, maintaining, upgrading, extending, testing, documenting, and improving the platform; it is not the platform. The platform must be capable of: operating without an active Claude Code session; operating without an active Claude conversation; continuing 24/7 operation within its authorized operating boundaries; maintaining persistent state; recovering from supported failures; enforcing deterministic risk and capital controls; executing authorized trading operations; monitoring itself; recording audit history; maintaining configuration and strategy versions; being deployed independently; being upgraded through controlled engineering processes; being restored after failure; being migrated between supported environments; receiving future features and improvements. Claude Code may return later and continue engineering the platform, but the platform must never depend on Claude Code being continuously active in order to operate.

PLT-029 states for the platform what constitution Rule 198 asks of the builder. It is about Claude Code, the builder. AI models the platform itself uses through its AI gateway (AIL-006) are platform components: provider-agnostic (AIL-007), with deterministic fallback when unavailable (AIL-011). Rebuilding production without the owner is OPS-017; how the platform keeps its knowledge is GOV-023.

## Findings (all resolved)

OQ-01 → [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md) (single operator, no custody). OQ-13 → [DEC-017](../decisions/DEC-017-reporting-alerting-and-performance-targets.md) (reporting and alerting owned by Monitoring and Observability). DUP-20 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md).
