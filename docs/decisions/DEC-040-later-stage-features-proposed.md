# DEC-040 — A stage's features are PROPOSED until the owner approves its plan

- **Status:** ACCEPTED
- **Date:** 2026-10-07
- **Decided by:** project owner ([owner decisions 7](../handoffs/owner-decisions-07-later-stage-feature-state.md), answering OQ-29); the builder's: the wording that applies it to the roadmap, architecture governance, and the records
- **Resolves:** OQ-29 (the [quality audit](../traceability/quality-audit-2026-10-06.md)'s Q-07)

## Context

GOV-024 is the canonical feature lifecycle (IDEA → PROPOSED → APPROVED → DESIGNED → …), and decision D5 of the Stage 1 plan ([DEC-038](DEC-038-stage-1-plan-approved.md)) records each major feature's state in one table, the roadmap's feature-status table. From Stage 1's checkpoint A that table showed APPROVED for every feature of stages 2 to 7: the builder's reading of the owner's acceptance of the documentation review ([DEC-036](DEC-036-owner-decisions-audit-findings.md)). The quality audit of 2026-10-06 found that no owner decision states that state and that the texts can be read both ways, and put the question to the owner with both readings, their consequences, and the builder's recommendation (APPROVED). On 2026-10-07 the owner chose "PROPOSED until each plan".

## Decision

The owner chose option B of the question as the [quality audit](../traceability/quality-audit-2026-10-06.md) states it (Q-07: option B, the sentence "In every option …", and B's consequences), to which the message shown with the question pointed; the option's short description is in owner decisions 7.

1. **A stage's features are PROPOSED** in GOV-024's terms until the owner approves that stage's plan. With that approval they become APPROVED, and DESIGNED as the plan designs them, as Stage 1's items became DESIGNED with its approved plan (DEC-038). This applies now to the features of stages 2 to 7.
2. **It sets a feature state only.** The requirements of those stages keep their classes and stay accepted as reviewed (DEC-036); the decisions the builder made under the owner's delegations stay in effect and may be overridden by a new decision record; nothing beyond Stage 1 is authorized (DEC-038).
3. **Two words kept apart.** PROPOSED here is the GOV-024 feature state, not the requirement class PROPOSED (ARCH-015). Staged features are kept apart from items in no stage: those have no row in the table, belong to no stage's scope, and their class is their status (ARCH-029).

## Applied

| Where | Change |
|---|---|
| [Roadmap](../roadmap/roadmap.md), feature-status table | The rows for stages 2 to 7 show PROPOSED; the table's introduction states decision 1; the sentence on items in no stage reworded (decision 3) |
| [Architecture governance](../architecture/architecture-governance.md), "Status vocabularies" | Decision 1, beside D5 and D6 |
| [Glossary](../glossary.md) | PROPOSED as a feature state and as a requirement class: DISTINCT |
| [Stage record](../traceability/stage-01-foundation.md) | Its row on the later stages' state records the owner's decision, which replaces the earlier reading |
| [Open-question register](../open-questions/register.md) | OQ-29 ANSWERED |
| The [project state](../project-state.md), the [documentation index](../README.md), the [decision log](README.md) | Updated |

## Reading notes (builder)

| Phrase | Reading |
|---|---|
| "when you approve that stage's plan" | The owner's explicit approval of the plan, as DEC-038 approved Stage 1's. The authorization to implement remains its own statement (constitution Rules 134 to 136), though the owner may give both together, as on 2026-10-05 |
| D6 | PROPOSED is not ACTIVE, so the features of stages 2 to 7 are not ACTIVE in GOV-009's terms until their stage's plan is approved |

## Alternatives considered

- **APPROVED now**, the builder's recommendation: every staged item approved scope at once, designed and authorized stage by stage. Not chosen by the owner.
- **Another state named by the owner.** Not chosen.

## Consequences

- No requirement changes; GOV-024 itself is unchanged.
- Stage 1's rows are unchanged.
- When the owner approves the next stage's plan, that stage's rows move to APPROVED, and to DESIGNED as its plan designs them.
