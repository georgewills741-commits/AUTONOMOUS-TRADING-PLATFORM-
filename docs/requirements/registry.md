# Requirements Registry

> **Index only.** Requirement text lives in the linked specification (DEC-003). This table is generated from the specifications, so rebuild or edit it together with them. Conventions: [README](README.md).
>
> **Source:** Handoff Part 1 · **Status of every entry:** DOCUMENTED — not implemented, not verified · **Total:** 228 requirements

## Summary by class

| Class | Count |
|---|---|
| CONFIRMED REQUIREMENT | 62 |
| CONFIRMED ARCHITECTURAL PRINCIPLE | 43 |
| CONSTRAINT | 66 |
| SYSTEM REQUIREMENT | 52 |
| PROPOSED | 1 |
| PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION | 4 |

Requiring confirmation before they can become production requirements: every PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION and PROPOSED entry, plus LED-001, which is conditional on OQ-01.

## Registry

| ID | Title | Class | Source | Owner | Specification | Stage (§95) |
|---|---|---|---|---|---|---|
| PLT-001 | Platform identity | CONFIRMED REQUIREMENT | §01 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| PLT-002 | Platform capability scope | CONFIRMED REQUIREMENT | §01 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| PLT-003 | Long-lived production platform | CONFIRMED ARCHITECTURAL PRINCIPLE | §01 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| PLT-004 | Controlled autonomous trading environment | CONFIRMED REQUIREMENT | §02 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| PLT-005 | No assumed profit | CONSTRAINT | §02 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| PLT-006 | Platform safety priority | CONFIRMED ARCHITECTURAL PRINCIPLE | §82 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| PLT-007 | No guaranteed returns | CONSTRAINT | §83 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| PLT-008 | No fixed daily percentage | CONSTRAINT | §83 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| PLT-009 | Platform objective | CONFIRMED REQUIREMENT | §83 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| MODE-001 | Four operating modes | CONFIRMED REQUIREMENT | §31 | Operating modes (owner not assigned, OQ-08) | [product/operating-modes.md](../product/operating-modes.md) | Not mapped |
| MODE-002 | Controlled mode transitions | CONSTRAINT | §31 | Operating modes (owner not assigned, OQ-08) | [product/operating-modes.md](../product/operating-modes.md) | Not mapped |
| ARCH-001 | Multiple trading systems | CONFIRMED ARCHITECTURAL PRINCIPLE | §03 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-002 | One platform, not three applications | CONSTRAINT | §03 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-003 | Reuse of common infrastructure | CONFIRMED ARCHITECTURAL PRINCIPLE | §04 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-004 | Ownership split | CONFIRMED ARCHITECTURAL PRINCIPLE | §04 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-005 | Two kinds of monitoring | CONFIRMED ARCHITECTURAL PRINCIPLE | §08 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-006 | Consistency and anti-drift | CONFIRMED REQUIREMENT | §69 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-007 | Changes checked against architecture | CONSTRAINT | §69 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-008 | Canonical conceptual flow | CONFIRMED ARCHITECTURAL PRINCIPLE | §70 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-009 | Explicit layer authority | CONSTRAINT | §70 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-010 | Numerical precision | CONFIRMED REQUIREMENT | §79 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-011 | Exchange-specific precision | CONSTRAINT | §79 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-012 | System boundary definition | CONFIRMED ARCHITECTURAL PRINCIPLE | §92 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-013 | Feature ownership chain | CONFIRMED ARCHITECTURAL PRINCIPLE | §93 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-014 | Dependencies respected | CONFIRMED ARCHITECTURAL PRINCIPLE | §94 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-015 | Feature classification | CONFIRMED REQUIREMENT | §96 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-016 | Duplication control | CONFIRMED ARCHITECTURAL PRINCIPLE | §97 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| ARCH-017 | Canonical source of truth | CONFIRMED ARCHITECTURAL PRINCIPLE | §98 | Platform architecture (cross-cutting) | [architecture/overview.md](../architecture/overview.md) | FOUNDATION |
| RMP-001 | Minimum stage classes | CONFIRMED REQUIREMENT | §95 | Roadmap | [roadmap/roadmap.md](../roadmap/roadmap.md) | FOUNDATION |
| EXA-001 | Standardized adapters | CONFIRMED ARCHITECTURAL PRINCIPLE | §42 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| EXA-002 | Candidate venues | PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION | §42 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| EXA-003 | Adapter responsibilities | SYSTEM REQUIREMENT | §42 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| EXA-004 | Standardized interfaces for the rest of the platform | CONFIRMED ARCHITECTURAL PRINCIPLE | §42 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| MKD-001 | Foundational shared infrastructure | CONFIRMED ARCHITECTURAL PRINCIPLE | §10 | SYS-02 Market-Data Infrastructure | [systems/market-data.md](../systems/market-data.md) | DATA FOUNDATION |
| MKD-002 | Data coverage | SYSTEM REQUIREMENT | §10 | SYS-02 Market-Data Infrastructure | [systems/market-data.md](../systems/market-data.md) | DATA FOUNDATION |
| MKD-003 | Market-data pipeline | CONFIRMED ARCHITECTURAL PRINCIPLE | §10 | SYS-02 Market-Data Infrastructure | [systems/market-data.md](../systems/market-data.md) | DATA FOUNDATION |
| MKD-004 | Data integrity protections | CONFIRMED REQUIREMENT | §10 | SYS-02 Market-Data Infrastructure | [systems/market-data.md](../systems/market-data.md) | DATA FOUNDATION |
| QNT-001 | Calculations without an LLM | CONFIRMED ARCHITECTURAL PRINCIPLE | §12 | SYS-03 Quantitative Engine | [systems/quantitative-engine.md](../systems/quantitative-engine.md) | DATA FOUNDATION |
| QNT-002 | Calculation scope | SYSTEM REQUIREMENT | §12 | SYS-03 Quantitative Engine | [systems/quantitative-engine.md](../systems/quantitative-engine.md) | DATA FOUNDATION |
| QNT-003 | Deterministic-first rule | CONSTRAINT | §12 | SYS-03 Quantitative Engine | [systems/quantitative-engine.md](../systems/quantitative-engine.md) | DATA FOUNDATION |
| RGM-001 | Explicit regime awareness | CONFIRMED REQUIREMENT | §11 | SYS-04 Market Regime Engine | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | DATA FOUNDATION |
| RGM-002 | Regime states | SYSTEM REQUIREMENT | §11 | SYS-04 Market Regime Engine | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | DATA FOUNDATION |
| RGM-003 | No forced classification | CONSTRAINT | §11 | SYS-04 Market Regime Engine | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | DATA FOUNDATION |
| RGM-004 | Regime-based strategy rejection | SYSTEM REQUIREMENT | §11 | SYS-04 Market Regime Engine | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | DATA FOUNDATION |
| OPP-001 | Monitor the whole configured universe | CONFIRMED REQUIREMENT | §08 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-002 | Scan dimensions | SYSTEM REQUIREMENT | §08 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-003 | Discover within the authorized universe | CONFIRMED REQUIREMENT | §08 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-004 | Not everything through AI | CONSTRAINT | §08 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-005 | Monitoring pipeline | CONFIRMED ARCHITECTURAL PRINCIPLE | §08 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-006 | Shared detection capability | CONFIRMED ARCHITECTURAL PRINCIPLE | §09 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-007 | Detection scope | SYSTEM REQUIREMENT | §09 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-008 | Deterministic screening, selective AI | CONFIRMED ARCHITECTURAL PRINCIPLE | §09 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| TNP-001 | Realistic executable economics | CONFIRMED REQUIREMENT | §13 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-002 | Conceptual cost stack | CONFIRMED ARCHITECTURAL PRINCIPLE | §13 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-003 | Formal formula required | CONFIRMED REQUIREMENT | §13 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-004 | Displayed differences are not profit | CONSTRAINT | §13 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-005 | No universal minimum profit threshold | CONSTRAINT | §14 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-006 | Positive-net opportunities are eligible | CONFIRMED REQUIREMENT | §14 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-007 | Economics, not labels | CONFIRMED REQUIREMENT | §14 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-008 | Small opportunities may accumulate | CONFIRMED REQUIREMENT | §15 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-009 | No large-trades-only assumption | CONSTRAINT | §15 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-010 | Cumulative effect counts | CONFIRMED REQUIREMENT | §15 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-011 | Small profit is not an automatic trade | CONSTRAINT | §15 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-012 | No conceptual ceiling | CONSTRAINT | §16 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-013 | Cumulative daily results are not capped | CONFIRMED REQUIREMENT | §16 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-014 | No guaranteed daily return | CONSTRAINT | §16 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-015 | Multi-dimensional quality | CONFIRMED REQUIREMENT | §17 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| TNP-016 | Percentage thresholds only as configurable filters | CONSTRAINT | §17 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION |
| CAP-001 | Single authoritative capital state | CONFIRMED ARCHITECTURAL PRINCIPLE | §18 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-002 | Capital categories | SYSTEM REQUIREMENT | §18 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-003 | No assumed capital | CONSTRAINT | §18 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-004 | Reservation flow | CONFIRMED ARCHITECTURAL PRINCIPLE | §19 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-005 | Reservation release | CONFIRMED REQUIREMENT | §19 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-006 | Dynamic capital allocation | SYSTEM REQUIREMENT | §20 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-007 | Efficiency, not exposure | CONSTRAINT | §20 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-008 | Opportunity competition | CONFIRMED ARCHITECTURAL PRINCIPLE | §21 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-009 | Not profitability alone | CONSTRAINT | §21 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-010 | Accumulating realized results | SYSTEM REQUIREMENT | §22 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-011 | Reinvesting realized profits | CONFIRMED REQUIREMENT | §22 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-012 | Compounding flow | CONFIRMED ARCHITECTURAL PRINCIPLE | §22 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-013 | Compounding is not a promise | CONSTRAINT | §22 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-014 | Respect existing commitments | CONSTRAINT | §23 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-015 | Grounds for rejecting a new opportunity | SYSTEM REQUIREMENT | §23 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| PRT-001 | One centralized portfolio view | CONFIRMED ARCHITECTURAL PRINCIPLE | §24 | SYS-08 Portfolio Management | [systems/portfolio-management.md](../systems/portfolio-management.md) | CORE TRADING FOUNDATION |
| PRT-002 | Tracked state | SYSTEM REQUIREMENT | §24 | SYS-08 Portfolio Management | [systems/portfolio-management.md](../systems/portfolio-management.md) | CORE TRADING FOUNDATION |
| PRT-003 | No competing portfolio truths | CONSTRAINT | §24 | SYS-08 Portfolio Management | [systems/portfolio-management.md](../systems/portfolio-management.md) | CORE TRADING FOUNDATION |
| RSK-001 | Deterministic enforcement | CONFIRMED ARCHITECTURAL PRINCIPLE | §25 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-002 | Risk controls | SYSTEM REQUIREMENT | §25 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-003 | AI cannot bypass risk | CONSTRAINT | §25 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-004 | Risk decision hierarchy | CONFIRMED ARCHITECTURAL PRINCIPLE | §26 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-005 | No override from below | CONSTRAINT | §26 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-006 | Valid outcomes | SYSTEM REQUIREMENT | §27 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-007 | No manufactured confidence | CONSTRAINT | §27 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| EXE-001 | Deterministic execution | CONFIRMED ARCHITECTURAL PRINCIPLE | §39 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-002 | Responsibilities | SYSTEM REQUIREMENT | §39 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-003 | Never trust AI claims of success | CONSTRAINT | §39 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-004 | Revalidate before execution | CONFIRMED REQUIREMENT | §40 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-005 | A timeout is not a failure | CONSTRAINT | §41 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-006 | Timeout handling | CONFIRMED REQUIREMENT | §41 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| REC-001 | External reality changes while offline | CONFIRMED ARCHITECTURAL PRINCIPLE | §71 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-002 | Recovery sequence | CONFIRMED REQUIREMENT | §71 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-003 | Restart does not authorize trading | CONSTRAINT | §72 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-004 | Resume preconditions | CONFIRMED REQUIREMENT | §72 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-005 | Determine real trade state | CONFIRMED REQUIREMENT | §73 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-006 | Never restore stale memory | CONSTRAINT | §73 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| POL-001 | User rules outside AI context | CONSTRAINT | §29 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | Not mapped (CF-06) |
| POL-002 | Structured, persistent, versioned policy | CONFIRMED REQUIREMENT | §29 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | Not mapped (CF-06) |
| POL-003 | Every meaningful change is a new version | CONFIRMED REQUIREMENT | §30 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | Not mapped (CF-06) |
| POL-004 | Change process | CONFIRMED REQUIREMENT | §30 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | Not mapped (CF-06) |
| NLP-001 | Built-in natural-language interface | CONFIRMED REQUIREMENT | §28 | SYS-13 Natural Language Policy Interface | [systems/policy/natural-language-policy-interface.md](../systems/policy/natural-language-policy-interface.md) | AI INTELLIGENCE |
| NLP-002 | Instruction categories | SYSTEM REQUIREMENT | §28 | SYS-13 Natural Language Policy Interface | [systems/policy/natural-language-policy-interface.md](../systems/policy/natural-language-policy-interface.md) | AI INTELLIGENCE |
| NLP-003 | Interface, not authority | CONFIRMED ARCHITECTURAL PRINCIPLE | §28 | SYS-13 Natural Language Policy Interface | [systems/policy/natural-language-policy-interface.md](../systems/policy/natural-language-policy-interface.md) | AI INTELLIGENCE |
| NLP-004 | Interpretation pipeline | CONFIRMED ARCHITECTURAL PRINCIPLE | §28 | SYS-13 Natural Language Policy Interface | [systems/policy/natural-language-policy-interface.md](../systems/policy/natural-language-policy-interface.md) | AI INTELLIGENCE |
| NLP-005 | Never silently more permissive | CONSTRAINT | §28 | SYS-13 Natural Language Policy Interface | [systems/policy/natural-language-policy-interface.md](../systems/policy/natural-language-policy-interface.md) | AI INTELLIGENCE |
| NLP-006 | Surface ambiguity | CONFIRMED REQUIREMENT | §28 | SYS-13 Natural Language Policy Interface | [systems/policy/natural-language-policy-interface.md](../systems/policy/natural-language-policy-interface.md) | AI INTELLIGENCE |
| STR-001 | Strategy lifecycle | CONFIRMED REQUIREMENT | §34 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| STR-002 | No AI shortcut through stages | CONSTRAINT | §34 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| STR-003 | Strategy Factory responsibilities | SYSTEM REQUIREMENT | §35 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| STR-004 | Factory cannot touch live trading | CONSTRAINT | §35 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| STR-005 | Every meaningful change is a new version | CONFIRMED REQUIREMENT | §36 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| STR-006 | No silent production changes | CONSTRAINT | §36 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| STR-007 | What research may do | CONFIRMED ARCHITECTURAL PRINCIPLE | §37 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| STR-008 | What research must not touch | CONSTRAINT | §37 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| STR-009 | Improvement path | CONFIRMED REQUIREMENT | §38 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| STR-010 | Forbidden reaction to losses | CONSTRAINT | §38 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| BKT-001 | Backtesting scope | SYSTEM REQUIREMENT | §33 | SYS-15 Backtesting | [systems/strategy/backtesting.md](../systems/strategy/backtesting.md) | DIRECTIONAL TRADING |
| BKT-002 | Bias and leakage protections | CONFIRMED REQUIREMENT | §33 | SYS-15 Backtesting | [systems/strategy/backtesting.md](../systems/strategy/backtesting.md) | DIRECTIONAL TRADING |
| BKT-003 | A backtest is not authorization | CONSTRAINT | §33 | SYS-15 Backtesting | [systems/strategy/backtesting.md](../systems/strategy/backtesting.md) | DIRECTIONAL TRADING |
| PAP-001 | Production architecture, realistically | CONFIRMED REQUIREMENT | §32 | SYS-16 Paper Trading | [systems/strategy/paper-trading.md](../systems/strategy/paper-trading.md) | DIRECTIONAL TRADING |
| PAP-002 | What paper trading accounts for | SYSTEM REQUIREMENT | §32 | SYS-16 Paper Trading | [systems/strategy/paper-trading.md](../systems/strategy/paper-trading.md) | DIRECTIONAL TRADING |
| DIR-001 | Purpose | CONFIRMED REQUIREMENT | §05 | SYS-17 Directional Trading System | [systems/directional-trading.md](../systems/directional-trading.md) | DIRECTIONAL TRADING |
| DIR-002 | Responsibilities | SYSTEM REQUIREMENT | §05 | SYS-17 Directional Trading System | [systems/directional-trading.md](../systems/directional-trading.md) | DIRECTIONAL TRADING |
| DIR-003 | Cannot bypass platform controls | CONSTRAINT | §05 | SYS-17 Directional Trading System | [systems/directional-trading.md](../systems/directional-trading.md) | DIRECTIONAL TRADING |
| XAR-001 | Purpose | CONFIRMED REQUIREMENT | §06 | SYS-18 Cross-Exchange Arbitrage System | [systems/arbitrage/cross-exchange-arbitrage.md](../systems/arbitrage/cross-exchange-arbitrage.md) | ARBITRAGE |
| XAR-002 | Real executable economics | CONSTRAINT | §06 | SYS-18 Cross-Exchange Arbitrage System | [systems/arbitrage/cross-exchange-arbitrage.md](../systems/arbitrage/cross-exchange-arbitrage.md) | ARBITRAGE |
| XAR-003 | Responsibilities | SYSTEM REQUIREMENT | §06 | SYS-18 Cross-Exchange Arbitrage System | [systems/arbitrage/cross-exchange-arbitrage.md](../systems/arbitrage/cross-exchange-arbitrage.md) | ARBITRAGE |
| XAR-004 | A price gap is not an opportunity | CONSTRAINT | §06 | SYS-18 Cross-Exchange Arbitrage System | [systems/arbitrage/cross-exchange-arbitrage.md](../systems/arbitrage/cross-exchange-arbitrage.md) | ARBITRAGE |
| TAR-001 | Purpose | CONFIRMED REQUIREMENT | §07 | SYS-19 Triangular Arbitrage System | [systems/arbitrage/triangular-arbitrage.md](../systems/arbitrage/triangular-arbitrage.md) | ARBITRAGE |
| TAR-002 | Responsibilities | SYSTEM REQUIREMENT | §07 | SYS-19 Triangular Arbitrage System | [systems/arbitrage/triangular-arbitrage.md](../systems/arbitrage/triangular-arbitrage.md) | ARBITRAGE |
| ARB-001 | Capability list | SYSTEM REQUIREMENT | §43 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-002 | Reuse shared infrastructure | CONSTRAINT | §43 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-003 | What the database records | SYSTEM REQUIREMENT | §44 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-004 | Purpose of the database | CONFIRMED REQUIREMENT | §44 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-005 | No automatic transfer after every trade | CONSTRAINT | §45 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-006 | Rebalancing evaluation | SYSTEM REQUIREMENT | §45 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-007 | Rebalancing is a capital-management decision | CONFIRMED ARCHITECTURAL PRINCIPLE | §45 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-008 | Sufficient reserves | CONFIRMED REQUIREMENT | §46 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-009 | Reserve lives in the Global Capital Authority | CONSTRAINT | §46 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-010 | Kill-switch triggers | SYSTEM REQUIREMENT | §47 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-011 | Global safety stays authoritative | CONSTRAINT | §47 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| PFC-001 | Expected-vs-actual comparison | CONFIRMED REQUIREMENT | §48 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| PFC-002 | Continuous comparison | SYSTEM REQUIREMENT | §49 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| PFC-003 | What it detects | SYSTEM REQUIREMENT | §49 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| PFC-004 | Only policy-permitted actions | CONSTRAINT | §49 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| PFC-005 | Two separate kinds of health | CONFIRMED ARCHITECTURAL PRINCIPLE | §50 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| AIL-001 | AI responsibilities | SYSTEM REQUIREMENT | §51 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
| AIL-002 | AI proposes, deterministic infrastructure enforces | CONFIRMED ARCHITECTURAL PRINCIPLE | §51 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
| AIL-003 | What AI must never do | CONSTRAINT | §52 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
| AIL-004 | No per-tick AI | CONSTRAINT | §53 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
| AIL-005 | Event-driven activation | CONFIRMED ARCHITECTURAL PRINCIPLE | §53 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
| AIV-001 | Evidence references | CONFIRMED REQUIREMENT | §64 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-002 | Mark unverifiable claims | CONFIRMED REQUIREMENT | §64 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-003 | Unverified claims are not evidence | CONSTRAINT | §64 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-004 | Machine-validated output | CONFIRMED REQUIREMENT | §65 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-005 | Conceptual output schema | SYSTEM REQUIREMENT | §65 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-006 | Reject malformed output | CONSTRAINT | §65 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-007 | Validation chain for important decisions | CONFIRMED ARCHITECTURAL PRINCIPLE | §66 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-008 | Validation policy options | SYSTEM REQUIREMENT | §66 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-009 | Risk remains authoritative | CONSTRAINT | §66 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-010 | Confidence is not probability | CONSTRAINT | §67 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-011 | Compare confidence with outcomes | CONFIRMED REQUIREMENT | §67 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-012 | Responses to overconfidence | SYSTEM REQUIREMENT | §67 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AGT-001 | Previously discussed roster | PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION | §54 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-002 | Find overlaps before implementation | CONFIRMED REQUIREMENT | §54 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-003 | No duplicate agents | CONSTRAINT | §54 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-004 | Trading Director | SYSTEM REQUIREMENT | §55 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-005 | Proposals are validated deterministically | CONFIRMED ARCHITECTURAL PRINCIPLE | §55 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-006 | Devil's Advocate | SYSTEM REQUIREMENT | §56 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-007 | Power to reject | CONFIRMED REQUIREMENT | §56 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-008 | Market Analyst | SYSTEM REQUIREMENT | §57 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-009 | Does not replace quantitative calculation | CONSTRAINT | §57 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-010 | Quant Research Agent | SYSTEM REQUIREMENT | §58 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-011 | Does not replace the Quantitative Engine | CONSTRAINT | §58 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-012 | AI strategy research and optimization | SYSTEM REQUIREMENT | §59 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-013 | Formal lifecycle required | CONSTRAINT | §59 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-014 | Performance Analyst | SYSTEM REQUIREMENT | §60 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| AGT-015 | Problem attribution | CONFIRMED REQUIREMENT | §60 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| RTR-001 | Routing tiers | SYSTEM REQUIREMENT | §63 | SYS-24 Model Router | [ai/model-management.md](../ai/model-management.md) | AI INTELLIGENCE |
| RTR-002 | Routing factors | SYSTEM REQUIREMENT | §63 | SYS-24 Model Router | [ai/model-management.md](../ai/model-management.md) | AI INTELLIGENCE |
| COST-001 | What the AI Cost Manager monitors | SYSTEM REQUIREMENT | §62 | SYS-25 AI Cost Manager | [ai/model-management.md](../ai/model-management.md) | AI INTELLIGENCE |
| MEV-001 | Evaluation dimensions | SYSTEM REQUIREMENT | §61 | SYS-26 Model Evaluation | [ai/model-management.md](../ai/model-management.md) | Not mapped |
| MEV-002 | Model performance is not profitability | CONSTRAINT | §61 | SYS-26 Model Evaluation | [ai/model-management.md](../ai/model-management.md) | Not mapped |
| MEM-001 | Knowledge not only in AI context | CONSTRAINT | §68 | SYS-27 AI Memory / Project Knowledge | [ai/ai-memory.md](../ai/ai-memory.md) | AI INTELLIGENCE |
| MEM-002 | Knowledge/memory architecture | SYSTEM REQUIREMENT | §68 | SYS-27 AI Memory / Project Knowledge | [ai/ai-memory.md](../ai/ai-memory.md) | AI INTELLIGENCE |
| MEM-003 | Memory properties | CONFIRMED REQUIREMENT | §68 | SYS-27 AI Memory / Project Knowledge | [ai/ai-memory.md](../ai/ai-memory.md) | AI INTELLIGENCE |
| MEM-004 | Not a second source of truth | CONSTRAINT | §68 | SYS-27 AI Memory / Project Knowledge | [ai/ai-memory.md](../ai/ai-memory.md) | AI INTELLIGENCE |
| MON-001 | Trading signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-002 | Infrastructure signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-003 | Exchange signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-004 | AI signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-005 | Risk signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-006 | Recovery signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| HLT-001 | Health states | SYSTEM REQUIREMENT | §74 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | Not mapped |
| HLT-002 | Formal state machine required | CONFIRMED REQUIREMENT | §74 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | Not mapped |
| HLT-003 | Expected failures | CONFIRMED REQUIREMENT | §90 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | Not mapped |
| HLT-004 | Fail safely | CONSTRAINT | §90 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | Not mapped |
| HLT-005 | Degradation examples | CONFIRMED ARCHITECTURAL PRINCIPLE | §91 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | Not mapped |
| HLT-006 | Per-subsystem failure behavior | CONFIRMED REQUIREMENT | §91 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | Not mapped |
| AUD-001 | Traceable actions | CONFIRMED REQUIREMENT | §86 | SYS-30 Auditability / Event and Decision History | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | Not mapped |
| AUD-002 | Audit record contents | SYSTEM REQUIREMENT | §86 | SYS-30 Auditability / Event and Decision History | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | Not mapped |
| AUD-003 | Events to preserve | SYSTEM REQUIREMENT | §87 | SYS-30 Auditability / Event and Decision History | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | Not mapped |
| SEC-001 | Protected assets | CONFIRMED REQUIREMENT | §89 | SYS-31 Security Architecture | [security/security-architecture.md](../security/security-architecture.md) | FOUNDATION |
| SEC-002 | No unrestricted credentials for AI agents | CONSTRAINT | §89 | SYS-31 Security Architecture | [security/security-architecture.md](../security/security-architecture.md) | FOUNDATION |
| CUS-001 | Platform-account architecture | PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION | §84 | SYS-32 Platform Account / Custody | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | Not mapped (requires confirmation) |
| CUS-002 | What it would require | PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION | §84 | SYS-32 Platform Account / Custody | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | Not mapped (requires confirmation) |
| CUS-003 | Not assumed approved | CONSTRAINT | §84 | SYS-32 Platform Account / Custody | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | Not mapped (requires confirmation) |
| LED-001 | Authoritative internal accounting, if user-facing | CONFIRMED REQUIREMENT | §85 | SYS-33 Ledger / Accounting | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | Not mapped (conditional) |
| LED-002 | Potential ledger scope | PROPOSED | §85 | SYS-33 Ledger / Accounting | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | Not mapped (conditional) |
| LED-003 | Trading-engine state is not the ledger | CONSTRAINT | §85 | SYS-33 Ledger / Accounting | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | Not mapped (conditional) |
| PERF-001 | Continuous operation | CONFIRMED REQUIREMENT | §75 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| PERF-002 | Performance is first-class | CONFIRMED REQUIREMENT | §76 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| PERF-003 | Latency-sensitive path | CONFIRMED ARCHITECTURAL PRINCIPLE | §77 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| PERF-004 | AI off the latency path | CONSTRAINT | §77 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| PERF-005 | Performance engineering techniques | CONFIRMED ARCHITECTURAL PRINCIPLE | §78 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| PERF-006 | Measured technology choices | CONSTRAINT | §78 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| OPS-001 | Operational readiness is not project completion | CONFIRMED ARCHITECTURAL PRINCIPLE | §80 | Deployment and operational readiness | [operations/deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) | OPERATIONALIZATION |
| OPS-002 | Subsystems can go live independently | CONFIRMED REQUIREMENT | §80 | Deployment and operational readiness | [operations/deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) | OPERATIONALIZATION |
| OPS-003 | Development while online | CONFIRMED REQUIREMENT | §81 | Deployment and operational readiness | [operations/deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) | OPERATIONALIZATION |
