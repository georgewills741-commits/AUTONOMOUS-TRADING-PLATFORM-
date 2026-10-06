# DEC-037 — Final decision and integrity checkpoint: first-round answers preserved, quotations annotated

- **Status:** ACCEPTED
- **Date:** 2026-10-05
- **Decided by:** builder, under the owner's request of 2026-10-05 for a final human-decision, knowledge-base, consistency, and repository checkpoint (the [checkpoint record](../traceability/final-decision-checkpoint-2026-10-05.md)), and under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim)
- **Resolves:** the master knowledge-base audit's finding A-17 (the owner's first-round answers, and the options shown with CF-11 to CF-13, were not recorded verbatim)

## Context

The owner asked for a final audit of everything handed off and decided, verifying the decisions the owner actually made rather than the repository's summaries of them. The audit compared every decision the repository attributes to the owner with the questions as asked and the answers as given in the builder session's record, the record from which owner decisions 2 to 5 were preserved. Three things were found:

1. **The first round was never preserved.** The owner's instruction of 2026-09-30 to resolve every open item before Part 2 (under which the builder accepted DEC-001 to DEC-005 and decided DEC-010 to DEC-018) and the answers to OQ-01, OQ-03, OQ-04, and OQ-16, applied by DEC-006 to DEC-009, existed in the repository only as summaries (finding A-17). The options shown with the CF-11 to CF-13 questions were not preserved either.
2. **Three decision records quote those answers with edits.** DEC-007 adds a comma. DEC-008 adds a comma, changes "exchange" to "exchanges" and "bybit" to "Bybit", and replaces "and many more like kucoin exchange" with "and KuCoin"; its five initial venues are the builder's reading of the answer, reported to the owner the same day without objection, and its decision 2 (room for more venues) carries "many more". DEC-009 changes "suit" to "suits" and "mt" to "my" and leaves out "well". None of the edits changes a decision, but a quotation must be exact (constitution Rules 26, 181).

The audit also found a wording point. The option the owner chose for OQ-01 read "No custody, deposits, withdrawals, or user accounts". DEC-006's decision text says "no deposit or withdrawal handling for others", and the CF-21 question of 2026-10-03 quoted that text as the owner's original decision. The words "for others" are the builder's, so the CF-21 question presented builder wording as the owner's. The outcome is not affected, because it rests on the owner's own later instructions: owner correction 1 requires autonomous rebalancing (item 1) through a separate rebalancing transfer authority between approved accounts that "must not become a general-purpose withdrawal mechanism" (item 4); owner decisions 3, Q6, requires automatic rebalancing of the capital buckets; and the owner explicitly chose PLT-010's present wording on 2026-10-03 ([DEC-036](DEC-036-owner-decisions-audit-findings.md)). Newer explicit owner instructions take precedence over an earlier option's wording, so no owner decision is needed.

## Decision

1. The owner's instruction that started the first round, and its questions as asked and answers as given, are preserved verbatim as [owner decisions 1](../handoffs/owner-decisions-01-part-1-open-items.md) (HISTORICAL); the options shown with the CF-11 to CF-13 questions are preserved as a supplement to owner decisions 2, [owner decisions 2: options shown](../handoffs/owner-decisions-02-options-shown.md). Both have a line in the preserved-texts manifest.
2. DEC-006 to DEC-009 keep their text. Each gets a "Later changes" line that points to the verbatim answer and states how its quotation or wording differs; the open-question register's OQ-01, OQ-03, OQ-04, OQ-16, and OQ-28 rows point to the verbatim answers. DEC-021 to DEC-023, which say the options shown with their questions are not in the repository, get a "Later changes" line pointing to the options supplement.
3. The CF-21 wording point is recorded in the "Later changes" lines of DEC-006 and DEC-036, in CF-21's status, and in the checkpoint record (finding F-02), with the precedence that settles it, and it is reported to the owner.

## Alternatives considered

- **Leave finding A-17 as it was:** rejected; the verbatim answers are available, and the owner asked for the actual decisions to be verified.
- **Correct the quotations inside DEC-006 to DEC-009:** rejected; decision records are not rewritten (constitution Rule 165: history is not destroyed). "Later changes" lines are the repository's convention.
- **Ask the owner to re-confirm DEC-006 to DEC-009:** not needed; the verbatim answers match each decision, and the one wording point is settled by the owner's later explicit instructions.

## Consequences

- No requirement and no decision changes (`tools/docs/compare_requirements.py 47f5348 --strict` shows no change).
- The decisions the repository attributes to the owner are traceable to the owner's words as given: DEC-006 to DEC-009, DEC-021 to DEC-023, DEC-026 to DEC-030, DEC-035, DEC-036, and DEC-038 to owner decisions 1 to 6; DEC-019 and DEC-020 to owner correction 1; DEC-032 to DEC-034 to the owner's texts under `docs/builder/`. The builder-decided records rest on the owner's delegations, now also preserved (owner decisions 1).
