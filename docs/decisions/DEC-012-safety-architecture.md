# DEC-012 — Safety architecture: kill switches, health state machine, system safety rules

- **Status:** ACCEPTED (delegated: builder decision under the owner's instruction to resolve all open items; the owner may override)
- **Later changes:** CAP-022, SEC-003, HLT-007, HLT-008, HLT-009, and REC-009 are superseded by [DEC-019](DEC-019-company-grade-autonomous-operating-model.md). RSK-009 (kill-switch reset) is under owner review as CF-11.
- **Date:** 2026-09-30
- **Resolves:** DUP-04, OQ-06, OQ-07, OQ-20

## Context

Part 1 puts kill switches, emergency shutdown, and safe mode in four places (§25, §27, §47, §74). It defers to a "global safety architecture" it never defines, lists health states without transitions, and places "system safety" at the top of the risk hierarchy without saying what it contains.

## Decision

**Global safety architecture = Risk Engine + System Health** (RSK-008, HLT-010).
- The **Risk Engine** owns trading authorization and every kill switch: global, per venue, per instrument type, per strategy, and the arbitrage kill switch. The arbitrage switch is a Risk Engine rule set using the ARB-010 triggers.
- **System Health** owns the platform state. The Risk Engine reads that state before authorizing any trade.

**Kill switches (RSK-009):**
- They may be activated automatically by deterministic rules (including Performance Controller rules, PFC-008) or by the operator.
- Only the operator can reset one, and only after reconciliation succeeds and health permits trading.
- AI cannot activate or reset a kill switch; it may only recommend activation.

**Health state machine (HLT-007 to HLT-009):**
- Overall states: STARTING, RECOVERING, HEALTHY, DEGRADED, SAFE MODE, TRADING HALTED, EMERGENCY, STOPPED.
- EXCHANGE DEGRADED (per venue), DATA DEGRADED, and AI DEGRADED are component conditions that make the overall state DEGRADED.
- WARNING is an alert severity, not a trading state.

| State | Trading |
|---|---|
| HEALTHY | Allowed |
| DEGRADED | Only strategies not depending on a degraded component |
| SAFE MODE | No new positions; reduce and close only |
| TRADING HALTED | No orders except those the operator approves |
| EMERGENCY | Cancel all open orders; no new orders; operator alerted; positions closed automatically only if policy explicitly enables it |
| STARTING, RECOVERING, STOPPED | None |

- Any state can move automatically to SAFE MODE, TRADING HALTED, or EMERGENCY.
- Leaving those three requires the operator and the safe-resume checks (REC-004).
- STARTING → RECOVERING → HEALTHY happens only after reconciliation succeeds.
- Automatic resume after a restart happens only if the operator has enabled it, and only when the platform was HEALTHY before the interruption and reconciliation found no mismatches (REC-009).

**System safety rules (RSK-010):** the top layer of the risk hierarchy. Each rule comes from Part 1:
1. No order unless system health permits trading (§72, §74).
2. No order without Risk Engine authorization and a capital reservation (§19, §25).
3. No real order outside an authorized live mode (§31).
4. Active kill switches are always respected (§25, §47).
5. No trading on a venue or asset with unresolved reconciliation mismatches (§71).
6. No trading on stale market data (§10, §40).
7. Orders must satisfy exchange precision and rules (§39, §79).
8. Trading credentials must not allow withdrawals (§89).

**Rebalancing and withdrawal permission:**
- Trading API keys never carry withdrawal permission (SEC-003).
- Rebalancing transfers (§45) are therefore proposed by the platform and executed after operator confirmation by default (CAP-022).
- Automated transfers can be enabled only by an important policy change. They use a separate key restricted to the venue's withdrawal-address whitelist, containing only the operator's own venue accounts.

## Consequences

"Global safety architecture" in §47 now has a definition. The health state machine is formal enough for Part 2 contracts, satisfying HLT-002's intent.
