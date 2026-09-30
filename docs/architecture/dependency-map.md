# Dependency Map

> **Status:** ACTIVE — derived from Handoff Part 1, updated 2026-09-30 with decisions DEC-006 to DEC-024 and Handoff Part 2 (edges D-54 to D-63). Part 2 gave roadmap sequences (RMP-004 to RMP-011) but no complete per-requirement dependency list; requirement-level dependencies are recorded when interfaces are designed (ARCH-030).
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
| D-47 | SYS-07 Global Capital Authority (rebalancing decision) | SYS-20 Arbitrage Intelligence (evaluation), SYS-12 Policy System (rebalancing controls), SYS-28 / SYS-29 (venue health) | DECIDED (DEC-019) | CAP-023, CAP-025 |
| D-48 | SYS-10 Execution Engine (transfers) | SYS-01 Exchange Adapters (transfer and transfer-status support) | DECIDED (DEC-019) | EXE-009, EXA-010 |
| D-49 | SYS-10 Execution Engine, SYS-11 Recovery | Execution lease (PostgreSQL) | DECIDED (DEC-019) | EXE-010, REC-013, TEC-013 |
| D-50 | SYS-09 Risk Engine (emergency controller) | SYS-12 Policy System (safety and position-protection policy), SYS-29 System Health, SYS-21 Performance Controller (degradation signals) | DECIDED (DEC-019) | RSK-015 to RSK-017, PERF-011 |
| D-51 | SYS-34 Readiness System (the Governance and Readiness Engine of DEC-023; registered separately from SYS-14 by DEC-024) | SYS-15, SYS-16, SYS-07 (capital availability), SYS-04 (regime), SYS-09 (risk validation), SYS-12 (policy validation), SYS-29 (system health) | DECIDED (DEC-019) | STR-013 to STR-016 |
| D-52 | SYS-06 True Net-Profit Engine (latency decay) | Measured latency from SYS-28 Monitoring | DECIDED (DEC-019) | TNP-023, PERF-010 |
| D-53 | SYS-09 Risk Engine (kill-switch recovery) | SYS-11 Reconciliation, SYS-29 System Health, SYS-02 Market Data (freshness), SYS-07 Capital (reservations), SYS-12 Policy | DECIDED (DEC-021) | RSK-021, RSK-023 |
| D-54 | SYS-34 Readiness System (evidence) | SYS-21 Performance Controller, SYS-28 incident records, SYS-02 data quality, SYS-11 reconciliation health, SYS-26 model behavior, in addition to D-51 | STATED | P2§65, P2§67; RDY-002 |
| D-55 | SYS-14 Strategy Management (APPROVAL stage) | SYS-34 Readiness System | DECIDED (DEC-024) | STR-019, RDY-006 |
| D-56 | SYS-16 Paper Trading | SYS-10 execution interface, SYS-07 (simulated capital), SYS-09 Risk Engine, SYS-02 live market data | STATED | P2§58, P2§60, P2§61; PAP-004, PAP-006, PAP-007 |
| D-57 | SYS-21 Performance Controller | SYS-16 paper results, SYS-05 Opportunity Database | STATED | P2§63, P2§75, P2§76; PFC-010, PFC-012, PFC-013 |
| D-58 | SYS-05 Opportunity Database | SYS-30 event and decision history | DECIDED (DEC-024) | OPP-016 |
| D-59 | SYS-28 Daily System Intelligence | Read-only: SYS-02, SYS-04, SYS-05, SYS-07, SYS-08, SYS-09, SYS-11, SYS-14, SYS-21, SYS-25, SYS-26, SYS-29, SYS-30, SYS-34, incident records | DECIDED (DEC-024) | DSI-006 |
| D-60 | SYS-22 AI Resource & Decision Governor | SYS-25 AI Cost Manager (budgets), SYS-24 Model Router (model selection) | DECIDED (DEC-024) | AIL-009 |
| D-61 | Hosting, backup, and migration (MIG) | SYS-11 Reconciliation, SYS-33 Ledger, SYS-10 (active execution authority), SYS-31 Security (secrets) | STATED | P2§139–P2§144; MIG-013 to MIG-018 |
| D-62 | SYS-09 Risk Engine (loss-streak and excessive-trading protection) | SYS-08 Portfolio and SYS-30 audit trail (trade and loss history), SYS-12 Policy (thresholds) | INFERRED (inputs not stated) | P2§40, P2§41; RSK-026, RSK-027 |
| D-63 | SYS-06 True Net-Profit Engine | SYS-03 Fee Engine and Slippage Engine (restates D-08 with Part 2's names) | DECIDED (DEC-011, DEC-024) | QNT-007 |

## Stage-level dependencies (DECIDED, [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md); Performance Controller placement changed by [DEC-024](../decisions/DEC-024-part-2-reconciliation.md))

```text
FOUNDATION
   ↓
DATA FOUNDATION
   ↓
CORE TRADING FOUNDATION   (incl. Policy System, operating modes, audit, system health, ledger)
   ↓
DIRECTIONAL TRADING       (builds the shared strategy management, backtesting, paper trading,
                           the Readiness System, and the Performance Controller's core)
   ↓
ARBITRAGE                 (uses them; adds arbitrage cost components and arbitrage performance tracking)
   ↓
AI INTELLIGENCE           (AI proposals validated by CORE's Risk Engine)
   ↓
OPERATIONALIZATION        (monitoring, reporting, hardening, deployment, canary, live operation)
```
