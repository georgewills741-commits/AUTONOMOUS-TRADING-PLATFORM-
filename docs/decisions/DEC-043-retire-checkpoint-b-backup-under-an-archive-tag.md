# DEC-043 — Retire checkpoint B's temporary backup under an archive tag

- **Status:** ACCEPTED
- **Later changes:** On 2026-10-13 the reconciliation with checkpoint B's commit found that the labels decision 2 names, "(TEMPORARY, UNVERIFIED, NOT FOR MERGE)", are in the messages of nine of the backup's eleven commits. The first two, `ab78d52` and `540fe4a`, made before the owner's lifecycle message, say UNVERIFIED, NOT APPROVED, NOT A VERIFIED CHECKPOINT, NOT PRODUCTION-READY, and NOT AUTHORIZED FOR MERGE. All eleven say UNVERIFIED, NOT APPROVED, NOT A VERIFIED CHECKPOINT, and NOT PRODUCTION-READY ([checkpoint B verification](../traceability/stage-01-checkpoint-b-verification.md#reconciliation-of-the-temporary-backup)). Also on 2026-10-13, this environment's access to GitHub refused to create the tag (HTTP 403), so the branch is kept until the tag exists on GitHub ([DEC-044](DEC-044-preserve-archive-tag-answers-and-convergence-audit.md), decision 2). On 2026-10-20 the owner chose an archive branch instead of the tag ([DEC-052](DEC-052-apply-owner-answers-on-order-of-work-and-backups.md), decision 4): the backup's last commit is kept under `claude/archive/unverified-backup-checkpoint-b`, and its branch, whose deletion this environment refuses, stays at that commit. The text below is kept as written.
- **Date:** 2026-10-13
- **Decided by:** project owner ([owner decisions 11](../handoffs/owner-decisions-11-retiring-the-checkpoint-b-backup.md), answering OQ-30); the builder's: the wording that applies it to the records
- **Resolves:** OQ-30 ([DEC-042](DEC-042-preserve-anti-drift-rules-and-backup-instructions.md), decision 6)

## Context

DEC-042 made the branch `claude/unverified-backup-checkpoint-b` the temporary backup of checkpoint B's work while its gates ran, under the owner's instructions ([owner decisions 10](../handoffs/owner-decisions-10-unverified-backup-and-lifecycle.md)): after checkpoint B's commit is pushed, the builder compares the backup with it by owner decisions 10's eight checks and records the result. The repository has no branch-retention policy, and owner decisions 10 asks that none be invented, so what then happens to the branch was put to the owner as OQ-30. On 2026-10-13, while checkpoint B's third gate was still running, the owner chose "Tag, then delete". The answer is preserved now, in checkpoint B's commit, for the reason DEC-042 gives for the owner's other messages: no owner decision exists only in the session (master execution constitution §01, §90).

## Decision

1. **Once the eight checks pass and their result is recorded,** the builder keeps the backup's last commit under the tag `archive/unverified-backup-checkpoint-b`, pushes the tag, and then deletes the branch `claude/unverified-backup-checkpoint-b` from the remote. The commits the records name stay reachable through the tag, for audit and diagnosis (constitution Rule 165), and no branch is left over.
2. **The tag is an archive, not a checkpoint.** It keeps unverified work: it is never merged, built on, or presented as verified, and its commits say so themselves (TEMPORARY, UNVERIFIED, NOT FOR MERGE). Checkpoint B's own commit is the verified state.
3. **If a check fails,** nothing is tagged or deleted: the backup stays as it is, and traceable, until the difference is resolved, as owner decisions 10 requires, and the failure is recorded.
4. **It decides this backup only.** Whether owner decisions 10's lifecycle, with this way of retiring a backup, joins a builder text that `CLAUDE.md` loads is decided with owner decisions 9's adoption (DEC-042, decision 7).

## Applied

| Where | Change |
|---|---|
| [Open-question register](../open-questions/register.md) | OQ-30 ANSWERED |
| [DEC-042](DEC-042-preserve-anti-drift-rules-and-backup-instructions.md) | Decision 6 points here |
| [Checkpoint B verification](../traceability/stage-01-checkpoint-b-verification.md), "Identity" | How the backup ends |
| The [project state](../project-state.md) ("Decisions pending", "Other branches", "Next approved step", item 1), the [documentation index](../README.md), the [decision log](README.md), the preserved-text manifest | Updated |

## Alternatives considered

- **Delete the branch** once the checks pass: no branch is left, but its commits become unreachable and may be removed from the remote, so the hashes in the records would point to nothing. Not chosen by the owner.
- **Keep the branch:** nothing is lost, but a parallel branch stays, which owner decisions 10's lifecycle discourages. Not chosen by the owner.
