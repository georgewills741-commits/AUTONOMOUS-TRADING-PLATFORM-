# Platform Overview

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **Owner:** platform-wide (product level) · **Sources:** §01, §02, §82, §83
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

## Findings (all resolved)

OQ-01 → [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md) (single operator, no custody). OQ-13 → [DEC-017](../decisions/DEC-017-reporting-alerting-and-performance-targets.md) (reporting and alerting owned by Monitoring and Observability). DUP-20 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md).
