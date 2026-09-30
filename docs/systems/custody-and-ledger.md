# Platform Account, Custody and Ledger

> **Status:** custody is **FUTURE**, not built: the owner chose a single-operator platform ([DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md)). The **internal trading ledger is CONFIRMED** (LED-004 to LED-007).
>
> **Systems:** SYS-32 Platform Account / Custody (FUTURE), SYS-33 Trading Ledger · **Roadmap stage:** ledger in CORE TRADING FOUNDATION; custody none ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) · **Sources:** §84, §85

## Platform account / custody

- **CUS-001** Platform-account architecture · FUTURE · §84 — A previously discussed architecture involved: user → platform account → authorized capital → controlled trading infrastructure → supported venues / wallets → execution. This remains classified as previously discussed architecture that requires formal confirmation before becoming a final production requirement.
- **CUS-002** What it would require · FUTURE · §84 — If retained, it requires: custody; wallet management; deposit monitoring; blockchain monitoring; double-entry ledger; internal balances; reconciliation; withdrawal controls; security; key management; compliance architecture; exchange-account management.
- **CUS-003** Not assumed approved · CONSTRAINT · §84 — Claude must not silently assume this model is approved.

## Ledger / accounting

- **LED-001** Authoritative internal accounting, if user-facing · CONFIRMED REQUIREMENT · §85 — If the platform becomes a user-facing capital platform, internal accounting must be authoritative.
- **LED-002** Potential ledger scope · DEPRECATED / REPLACED · §85 — Potential requirements: deposits; withdrawals; trading; fees; realized P&L; internal transfers; capital allocation; reservations; user balances; venue balances.
- **LED-003** Trading-engine state is not the ledger · CONSTRAINT · §85 — Temporary trading-engine state must not become the authoritative financial ledger.

LED-001 is conditional in the handoff's own wording: it applies only if the platform becomes a user-facing capital platform, which it currently does not ([DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md)). LED-002 was the §85 "potential requirements" list, written for a user-facing platform; it is replaced by LED-005.

## Decisions applied (2026-09-30)

CUS-001 and CUS-002 are reclassified FUTURE (owner decision). LED-002 is replaced by LED-005.

- **LED-004** Internal trading ledger · CONFIRMED REQUIREMENT · DEC-006 — The platform keeps an internal double-entry trading ledger, even though it is not user-facing. It is the authoritative record of realized financial history.
- **LED-005** Ledger scope for a single operator · SYSTEM REQUIREMENT · DEC-006 — The ledger records: trades; fees; funding payments; borrow interest; realized P&L; transfers between venues; operator deposits and withdrawals made directly at venues (detected through reconciliation); venue balances.
- **LED-006** Ledger authority · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-006 — Realized P&L, fees, and balances shown by Portfolio Management and used by the Global Capital Authority are derived from the ledger. Neither keeps an independent copy.
- **LED-007** Append-only ledger · CONSTRAINT · DEC-006 — Ledger entries are append-only. Corrections are made with reversing entries, never by editing or deleting.

## Findings (all resolved)

OQ-01 → [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md) (owner: single operator; custody FUTURE). OQ-02 → [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md) (LED-004 to LED-007). DUP-17 → [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md) (LED-006). DUP-16 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (REC-008).
