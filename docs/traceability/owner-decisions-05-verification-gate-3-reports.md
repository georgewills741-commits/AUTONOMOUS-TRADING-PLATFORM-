# Owner decisions 5 verification — Gate 3 Report

> **Status:** REFERENCE (evidence) — the report of the independent Gate 3 review of the change whose record is [Owner Decisions 5 — Verification Record](owner-decisions-05-verification.md), committed so that what the record says of each run can be checked against what the reviewer reported ([DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md), decision 5; [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 3). It is reproduced in a text block exactly as given; nothing in it was replaced. The sha256 of each report is stated as given and, where anything was replaced, as shown; the text it covers is the block's lines joined by line breaks, with a final line break where the entry says the report ends with one. It defines nothing; the record is the account of the review. The headings use the record's names for the runs.

## Independent review

- **Reviewer:** a fresh-context subagent, launched 2026-10-03, 01:00 UTC; report given 2026-10-03, 01:10 UTC
- **sha256:** `b6c33f33a05411f0f27debcb830311a9c2c30552fb4f5160825e4ab9b5921766`, as given and as shown

```text
Overall verdict: PASS

I found no blocking defects. The verbatim record, DEC-036, the requirement changes, the tooling and project memory all hold up. There are six non-blocking findings. Fix finding 1 before the commit; the others are optional tidy-ups.

## Findings

1. **Non-blocking: MKD-007's rewording narrows its scope, and the record does not say so.** `docs/systems/market-data.md:18`
   - Old text: "Market data is kept in TimescaleDB for 30 days and permanently in compressed Parquet archives (OHLCV, trades, order-book snapshots) for backtesting". The bracket described what goes into the archives; all market data went into TimescaleDB.
   - New text: "Market data (OHLCV, trades, order-book snapshots) is stored and archived for backtesting." The bracket and "for backtesting" now apply to all stored market data.
   - Read that way, MKD-007 now stores only three data types, and only for backtesting. MKD-002 also covers bid/ask, funding rates and metadata, and MKD-003 sends stored data to the live quantitative engine.
   - The owner's option only said "point to it instead of repeating the numbers". DEC-036's reading notes explain dropping "permanently" but not this change.
   - Nothing is actually lost, because TEC-012 still says "Market data is kept 30 days in TimescaleDB". Still, it is an unlabelled change of meaning in a requirement (Rule 56).
   - Fix: reword to "Market data is stored, and OHLCV, trades, and order-book snapshots are archived for backtesting. The storage tiers and their retention periods are set in TEC-012 (V-18), on the storage of TEC-006." Then re-run `compare_requirements.py` with the same `--expect-changed`.

2. **Non-blocking: DEC-009's "Later changes" line is literally untrue.** `docs/decisions/DEC-009-technology-stack.md:4`
   - It says "The retention values below are stated only in TEC-012", but the record itself states them at lines 44–45.
   - The same wording appears as "Stated only in TEC-012" in `docs/requirements/values-register.md:28-29`, a register that itself states 30 days and 90 days.
   - Fix: say "Among the requirements, the retention values below are stated only in TEC-012" (DEC-009). In V-18 and V-19, say "No other requirement states it (DUP-40, DEC-036)".

3. **Non-blocking (optional): MIG-033 is missing from two places that list the related rules.**
   - The reliability index's "Standby, failover, migration, backup" table (`docs/operations/reliability-and-recovery-model.md:41-45`) does not cite MIG-033.
   - Nor do the "Later decisions affecting TEC-011" notes (`docs/architecture/technology-stack.md:23-26`).
   - MIG-033 is now the rule behind "production on at least two hosts". Fix: add MIG-033 to the "Main copy fails" or "Disaster" row, and one clause to the TEC-011 note.

4. **Non-blocking (optional): DEC-028 still describes DEC-006 as "no custody, no withdrawals by the platform".** `docs/decisions/DEC-028-capital-buckets-and-progressive-activation.md:37`
   - DEC-036 (CF-21) has now made explicit that DEC-006 means "for others". DEC-028's "Later changes" line (line 8) predates that and does not mention CF-21 or DEC-036.
   - Fix: append "PLT-010 now matches DEC-006's 'for others' (DEC-036, CF-21)."

5. **Non-blocking (optional, already present at 16df57f): DEC-035's "Next" line is out of date.** `docs/decisions/DEC-035-owner-decisions-part-3-findings.md:53`
   - It still reads "Next: the TC-08 work, then the complete documentation review ..., then the Stage 1 plan". Its "Later changes" line only covers TC-08.
   - Fix: extend that "Later changes" line with "the complete documentation review is done and accepted, and Stage 1 planning is authorized (DEC-036)".

6. **Non-blocking (optional): two traceability and wording points.**
   - The reworded PLT-010, MKD-007 and MON-009 still sit under "Decisions applied (2026-09-30)". Their spec headers and the "Sources:" line (`docs/product/platform-overview.md:62`) name only DEC-006, DEC-009 and DEC-017. The new wording is traceable only through the Findings notes and the decision records' "Later changes" lines. Fix: add "(wording: DEC-036)" to each "Sources" line.
   - `docs/open-questions/register.md:41` marks OQ-28 "RESOLVED", while the register's own rule at line 5 says to mark an answered item "ANSWERED" (OQ-27 uses ANSWERED). The register already mixed the two words before this change. Fix: use "ANSWERED", or leave it.

## What I verified

**Fidelity (item 1): pass.**
- I extracted the last two AskUserQuestion calls from the transcript (lines 7225 and 7237) and their results (7230 and 7238).
- A script parsed the record back and compared it field by field: 7 of 7 labels, questions, every option label and description, and all 7 answers are identical.
- The results have no annotations, and none of the answers uses "Other". The owner's choices match the summary in the brief.
- The banner and formatting note are accurate. The audit's item 21 lists the same seven items, including "optionally confirm" for the feature process.

**Faithfulness (item 2): pass, except finding 1.**
- MIG-033 states only the chosen CF-20 option. Its additions are labelled:
  - RDY-022 and RMP-010 as "the same readiness bar" appear in DEC-036's reading notes.
  - "Local hosting stays supported" is implied by the rejected option, which "narrows MIG-001".
  - "At least an active and a standby host" was already the repository's wording, in DEC-029 and the TEC-011 note.
- The new PLT-010 matches DEC-006 decision 1 and quotes SEC-006's "no general withdrawal or custody authority". Its pointer to SEC-007 inherits SEC-007's "where supported". It adds no permission. Naming SEC-007 goes beyond the option, but the reading notes label it.
- MON-009 keeps its behavior: logs are rotated and kept separate from AUD-006.
- Keeping MKD-007's class is handled honestly, in DEC-036's reading notes and the DUP-40 resolution.
- OQ-28 is applied without changing PLT-011.
- DEC-036's "Alternatives considered" matches the options that were not chosen.

**Requirement integrity (item 3): pass.**
- `compare_requirements.py 16df57f --strict --expect-changed=MKD-007:text,MON-009:text,PLT-010:text` exits 0. Requirements go from 733 to 734: MIG-033 added, three text-only changes, no class, title or source change.
- MIG-033's line format, CONSTRAINT class, DEC-036 source, "(owner decision)" section (the same style as MIG-029 and MIG-030) and OPERATIONALIZATION stage are consistent.
- MIG-033 does not duplicate any existing requirement.

**Stale statements (item 4): pass.**
- I swept every active document for CF-20, CF-21, DUP-40, OQ-28, "pending documentation review", "await…", "for the owner", "stand as written", the old PLT-010 wording, "30 days"/"90 days", requirement totals and "documentation review". This included the System Rules Register, glossary, maps, registries, roadmap and READMEs.
- Every remaining hit is in historical verification records, register entries kept as written, or the audit record, which carries a "Later changes" line.

**Project memory (item 5): pass.**
- The project state's gate table, continuation contract, open questions, next step ("write the Stage 1 plan, gates, commit, stop") and "Do not implement yet: Anything" are correct.
- In the checkpoint log, the 16df57f row is filled in and the last row reads "The commit that adds this row".
- `docs/README.md`, `docs/traceability/README.md` and `docs/decisions/README.md` are consistent with it.

**Tooling (item 6): pass. All commands were run on the copy.**
- `build_index.py --check-only` exits 0: 734 requirements, 99 findings, 36 decisions.
- Running the full `build_index.py` on the copy regenerates `docs/` byte-identical to the working tree.
- `selftest.py` passes; `ruff check`, `ruff format --check` and `mypy --check-untyped-defs` are clean.
- The registry has 0 "pending documentation review" and 512 "reviewed (DEC-036)" (223 from Part 1, 181 from Part 2, 108 from Part 3).
- Normalizing the approval text leaves only the header counts, the column explanation and the MIG-033 row as registry differences.
- The only code change is the generator text in `build_index.py`, in two hunks.
- The manifest hash `de220fef…` matches the file (title line plus body). Changing one word in the body makes the checker exit 1; a change to the banner only passes; restoring the file passes.

**Hygiene (item 7): pass.**
- `git diff --check` with the untracked files added via `git add -N` on the copy: exit 0.
- The new files have no CRs. The added lines contain no secrets, no local paths and no model identifiers.
- The only ignored files are caches: `__pycache__`, `.mypy_cache`, `.ruff_cache`.

**Repository status (read-only):** `git status --short` was identical at start and end (33 entries: 30 modified, 3 untracked), with HEAD at 16df57f. All experiments ran on a copy in my scratchpad (`gate3-od5/repo`).
```

## Launches that stopped before reporting

None.
