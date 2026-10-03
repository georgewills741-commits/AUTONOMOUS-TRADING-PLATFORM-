# Portfolio Management

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-08 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION · **Sources:** §24

Canonical definition of the platform's single portfolio view.

## Requirements

- **PRT-001** One centralized portfolio view · CONFIRMED ARCHITECTURAL PRINCIPLE · §24 — The platform requires one centralized portfolio view.
- **PRT-002** Tracked state · SYSTEM REQUIREMENT · §24 — It should track: positions; balances; exposure; unrealized P&L; realized P&L; allocated capital; reserved capital; available capital; pending orders; strategy exposure; exchange exposure; asset exposure; risk exposure.
- **PRT-003** No competing portfolio truths · CONSTRAINT · §24 — Trading systems consume portfolio state; they do not create competing portfolio truths.

## Decisions applied (2026-09-30)

- **PRT-004** Capital and realized P&L are read-only here · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — Allocated, reserved, and available capital shown in the portfolio are read from the Global Capital Authority; realized P&L is read from the ledger. The portfolio owns only the positions and exposure views.
- **PRT-005** Derivatives and margin exposure · SYSTEM REQUIREMENT · DEC-007 — The portfolio also tracks leverage, notional exposure, margin, liquidation prices, and funding and borrow accruals for derivatives and margin positions.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **PRT-006** P&L attribution · SYSTEM REQUIREMENT · P2§99 — P&L should be attributable where possible to: strategy; venue; market; asset; trade; opportunity; arbitrage route.

P2§43 (one Portfolio Authority) is PRT-001 to PRT-003. Realized P&L comes from the ledger (PRT-004, LED-006), so attributing it requires ledger entries that carry the strategy, opportunity, and route identifiers.

## Boundary (§92)

- **Owns:** the centralized portfolio view (PRT-001).
- **Updated from:** execution results and reconciliation. In the canonical flow, portfolio state is the final layer after reconciliation (ARCH-008).
- **Used by:** trading systems, the Risk Engine (exposure and portfolio limits), the Trading Director (portfolio state, existing positions), and monitoring.
- **Not yet specified in Part 1:** interfaces, update ordering, failure behavior, tests.

## Findings

**Open:** OQ-28: whether the instrument scope (PLT-011, [DEC-007](../decisions/DEC-007-instrument-scope.md)) includes derivatives beyond perpetual futures and margin ([open-question register](../open-questions/register.md); raised by the [master knowledge-base audit](../traceability/master-knowledge-base-audit-2026-10-02.md)). The requirements here stand as written until the owner answers. PRT-005 tracks leverage, margin, liquidation, and funding.

Resolved:

DUP-02 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (PRT-004). DUP-17 → [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md) (the ledger is authoritative for realized P&L, LED-006).
