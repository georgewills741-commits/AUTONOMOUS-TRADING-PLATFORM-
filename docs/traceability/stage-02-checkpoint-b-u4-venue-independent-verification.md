# Stage 2, Checkpoint B, Increment 2 (U4's Venue-Independent Parts) — Verification Record

> **Status:** ACTIVE record of the second increment of Stage 2's checkpoint B: U4's parts that need no venue's data, in `atp.exchange` (the adapter interface, the size limit and exact decoding of messages, the outcomes of requests, the rate-limit manager, and connection resilience), with the structure test's rules for CCXT and TLS; the owner's messages of 2026-11-20, 21:13 UTC, and 2026-11-21, 05:47 UTC, preserved as [owner decisions 46](../handoffs/owner-decisions-46-open-venue-items-and-other-venues.md) ([DEC-079](../decisions/DEC-079-owner-messages-on-open-venue-items-and-other-venues.md)); and the reconciliation of the backup commits of the change that records owner decisions 45 with its commit, `395a657` ([DEC-071](../decisions/DEC-071-one-reusable-backup-branch.md), decision 4). Its three gates: "Final status and remaining issues". The stage's status, how checkpoint B is built in increments, and the builder's choices: the [Stage 2 record](stage-02-data-foundation.md). Format: [traceability README](README.md).

## Identity

- **Date:** 2026-11-20 to 2026-11-21.
- **Stage:** Stage 2 (DATA FOUNDATION), checkpoint B, as the [Stage 2 plan](../roadmap/stage-02-data-foundation-plan.md) defines it (U4 and U5), authorized by [DEC-073](../decisions/DEC-073-stage-2-plan-approved-with-changes.md) (decision 6); this increment builds U4's parts that need no venue's data ([Stage 2 record](stage-02-data-foundation.md), "Checkpoint B: increments").
- **Starts from:** commit `395a657` on branch `claude/code-builder-constitution-rrewgf`, equal to the remote: the change that records owner decisions 45 ([owner decisions 45 verification](owner-decisions-45-verification.md)), whose machine checks passed ([run 44822047969](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/44822047969), triggered by its push: its jobs "checks" and "secrets" both passing). This record's own commit is entered in the project state's checkpoint log by the next change.
- **Temporary backup** ([DEC-057](../decisions/DEC-057-progress-continuity-no-loss-and-recovery.md), decision 4; DEC-071): the reusable branch `claude/unverified-backup-reusable`, reused after the eight checks below. This change's first backup commit, `96fbe3b`, has as its parent `886884b`, the last backup commit of the change that records owner decisions 45, and was pushed at 21:46:59 UTC, as the same command wrote owner decisions 46's first message and DEC-079 into the repository; U4's code and tests, drafted first in the builder's workspace, entered the repository with the second, `aa17a9e`, at 21:56 UTC. Each later commit is a child of the branch's tip, pushed as a fast-forward and never forced, and each command that writes to the working tree runs the backup after its last write. Each commit carries the seven labels of [DEC-042](../decisions/DEC-042-preserve-anti-drift-rules-and-backup-instructions.md) (decision 4) and the emergency checkpoint record of master execution constitution §132, and no marker; the repository test for secrets runs on its snapshot before its push, and on GitHub only that test runs (check 9). Its reconciliation with this change's commit is recorded by the next change.
- **Interruptions:** the session stood still from 22:36 UTC on 2026-11-20, when the account's 5-hour usage limit stopped it while the mutation check ran on in the background (the limit reset at 02:10 UTC; the worker's restart at 23:42 UTC met the limit again), until the owner's message of 2026-11-21, 05:47 UTC. The working tree then equalled the tree of the last backup commit, `cb5cf3e` (`429e4659`), pushed at 22:34 UTC, so nothing was lost; the mutation check had ended at 22:56 UTC (check 8).

## Scope

