# DEC-066 — Preserve the owner's question of 2026-11-09, 20:12 UTC, on what is going on, hoping that no problem draws the work back (owner decisions 33)

- **Status:** ACCEPTED
- **Date:** 2026-11-10
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept). The message is the owner's.

## Context

On 2026-11-09, while the fourth Gate 3 run of the change that writes Stage 1's completion certificate was under way, the owner asked what is going on, hoping that everything is in order and that there is no problem, and wrote that the owner does not want problems that might draw the work back. The client queued the message at 20:10:43 UTC and delivered it at 20:12:30 UTC as a user turn of its own, of origin human, not one of the client's own entries, so it is the owner's message.

The builder answered at 20:13 UTC:

- **In order:** the change was in what the builder called its final independent review, run 4, started at 20:10 UTC.
- **Safe:** nothing is lost, the work being backed up on GitHub and identical to the working tree; no code changes, the 749 requirements are unchanged, and checks 1 to 6 pass; the reviews catch mistakes before a commit, and the blocking findings fell from six to four to two; the one real issue, the secret test on backups, is fixed, now run before each backup push, and a scan of the 20 affected backups found nothing.
- **Honestly:** run 4 might still find small wording issues, fixed and reviewed again before the commit.
- **Next:** the commit, its push, and the machine checks; then the owner's approval to plan Stage 2, with the questions on owner decisions 29.
- **The message:** kept word for word, with this change or the next, depending on whether another run follows.

Run 4 then failed, with three blocking findings ([Stage 1 certificate verification](../traceability/stage-01-certificate-verification.md), W-31 to W-33). One of them, W-32, completes the correction on the secret test: no backup had it either whose run failed at an earlier step, 29 of them, so the scan of the 20 marked backups did not cover every snapshot that had no test on GitHub. Every commit on GitHub was then scanned, with no finding ([DEC-064](DEC-064-retired-branches-kept-and-backup-commits-skip-checks.md), decision 2). The builder tells the owner with this change's report.

## Decision

1. **The message is preserved word for word**, as [owner decisions 33](../handoffs/owner-decisions-33-question-on-what-is-going-on.md), a HISTORICAL source listed in the preserved-text manifest. It was taken by script from its user turn of 20:12 UTC in the session record, at 20:13 UTC, and kept byte for byte, including the space that ends it, so `git diff --check` reports its line; the text is not trimmed to satisfy it. It was kept in the builder's scratch folder until run 4 reported, which settled the change that preserves it. Its file, written at 20:46 UTC, was pushed to this change's temporary backup on 2026-11-10 at 01:53 UTC: the 5-hour limit stopped the session at 20:46 UTC, before the push ([Stage 1 certificate verification](../traceability/stage-01-certificate-verification.md), "Failures and fixes"; [DEC-057](DEC-057-progress-continuity-no-loss-and-recovery.md), decision 4).
2. **It changes nothing.** It asks a question, which the builder answered. The run that failed after the answer is recorded with its fixes, and the work goes on in the order of the [project state](../project-state.md)'s "Next approved step".
3. **It is preserved with this change, whose record names it.** A record names the owner's messages received up to the copy that its last Gate 3 run reviews ([traceability README](../traceability/README.md), Scope). The message came after run 4's copy (20:09 UTC); run 4 failed, and run 5 reviews a copy made after the message, as with owner decisions 32 ([DEC-065](DEC-065-preserve-owner-question-on-skipping-checks.md), decision 3).

## Alternatives considered

- **Treat it as procedural.** Not chosen: it asks a question, which DEC-047 (decision 7) keeps, as the owner's questions of the same kind were kept ([DEC-063](DEC-063-preserve-owner-question-of-2026-11-09.md), DEC-065, and earlier).
- **Preserve it with the next change.** Not chosen: the Scope rule ties a message to the record whose last Gate 3 run reviews a copy made after it, and that record is this change's.
- **Trim its space, so that `git diff --check` stays clean.** Not chosen: a text kept in a text block equals the message as received, byte for byte (the [documentation tools](../../tools/docs/README.md)' rule for preserved texts).

## Consequences

- Owner decisions 33 is listed in the preserved-text manifest and the documentation index.
- This change's record names the message.
- No requirement, rule, gate, or code changes. Nothing here authorizes work beyond [DEC-038](DEC-038-stage-1-plan-approved.md)'s Stage 1.
