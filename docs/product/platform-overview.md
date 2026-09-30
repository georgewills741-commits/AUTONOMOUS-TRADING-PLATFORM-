# Platform Overview

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **Owner:** platform-wide (product level) · **Sources:** §01, §02, §82, §83
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
| 2 | Establishing authorized capital. | SYS-12 Policy System (capital authorization) with SYS-07 Global Capital Authority; custody model unconfirmed (OQ-01) |
| 3 | Receiving user objectives and restrictions. | SYS-13 Natural Language Policy Interface |
| 4 | Understanding those instructions through a controlled policy interface. | SYS-13 Natural Language Policy Interface |
| 5 | Representing them as structured, persistent policy. | SYS-12 Policy System |
| 6 | Enforcing applicable hard constraints deterministically. | SYS-09 Risk Engine, using SYS-12 Policy System |
| 7 | Monitoring the configured market universe continuously. | SYS-05 Opportunity Detection Engine, on SYS-02 Market Data |
| 8 | Detecting potential opportunities. | SYS-05 Opportunity Detection Engine |
| 9 | Evaluating opportunities deterministically. | SYS-06 True Net-Profit Engine |
| 10 | Selecting appropriate validated strategies. | Unclear: SYS-17 lists "strategy selection"; SYS-14 owns validated versions (DUP-20) |
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
| 22 | Generating reports and alerts. | **No owner defined in Part 1** (OQ-13) |
| 23 | Improving strategies through controlled research. | SYS-14 Strategy Management |
| 24 | Preventing unvalidated AI reasoning from directly controlling protected trading infrastructure. | SYS-22 AI Intelligence Layer (hard-safety boundary) with SYS-09 Risk Engine |

## Priorities and return expectations

- **PLT-006** Platform safety priority · CONFIRMED ARCHITECTURAL PRINCIPLE · §82 — The project's conceptual hierarchy is: 1. Capital Preservation; 2. Risk Control; 3. Execution Safety; 4. Positive Net Profitability; 5. Capital Efficiency; 6. Compounding / Growth; 7. Opportunity Targets. Higher priorities cannot be overridden by lower ones.
- **PLT-007** No guaranteed returns · CONSTRAINT · §83 — The platform must never assume: fixed profit per trade; fixed daily return; guaranteed arbitrage profit; guaranteed strategy performance; guaranteed AI accuracy.
- **PLT-008** No fixed daily percentage · CONSTRAINT · §83 — The system is not constrained to a fixed daily percentage either.
- **PLT-009** Platform objective · CONFIRMED REQUIREMENT · §83 — Its objective is: maximize risk-adjusted, executable, net profitability while preserving capital and avoiding unnecessary exposure.

How these principles apply to individual opportunities (positive-net execution, small-profit accumulation, no profit ceiling) is defined in the [True Net-Profit Engine](../systems/true-net-profit-engine.md). How realized results are reinvested is defined in [Global Capital Authority](../systems/capital-management.md).

## Related findings

OQ-01 (custody and user model), OQ-13 (reporting), DUP-20 (strategy selection) — see [open questions](../open-questions/register.md) and [findings register](../conflicts/register.md).
