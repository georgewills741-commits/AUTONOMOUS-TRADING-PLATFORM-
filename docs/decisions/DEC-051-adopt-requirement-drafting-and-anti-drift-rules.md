# DEC-051 — Adopt the owner's requirement drafting and anti-drift rules as the sixth builder text; the owner's other rule sets stay in force through their decision records

- **Status:** ACCEPTED
- **Date:** 2026-10-20
- **Decided by:** builder, carrying out the step [DEC-042](DEC-042-preserve-anti-drift-rules-and-backup-instructions.md) (decision 2) set, with its own decision record and three gates, for rules the owner sent as "PERMANENT BUILDER RULES" ([owner decisions 9](../handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md)). The rules and the other rule sets of decision 3 are the owner's. The reading of decision 2 and the mapping behind decision 3 are the builder's, made under the owner's Rule 0 (owner decisions 9 and 17), within what it lets the builder do without asking ([DEC-048](DEC-048-preserve-and-apply-rule-0.md)).

## Context

On 2026-10-07, during Stage 1, the owner sent the "CANONICAL REQUIREMENT DRAFTING & ANTI-DRIFT RULES": thirty-one rules, Rule 0 to Rule 30, marked permanent, continuous, mandatory, and non-optional. They govern requirement drafting, reconciliation, architecture work, implementation, and the project's evolution. They replace none of the existing rules: "Whenever an existing project rule already covers a situation, that existing rule remains authoritative." DEC-042 preserved them word for word. Its decision 2 made their adoption as a builder text that `CLAUDE.md` loads a later change, with its own decision record and three gates, before the audit of [owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md), which drafts requirements.

Four more rule sets of the owner followed:
- owner decisions 10's lifecycle for temporary backups (2026-10-13);
- the lasting rules of owner decisions 13 (2026-10-13);
- owner decisions 14 and 15 (2026-10-14);
- owner decisions 17, Rule 0 (2026-10-19).

The records that preserve or apply them each left one question to this step: whether they join the builder texts. Those records are DEC-042 (decision 7), [DEC-044](DEC-044-preserve-archive-tag-answers-and-convergence-audit.md) (decision 4), [DEC-045](DEC-045-apply-foundation-convergence-audit.md) (decision 9), [DEC-046](DEC-046-preserve-company-grade-order-and-traceability-rules.md) (decision 2), [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 2), and DEC-048 (decision 2). Meanwhile each rule set applies through its record. DEC-048 asked that the step first map them under Rule 0, "each rule set against the existing canonical texts first, and only a real gap adopted, without a parallel text".

The step starts from its [draft](../drafts/draft-adoption-of-owner-decisions-09.md) of 2026-10-07 and 2026-10-12 (DEC-046, decision 5; DEC-047, decision 3). Compared with the canonical records:
- Its copy of the rules for `docs/builder/` would be a second copy of a preserved text ([owner decisions 15](../handoffs/owner-decisions-15-stage-transition-persistence-and-commit-integrity.md), §8).
- Its number, DEC-042, has since been used.
- Its script was written to edit files as they stood on 2026-10-12; it was never run on the repository.
- Its reading notes remain valid. They are kept in decision 2, with what the decisions since have added.

## Decision

1. **Owner decisions 9 is the sixth builder text.** `CLAUDE.md` loads it in every session from its preserved copy, which stays where it is, under `docs/handoffs/`.
   - Its banner changes from HISTORICAL to ACTIVE, by this decision. Its text and its line in the preserved-text manifest do not change.
   - How the builder texts combine is unchanged ([DEC-033](DEC-033-adopt-master-execution-constitution.md)): all six apply, and where they differ, the stricter applies.
   - Its own master directive fits that rule. An existing rule that covers a situation stays authoritative. It adds to the existing rules and loosens none; for example, Rule 23 asks for a final reconciliation report before a batch of drafted requirements becomes authoritative.
