# Portfolio Management

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-08 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION · **Sources:** §24

Canonical definition of the platform's single portfolio view.

## Requirements

- **PRT-001** One centralized portfolio view · CONFIRMED ARCHITECTURAL PRINCIPLE · §24 — The platform requires one centralized portfolio view.
- **PRT-002** Tracked state · SYSTEM REQUIREMENT · §24 — It should track: positions; balances; exposure; unrealized P&L; realized P&L; allocated capital; reserved capital; available capital; pending orders; strategy exposure; exchange exposure; asset exposure; risk exposure.
- **PRT-003** No competing portfolio truths · CONSTRAINT · §24 — Trading systems consume portfolio state; they do not create competing portfolio truths.

## Boundary (§92)

- **Owns:** the centralized portfolio view (PRT-001).
- **Updated from:** execution results and reconciliation. In the canonical flow, portfolio state is the final layer after reconciliation (ARCH-008).
- **Used by:** trading systems, the Risk Engine (exposure and portfolio limits), the Trading Director (portfolio state, existing positions), and monitoring.
- **Not yet specified in Part 1:** interfaces, update ordering, failure behavior, tests.

## Findings

- DUP-02: allocated, reserved, and available capital are tracked here and are also the authoritative state of the [Global Capital Authority](capital-management.md) (CAP-001, CAP-002). There must not be two capital truths.
- DUP-17: realized P&L is tracked here and would also be recorded by the ledger (LED-002), if a ledger is confirmed.
