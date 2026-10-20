# TC-08 verification — Gate 3 Reports

> **Status:** REFERENCE (evidence) — the reports of the independent Gate 3 reviews of the change whose record is [TC-08 Alternatives — Verification Record](tc-08-alternatives-verification.md), committed so that what the record says of each run can be checked against what the reviewer reported ([DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md), decision 5; [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 3). Each is reproduced in a text block exactly as given; nothing in them was replaced. The sha256 of each report is stated as given and, where anything was replaced, as shown; the text it covers is the block's lines joined by line breaks, with a final line break where the entry says the report ends with one. It defines nothing; the record is the account of the reviews. The headings use the record's names for the runs.

## First review

- **Reviewer:** a fresh-context subagent, launched 2026-10-02, 06:17 UTC; report given 2026-10-02, 06:29 UTC
- **sha256:** `0efe484627bcc9e143d07a3494c5e1e1cb69bccc6256bd15cfc83b4f01f6d12c`, as given and as shown

```text
## Gate 3 independent review: TC-08 "Alternatives considered" change (working tree vs 0b3f97a)

**Verdict: FAIL.** One finding is BLOCKING. It is a one-bullet fix plus small updates to the verification record. Everything else passes, and the remaining findings are non-blocking.

### Findings

**1. BLOCKING: DEC-016, last bullet, makes a false "none recorded" claim and leaves out a sourced alternative.**
- `docs/decisions/DEC-016-roadmap-stage-placement.md` line 35 says: "No other stage order was recorded; the stages keep §95's order."
- The repository did record a different stage order, as a proposal, before DEC-016 replaced it:
  - `git show b850eaa:docs/roadmap/roadmap.md` line 3: "**Sequencing is PROPOSED.**"
  - Same file, line 25: "The PROPOSED dependency order (the two trading stages can run in parallel, and AI INTELLIGENCE follows CORE) is in the dependency map."
  - `git show b850eaa:docs/architecture/dependency-map.md` line 63: "## Stage-level dependencies (PROPOSED)". Its diagram puts DIRECTIONAL and ARBITRAGE side by side after CORE.
  - CF-05 at b850eaa pointed to it: "Status: OPEN. The proposed placements are in the roadmap."
- DEC-016 chose "Stages run **sequentially**" (RMP-002) instead. The bullet therefore misstates project history (Rule 181) and leaves out an alternative the repository shows, which is exactly what the owner asked to be added.
- This also makes three statements in the verification record untrue: check 2 (PASS), Gate 2's "every record … now states its alternatives", and the DEC-016 row of the source table.
- **Fix:**
  - Replace the bullet with: "**Parallel trading stages** (the builder's PROPOSED order when Part 1 was documented: DIRECTIONAL TRADING and ARBITRAGE in parallel after CORE TRADING FOUNDATION, AI INTELLIGENCE after CORE; roadmap and dependency map at commit b850eaa): not taken; stages run sequentially in §95 order (RMP-002). No reason is recorded."
  - Add "b850eaa roadmap and dependency map" to the DEC-016 row of the source table.
  - Add "an earlier version of a document (git history)" to the "what counts as sourced" criterion. DEC-011's bullet already relies on b850eaa. Mirror the criterion in project-state line 167.

**2. Non-blocking: DEC-007 bullet 2 recasts the record and is inconsistent with DEC-008.**
- The bullet calls the three types "this record's reading" of the owner's "all". The record itself states as fact: "The owner chose all three instrument types".
- It also gives no outcome for "other derivatives".
- DEC-008 bullet 1 treats the same kind of unrecorded first-round "all" as fact ("the owner chose all of them").
- The underlying observation is fair: OQ-04 names "other derivatives", and the question put to the owner is not recorded (I checked git history and commit 9fdbc3f).
- **Fix:** use neutral wording, for example: "Other derivatives (OQ-04 also named them): not in PLT-011. The question put to the owner is not recorded, so the repository cannot show whether this option was offered." Treat DEC-007 and DEC-008 the same way. Consider listing the scope ambiguity explicitly for the documentation review; project-state next step 1 does not mention it.

**3. Non-blocking: DEC-011 bullet 2 cites §09 for a ranking claim that §09 does not make.**
- §09 does not mention ranking. Only §06 (line 266) and §43 (line 1269) say "Opportunity ranking". The register row covers "discovery and ranking" together.
- The alternative itself is sourced, because OPP-011 ("Detection, not allocation ranking") rules it out.
- The bullet also omits the register's "quality dimensions (§17)" claimant.
- **Fix:** cite "Opportunity Detection (DUP-10's claimant; ruled out by OPP-011)" instead of "(§09)".

**4. Non-blocking: DEC-012 bullet 1 ("No other owner was put forward") does not follow the approach used in DEC-011.**
- DEC-011 lists the register's claimants as the alternative not chosen.
- DUP-04 also lists claimants: §47's arbitrage kill switch, System Health (§74), §27, and an undefined "global safety architecture" (§47). DEC-012's Context names the four places too.
- **Fix:** add a bullet "Safety split across the four places Part 1 uses (§25, §27, §47, §74) / a separate 'global safety architecture': not taken (RSK-008, HLT-010)", or reword the claim.

**5. Non-blocking: DEC-013's "none recorded" list is incomplete.**
- DUP-14, DUP-15, and OQ-12 are resolved by DEC-013, but no bullet covers them.
- DUP-14 lists three claimants; DUP-15's proposal was adopted.
- **Fix:** add them to the last bullet, or add a DUP-14 "claimants not chosen" bullet.

**6. Non-blocking: DEC-022 bullet 4 states the owner's answer more strongly than the owner wrote it.**
- The bullet says persisted state "is never relied on before it has been compared with authoritative external state".
- The owner wrote "must never be blindly trusted as authoritative financial state" and "should be compared against authoritative external state rather than assumed correct" (owner decisions 2).
- **Fix:** quote REC-014's wording.

**7. Non-blocking: DEC-023 bullet 2's citation does not support its claim.**
- The bullet says the owner's answer "follows the same model" and cites "Consistency" above.
- That section says STR-014, MODE-007, and PLT-014 express the same model. It says nothing about CF-13's proposal, and the CF-13 register entry does not say the answer follows the proposal (unlike CF-11).
- The claim is reasonable, but it is the builder's inference. **Fix:** label it as the builder's reading, or drop the citation.

**8. Non-blocking: DEC-003's existing section was "checked and left unchanged" but misses a sourced alternative.**
- Under the stated criterion, CF-10's other side (classifying requirements with the constitution's Rule 20 types) qualifies, and it is not listed.
- Either add it, or say in the verification record that the five earlier sections were deliberately not extended.

**9. Non-blocking: gaps in the verification record (`docs/traceability/tc-08-alternatives-verification.md`).**
- (a) It has no "Failures and fixes" section, which the traceability README requires.
- (b) The exceptions listed for check 9 leave out the TC-08 register row's Concern text, which still reads "Most of DEC-001 to DEC-030 have no 'Alternatives' section". That text follows the register's keep-as-raised convention, but it should be named as an exception.
- (c) Gate 1 counts check 2 as passed, but check 2 depends on Gate 3.
- (d) Observation 2 (the CF-11 to CF-13 options were not recorded) is not carried into project-state "Next approved step" item 1. Observation 1 is.

### Verified and found correct
- **Bullets:** 75 bullets across the 25 new sections, plus DEC-018's "None recorded" line, each checked against its cited source: the registers (current and at b850eaa), the record text, owner decisions 2, 3, and 4, OC-1, and Part 1/Part 2 §00, §05, §09, §54, §66, §74, §95, §99, P2§6, P2§200.
  - Accurate: 66.
  - With a non-blocking issue: 8 (findings 2, 3, 4, 5, 6, 7).
  - False: 1 (finding 1).
- **No invented options:** every quote or paraphrase of an owner option in DEC-026 to DEC-030 matches owner decisions 3. The "options not in the repository" statements for DEC-021 to DEC-023 are true; I checked 419b8da and 03716bf.
- **DEC-018 "None recorded":** true. OQ-21 lists no options, §05 only lists trend analysis and momentum, and there are no earlier versions.
- **"Except for DUP-10" (DEC-011):** true for all 14 DUP rows. All 22 DUP rows are identical to b850eaa in the first four columns.
- **Decision text unchanged:** each of the 25 files has exactly one added hunk starting at "## Alternatives considered", with 0 lines deleted. DEC-031, DEC-035, and the decision log differ only by their status, "Later changes", or summary line.
- **Section count:** 30 of 30 records have exactly one "## Alternatives considered", and DEC-031 to DEC-035 have one too, so architecture-governance's "Every decision record has …" is true.
- **Stale statements:** none found in active documents, README.md, or CLAUDE.md. Historical text is covered by a status line or "Later changes" note in DEC-031, DEC-035, part-3-verification, and owner-decisions-04-verification. The P3§474 row, index, roadmap, open-question register, and decision log are current.
- **Project state:** gate table, objective, continuation contract, next steps, and in-progress are consistent. Checkpoint log: the 0b3f97a row is filled in, and the last row is "The commit that adds this row".
- **Verification record:** all other checks-table, scope-table, and source-table claims are true. The figures 733/47/95/35/34/47, the 34 selftest cases, the numstat description, and the tool versions all match what I got.
- **Hygiene:** no secrets, local absolute paths, model identifiers, or stray files. The new file has no trailing whitespace.

### Commands run (all exit 0)
- `python3 tools/docs/build_index.py --check-only`: 733 requirements, 47 prefixes, 95 findings, 35 decisions, 34 systems, 47 system rules.
- `python3 tools/docs/compare_requirements.py 0b3f97a --strict`: 0 added, 0 removed, 0 changed.
- `python3 tools/docs/selftest.py`: PASS, 34 cases.
- `ruff check tools/docs`: all passed. `ruff format --check tools/docs`: 3 files already formatted. `mypy --check-untyped-defs tools/docs`: no issues.
- `git diff --check`: clean.
- `git diff --numstat -- docs/decisions/`: 0 deletions in DEC-002 to DEC-030; 1/1 for DEC-031 and README; 1/0 for DEC-035.
- Python 3.11.15, ruff 0.15.8, mypy 1.19.1.
- Supporting history checks: `git show b850eaa:` on the roadmap, dependency map, and register; 9fdbc3f and 419b8da project state; 03716bf message; plus `git log -S` and `git grep` searches.

### Repository state
`git status --short` is byte-identical to the snapshot I took at the start (diffed). Ignored entries are only `.mypy_cache/`, `.ruff_cache/`, and `tools/docs/__pycache__/`. HEAD is still 0b3f97a. I made no edits, stages, or commits; my scratch files are only in the scratchpad.
```

## Re-run

- **Reviewer:** a fresh-context subagent, launched 2026-10-02, 18:04 UTC; report given 2026-10-02, 18:19 UTC
- **sha256:** `dccd7060fc6c204e5cbf08b0e320e555fbda5a31a106422d9a69b82d79a77bff`, as given and as shown

```text
## Gate 3 re-run (independent review) of the TC-08 change on top of 0b3f97a

**Overall verdict: PASS.** I found no blocking findings and 7 non-blocking ones. I worked read-only and ran every experiment in a copy of the repository under the scratchpad. `git status --short` is identical at the start and end of the review, and the only ignored entries are `.mypy_cache/`, `.ruff_cache/` and `tools/docs/__pycache__/`.

Two placeholders must be filled before the commit: in `docs/traceability/tc-08-alternatives-verification.md`, Gate 3 says "**Re-run:** to be completed below before the commit", and "Final status" says "To be completed after the Gate 3 re-run".

### Findings (all non-blocking)

1. **DEC-030 misses an option the record names and defers.**
   - **Where:** `docs/decisions/DEC-030-high-availability-and-single-active-copy.md`, "Alternatives considered".
   - **Evidence:** DEC-030's own Notes say: "**Where the lease lives** (a replicated database or an external coordinator) is an implementation choice made when OPERATIONALIZATION is planned."
   - **Why it matters:** the verification record's criterion counts "an option the record itself names and rules out or defers", and DEC-009's added bullet (external vendors, FUTURE) applies that rule. As a result, Gate 2's claim that "every record ... states the alternatives the repository records" is not quite true. The section makes no "none recorded" claim, so this is a gap, not a false statement.
   - **Fix:** add a bullet such as "**Where the lease lives** (a replicated database or an external coordinator): deferred; an implementation choice made when OPERATIONALIZATION is planned ('Notes' above)."

2. **Check 4 in the verification record overstates what the history shows.**
   - **Where:** check 4 says "No decision record ever lost a line other than a status line."
   - **Evidence:** `git log -p` shows other lines were also replaced:
     - 9fdbc3f: DEC-002 "Resolves (provisionally): CF-07"; DEC-003 "Resolves (provisionally): CF-10 · Raises: OQ-23"; and DEC-003's Consequences sentence "The interpretation above needs owner confirmation (OQ-23)…".
     - 03716bf: DEC-012's "Later changes" line and DEC-019's "Raises for owner review" line.
   - None of these lines held an alternative, so the conclusion still holds.
   - **Fix:** "…other than status, header (Resolves/Raises/Later changes) lines and DEC-003's OQ-23 sentence; none held an alternative."

3. **DEC-005 cites the wrong range of resolving records.**
   - **Where:** DEC-005's bullet says the findings were "later resolved by decision records (DEC-006 to DEC-018)".
   - **Evidence:** the findings register says "The 32 Part 1 findings are RESOLVED by decision records DEC-002, DEC-003, DEC-006, and DEC-010 to DEC-016". CF-07 and CF-10 fall outside the cited range.
   - **Fix:** "(DEC-002, DEC-003, DEC-006, DEC-010 to DEC-016; open questions by DEC-006 to DEC-018)", or simply "by later decision records".

4. **DEC-009's added introductory line is inaccurate.**
   - **Where:** the italic line says the new bullet "is recorded elsewhere in the repository".
   - **Evidence:** its source is DEC-009's own "Retention" section ("external vendors are FUTURE"), with OQ-22 as the question. The template line was reused from DEC-003, where it is accurate.
   - **Fix:** "…the one below is recorded in this record's Retention section (OQ-22)…".

5. **DEC-019 may miss options the owner named and ruled out.** This is a judgement call.
   - **Where:** DEC-019 lists only the five defaults.
   - **Evidence:**
     - OC-1 item 7: "An emergency should not be treated as one universal action."
     - OC-1 item 9: "The system must not blindly close every position during an emergency."
     - Both are carried into RSK-015 to RSK-017, which cite DEC-019.
     - OC-1's closing note: "You do not want: restart → immediately send orders."
     - The "keep positions" side and the "one universal action" side are arguably covered by the defaults. "Close every position" and "restart straight into sending orders" are not.
   - **Fix:** add them with OC-1 or RSK-017 as the source, or record that the section is limited to the defaults shown.
   - The same class exists elsewhere, for example Q6's option text "rather than fixed in code" for DEC-028. The documentation review could treat it as one item.

6. **Builder readings are labelled less clearly than in DEC-023.**
   - DEC-030 bullets 3 and 5 ("Failover is fast and automatic, so it relies on the shared lease"; "so it is read as acquiring the execution lease…") rest on Notes that are the builder's ("Decided by: … the notes below are the builder's"). They are not attributed to the owner, but they are not labelled "Builder's reading:" as DEC-023's is.
   - DEC-008 bullet 1 still says the owner's answer "gave five initial venues". This matches DEC-008's own "Initial venues (owner)", but it is less neutral than DEC-007's fixed wording.
   - **Fix (optional):** label the DEC-030 bullets "Builder's reading"; in DEC-008 write "the decided set is five initial venues and room for more (EXA-005, EXA-006), decided on the owner's answer ('…')".

7. **DEC-022 bullet 4 omits one replacing requirement.** It says the owner's answer replaced REC-007 and REC-011 "(REC-014, REC-015)". The recovery specification says REC-011 is replaced by REC-015 *and REC-016*. **Fix:** add REC-016.

### The 9 earlier findings: all fixed, and each fix is accurate
1. **DEC-016:** the parallel-stages bullet now quotes the roadmap at b850eaa exactly: "The PROPOSED dependency order (the two trading stages can run in parallel, and AI INTELLIGENCE follows CORE)".
   - "No reason is recorded" holds. DEC-016, RMP-002, the resolution record and the dependency map at 9fdbc3f give no reason.
   - DEC-016's table does say "ARBITRAGE depends on them", but that dependency was already known at b850eaa, when parallel stages were still proposed, so it is not a recorded reason.
   - The criterion and check 4 were added as stated.
2. **DEC-007 and DEC-008** now have neutral wording, and say the question put to the owner is not recorded. Observation 1 is in the project state's next step.
3. **DEC-011** now follows DUP-10's list. "Opportunity ranking" appears in Part 1 at §06 (line 266) and §43 (line 1269). TNP-021 produces the TNP-015 quality dimensions.
4. **DEC-012** now names DUP-04's claimants (§25, §47, §74, the §27 outcomes, and the "global safety architecture").
5. **DEC-013** has the DUP-14 bullet; DUP-15 and OQ-12 are named, and OQ-12 is in the "no other" line.
6. **DEC-022** quotes REC-014 verbatim (both quotes).
7. **DEC-023's** reading is labelled "Builder's reading:".
8. **DEC-003** has the CF-10 bullet and **DEC-009** the deferred-vendors bullet, each under an "Added on" line.
9. **The verification record** now has "Failures and fixes"; check 10 names the TC-08 Concern text; Gate 1 reads "checks 1 and 3 to 11"; observation 2 is in the project state.

### What I verified and found correct
- **Fidelity:** I checked all 77 added bullets in the 27 changed records, plus DEC-018's line, against the cited sources: CF-01 to CF-16, DUP-01 to DUP-31, OQ-03 to OQ-26, TC-02 to TC-07, owner decisions 2 and 3, OC-1, the Part 1 and Part 2 handoff sections, and the RSK/REC/STR/HLT/PLT/EXA texts. Quotes are verbatim or faithful, nothing is attributed to the owner beyond what the owner wrote, and I found no invented alternative or reason. The issues are findings 3, 4, 6 and 7 above.
- **History sweep:**
  - The registers at b850eaa match the current ones: the DUP rows, all OQ and TC rows (first four columns) and the CF proposals marked "as first written".
  - The project state at 16d317c, b850eaa, 9fdbc3f, 419b8da and b6f005e matches DEC-001, DEC-016, DEC-019 and the options in owner decisions 3. The CF-11 to CF-13 options are not in the repository.
  - The proposed placements at b850eaa match DEC-016's table.
- **"None recorded" claims:** all 8 are accurate (DEC-008, DEC-012, DEC-013, DEC-015, DEC-017, DEC-018, and the three "options not in the repository" lines).
- **No decision changed:** only lines were added to DEC-001..030. DEC-031 and the decision log each have one line replaced, and DEC-035 gained one line.
- **Structure:** all 30 records have exactly one "## Alternatives considered" section, placed before Consequences or at the end. 27 records carry the "Added on" line; DEC-001, DEC-006 and DEC-014 are unchanged.
- **Consistency:**
  - Updated documents: the project state (gate table, objective, continuation contract, next step with both observations, the 0b3f97a row, and the new last row "The commit that adds this row"), the register, the decision log, the governance note, the index, the roadmap, the DEC-031 and DEC-035 status lines, the "Later changes" note in owner decisions 4, and the P3§474 row.
  - Other "TC-08" and "next checkpoint" hits sit under historical "Later changes" or status notes.
  - The verbatim texts under docs/handoffs and docs/builder, README.md and CLAUDE.md are unchanged.
- **Verification record:** apart from findings 1 and 2, every claim checks out, including the scope table, the source table and the counts (733/47/95/35/34/47; 34 selftest cases).

### Commands run (in the scratchpad copy), all exit 0
- `python3 tools/docs/build_index.py --check-only`: 733 requirements, 47 prefixes, 95 findings, 35 decisions, 34 systems, 47 system rules.
- `python3 tools/docs/compare_requirements.py 0b3f97a --strict`: 0 added, 0 removed, 0 changed.
- `python3 tools/docs/selftest.py`: PASS, 34 cases.
- `ruff check tools/docs`: all checks passed.
- `ruff format --check tools/docs`: 3 files already formatted.
- `mypy --check-untyped-defs tools/docs`: no issues.
- `git diff --check`: clean, including the untracked record (added with intent-to-add in the copy only).
- `git diff --numstat -- docs/decisions/`: as described above.
- Hygiene scan of the diff and the new record: no secrets, local paths or model identifiers; the new file has no trailing whitespace and ends with a newline.
- Environment: Python 3.11.15, ruff 0.15.8, mypy 1.19.1.
```

## Launches that stopped before reporting

- Re-run, earlier attempt: launched 2026-10-02, 06:35 UTC; it stopped at the session usage limit before it reported, so no report exists.
