# DEC-063 — Preserve the owner's question of 2026-11-09, 14:01 UTC, on where the work stands and whether everything is in order (owner decisions 30)

- **Status:** ACCEPTED
- **Date:** 2026-11-09
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept). The message is the owner's.

## Context

On 2026-11-06 at 12:38 UTC the weekly usage limit stopped the session, and with it the first Gate 3 launch of the change that repeats X10 and writes Stage 1's completion certificate (X6), before that reviewer reported ([Stage 1 certificate verification](../traceability/stage-01-certificate-verification.md), "Gates"). The limit reset on 2026-11-09 at 12:00 UTC. At 14:01 UTC the owner asked where the work stands now, and said that the owner hopes there is no problem and that everything is in order. It is a user turn of its own in the session record, of origin human, not one of the client's own entries (its notices of restarts, the stop hook's feedback, its notices of background tasks), so it is the owner's message.

The builder answered at 14:03 UTC, from the repository and GitHub:

- **Where the work is:** Stage 1, FOUNDATION, at its exit. Its last commit, `6d58014`, is on the designated branch with passing machine checks (1,108 tests); the code is unchanged since checkpoint D; no blocking finding is open.
- **Whether everything is in order:** yes, and nothing was lost. The certificate's change is complete and passes its checks 1 to 6. It is uncommitted, and its backup on GitHub, `3365a98`, holds the same tree as the working tree, checked at 14:02 UTC.
- **What happened:** the change was sent to its independent review on 2026-11-06; the weekly limit stopped the session and the reviewer at 12:38 UTC, before the reviewer reported.
- **What comes next:** the question preserved in the same change; a fresh reviewer on a new copy ([DEC-049](DEC-049-preserve-owner-messages-of-2026-10-20.md)); the fixes, the commit, the push, and the machine checks; then four questions to the owner (the approval to plan Stage 2, X8; the retired backup branches; the reading of the aspirational daily objective of owner decisions 29; and adaptive execution, EXE-011); then the mapping of owner decisions 29 ([DEC-062](DEC-062-preserve-and-map-universal-opportunity-directive.md)).

## Decision

1. **The message is preserved word for word**, as [owner decisions 30](../handoffs/owner-decisions-30-question-on-where-the-work-stands-after-the-weekly-limit.md), a HISTORICAL source listed in the preserved-text manifest. It was taken by script from its user turn of 14:01 UTC in the session record and kept byte for byte, including the space that ends its line, so `git diff --check` reports that line; the text is not trimmed to satisfy it. It was pushed to this change's temporary backup at 14:04 UTC ([DEC-057](DEC-057-progress-continuity-no-loss-and-recovery.md), decision 4).
2. **It changes nothing.** It asks a question, which the builder answered from the repository. The work goes on in the order of the [project state](../project-state.md)'s "Next approved step".
3. **It is preserved with this change, whose record names it.** A record names the owner's messages received up to the copy that its last Gate 3 run reviews ([traceability README](../traceability/README.md), Scope). The launch of 2026-11-06 was stopped before it reported, and a fresh run reviews a new copy, made after this message. So the message comes before that copy, as [owner decisions 25](../handoffs/owner-decisions-25-question-on-the-stage-and-progress.md) and [owner decisions 27](../handoffs/owner-decisions-27-questions-on-quality-position-and-the-directive.md) came before the copies of the changes that preserved them ([DEC-056](DEC-056-preserve-owner-question-of-2026-10-29.md), [DEC-060](DEC-060-preserve-owner-questions-of-2026-11-03.md)).

## Alternatives considered

- **Treat it as procedural.** Not chosen: it asks a question, which DEC-047 (decision 7) keeps, as owner decisions 25, 27, and 28, questions of the same kind, were kept (DEC-056, DEC-060, [DEC-061](DEC-061-preserve-owner-question-on-progress-of-2026-11-03.md)).
- **Preserve it with the next change.** Not chosen: it arrived before the copy that this change's last Gate 3 run reviews, so this change's record names it (the Scope rule), and the next change would leave the owner's words only in the session record for longer (DEC-057, decision 4).
- **Trim the space that ends its line, so that `git diff --check` stays clean.** Not chosen: a text kept in a text block equals the message as received, byte for byte (the [documentation tools](../../tools/docs/README.md)' rule for preserved texts).

## Consequences

- Owner decisions 30 is listed in the preserved-text manifest and the documentation index.
- This change's record names the message.
- No requirement, rule, gate, or code changes. Nothing here authorizes work beyond [DEC-038](DEC-038-stage-1-plan-approved.md)'s Stage 1.
