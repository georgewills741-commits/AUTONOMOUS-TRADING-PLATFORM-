# DEC-069 — Preserve the owner's three questions of 2026-11-11, on what remains, on how long Stage 2 will take, and on upgrading to the 200-dollar plan (owner decisions 35)

- **Status:** ACCEPTED
- **Date:** 2026-11-16
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept). The messages are the owner's.

## Context

On 2026-11-11 the 5-hour usage limit stopped the session at 05:27 UTC, during the first Gate 3 run of the change that maps [owner decisions 29](../handoffs/owner-decisions-29-universal-opportunity-intelligence-and-profit-optimization.md) to the canonical requirements ([DEC-068](DEC-068-universal-opportunity-directive-mapped.md)). The session resumed with the owner's "Okay" of 11:50 UTC, and the run was resumed the same minute ([DEC-049](DEC-049-preserve-owner-messages-of-2026-10-20.md), decision 3). While it ran, the owner sent three messages: at 11:52 UTC, what is remaining; at 12:00 UTC, how long Stage 2 will take to complete, with the instruction to continue while answering; at 12:04 UTC, about upgrading to the 200-dollar plan. The client delivered each as a user turn of its own, of origin human, in the second its queue entry was made (11:52:25, 12:00:12, and 12:04:27 UTC), not one of the client's own entries (its resume prompts, notices of restarts, the stop hook's feedback, its notices of background tasks), so each is the owner's message.

The builder answered each from the repository:

- **What is remaining** (11:52 UTC): the mapping change, the only work in progress, in its Gate 3 review; then, each through the three gates, the workflow's change of [DEC-064](DEC-064-retired-branches-kept-and-backup-commits-skip-checks.md) (decision 2) and Stage 2's plan, which comes to the owner for approval, nothing of Stage 2 being built before it; waiting on the owner, that approval and the deletion of the fourteen retired backup branches on GitHub, which this environment is refused; after Stage 2, Stages 3 to 7, each with its own plan and the owner's approval; no trading capability yet; the 5-hour limit pausing the reviews without losing work, everything being backed up on GitHub as it changes; the question kept word for word with the next change that records the owner's messages.
- **How long Stage 2 will take** (12:01 UTC): about two to three months from then, "a rough range, not a promise", to be firmed up once the plan exists: about a week before Stage 2 starts (the mapping, the workflow's change, the plan, and the owner's approval of it), then roughly six to ten weeks to build it, Stage 2 having about 67 requirements in the [registry](../requirements/registry.md) against the 25 that Stage 1's plan delivered in about five weeks; what moves it: the usage limits above all, the number of review runs, access to the exchanges' public market data from this environment, and the owner's decisions in the plan, which will split the stage into checkpoints, each with its estimate.
- **Upgrading to the 200-dollar plan** (12:04 UTC): the owner's decision; the builder cannot see the owner's plan, and this environment's documentation, which the builder read, does not cover plans; the usage limits are the project's largest delay: the weekly limit's stops of about four days, from 2026-10-29 to 2026-11-02, and three, from 2026-11-06 to 2026-11-09, several 5-hour stops a day lately, and the time after each reset until the owner's next message; an upgrade would mean fewer and shorter stops, and would change neither the gates nor the owner's approvals, nor make the platform depend on any plan.

Two statements of these answers were not right, and the builder corrected them to the owner on 2026-11-16, in the session:

- The answer of 11:52 UTC said that each retired backup's work "is saved in the main branch and an archive branch". It is saved in the commits of the designated branch, `claude/code-builder-constitution-rrewgf`, and in the backup's archive branch (the [project state](../project-state.md)'s "Branches"); the branch `main` holds only the repository's initial commit, `7172a5c`.
- The answer of 12:04 UTC gave each Gate 3 review "roughly 370,000 to 410,000 tokens". The client's notices of the seventeen earlier Gate 3 runs whose totals the session record holds, from 2026-11-02 to 2026-11-11, give 315,902 to 455,716 tokens a run, a wider range than the answer's.

One expectation of the answers did not hold: the mapping change was not finished that day. Its first Gate 3 run reported at 12:07 UTC; its fixes were applied and backed up at 12:10 UTC; and the weekly usage limit stopped the session at 12:11 UTC, until the owner's "Try again" of 2026-11-16, 18:21 UTC, the limit having reset that day at 12:00 UTC.

## Decision

1. **The messages are preserved word for word**, as [owner decisions 35](../handoffs/owner-decisions-35-questions-on-what-remains-stage-2-and-the-plan.md), a HISTORICAL source listed in the preserved-text manifest, each under its own dated heading. They were taken by script from their user turns of 11:52, 12:00, and 12:04 UTC in the session record, on 2026-11-16, and kept byte for byte, including the spaces that end each of their lines, so `git diff --check` reports those four lines in this change; the texts are not trimmed to satisfy it.
2. **They change nothing.** Each asks a question, which the builder answered, and the second asks the builder to continue while answering, which the existing order of work already provides ([DEC-048](DEC-048-preserve-and-apply-rule-0.md), decision 5). The choice of plan is the owner's, and nothing in the project depends on it. The work goes on in the order of the project state's "Next approved step".
3. **They are preserved with the change in progress when they arrived**, the mapping of owner decisions 29, whose record names them ([traceability README](../traceability/README.md), Scope). Its first Gate 3 run reviewed a copy made before them, at 05:19 UTC; it failed, and its second run reviews a copy made after them, as with owner decisions 33 ([DEC-066](DEC-066-preserve-owner-question-on-what-is-going-on.md), decision 3). The answer of 11:52 UTC, which put the question with the next change, was given while no second run was foreseen.

## Alternatives considered

- **Treat them as procedural.** Not chosen: each asks a question, which DEC-047 (decision 7) keeps, as the owner's questions of the same kind were kept ([DEC-060](DEC-060-preserve-owner-questions-of-2026-11-03.md), [DEC-061](DEC-061-preserve-owner-question-on-progress-of-2026-11-03.md), DEC-066, and earlier).
- **Preserve them with the next change.** Not chosen: the Scope rule ties a message to the record whose last Gate 3 run reviews a copy made after it, and that record is the mapping's.
- **One preserved text for each question.** Not chosen: three questions of one morning, sent during one change, are kept together, as [owner decisions 27](../handoffs/owner-decisions-27-questions-on-quality-position-and-the-directive.md) keeps two (DEC-060).
- **Trim the spaces that end their lines, so that `git diff --check` stays clean.** Not chosen: a text kept in a text block equals the message as received, byte for byte (the [documentation tools](../../tools/docs/README.md)' rule for preserved texts).

## Consequences

- Owner decisions 35 is listed in the preserved-text manifest and the documentation index.
- The mapping's record names the messages; the owner's "Okay" of 2026-11-11, 11:50 UTC, and "Try again" of 2026-11-16, 18:21 UTC, are procedural (DEC-047, decision 7).
- No requirement, rule, gate, or code changes. Nothing here authorizes any stage's implementation: Stage 2's planning is authorized and its implementation is not ([DEC-067](DEC-067-stage-1-exit-and-owner-answers-of-2026-11-10.md), decision 2).
