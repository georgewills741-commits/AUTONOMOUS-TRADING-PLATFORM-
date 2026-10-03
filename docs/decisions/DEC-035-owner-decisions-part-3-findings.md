# DEC-035 — Owner decisions on the Part 3 findings; Part 3 reconciliation approved

- **Status:** ACCEPTED
- **Date:** 2026-10-02
- **Decided by:** project owner ([owner decisions 4](../handoffs/owner-decisions-04-part-3-findings.md), eight multiple-choice answers); the wording of RSK-049 and GOV-024, taken from the options the owner chose, and the reading notes are the builder's
- **Later changes:** TC-08's work is done: DEC-001 to DEC-030 all have an "Alternatives considered" section since 2026-10-02 ([TC-08 verification](../traceability/tc-08-alternatives-verification.md)). The complete documentation review is done and accepted, and Stage 1 planning is authorized ([DEC-036](DEC-036-owner-decisions-audit-findings.md), 2026-10-03). The text below is kept as written.

## Context

The Part 3 reconciliation ([DEC-031](DEC-031-part-3-reconciliation.md)) left items for the owner: confirm CF-17 and CF-18, answer OQ-27, accept or change TC-08's recommendation, check the DUP-34 and DUP-35 readings, and review the reconciliation (P3§541 items 29–30). The master execution constitution's adoption ([DEC-033](DEC-033-adopt-master-execution-constitution.md)) added CF-19. The owner answered all of them on 2026-10-02.

## Decisions

| Item | Owner's decision | Applied |
|---|---|---|
| CF-17 rule precedence | Security ranks above the user's hard policy, below the safety floor | RSK-049 added in the [Risk Engine](../risk/risk-engine.md). RSK-048, which put security below the user's hard constraints, is DEPRECATED / REPLACED (class only; wording kept). SR-02 now rests on RSK-049 |
| CF-18 capital growth | The builder's resolution confirmed | No requirement change: growth raises limits or authorized capital only where policy already authorizes that scaling and readiness has validated it; anything else is a POL-005 change |
| CF-19 feature lifecycle | The master execution constitution's lifecycle (§107), with Part 3's names mapped onto it | GOV-024 added in [Architecture governance](../architecture/architecture-governance.md). GOV-018 (Part 3's proposed statuses) is DEPRECATED / REPLACED (class only; wording kept) |
| OQ-27 Part 4 | No Part 4 is coming; Parts 1 to 3 are complete | OQ-27 answered. The complete documentation review treats Parts 1 to 3, the owner's decisions, and the builder texts as the complete knowledge base |
| TC-08 older records' alternatives | Add them now, wherever the repository shows what was considered; records with no sourced alternatives say so | The builder's next checkpoint amends DEC-001 to DEC-030. Nothing is reconstructed from memory (constitution Rule 181) |
| DUP-34 Rebalancing Engine | Confirmed: a component of the Global Capital Authority, not a separate system | Unchanged (CAP-037 to CAP-042); marked confirmed |
| DUP-35 emergency state names | Confirmed: mapped onto the adopted safety levels | Unchanged (RSK-015 and the mapping in the Risk Engine); marked confirmed |
| Part 3 human review | Approved | DEC-031 is confirmed by the owner; P3§541 items 29–30 are done |

## Reading notes (builder)

| Item | Reading |
|---|---|
| CF-17, "security" | The security layer of P3§471: the security controls outside the safety floor, for example the transfer-authority restrictions (SEC-006, SEC-007) and AI least privilege (SEC-008). Security rules inside the floor were already on top (RSK-010) |
| CF-17, "a formal, audited security change" | The owner's words. Who proposes and approves such a change, and how, is specified with the security and policy design; this record adds nothing to it |
| CF-17 and RSK-004 | RSK-004's layers keep their order. RSK-049 places security between system safety and the user's hard constraints |
| CF-19, where statuses are kept | Decided when Stage 1 is planned. Until then no separate feature registry is created (DUP-32, GOV-014) |
| CF-19 and GOV-009 | The option shown did not cover GOV-009's deprecation statuses. Reading kept as the builder's in Architecture governance ("Status vocabularies"): SUNSET_PENDING and REPLACED refine DEPRECATED and RETIRED; fixed when Stage 1 is planned |
| CF-19 and strategies | Strategies keep their own lifecycle (STR-001, STR-024). The two lifecycles share the names APPROVED, CANARY, PRODUCTION, and RETIRED, which must keep one meaning (TC-10) |

## Alternatives considered

The options the owner did not choose, quoted in full in [owner decisions 4](../handoffs/owner-decisions-04-part-3-findings.md):

- CF-17: keep Part 3's order (security below the user's hard constraints).
- CF-18: always ask the owner before any limit rises; or fully automatic scaling whenever readiness validates.
- CF-19: Part 3's statuses as canonical; or decide at Stage 1.
- OQ-27: a Part 4 is coming; or not sure yet.
- TC-08: add alternatives only when a record is next amended; or leave older records as they are.
- DUP-34: register the Rebalancing Engine as its own system.
- DUP-35: replace the safety levels with Part 3's names.
- Part 3 review: not yet.

## Consequences

- Requirements: RSK-049 and GOV-024 added; RSK-048 and GOV-018 reclassified DEPRECATED / REPLACED, their wording kept. The comparison with the previous checkpoint shows exactly these two changes (`tools/docs/compare_requirements.py 3b6f372 --strict --expect-changed=GOV-018:cls,RSK-048:cls`).
- Findings: every conflict (CF) is resolved; OQ-27 is answered; TC-08 is decided, with its work next; TC-09 and TC-10 stay open by design until their stages are planned.
- Next: the TC-08 work, then the complete documentation review (handoff §101; P2§329), then the Stage 1 plan for the owner's approval. Implementation still needs the owner's explicit approval, such as "Begin Stage 1" (constitution Rules 134–135).
