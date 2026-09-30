# Platform Account, Custody and Ledger

> **Status: PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION.** Nothing in this document is an approved production requirement except where marked. Do not design or build against it until OQ-01 is resolved.
>
> **Systems:** SYS-32 Platform Account / Custody (requires confirmation), SYS-33 Ledger / Accounting (conditional) · **Roadmap stage:** not mapped by §95 · **Sources:** §84, §85

## Platform account / custody

- **CUS-001** Platform-account architecture · PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION · §84 — A previously discussed architecture involved: user → platform account → authorized capital → controlled trading infrastructure → supported venues / wallets → execution. This remains classified as previously discussed architecture that requires formal confirmation before becoming a final production requirement.
- **CUS-002** What it would require · PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION · §84 — If retained, it requires: custody; wallet management; deposit monitoring; blockchain monitoring; double-entry ledger; internal balances; reconciliation; withdrawal controls; security; key management; compliance architecture; exchange-account management.
- **CUS-003** Not assumed approved · CONSTRAINT · §84 — Claude must not silently assume this model is approved.

## Ledger / accounting

- **LED-001** Authoritative internal accounting, if user-facing · CONFIRMED REQUIREMENT · §85 — If the platform becomes a user-facing capital platform, internal accounting must be authoritative.
- **LED-002** Potential ledger scope · PROPOSED · §85 — Potential requirements: deposits; withdrawals; trading; fees; realized P&L; internal transfers; capital allocation; reservations; user balances; venue balances.
- **LED-003** Trading-engine state is not the ledger · CONSTRAINT · §85 — Temporary trading-engine state must not become the authoritative financial ledger.

LED-001 is conditional in the handoff's own wording: it applies only if the platform becomes a user-facing capital platform. That condition is unresolved (OQ-01). LED-002 is classified PROPOSED because §85 calls those items "potential requirements".

## Findings

- OQ-01: confirm or reject the platform-account / custody model, and state whether the platform serves one operator or many users.
- OQ-02: the compounding flow (CAP-012) passes through "accounting / ledger" even though LED-001 is conditional. Is a ledger needed in either case?
- DUP-17: realized P&L would be recorded here and in Portfolio Management (PRT-002).
- DUP-16: custody reconciliation (CUS-002) would sit alongside [Recovery and Reconciliation](recovery-and-reconciliation.md).
