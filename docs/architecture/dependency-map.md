# Dependency Map

> **Status:** ACTIVE — derived from Handoff Part 1, updated 2026-09-30 with decisions DEC-006 to DEC-018. Part 2 promises "complete dependency mapping"; revise this map when it arrives.
>
> Canonical record of which systems depend on which (ARCH-014). **STATED** edges come directly from handoff text (source given). **DECIDED** edges were fixed by a decision record. **INFERRED** edges are the builder's reading of the text. System IDs are from the [system registry](system-registry.md).

## Handoff reference chain (§94)

```text
EXCHANGE ADAPTER → MARKET DATA → QUANTITATIVE ENGINE → OPPORTUNITY DETECTION
  → STRATEGY → RISK → CAPITAL → EXECUTION → PORTFOLIO / RECONCILIATION
```

This is a build-dependency chain. The runtime order, with the capital authority before the risk check as in §19, is fixed in [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (CF-01 resolved).

## System dependencies

"A depends on B" means A cannot work, or cannot be completed, without B.

| # | Dependent | Depends on | Basis | Source |
|---|---|---|---|---|
| D-01 | SYS-02 Market Data | SYS-01 Exchange Adapters | STATED | §10, §94 |
| D-02 | SYS-03 Quantitative Engine | SYS-02 Market Data | STATED | §10, §94 |
| D-03 | SYS-05 Opportunity Detection | SYS-02 Market Data, SYS-03 Quantitative Engine | STATED | §08, §10, §94 |
| D-04 | SYS-05 Opportunity Detection | SYS-04 Market Regime Engine | INFERRED (scans "market regimes", detects "market-regime changes") | §08, §09 |
| D-05 | SYS-04 Market Regime Engine | SYS-02 Market Data, SYS-03 Quantitative Engine | INFERRED (inputs not stated) | §11 |
| D-06 | SYS-17, SYS-18, SYS-19 trading systems | SYS-05 Opportunity Detection | STATED | §09, §94 |
| D-07 | SYS-17 Directional | SYS-04 Market Regime Engine | STATED ("regime compatibility"; RGM-004) | §05, §11 |
| D-08 | SYS-06 True Net-Profit Engine | SYS-03 Quantitative Engine (fees, spread, slippage) | DECIDED (DEC-011) | §12, §13 |
| D-09 | SYS-06 True Net-Profit Engine | SYS-02 Market Data (order books, funding rates, exchange metadata) | INFERRED | §10, §13 |
| D-10 | SYS-18, SYS-19 arbitrage systems | SYS-06 True Net-Profit Engine | DECIDED (DEC-011) | §06, §07, §13 |
| D-11 | SYS-18, SYS-19 arbitrage systems | SYS-20 Arbitrage Intelligence | DECIDED (DEC-011) | §43 |
| D-12 | SYS-09 Risk Engine | Strategy output from SYS-17/18/19 | STATED | §94 |
| D-13 | SYS-09 Risk Engine | SYS-12 Policy System (user hard constraints) | STATED | §26, §28–§29 |
| D-14 | SYS-09 Risk Engine | SYS-08 Portfolio (exposure, portfolio limits) | INFERRED | §24, §25 |
| D-15 | SYS-07 Global Capital Authority | SYS-09 Risk Engine (risk check) | STATED; order fixed by DEC-010 | §19, §21 |
| D-16 | SYS-07 Global Capital Authority | SYS-12 Policy System (user policy, capital authorization) | STATED | §20, §22, §28 |
| D-17 | SYS-07 Global Capital Authority | SYS-33 Ledger / accounting (compounding) | DECIDED (DEC-006); unconditional | §22 |
| D-18 | SYS-10 Execution Engine | SYS-07 Global Capital Authority (reservation) | STATED | §19, §94 |
| D-19 | SYS-10 Execution Engine | SYS-09 Risk Engine | STATED | §77, §94 |
| D-20 | SYS-10 Execution Engine | SYS-01 Exchange Adapters | STATED | §02 item 16, §42 |
| D-21 | SYS-10 Execution Engine | SYS-11 Recovery and Reconciliation (after a timeout) | STATED | §41 |
| D-22 | SYS-08 Portfolio | SYS-10 Execution, SYS-11 Reconciliation | STATED | §70, §94 |
| D-23 | SYS-11 Recovery and Reconciliation | SYS-01 Exchange Adapters (balances, positions, open orders, fills) | STATED | §71 |
| D-24 | SYS-11 Recovery and Reconciliation | SYS-09 Risk, SYS-07 Capital, SYS-12 Policy, SYS-14 Strategy (validation steps) | STATED | §71, §72 |
| D-25 | SYS-13 NL Policy Interface | SYS-12 Policy System | STATED | §28 |
| D-26 | SYS-13 NL Policy Interface | SYS-22 AI Intelligence Layer (LLM interpretation) | STATED | §28 |
| D-27 | SYS-14 Strategy Management | SYS-15 Backtesting, SYS-16 Paper Trading | STATED | §34, §35 |
| D-28 | SYS-17/18/19 trading systems | SYS-14 Strategy Management (validated strategy versions) | STATED | §02 item 10, §34, §36 |
| D-29 | SYS-16 Paper Trading | SYS-09 Risk, SYS-07 Capital, SYS-08 Portfolio, SYS-10 Execution (production architecture) | STATED | §32 |
| D-30 | SYS-15 Backtesting | SYS-02 Market Data (historical), with risk, capital, and portfolio constraints | STATED | §33 |
| D-31 | SYS-21 Performance Controller | SYS-20 Arbitrage Intelligence (opportunity database), SYS-30 Audit, SYS-08 Portfolio | DECIDED (DEC-011) | §44, §48, §49 |
| D-32 | SYS-23 AI Agents | SYS-22 AI Intelligence Layer (validation), SYS-24 Model Router | INFERRED | §63–§66 |
| D-33 | SYS-23 Trading Director | Market data, quantitative features, regime, portfolio, policy, risk state | STATED (listed inputs) | §55 |
| D-34 | SYS-09 Risk Engine | SYS-23 Trading Director proposals (validated) | STATED | §55, §66 |
| D-35 | SYS-24 Model Router | SYS-26 Model Evaluation, SYS-25 AI Cost Manager | DECIDED (DEC-013) | §63 |
| D-36 | SYS-22 Hallucination Firewall | Evidence identifiers from SYS-02, SYS-03, SYS-30 | DECIDED (DEC-013) | §64 |
| D-37 | SYS-20 Arbitrage Intelligence | SYS-07 Global Capital Authority (reserve, rebalancing decision) | STATED | §45, §46 |
| D-38 | SYS-28 Monitoring | All systems | INFERRED | §88 |
| D-39 | SYS-29 System Health | SYS-28 Monitoring | INFERRED | §74, §88 |
| D-40 | SYS-30 Audit | All acting systems ("which system acted") | STATED | §86 |
| D-41 | SYS-09 Risk Engine | SYS-29 System Health (platform state before every authorization) | DECIDED (DEC-012) | RSK-010, HLT-010 |
| D-42 | SYS-23 AI Agents, SYS-13 NL Policy Interface | SYS-22 AI gateway (all AI calls) | DECIDED (DEC-013) | AIL-006 |
| D-43 | SYS-08 Portfolio | SYS-33 Ledger (realized P&L) | DECIDED (DEC-006) | LED-006, PRT-004 |
| D-44 | SYS-05 Opportunity Detection | SYS-12 Policy System (universe exclusions) | DECIDED (DEC-008) | OPP-009 |
| D-45 | SYS-28 Monitoring (reports) | SYS-33 Ledger, SYS-08 Portfolio, SYS-30 Audit, SYS-21 Performance Controller | DECIDED (DEC-017) | MON-008 |
| D-46 | SYS-33 Ledger | SYS-11 Reconciliation (venue-side deposits, withdrawals, balances) | DECIDED (DEC-006) | LED-005 |

## Stage-level dependencies (DECIDED, [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md))

```text
FOUNDATION
   ↓
DATA FOUNDATION
   ↓
CORE TRADING FOUNDATION   (incl. Policy System, operating modes, audit, system health, ledger)
   ↓
DIRECTIONAL TRADING       (builds the shared strategy management, backtesting, paper trading)
   ↓
ARBITRAGE                 (uses them; adds arbitrage cost components and the Performance Controller)
   ↓
AI INTELLIGENCE           (AI proposals validated by CORE's Risk Engine)
   ↓
OPERATIONALIZATION        (monitoring, reporting, hardening, deployment, canary, live operation)
```
