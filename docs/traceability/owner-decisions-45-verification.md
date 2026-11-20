# Owner Decisions 45 Verification — The Server's Work, and an Evidence Pack on Three Exchanges' Terms

> **Status:** ACTIVE record of the change that preserves the owner's messages of 2026-11-20, 12:33 and 16:04 UTC, the second with an evidence pack on the terms of Binance, Bybit, and Coinbase ([owner decisions 45](../handoffs/owner-decisions-45-server-work-question-and-exchange-terms-evidence-pack.md); [the pack](../handoffs/owner-decisions-45-exchange-terms-evidence-pack-2026-11-20.pdf)), records the pack under OQ-34 ([DEC-078](../decisions/DEC-078-owner-messages-and-exchange-terms-evidence-pack.md)), and reconciles the backup commits of the change that builds checkpoint B's first increment (U5) with its commit, `7597a62` ([DEC-071](../decisions/DEC-071-one-reusable-backup-branch.md), decision 4). Its three gates: "Final status and remaining issues". Format: [traceability README](README.md).

## Identity

- **Date:** 2026-11-20.
- **Stage:** Stage 2 (DATA FOUNDATION). This change records the owner's messages and evidence; it changes documentation only, builds nothing, buys nothing, and contacts no venue endpoint: three of the venues' official legal pages were read once each.
- **Starts from:** commit `7597a62` on branch `claude/code-builder-constitution-rrewgf`, equal to the remote: the change that builds checkpoint B's first increment, U5 ([checkpoint B (U5) verification](stage-02-checkpoint-b-u5-verification.md)), whose machine checks passed ([run 44775556621](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/44775556621): the job `secrets` from 16:39:31 to 16:39:51 UTC and the job `checks` from 16:39:31 to 16:42:06 UTC, both passing; the only run for that commit). This record's own commit is the checkpoint log's row "The commit that adds this row", which the next change completes.
- **Temporary backup** ([DEC-057](../decisions/DEC-057-progress-continuity-no-loss-and-recovery.md), decision 4; DEC-071): the reusable branch `claude/unverified-backup-reusable`, reused after the eight checks below. This change's first backup commit, `4801465`, has as its parent `b8f0e3f`, the last backup commit of the change that builds U5, and was pushed at 16:50 UTC, by the command that wrote this change's first files; each later commit is a child of the branch's tip, pushed as a fast-forward and never forced. Each command that writes to the working tree runs the backup after its last write.

## Scope

**Added:** [owner decisions 45](../handoffs/owner-decisions-45-server-work-question-and-exchange-terms-evidence-pack.md), with the attached evidence pack beside it ([the pack](../handoffs/owner-decisions-45-exchange-terms-evidence-pack-2026-11-20.pdf)); [DEC-078](../decisions/DEC-078-owner-messages-and-exchange-terms-evidence-pack.md); this record.

