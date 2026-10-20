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
- **This change's backup** (DEC-052, decision 3): `claude/unverified-backup-item-3`, pushed after Gate 3 run 1 failed, at `1f5bdb7` with the copy that run reviewed, and again with the tree committed after run 1's fixes. Its reconciliation with this change's commit, its archive branch, and the deletion are recorded by checkpoint C's record.
- **The draft item 3 started from** ([draft](../drafts/draft-adoption-of-owner-decisions-09.md), DEC-046, decision 5): read first and compared with the canonical records. Its reading notes are kept in DEC-051's decision 2, with what the decisions since have added. Its copy of the rules is superseded: it would be a second copy of a preserved text (owner decisions 15, §8). So are its number, DEC-042, since used, and its script, which edited files as they stood on 2026-10-12.
- **Out of scope:** platform code, configuration, and requirements (none changed); items 4 to 6 of "Next approved step".
- **The owner's messages after the last one the previous record names** (the [earlier Gate 3 reports verification](gate-3-reports-verification.md), whose list ends with "Try again" of 2026-10-20, 21:44 UTC), up to the copy that this record's last Gate 3 run reviews: the message of 22:04 UTC, and the answers of 22:26 and 22:28 UTC to the builder's questions. All are preserved word for word in this change, as owner decisions 20 (DEC-052).

## Checks

| Check | Command or method | Result |
|---|---|---|
| Documentation checker | `python3 tools/docs/build_index.py --check-only` | Exit 0 |
| Documentation tools self-test | `python3 tools/docs/selftest.py` | PASS |
| No requirement changed | `python3 tools/docs/compare_requirements.py af177dd --strict` | 0 added, removed, or changed |
| Round trip of owner decisions 20 | The typed message taken by script from its user turn in the session record (2026-10-20, 22:04:49 UTC), and each answer from the record of the builder's questions (22:26:30 and 22:28:54 UTC), each compared with its text block; the questions and options compared with the questions as asked; the file's manifest line computed by the checker's rule; the script composes the file, and its output is byte-identical to the committed file (`cmp`) | The message (416 characters) and the three answers (Q1 457, Q2 380, and Q3 35 characters) identical to their text blocks; the questions and options identical to those asked; the manifest line, `6e50c998…`, the one the checker computes |
| Preserved texts | The manifest gains only owner decisions 20's line; under `docs/handoffs/` and `docs/builder/`, only the five banners named in the Scope change, and owner decisions 20 is added | As stated: one manifest line added; each of the five banners changed on its line 3 only; owner decisions 20 added |
| Whitespace | `git diff --check` | Nothing reported |
| Repository tests | `uv run --locked pytest tests/repository` | 295 passed |
| Lint, format, and types of the tools | `uv run --locked ruff check`; `uv run --locked ruff format --check`; `uv run --locked mypy --config-file tools/docs/mypy.ini` | Pass |
| `CLAUDE.md` loads six texts | Each `@` line of `CLAUDE.md` names an existing file; the six are the five under `docs/builder/` and owner decisions 9 | Six `@` lines, each an existing file: the five builder texts and owner decisions 9 |
| The mapping's citations | A script lists every constitution Rule, master execution constitution section, quality directive section, and owner decisions 9 Rule that the reconciliation's second column cites, with that rule's heading, and each heading is read against its row; each decision and mechanism the third and fourth columns cite is read where it is defined | Each says what its row claims |
| The mapping's coverage | A script lists the numbered sections of owner decisions 14 (1 to 41) and 15 (1 to 31) and the fourteen framed headings of owner decisions 17, and finds each in the mapping's first column, by number or by exact heading; the rest read by hand: five headings of owner decisions 17 named there in other words, and the unnumbered parts of the three texts | All covered |
| TODO markers (owner decisions 14, §34) | `git grep -nE "TODO\|FIXME\|XXX\|HACK" -- src tests tools contracts pyproject.toml .github` | None |
| The branches on GitHub | `git ls-remote origin` | `claude/archive/unverified-backup-checkpoint-b` and `claude/unverified-backup-checkpoint-b` both at `ee84f26`; `claude/code-builder-constitution-rrewgf` at `af177dd`; `claude/unverified-backup-item-3`, this change's backup (Scope) |

