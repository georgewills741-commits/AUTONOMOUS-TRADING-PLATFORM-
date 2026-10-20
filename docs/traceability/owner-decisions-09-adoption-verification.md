# Owner Decisions 9 Adoption and the Owner's Answers of 2026-10-20 — Verification Record

> **Status:** verification record of the change that adopts the owner's requirement drafting and anti-drift rules ([owner decisions 9](../handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md)) as the sixth builder text, records how they read, and keeps the owner's other rule sets in force through their decision records after mapping their rules ("Next approved step", item 3; [DEC-051](../decisions/DEC-051-adopt-requirement-drafting-and-anti-drift-rules.md)); and that preserves and applies the owner's answers of 2026-10-20 on the order of work and on backups ([owner decisions 20](../handoffs/owner-decisions-20-question-on-the-rules-order-of-work-and-backups.md); [DEC-052](../decisions/DEC-052-apply-owner-answers-on-order-of-work-and-backups.md)), with which item 1 is done as far as this environment allows. Format: [traceability README](README.md).

## Identity

- **Dates:** 2026-10-20
- **Stage:** 1 — FOUNDATION, after checkpoint B and the convergence audit, before checkpoint C
- **Starts from:** commit `af177dd` on branch `claude/code-builder-constitution-rrewgf`, equal to the remote. This record's own commit is entered in the project state's checkpoint log by the next checkpoint

## Scope

- **New:**
  - [DEC-051](../decisions/DEC-051-adopt-requirement-drafting-and-anti-drift-rules.md) and the [owner rule sets reconciliation](owner-rule-sets-reconciliation.md);
  - [owner decisions 20](../handoffs/owner-decisions-20-question-on-the-rules-order-of-work-and-backups.md) and [DEC-052](../decisions/DEC-052-apply-owner-answers-on-order-of-work-and-backups.md);
  - this record.
