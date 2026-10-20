# DEC-050 — Preserve the owner's two questions of 2026-10-20 (owner decisions 19)

- **Status:** ACCEPTED
- **Date:** 2026-10-20
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept). The questions are the owner's.

## Context

On 2026-10-20, during the Gate 3 runs of the change that commits the reports of earlier Gate 3 runs as evidence ("Next approved step", item 2), the owner asked two questions: the first sent at 11:49 UTC, after its third run reported, and received at 11:57, after its fourth run began; the second at 12:39, before that run reported. The first asked whether the builder still knows what is being built, what this company project is, and what it is all about. The second asked whether what the builder showed in answer is everything discussed and handed over, or only a summary, since the project is company-grade. Both asked the builder to continue its work while answering.

The builder answered each from the repository, not from memory:
- the first from the [platform overview](../product/platform-overview.md), the [roadmap](../roadmap/roadmap.md), and the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md);
- the second with what the repository holds: the owner's handoffs and decisions kept word for word, and the documents, requirements, systems, system rules, values, decisions, and findings, with the counts the documentation checker and the registers give.

The answers changed nothing.

## Decision

1. **Both messages are preserved word for word**, as [owner decisions 19](../handoffs/owner-decisions-19-questions-on-the-project-and-the-knowledge-base.md), a HISTORICAL source listed in the preserved-text manifest.
   - Each was taken by script from its own user turn in the session record and kept byte for byte. That includes the space that ends each, so `git diff --check` reports those two lines in this change; the text is not trimmed to satisfy it.
   - They are kept because they are questions: [owner decisions 16](../handoffs/owner-decisions-16-short-instructions-approvals-and-questions.md) keeps a question on the state of the work, and [owner decisions 18](../handoffs/owner-decisions-18-question-go-ahead-and-review-relaunch.md) a question on the rules ([DEC-049](DEC-049-preserve-owner-messages-of-2026-10-20.md)).
   - The owner's "Continue" messages of the same day stay procedural (DEC-047, decision 7).
2. **They change nothing.** No requirement, rule, decision, or plan changes. The instruction to continue while answering is the owner's instruction of 2026-10-19, applied as [DEC-048](DEC-048-preserve-and-apply-rule-0.md) (decision 5) says.

## Alternatives considered

- **Treat them as procedural.** Not chosen: they are questions, which owner decisions 16 and 18 keep.
- **Trim the final spaces, so that `git diff --check` stays clean.** Not chosen: a text kept in a text block equals the message as received byte for byte (the [documentation tools](../../tools/docs/README.md)' rule for preserved texts). The check's two reports are explained in this change's verification record.
- **Preserve them with the next change.** Not chosen: they arrived during this change's Gate 3 runs, and its record names the owner's messages up to the copy its last run reviews, with where each is preserved, as owner decisions 18 was preserved with the change in whose runs its messages arrived (DEC-049).

## Consequences

- Owner decisions 19 is listed in the preserved-text manifest and the documentation index.
- The verification record of the change names the messages ([traceability README](../traceability/README.md), Scope).
- No requirement, rule, gate, or code changes. Nothing here authorizes work beyond [DEC-038](DEC-038-stage-1-plan-approved.md)'s Stage 1.
