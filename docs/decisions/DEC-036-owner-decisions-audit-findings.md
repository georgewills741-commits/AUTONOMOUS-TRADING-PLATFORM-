# DEC-036 — Owner decisions on the audit findings; documentation review accepted; Stage 1 planning authorized

- **Status:** ACCEPTED
- **Date:** 2026-10-03
- **Decided by:** project owner ([owner decisions 5](../handoffs/owner-decisions-05-audit-findings.md), seven multiple-choice answers); the wording of MIG-033 and of the changed PLT-010, MKD-007, and MON-009, taken from the options the owner chose, and the reading notes are the builder's
- **Later changes:** The CF-21 question quoted DEC-006's decision text ("no deposit or withdrawal handling for others") as the owner's original decision; the option the owner actually chose on 2026-09-30 read "No custody, deposits, withdrawals, or user accounts" (owner decisions 1). The CF-21 decision stands on the owner's own later instructions and the owner's explicit choice of PLT-010's wording; see [DEC-037](DEC-037-final-decision-and-integrity-checkpoint.md) and finding F-02 of the [final decision checkpoint](../traceability/final-decision-checkpoint-2026-10-05.md). On 2026-10-05 the owner approved the Stage 1 plan and authorized Stage 1 implementation ([DEC-038](DEC-038-stage-1-plan-approved.md)). The text below is kept as written.
- **Resolves:** CF-20, CF-21, DUP-40, OQ-28 (raised by the [master knowledge-base audit](../traceability/master-knowledge-base-audit-2026-10-02.md)); the audit's acceptance (its finding A-19); the optional confirmation of the feature process; the authorization of Stage 1 planning

## Context

The master knowledge-base audit, the complete documentation review that handoff §101 and P2§329 require before implementation, gave verdict B (ready with non-blocking findings) and left seven items for the owner: two decisions (CF-20, OQ-28), two that could be decided or delegated (CF-21, DUP-40), an optional confirmation (whether GOV-002 with GOV-022 is the feature process meant), the acceptance of the review, and the authorization of Stage 1 planning. The owner answered all seven on 2026-10-03.

## Decisions

| Item | Owner's decision | Applied |
|---|---|---|
| CF-20 hosting | Production never depends on any one machine, the owner's computer included: an active host plus a standby (DEC-030), rebuilt without the owner (OPS-017). The owner's computer may be a production host only if it meets the same readiness bar as a server | MIG-033 added in [Hosting and migration](../operations/hosting-and-migration.md). MIG-001 and MIG-002 are unchanged: local hosting stays supported |
| OQ-28 instrument scope | Spot, perpetual futures, and margin; no other derivatives | No requirement change: PLT-011 confirmed as it stands. Every type stays gated by its risk controls (PLT-012) |
| CF-21 PLT-010's wording | Match DEC-006: "no deposit or withdrawal handling for others", pointing to SEC-006 | PLT-010 reworded in the [platform overview](../product/platform-overview.md). Its old text: "The platform trades for one operator, using the operator's own accounts at supported venues through API keys. It does not take custody of funds and has no deposit, withdrawal, or multi-user account functions." |
| DUP-40 retention values | The values live only in TEC-012; MKD-007 and MON-009 point to it instead of repeating the numbers | MKD-007 reworded in [Market Data](../systems/market-data.md) and MON-009 in [Monitoring and observability](../operations/monitoring-and-observability.md); the [values register](../requirements/values-register.md)'s V-18 and V-19 now name TEC-012 as the place of the value. Old texts: MKD-007 "Market data is kept in TimescaleDB for 30 days and permanently in compressed Parquet archives (OHLCV, trades, order-book snapshots) for backtesting (TEC-006, TEC-012)."; MON-009 "Structured operational logs are kept here and rotated after 90 days. They are separate from the audit trail (AUD-006)." |
| Feature process | GOV-002 with GOV-022 is the process meant; the owner's 19-step sequence stays mapped onto it | No requirement change; the note in [Architecture governance](../architecture/architecture-governance.md) now says the owner confirmed it |
| Documentation review | Accepted | The complete documentation review (handoff §101; P2§329) is done and accepted. The [registry](../requirements/registry.md)'s Approval column for the 512 handoff requirements now reads "reviewed (DEC-036)" instead of "pending documentation review" |
| Stage 1 planning | Authorized | The builder writes the Stage 1 (FOUNDATION) plan, with the fields of constitution Rule 140, for the owner's approval. No platform code is written until the owner separately says "Begin Stage 1" (constitution Rules 134–135) |

## Reading notes (builder)

| Item | Reading |
|---|---|
| CF-20, "the same readiness bar as a server" | The production-readiness criteria of the readiness model (RDY-022) and the production hardening checklist (RMP-010), applied to every production host alike. MIG-033 states this; it adds no new criterion |
| CF-20 and the builder's machine | The register recorded a third reading, in which "the user's laptop" meant the machine the builder works on. The chosen option covers it: no production copy depends on any one machine, and the platform does not depend on Claude Code (PLT-029) |
| DUP-40, MKD-007's class | The register's proposed resolution also moved MKD-007 to TEC-012's class. The option shown to the owner did not mention a class change, so MKD-007 keeps its class (SYSTEM REQUIREMENT): what remains in it is behavior (market data is stored and archived for backtesting), not values. MON-009 keeps its class, as proposed |
| DUP-40, "permanently" | TEC-012 also says how long the archive is kept (permanently). MKD-007 now points to TEC-012 for every storage tier and retention period, so no retention value is stated twice |
| DUP-40, MKD-007's scope | MKD-007 keeps its scope: all market data is stored, and OHLCV, trades, and order-book snapshots are what the archive holds for backtesting, as in its old text. Only the storage technologies and retention values moved to TEC-012 |
| CF-21 | SEC-006 and SEC-007 are unchanged. The new PLT-010 names them; it adds no permission: rebalancing transfers remain limited to the operator's own approved accounts with separate credentials, and the platform holds no general withdrawal or custody authority |
| Review accepted | Acceptance closes the documentation review. It does not authorize implementation; it does not approve the Stage 1 plan, which is still to be written |

## Alternatives considered

The options the owner did not choose, quoted in full in [owner decisions 5](../handoffs/owner-decisions-05-audit-findings.md):

- CF-20: production never on the owner's computer (servers or cloud only; the owner's computer for development, research, and paper trading).
- OQ-28: add dated futures; or add dated futures and options.
- CF-21: delegate the wording to the builder; or no transfers at all (PLT-010 literal, dropping the rebalancing transfers of DEC-019).
- DUP-40: delegate to the builder; or keep the values in both places.
- Feature process: add the owner's 19 steps as a separate requirement.
- Documentation review: ask for changes first.
- Stage 1 planning: not yet.

## Consequences

- Requirements: MIG-033 added; PLT-010, MKD-007, and MON-009 reworded, each keeping its title, class, and source. The comparison with the previous checkpoint shows exactly these changes (`tools/docs/compare_requirements.py 16df57f --strict --expect-changed=MKD-007:text,MON-009:text,PLT-010:text`).
- Findings: CF-20, CF-21, DUP-40, and OQ-28 are resolved. No conflict, duplicate, or open question is open except TC-09 and TC-10, which stay open by design until OPERATIONALIZATION and CORE TRADING FOUNDATION are planned.
- Tooling: the registry generator's Approval text for handoff requirements changes from "pending documentation review" to "reviewed (DEC-036)".
- Next: the Stage 1 plan for the owner's approval. Implementation still needs the owner's explicit "Begin Stage 1".
