# DEC-052 — The owner's answers of 2026-10-20: checkpoints C and D before items 4 and 5; backups during long gate cycles; archive branches

- **Status:** ACCEPTED
- **Date:** 2026-10-20
- **Decided by:** project owner ([owner decisions 20](../handoffs/owner-decisions-20-question-on-the-rules-order-of-work-and-backups.md)); the builder's: the wording that applies the answers to the records, and when a gate cycle counts as long (decision 3)
- **Resolves:** OQ-31 ([DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md), decision 6)

## Context

On 2026-10-20, while the seventh Gate 3 run of the change that commits the reports of earlier Gate 3 runs as evidence ("Next approved step", item 2) was running, the owner asked whether the builder had questions and whether it really follows the rules, recalling the instruction to fix problems at their root and avoid loops: the project has been in Stage 1 since it started, and the owner's weekly usage had reached 69%.

The builder put two questions to the owner: whether checkpoints C and D should come before items 4 and 5, and OQ-31, how work under verification is kept safe during a long gate cycle. The owner chose the first option of each. To the first the owner added that nothing should cause problems and the rules must stay intact and always be used; to the second, that the builder, not the owner, does every step. This environment cannot create tags ([DEC-044](DEC-044-preserve-archive-tag-answers-and-convergence-audit.md), decision 2), so the builder asked whether archive branches may replace archive tags, and the owner said yes.

## Decision

1. **Owner decisions 20 is preserved word for word**, as a HISTORICAL source listed in the preserved-text manifest. The typed message and each answer were taken by script from the session record and are kept as recorded, with the questions and options as asked.
2. **The order of work.** After item 3 of "Next approved step", checkpoints C and D (item 6) come next. Items 4 and 5 follow checkpoint D and come before Stage 1's exit reports (X9 and X10 in the [stage record](../traceability/stage-01-foundation.md)) and its completion certificate.
   - During checkpoint C, U4 and U5 are checked against the configuration and security rules of [owner decisions 14](../handoffs/owner-decisions-14-company-grade-order-and-traceability.md) (its §20 and §21), which item 5 reconciles with the requirements.
   - This changes the order that [DEC-046](DEC-046-preserve-company-grade-order-and-traceability-rules.md) set (decision 6), and nothing else. Every builder text, gate, decision, and rule applies as before, as the owner asked.
3. **Work under a long gate cycle is backed up** (OQ-31: option (b), with the builder doing every step). A gate cycle counts as long once its first Gate 3 run has failed, or when a session would end with the work uncommitted.
   - The builder then pushes the work to a temporary backup branch, `claude/unverified-backup-<change>`, under [owner decisions 10](../handoffs/owner-decisions-10-unverified-backup-and-lifecycle.md)'s lifecycle and the labels of [DEC-042](DEC-042-preserve-anti-drift-rules-and-backup-instructions.md) (decision 4), and pushes it again as the work changes. Nothing on it is merged, built on, or used as evidence for a gate.
   - After the verified commit, the builder reconciles the branch with it by owner decisions 10's eight checks and records the result.
   - It then keeps the branch's last commit under an archive branch, `claude/archive/` followed by the backup's name without `claude/`, and deletes the backup branch while it is still at that commit.
   - Where the environment refuses the deletion, the backup branch stays at the archived commit, and the [project state](../project-state.md) names it.
4. **Archive branches replace archive tags**, for checkpoint B's backup too ([DEC-043](DEC-043-retire-checkpoint-b-backup-under-an-archive-tag.md); DEC-044, decision 2).
   - On 2026-10-20 the builder pushed `claude/archive/unverified-backup-checkpoint-b` at `ee84f26`, and checked it on GitHub.
   - The branch `claude/unverified-backup-checkpoint-b`, still at `ee84f26`, could not be deleted. A git push of the deletion, made only if the branch was still at `ee84f26`, was cut off five times ("the remote end hung up unexpectedly"). One attempt through the GitHub API answered HTTP 403: "Write access to this GitHub API path is not permitted through this proxy."
   - So the branch stays at `ee84f26`, the commit its archive keeps. A session whose access allows it deletes the branch while it is still there. Stage 1's completion certificate lists its state (DEC-044, decision 2).
   - "Next approved step", item 1, is done as far as this environment allows.
5. **Nothing else changes.** No requirement, system rule, gate, or code changes. Nothing here authorizes work beyond [DEC-038](DEC-038-stage-1-plan-approved.md)'s Stage 1.

## Alternatives considered

- **The recorded order:** items 3 to 5, then checkpoints C and D. Not chosen by the owner.
- **Archive tags pushed by the owner.** Not chosen: the owner asked that the builder do every step, and this environment cannot create tags.
- **No archive, the backup branch kept as it is** (OQ-31's option (c)). Not chosen by the owner. It is what remains where a deletion is refused.

## Consequences

- OQ-31 is RESOLVED in the [open-question register](../open-questions/register.md).
- The project state gives the new order of "Next approved step", item 1's state, the branches, and the blockers.
- "Later changes" lines are added to DEC-042, DEC-043, DEC-044, DEC-046, and DEC-047.
- The stage record's "Blockers" row, and its note on the certificate, give the backup's state.
