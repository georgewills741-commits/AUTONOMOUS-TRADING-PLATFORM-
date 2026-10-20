# Draft — The Adoption of Owner Decisions 9

> **Status:** DRAFT — NOT APPROVED, NOT AUTHORITATIVE, NOT VERIFIED, NOT PRODUCTION-READY. The builder's unverified work for item 3 of the [project state](../project-state.md)'s "Next approved step" (the adoption of [owner decisions 9](../handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md) as a builder text), made on 2026-10-07 and 2026-10-12 in the builder's session workspace, never reviewed, and kept only there until DEC-047 (decision 3) had it committed as a draft. Nothing in it is decided or in force, and it predates owner decisions 10 to 15 and DEC-042 to DEC-047. It is committed as a draft under [owner decisions 15](../handoffs/owner-decisions-15-stage-transition-persistence-and-commit-integrity.md) (§1, §7, §8), as [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md) (decision 3) decides; [DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md) (decision 5) classifies it. Each file is kept in a text block, so nothing in it defines or changes a requirement, decision, or record.
>
> **Disposition:** SUPERSEDED AND RETIRED on 2026-10-20 by [DEC-051](../decisions/DEC-051-adopt-requirement-drafting-and-anti-drift-rules.md), which item 3 wrote after comparing this draft with the canonical records: its reading notes are kept in DEC-051's decision 2; its copy of the rules (a second copy of a preserved text), its number (DEC-042, since used), and its script are superseded ([drafts index](README.md)). Until then: COMMITTED AS DRAFT. A Gate 3 brief written for it on 2026-10-12 was never used and is not kept.

## The draft builder text

A copy of owner decisions 9 drafted as a builder text for `docs/builder/`. Its body, the rules in a text block, is the text of [owner decisions 9](../handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md) exactly (the same 23,757 characters), so only its title and banner, which are the draft's own, are kept here (owner decisions 15, §8: no second copy of a source). The banner calls the text adopted; it never was. Original: 25,216 bytes, sha256 `def73ae6ce2dca5e34ef0163d143b8212753089e229eb2fec9f56bf197d4e2de`.

```text
# Canonical Requirement Drafting and Anti-Drift Rules

> **Status:** ACTIVE — permanent builder rules set by the project owner on 2026-10-07, during Stage 1, while checkpoint B was in its third verification gate. Adopted by [DEC-042](../decisions/DEC-042-adopt-requirement-drafting-and-anti-drift-rules.md) and loaded into every Claude Code session through `CLAUDE.md`, together with the [builder constitution](claude-code-builder-constitution.md), the [checkpoint and verification rule](checkpoint-and-verification-rule.md), the [master execution constitution](master-execution-constitution.md), the [directive on verification and platform independence](verification-and-platform-independence-directive.md), and the [quality, consistency, verification and correction directive](quality-consistency-and-correction-directive.md). All six apply; where they differ, the stricter applies (DEC-033). As its own text says, it reinforces the existing rules and replaces none of them.
>
> **Formatting note:** the rules are reproduced inside one text block exactly as received, so that their lines, separator lines, lists, and arrows stay as they were sent. Nothing was added, removed, or changed in them. The title and this banner are the builder's.
```

## The draft decision record

The decision record that would have adopted it, numbered DEC-042 in the draft; that number has since been used for another decision. Original: 4,597 bytes, sha256 `9bfb9947ed9a1bd000ce51b63e2bfe7c1bedc2e9b6f2ce0535fd9e99d688d05a`.

