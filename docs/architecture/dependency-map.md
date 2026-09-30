# Dependency Map

> **Status:** ACTIVE — derived from Handoff Part 1 on 2026-09-30. Part 2 promises "complete dependency mapping"; revise this map when it arrives.
>
> Canonical record of which systems depend on which (ARCH-014). **STATED** edges come directly from handoff text (source given). **INFERRED** edges are the builder's reading of the text and need confirmation. System IDs are from the [system registry](system-registry.md).

## Handoff reference chain (§94)

```text
EXCHANGE ADAPTER → MARKET DATA → QUANTITATIVE ENGINE → OPPORTUNITY DETECTION
  → STRATEGY → RISK → CAPITAL → EXECUTION → PORTFOLIO / RECONCILIATION
```

§19 and §21 order capital before risk. That inconsistency is CF-01.

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
| D-08 | SYS-06 True Net-Profit Engine | SYS-03 Quantitative Engine (fees, spread, slippage) | INFERRED | §12, §13 |
| D-09 | SYS-06 True Net-Profit Engine | SYS-02 Market Data (order books, funding rates, exchange metadata) | INFERRED | §10, §13 |
| D-10 | SYS-18, SYS-19 arbitrage systems | SYS-06 True Net-Profit Engine | INFERRED (depends on DUP-01 resolution) | §06, §07, §13 |
| D-11 | SYS-18, SYS-19 arbitrage systems | SYS-20 Arbitrage Intelligence | INFERRED | §43 |
| D-12 | SYS-09 Risk Engine | Strategy output from SYS-17/18/19 | STATED | §94 |
| D-13 | SYS-09 Risk Engine | SYS-12 Policy System (user hard constraints) | STATED | §26, §28–§29 |
| D-14 | SYS-09 Risk Engine | SYS-08 Portfolio (exposure, portfolio limits) | INFERRED | §24, §25 |
| D-15 | SYS-07 Global Capital Authority | SYS-09 Risk Engine (risk check) | STATED (order disputed, CF-01) | §19, §21 |
| D-16 | SYS-07 Global Capital Authority | SYS-12 Policy System (user policy, capital authorization) | STATED | §20, §22, §28 |
| D-17 | SYS-07 Global Capital Authority | SYS-33 Ledger / accounting (compounding) | STATED, conditional (OQ-02) | §22 |
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
| D-31 | SYS-21 Performance Controller | SYS-20 Arbitrage Intelligence (opportunity database), SYS-30 Audit, SYS-08 Portfolio | INFERRED | §44, §48, §49 |
| D-32 | SYS-23 AI Agents | SYS-22 AI Intelligence Layer (validation), SYS-24 Model Router | INFERRED | §63–§66 |
| D-33 | SYS-23 Trading Director | Market data, quantitative features, regime, portfolio, policy, risk state | STATED (listed inputs) | §55 |
| D-34 | SYS-09 Risk Engine | SYS-23 Trading Director proposals (validated) | STATED | §55, §66 |
| D-35 | SYS-24 Model Router | SYS-26 Model Evaluation, SYS-25 AI Cost Manager | INFERRED ("current model performance", "cost", "budget") | §63 |
| D-36 | SYS-22 Hallucination Firewall | Evidence identifiers from SYS-02, SYS-03, SYS-30 | INFERRED (TC-06) | §64 |
| D-37 | SYS-20 Arbitrage Intelligence | SYS-07 Global Capital Authority (reserve, rebalancing decision) | STATED | §45, §46 |
| D-38 | SYS-28 Monitoring | All systems | INFERRED | §88 |
| D-39 | SYS-29 System Health | SYS-28 Monitoring | INFERRED | §74, §88 |
| D-40 | SYS-30 Audit | All acting systems ("which system acted") | STATED | §86 |

## Stage-level dependencies (PROPOSED)

Derived from the edges above. The roadmap uses this order; the handoff reserves final sequencing for the master roadmap (§95).

```text
FOUNDATION
   ↓
DATA FOUNDATION ──────────────┐
   ↓                          │
CORE TRADING FOUNDATION       │   (needs structured Policy System — CF-06)
   ↓            ↓             │
DIRECTIONAL   ARBITRAGE       │
   ↓            ↓             ↓
AI INTELLIGENCE  (AI proposals are validated by CORE's Risk Engine)
   ↓
OPERATIONALIZATION  (monitoring, recovery, deployment; parts needed earlier — CF-05)
```