**Added:** `src/atp/exchange/`, a new package, SYS-01's parts that no single venue owns: `_messages.py` (a message's size limit, its exact decoding, and the record of untranslatable input), `_requests.py` (each request's result as an outcome), `_backoff.py`, `_ratelimit.py` (the rate-limit manager and the retry of reads), `_resilience.py` (the circuit breaker, a venue's health, and keeping a stream connected), and `_interface.py` (the adapter interface), with its `__init__.py`; its tests, `tests/exchange/` (`test_messages.py`, `test_requests.py`, `test_ratelimit.py`, `test_resilience.py`, and `test_interface.py`); three committed schemas under `contracts/`: `atp.exchange.backoff`, `atp.exchange.rate-limit`, and `atp.exchange.resilience-limits`, each at 1.0; [owner decisions 46](../handoffs/owner-decisions-46-open-venue-items-and-other-venues.md), the owner's messages of 2026-11-20, 21:13 UTC, and 2026-11-21, 05:47 UTC, and [DEC-079](../decisions/DEC-079-owner-messages-on-open-venue-items-and-other-venues.md), which preserves and applies them; this record.

**Changed:** the structure test (the rules that CCXT is imported only in `atp.exchange` and given no credential, that nothing in `src/` turns TLS verification off, and `atp.exchange`'s import rule, with their planted samples); `tools/mutation/mutations.py` (155 entries for U4's rules, with their files' constants); the preserved-text manifest, `tools/docs/preserved-texts.sha256` (owner decisions 46's line); the [decision log](../decisions/README.md) (DEC-079's row); the [Stage 2 record](stage-02-data-foundation.md); the [architecture-to-repository map](../architecture/source-of-truth-map.md#architecture-to-repository) (`atp.exchange`'s row) and the [contract conventions](../architecture/contracts.md) (the system contracts written so far); the [system registry](../architecture/system-registry.md) (its note on what is implemented, stale since Stage 2's checkpoint A); the [exchange-adapters specification](../systems/exchange-adapters.md) (its status line, and what has been specified since its notes were written); the [open-question register](../open-questions/register.md) (OQ-34); the [roadmap](../roadmap/roadmap.md) (DATA FOUNDATION's row and U4's feature row); the [project state](../project-state.md); the root README, the [documentation index](../README.md), and the [traceability README](README.md); the generated [verification matrix](verification-matrix.md).

**Requirements:** none added, removed, or changed (check 3).

**Out of scope:** each venue's adapter, its recorded responses, and its live check, after that venue's verification (OQ-34); any request to a venue; the values of the rate, backoff, and resilience limits, given with each adapter; the transports and the real clock and wait, given by the adapters and the process (U10; the Stage 2 record's "Carried to later units"); checkpoint C, whose order the owner is asked about (DEC-079, decision 5).

**The owner's messages after the last one the previous record names** ([owner decisions 45 verification](owner-decisions-45-verification.md), "Final status and remaining issues": the message of 21:13 UTC, after its run 2's copy, is the next record's), up to the copy that this record's last Gate 3 run reviews: the message of 2026-11-20, 21:13 UTC, on the open items of OQ-34 and on other venues, and the message of 2026-11-21, 05:47 UTC, which repeats those items and says to forget about the terms of any exchange and to continue or proceed to the next thing, both preserved as [owner decisions 46](../handoffs/owner-decisions-46-open-venue-items-and-other-venues.md) ([DEC-079](../decisions/DEC-079-owner-messages-on-open-venue-items-and-other-venues.md)). The client's summary of the conversation at 22:21 UTC, the usage limit's notices at 22:36 and 22:56 UTC and with the worker's restart at 23:42 UTC, the notices of background tasks, and the reports of Gate 3's reviewer are the client's own.

## Checks

The change's own checks, on the working tree with this change: the documentation tools with the system Python 3.11, the [developer guide](../development.md)'s checks through `uv run --locked`, the mutation runner on git clones, git, and GitHub's branch list and workflow runs.

| # | Check | How | Result |
|---|---|---|---|
| 1 | The documentation checker | `python3 tools/docs/build_index.py --check-only`, after `python3 tools/docs/build_index.py` | @@C1@@ |
| 2 | The documentation tools' self-test | `python3 tools/docs/selftest.py` | @@C2@@ |
| 3 | No requirement added, removed, or changed | `python3 tools/docs/compare_requirements.py 395a657 --strict` | @@C3@@ |
| 4 | The developer guide's checks, and the build | `uv run --locked` with `ruff check`, `ruff format --check`, `mypy`, `mypy --config-file tools/docs/mypy.ini`, and `pytest`; `uv build` | @@C4@@ |
| 5 | Hygiene of the change | `git diff --check 395a657`, its new files included; a scan of the lines it adds for local paths, session or model identifiers, and the shapes of secrets | @@C5@@ |
| 6 | The preserved texts | The change's files against `395a657`, its new files included, under `docs/handoffs` and `docs/builder`; owner decisions 46's two messages compared by script with the session record | @@C6@@ |
| 7 | Quotations | The quotation script on the lines this change adds to the documents; each quotation of a source outside the repository looked for in it | @@C7@@ |
| 8 | Check 7, the mutation check ([DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md), decision 6) | `tools/mutation/run.py` on git clones of the working tree, each with its remote removed, in four slices (`--slice K/4`), the runner's selection set by a wrapper around its functions: this change's entries (`S2-U4 `), first on the code as first written, then on the code with the builder's review's fixes; then the entries that the change's documents and structure test may affect: the 62 whose checks read the documents (by the repository test for secrets and by the documentation tools' self-test) and the structure test's 119 from before this change | @@C8@@ |
| 9 | The reusable branch | `git rev-list --parents` on the branch fetched from GitHub; the labels, record, trailers, and marker of each commit; GitHub's workflow runs for the branch and their jobs; GitHub's branch information | @@C9@@ |
| 10 | Stale statements ([DEC-069](../decisions/DEC-069-owner-questions-and-efficiency-directive.md), decision 4) | The stale-statement script on the active documents, by subject: checkpoint B and U4 (`checkpoint B`, `U4`, `is next`, `not implemented`, `is implemented`), the backups' reconciliation (`owner decisions 45`, `holds the backup`), the owner's last messages and decisions (`owner decisions 46`, `DEC-079`, `21:13`, `DEC-001 to`), the session's stops (`stood still`, `usage limit`), and the next work (`checkpoint C`, `Next safe action`); each line that states the current state read whole | @@C10@@ |
| 11 | U4's acceptance, for the parts that need no venue's data | The plan's U4 against the code and the tests | @@C11@@ |

## Reconciliation of the last change's temporary backup

Owner decisions 10's eight checks, on the backup commits of the change that records owner decisions 45, against its commit `395a657`, before the reusable branch was used again ([DEC-071](../decisions/DEC-071-one-reusable-backup-branch.md), decision 4), on 2026-11-20 from 21:41:11 to 21:42:32 UTC. The branch held 19 commits after `b8f0e3f`, the last commit the previous reconciliation checked: `4801465` (16:50 UTC) to `886884b` (21:37 UTC), each with a single parent, the one before it, and each with the seven labels, the emergency checkpoint record, and both trailers, and none with the marker.

| # | Check (owner decisions 10) | Evidence | Result |
|---|---|---|---|
| 1 | Every intended valid change is preserved | `395a657`'s tree is `886884b`'s, `f939ec4a` (`git diff --name-only`: no difference) | PASS |
| 2 | Corrections made during verification are preserved | The same tree: the fixes of that change's Gate 3 runs 1 and 2, and its record's account of them | PASS |
| 3 | No required work exists only on the temporary backup | Each of the 12 files the commits change against `b8f0e3f`, whose tree is `7597a62`'s, is in `395a657`; outside `docs/`, the documentation tools' README and the preserved-text manifest; no file is in an intermediate commit and not in the last | PASS |
| 4 | No unverified or rejected implementation is accidentally promoted | `395a657`'s parent is `7597a62`; none of the 19 commits is in its history or in that of `main`, at `7172a5c` | PASS |
| 5 | The authoritative branch contains the correct final state | On a fresh clone of the designated branch, at `395a657` (21:41:22 UTC): the documentation checker and its self-test pass, and the requirement comparison with `7597a62` finds 758 requirements before and after, none added, removed, or changed | PASS |
| 6 | Required documentation and traceability are updated | `395a657` holds that change's record with its final status, PASS for its gates, the checkpoint log's row, and its backup in the project state's "In progress, possibly partial", "Other branches", and "Next safe action" | PASS |
| 7 | The official verified checkpoint has been successfully pushed | `395a657` is the tip of the remote designated branch, and the machine checks passed on it ([run 44822047969](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/44822047969), triggered by its push: both jobs passing) | PASS |
| 8 | Repository status is clean and consistent | `git status --porcelain` printed nothing at `395a657` (21:42:12 UTC) | PASS |

**Result: PASS.** The backup commits' work is VERIFIED AND INCORPORATED in `395a657`. The last backup commit checked is `886884b`. The branch is then reused for this change; it is not protected, and GitHub ran only the job `secrets` on each of the 19 pushes, each passing, its job `checks` skipped.

## Gates

**Verification 1 — the code works as intended:** @@V1@@

**Verification 2 — architecture and consistency:** @@V2@@

**Verification 3 — independent end-to-end and failure audit:** @@V3@@

## Findings

@@FINDINGS@@

## Failures and fixes

| Failure | Cause | Fix | Re-run |
|---|---|---|---|
| The builder's review of the draft, before it entered the repository, found that `maintain_connection` recorded a success as soon as a connection opened, so a venue whose connections open and deliver nothing would never back off or open its circuit | The builder's drafting | A connection counts as a success only at its first message, with a test of connections that go stale or drop before any message | Check 4 |
| ruff and mypy refused the first draft: the order of `__all__`, an unneeded suppression, the order of imports, and a check of a type that mypy found unreachable | The builder's drafting | ruff's own fixes and format; the check written as `type(...) is not` | Check 4 |
| Writing the tests found two expectations wrong: a weight's wait in the sliding window, and the time of a stream's fifth connection | The builder's arithmetic | Each expectation recomputed from the rule and corrected, and the fake clock made to let what was due run before time passes | Check 4 |
| The mutation runner refused the first clones | They were copies without `.git`, and `rsync` is not installed | Copies made with `tar`, `.git` included, each with its remote removed | Check 8 |
| The builder's review after the code entered the repository found three defects: a circuit's trial that the venue refused, by a rate-limit refusal or a refusal of the request as sent, or whose outcome was never recorded, left the circuit half-open for good, the venue then refused every request; a failure of the request queue's clock or wait left every waiting request waiting for good; and `retry_read` waited only its backoff after a rate-limit refusal, though the venue asked for longer. The venue's state also kept RATE_LIMITED after a later answer that was not a rate-limit refusal, which its docstring did not say | The builder's drafting: the trial's end and the queue's failures not traced through every outcome | A trial so ended lets another request be the trial, and a trial without an outcome expires after the open time; the queue gives its failure to each waiting request; a retry waits the longer of its backoff and the venue's wait; RATE_LIMITED holds only while it is the last outcome; each with its tests and mutation entries ("Gate 2") | Checks 4 and 8 |
| The mutation check: `S2-U4 a request leaving its window one tick late` survived | An equivalent mutation: an entry exactly at its window's end, kept one tick longer, frees its weight at once when the wait is computed, so the wait is the same | Replaced by `S2-U4 a request leaving its window one tick early`, which a request one tick before the window's end kills | Check 8 |
| ruff refused the queue's handler of any failure (BLE001) | The rule against catching every exception | The handler kept, since a failure of the clock or wait given to the queue may be of any type and is passed to each waiting request, not swallowed; the suppression given its reason on its line | Check 4 |
| The builder's scan for stale statements found the system registry saying that no system is implemented, false since Stage 2's checkpoint A, and the project state's last update dated 2026-11-19 | Earlier changes, which updated the feature-status table and not the registry's note, and did not change the date | The note now says that no system is complete and where the systems built in part are recorded; the date brought up to the change | Checks 1 and 10 |

@@MOREFAILURES@@

## Final status and remaining issues

@@FINAL@@

## Environment

This cloud environment, in the United States. Python 3.12.3 for the platform, through uv 0.12.23 and `uv run --locked`; the system Python 3.11.18 for the documentation tools; git and GitHub's API for the branches and the machine checks' runs. No container, database, or network access to a venue was used.