## Gates

- **Gate 1:** the checks above.
- **Gate 2:** by the builder, under Rule 0 ([DEC-048](../decisions/DEC-048-preserve-and-apply-rule-0.md)):
  - One copy of each text. Owner decisions 9 is loaded from its preserved copy; no second copy is made.
  - No parallel rule text. The owner's other rule sets are mapped, not loaded. Each of their gaps is handled in an existing mechanism or a scheduled step, and the one handled here, the document classes, reinforces the documentation index's labels table.
  - Owner decisions 20 is preserved through the existing mechanism, as owner decisions 18 and 19 were: a HISTORICAL text under `docs/handoffs/`, its manifest line, and its decision record. DEC-052 applies the owner's answers through the existing records: the project state's order of work, the open-question register, owner decisions 10's lifecycle for backups, and "Later changes" lines.
  - No requirement, system rule, gate, or code changed.
- **Gate 3:** an independent reviewer, a separate agent started with a fresh context, on a push-disabled copy of the repository at `af177dd` with the change applied, identified by the hash of its `git diff`. Its brief gave DEC-045's decision 2 for severity: blocking only with the provenance violated, or a statement shown false or overstated; everything else non-blocking or optional. Findings are numbered A1, A2, and so on.
  - **The baseline** the brief named: for item 3, the project state's item 3 at `af177dd` and the questions that DEC-042 (decisions 2 and 7), DEC-044 (decision 4), DEC-045 (decision 9), DEC-046 (decision 2), DEC-047 (decision 2), and DEC-048 (decision 2) each leave to it, and DEC-046 (decision 5) and DEC-047 (decision 3) for its draft; for the owner's answers, owner decisions 20 and OQ-31 as the register stated it at `af177dd`; owner decisions 9, 10, 13, 14, 15, 17, and 20, and the five builder texts; DEC-033; DEC-037; the tools README's rule on preserved texts; DEC-004 and DEC-047 (decision 7); DEC-045 (decisions 1 to 7); the traceability README, DEC-048, and DEC-049 (decision 3); the Stage 1 plan's sections 5, 8, and 9 (item 4); the project state at `af177dd` and the branches on GitHub. "Out of scope: whether the owner's rules or answers are wise; items 4 to 6."
  - **Run 1** (copy `930ba8c1fd47…`): a reviewer launched on 2026-10-20 at 22:42 UTC, which reported at 23:01 UTC. **FAIL**: blocking A1 to A3; non-blocking A4 to A6; optional A7 to A9. Its report opens: "The adoption is sound: `CLAUDE.md` loads six existing files and there is no second copy of any text."
  - **The builder's own separate pass:** Gate 2 above.
  - **Blocking findings per run:** three in run 1; none caused by fixes or reopened.

