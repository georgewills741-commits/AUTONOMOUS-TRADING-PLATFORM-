# Requirements Registry

> **Index only.** Requirement text lives in the linked specification (DEC-003). This table is generated from the specifications, so rebuild or edit it together with them. Conventions: [README](README.md).
>
> **Sources:** Handoff Part 1 (228) and decision records (109) · **Status of every entry:** DOCUMENTED — not implemented, not verified · **Total:** 337 requirements

## Summary by class

| Class | Count |
|---|---|
| CONFIRMED REQUIREMENT | 96 |
| CONFIRMED ARCHITECTURAL PRINCIPLE | 85 |
| CONSTRAINT | 89 |
| SYSTEM REQUIREMENT | 62 |
| FUTURE | 2 |
| DEPRECATED / REPLACED | 3 |

Nothing awaits confirmation. The previously discussed and proposed items were decided on 2026-09-30: FUTURE entries are recorded but not built, and each DEPRECATED / REPLACED entry names its replacement in its specification. LED-001 stays conditional on a user-facing platform, which the platform currently is not (DEC-006).

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
| PLT-010 | Single-operator platform | CONFIRMED REQUIREMENT | DEC-006 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| PLT-011 | Instrument scope | CONFIRMED REQUIREMENT | DEC-007 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| PLT-012 | Instrument types gated by their risk controls | CONSTRAINT | DEC-007 | Platform (product level) | [product/platform-overview.md](../product/platform-overview.md) | — (platform-wide) |
| MODE-001 | Four operating modes | CONFIRMED REQUIREMENT | §31 | Operating modes (Policy System, POL-008) | [product/operating-modes.md](../product/operating-modes.md) | CORE TRADING FOUNDATION |
| MODE-002 | Controlled mode transitions | CONSTRAINT | §31 | Operating modes (Policy System, POL-008) | [product/operating-modes.md](../product/operating-modes.md) | CORE TRADING FOUNDATION |
| MODE-003 | Per-strategy modes under a platform maximum | CONFIRMED REQUIREMENT | DEC-015 | Operating modes (Policy System, POL-008) | [product/operating-modes.md](../product/operating-modes.md) | CORE TRADING FOUNDATION |
| MODE-004 | Mode transitions | CONSTRAINT | DEC-015 | Operating modes (Policy System, POL-008) | [product/operating-modes.md](../product/operating-modes.md) | CORE TRADING FOUNDATION |
| MODE-005 | Supervised authorization | SYSTEM REQUIREMENT | DEC-015 | Operating modes (Policy System, POL-008) | [product/operating-modes.md](../product/operating-modes.md) | CORE TRADING FOUNDATION |
| MODE-006 | Modes vs environments | CONSTRAINT | DEC-015 | Operating modes (Policy System, POL-008) | [product/operating-modes.md](../product/operating-modes.md) | CORE TRADING FOUNDATION |
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
| TEC-001 | Primary language | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| TEC-002 | Rust only for measured hot paths | CONSTRAINT | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| TEC-003 | Exact decimal arithmetic | CONSTRAINT | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| TEC-004 | Validated contracts | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| TEC-005 | Exchange connectivity library | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| TEC-006 | Storage | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| TEC-007 | Messaging | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| TEC-008 | Modular monolith | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| TEC-009 | Reproducible tooling | CONFIRMED REQUIREMENT | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| TEC-010 | Observability stack | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| TEC-011 | Deployment | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| TEC-012 | Data retention | CONFIRMED REQUIREMENT | DEC-009 | Technology stack | [architecture/technology-stack.md](../architecture/technology-stack.md) | FOUNDATION |
| RMP-001 | Minimum stage classes | CONFIRMED REQUIREMENT | §95 | Roadmap | [roadmap/roadmap.md](../roadmap/roadmap.md) | FOUNDATION |
| RMP-002 | Sequential stages | CONFIRMED REQUIREMENT | DEC-016 | Roadmap | [roadmap/roadmap.md](../roadmap/roadmap.md) | FOUNDATION |
| EXA-001 | Standardized adapters | CONFIRMED ARCHITECTURAL PRINCIPLE | §42 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| EXA-002 | Candidate venues | DEPRECATED / REPLACED | §42 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| EXA-003 | Adapter responsibilities | SYSTEM REQUIREMENT | §42 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| EXA-004 | Standardized interfaces for the rest of the platform | CONFIRMED ARCHITECTURAL PRINCIPLE | §42 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| EXA-005 | Initial venues | CONFIRMED REQUIREMENT | DEC-008 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| EXA-006 | New venues without platform changes | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-008 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| EXA-007 | Legitimate access only | CONSTRAINT | DEC-008 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| EXA-008 | Order-state query is mandatory | CONSTRAINT | DEC-008 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| EXA-009 | Instrument support per venue | SYSTEM REQUIREMENT | DEC-007 | SYS-01 Exchange Adapter Layer | [systems/exchange-adapters.md](../systems/exchange-adapters.md) | DATA FOUNDATION |
| MKD-001 | Foundational shared infrastructure | CONFIRMED ARCHITECTURAL PRINCIPLE | §10 | SYS-02 Market-Data Infrastructure | [systems/market-data.md](../systems/market-data.md) | DATA FOUNDATION |
| MKD-002 | Data coverage | SYSTEM REQUIREMENT | §10 | SYS-02 Market-Data Infrastructure | [systems/market-data.md](../systems/market-data.md) | DATA FOUNDATION |
| MKD-003 | Market-data pipeline | CONFIRMED ARCHITECTURAL PRINCIPLE | §10 | SYS-02 Market-Data Infrastructure | [systems/market-data.md](../systems/market-data.md) | DATA FOUNDATION |
| MKD-004 | Data integrity protections | CONFIRMED REQUIREMENT | §10 | SYS-02 Market-Data Infrastructure | [systems/market-data.md](../systems/market-data.md) | DATA FOUNDATION |
| MKD-005 | Evidence identifiers | CONFIRMED REQUIREMENT | DEC-013 | SYS-02 Market-Data Infrastructure | [systems/market-data.md](../systems/market-data.md) | DATA FOUNDATION |
| MKD-006 | Freshness limits | CONSTRAINT | DEC-012 | SYS-02 Market-Data Infrastructure | [systems/market-data.md](../systems/market-data.md) | DATA FOUNDATION |
| MKD-007 | Storage and retention | SYSTEM REQUIREMENT | DEC-009 | SYS-02 Market-Data Infrastructure | [systems/market-data.md](../systems/market-data.md) | DATA FOUNDATION |
| QNT-001 | Calculations without an LLM | CONFIRMED ARCHITECTURAL PRINCIPLE | §12 | SYS-03 Quantitative Engine | [systems/quantitative-engine.md](../systems/quantitative-engine.md) | DATA FOUNDATION |
| QNT-002 | Calculation scope | SYSTEM REQUIREMENT | §12 | SYS-03 Quantitative Engine | [systems/quantitative-engine.md](../systems/quantitative-engine.md) | DATA FOUNDATION |
| QNT-003 | Deterministic-first rule | CONSTRAINT | §12 | SYS-03 Quantitative Engine | [systems/quantitative-engine.md](../systems/quantitative-engine.md) | DATA FOUNDATION |
| QNT-004 | Primitive metrics only | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-03 Quantitative Engine | [systems/quantitative-engine.md](../systems/quantitative-engine.md) | DATA FOUNDATION |
| RGM-001 | Explicit regime awareness | CONFIRMED REQUIREMENT | §11 | SYS-04 Market Regime Engine | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | DATA FOUNDATION |
| RGM-002 | Regime states | SYSTEM REQUIREMENT | §11 | SYS-04 Market Regime Engine | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | DATA FOUNDATION |
| RGM-003 | No forced classification | CONSTRAINT | §11 | SYS-04 Market Regime Engine | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | DATA FOUNDATION |
| RGM-004 | Regime-based strategy rejection | SYSTEM REQUIREMENT | §11 | SYS-04 Market Regime Engine | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | DATA FOUNDATION |
| RGM-005 | Deterministic classification | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-04 Market Regime Engine | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | DATA FOUNDATION |
| RGM-006 | Authority over regime state | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-04 Market Regime Engine | [systems/market-regime-engine.md](../systems/market-regime-engine.md) | DATA FOUNDATION |
| OPP-001 | Monitor the whole configured universe | CONFIRMED REQUIREMENT | §08 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-002 | Scan dimensions | SYSTEM REQUIREMENT | §08 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-003 | Discover within the authorized universe | CONFIRMED REQUIREMENT | §08 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-004 | Not everything through AI | CONSTRAINT | §08 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-005 | Monitoring pipeline | CONFIRMED ARCHITECTURAL PRINCIPLE | §08 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-006 | Shared detection capability | CONFIRMED ARCHITECTURAL PRINCIPLE | §09 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-007 | Detection scope | SYSTEM REQUIREMENT | §09 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-008 | Deterministic screening, selective AI | CONFIRMED ARCHITECTURAL PRINCIPLE | §09 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-009 | Trading universe | CONFIRMED REQUIREMENT | DEC-008 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-010 | Single owner of market monitoring | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-011 | Detection, not allocation ranking | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| OPP-012 | Tiered monitoring | SYSTEM REQUIREMENT | DEC-017 | SYS-05 Opportunity Detection Engine | [systems/opportunity-detection.md](../systems/opportunity-detection.md) | DATA FOUNDATION |
| TNP-001 | Realistic executable economics | CONFIRMED REQUIREMENT | §13 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-002 | Conceptual cost stack | CONFIRMED ARCHITECTURAL PRINCIPLE | §13 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-003 | Formal formula required | CONFIRMED REQUIREMENT | §13 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-004 | Displayed differences are not profit | CONSTRAINT | §13 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-005 | No universal minimum profit threshold | CONSTRAINT | §14 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-006 | Positive-net opportunities are eligible | CONFIRMED REQUIREMENT | §14 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-007 | Economics, not labels | CONFIRMED REQUIREMENT | §14 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-008 | Small opportunities may accumulate | CONFIRMED REQUIREMENT | §15 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-009 | No large-trades-only assumption | CONSTRAINT | §15 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-010 | Cumulative effect counts | CONFIRMED REQUIREMENT | §15 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-011 | Small profit is not an automatic trade | CONSTRAINT | §15 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-012 | No conceptual ceiling | CONSTRAINT | §16 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-013 | Cumulative daily results are not capped | CONFIRMED REQUIREMENT | §16 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-014 | No guaranteed daily return | CONSTRAINT | §16 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-015 | Multi-dimensional quality | CONFIRMED REQUIREMENT | §17 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-016 | Percentage thresholds only as configurable filters | CONSTRAINT | §17 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-017 | Sole owner of the true net expected result | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-018 | Formula | CONFIRMED REQUIREMENT | DEC-014 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-019 | Uncertainty margin from measured uncertainty | CONSTRAINT | DEC-014 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-020 | Economic eligibility | CONFIRMED REQUIREMENT | DEC-014 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-021 | Comparable quality measure | SYSTEM REQUIREMENT | DEC-011 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
| TNP-022 | Continuous calibration | CONFIRMED REQUIREMENT | DEC-014 | SYS-06 True Net-Profit Engine | [systems/true-net-profit-engine.md](../systems/true-net-profit-engine.md) | CORE TRADING FOUNDATION (+ ARBITRAGE cost components) |
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
| CAP-016 | Runtime order of capital and risk | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-010 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-017 | Allocation and ranking authority | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-018 | Rebalancing decisions | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-019 | Capital derived from the ledger | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-006 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-020 | Collateral and margin categories | SYSTEM REQUIREMENT | DEC-007 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-021 | Reservation on the latency-sensitive path | CONFIRMED REQUIREMENT | DEC-010 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| CAP-022 | Rebalancing transfers need confirmation by default | CONSTRAINT | DEC-012 | SYS-07 Global Capital Authority | [systems/capital-management.md](../systems/capital-management.md) | CORE TRADING FOUNDATION |
| PRT-001 | One centralized portfolio view | CONFIRMED ARCHITECTURAL PRINCIPLE | §24 | SYS-08 Portfolio Management | [systems/portfolio-management.md](../systems/portfolio-management.md) | CORE TRADING FOUNDATION |
| PRT-002 | Tracked state | SYSTEM REQUIREMENT | §24 | SYS-08 Portfolio Management | [systems/portfolio-management.md](../systems/portfolio-management.md) | CORE TRADING FOUNDATION |
| PRT-003 | No competing portfolio truths | CONSTRAINT | §24 | SYS-08 Portfolio Management | [systems/portfolio-management.md](../systems/portfolio-management.md) | CORE TRADING FOUNDATION |
| PRT-004 | Capital and realized P&L are read-only here | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-08 Portfolio Management | [systems/portfolio-management.md](../systems/portfolio-management.md) | CORE TRADING FOUNDATION |
| PRT-005 | Derivatives and margin exposure | SYSTEM REQUIREMENT | DEC-007 | SYS-08 Portfolio Management | [systems/portfolio-management.md](../systems/portfolio-management.md) | CORE TRADING FOUNDATION |
| RSK-001 | Deterministic enforcement | CONFIRMED ARCHITECTURAL PRINCIPLE | §25 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-002 | Risk controls | SYSTEM REQUIREMENT | §25 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-003 | AI cannot bypass risk | CONSTRAINT | §25 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-004 | Risk decision hierarchy | CONFIRMED ARCHITECTURAL PRINCIPLE | §26 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-005 | No override from below | CONSTRAINT | §26 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-006 | Valid outcomes | SYSTEM REQUIREMENT | §27 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-007 | No manufactured confidence | CONSTRAINT | §27 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-008 | Kill switches and the global safety architecture | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-012 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-009 | Kill-switch activation and reset | CONSTRAINT | DEC-012 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-010 | System safety rules | CONFIRMED REQUIREMENT | DEC-012 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-011 | Final position size | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-010 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-012 | Arbitrage risk as rule sets | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-013 | Derivatives and margin controls | CONFIRMED REQUIREMENT | DEC-007 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| RSK-014 | Uncertainty means no new position | CONSTRAINT | DEC-013 | SYS-09 Risk Engine | [risk/risk-engine.md](../risk/risk-engine.md) | CORE TRADING FOUNDATION |
| EXE-001 | Deterministic execution | CONFIRMED ARCHITECTURAL PRINCIPLE | §39 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-002 | Responsibilities | SYSTEM REQUIREMENT | §39 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-003 | Never trust AI claims of success | CONSTRAINT | §39 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-004 | Revalidate before execution | CONFIRMED REQUIREMENT | §40 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-005 | A timeout is not a failure | CONSTRAINT | §41 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-006 | Timeout handling | CONFIRMED REQUIREMENT | §41 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-007 | Reconciliation is invoked, not reimplemented | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| EXE-008 | Client order IDs | CONSTRAINT | DEC-008 | SYS-10 Execution Engine | [systems/execution-engine.md](../systems/execution-engine.md) | CORE TRADING FOUNDATION |
| REC-001 | External reality changes while offline | CONFIRMED ARCHITECTURAL PRINCIPLE | §71 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-002 | Recovery sequence | CONFIRMED REQUIREMENT | §71 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-003 | Restart does not authorize trading | CONSTRAINT | §72 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-004 | Resume preconditions | CONFIRMED REQUIREMENT | §72 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-005 | Determine real trade state | CONFIRMED REQUIREMENT | §73 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-006 | Never restore stale memory | CONSTRAINT | §73 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-007 | Verify the database before loading from it | CONFIRMED REQUIREMENT | DEC-010 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-008 | Sole owner of reconciliation | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| REC-009 | Resuming after a restart | CONSTRAINT | DEC-012 | SYS-11 Recovery and Reconciliation | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| POL-001 | User rules outside AI context | CONSTRAINT | §29 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | CORE TRADING FOUNDATION |
| POL-002 | Structured, persistent, versioned policy | CONFIRMED REQUIREMENT | §29 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | CORE TRADING FOUNDATION |
| POL-003 | Every meaningful change is a new version | CONFIRMED REQUIREMENT | §30 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | CORE TRADING FOUNDATION |
| POL-004 | Change process | CONFIRMED REQUIREMENT | §30 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | CORE TRADING FOUNDATION |
| POL-005 | Important changes need confirmation | CONFIRMED REQUIREMENT | DEC-015 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | CORE TRADING FOUNDATION |
| POL-006 | Simulation before loosening | CONFIRMED REQUIREMENT | DEC-015 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | CORE TRADING FOUNDATION |
| POL-007 | Tightening changes activate immediately | CONFIRMED REQUIREMENT | DEC-015 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | CORE TRADING FOUNDATION |
| POL-008 | Operating mode is policy | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-015 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | CORE TRADING FOUNDATION |
| POL-009 | Single location of policy | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-015 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | CORE TRADING FOUNDATION |
| POL-010 | Structured editing before the NL interface | CONFIRMED REQUIREMENT | DEC-015 | SYS-12 Policy System | [systems/policy/policy-system.md](../systems/policy/policy-system.md) | CORE TRADING FOUNDATION |
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
| STR-011 | Canary | CONFIRMED REQUIREMENT | DEC-015 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| STR-012 | The Strategy Factory owns the research process | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-14 Strategy Management | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) | DIRECTIONAL TRADING |
| BKT-001 | Backtesting scope | SYSTEM REQUIREMENT | §33 | SYS-15 Backtesting | [systems/strategy/backtesting.md](../systems/strategy/backtesting.md) | DIRECTIONAL TRADING |
| BKT-002 | Bias and leakage protections | CONFIRMED REQUIREMENT | §33 | SYS-15 Backtesting | [systems/strategy/backtesting.md](../systems/strategy/backtesting.md) | DIRECTIONAL TRADING |
| BKT-003 | A backtest is not authorization | CONSTRAINT | §33 | SYS-15 Backtesting | [systems/strategy/backtesting.md](../systems/strategy/backtesting.md) | DIRECTIONAL TRADING |
| PAP-001 | Production architecture, realistically | CONFIRMED REQUIREMENT | §32 | SYS-16 Paper Trading | [systems/strategy/paper-trading.md](../systems/strategy/paper-trading.md) | DIRECTIONAL TRADING |
| PAP-002 | What paper trading accounts for | SYSTEM REQUIREMENT | §32 | SYS-16 Paper Trading | [systems/strategy/paper-trading.md](../systems/strategy/paper-trading.md) | DIRECTIONAL TRADING |
| PAP-003 | Paper does not validate small margins | CONSTRAINT | DEC-014 | SYS-16 Paper Trading | [systems/strategy/paper-trading.md](../systems/strategy/paper-trading.md) | DIRECTIONAL TRADING |
| DIR-001 | Purpose | CONFIRMED REQUIREMENT | §05 | SYS-17 Directional Trading System | [systems/directional-trading.md](../systems/directional-trading.md) | DIRECTIONAL TRADING |
| DIR-002 | Responsibilities | SYSTEM REQUIREMENT | §05 | SYS-17 Directional Trading System | [systems/directional-trading.md](../systems/directional-trading.md) | DIRECTIONAL TRADING |
| DIR-003 | Cannot bypass platform controls | CONSTRAINT | §05 | SYS-17 Directional Trading System | [systems/directional-trading.md](../systems/directional-trading.md) | DIRECTIONAL TRADING |
| DIR-004 | Directional logic, shared infrastructure | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-17 Directional Trading System | [systems/directional-trading.md](../systems/directional-trading.md) | DIRECTIONAL TRADING |
| DIR-005 | Initial research candidates | SYSTEM REQUIREMENT | DEC-018 | SYS-17 Directional Trading System | [systems/directional-trading.md](../systems/directional-trading.md) | DIRECTIONAL TRADING |
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
| ARB-012 | Arbitrage systems use shared owners | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-013 | Deterministic arbitrage | CONSTRAINT | DEC-013 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| ARB-014 | Opportunity database is derived from events | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-20 Arbitrage Intelligence | [systems/arbitrage/arbitrage-intelligence.md](../systems/arbitrage/arbitrage-intelligence.md) | ARBITRAGE |
| PFC-001 | Expected-vs-actual comparison | CONFIRMED REQUIREMENT | §48 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| PFC-002 | Continuous comparison | SYSTEM REQUIREMENT | §49 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| PFC-003 | What it detects | SYSTEM REQUIREMENT | §49 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| PFC-004 | Only policy-permitted actions | CONSTRAINT | §49 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| PFC-005 | Two separate kinds of health | CONFIRMED ARCHITECTURAL PRINCIPLE | §50 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| PFC-006 | One platform-wide controller | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| PFC-007 | Detection here, interpretation by the analyst | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-013 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| PFC-008 | Permitted actions | CONFIRMED REQUIREMENT | DEC-012 | SYS-21 Performance Controller | [systems/performance-controller.md](../systems/performance-controller.md) | ARBITRAGE |
| AIL-001 | AI responsibilities | SYSTEM REQUIREMENT | §51 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
| AIL-002 | AI proposes, deterministic infrastructure enforces | CONFIRMED ARCHITECTURAL PRINCIPLE | §51 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
| AIL-003 | What AI must never do | CONSTRAINT | §52 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
| AIL-004 | No per-tick AI | CONSTRAINT | §53 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
| AIL-005 | Event-driven activation | CONFIRMED ARCHITECTURAL PRINCIPLE | §53 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
| AIL-006 | AI gateway | CONFIRMED REQUIREMENT | DEC-013 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
| AIL-007 | Provider-agnostic | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-009 | SYS-22 AI Intelligence Layer | [ai/ai-architecture.md](../ai/ai-architecture.md) | AI INTELLIGENCE |
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
| AIV-013 | Decision values | CONFIRMED REQUIREMENT | DEC-013 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-014 | Validation policy | CONFIRMED REQUIREMENT | DEC-013 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AIV-015 | Important decisions | CONFIRMED REQUIREMENT | DEC-013 | SYS-22 AI Intelligence Layer (output validation) | [ai/ai-output-validation.md](../ai/ai-output-validation.md) | AI INTELLIGENCE |
| AGT-001 | Previously discussed roster | DEPRECATED / REPLACED | §54 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
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
| AGT-016 | Final agent roster | CONFIRMED REQUIREMENT | DEC-013 | SYS-23 AI Agents | [ai/agents.md](../ai/agents.md) | AI INTELLIGENCE |
| RTR-001 | Routing tiers | SYSTEM REQUIREMENT | §63 | SYS-24 Model Router | [ai/model-management.md](../ai/model-management.md) | AI INTELLIGENCE |
| RTR-002 | Routing factors | SYSTEM REQUIREMENT | §63 | SYS-24 Model Router | [ai/model-management.md](../ai/model-management.md) | AI INTELLIGENCE |
| RTR-003 | Deterministic routing | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-013 | SYS-24 Model Router | [ai/model-management.md](../ai/model-management.md) | AI INTELLIGENCE |
| COST-001 | What the AI Cost Manager monitors | SYSTEM REQUIREMENT | §62 | SYS-25 AI Cost Manager | [ai/model-management.md](../ai/model-management.md) | AI INTELLIGENCE |
| COST-002 | AI Cost Manager is deterministic | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-013 | SYS-25 AI Cost Manager | [ai/model-management.md](../ai/model-management.md) | AI INTELLIGENCE |
| MEV-001 | Evaluation dimensions | SYSTEM REQUIREMENT | §61 | SYS-26 Model Evaluation | [ai/model-management.md](../ai/model-management.md) | AI INTELLIGENCE |
| MEV-002 | Model performance is not profitability | CONSTRAINT | §61 | SYS-26 Model Evaluation | [ai/model-management.md](../ai/model-management.md) | AI INTELLIGENCE |
| MEV-003 | Model Evaluation is deterministic | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-013 | SYS-26 Model Evaluation | [ai/model-management.md](../ai/model-management.md) | AI INTELLIGENCE |
| MEM-001 | Knowledge not only in AI context | CONSTRAINT | §68 | SYS-27 AI Memory / Project Knowledge | [ai/ai-memory.md](../ai/ai-memory.md) | AI INTELLIGENCE |
| MEM-002 | Knowledge/memory architecture | SYSTEM REQUIREMENT | §68 | SYS-27 AI Memory / Project Knowledge | [ai/ai-memory.md](../ai/ai-memory.md) | AI INTELLIGENCE |
| MEM-003 | Memory properties | CONFIRMED REQUIREMENT | §68 | SYS-27 AI Memory / Project Knowledge | [ai/ai-memory.md](../ai/ai-memory.md) | AI INTELLIGENCE |
| MEM-004 | Not a second source of truth | CONSTRAINT | §68 | SYS-27 AI Memory / Project Knowledge | [ai/ai-memory.md](../ai/ai-memory.md) | AI INTELLIGENCE |
| MEM-005 | Reference, never copy | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-27 AI Memory / Project Knowledge | [ai/ai-memory.md](../ai/ai-memory.md) | AI INTELLIGENCE |
| MON-001 | Trading signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-002 | Infrastructure signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-003 | Exchange signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-004 | AI signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-005 | Risk signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-006 | Recovery signals | SYSTEM REQUIREMENT | §88 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-007 | Alerting | CONFIRMED REQUIREMENT | DEC-017 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-008 | Reporting | CONFIRMED REQUIREMENT | DEC-017 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| MON-009 | Operational logs | SYSTEM REQUIREMENT | DEC-017 | SYS-28 Monitoring and Observability | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md) | OPERATIONALIZATION |
| HLT-001 | Health states | SYSTEM REQUIREMENT | §74 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| HLT-002 | Formal state machine required | CONFIRMED REQUIREMENT | §74 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| HLT-003 | Expected failures | CONFIRMED REQUIREMENT | §90 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| HLT-004 | Fail safely | CONSTRAINT | §90 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| HLT-005 | Degradation examples | CONFIRMED ARCHITECTURAL PRINCIPLE | §91 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| HLT-006 | Per-subsystem failure behavior | CONFIRMED REQUIREMENT | §91 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| HLT-007 | Formal states | CONFIRMED REQUIREMENT | DEC-012 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| HLT-008 | Trading allowed per state | CONSTRAINT | DEC-012 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| HLT-009 | Transitions | CONSTRAINT | DEC-012 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| HLT-010 | Ownership of platform state | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-012 | SYS-29 System Health | [operations/system-health.md](../operations/system-health.md) | CORE TRADING FOUNDATION / OPERATIONALIZATION |
| AUD-001 | Traceable actions | CONFIRMED REQUIREMENT | §86 | SYS-30 Auditability / Event and Decision History | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | CORE TRADING FOUNDATION |
| AUD-002 | Audit record contents | SYSTEM REQUIREMENT | §86 | SYS-30 Auditability / Event and Decision History | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | CORE TRADING FOUNDATION |
| AUD-003 | Events to preserve | SYSTEM REQUIREMENT | §87 | SYS-30 Auditability / Event and Decision History | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | CORE TRADING FOUNDATION |
| AUD-004 | Append-only and permanent | CONSTRAINT | DEC-009 | SYS-30 Auditability / Event and Decision History | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | CORE TRADING FOUNDATION |
| AUD-005 | Authoritative event record | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-011 | SYS-30 Auditability / Event and Decision History | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | CORE TRADING FOUNDATION |
| AUD-006 | Separate from operational logs | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-017 | SYS-30 Auditability / Event and Decision History | [systems/audit-and-event-history.md](../systems/audit-and-event-history.md) | CORE TRADING FOUNDATION |
| SEC-001 | Protected assets | CONFIRMED REQUIREMENT | §89 | SYS-31 Security Architecture | [security/security-architecture.md](../security/security-architecture.md) | FOUNDATION |
| SEC-002 | No unrestricted credentials for AI agents | CONSTRAINT | §89 | SYS-31 Security Architecture | [security/security-architecture.md](../security/security-architecture.md) | FOUNDATION |
| SEC-003 | Trading keys cannot withdraw | CONSTRAINT | DEC-012 | SYS-31 Security Architecture | [security/security-architecture.md](../security/security-architecture.md) | FOUNDATION |
| SEC-004 | Credential separation | CONSTRAINT | DEC-015 | SYS-31 Security Architecture | [security/security-architecture.md](../security/security-architecture.md) | FOUNDATION |
| SEC-005 | Secrets handling | CONSTRAINT | DEC-009 | SYS-31 Security Architecture | [security/security-architecture.md](../security/security-architecture.md) | FOUNDATION |
| CUS-001 | Platform-account architecture | FUTURE | §84 | SYS-32 Platform Account / Custody | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | None (FUTURE) |
| CUS-002 | What it would require | FUTURE | §84 | SYS-32 Platform Account / Custody | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | None (FUTURE) |
| CUS-003 | Not assumed approved | CONSTRAINT | §84 | SYS-32 Platform Account / Custody | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | None (FUTURE) |
| LED-001 | Authoritative internal accounting, if user-facing | CONFIRMED REQUIREMENT | §85 | SYS-33 Trading Ledger | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | CORE TRADING FOUNDATION |
| LED-002 | Potential ledger scope | DEPRECATED / REPLACED | §85 | SYS-33 Trading Ledger | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | CORE TRADING FOUNDATION |
| LED-003 | Trading-engine state is not the ledger | CONSTRAINT | §85 | SYS-33 Trading Ledger | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | CORE TRADING FOUNDATION |
| LED-004 | Internal trading ledger | CONFIRMED REQUIREMENT | DEC-006 | SYS-33 Trading Ledger | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | CORE TRADING FOUNDATION |
| LED-005 | Ledger scope for a single operator | SYSTEM REQUIREMENT | DEC-006 | SYS-33 Trading Ledger | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | CORE TRADING FOUNDATION |
| LED-006 | Ledger authority | CONFIRMED ARCHITECTURAL PRINCIPLE | DEC-006 | SYS-33 Trading Ledger | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | CORE TRADING FOUNDATION |
| LED-007 | Append-only ledger | CONSTRAINT | DEC-006 | SYS-33 Trading Ledger | [systems/custody-and-ledger.md](../systems/custody-and-ledger.md) | CORE TRADING FOUNDATION |
| PERF-001 | Continuous operation | CONFIRMED REQUIREMENT | §75 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| PERF-002 | Performance is first-class | CONFIRMED REQUIREMENT | §76 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| PERF-003 | Latency-sensitive path | CONFIRMED ARCHITECTURAL PRINCIPLE | §77 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| PERF-004 | AI off the latency path | CONSTRAINT | §77 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| PERF-005 | Performance engineering techniques | CONFIRMED ARCHITECTURAL PRINCIPLE | §78 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| PERF-006 | Measured technology choices | CONSTRAINT | §78 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| PERF-007 | Initial design targets | CONFIRMED REQUIREMENT | DEC-017 | Performance (cross-cutting) | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) | OPERATIONALIZATION |
| OPS-001 | Operational readiness is not project completion | CONFIRMED ARCHITECTURAL PRINCIPLE | §80 | Deployment and operational readiness | [operations/deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) | OPERATIONALIZATION |
| OPS-002 | Subsystems can go live independently | CONFIRMED REQUIREMENT | §80 | Deployment and operational readiness | [operations/deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) | OPERATIONALIZATION |
| OPS-003 | Development while online | CONFIRMED REQUIREMENT | §81 | Deployment and operational readiness | [operations/deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) | OPERATIONALIZATION |
| OPS-004 | Separate environments | CONFIRMED REQUIREMENT | DEC-015 | Deployment and operational readiness | [operations/deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) | OPERATIONALIZATION |
| OPS-005 | Traceable, reversible deployments | CONFIRMED REQUIREMENT | DEC-009 | Deployment and operational readiness | [operations/deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) | OPERATIONALIZATION |
