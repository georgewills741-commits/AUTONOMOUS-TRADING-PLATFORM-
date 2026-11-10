# DEC-062 — Preserve the owner's directive of 2026-11-06 on universal opportunity intelligence, profit optimization, and controlled implementation (owner decisions 29), and map its parts to the canonical requirements in the next change

- **Status:** ACCEPTED
- **Date:** 2026-11-06
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept). The message, its directive, and its instructions are the owner's.
- **Later changes:** On 2026-11-10 the change after the certificate's recorded Stage 1's exit, the owner's approval to plan Stage 2 with the owner's answers on two of the directive's points ([DEC-067](DEC-067-stage-1-exit-and-owner-answers-of-2026-11-10.md)). The mapping of decision 3 follows that change, and applies those answers; its place in the order of work, before Stage 2's plan, is unchanged.

## Context

On 2026-11-06 at 11:59 UTC the owner sent a message, the first since the session stood still from 2026-11-05, 03:54 UTC, when the 5-hour limit stopped it. The change that repeats X10 of Stage 1's exit checklist on `6d58014` and writes the stage's completion certificate (X6) was in progress, and the copy that its Gate 3 run reviews had not been made ([Stage 1 certificate verification](../traceability/stage-01-certificate-verification.md)). The message is a user turn of its own in the session record, of origin human, not one of the client's own entries, so it is the owner's.

Its first line asks the builder to continue what it is doing; to take the most valuable parts of the directive that follows and put them where they belong; not to make mistakes; and to ask for any permission it needs on the GitHub repository, such as the permission to delete. The directive, "AUTONOMOUS TRADING PLATFORM — UNIVERSAL OPPORTUNITY INTELLIGENCE, PROFIT OPTIMIZATION & CONTROLLED IMPLEMENTATION", has twenty sections and a final directive:

- **The platform:** its objective and an aspirational daily objective of about 1.2% net that is never forced (§3, §12); universal opportunity discovery, small opportunities, and the preference ladder (§4, §9); discovery intensity (§5); multiple exchanges (§6); net profitability (§7); capital allocation (§8); the coordination of strategies (§10); AI's authority and cost (§11); execution quality (§13); performance measurement (§14); and capital protection (§15).
- **The builder:** its role (§1); a repository audit before any implementation, which classifies each requirement as VERIFIED EXISTING, EXISTING BUT INCOMPLETE, IMPLEMENTED BUT UNVERIFIED, MISSING, CONFLICTING, UNNECESSARY DUPLICATE, or BLOCKED (§2); three verification gates (§16); root-cause correction (§17); change management (§18); a workflow (§19); and a final report (§20).

It ends: "BEGIN WITH THE REPOSITORY AUDIT. PRESERVE THE EXISTING CHECKPOINT. IMPLEMENT ONLY WHAT IS GENUINELY NECESSARY."

Several of its platform principles are already in the canonical requirements, some since [owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md) restated them and its audit added them ([DEC-058](DEC-058-opportunity-universe-and-economics.md)). Among them:

- the order 3%, 2%, 1.5%, 1%, 0.9%, and lower, as a search priority only (OPP-022, from DEC-058);
- scanning that does not stop at a found opportunity (OPP-021, from DEC-058);
- no guaranteed or fixed daily return, and no daily ceiling (TNP-012 to TNP-014, TNP-026);
- economic eligibility from the true net expected result (TNP-018 to TNP-020).

Which of its parts the canonical requirements already state, and which they do not, is what the mapping establishes. The directive's three gates (§16) are numbered and named differently from [DEC-032](DEC-032-adopt-checkpoint-and-verification-rule.md)'s.

## Decision

1. **The message is preserved word for word**, as [owner decisions 29](../handoffs/owner-decisions-29-universal-opportunity-intelligence-and-profit-optimization.md), a HISTORICAL source listed in the preserved-text manifest.
   - It was taken by script from its user turn of 11:59 UTC in the session record and kept byte for byte, including the space that ends its first line and the line break that ends its last. So `git diff --check` reports that line; the text is not trimmed to satisfy it.
   - It was pushed to this change's temporary backup at 12:02 UTC, three minutes after it arrived ([DEC-057](DEC-057-progress-continuity-no-loss-and-recovery.md), decision 4).
