# Owner Decisions 41 Verification — the Owner's Answers on Jurisdiction, Operator, Server, and Exchanges

> **Status:** ACTIVE record of the change that preserves the owner's answers of 2026-11-19 to OQ-34 ([owner decisions 41](../handoffs/owner-decisions-41-answers-on-jurisdiction-operator-server-and-exchanges.md)), applies them ([DEC-074](../decisions/DEC-074-owner-answers-on-jurisdiction-operator-server-and-exchanges.md)), verifies the venues for the owner's country, compares hosting options for the owner's approval, and reconciles the backup commits of Stage 2's checkpoint A with its commit ([DEC-071](../decisions/DEC-071-one-reusable-backup-branch.md), decision 4). Its three gates: "Final status".

## Identity

- **Date:** 2026-11-19.
- **Stage:** Stage 2 (DATA FOUNDATION). This change records the owner's answers; it changes documentation only, builds nothing, and contacts no venue endpoint: the venues' legal pages and the providers' price pages were read.
- **Starts from:** commit `ec4de57` on branch `claude/code-builder-constitution-rrewgf`, equal to the remote: Stage 2's checkpoint A ([checkpoint A verification](stage-02-checkpoint-a-verification.md)), whose machine checks passed ([run 44551519578](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/44551519578): the job `secrets` from 15:09:02 to 15:09:15 UTC and the job `checks` from 15:09:02 to 15:11:02 UTC, both passing; the only run for that commit). This record's own commit is the checkpoint log's row "The commit that adds this row".
- **Temporary backup** ([DEC-057](../decisions/DEC-057-progress-continuity-no-loss-and-recovery.md), decision 4; DEC-071): the reusable branch `claude/unverified-backup-reusable`, reused after the eight checks below. This change's first backup commit, `9a56f70`, has as its parent `f197069`, the last backup commit of checkpoint A's change, and was pushed at 19:36 UTC; each later commit is a child of the branch's tip, pushed as a fast-forward and never forced. Each command that writes to the working tree ends with the backup.
- **Interruptions:** the session stood still from 19:40 UTC, when the weekly usage limit stopped it (the client's notice gave its reset as 2026-11-23, 12:00 UTC), until its worker was restarted at 19:53 UTC, the owner's "Try again" arriving with it; the working tree then equalled the tree of the backup commit `949e01c` (`c8054418`), and the scratch drafts were intact, so nothing was lost.

## Scope

**Added:** this record; [owner decisions 41](../handoffs/owner-decisions-41-answers-on-jurisdiction-operator-server-and-exchanges.md), taken by script from the session record and equal to it (check 6); DEC-074.

**Changed:** the [Stage 2 record](stage-02-data-foundation.md) (two sections, "Venue verification for the operator's country" and "Hosting options for Stage 2's live work"; the result of checkpoint A's venue verification, which points to them; checkpoint B's carried items on the venues); the [open-question register](../open-questions/register.md) (its banner; OQ-34 narrowed; OQ-35 added); the [project state](../project-state.md) (its summary; the continuation contract's rows on the current task, the work in progress, what is blocked, the stage's convergence and the session's stops, the decisions in effect and pending, the other branches, the known risks, and the next safe action; the active temporary backup; the open questions; the recent decisions and changes; the checkpoint log, checkpoint A's row given its commit); the [roadmap](../roadmap/roadmap.md) (Stage 2's row); the [documentation index](../README.md); the [decision log](../decisions/README.md); the [traceability README](README.md)'s list of records; and the manifest of preserved texts (owner decisions 41's line).

**Requirements:** none added, removed, or changed (check 3).

**Out of scope:** ordering or setting up a server; any request to a venue's API; checkpoint B's work.

**The owner's messages after the last one the previous record names** ([checkpoint A verification](stage-02-checkpoint-a-verification.md): the "Continue" of 14:46 UTC, after its run 4's copy), up to the copy that this record's last Gate 3 run reviews: the messages of 16:57, 17:04, 17:11, 17:16, 17:20, 17:24, 18:55, and 19:00 UTC, and the answers of 19:26 UTC, preserved as owner decisions 41 (DEC-074); and the "Try again" of 19:53 UTC, procedural ([DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 7). The notices that the usage limit had stopped the session (19:40 UTC) and that its worker was restarted (19:53 UTC), the reports of the page-reading agents and of Gate 3's reviewer, and the notices of background tasks are the client's own.

## Checks

The change's own checks, on the working tree with this change: the documentation tools with the system Python 3.11, the [developer guide](../development.md)'s checks through `uv run --locked`, git, and GitHub's branch list and workflow runs.

| # | Check | How | Result |
|---|---|---|---|
| 1 | The documentation checker | `python3 tools/docs/build_index.py --check-only`, after `python3 tools/docs/build_index.py` | @@C1@@ |
| 2 | The documentation tools' self-test | `python3 tools/docs/selftest.py` | @@C2@@ |
| 3 | No requirement added, removed, or changed | `python3 tools/docs/compare_requirements.py ec4de57 --strict` | @@C3@@ |
| 4 | The developer guide's checks | `uv run --locked` with `ruff check`, `ruff format --check`, `mypy`, `mypy --config-file tools/docs/mypy.ini`, and `pytest` | @@C4@@ |
| 5 | Hygiene of the change | `git diff --check ec4de57`, its new files included; a scan of the lines it adds for local paths, session or model identifiers, and the shapes of secrets | @@C5@@ |
| 6 | The preserved texts | `git diff --name-only ec4de57 -- docs/handoffs docs/builder`; owner decisions 41's messages compared by script with the session record | @@C6@@ |
| 7 | Quotations | The quotation script on the lines this change adds to the documents; each quotation of a source outside the repository looked for in it | @@C7@@ |
| 8 | The reusable branch | `git rev-list --parents` on the branch fetched from GitHub; the labels, record, trailers, and marker of each commit; GitHub's workflow runs for the branch and their jobs; GitHub's branch information | @@C8@@ |
| 9 | Stale statements ([DEC-069](../decisions/DEC-069-owner-questions-and-efficiency-directive.md), decision 4) | The stale-statement script on the active documents, by subject: OQ-34 and the venues' status (`OQ-34`, `no venue`, `verified for public market data`), the last decision (`DEC-073`, `DEC-001 to`), checkpoint A's backup (`checkpoint A's backup`, `holds the backup`), and the session's stops (`stood still`, `04:38`); each line that states the current state read whole | @@C9@@ |
| 10 | The venues and the offers as recorded | The Stage 2 record's two new sections, DEC-074, and OQ-34 read back, statement by statement, against the page-reading agents' reports (2026-11-19, from 19:30 UTC) and the web search, as the session record holds them | @@C10@@ |

The mutation check ([DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md), decision 6) does not apply: this change adds no code, test, or rule, as the change that recorded the plan's approval added none.

## Reconciliation of the last change's temporary backup

Stage 2's checkpoint A, committed as `ec4de57`, was backed up on the reusable branch in 59 commits, each on the one before and the first, `83de638`, on `4d02fce`, committed from 2026-11-17, 23:49 UTC, to 2026-11-19, 15:08 UTC (`f197069`). Each carries the seven labels, the emergency checkpoint record of §132, and both trailers, and none carries the marker (checked by script on 2026-11-19, 19:31 UTC).

| # | Check (owner decisions 10) | Evidence | Result |
|---|---|---|---|
| 1 | Every intended valid change is preserved | `ec4de57`'s tree is `f197069`'s, `b8129a81` (`git diff --name-only`: no difference) | PASS |
| 2 | Corrections made during verification are preserved | The same tree: the fixes of checkpoint A's four Gate 3 runs and its record's account of them | PASS |
| 3 | No required work exists only on the temporary backup | Each of the 66 files the commits change against `4d02fce`, whose tree is `447290f`'s, is in `ec4de57`, 51 of them outside `docs/`; no file is in an earlier commit and not in the last | PASS |
| 4 | No unverified or rejected implementation is accidentally promoted | `ec4de57`'s parent is `447290f`; none of the 59 commits is in its history or in that of `main`, at `7172a5c` (`git merge-base --is-ancestor`) | PASS |
| 5 | The authoritative branch contains the correct final state | On a fresh clone of the designated branch from GitHub, at `ec4de57` (19:33 UTC): the documentation checker and its self-test pass, and `compare_requirements.py 447290f --strict` reports 757 requirements before and after; the tests and the mutation list ran on its tree (checkpoint A's record, checks 4 and 8) and the tests in the machine checks | PASS |
| 6 | Required documentation and traceability are updated | `ec4de57` holds checkpoint A's record with its final status, PASS for its gates, the checkpoint log's row, and the backup in the project state's "Branches", as active until reconciled | PASS |
| 7 | The official verified checkpoint has been successfully pushed | `ec4de57` is on the remote branch, pushed at 15:09 UTC, and the machine checks passed on it ([run 44551519578](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/44551519578)) | PASS |
| 8 | Repository status is clean and consistent | The working tree was clean at `ec4de57` after the commit and its push, and again at 19:28 UTC, when this change began | PASS |

**Result: PASS.** The backup commits' work is VERIFIED AND INCORPORATED in `ec4de57`. The last backup commit checked is `f197069`. The branch is then reused for this change, as DEC-071 provides (decisions 4 and 5). GitHub ran the workflow on each of the 59 pushes, each run passing its job `secrets` with its job `checks` skipped, and the branch is not protected.

## Gates

**Verification 1 — the change works as intended:** PASS. Checks 1 to 10 pass on the tree that Gate 3's copy holds.

**Verification 2 — architecture and consistency:** PASS, by the builder's review of the whole diff. Each answer is applied through an existing rule, none duplicated: the operator through PLT-010 and DEC-006; the venues through D1 and DEC-073's decision 3, the five candidates kept (EXA-005) and other venues admitted only by EXA-006's assessment; the server through D2, which allows an environment the owner provides (MIG-004), with no purchase and no change to the stack (TEC-011, TEC-012); the owner's permanent conditions through the requirements and decisions that already state them. OQ-34 is narrowed in place; the clause that conflicts with PLT-010 becomes OQ-35, not a change. No requirement, rule, authority, process, or document type is added; statuses follow the owner's four words (VERIFIED, NOT VERIFIED, RESTRICTED, PENDING OWNER APPROVAL); no credential, venue endpoint, or account is used.

**Verification 3 — independent end-to-end and failure audit:** PENDING: run 1. The run is made by an independent reviewer, a separate agent started with a fresh context ([DEC-049](../decisions/DEC-049-preserve-owner-messages-of-2026-10-20.md)), on a push-disabled copy of the repository at `ec4de57` with the change applied, made as the traceability README states and identified by the hash of its `git diff`; its brief gives the baseline of [DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md)'s decision 1 and the severity of its decision 2, and its findings are numbered L-01, L-02, and so on (decision 3).

- **The builder's own separate pass:** check 10, made after the drafts and before the copy, found two statements to correct: DEC-074 said Kraken and Bitget were read, though Bitget's pages answered HTTP 404, and owner decisions 41's banner and DEC-074 gave the builder's first list of questions as 17:26 UTC, and the Stage 2 record the readers' start as 19:28 UTC, against the session record's 17:25 and 19:30 UTC; each corrected before the copy.

## Failures and fixes

| Failure | Cause | Fix | Re-run |
|---|---|---|---|
| Binance's, Bybit's, and Coinbase's terms stayed unreadable (pages drawn by the browser; HTTP 503; HTTP 403), Bitget's two pages answered HTTP 404, and KuCoin's API introduction HTTP 404 | The sites' answers to an automated reader | Not fetched again, as the owner asked; the missing evidence, with its official addresses, put to the owner (OQ-34) | — |
| A script stopped after writing owner decisions 41, before its manifest line | The manifest's hash covers a text's title and body without its banner, and its comment lines have no hash | The line added with the hash the documentation checker gives; the backup pushed in the same command | Check 1 |
| The weekly usage limit stopped the session at 19:40 UTC | The account's weekly limit | Resumed after the worker's restart at 19:53 UTC; nothing lost (Identity) | — |
| Two statements of the drafts wrong before the copy: Bitget called read, and two times a minute or two off | Written from what was meant, before the session record was read (checkpoint A's decision 7 root cause) | Corrected from the readers' reports and the session record (Gates, the builder's pass) | Check 10 |

## Final status and remaining issues

PENDING

## Environment

This cloud environment, in the United States (its outbound address in Council Bluffs, Iowa, on Google's network, as checkpoint A read it). The documentation tools with the system Python 3.11.18; the developer guide's checks through uv 0.12.23 and `uv run --locked`; git and GitHub's API for the branches and the machine checks' runs. The venues' and the providers' pages read by page-reading agents, which fetched through this environment.
