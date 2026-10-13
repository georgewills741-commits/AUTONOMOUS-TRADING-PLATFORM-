# DEC-041 — Preserve the owner's opportunity-universe and economics directive as soon as received

- **Status:** ACCEPTED
- **Date:** 2026-10-07
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and the owner's checkpoint rule ([DEC-032](DEC-032-adopt-checkpoint-and-verification-rule.md): "EVERYTHING MUST BE PRESERVED IN THE REPOSITORY"); the directive itself is the owner's

## Context

On 2026-10-07 the owner sent a message during Stage 1, after checkpoint B was built and while its three gates were running ([owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md)). It asks for a repository-backed status report, restates the opportunity-universe and trading-economics principles, and asks for an audit of the canonical requirements against them, with corrections where the resolution is established and owner questions where it is not.

The builder planned the audit as its own change after checkpoint B's commit, so as not to mix unrelated work in one commit (constitution Rule 162). Gate 3 of checkpoint B (its [verification record](../traceability/stage-01-checkpoint-b-verification.md), run 1, finding 7) then found that the project state named the audit as the next step while the owner's text existed only in the session: a fresh session could not have continued (master execution constitution §01, §88, §90).

## Decision

1. **The owner's message is preserved word for word now**, in checkpoint B's commit, as owner decisions 8, a HISTORICAL source listed in the preserved-text manifest.
2. **It changes nothing yet.** No requirement, rule, or document is changed by this record. The audit the owner asked for follows checkpoint B, in the order the [project state](../project-state.md) records, with its own decision record and verification record; that record applies the directive.
3. **The status report** the owner asked for is answered from the project state and the stage record, which are the canonical status.

## Alternatives considered

- **Keep the text only in the session until the audit's commit.** Rejected: a session ending in between would lose the owner's words, and the committed project state would point to text that does not exist (Gate 3's finding).
- **Make the whole audit part of checkpoint B's commit.** Rejected: it would mix the audit's documentation changes with checkpoint B's code and records (constitution Rule 162; master execution constitution §126).

## Consequences

- Checkpoint B's commit also carries this record and the preserved text; its verification record says so.
- The next session, or this one, applies the directive from the repository alone.
