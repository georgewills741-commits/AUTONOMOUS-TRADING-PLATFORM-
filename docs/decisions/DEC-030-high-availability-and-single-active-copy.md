# DEC-030 — High availability, and only one active copy during migration

- **Status:** ACCEPTED
- **Date:** 2026-09-30
- **Decided by:** project owner ([owner decisions 3, Q5 and Q9](../handoffs/owner-decisions-03-part-2-findings.md)); REC-024, MIG-030, and the notes below are the builder's
- **Resolves:** TC-07; approves high availability (REC-021)

## Decision

| Requirement | What it says |
|---|---|
| REC-021 | Reclassified from FUTURE to CONFIRMED REQUIREMENT: high availability is approved and planned. Its failover sequence (check ownership, orders, positions, capital, and exchange state, then reconcile, then activate) is unchanged |
| REC-023 | A standby copy takes over automatically when the active copy fails, but only after it has checked and reconciled state and acquired the execution lease |
| REC-024 | (Builder) The active and standby copies of an account use one execution-lease authority that both can reach, with fencing tokens, so at most one copy can hold the lease |
| MIG-029 | During every move, freeze the old copy, then create new exchange API keys for the new location and delete the old ones, so the exchange itself refuses the old copy (TC-07) |
| MIG-030 | (Builder) The destination does not trade on a venue until the old key for that venue is revoked. Where a venue offers no API for creating and revoking keys, the rotation is an operator step of the migration |

## Notes (builder; the owner may correct them)

- **"Explicit activation" (REC-022).** The owner chose a standby that takes over automatically. Explicit activation is therefore read as acquiring the execution lease under a policy authorization, after state validation and reconciliation. It is not a human action. This is consistent with PLT-013 and PLT-014.
- **Two different mechanisms.** Failover (REC-023) is fast and automatic, so it relies on the shared lease (REC-024), not on key rotation. Migration (MIG-029) is a planned move between hosts with separate databases, so it relies on freezing the source and rotating keys, which the venue enforces.
- **Where the lease lives** (a replicated database or an external coordinator) is an implementation choice made when OPERATIONALIZATION is planned.
- **Stage:** OPERATIONALIZATION, as part of production hardening. Infrastructure as code covers the failover configuration ([DEC-029](DEC-029-infrastructure-as-code.md)).

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **Decide later** (Q5 in [owner decisions 3](../handoffs/owner-decisions-03-part-2-findings.md): leave TC-07 open until the migration feature is planned): not chosen.
- **A lease held outside both hosts** for migration (one of TC-07's candidates): not taken. Key rotation is the only candidate the venue itself enforces (TC-07). A shared lease authority is used for failover instead (REC-024).
- **Key rotation for failover too:** not used. Builder's reading ("Notes" above): failover is fast and automatic, so it relies on the shared lease.
- **Not now** (Q9, the builder's recommendation: one active copy that restarts itself automatically, revisited after the platform goes live): not chosen. The owner chose to plan high availability now.
- **"Explicit activation" (REC-022) as a human action:** not taken. Builder's reading ("Notes" above): because the owner chose a standby that takes over automatically, explicit activation is acquiring the execution lease under a policy authorization.
- **Where the lease lives,** a replicated database or an external coordinator: deferred, as an implementation choice made when OPERATIONALIZATION is planned ("Notes" above).