2. **Its first instruction is followed: the work in progress continues.** The certificate's change goes on in the order of the [project state](../project-state.md)'s "Next approved step": the certificate (X6) is committed after its gates, and the owner's approval to plan Stage 2 (X8) is asked for after that commit.
3. **The instruction to "choose the most valuable part and put them to where the belong" is carried out by the next change, as its own change**, as owner decisions 8 was ([DEC-041](DEC-041-preserve-opportunity-and-economics-directive.md), then DEC-058).
   - **The platform's parts:** each requirement of the directive is mapped to the canonical requirement, rule, or decision that already states it, with the directive's own classification (§2) and its evidence. A requirement is refined, or drafted, only where none states it, under [owner decisions 9](../handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md)'s drafting rules and Rule 0 ([owner decisions 17](../handoffs/owner-decisions-17-reuse-reinforce-and-enhance-existing-controls.md); [DEC-048](DEC-048-preserve-and-apply-rule-0.md)), so that no second source, authority, or component appears. Anything that needs the owner's decision is put to the owner, with its options.
   - **The builder's parts** (§1, §2, §16 to §20) are mapped the same way, to the six builder texts and the owner's rule sets, its three gates included, so that DEC-032's gates keep their names and their meaning (owner decisions 9, Rules 3 and 27).
   - **The tools:** the mapping uses git, the documentation tools, and the repository's own indexes. Graphify is not available in this environment, and the directive asks for it only "when available and materially useful" and says: "Do not fabricate findings if a tool or repository is inaccessible."
   - **Its place in the order of work:** after this change's commit and before Stage 2's plan, which builds on the requirements it maps. It writes documentation only.
4. **The permission it offers, on the retired backup branches.**
   - This session's access to GitHub refuses the deletion of the twelve retired temporary backup branches, with HTTP 403 ([DEC-054](DEC-054-configuration-size-limit-and-retired-backup-branches.md), decision 4).
   - The builder planned to ask, with X8, how the owner wants them handled, deletion or their carrying past Stage 1 ([DEC-044](DEC-044-preserve-archive-tag-answers-and-convergence-audit.md), decision 2). The owner raised it first, on 2026-11-09, before this record's commit; the builder asked then, saying that no permission it can request changes the refusal, and the owner chose to keep them until the owner removes them ([DEC-064](DEC-064-retired-branches-kept-and-backup-commits-skip-checks.md)).
   - The archive branches are kept ([DEC-052](DEC-052-apply-owner-answers-on-order-of-work-and-backups.md), decision 3).
5. **Nothing else changes now.** No requirement, rule, gate, value, or code changes with this record. Stage 1's exit criteria stay fixed (DEC-057, decision 5). The directive's trading capability is built only by the stages that build it, each with its own approved plan ([DEC-038](DEC-038-stage-1-plan-approved.md)). The directive's §19 allows that wait: "Stop only where a genuine safety, authorization, external-service, capital-allocation, or unresolved technical blocker prevents responsible continuation."
6. **It is preserved with this change, whose record names it.** It arrived before the copy that this change's Gate 3 run reviews ([traceability README](../traceability/README.md), Scope), as [owner decisions 25](../handoffs/owner-decisions-25-question-on-the-stage-and-progress.md) and [owner decisions 27](../handoffs/owner-decisions-27-questions-on-quality-position-and-the-directive.md) were preserved with the change in progress when they arrived ([DEC-056](DEC-056-preserve-owner-question-of-2026-10-29.md), [DEC-060](DEC-060-preserve-owner-questions-of-2026-11-03.md)).

## Alternatives considered

- **Map it in this change.** Not chosen: the mapping reads the requirements of every later stage, while this change closes Stage 1 under fixed criteria. One change for each keeps both reviewable (constitution Rules 66, 161, and 162; DEC-041), and the certificate closes without waiting for the mapping ([owner decisions 26](../handoffs/owner-decisions-26-progress-continuity-no-loss-and-recovery.md)).
- **Preserve only its most valuable parts.** Not chosen: the owner's messages are kept whole (DEC-004; DEC-047, decision 7). The selection the owner asks for applies to what goes into the canonical requirements, not to what is kept.
- **Load it as a seventh builder text.** Not chosen: Rule 0 reinforces the existing rules rather than adding a parallel set (owner decisions 17; DEC-048). The mapping shows, for each of its builder rules, the builder text or rule set that already states it, or the gap it fills.
- **Try the deletion again now.** Not chosen: nothing shows that this environment's access has changed. The owner offered to give the permission when asked; the message does not ask for another attempt (DEC-054, decision 4).

## Consequences

- Owner decisions 29 is listed in the preserved-text manifest and the documentation index.
- This change's record names the message.
- The project state's "Next approved step" names the mapping as the next change, and the certificate's "Remaining future work" names it too.
- The question to the owner after the certificate's commit carries X8; the choice on the retired branches was asked and answered on 2026-11-09 (DEC-064).
- No requirement, rule, gate, or code changes. Nothing here authorizes work beyond DEC-038's Stage 1.
