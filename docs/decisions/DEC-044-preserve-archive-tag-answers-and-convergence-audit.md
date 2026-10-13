# DEC-044 — Preserve the owner's answers on the archive tag and the Foundation convergence audit; the audit comes first

- **Status:** ACCEPTED
- **Date:** 2026-10-13
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and the owner's checkpoint rule ([DEC-032](DEC-032-adopt-checkpoint-and-verification-rule.md): "EVERYTHING MUST BE PRESERVED IN THE REPOSITORY"); the answers, the choice to continue, and the directive are the owner's

## Context

Two exchanges with the owner on 2026-10-13, after checkpoint B's commit (`4816059`) and the record of its backup's reconciliation (`813fa90`):

- **The archive tag** ([owner decisions 12](../handoffs/owner-decisions-12-archive-tag-refused.md)). [DEC-043](DEC-043-retire-checkpoint-b-backup-under-an-archive-tag.md) keeps the backup's last commit, `ee84f26`, under the tag `archive/unverified-backup-checkpoint-b` before its branch is deleted. As observed on 2026-10-13, this environment's access to GitHub refused to create the tag: a `git push` of the tag failed with HTTP 403 six times, and the GitHub REST API answered HTTP 403, "Write access to this GitHub API path is not permitted through this proxy.", for `POST /repos/{owner}/{repo}/git/tags` and for `POST /repos/{owner}/{repo}/git/refs`. Asked how to finish, the owner first asked for a careful retry, which was refused the same way; then asked whether the problem was permission and, told that it is a permission rule of this cloud session's access to GitHub, said they would wait for the limit to be lifted; told that it does not reset on a timer, the owner chose to continue the next approved steps while the branch waits.
- **The convergence audit** ([owner decisions 13](../handoffs/owner-decisions-13-foundation-verification-convergence-audit.md)). The owner then ordered a mandatory audit, before the gate cycle continues, of whether Stage 1 (FOUNDATION) verification converges: its baseline, the history of every gate and finding, the authority behind each blocker and behind the mutation check, whether completion criteria moved, and objective, finite exit criteria. It authorizes no bypass, new feature, scope expansion, or lowering of quality, and asks that existing mechanisms be reused rather than duplicated (its §0, §1).

## Decision

1. **Both are preserved word for word now**, as owner decisions 12 and 13, HISTORICAL sources listed in the preserved-text manifest, for the reason [DEC-042](DEC-042-preserve-anti-drift-rules-and-backup-instructions.md) gives: no owner decision or instruction exists only in the session (master execution constitution §01, §90).
2. **The backup branch is kept as it is until the tag exists on GitHub.** DEC-043's order is unchanged: the tag, then the branch's deletion. The step is recorded as a blocker in the [project state](../project-state.md). A session tries to create the tag again only when the owner says this environment's access to GitHub has changed, or when the session has other access to GitHub: one attempt, and if it is refused, the refusal is recorded and the branch left. The owner may also push the tag. A session that finds the tag on GitHub (a local tag does not count) whose commit is `ee84f26` deletes the branch only while it is still at `ee84f26`, then records the final state; a tag on another commit stops the step. Stage 1's completion certificate lists this step's state; carrying it past Stage 1 needs the owner's explicit, recorded approval (master execution constitution §20).
3. **The convergence audit comes first.** It is made before any further gate cycle: before the adoption of [owner decisions 9](../handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md), the audit of [owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md), and checkpoint C. The owner's "Continue the next steps" is applied in that order. Finishing the backup's retirement, once the tag is on GitHub, does not wait for the audit. The audit is recorded in `docs/traceability/`, in its own change and through the existing three gates (its §30). As its §0 and §1 ask, it reuses the canonical homes: the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md) for the baseline and the completion criteria, the [stage record](../traceability/stage-01-foundation.md) for the exit checklist and the completion certificate, and the checkpoints' verification records for the history.
4. **Whether owner decisions 13's lasting rules join a builder text** that `CLAUDE.md` loads is decided with the audit's result, together with owner decisions 9's adoption: the audit first finds which of its rules the existing builder texts already state.

## Alternatives considered

- **Keep the owner's answers as quotations in the checkpoint B verification record only.** Rejected: owner answers are kept word for word under `docs/handoffs/`, with the questions as asked and the options shown ([DEC-037](DEC-037-final-decision-and-integrity-checkpoint.md); owner decisions 11). The record's Gate 3 review raised it.
- **Start the audit before committing this preservation and the record of the blocker.** Rejected: the audit takes hours, and meanwhile the owner's messages and the backup's state would exist only in the session (master execution constitution §01, §90; owner decisions 13, §35).
- **Adopt owner decisions 13 as a builder text now.** Not chosen: its §0 and §1 ask first to reuse existing mechanisms, and the audit is what finds which of its rules are already covered.
- **Delete the backup branch without the tag.** Rejected: the owner chose "Tag, then delete" over "Delete it" (owner decisions 11), so that the commits the records name stay reachable.

## Consequences

- The [project state](../project-state.md) records the blocker, the next steps with the audit first, and DEC-001 to DEC-044.
- DEC-043 gets a "Later changes" line pointing here.
- No requirement changes. Nothing here authorizes implementation beyond DEC-038's Stage 1.
