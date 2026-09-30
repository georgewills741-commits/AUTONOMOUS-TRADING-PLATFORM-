# DEC-006 — Single-operator platform, no custody, internal trading ledger

- **Status:** ACCEPTED
- **Date:** 2026-09-30
- **Decided by:** project owner (operator and custody model, OQ-01); builder under the owner's instruction to resolve all open items (ledger scope, OQ-02, DUP-17). The owner may override the delegated parts.
- **Resolves:** OQ-01, OQ-02, DUP-17
- **Affects:** [platform overview](../product/platform-overview.md), [custody and ledger](../systems/custody-and-ledger.md), [Global Capital Authority](../systems/capital-management.md), [portfolio](../systems/portfolio-management.md), [security](../security/security-architecture.md)

## Context

§84 describes a previously discussed platform-account / custody model and forbids assuming it is approved. §85 makes an authoritative ledger conditional on a user-facing platform. However, the §22 compounding flow passes every realized result through "accounting / ledger" regardless.

## Decision

1. **Owner decision:** the platform trades for **one operator**, using the operator's own accounts at supported venues through API keys. There is no custody, no deposit or withdrawal handling for others, and no multi-user accounts.
2. The §84 custody model (CUS-001, CUS-002) is reclassified from PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION to **FUTURE**. It is recorded, not built. LED-001 stays as written; its condition (user-facing) does not currently hold.
3. **Delegated:** the platform nevertheless keeps an **internal double-entry trading ledger**, because compounding (CAP-012), realized P&L, fees, funding, and transfers need one authoritative financial history. LED-003 already forbids trading-engine state from serving as that record.
4. **Authority layering (DUP-17):**
   - The ledger is authoritative for realized financial history and balances.
   - The Global Capital Authority derives available capital from ledger-confirmed balances, minus reservations and commitments.
   - The portfolio shows realized P&L read from the ledger.
5. LED-002 (the §85 "potential requirements" list, which assumed multiple users) is marked DEPRECATED / REPLACED by LED-005, the single-operator scope.

## Alternatives considered

- **Multi-user with or without custody:** rejected by the owner.
- **No ledger, with realized P&L held by the portfolio:** rejected. It leaves compounding and reconciliation without an authoritative financial record, contrary to LED-003 and CAP-012.

## Consequences

New requirements PLT-010, LED-004 to LED-007, and CAP-019 were added. Security scope drops user accounts (SEC-001 "user accounts" now means the operator's own access). The ledger joins CORE TRADING FOUNDATION ([DEC-016](DEC-016-roadmap-stage-placement.md)).