- **Changed:**
  - `CLAUDE.md`: six builder texts, owner decisions 9 loaded from its preserved copy, and the rule sets that stay in force through their decision records named;
  - the banners of owner decisions 9 (ACTIVE), 14, and 15, and of the master execution constitution and the quality directive. Banners only: no preserved text changed, and the manifest gains one line, owner decisions 20's;
  - the root README, the documentation index (the builder texts, the handoffs, the drafts, the traceability records, and which label is each of owner decisions 14's document classes), architecture governance, the source-of-truth map, and the glossary (reconciliation categories);
  - "Later changes" lines of DEC-033, DEC-039, DEC-042, DEC-043, DEC-044, DEC-045, DEC-046, DEC-047, and DEC-048, and the decision log;
  - the open-question register (OQ-31 RESOLVED) and the stage record (its "Blockers" row and its note on the certificate);
  - the drafts index and the draft of item 3 (SUPERSEDED AND RETIRED);
  - this directory's index and the project state.
- **On GitHub, as DEC-052 records (decision 4):** the branch `claude/archive/unverified-backup-checkpoint-b` pushed at `ee84f26`; the deletion of `claude/unverified-backup-checkpoint-b` refused by this environment, so that branch stays at `ee84f26`.
- **The draft item 3 started from** ([draft](../drafts/draft-adoption-of-owner-decisions-09.md), DEC-046, decision 5): read first and compared with the canonical records. Its reading notes are kept in DEC-051's decision 2, with what the decisions since have added. Its copy of the rules is superseded: it would be a second copy of a preserved text (owner decisions 15, §8). So are its number, DEC-042, since used, and its script, which edited files as they stood on 2026-10-12.
- **Out of scope:** platform code, configuration, and requirements (none changed); items 4 to 6 of "Next approved step".
- **The owner's messages after the last one the previous record names** (the [earlier Gate 3 reports verification](gate-3-reports-verification.md), whose list ends with "Try again" of 2026-10-20, 21:44 UTC), up to the copy that this record's last Gate 3 run reviews: the message of 22:04 UTC, and the answers of 22:26 and 22:28 UTC to the builder's questions. All are preserved word for word in this change, as owner decisions 20 (DEC-052).

## Checks

| Check | Command or method | Result |
|---|---|---|
| Documentation checker | `python3 tools/docs/build_index.py --check-only` | Exit 0 |
| Documentation tools self-test | `python3 tools/docs/selftest.py` | PASS |
| No requirement changed | `python3 tools/docs/compare_requirements.py af177dd --strict` | 0 added, removed, or changed |
| Round trip of owner decisions 20 | The typed message taken by script from its user turn in the session record (2026-10-20, 22:04:49 UTC), and each answer from the record of the builder's questions (22:26:30 and 22:28:54 UTC), each compared with its text block; the questions and options compared with the questions as asked; the file's manifest line computed by the checker's rule | The message (416 characters) and the three answers (380, 457, and 35 characters) identical to their text blocks; the questions and options identical to those asked; the manifest line, `6e50c998…`, the one the checker computes |
| Preserved texts | The manifest gains only owner decisions 20's line; under `docs/handoffs/` and `docs/builder/`, only the five banners named in the Scope change, and owner decisions 20 is added | As stated: one manifest line added; each of the five banners changed on its line 3 only; owner decisions 20 added |
| Whitespace | `git diff --check` | Nothing reported |
| Repository tests | `uv run --locked pytest tests/repository` | 295 passed |
| Lint, format, and types of the tools | `uv run --locked ruff check`; `uv run --locked ruff format --check`; `uv run --locked mypy --config-file tools/docs/mypy.ini` | Pass |
| `CLAUDE.md` loads six texts | Each `@` line of `CLAUDE.md` names an existing file; the six are the five under `docs/builder/` and owner decisions 9 | Six `@` lines, each an existing file: the five builder texts and owner decisions 9 |
| The mapping's citations | A script lists every constitution Rule, master execution constitution section, quality directive section, and owner decisions 9 Rule that the reconciliation's second column cites, with that rule's heading, and each heading is read against its row; each decision and mechanism the third and fourth columns cite is read where it is defined | Each says what its row claims |
| The mapping's coverage | A script lists the numbered sections of owner decisions 14 (1 to 41) and 15 (1 to 31) and the fourteen framed headings of owner decisions 17, and finds each in the mapping's first column, by number or by exact heading; the rest read by hand: five headings of owner decisions 17 named there in other words, and the unnumbered parts of the three texts | All covered |
| TODO markers (owner decisions 14, §34) | `git grep -nE "TODO\|FIXME\|XXX\|HACK" -- src tests tools contracts pyproject.toml .github` | None |
| The branches on GitHub | `git ls-remote origin` | `claude/archive/unverified-backup-checkpoint-b` and `claude/unverified-backup-checkpoint-b` both at `ee84f26`; `claude/code-builder-constitution-rrewgf` at `af177dd` |

## Gates

- **Gate 1:** the checks above.
- **Gate 2:** by the builder, under Rule 0 ([DEC-048](../decisions/DEC-048-preserve-and-apply-rule-0.md)):
  - One copy of each text. Owner decisions 9 is loaded from its preserved copy; no second copy is made.
  - No parallel rule text. The owner's other rule sets are mapped, not loaded. Each of their gaps is handled in an existing mechanism or a scheduled step, and the one handled here, the document classes, reinforces the documentation index's labels table.
  - Owner decisions 20 is preserved through the existing mechanism, as owner decisions 18 and 19 were: a HISTORICAL text under `docs/handoffs/`, its manifest line, and its decision record. DEC-052 applies the owner's answers through the existing records: the project state's order of work, the open-question register, owner decisions 10's lifecycle for backups, and "Later changes" lines.
  - No requirement, system rule, gate, or code changed.
- **Gate 3:** PENDING.

## Failures and fixes

None yet.

## Final status and remaining issues

**IN VERIFICATION** until the last Gate 3 run reports.

Remaining, each in its canonical place: items 4 to 6 of "Next approved step", in the owner's order (DEC-052); the deletion of checkpoint B's backup branch, which this environment refuses (the project state's "Blockers").

## Environment

System Python 3.11 for the documentation tools; uv, pytest, ruff, and mypy from the lockfile; git.
