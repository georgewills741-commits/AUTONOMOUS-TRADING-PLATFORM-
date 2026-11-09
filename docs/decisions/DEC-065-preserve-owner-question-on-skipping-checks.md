# DEC-065 — Preserve the owner's question of 2026-11-09, 15:00 UTC, on whether keeping temporary backup commits out of the machine checks could cause problems (owner decisions 32)

- **Status:** ACCEPTED
- **Date:** 2026-11-09
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept). The message is the owner's.

## Context

On 2026-11-09 at 15:00 UTC, while the second Gate 3 run of the change that writes Stage 1's completion certificate was under way, the owner quoted the builder's summary of its choice on the emails of failed machine checks ([DEC-064](DEC-064-retired-branches-kept-and-backup-commits-skip-checks.md), decision 2) and wrote that the owner hopes it will not create problems in the future. It is a user turn of its own in the session record, of origin human, not one of the client's own entries, so it is the owner's message.

The builder answered at 15:01 UTC:

- **No.** The `[skip ci]` marker only tells GitHub not to run the checks for one backup snapshot. The snapshot is still pushed at once, so the backup that prevents loss works as before.
- **No checking is lost.** Every commit on the working branch runs every check on GitHub, and the marker is only in backup snapshots, never in a real commit. Backups are never evidence: before any commit, the builder runs every check, and an independent reviewer runs them again in a fresh copy. The checks on snapshots produced only false alarms.
- **What would have to go wrong, and its guard:**
  - The marker reaching a real commit. Real commits are written fresh, never copied from a backup, so this cannot happen by accident; the builder confirms on GitHub that the checks run on every real commit, starting with the certificate's.
  - A session forgetting the marker. The only effect would be the emails again, until the workflow's own rule after Stage 1's exit, whose verification shows on GitHub that a real commit runs every check and a backup push does not.
- **Where it is written:** DEC-064 and the [developer guide](../development.md).

The builder also said that the message, which came after the copy that the second run reviews, would be preserved with the next change. That run failed, and a third run follows on a new copy, made after the message.

Gate 3's third run (19:45 UTC) found one point of that answer wrong ([Stage 1 certificate verification](../traceability/stage-01-certificate-verification.md), W-23): checking was lost. The machine checks' run of the repository test for secrets on each push was the threat model's monitoring of SEC-005, and since 14:36 UTC no backup had it. The builder corrected its answer to the owner after that run, in its messages from 19:53 UTC, and [DEC-064](DEC-064-retired-branches-kept-and-backup-commits-skip-checks.md) (decision 2) now keeps that test on each backup snapshot, before its push; the 20 backups pushed with the marker were scanned, with no finding.

## Decision

1. **The message is preserved word for word**, as [owner decisions 32](../handoffs/owner-decisions-32-question-on-skipping-checks-for-backup-commits.md), a HISTORICAL source listed in the preserved-text manifest. It was taken by script from its user turn of 15:00 UTC in the session record and kept byte for byte, including the two spaces after "problem" and the space that ends its first line, so `git diff --check` reports that line; the text is not trimmed to satisfy it. It was pushed to this change's temporary backup at 15:05 UTC ([DEC-057](DEC-057-progress-continuity-no-loss-and-recovery.md), decision 4).
2. **It changes nothing by itself.** It asks whether the choice could cause problems, which the builder answered. DEC-064 stands, its decision 2 corrected on the point of the answer that Gate 3's third run found wrong (above).
3. **It is preserved with this change, whose record names it**, and not with the next one as the builder first said. A record names the owner's messages received up to the copy that its last Gate 3 run reviews ([traceability README](../traceability/README.md), Scope), and this change's last run reviews a copy made after the message.

## Alternatives considered

- **Treat it as procedural.** Not chosen: it asks a question, which DEC-047 (decision 7) keeps, as the owner's questions of the same kind were kept ([DEC-063](DEC-063-preserve-owner-question-of-2026-11-09.md), and earlier).
- **Preserve it with the next change, as first said.** Not chosen: the Scope rule ties a message to the record whose last Gate 3 run reviews a copy made after it, and that record is this change's.
- **Trim its spaces, so that `git diff --check` stays clean.** Not chosen: a text kept in a text block equals the message as received, byte for byte (the [documentation tools](../../tools/docs/README.md)' rule for preserved texts).

## Consequences

- Owner decisions 32 is listed in the preserved-text manifest and the documentation index.
- This change's record names the message.
- No requirement, rule, gate, or code changes. Nothing here authorizes work beyond [DEC-038](DEC-038-stage-1-plan-approved.md)'s Stage 1.
