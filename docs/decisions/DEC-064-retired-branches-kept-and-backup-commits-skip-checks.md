# DEC-064 — Keep the retired backup branches until the owner removes them, and keep temporary backup commits out of the machine checks, but not out of the secret test (owner decisions 31)

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
   - They stay RETIRED — DELETION BLOCKED — SAFE TO DELETE WHEN PERMITTED, and no deletion is tried from this environment unless the owner asks for one (DEC-054, decision 4).
   - When the owner deletes them, the next session records each as RETIRED — PHYSICALLY DELETED, after checking on GitHub that its archive branch is still at the branch's last commit. The archive branches are kept (DEC-052, decision 3).
   - A branch retired later the same way is kept likewise and named to the owner, so that the owner can remove it with the others. Carrying it past Stage 1 needs the owner's explicit, recorded approval, as theirs did (DEC-044, decision 2).
2. **The choice on the emails: temporary backup commits are kept out of the machine checks, but not out of the secret test.**
   - **Now:** from 2026-11-09, 14:29 UTC, each backup commit carries GitHub's `[skip ci]` marker in its message, so GitHub starts no run for it and sends no email about it. The first such backup was pushed at 14:36 UTC.
   - **The gates lose nothing; the secret test is kept, before the push.** A backup is evidence for no gate (DEC-052, decision 3), and the builder runs the checks before each Gate 3 copy and each commit; every commit on the designated branch and every pull request still run every check. But the machine checks' run of the repository test for secrets, their last step, on each push whose earlier steps pass, was also the [threat model](../security/threat-model.md)'s monitoring of SEC-005: with the marker, a secret in a backup snapshot would not have been caught on GitHub, and a backup's branch cannot be deleted from this environment (DEC-054, decision 4). A backup whose run failed at an earlier step had no such check either: on GitHub, 29 runs of backup commits failed at the documentation checker, 7 of this branch's 27 and 22 on the retired backup branches, and their step "Tests" was skipped. This decision first said that no verification is lost; Gate 3's third and fourth runs of the certificate's change found the gaps ([Stage 1 certificate verification](../traceability/stage-01-certificate-verification.md), W-23 and W-32). So, from the first backup after the third run reported (19:45 UTC), the builder runs the repository test for secrets on each backup snapshot before its push, and a finding stops the push: a secret the test recognizes does not reach GitHub through a backup, whereas the machine checks found one only after its push. And every commit on GitHub, 206 on its 27 branches, with 181 distinct trees, was scanned on 2026-11-09 at 20:43 UTC, every file of each, with that test's own scanner: no finding; the 20 backups pushed with the marker, from 14:36 to 19:28 UTC, and the 29 whose runs failed before the test are among them.
   - **Later, as its own change through the three gates, after Stage 1's exit (X8):** the workflow itself runs the repository test for secrets on every push and every pull request, whether or not its other checks pass, and its other checks on every pull request and on every push but one to a `claude/unverified-backup-*` or `claude/archive/*` branch, and backup commits then carry no marker. The rule then does not depend on a marker in a message; the machine checks monitor SEC-005 on every push, whatever the other checks find, while the builder's test before each backup push goes on; and the rule holds for the code work of later stages, where a snapshot taken in the middle of work fails the other checks more often. The same change brings the workflow's header comment and the verification matrix's generated sentence, each of which says that the checks run on every push, into line.
   - **Not now:** the workflow is part of the stage that its completion certificate certifies at `6d58014`.
   - **The Stage 1 plan's "every push"**, in its scope, U6's content, D4, and the rows that name the machine checks, which the verification matrix repeats, reads from now on: every push except a temporary backup commit's, whose snapshot the builder checks with the secret test before its push. The [developer guide](../development.md) and the [threat model](../security/threat-model.md) say so.
3. **Nothing else changes now.** No requirement, rule, gate, or code changes with this record. The workflow's change comes as described in decision 2.

## Alternatives considered

- **Try the deletion again now.** Not chosen: nothing shows that this environment's access has changed (DEC-054, decision 4), and the owner chose to keep the branches.
- **Keep the checks on every backup push, and push only snapshots that pass.** Not chosen: a backup is pushed as soon as an edit exists (DEC-057, decision 4), before the related edits are all in place. In later stages, a snapshot of code in progress fails its tests too, so the failures and their emails would go on.
- **The owner turns off GitHub's emails about failed runs.** Not chosen: it would also hide the failures that matter, those of the designated branch.
- **Change the workflow now.** Not chosen: it would change, before the stage's exit, the stage that its completion certificate certifies.
- **Rely on the marker alone, for good.** Not chosen: a rule kept only in each commit's message depends on every session remembering it. The workflow's own rule does not.
- **The marker with no check for secrets on backups.** This decision's first form, from 14:29 UTC, not kept: a secret in a backup snapshot would reach GitHub unchecked, on a branch that cannot be deleted from this environment (W-23).
- **The workflow skipping the backup and archive branches altogether, later.** This decision's first plan, not kept: the monitoring of SEC-005 would then rest on the builder alone. A failed run of the secret test alone is a finding the owner should hear of, so its email is wanted.

## Consequences

- Owner decisions 31 is listed in the preserved-text manifest and the documentation index.
- The project state's "Branches" and the stage record's completion certificate record the owner's approval to keep the retired branches.
- The developer guide and the [threat model](../security/threat-model.md) state the exception for temporary backup commits and the secret test before each backup push, and so does the stage record's "Security status".
- The project state's "Next approved step" names the workflow's change, after the owner's approval to plan Stage 2 (X8).
- Nothing here authorizes work beyond [DEC-038](DEC-038-stage-1-plan-approved.md)'s Stage 1.