**Changed:** the [Stage 2 record](stage-02-data-foundation.md) ("Venue verification for the operator's country": the pack's evidence, the reading of its new links, and the "Result"); the [open-question register](../open-questions/register.md) (OQ-34 narrowed again); the [project state](../project-state.md); the [decision log](../decisions/README.md) (DEC-078's row); the [documentation index](../README.md) and the [traceability README](README.md); the preserved-text manifest, `tools/docs/preserved-texts.sha256` (the two new files' lines).

**Requirements:** none added, removed, or changed (check 3).

**Out of scope:** U4's parts that need no venue's data, the next change; any venue's adapter, endpoint, or account; contacting an exchange, which the owner may do with the pack's five questions; the server.

**The owner's messages after the last one the previous record names** ([checkpoint B (U5) verification](stage-02-checkpoint-b-u5-verification.md), Scope: those delivered after its run 2's copy are the next record's), up to the copy that this record's last Gate 3 run reviews: the question queued at 12:07 UTC and delivered at 12:33 UTC, on the server's work, and the message of 16:04 UTC with the evidence pack, preserved as owner decisions 45 ([DEC-078](../decisions/DEC-078-owner-messages-and-exchange-terms-evidence-pack.md)). The notices of uncommitted changes at 12:33 UTC, twice, and at 16:07 UTC, the usage limit's notices of 12:34 and 13:04 UTC, the notice of the worker's restart at 13:04 UTC, the notices of background tasks, and the reports of Gate 3's reviewers and of the page-reading agent are the client's own.

## Checks

The change's own checks, on the working tree with this change: the documentation tools with the system Python 3.11, the [developer guide](../development.md)'s checks through `uv run --locked`, git, and GitHub's branch list and workflow runs.

| # | Check | How | Result |
|---|---|---|---|
| 1 | The documentation checker | `python3 tools/docs/build_index.py --check-only`, after `python3 tools/docs/build_index.py` | PASS: exit 0; 758 requirements; the generated files unchanged by this change |
| 2 | The documentation tools' self-test | `python3 tools/docs/selftest.py` | PASS: 62 cases, its two controls included |
| 3 | Requirements added, removed, or changed | `python3 tools/docs/compare_requirements.py 7597a62 --strict` | PASS: 758 requirements before and after; none added, removed, or changed |
| 4 | The developer guide's checks | `uv run --locked` with `ruff check`, `ruff format --check`, `mypy`, `mypy --config-file tools/docs/mypy.ini`, and `pytest` | PASS on 2026-11-20 from 16:53 to 16:57 UTC: each exits 0; 1,560 tests pass, the repository test for secrets among them, on a tree that holds the pack; no code or test changes |
| 5 | Hygiene of the change | `git diff --check 7597a62`, its new files included; a scan of the lines it adds for local paths, session or model identifiers, and the shapes of secrets | PASS on 2026-11-20 at 16:58 UTC: 11 files, 4 added and 7 changed, 169 lines added, the pack a binary file; `git diff --check` reports only lines 10 and 16 of owner decisions 45, the spaces that end the owner's two messages, kept as received (DEC-078, decision 1); the scan finds no local path, session or model identifier, or secret's shape |
| 6 | The preserved texts | The change's files against `7597a62`, its new files included, under `docs/handoffs` and `docs/builder`; owner decisions 45 compared by script with the session record, a block with the owner's recorded user turn of its minute, the words after the client's reference to the attached file where the turn begins with one, and the pack with the attached file by sha256 | PASS: the only files there are owner decisions 45 and the pack, added; its first message is in it byte for byte, 98 characters, with the space that ends it; its second, after the client's reference to the attached file, 57 characters, with the space that ends it; and the pack's sha256 equals the attached file's (`a67b9851…`) |
| 7 | Quotations | The quotation script on the lines this change adds to the documents; each quotation of a source outside the repository looked for in it | PASS: 20 distinct quotations in the lines this change adds to the documents, each found where it is quoted from: the owner's words `server jurisdiction` (owner decisions 41), in OQ-34, and `Continue`, `Try again`, and `Okay`, in the project state's lists of the session's stops, on lines this change rewrites; 15 names of sections, headings, or rows of the repository's documents; and the text between the two quotation marks that DEC-078 and owner decisions 45's banner show in code, which the script pairs and finds in that banner |
| 8 | The reusable branch | `git rev-list --parents` on the branch fetched from GitHub; the labels, record, trailers, and marker of each commit; GitHub's workflow runs for the branch and their jobs; GitHub's branch information | PASS: on 2026-11-20 at 16:58 UTC, 6 commits of this change, from `4801465`, on `b8f0e3f`, to `bb2cd9b`, each the child of the one before, each with the seven labels, the emergency checkpoint record, and both trailers, and none with the marker; GitHub ran the workflow on each push, 6 runs, each passing its job `secrets` with its job `checks` skipped; the branch is not protected. The commits after it, the one whose tree Gate 3's copy holds among them, are checked with the final status |
| 9 | Stale statements ([DEC-069](../decisions/DEC-069-owner-questions-and-efficiency-directive.md), decision 4) | The stale-statement script on the active documents, by subject: the last decision (`DEC-001 to`), the owner's messages and the pack (`owner decisions 4[45]`, `DEC-07[78]`, `evidence pack`), the backups' reconciliation (`holds the backup`, `7597a62`), the venues' status (`NOT VERIFIED`), and the next action (`U4's parts`, `Next safe action`); each line that states the current state read whole | PASS: each current statement of these subjects agrees with the change: owner decisions 45 and DEC-078 are named where owner decisions 44 and DEC-077 are, the decisions in effect run to DEC-078, the reusable branch's account names this change's backups and U5's as VERIFIED AND INCORPORATED in `7597a62`, OQ-34 and the project state's decisions pending name the pack, and U4's parts that need no venue's data are the next action |
| 10 | The new statements on the venues | DEC-078, the Stage 2 record's new paragraph and "Result", and OQ-34 read back, statement by statement, against the pack, the page-reading agent's report of 16:45 UTC, and the session record | PASS after one correction: each statement found in the pack, the page-reading agent's report, or the session record; DEC-078's account of the builder's answer of 16:07 UTC reworded to the answer's own terms ("Failures and fixes") |

The mutation check ([DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md), decision 6) does not apply: this change adds no code, test, or rule.

## Reconciliation of the last change's temporary backup

Owner decisions 10's eight checks, on the backup commits of the change that builds checkpoint B's first increment (U5), against its commit `7597a62`, before the reusable branch was used again ([DEC-071](../decisions/DEC-071-one-reusable-backup-branch.md), decision 4), on 2026-11-20 from 16:42:45 to 16:44:23 UTC. The branch held 33 commits after `18c6fcd`, the last commit the previous reconciliation checked: from `c9eed3e` (04:55 UTC) to `b8f0e3f` (16:37 UTC), each with a single parent, the one before it, and each with the seven labels, the emergency checkpoint record, and both trailers, and none with the marker.

| # | Check (owner decisions 10) | Evidence | Result |
|---|---|---|---|
| 1 | Every intended valid change is preserved | `7597a62`'s tree is `b8f0e3f`'s, `761b6cca` (`git diff --name-only`: no difference) | PASS |
| 2 | Corrections made during verification are preserved | The same tree: the fixes of that change's Gate 3 runs 1 and 2, and its record's account of them | PASS |
| 3 | No required work exists only on the temporary backup | Each of the 38 files the commits change against `18c6fcd`, whose tree is `af0d9a6`'s, is in `7597a62`; no file is in an intermediate commit and not in the last | PASS |
| 4 | No unverified or rejected implementation is accidentally promoted | `7597a62`'s parent is `af0d9a6`; none of the 33 commits is in its history or in that of `main`, at `7172a5c` | PASS |
| 5 | The authoritative branch contains the correct final state | On a fresh clone of the designated branch, at `7597a62` (16:42:51 UTC): the documentation checker and its self-test pass, and the requirement comparison with `af0d9a6` finds 758 requirements before and after, none added, removed, or changed | PASS |
| 6 | Required documentation and traceability are updated | `7597a62` holds that change's record with its final status, PASS for its gates, the checkpoint log's row, and its backup in the project state's "In progress, possibly partial", "Other branches", and "Next safe action" | PASS |
| 7 | The official verified checkpoint has been successfully pushed | `7597a62` is the tip of the remote designated branch, and the machine checks passed on it ([run 44775556621](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/44775556621), triggered by its push: both jobs passing) | PASS |
| 8 | Repository status is clean and consistent | `git status --porcelain` printed nothing at `7597a62` (16:43:47 UTC) | PASS |

**Result: PASS.** The backup commits' work is VERIFIED AND INCORPORATED in `7597a62`. The last backup commit checked is `b8f0e3f`. The branch is then reused for this change; it is not protected, and GitHub ran only the job `secrets` on each of the 33 pushes, each passing, its job `checks` skipped.

## Gates

**Verification 1 — the change works as intended:** PASS. Checks 1 to 10 pass on the tree that Gate 3's copy holds.

**Verification 2 — architecture and consistency:** PASS, by the builder's review of the whole diff. The owner's two messages are preserved word for word and listed in the manifest, the client's reference to the attached file left out and the file preserved beside them, as DEC-078 decides, with its reasons and alternatives. The pack is recorded where D1's verification is recorded, the Stage 2 record's "Venue verification for the operator's country", and in OQ-34, its canonical open question, as evidence the owner gave, not as the venues' terms: no venue's status changes, no venue is enabled, and no exchange is contacted (DEC-073, decision 3; DEC-075, decision 3). The pages the pack cites that failed before were not fetched again (owner decisions 41), and the two new pages that failed were not retried. No requirement, rule, code, or test changes; the project state, the decision log, and the indexes are brought up to the change, and the next action is U4's parts that need no venue's data.

**Verification 3 — independent end-to-end and failure audit:** PENDING: run 1, made by an independent reviewer, a separate agent started with a fresh context ([DEC-049](../decisions/DEC-049-preserve-owner-messages-of-2026-10-20.md)), on a push-disabled copy of the repository at `7597a62` with the change applied, made as the traceability README states and identified by the hash of its `git diff`; its brief gives the baseline of [DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md)'s decision 1 and the severity of its decision 2, and its findings are numbered K-01, K-02, and so on (decision 3).

## Findings

None yet: Gate 3's run 1 is pending.

## Failures and fixes

| Failure | Cause | Fix | Re-run |
|---|---|---|---|
| The documentation checker failed on the first write: DEC-078's name of the hash, in capitals with a hyphen, was read as a requirement's identifier, and three links named this record before it existed | The name's shape; the record written after the files that link to it | The name written in lower case, without the hyphen; this record added | Check 1 |
| Read back against the session record, DEC-078 said that the five questions were only the owner's to send; the builder's answer of 16:07 UTC said that sending them is the owner's call and that the builder cannot contact the exchanges | The builder's paraphrase | The sentence reworded to the answer's terms | Check 10 |

## Final status and remaining issues

PENDING: Gate 3's run 1. Gates 1 and 2: PASS ("Gates").

## Environment

This cloud environment, in the United States. Python 3.12.3 through uv 0.12.23 and `uv run --locked`; the system Python 3.11.18 for the documentation tools; git and GitHub's API for the branches and the machine checks' runs; one page-reading agent, which fetched three official pages once each. No container, database, account, or venue endpoint was used.