| ID | Run | Finding and evidence | Class (owner decisions 13, §6) | Severity | Relation (§5) | Provenance | Fix | Status |
|---|---|---|---|---|---|---|---|---|
| A1 | 1 | The project state gave only the first of DEC-052 decision 3's two triggers of a backup, a failed first Gate 3 run, in three places; the second, a session that would end with the work uncommitted, was only in DEC-052 | Documentation issue (incomplete; continuity) | Blocking | New | DEC-045, decision 2: a continuity gap; it narrowed DEC-052 decision 3 and the owner's answer to OQ-31 (owner decisions 20) | Both triggers, in the three places, in the wording the review specified | Fixed |
| A2 | 1 | The owner rule sets reconciliation said owner decisions 10 is applied to checkpoint B's backup with "its retention under an archive tag"; DEC-052 decision 4 replaced the tag with an archive branch, which exists on GitHub | Documentation issue (stale) | Blocking | New | DEC-045, decision 2; DEC-052, decision 4 | "its retention: under an archive tag (DEC-043) until 2026-10-20, when the owner chose an archive branch instead (DEC-052, decision 4)" | Fixed |
| A3 | 1 | DEC-048's decisions 4 and 5 leave OQ-31 with the owner, to be asked before checkpoint C; the "Later changes" line this change added to DEC-048 named only DEC-051, and DEC-052's Consequences left DEC-048 out | Documentation issue (incomplete; continuity) | Blocking | New | The brief's check 6 (a record still saying OQ-31 is open); DEC-037 | DEC-048's line names the owner's answer and the new order; DEC-052's Consequences name DEC-048 | Fixed |
| A4 | 1 | DEC-051 decision 2 prefers, where a gap can be closed without rewording, a new requirement that names the one it extends; owner decisions 9's Rule 16 makes strengthening the existing control the default. The reviewer judged the reading defensible (Rule 9) but would make it differently | Non-blocking improvement | Non-blocking | New | — | The reviewer's wording, which changes a decision, so it is applied by a "Later changes" line on DEC-051 in its own change (DEC-045, decisions 5 and 7) | Open: settled before any requirement is drafted or refined under that reading, and before item 4 at the latest (the project state's "Non-blocking findings") |
| A5 | 1 | DEC-052 decision 3 left out a step of the option the owner chose ("verify it"; owner decisions 20); owner decisions 15's §16 also asks for the check | Documentation issue (incomplete) | Non-blocking | New | — | "checks the archive branch on GitHub at that commit": it restores the owner's chosen option, so it changes no decision or owner answer | Fixed |
| A6 | 1 | The round-trip row gave the answers' lengths in the session record's order, not the file's, and did not say that the script composes the file and that its output was compared with the committed file | Documentation issue (incomplete) | Non-blocking | New | — | The lengths by question, and the comparison (`cmp`) | Fixed |
| A7 | 1 | DEC-052's "Decided by" did not name the builder's reading of the chosen option's "final exit report" as the exit reports X9 and X10, and the stage record did not place items 4 and 5 before X9 | Non-blocking improvement | Optional | New | — | Both, in the wording the review specified | Fixed |
| A8 | 1 | The project state's "Blockers" row generalized from one branch: "This environment refuses to delete branches" | Non-blocking improvement | Optional | New | — | "This environment refused to delete the branch of checkpoint B's backup" | Fixed |
| A9 | 1 | The drafts index labels the whole draft SUPERSEDED AND RETIRED, though its reading notes were kept in DEC-051, as its disposition says | Non-blocking improvement | Optional | New | — | Suggested only if DEC-051 is reopened for A4 | Not applied: DEC-051 is not reopened in this change |

## Failures and fixes

| Failure | Cause | Fix | Re-run |
|---|---|---|---|
| Gate 3 run 1: three blocking findings (A1 to A3) | Statements of the current state not updated everywhere DEC-052 changed it: the project state, the reconciliation, and DEC-048 | A1 to A3, A5 to A8 above, in the wording run 1 specified; A4 open; A9 not applied. That wording changes no requirement, decision, owner answer, or verbatim text, so no further independent run was made ([DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md), decision 5) | None (DEC-045, decision 5) |

## Final status and remaining issues

**PASS**: Gate 1, Gate 2, and Gate 3. Gate 3 passed after run 1, whose findings were fixed in the wording it specified, without a further run (DEC-045, decision 5), on the tree that is committed apart from that wording and run 1's result. Three blocking findings, each new and fixed; none caused by fixes or reopened.

Remaining, each in its canonical place: items 4 to 6 of "Next approved step", in the owner's order (DEC-052); A4, open (above; the project state's "Non-blocking findings"); this change's backup, to be reconciled and archived after its commit (the project state's "Other branches"); the deletion of checkpoint B's backup branch, which this environment refused (the project state's "Blockers").

## Environment

System Python 3.11 for the documentation tools; uv, pytest, ruff, and mypy from the lockfile; git.
