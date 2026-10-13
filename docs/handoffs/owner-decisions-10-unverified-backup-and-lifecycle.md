# Owner Decisions 10 — The unverified backup of checkpoint B; a temporary backup's lifecycle

> **Status:** HISTORICAL — source input: two messages of the owner, sent during Stage 1 while checkpoint B's third gate was pending. The first (2026-10-12) asks the builder to check whether the existing rules permit an isolated backup of unverified work; if they do, to preserve the work that way, labelled as unverified and not for merge, and if not, to report the conflict; and to continue the verification sequence without bypassing any gate. The second (2026-10-13) sets the lifecycle of such a temporary backup, from its creation to its reconciliation with the verified checkpoint and its retirement or retention under the repository's policy, asking the owner where no policy exists. This is **not** an active source of truth. It is preserved by [DEC-042](../decisions/DEC-042-preserve-anti-drift-rules-and-backup-instructions.md), which records how it is applied; the [project state](../project-state.md) records the backup's status.
>
> **Formatting note:** each message is reproduced inside one text block exactly as received. Nothing was added, removed, or changed in them. The title, this banner, and the two headings are the builder's.

## The owner's message of 2026-10-12

```text
Continue according to the established canonical project rules.

Do NOT bypass DEC-032, DEC-033, Gate 3, Review 8, the three-pass verification process, or any other existing verification requirement merely to commit faster.

However, I also do not want substantial project work to exist only inside an ephemeral container where it could be lost.

First inspect the canonical repository rules and confirm the correct mechanism already established for preserving unverified work without falsely promoting it to a verified checkpoint.

If the existing rules permit an explicitly isolated backup/checkpoint branch for unverified work, then preserve the current work there in the safest repository-consistent way, clearly marking it as:

UNVERIFIED
NOT APPROVED
NOT A VERIFIED CHECKPOINT
NOT PRODUCTION-READY
NOT AUTHORIZED FOR MERGE

This backup must NOT bypass Gate 3, must NOT become the authoritative verified branch, must NOT be merged into the verified/main branch, and must NOT be treated as evidence that the work passed verification.

Do not create a new backup mechanism, branch convention, workflow, authority, or policy if the repository already defines one. Reinforce and follow the existing canonical mechanism.

Then continue the current verification sequence:

1. Allow the mutation test run to finish completely.
2. Record the complete mutation-testing result and evidence.
3. Investigate and correct any failures rather than bypassing them.
4. Run Review 8 / independent Gate 3 exactly as required.
5. Resolve every blocking finding.
6. Rerun any affected tests or verification gates after corrections.
7. Confirm all required three-pass verification requirements are satisfied.
8. Perform the required repository completeness, documentation, traceability, diff, and git-status checks.
9. Confirm there are no unintended files, duplicate implementations, conflicting requirements, architectural drift, unresolved blocking findings, or accidental scope expansion.
10. Only after the canonical commit gate genuinely passes, create the official checkpoint commit.
11. Push the verified checkpoint according to the established repository workflow.

Do not call the current work complete, verified, approved, production-ready, or safe to merge while Review 8 / Gate 3 remains incomplete.

IMPORTANT:

A backup of unverified work protects against data loss.
It does NOT constitute verification.

A commit is a repository checkpoint.
It does NOT by itself prove correctness.

The verified checkpoint must still require the complete canonical verification process.

Also, before creating any separate backup branch, confirm that doing so is compatible with the existing repository rules. If DEC-032/DEC-033 or another canonical rule prohibits even an isolated unverified backup commit, do not violate that rule. Instead report the exact conflict and the safest compliant preservation option for my decision.

Continue autonomously through all actions already authorized by the canonical project rules. Stop and ask me only if a genuine owner-level decision is required.

Maintain the permanent project principles:

NO BYPASSING VERIFICATION.
NO FALSE COMPLETION CLAIMS.
NO UNVERIFIED WORK PROMOTED AS VERIFIED.
NO SILENT ARCHITECTURAL CHANGES.
NO DUPLICATE SYSTEMS OR AUTHORITIES.
NO LOSS OF SUBSTANTIAL PROJECT WORK.
NO NEW PROCESS WHEN A CANONICAL PROCESS ALREADY EXISTS.

Preserve first where canonically permitted.
Verify completely.
Correct failures.
Reverify.
Then create and push the authoritative checkpoint.
```

