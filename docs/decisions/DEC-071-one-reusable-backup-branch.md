# DEC-071 — One reusable temporary backup branch for sequential changes, under the owner's twelve conditions (owner decisions 38)

- **Status:** ACCEPTED
- **Date:** 2026-11-16
- **Decided by:** the project owner (the approval and its twelve conditions, [owner decisions 38](../handoffs/owner-decisions-38-one-reusable-backup-branch.md)); the builder's: how the conditions are met.

## Context

Until 2026-11-16 each change backed up its uncommitted work on a temporary branch of its own ([DEC-052](DEC-052-apply-owner-answers-on-order-of-work-and-backups.md), decision 3; [DEC-057](DEC-057-progress-continuity-no-loss-and-recovery.md), decision 4). After the change's commit, owner decisions 10's eight checks reconciled the branch with it; its last commit was kept under an archive branch; its deletion was tried once, and this environment refused it; and owner decisions 22's ten checks retired it ([DEC-054](DEC-054-configuration-size-limit-and-retired-backup-branches.md), decision 4; [DEC-067](DEC-067-stage-1-exit-and-owner-answers-of-2026-11-10.md), decision 5). By then fifteen retired branches and fifteen archive branches were on GitHub, and each change's record carried an archive, a deletion attempt, ten checks, and a report A to L. On 2026-11-16 the builder proposed one reusable branch instead, at 19:10 UTC, and asked the owner at 19:15 UTC. At 19:21 UTC the owner approved it, and the same minute set twelve mandatory conditions.

## Decision

1. **The messages are preserved word for word**, as owner decisions 38, a HISTORICAL source listed in the preserved-text manifest, taken by script from the session record, with the question and its options as [owner decisions 34](../handoffs/owner-decisions-34-approval-to-plan-stage-2-and-answers-on-the-directive.md) keeps its own.
2. **From this change on, sequential changes back up on one branch**, `claude/unverified-backup-reusable`. Its name falls under the workflow's pattern for temporary backup branches, so its pushes run only the repository test for secrets ([DEC-064](DEC-064-retired-branches-kept-and-backup-commits-skip-checks.md), decision 2). Its first commit, `97f3c29`, has as its parent the last commit of the workflow change's backup, `ba4158c`, so that the whole history of that branch is reachable from it.
3. **It is append-only.** Each backup commit is a child of the branch's tip, pushed as a fast-forward and never forced; nothing on the branch is reset, deleted, or made unreachable; each commit keeps its SHA, the labels of [DEC-042](DEC-042-preserve-anti-drift-rules-and-backup-instructions.md) (decision 4), and the emergency checkpoint record of master execution constitution §132; and the repository test for secrets runs on each snapshot before its push.
4. **Before the branch is reused**, owner decisions 10's eight checks reconcile the previous change's backup commits with its verified commit, and the record of the change that reuses it names the last backup commit they checked. The three gates are unchanged.
5. **No archive branch, deletion attempt, ten checks, or report A to L for each change.** The fifteen retired branches and their archive branches are kept under their rules (DEC-064; DEC-067, decision 5). So is the workflow change's branch, `claude/unverified-backup-workflow`, the last branch of a single change: the eight checks reconcile it with `62f9eb1`, and it is kept as it is, without an archive branch, since its commits are reachable from the reusable branch, and with no deletion attempt.
6. **Overlapping work keeps its own branch.** A change that must back up while another change's backup is not yet reconciled uses a branch of its own, under the lifecycle of a single change.
7. **Recovery was verified before the branch was relied on.** On 2026-11-16, at 19:46 UTC, a fresh clone of the repository from GitHub restored the reusable branch's tip in a worktree. Its tree equals the working tree's snapshot, file by file: 312 files, apart from the test library's cache, which git ignores. `ba4158c` is in its history. After a long pause, a session finds the branch on the remote and in the [project state](../project-state.md)'s "Branches" (`CLAUDE.md`'s "Where to start"). Had the test failed, the lifecycle of a single change would have stayed.

## Alternatives considered

- **Keep a branch for each change.** Not chosen: the owner approved the reusable branch.
- **Name it `claude/unverified-backup`.** Not chosen: the workflow's pattern is `claude/unverified-backup-*`, so its pushes would run every check.
- **Start it from `62f9eb1`.** Not chosen: the workflow change's backup history would not be reachable from it.

## Consequences

- DEC-042, DEC-052, and DEC-057 gain a line under "Later changes"; the owner rule sets reconciliation's account of owner decisions 10 names this decision; the project state's "Other branches" and "Branches" describe the reusable branch.
- No requirement, platform rule, gate, or code changes.
