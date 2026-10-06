# DEC-038 — Stage 1 plan approved; Stage 1 implementation authorized

- **Status:** ACCEPTED
- **Date:** 2026-10-05
- **Decided by:** project owner ([owner decisions 6](../handoffs/owner-decisions-06-stage-1-plan.md), two multiple-choice answers); the reading notes are the builder's
- **Approves:** the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md), with its decisions D1 to D11 as recommended
- **Authorizes:** implementation of Stage 1 (FOUNDATION) only

## Context

The owner authorized Stage 1 planning on 2026-10-03 ([DEC-036](DEC-036-owner-decisions-audit-findings.md)). The builder wrote the plan; it passed the three gates on 2026-10-05, with Gate 3 passing on its fourth run ([Stage 1 plan verification](../traceability/stage-01-plan-verification.md)). The final decision checkpoint of 2026-10-05 ([record](../traceability/final-decision-checkpoint-2026-10-05.md)) found two matters requiring the owner: the plan's eleven decisions, and the authorization to implement (constitution Rules 134–135). The owner answered both on 2026-10-05.

## Decisions

| Item | Owner's decision | Applied |
|---|---|---|
| D1 to D11 | Approved, all as recommended | The plan's status is APPROVED; each D-item is in force as the plan states it |
| D5: where each feature's GOV-024 state is recorded | One feature-status table in the master roadmap, kept current at every checkpoint | The table is created at checkpoint A, when Stage 1 starts, and kept current at every checkpoint, also after a feature's stage closes (D5); [Architecture governance](../architecture/architecture-governance.md) and the [system registry](../architecture/system-registry.md) point to it |
| D6: GOV-009's statuses next to GOV-024 | ACTIVE: from APPROVED to PRODUCTION; SUNSET_PENDING: DEPRECATED with a planned removal date; REPLACED: DEPRECATED or RETIRED, naming its replacement | Architecture governance's "Status vocabularies" note; this part of TC-10 is decided (the [open-question register](../open-questions/register.md) and the [glossary](../glossary.md) say so); TC-10 stays open for the other shared names |
| D11: dependencies Stage 1 adds | Approved: Pydantic v2; pytest, Hypothesis, ruff, mypy; the build backend `uv_build`; the GitHub actions `actions/checkout` and `astral-sh/setup-uv` for the machine checks | This record is the decision record the [technology stack](../architecture/technology-stack.md) requires for a dependency it does not list; the technology stack names the two additions (the build backend and the actions) |
| Stage 1 implementation | Authorized ("Begin Stage 1") | Implementation of Stage 1 may start: the stage record is created and checkpoint A begins after this decision's checkpoint is committed |

## Reading notes (builder)

| Item | Reading |
|---|---|
| Scope of the authorization | Stage 1 only (RMP-002). It does not authorize any later stage, approve any later architecture change (constitution Rule 136), or authorize trading, credentials, or deployment, none of which Stage 1 contains |
| D1 to D11 in force | The plan is the canonical statement of each D-item. Where a D-item names a document to be written (D2), that document is written during the stage and becomes the canonical home of its topic |
| The workflow push | The plan's risk that pushing a workflow file may need a credential with workflow permission stays as written: if the push is refused, it is recorded as a blocker for the owner, and the workflow is not dropped silently |
| The build backend's pin | The approved plan said "one exact version" in U1 and "version range" in D11. The stricter applies: one exact version (constitution Rule 102); D11's wording is aligned with U1 |
| Licenses | The licenses of the dependencies D11 adds are checked when they are added, at checkpoint A, and recorded in the stage record (DEC-009's consequences; constitution Rule 99) |

## Alternatives considered

The options the owner did not choose, quoted in full in [owner decisions 6](../handoffs/owner-decisions-06-stage-1-plan.md):

- D1 to D11: not yet (read the plan first), or changes to named D-items. Each D-item's own alternative is listed in the plan's section 10.
- Stage 1 implementation: approve the plan but start later; or not yet.

## Consequences

- No requirement changes (`tools/docs/compare_requirements.py 47f5348 --strict` shows no change). D5 and D6 settle where statuses are kept and how two status vocabularies relate; neither changes a requirement's text or class.
- Stage 1 moves from planning to implementation. The next action is checkpoint A of the plan: create the stage record, then U1 (development environment) and U6 (testing foundation and machine checks), through the three gates.
- Implementation of any later stage still needs its own plan and the owner's explicit approval.
