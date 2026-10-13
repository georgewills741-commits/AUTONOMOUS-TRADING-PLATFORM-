# Owner Decisions 11 — Retiring checkpoint B's temporary backup

> **Status:** HISTORICAL — source input: the owner's answer of 2026-10-13 to OQ-30, which [DEC-042](../decisions/DEC-042-preserve-anti-drift-rules-and-backup-instructions.md) put to the owner: what happens to the temporary backup branch of checkpoint B's work once it has been reconciled with the verified checkpoint, since the repository has no branch-retention policy. This is **not** an active source of truth. The answer is applied through [DEC-043](../decisions/DEC-043-retire-checkpoint-b-backup-under-an-archive-tag.md).
>
> **Formatting note:** the owner's request that preceded the question is reproduced first, inside a text block exactly as written. The question was then asked as one multiple choice; it is recorded with the short label shown above it, the question as asked, the options shown (label, then description), and the option the owner chose. The owner added no written note. Nothing was added, removed, or changed in what was written, shown, or answered; the headings and the bold field names are the builder's.

## The owner's request

```text
full the question for me
```

## Round 1

### Q1 — the backup branch after its reconciliation

**Label shown:** OQ-30

**Question as asked:** OQ-30: Once checkpoint B's verified commit is pushed and the temporary backup branch `claude/unverified-backup-checkpoint-b` passes your eight reconciliation checks, what should happen to that branch? The repository has no branch-retention policy, so this is your call; until you decide, the branch stays as it is.

**Options shown:**

- Tag, then delete (Recommended) — Keep its last commit under an archive tag (archive/unverified-backup-checkpoint-b), then delete the branch. No leftover branch, and the backup stays retrievable for audit, so the commit hashes in the records keep pointing to something.
- Delete it — Delete the branch once the checks pass and are recorded. The records keep its commit hashes, but those commits become unreachable and may eventually be removed from GitHub, so the hashes would then point to nothing.
- Keep the branch — Leave the branch as it is, labelled TEMPORARY and NOT FOR MERGE. Nothing is lost, but a parallel branch stays around, which your backup lifecycle rules discourage.

**Owner's answer:** Tag, then delete (Recommended)