2. **How it reads.** This is the builder's reading, recorded so that items 4 and 5 of "Next approved step" apply it the same way. The owner can correct it.

   | In owner decisions 9 | Reading |
   |---|---|
   | "Global Trading Constitution" (Rule 1) | No document has that name. It is read as [DEC-032](DEC-032-adopt-checkpoint-and-verification-rule.md) reads the "Global Game Constitution equivalent": the platform principles index (ARCH-028, in the [platform overview](../product/platform-overview.md)) with the [System Rules Register](../requirements/system-rules-register.md) |
   | Rule 8's categories (EXISTING REQUIREMENT, REFINED EXISTING REQUIREMENT, NEW CONFIRMED REQUIREMENT, PROPOSAL, and the others) | The outcome of reconciling a drafted item, recorded in the record that drafts it. They are not requirement classes ([ARCH-015](../architecture/overview.md); the [requirements README](../requirements/README.md)), which a requirement keeps in its line. A NEW CONFIRMED REQUIREMENT is written with the class its wording calls for, such as a CONSTRAINT for a prohibition. The [glossary](../glossary.md) keeps the two apart (DISTINCT) |
   | REFINED EXISTING REQUIREMENT | An existing requirement never changes silently: its class changes only by a decision record (the [requirements README](../requirements/README.md)); its text is not reworded silently (constitution Rule 56; the [quality directive](../builder/quality-consistency-and-correction-directive.md), §2); the requirement comparison shows the change, run with `--expect-changed` naming each requirement the decision record changes (the [documentation tools](../../tools/docs/README.md)); and its impact is identified (ARCH-033). Where a gap can be closed without rewording, a new requirement that names the one it extends is preferred, so that what was approved stays as it was |
   | Rule 2 ("DRAFTING IS NOT APPROVAL"); Rule 4, provenance; Rule 15, the owner decision gate | A drafted requirement becomes authoritative only through a decision record that names its source, after Rule 23's report. The source is an owner decision, or an established rule that already determines the requirement (the [quality directive](../builder/quality-consistency-and-correction-directive.md), §2 and §6), and it is the requirement's provenance. A requirement that neither determines goes to the owner (Rule 15; owner decisions 17: a new requirement is among the matters for which the owner's decision is requested) |
   | Rule 18, three verification passes | DEC-033's three gates, as DEC-039 and DEC-045 apply them: the one procedure (DUP-39), not another |
   | Rule 20, "the project's existing lifecycle" | GOV-024's canonical feature lifecycle ([architecture governance](../architecture/architecture-governance.md)); Rule 20's steps are the work done through its states, not a second lifecycle |
   | Rule 23, the final reconciliation report | Made in the record that drafts the batch, before the decision record that makes the batch authoritative |

3. **The owner's other rule sets stay in force through their decision records and are not loaded as builder texts.** The [owner rule sets reconciliation](../traceability/owner-rule-sets-reconciliation.md) maps every rule of owner decisions 14, 15, and 17. It finds each one stated in a builder text, or applied by an existing mechanism or by the decision record that applies the rule set. The convergence audit (section 9) had done the same for owner decisions 13's lasting rules, and DEC-042 applies owner decisions 10's lifecycle.
   - Their real gaps are handled in existing mechanisms or in the steps already scheduled. Owner decisions 14's document classes (§6) are handled in this change, in the [documentation index](../README.md). The rest go to OQ-31, which the owner answered the same day ([DEC-052](DEC-052-apply-owner-answers-on-order-of-work-and-backups.md), decision 3); item 5; U7's matrix at checkpoint D; and X9 and X10 at Stage 1's exit.
   - Loading these rule sets in full would state most of their rules twice. That is what owner decisions 9 (Rules 3 and 16) and owner decisions 17 ("THE OBJECTIVE IS NOT MORE RULES.") ask the project not to do.
   - So each stays in force through its record, as that record applies it, together with the six builder texts; where they differ, the stricter applies (DEC-033). Where a record said it applied its rule set until this step, it now applies it without an end. The records are: owner decisions 10's lifecycle, DEC-042; owner decisions 13, DEC-045; owner decisions 14, DEC-046; owner decisions 15, DEC-047; owner decisions 17, DEC-048.
   - Their texts stay preserved as the sources those records apply. `CLAUDE.md` names them, so that every session finds them.
4. **The draft is superseded and retired.** Its reading notes are kept in decision 2. Its copy of the rules, its number, and its script are superseded by this record.
   - Owner decisions 10's terminal state SUPERSEDED AND RETIRED applies, as DEC-046 (decision 5) applies those states to drafts.
   - It stays in [`docs/drafts/`](../drafts/README.md), labelled, as the record of where this step started; it is never a source. The drafts index records its disposition.

## Alternatives considered

- **A copy of the rules in `docs/builder/`, as the draft made.** Rejected: it would be a second copy of a preserved text (owner decisions 15, §8; DEC-047, decision 3).
- **Moving the preserved file to `docs/builder/`.** Not chosen. Four dated records link to its path: DEC-042, DEC-044, DEC-048, and the checkpoint B verification record. Decision records are not rewritten (DEC-037). The file's banner says what it now is.
- **Loading owner decisions 10, 13, 14, 15, and 17 as builder texts too.** Not chosen. The mapping finds their rules already stated or applied, and each gap handled where it belongs. Loading them would state most rules twice. They stay in force through their records.
- **Applying owner decisions 9 through this record only, without loading it.** Not chosen. Its adoption as a builder text is the approved step (DEC-042, decision 2; the project state's item 3). The owner sent it as permanent builder rules for all requirement drafting, which items 4 and 5 will do.

## Consequences

- **`CLAUDE.md`** loads six builder texts and names the rule sets that stay in force through their records.
- **Six texts are named** by the root README, the documentation index, [architecture governance](../architecture/architecture-governance.md), the [source-of-truth map](../architecture/source-of-truth-map.md), and the banners of the master execution constitution and the quality directive.
- **Banners:** owner decisions 9's reads ACTIVE; owner decisions 14 and 15's name this record.
- **The documentation index** says which of its labels is each of owner decisions 14's document classes (§6).
- **The glossary** gains the reconciliation categories, DISTINCT from requirement classes.
- **"Later changes" lines:**
  - DEC-033 and DEC-039 note the sixth text;
  - DEC-042, DEC-044, DEC-045, DEC-046, DEC-047, and DEC-048 point here.
- **The drafts index** records the draft as SUPERSEDED AND RETIRED, and the draft's banner says so.
- **No requirement, system rule, gate, or code changes.** Nothing here authorizes work beyond [DEC-038](DEC-038-stage-1-plan-approved.md)'s Stage 1.
