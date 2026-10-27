# DEC-053 — Preserve the owner's status check of 2026-10-21, question of 2026-10-26, and instruction to continue of 2026-10-27 (owner decisions 21)

- **Status:** ACCEPTED
- **Date:** 2026-10-21; the second message added on 2026-10-26, the third on 2026-10-27
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept). The messages are the owner's.

## Context

On 2026-10-21 at 05:39 UTC, while Stage 1's checkpoint C was in its Gate 3, the owner sent a status, stage-integrity, and continuation check. It asks the builder to confirm from repository evidence that the project still follows the approved plan, roadmap, requirements, rules, and stage boundaries; to report the repository and commit state, classifying each material item before committing anything; to confirm each stage reached and the current one; to confirm that the permanent rules stored in the repository are still followed, reusing and reinforcing existing protections rather than duplicating them; and to continue the authorized work while answering. The builder had just stopped the first launch of checkpoint C's Gate 3 run 1, before it reported, to correct stale status statements its own sweep had found ([checkpoint C verification](../traceability/stage-01-checkpoint-c-verification.md)). The session then paused until 09:57 UTC.

The builder answered from the repository: the git state, the branches on GitHub, the project state, the stage record, the roadmap, the verification records, and the documentation checker.

On 2026-10-26 at 17:57 UTC, after Gate 3 run 1 had reported and while its findings were being fixed, the session having been paused since 2026-10-21 at 11:26 UTC, the owner asked where the work stands and whether it is actually progressing, and asked the builder to continue while answering, to be sure that everything is in order. The builder answered from the repository: the working tree, the backup branch on GitHub, the results of the checks and of the mutation run, and run 1's findings and fixes ([checkpoint C verification](../traceability/stage-01-checkpoint-c-verification.md)).

On 2026-10-27 at 04:05 UTC, after Gate 3 run 3 had reported and the session had stopped at the owner's usage limit, the owner wrote that the limit had reset and asked the builder to continue from where it left off. It is a user turn of its own in the session record, not one of the client's own entries (its resume prompts, the stop hook's feedback, its notices of finished background tasks), so it is the owner's message. The builder continued with the fixes of run 3's findings.

## Decision

1. **The three messages are preserved word for word**, as [owner decisions 21](../handoffs/owner-decisions-21-status-stage-integrity-and-continuation-check.md), a HISTORICAL source listed in the preserved-text manifest.
   - Each was taken by script from its own user turn in the session record and kept byte for byte. That includes the space that ends the first message's first line, so `git diff --check` reports that line in this change; the text is not trimmed to satisfy it.
   - The client's own "Continue from where you left off." prompts are not part of them, and stay procedural (DEC-047, decision 7).
2. **They change nothing.** Each instruction of the first message is already a rule of the repository, applied through the existing mechanisms; none is added or stated a second time ([owner decisions 17](../handoffs/owner-decisions-17-reuse-reinforce-and-enhance-existing-controls.md), Rule 0; [DEC-048](DEC-048-preserve-and-apply-rule-0.md)):
   - no claim without evidence: the master execution constitution (§55, §166) and the quality directive (§10);
   - each material item classified before a commit, important drafts committed as drafts, and nothing inappropriate committed: [owner decisions 15](../handoffs/owner-decisions-15-stage-transition-persistence-and-commit-integrity.md) (§1, §3, §5, §7), applied by [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md);
   - each stage confirmed from its outputs to its final status: the stage record's fields (master execution constitution §142) and its exit checklist;
   - existing protections reused, reinforced, and enhanced where evidence shows a real gap, never duplicated: Rule 0, applied by DEC-048;
   - work continued while answering, stopping only for an owner-level decision, a critical blocker, contradictory authority, or a safety rule: the owner's instruction of 2026-10-19, applied as DEC-048 (decision 5) says, with the stop rules of the master execution constitution (§153) and the quality directive (§2, §11).

   The second message asks a question and repeats the instruction to continue while answering, which is the same instruction of 2026-10-19. The third gives that instruction again.
3. **They are preserved with checkpoint C**, during whose Gate 3 they arrived. Checkpoint C's verification record names it ([traceability README](../traceability/README.md), Scope; DEC-048, decision 3).

## Alternatives considered

- **Treat them as procedural.** Not chosen: they ask questions and give instructions, which DEC-047 (decision 7) keeps, as owner decisions 19 was kept ([DEC-050](DEC-050-preserve-owner-questions-of-2026-10-20.md)).
- **Trim the space that ends the first message's first line, so that `git diff --check` stays clean.** Not chosen: a text kept in a text block equals the message as received byte for byte (the [documentation tools](../../tools/docs/README.md)' rule for preserved texts).
- **Preserve them with the next change.** Not chosen: they arrived during checkpoint C's Gate 3, and checkpoint C's record names the owner's messages up to the copy its last run reviews, with where each is preserved (DEC-050).
- **Write their instructions as new rules.** Not chosen: each is already stated (decision 2), and a second statement would compete with the first (Rule 0).
- **A second decision record and a second preserved text for the question of 2026-10-26, or for the instruction of 2026-10-27.** Not chosen: the three messages arrived during the same checkpoint's Gate 3 and change nothing, and one record kept owner decisions 19's two questions (DEC-050).

## Consequences

- Owner decisions 21 is listed in the preserved-text manifest and the documentation index.
- Checkpoint C's verification record names the three messages.
- No requirement, rule, gate, or code changes. Nothing here authorizes work beyond [DEC-038](DEC-038-stage-1-plan-approved.md)'s Stage 1.
