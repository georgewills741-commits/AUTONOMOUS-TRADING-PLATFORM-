# DEC-064 — Keep the retired backup branches until the owner removes them, and keep temporary backup commits out of the machine checks (owner decisions 31)

- **Status:** ACCEPTED
- **Date:** 2026-11-09
- **Decided by:** the owner, on the retired branches ([owner decisions 31](../handoffs/owner-decisions-31-retired-branches-and-failure-emails.md), Q1). On the emails, the builder chose, as the owner asked in the same answers (Q2).

## Context

- **The retired branches.** Twelve temporary backup branches are RETIRED — DELETION BLOCKED — SAFE TO DELETE WHEN PERMITTED, each at the commit its archive branch keeps (the [project state](../project-state.md)'s "Branches").
  - This session's access to GitHub refuses their deletion with HTTP 403 ([DEC-054](DEC-054-configuration-size-limit-and-retired-backup-branches.md), decision 4). The API's answer says that write access to that path is not permitted through the session's proxy. The builder knows of no permission it can request that changes this.
  - Carrying them past Stage 1 needs the owner's explicit, recorded approval ([DEC-044](DEC-044-preserve-archive-tag-answers-and-convergence-audit.md), decision 2).
- **The emails.** The machine checks, the workflow of U6, run on every push and pull request, as the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md)'s decision D4 says ([DEC-038](DEC-038-stage-1-plan-approved.md)). So every push of a temporary backup starts a run.
  - A backup is evidence for no gate ([DEC-052](DEC-052-apply-owner-answers-on-order-of-work-and-backups.md), decision 3).
  - A backup is pushed as soon as an edit exists ([DEC-057](DEC-057-progress-continuity-no-loss-and-recovery.md), decision 4), so it can hold a record whose index entries are not yet in place. Such a snapshot fails the documentation checker. On `claude/unverified-backup-x6`, 7 of its 27 runs failed, each within about 12 seconds, and GitHub emails the owner about each failed run.
  - The run the owner showed, on `d1c6727` at 14:04 UTC, failed because DEC-063 was not yet in the decision log, owner decisions 30 not yet in the manifest, and neither linked from the indexes. The next backup, 18 seconds later, passed, and so did the copy given to Gate 3 (`cc5e6a8`).
- **The owner's message and answers.** On 2026-11-09 at 14:18 UTC the owner invited the builder to request the permission to delete what is not needed, and mentioned these emails. The builder asked two questions at 14:21 UTC, and the owner answered at 14:27 UTC (owner decisions 31):
  - On the branches: keep them for now; the owner will remove them later, and asked whether that could cause a problem.
  - On the emails: the builder is to choose what suits the company-grade level discussed and will not cause problems in the future.
- **The builder's answer** at 14:29 UTC, on the branches: no problem. They are not used, merged, or built on; each is at the same commit as its archive branch; they get no pushes, so no runs; the only cost is their place in the branch list.

## Decision

1. **The twelve retired branches are kept until the owner removes them.**
   - This is the owner's explicit, recorded approval to carry them past Stage 1 (DEC-044, decision 2).
   - They stay RETIRED — DELETION BLOCKED — SAFE TO DELETE WHEN PERMITTED, and no deletion is tried from this environment (DEC-054, decision 4).
   - When the owner deletes them, the next session records each as RETIRED — PHYSICALLY DELETED, after checking on GitHub that its archive branch is still at the branch's last commit. The archive branches are kept (DEC-052, decision 3).
   - A branch retired later the same way is kept likewise and named to the owner, so that the owner can remove it with the others.
2. **The choice on the emails: temporary backup commits are kept out of the machine checks.**
   - **Now:** from 2026-11-09, 14:29 UTC, each backup commit carries GitHub's `[skip ci]` marker in its message, so GitHub starts no run for it and sends no email about it. The first such backup was pushed at 14:36 UTC.
   - **No verification is lost.** A backup is evidence for no gate (DEC-052, decision 3), and the builder runs the checks before each Gate 3 copy and each commit. Every commit on the designated branch and every pull request still run every check.
   - **Later, as its own change through the three gates, after Stage 1's exit (X8):** the workflow skips pushes to `claude/unverified-backup-*` and `claude/archive/*` branches itself. The rule then does not depend on a marker in a message, and it holds for the code work of later stages, where a snapshot taken in the middle of work fails more often.
   - **Not now:** the workflow is part of the stage that its completion certificate certifies at `6d58014`.
   - **D4's "every push"** reads from now on: every push except a temporary backup commit's. The [developer guide](../development.md) says so.
3. **Nothing else changes now.** No requirement, rule, gate, or code changes with this record. The workflow's change comes as described in decision 2.

## Alternatives considered

- **Try the deletion again now.** Not chosen: nothing shows that this environment's access has changed (DEC-054, decision 4), and the owner chose to keep the branches.
- **Keep the checks on every backup push, and push only snapshots that pass.** Not chosen: a backup is pushed as soon as an edit exists (DEC-057, decision 4), before the related edits are all in place. In later stages, a snapshot of code in progress fails its tests too, so the failures and their emails would go on.
- **The owner turns off GitHub's emails about failed runs.** Not chosen: it would also hide the failures that matter, those of the designated branch.
- **Change the workflow now.** Not chosen: it would change, before the stage's exit, the stage that its completion certificate certifies.
- **Rely on the marker alone, for good.** Not chosen: a rule kept only in each commit's message depends on every session remembering it. The workflow's own rule does not.

## Consequences

- Owner decisions 31 is listed in the preserved-text manifest and the documentation index.
- The project state's "Branches" and the stage record's completion certificate record the owner's approval to keep the retired branches.
- The developer guide states the exception for temporary backup commits.
- The project state's "Next approved step" names the workflow's change, after the owner's approval to plan Stage 2 (X8).
- Nothing here authorizes work beyond [DEC-038](DEC-038-stage-1-plan-approved.md)'s Stage 1.