## The owner's message of 2026-10-13

```text
==================================================
TEMPORARY BACKUP LIFECYCLE — MANDATORY
==================================================

If an isolated UNVERIFIED backup/checkpoint is created to protect work
from container/session loss, it must NEVER be abandoned or forgotten.

The backup has a temporary lifecycle and must remain traceable until it
is formally resolved.

Required lifecycle:

ACTIVE DEVELOPMENT
→ TEMPORARY UNVERIFIED BACKUP, IF NEEDED AND PERMITTED
→ CONTINUE VERIFICATION
→ COMPLETE TESTING
→ COMPLETE REVIEW / GATE 3
→ FIX BLOCKING FINDINGS
→ RETEST
→ REVERIFY
→ CREATE OFFICIAL VERIFIED CHECKPOINT
→ CONFIRM VERIFIED CHECKPOINT CONTAINS ALL INTENDED VALID WORK
→ PUSH VERIFIED CHECKPOINT
→ RECONCILE TEMPORARY BACKUP
→ RETIRE / DELETE TEMPORARY BACKUP WHEN SAFE
→ VERIFY REPOSITORY CLEANLINESS
→ RECORD FINAL STATE

The temporary backup must have an explicit status such as:

TEMPORARY
UNVERIFIED
PENDING VERIFICATION
NOT FOR MERGE
NOT PRODUCTION-READY

It must also be traceable to:

- the development session/work;
- the corresponding verification process;
- the eventual verified checkpoint or resolution.

IMPORTANT:

Do NOT forget the backup after verification succeeds.

Do NOT allow abandoned backup branches to accumulate.

Do NOT leave two competing versions of the same work.

Do NOT delete the backup before confirming that every intended valid
change is safely contained in the verified authoritative checkpoint.

Do NOT merge an unverified backup merely because it exists.

Before retiring the backup, compare it against the final verified
checkpoint and confirm that:

1. Every intended valid change is preserved.
2. Corrections made during verification are preserved.
3. No required work exists only on the temporary backup.
4. No unverified or rejected implementation is accidentally promoted.
5. The authoritative branch contains the correct final state.
6. Required documentation and traceability are updated.
7. The official verified checkpoint has been successfully pushed.
8. Repository status is clean and consistent.

Only after these checks may the temporary backup be retired according
to the repository's canonical branch-retention rules.

If repository policy requires retaining the backup for audit/history,
retain it according to that policy instead of deleting it.

If repository policy requires deletion after successful reconciliation,
delete it only after the reconciliation checks pass.

DO NOT INVENT A NEW RETENTION POLICY.

Follow the existing canonical repository policy.

If no canonical retention policy exists and a decision is materially
required, report that gap and ask me rather than silently choosing one.

==================================================
FAILURE CASE
==================================================

If Gate 3, Review 8, mutation testing, or another required verification
fails:

DO NOT discard the backup.

Preserve the work safely.

Correct the findings in the proper development state.

Rerun affected verification.

Keep the backup traceable until the work reaches one of these explicit
terminal states:

VERIFIED AND INCORPORATED
REJECTED AND RETIRED
SUPERSEDED AND RETIRED
PRESERVED FOR AUDIT ACCORDING TO POLICY

There must be NO forgotten state.

==================================================
SESSION INTERRUPTION
==================================================

If the Claude session, container, machine, or development environment
is interrupted before verification completes, the next authorized
development session must inspect the repository and recover the
temporary checkpoint before continuing.

Never blindly restart the same implementation and create duplicate work.

Repository state must be inspected first.

==================================================
FINAL RULE
==================================================

A temporary backup is a SAFETY MECHANISM, not a permanent parallel
development history.

CREATE IT ONLY WHEN PERMITTED AND NECESSARY.
TRACK IT.
VERIFY THE REAL WORK.
RECONCILE IT.
CONFIRM NOTHING IS LOST.
THEN RETIRE OR RETAIN IT ACCORDING TO CANONICAL POLICY.

NO FORGOTTEN BACKUPS.
NO ABANDONED BRANCHES.
NO DUPLICATE IMPLEMENTATIONS.
NO LOST VALID WORK.
NO UNVERIFIED PROMOTION.
NO PREMATURE DELETION.
```
