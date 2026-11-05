# DEC-061 — Preserve the owner's question of 2026-11-03, 19:58 UTC, on where exactly the work stands and whether it is really progressing (owner decisions 28)

- **Status:** ACCEPTED
- **Date:** 2026-11-03
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept). The message is the owner's.

## Context

On 2026-11-03 at 19:58 UTC, while the first Gate 3 run of X2 of Stage 1's exit checklist (the stage's own three gates on its final tree, [Stage 1 verification](../traceability/stage-01-verification.md)) was under way, and after the copy it reviewed had been made at 19:50 UTC, the owner asked where exactly the work stands and whether it is really progressing, and asked the builder to continue while answering. It is a user turn of its own in the session record, of origin human, delivered as a turn at once, not one of the client's own entries (its resume prompts, notices of restarts, the stop hook's feedback, its notices of background tasks), so it is the owner's message.

The builder answered at 20:00 UTC, from the repository and the machine checks:

- **Where the work is:** Stage 1, FOUNDATION, the first of the [roadmap](../roadmap/roadmap.md)'s seven stages and the only one authorized ([DEC-038](DEC-038-stage-1-plan-approved.md)), at its exit; its code complete and unchanged since checkpoint D (exact amounts, the contract kernel, the configuration and its secrets, the `atp config check` command; 1,108 tests; each rule's test failing when its rule is removed, 461 mutations); of the exit checklist, X7 and X9 done, X2 in its last gate, its technical gate already passed on the reviewed tree, and X10, the certificate (X6), and the owner's approval to plan Stage 2 (X8) remaining; no trading capability, by design.
- **Progress:** yes, measurably, but slowly: five changes committed through their three gates since the work resumed on 2026-11-02, item 5 and X9 among them on 2026-11-03, with three 5-hour usage limits that day; none of it adds product capability, since it closes Stage 1 under the owner's rules. What slows it: the usage limits, the longest from 2026-10-29 to 2026-11-02; independent reviews failing mostly on the records' wording rather than on code; and each change's verification work. The [project state](../project-state.md) rates the stage SLOWLY CONVERGING, with no blocking finding open and its exit criteria fixed ([DEC-057](DEC-057-progress-continuity-no-loss-and-recovery.md), decision 5).
- **Options:** the three ways to go faster offered on 2026-10-29 stay open, for the owner to decide ([DEC-056](DEC-056-preserve-owner-question-of-2026-10-29.md)); the builder applies none of them on its own.

## Decision

1. **The message is preserved word for word**, as [owner decisions 28](../handoffs/owner-decisions-28-question-on-where-the-work-stands-and-progress.md), a HISTORICAL source listed in the preserved-text manifest. It was taken by script from its user turn of 19:58 UTC in the session record and kept byte for byte, including the spaces that end its two lines, so `git diff --check` reports those lines in this change; the text is not trimmed to satisfy it.
2. **It changes nothing.** It asks a question, which the builder answered from the repository, and asks the builder to continue while answering, which the existing order of work already provides ([DEC-048](DEC-048-preserve-and-apply-rule-0.md), decision 5). The options of DEC-056 stay undecided; the work goes on in the order of the project state's "Next approved step".
3. **It is preserved with the next change, X10, whose record names it.** A record names the owner's messages received up to the copy that its last Gate 3 run reviews, and the next record names any received later ([traceability README](../traceability/README.md), Scope): the message came after the copy of X2's only Gate 3 run, so X2's record leaves it to the next change, as its final status says.

## Alternatives considered

- **Treat it as procedural.** Not chosen: it asks a question, which DEC-047 (decision 7) keeps, as [owner decisions 25](../handoffs/owner-decisions-25-question-on-the-stage-and-progress.md) and [owner decisions 27](../handoffs/owner-decisions-27-questions-on-quality-position-and-the-directive.md), questions of the same kind, were kept (DEC-056, [DEC-060](DEC-060-preserve-owner-questions-of-2026-11-03.md)).
- **Preserve it with X2's change, as those were preserved with the change in progress when they arrived.** Not chosen: those arrived before the copy their change's last Gate 3 run reviewed, and this one after it; adding it to X2's change would have added material that no Gate 3 run reviewed ([DEC-032](DEC-032-adopt-checkpoint-and-verification-rule.md)), or needed another run for it alone.
- **Trim the spaces that end its lines, so that `git diff --check` stays clean.** Not chosen: a text kept in a text block equals the message as received, byte for byte (the [documentation tools](../../tools/docs/README.md)' rule for preserved texts).

## Consequences

- Owner decisions 28 is listed in the preserved-text manifest and the documentation index.
- X10's record names the message.
- No requirement, rule, gate, or code changes. Nothing here authorizes work beyond [DEC-038](DEC-038-stage-1-plan-approved.md)'s Stage 1.