```text
# DEC-042 — Adopt the owner's canonical requirement drafting and anti-drift rules; six builder texts

- **Status:** ACCEPTED
- **Date:** 2026-10-12
- **Decided by:** project owner (rules sent on 2026-10-07, "PERMANENT BUILDER RULES"); the builder's: how they combine with the five other builder texts, and the readings below

## Context

On 2026-10-07, during Stage 1, while checkpoint B was in its third verification gate, the owner sent the "Canonical Requirement Drafting & Anti-Drift Rules": thirty-one rules (Rule 0 to Rule 30), marked permanent, continuous, mandatory, and non-optional, that govern all future requirement drafting, reconciliation, architecture, implementation, and evolution. They say they replace none of the existing rules: where an existing project rule covers a situation it remains authoritative, and the new rules reinforce, connect, and enforce the existing ones.

Five builder texts were in force, loaded by `CLAUDE.md` ([DEC-001](DEC-001-adopt-builder-constitution.md), [DEC-032](DEC-032-adopt-checkpoint-and-verification-rule.md), [DEC-033](DEC-033-adopt-master-execution-constitution.md), [DEC-034](DEC-034-verification-and-platform-independence.md), [DEC-039](DEC-039-adopt-quality-and-correction-directive.md)); DEC-033 fixes how they combine: all apply, and where they differ the stricter applies.

## Decision

1. **Adopted as the sixth builder text,** preserved word for word as [`docs/builder/requirement-drafting-and-anti-drift-rules.md`](../builder/requirement-drafting-and-anti-drift-rules.md), listed in the preserved-text manifest, and loaded in every session by `CLAUDE.md`.
2. **How it combines.** DEC-033's rule stays: all six texts apply, and where they differ the stricter applies. The new text's own "existing rule remains authoritative" fits that rule: it adds requirements on top of the existing ones (for example, a final reconciliation report before drafted requirements become authoritative, Rule 23) and loosens none.
3. **No requirement, decision, or document is changed by adopting it.** Its rules apply from now on, first to the audit the owner asked for on the same day ([owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md)), whose drafted requirements go through the rules' classification (Rule 8) and final reconciliation report (Rule 23) before they become authoritative.

## Reading notes (builder)

| Phrase | Reading |
|---|---|
| "Global Trading Constitution" (Rule 1) | The project has no document of that name. As for DEC-032's "Global Game Constitution equivalent", it is read as the platform principles index (ARCH-028, in the [platform overview](../product/platform-overview.md)) with the [System Rules Register](../requirements/system-rules-register.md) |
| Rule 8's categories (EXISTING REQUIREMENT, REFINED EXISTING REQUIREMENT, NEW CONFIRMED REQUIREMENT, PROPOSAL, …) | Outcomes of reconciling a drafted item, recorded in the reconciliation or audit record that drafts it. They do not replace the requirement classes of ARCH-015, which a requirement keeps in its specification line; a NEW CONFIRMED REQUIREMENT, for example, is written with the class its wording calls for (a CONSTRAINT for a prohibition) |
| "REFINED EXISTING REQUIREMENT" | Changing an existing requirement's text needs a decision record and shows in the requirement comparison (`--expect-changed`), as before (ARCH-033). Where a gap can be closed without rewording, a new requirement that names the one it extends ("In addition to …") remains the project's way, which also avoids changing what was approved |
| Rule 2, "drafting is not approval" | A requirement becomes authoritative only through a decision record that names its source: an owner decision, or an established rule that already determines it (the quality directive's §6). Its provenance (Rule 4) is that source |

## Alternatives considered

- **Keep the rules only as guidance in the session.** Rejected: the owner marked them permanent, and the repository is the project's memory (master execution constitution §01, §90).
- **Merge them into an existing builder text.** Rejected: preserved texts are never changed (DEC-004); a separate text with its own banner keeps each source exact.

## Consequences

- `CLAUDE.md` loads six builder texts; the manifest of preserved texts has a line for this one.
- The banners of the other builder texts that list their companions name this one too (a banner may change by decision; the texts do not).
- No requirement changes, so the requirement comparison shows nothing added, removed, or changed.
```

## The draft script

The script that would have applied the adoption to `CLAUDE.md`, the builder's directory, the decision log, and the project state; never run on the repository. Original: 9,713 bytes, sha256 `e27c99516b030207ccd3e2e6f9f5b3fac82173ec46dcc1749e808b35027bd2e1`.

```text
"""Apply DEC-042: adopt the owner's canonical requirement drafting and anti-drift rules.

Run from the repository root. Every replacement must match exactly once.
"""

import pathlib
import shutil
import sys

ROOT = pathlib.Path.cwd()
ADOPT = pathlib.Path(__file__).parent
TEXT = "requirement-drafting-and-anti-drift-rules.md"
DEC = "DEC-042-adopt-requirement-drafting-and-anti-drift-rules.md"


def replace(path: str, old: str, new: str) -> None:
    file = ROOT / path
    content = file.read_text(encoding="utf-8")
    count = content.count(old)
    if count != 1:
        sys.exit(f"{path}: expected one match, found {count}: {old[:80]!r}")
    file.write_text(content.replace(old, new), encoding="utf-8")


shutil.copyfile(ADOPT / TEXT, ROOT / "docs/builder" / TEXT)
shutil.copyfile(ADOPT / DEC, ROOT / "docs/decisions" / DEC)

# CLAUDE.md: six texts, and the import.
replace(
    "CLAUDE.md",
    "Five builder texts govern all work",
    "Six builder texts govern all work",
)
replace(
    "CLAUDE.md",
    "@docs/builder/quality-consistency-and-correction-directive.md\n",
    "@docs/builder/quality-consistency-and-correction-directive.md\n\n"
    "The owner's canonical requirement drafting and anti-drift rules "
    f"([DEC-042](docs/decisions/{DEC})):\n\n"
    f"@docs/builder/{TEXT}\n",
)

replace(
    "README.md",
    "the four other builder texts are in the same directory, and `CLAUDE.md` loads all five",
    "the five other builder texts are in the same directory, and `CLAUDE.md` loads all six",
)

replace(
    "docs/README.md",
    "([DEC-039](decisions/DEC-039-adopt-quality-and-correction-directive.md)). All five are ACTIVE and loaded by `CLAUDE.md` |",
    "([DEC-039](decisions/DEC-039-adopt-quality-and-correction-directive.md)) · "
    f"[Requirement drafting and anti-drift rules](builder/{TEXT}): the owner's rules for drafting, "
    "classifying, and reconciling requirements before they become authoritative, and against drift "
    f"([DEC-042](decisions/{DEC})). All six are ACTIVE and loaded by `CLAUDE.md` |",
)

replace(
    "docs/architecture/architecture-governance.md",
    "The five builder texts loaded by `CLAUDE.md` (the [builder constitution](../builder/claude-code-builder-constitution.md), the [checkpoint and verification rule](../builder/checkpoint-and-verification-rule.md), the [master execution constitution](../builder/master-execution-constitution.md), the [directive on verification and platform independence](../builder/verification-and-platform-independence-directive.md), and the [quality, consistency, verification and correction directive](../builder/quality-consistency-and-correction-directive.md))",
    "The six builder texts loaded by `CLAUDE.md` (the [builder constitution](../builder/claude-code-builder-constitution.md), the [checkpoint and verification rule](../builder/checkpoint-and-verification-rule.md), the [master execution constitution](../builder/master-execution-constitution.md), the [directive on verification and platform independence](../builder/verification-and-platform-independence-directive.md), the [quality, consistency, verification and correction directive](../builder/quality-consistency-and-correction-directive.md), and the [requirement drafting and anti-drift rules](../builder/"
    + TEXT
    + "))",
)

replace(
    "docs/decisions/DEC-033-adopt-master-execution-constitution.md",
    "- **Later changes:** Since 2026-10-06 five builder texts apply: the owner's quality, consistency, verification and correction directive was added ([DEC-039](DEC-039-adopt-quality-and-correction-directive.md)).",
    "- **Later changes:** Since 2026-10-06 five builder texts apply: the owner's quality, consistency, verification and correction directive was added ([DEC-039](DEC-039-adopt-quality-and-correction-directive.md)). Since 2026-10-12 six apply: the owner's canonical requirement drafting and anti-drift rules, sent on 2026-10-07, were added ([DEC-042]("
    + DEC
    + ")); this decision's rule for how the texts combine is unchanged.",
)

replace(
    "docs/decisions/DEC-039-adopt-quality-and-correction-directive.md",
    "- **Text:** [`docs/builder/quality-consistency-and-correction-directive.md`](../builder/quality-consistency-and-correction-directive.md) (verbatim, ACTIVE)\n",
    "- **Text:** [`docs/builder/quality-consistency-and-correction-directive.md`](../builder/quality-consistency-and-correction-directive.md) (verbatim, ACTIVE)\n"
    "- **Later changes:** Since 2026-10-12 six builder texts apply: the owner's canonical requirement drafting and anti-drift rules, sent on 2026-10-07, were added ([DEC-042]("
    + DEC
    + ")). Nothing in this decision changes.\n",
)

replace(
    "docs/builder/master-execution-constitution.md",
    "and, since 2026-10-06, the owner's [quality, consistency, verification and correction directive](quality-consistency-and-correction-directive.md) ([DEC-039](../decisions/DEC-039-adopt-quality-and-correction-directive.md)). All five apply; where they differ, the stricter applies (DEC-033).",
    "since 2026-10-06, the owner's [quality, consistency, verification and correction directive](quality-consistency-and-correction-directive.md) ([DEC-039](../decisions/DEC-039-adopt-quality-and-correction-directive.md)), and, since 2026-10-12, the owner's [canonical requirement drafting and anti-drift rules]("
    + TEXT
    + ") ([DEC-042](../decisions/"
    + DEC
    + ")). All six apply; where they differ, the stricter applies (DEC-033).",
)

replace(
    "docs/builder/quality-consistency-and-correction-directive.md",
    "and the [directive on verification and platform independence](verification-and-platform-independence-directive.md). All five apply; where they differ, the stricter applies (DEC-033, DEC-039).",
    "the [directive on verification and platform independence](verification-and-platform-independence-directive.md), and, since 2026-10-12, the owner's [canonical requirement drafting and anti-drift rules]("
    + TEXT
    + ") ([DEC-042](../decisions/"
    + DEC
    + ")). All six apply; where they differ, the stricter applies (DEC-033, DEC-039).",
)

replace(
    "docs/architecture/source-of-truth-map.md",
    "| How the builder texts combine; the one three-gate procedure | [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md) (DUP-39); what each gate covers now that code exists: [DEC-039](../decisions/DEC-039-adopt-quality-and-correction-directive.md) |",
    "| Owner's canonical requirement drafting and anti-drift rules | [docs/builder/"
    + TEXT
    + "](../builder/"
    + TEXT
    + ") ([DEC-042](../decisions/"
    + DEC
    + ")) |\n"
    "| How the builder texts combine; the one three-gate procedure | [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md) (DUP-39); what each gate covers now that code exists: [DEC-039](../decisions/DEC-039-adopt-quality-and-correction-directive.md); how the drafting rules' categories relate to requirement classes: [DEC-042](../decisions/"
    + DEC
    + ") |",
)

replace(
    "docs/decisions/README.md",
    "| Builder (preservation, [DEC-004](DEC-004-preserve-original-handoffs.md), [DEC-032](DEC-032-adopt-checkpoint-and-verification-rule.md)); the directive itself is the owner's | ACCEPTED |\n",
    "| Builder (preservation, [DEC-004](DEC-004-preserve-original-handoffs.md), [DEC-032](DEC-032-adopt-checkpoint-and-verification-rule.md)); the directive itself is the owner's | ACCEPTED |\n"
    f"| [DEC-042]({DEC}) | Adopt the owner's canonical requirement drafting and anti-drift rules; six builder texts; how their categories relate to requirement classes | Owner (rules sent on 2026-10-07); builder (how the texts combine, reading notes) | ACCEPTED |\n",
)

replace(
    "docs/glossary.md",
    "on 2026-10-07 with DEC-040 (PROPOSED as a feature state), and on 2026-10-07 by Stage 1's checkpoint B (outcome and risk outcome).",
    "on 2026-10-07 with DEC-040 (PROPOSED as a feature state), on 2026-10-07 by Stage 1's checkpoint B (outcome and risk outcome), and on 2026-10-12 with DEC-042 (reconciliation categories).",
)
replace(
    "docs/glossary.md",
    "| DISTINCT ([DEC-039](decisions/DEC-039-adopt-quality-and-correction-directive.md)) | [DEC-039](decisions/DEC-039-adopt-quality-and-correction-directive.md); [documentation index](README.md) |\n",
    "| DISTINCT ([DEC-039](decisions/DEC-039-adopt-quality-and-correction-directive.md)) | [DEC-039](decisions/DEC-039-adopt-quality-and-correction-directive.md); [documentation index](README.md) |\n"
    "| Reconciliation categories | The outcome of reconciling a drafted item, from Rule 8 of the owner's [requirement drafting and anti-drift rules](builder/"
    + TEXT
    + ") (EXISTING REQUIREMENT, REFINED EXISTING REQUIREMENT, NEW CONFIRMED REQUIREMENT, PROPOSAL, RECOMMENDATION, FUTURE CAPABILITY, OPEN QUESTION, REQUIRES OWNER DECISION, DEPRECATED, SUPERSEDED, UNNECESSARY/REJECTED), recorded in the record that drafts the item. They are not requirement classes: a requirement keeps its ARCH-015 class in its specification line, and a NEW CONFIRMED REQUIREMENT is written with the class its wording calls for | — | DISTINCT ([DEC-042](decisions/"
    + DEC
    + ")) | [DEC-042](decisions/"
    + DEC
    + "); [requirements README](requirements/README.md) |\n",
)

# The hash the checker reports, recomputed independently from the banner rule.
replace(
    "tools/docs/preserved-texts.sha256",
    "  docs/builder/quality-consistency-and-correction-directive.md\n",
    "  docs/builder/quality-consistency-and-correction-directive.md\n"
    "ba36fd787e5d4352ce7651b503d7c88db01df5f65cf01b62bfde05eaaaa0ddcd  docs/builder/"
    + TEXT
    + "\n",
)

print("applied")
```
