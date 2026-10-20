# Part 3 verification — Gate 3 Reports

> **Status:** REFERENCE (evidence) — the reports of the independent Gate 3 reviews of the change whose record is [Handoff Part 3 — Verification Record](part-3-verification.md), committed so that what the record says of each run can be checked against what the reviewer reported ([DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md), decision 5; [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 3). Each is reproduced in a text block exactly as given, except that local paths are shown as placeholders (`<repository>`). The sha256 of each report is stated as given and, where anything was replaced, as shown; the text it covers is the block's lines joined by line breaks, with a final line break where the entry says the report ends with one. It defines nothing; the record is the account of the reviews. The headings use the record's names for the runs.

## First review

- **Reviewer:** a fresh-context subagent, launched 2026-10-01, 18:16 UTC; report given 2026-10-01, 18:33 UTC
- **sha256:** `f3340fcf89b5f790fc90bd35a831cbb56b60453f9edceb8999454ee239dacbd2` as given; `d7963ca8df43823c88f03c08ed177e5a5b0f269a33c0b5661e86f8fefe8e082d` as shown, with 6 local paths replaced

```text
## Verification 3: independent review of the Part 3 integration (working tree vs a9034ce)

I changed nothing in the repository. I ran experiments only in a scratchpad copy of the repo.

### Findings

**1. BLOCKING: a P3§399 prohibition is not carried by the requirements its "Covered by" row cites**
- Where: `docs/traceability/part-3-reconciliation.md:68`
- Source (P3§399): "Concurrent opportunities must not create: Double capital allocation, Duplicate orders, **Conflicting strategy decisions**, Race conditions, Incorrect position state".
- The row says "Covered by PERF-013, CAP-027, EXE-008, REC-017". The reconciliation's own definition of "Covered by" is "fully met by the listed requirements".
- None of the four names conflicting strategy decisions:
  - PERF-013 says only that the platform "must account for concurrent … strategies" and that financial state transitions are atomic.
  - CAP-027 covers double reservation.
  - EXE-008 is client order IDs.
  - REC-017 is about after a restart.
- I also searched the PRT, DIR, CAP and RSK specs and found nothing explicit.
- Fix: either add a short requirement carrying this item, or map it explicitly in the row (for example to CAP-017, the single allocator, plus RSK-002 exposure and correlation limits) with a note that says so.

**2. BLOCKING: TNP-025 drops the source's "must" (modal-verb rule in requirements/README.md)**
- Where: `docs/systems/true-net-profit-engine.md:65`
- Source (P3§394): "Execution must still require: TRUE EXECUTABLE NET ECONOMICS. **The system must account for:** … Precision … Execution probability …"
- Requirement text: "In addition to the terms of TNP-018 and the latency decay of TNP-023, **the economics account for**: precision; execution probability."
- I ran a modal-verb count over all 107 P3-sourced requirements against their sources. This is the only place a "must" was lost.
- Fix: "…the system must account for: precision; execution probability."

**3. NON-BLOCKING: P3§449 factors are partly missing from the cited coverage**
- Where: `docs/traceability/part-3-reconciliation.md:118`
- Source: "The AI Resource Governor should determine whether an AI call is justified based on: Expected value, Task importance, Financial consequence, Latency, Cost, Available model, **Current workload**."
- The row cites AIL-008, AIL-009, RTR-002 and COST-002.
  - RTR-002 holds the Model Router's routing factors, not the Governor's admission factors.
  - AIL-008 lists what the Governor controls but no decision factors.
  - "Current workload" appears in none of them.
- Fix: list the admission factors (for example in an AIL note, or by extending the mapping) or record the gap.

**4. NON-BLOCKING: the claim that every PLT-027 "no …" item is indexed in the System Rules Register is false**
- Where: `docs/traceability/part-3-reconciliation.md:203` ("Each 'no ...' item is indexed in the System Rules Register") and `docs/product/platform-overview.md:125`.
- `grep -i 'hidden|migrat|OPS-020|OPS-007|assumption'` on `system-rules-register.md` returns nothing.
- So these items have no SR row: "No hidden state", "No undocumented production changes", "No unsafe migration", "No silent assumptions".
- PLT-027's text does keep all 14 items, so nothing is lost; only the claim is wrong.
- Fix: add SR rows (for example OPS-007/OPS-020, and MIG-007 to MIG-030), or reword both notes.

**5. NON-BLOCKING: CF-17 and CF-18 are labelled "RESOLVED" while also awaiting the owner, and the spec notes don't say so**
- `docs/conflicts/register.md:130` and `:136` say "RESOLVED … The owner is asked to confirm". The summary at `:9` says "18 conflicts…, all RESOLVED". `docs/README.md:45` still says "(all resolved)".
- The precedent is CF-14 at b6f005e: "**OPEN — owner decision required**" with "Proposed resolution — RECOMMENDED, NOT YET APPROVED".
- The spec notes `risk/risk-engine.md:122` (CF-17) and `systems/capital-management.md:107-108` (CF-18) state the readings as fact, with no "awaiting confirmation".
- `system-rules-register.md:39` (SR-20) relies on CF-18 in its "On violation" column, but its status is plain "DOCUMENTED". SR-26 does carry the note.
- The flags that do exist: DEC-031, project-state, the decisions README, the registry Approval column for RSK-048, and SR-02/SR-26.
- Fix: use a status such as "RESOLVED BY BUILDER — AWAITING OWNER CONFIRMATION", and add the same marker to the two spec notes and to SR-20.

**6. NON-BLOCKING: one effect of RSK-048 is not put to the owner**
- Where: `docs/risk/risk-engine.md:118`
- RSK-048 places "security" below "user hard constraints", following P3§471. DEC-026 only decided that the safety floor sits above the user.
- So security controls outside the floor rank below the user's hard policy. Examples: SEC-006/SEC-007 transfer restrictions and SEC-008 AI least privilege.
- This is the same "user policy vs a protective layer" question CF-14 was about. The CF-17 entry describes only the three added layers.
- Overall the reconciliation looks sound: it applies DEC-026, keeps RSK-004 unchanged, keeps RSK-005, and shows RSK-048 as "awaiting the owner's review".
- Fix: state this consequence explicitly in CF-17's question to the owner.

**7. NON-BLOCKING: the DUP-35 aliases create a term clash and one over-narrow mapping**
- Where: `docs/risk/risk-engine.md:123` and `docs/glossary.md:73` vs `docs/glossary.md:22`.
- "DEGRADED = CAUTION" makes DEGRADED an alias of a safety level. Glossary line 22 already defines DEGRADED as an HLT-011 health state "DISTINCT from safety level". It is also an RDY-011 and RDY-017 status. This goes against constitution Rule 33 (don't merge uncertain meanings) and Rule 59.
- "RECOVERY = CRITICAL RECOVERY" is too narrow. RSK-015 defines CRITICAL RECOVERY as "uncertain about financial/external state", but P3§372's RECOVERY is generic and includes transient recoveries (RSK-021/RSK-023).
- `docs/traceability/part-3-verification.md:32` says the DUP-34/DUP-35 readings are "listed for the owner". DEC-031's "Left for the owner" table (line 98) lists only CF-17, CF-18, OQ-27, TC-08 and the review.
- Fix: treat P3's DEGRADED as the health state (which feeds the safety level) or flag the clash in the glossary; widen the RECOVERY alias; list the DUP-35 aliases for the owner or reword line 32.

**8. NON-BLOCKING: REC-029's "incapable of uncontrolled live execution" rests only on the in-process lease**
- Where: `docs/systems/recovery-and-reconciliation.md:88`
- The note says "makes REC-022 technical: a standby holds no valid execution lease and therefore cannot place orders".
- But the fencing token is checked by the platform's own Execution Engine (TEC-013, EXE-010), not by the venue. TC-07 noted "Key rotation is the only one the venue enforces."
- The note leaves "How a standby obtains trading credentials when it takes over" open, but that question exists only in a spec note, not in the open-question register.
- Fix: soften "cannot place orders", and record the standby-credential question as a TC.

**9. NON-BLOCKING: a stale reference to a replaced requirement, in a line this change edited**
- Where: `docs/operations/deployment-and-operational-readiness.md:80` ends "Canary is defined in STR-011."
- STR-011 is DEPRECATED / REPLACED (STR-013 to STR-022). DEC-031 fixed exactly this kind of note in the Strategy Management spec.

**10. NON-BLOCKING: DEC-032 contradicts the new claim that records from DEC-031 onward have "Alternatives"**
- `architecture-governance.md:58` says "Decision records from DEC-031 onward include an 'Alternatives' section". `open-questions/register.md:53` (TC-08) says the same.
- `DEC-032-adopt-checkpoint-and-verification-rule.md` has no Alternatives section; grep confirms only DEC-031 among the new records has one.
- Fix: add one to DEC-032 (for example "None; owner instruction") or qualify the claim.

**11. NON-BLOCKING: some values-register entries are not updated or overlap**
- V-30 and V-31 (`values-register.md:40-41`) "Used by" still lists only RSK-026 and RSK-027. Their notes don't reflect `risk-engine.md:127` ("RSK-045, RSK-046 thresholds are values V-30 and V-31, which must now also be validated").
- V-39 (`:49`) "includes the capability eligibility thresholds of V-35". That defines one value under two IDs.
- V-39 is classed POLICY-CONTROLLED PARAMETER, but RDY-012 and P3§355 say thresholds are "determined by strategy economics; fees; …; policy; validation history", not set by the operator. Combined with the register's header rule ("Until it is set, the autonomous action … does not run"), no feature becomes available until the owner sets V-39 for it, which sits uneasily with RDY-014.

**12. NON-BLOCKING: dependency edge D-71 is misclassified and partly duplicates D-57**
- Where: `docs/architecture/dependency-map.md:92`
- D-71 is labelled "STATED" from P3§392/§393, but those sections name no systems. SYS-05 and SYS-04 are the builder's inference, so it should be INFERRED.
- Its SYS-21 → SYS-05 Opportunity Database edge already exists as D-57 (line 78).

**13. NON-BLOCKING: status headers are stale**
- 15 specs that now hold Part 3 requirements still say "DOCUMENTED (Handoff Parts 1 and 2)" or "(Handoff Part 2)" at line 3, and their Sources fields lack P3 sections. These are the risk engine, capital management, true net profit, opportunity detection, performance controller, market data, strategy management, recovery, system health, AI architecture, architecture overview, performance and latency, deployment, hosting and migration, incident management, and platform overview specs.
- `glossary.md:3` still says "DEC-006 to DEC-030 and Handoff Part 2".
- Only `readiness-system.md` was updated. The Part 2 round updated these headers.

**14. NON-BLOCKING: the registry's Stage column disagrees with the roadmap's Part 3 placement**
- The Stage column is one value per prefix, so it can't match per-requirement placement.
- Examples:

  | Requirement | Roadmap stage | Registry stage |
  |---|---|---|
  | CAP-037 to CAP-042 | ARBITRAGE (`roadmap.md:76`) | CORE TRADING FOUNDATION (`registry.md:253`) |
  | RSK-048 | FOUNDATION | CORE TRADING FOUNDATION |
  | PERF-018 to PERF-020 | DATA FOUNDATION | OPERATIONALIZATION |
  | HLT-014 | DATA FOUNDATION | CORE TRADING FOUNDATION / OPERATIONALIZATION |

- The pattern existed before (PERF-008 to PERF-010), but Part 3 widens it into two competing stage sources (constitution Rule 44).
- Fix: label the column "owner's default stage", or generate it from the roadmap.

**15. NON-BLOCKING: two checks that can pass without proving what they claim**
- **(a) Changes to sub-bullet lines are invisible.** `tools/docs/compare_requirements.py:20-21,39` (and `build_index.py`'s parser) read only the first line of a requirement. RSK-015's six owner-adopted safety-level definitions are indented continuation lines.
  - In a scratch copy I changed "SAFE MODE: the platform stops initiating new risk unless explicitly permitted…" to "SAFE MODE: the platform may keep initiating new risk".
  - `compare_requirements.py a9034ce --strict` exited 0 with "changed (0)", and `build_index.py --check-only` exited 0.
  - For this change I checked separately that no existing requirement or continuation line was removed or altered: `git diff -U0` shows no removed requirement lines.
  - Fix: append indented continuation lines to the requirement's text in both parsers.
- **(b) `--check-only` does not catch stale generated content.** `build_index.py:348-349` exits before comparing generated content.
  - I replaced RDY-009 with CAP-001 in the generated column for §352; `--check-only` still exited 0.
  - I regenerated in a scratch copy: `registry.md`, `handoff-coverage.md` and both reconciliations are byte-identical to the working tree, so the outputs are current.
  - Fix: in check-only mode, generate in memory and fail on any difference.
- **Cosmetic:** the `build_index.py` docstring (lines 7-8) is mangled. part-3-reconciliation is spliced into part-2's parenthetical.

**16. NON-BLOCKING (minor precision): some "Covered by" or "restated" notes leave out the requirement that actually covers the content**
- §441 (line 110): "→ CAPABILITY ASSESSMENT" is covered by RDY-024 and CAP-046, which are not listed.
- §422 (line 91): the RECONCILIATION response is PLT-025, which is not listed.
- §517 and §521 (lines 186, 190) say "Loop restated in CAP-046", but CAP-046's text holds only §483's chain and §484's reverse. §521's "FEATURE ELIGIBILITY … EXECUTION CAPACITY → CONTINUOUS REASSESSMENT" and §517's "MONITOR → REASSESS" are not in it (RDY-024 and CAP-035 cover them in substance).

### Checked and found correct

- **Checker and comparison:**
  - `build_index.py --check-only` passes.
  - `compare_requirements.py a9034ce` shows 109 added, 0 removed, 0 changed.
  - `git diff -U0` shows no requirement line removed.
- **Counts agree everywhere:**
  - Requirements: 721 total (Part 1 228, Part 2 185, Part 3 107, decisions 201 = 199 + RSK-048 + RDY-026), 109 new.
  - Prefixes 47; findings 91 (CF 18, DUP 38, OQ 27, TC 8); decisions 32.
  - SR-01 to SR-42; D-66 to D-71; V-36 to V-39 (39 entries).
- **Coverage, sources and wording:**
  - All 200 sections have rows, and every P3 source cites an existing section.
  - I read all of §351 to §550 and compared every new requirement with its source. Conditions are kept throughout, including "unless explicitly authorized and validated", "where technically possible", "where approved/applicable", "where safe", "unless an explicit risk/capital policy requires it", "unless an explicitly validated strategy and policy authorize", and "if failover is implemented". GOV-018 is correctly PROPOSED ("may maintain").
  - "In addition to" lists add only new items: CAP-037/023/024, CAP-044/002/029, CAP-045/030, RDY-015/STR-013/RDY-002, REC-027/018, PFC-016/012/013, PERF-018/008, PERF-020/010/VER-001, OPP-018/002, ARCH-037/027, GOV-007/ARCH-025, RSK-045/046, PLT-025/RSK-006.
- **"Covered by" rows:** I checked all 42 against the cited requirement text. Apart from findings 1, 3 and 16 they hold, including §369, §372, §376, §380, §382, §400, §419, §421, §423, §429–§432, §439, §445–§448, §451, §453–§456, §458, §459, §477, §493–§495, §513–§516, §524, §531, §538, §539 and §543.
- **P3§535 checklist:** all 140 items are traced. The stated classes match the actual classes of every cited requirement (scripted check). None rests on a PROPOSED, FUTURE or DEPRECATED requirement.
- **Classification:** follows DEC-024 decision 1. RSK-048 and RDY-026 show "Decided by: Builder; awaiting the owner's review", which is consistent with the DEC-024 precedent.
- **Owner decisions are preserved:**
  - DEC-026: RSK-004 unchanged; safety floor on top.
  - DEC-028: CAP-032 and RDY-008; eligibility never exceeds authorization.
  - DEC-030: one lease authority; the P3§494 exception is correctly not applied.
  - POL-005 to POL-007: CF-18 sends any unauthorized increase to POL-005.
  - AI limits: AIL-003 and ARCH-020 untouched; AIL-018 to AIL-020 grant no authority.
  - CF-18's reading is conservative and keeps every requirement.
- **No duplicate authority:** the Rebalancing Engine, Eligibility Engine, Canary Readiness Engine and capability registry are all components of existing owners. The System Rules Register indexes requirements rather than restating them; its classification column matches the first canonical requirement.
- **Cross-references:** every ID cited in the new notes points at the right requirement (EXA-015, OPS-005, MODE-003, PFC-005, PFC-008, CAP-019, RSK-011, OPP-004, EXE-002, LED-004/006, AUD-008/009, and others). No new document cites a deprecated requirement.
- **Generated files** (`registry.md`, `handoff-coverage.md`, both reconciliations) are current.
- **Repository completeness:**
  - `git diff --check a9034ce` is clean, and the untracked files have no trailing whitespace, no CRLF, and all end in a newline.
  - No ignored files and no `.gitignore`. All 10 untracked files belong in the commit. No secrets and no binaries.
  - The only placeholder is the expected `GATES_PLACEHOLDER`.

Key files: `<repository>/docs/traceability/part-3-reconciliation.md`, `<repository>/docs/systems/true-net-profit-engine.md`, `<repository>/docs/conflicts/register.md`, `<repository>/docs/risk/risk-engine.md`, `<repository>/tools/docs/compare_requirements.py`, `<repository>/tools/docs/build_index.py`.
```

## Re-run

- **Reviewer:** a fresh-context subagent, launched 2026-10-01, 18:39 UTC; report given 2026-10-01, 18:49 UTC
- **sha256:** `3ba1a21524437ec43e8cdaff7bd22e97bfdbe737f176eb2a1225ddca7c14ec9c`, as given and as shown

```text
Gate 3 re-run (independent, read-only) of the working tree against a9034ce. I changed nothing in the repository. All experiments ran in a copy in the session scratchpad. `git status` shows the same 35 modified and 10 untracked files before and after the review.

**Checks run:** `build_index.py --check-only` passes with exit 0: 723 requirements (Part 1: 228, Part 2: 185, Part 3: 109, decisions: 201), 47 prefixes, 92 findings, 32 decisions, 34 systems, 45 system rules, 153 of 200 Part 3 sections producing requirements. `compare_requirements.py a9034ce --strict` exits 0 with 111 added, 0 removed, 0 changed. `git diff --check a9034ce` is clean. The expected counts (111, 723, 45, 92 = CF 18 + DUP 38 + OQ 27 + TC 9, 153/200) agree everywhere except the stale figures in finding 2.

## Findings (none blocking)

**1. NON-BLOCKING: DUP-35 "aliases" wording is still in four places. This is the unfinished part of earlier fix 7.**
- Where:
  - `docs/traceability/part-3-reconciliation.md:41` (row 372): "Covered by RSK-015, RSK-020, RSK-023, HLT-011: the names are aliases of the safety levels (DUP-35)"
  - `docs/architecture/system-registry.md:93`: "Emergency state model | P3§372 | Aliases of SYS-09's safety levels (DUP-35)"
  - `docs/decisions/DEC-031-part-3-reconciliation.md:66`: "P3§372's names are aliases (DUP-35)"
  - `docs/traceability/part-3-verification.md:32`: "DUP-35's aliases"
- Why it matters: these contradict the corrected mapping in three places:
  - `risk-engine.md:123`: "without merging different meanings … DEGRADED = the health state DEGRADED (HLT-011) … is not itself a safety level"
  - glossary: "MAPPED (DUP-35); DEGRADED keeps its HLT-011 meaning"
  - `DEC-031:47`
- The system registry's "Named in Part 3" table is where each name's resolution is recorded, so two documents now resolve the same names differently.
- Fix:
  - Reword all four places to "mapped onto the safety levels (RSK-015) and health states (HLT-011) without merging meanings; mapping in the Risk Engine".
  - In row 372, add RSK-021 and RSK-022 to "Covered by", because RECOVERY now maps to RSK-021 to RSK-023.
  - In the system registry, name SYS-29 as well as SYS-09.

**2. NON-BLOCKING: some ranges and counts were not updated after PERF-022, AIL-021 and SR-43 to SR-45 were added.**
- `DEC-031:29` says "AIL-018 to AIL-020"; it should be AIL-021.
- `DEC-031:35` says "(new, SR-01 to SR-42)"; it should be SR-45.
- `DEC-031:38` says "PERF-018 to PERF-021"; it should be PERF-022.
- `part-3-verification.md:206` says "Near-duplicate text check over all 721 requirements"; the total is 723.
  - I re-ran a similarity check that includes the two new requirements. Neither creates a near-duplicate: PERF-022's closest match is CAP-027 (Jaccard 0.20), AIL-021's is AIL-020 (0.29). So the conclusion stands; only the count is stale.
- `part-3-verification.md:241` says "AIL-018 to AIL-020 only restrict AI"; it should be AIL-021.
- Optional: the AI Resource Governor row in `system-registry.md:87` does not cite AIL-021.

**3. NON-BLOCKING: a "must be validated" rule is attached to the excessive-trading thresholds without a source.**
- Where:
  - `values-register.md:41` (V-31): "Validated, not only configured (P3§435, P3§436)"
  - `risk-engine.md:127`: "RSK-045, RSK-046 thresholds are values V-30 and V-31, which must now also be validated, not only configured."
- Evidence: P3§436 has no validation wording ("…and determine whether the behavior is legitimate or pathological"). P3§435's "The exact thresholds must be validated rather than arbitrarily fixed" sits under LOSS-STREAK PROTECTION and is carried only by RSK-045 (V-30). RSK-046 has no such clause.
- The effect is a stricter rule on RSK-046 that no source states. That is requirement broadening (constitution Rule 56), although it does not weaken any control.
- Fix: limit the "must be validated" note to RSK-045 and V-30. For V-31, cite RSK-046's "legitimate or pathological" determination. Alternatively, record the stricter reading as a builder recommendation.

**4. NON-BLOCKING: one leftover from fix 14.** `docs/requirements/README.md:8` still lists the registry columns as "…canonical document, and roadmap stage". The column is now "Default stage", and the roadmap is authoritative for individual placement.
- Fix: say "default stage (the roadmap is authoritative for individual placement)".

**5. NON-BLOCKING: the new tool behaviour from fix 15 is not documented.** In `tools/docs/README.md`, line 7 still says "check only; writes nothing", and "What it checks" (line 21 on) does not mention two things:
- `--check-only` now fails when a generated file is out of date;
- both parsers now treat indented continuation lines as part of a requirement's text.
- Fix: add one bullet for each.

**6. NON-BLOCKING: TC-09 is listed inconsistently.**
- Where:
  - `part-3-reconciliation.md:13` lists the findings Part 3 produced as "(CF-17, CF-18, DUP-32 to DUP-38, OQ-27, TC-08)", omitting TC-09, which cites P3§496. Row 496 (line 165) does not mention TC-09.
  - `part-3-verification.md:50` (item 28) lists "OQ-27, TC-08, and the confirmations of CF-17 and CF-18", with no TC-09 and no DUP-34 or DUP-35 readings.
  - `DEC-031:106` puts TC-09 under "Left for the owner".
  - `docs/README.md:5` and `decisions/README.md:49` name only CF-17, CF-18, OQ-27 and TC-08 for the owner.
  - `project-state.md:14` says "TC-09 is decided when OPERATIONALIZATION is planned".
  - `project-state.md:37` says "answers the four items listed under 'Open questions'", but that table has six rows.
- Fix: choose one framing (recorded now, decided when OPERATIONALIZATION is planned) and apply it everywhere.

**7. NON-BLOCKING (trivial): fix 13 is not quite complete.** The status line at `readiness-system.md:3` leaves out P3§527, which RDY-016 cites ("P3§381, P3§527").
- Fix: add P3§527.

**Repository completeness:**
- No ignored files and no `.gitignore`.
- All 10 untracked files belong to this change. Each ends with a newline and has no trailing whitespace, CR, or tab.
- No secrets, keys or credentials in the diff or the new files.
- The commit hashes in the checkpoint log exist.

**Owner decisions and controls:**
- No contradiction found with DEC-026, DEC-028, DEC-030 or POL-005 to POL-007.
- No fix weakens a safety, risk, capital or AI-authority control.
- RSK-048's ranking of security below user hard policy is put to the owner in CF-17.
- V-39's "policy can only tighten" is stricter than required and consistent with RDY-008 and POL-007.

## The 16 earlier findings
1. **FIXED.** PERF-022 matches P3§399 word for word with the same modal verbs: "must not create" and "should be atomic where required". It is a CONSTRAINT, like PERF-013. It is in the registry, in SR-21, in row 399 ("Also"), and in the roadmap under CORE TRADING FOUNDATION. (Stale ranges in DEC-031: finding 2.)
2. **FIXED.** TNP-025 now says "the system must account for: precision; execution probability", matching P3§394's "must". P3§424's "should" is kept. Liquidity and the other costs are covered by TNP-018's order-book walk and TNP-024.
3. **FIXED.** AIL-021 matches P3§449, including "current workload". Its "should" verbs are kept, its class SYSTEM REQUIREMENT matches AIL-008, it is placed in AI INTELLIGENCE, and row 449 and the AI note are corrected. (Stale ranges: finding 2.)
4. **FIXED.** All 14 "no …" items of P3§534 map to a rule:
   - SR-01: shortcuts around financial authority (RSK-010)
   - SR-45: hidden state; silent assumptions
   - SR-03 and SR-36: uncontrolled AI
   - SR-31: duplicate authorities
   - SR-43: undocumented production changes
   - SR-37: unvalidated self-improvement
   - SR-44: unsafe migration
   - SR-33: uncontrolled failover
   - SR-05: forced trading
   - SR-19: fixed-return assumptions; artificial daily ceiling
   - SR-26: more capital means more risk
   - SR-27: restart means safe to resume

   SR-43 to SR-45 and the changed SR-19, SR-21 and SR-37 each cite requirements that say what the rule claims, and their classes match. ARCH-029 is a loose fit for "no silent assumptions", but PLT-027 carries the words. Optional: write this mapping into row 534.
5. **FIXED.** CF-17 and CF-18 now read "RESOLVED BY BUILDER — AWAITING OWNER CONFIRMATION". The markers are in the risk and capital notes, SR-02, SR-20, SR-26 and `docs/README`.
6. **FIXED.** The security-ranking consequence is stated in CF-17, the risk note, DEC-031 and the project state.
7. **NOT FIXED (partly).** The risk engine, glossary, register, DEC-031 decision 3 and the reliability model are corrected, but four documents still say "aliases" (finding 1).
8. **FIXED.** The REC-029 note now matches DEC-030 and EXE-010, and TC-09 is recorded with sound sources. (Listing inconsistencies: finding 6.)
9. **FIXED.** The Deployment and Operational Readiness note now cites STR-013 to STR-022 and OPS-011, OPS-013.
10. **FIXED.** DEC-032 now has an "Alternatives considered" section.
11. **FIXED, with a new defect.** V-30 and V-31 are updated. V-39 as OBSERVED ("derived per feature from evidence") stretches DEC-020's "measured by the running platform" but is explicitly qualified. It is consistent with RDY-011, RDY-012 (no fixed balance threshold) and RDY-014 (its exception is narrower than RDY-014). Default-deny is kept: a feature without a derived profile is DEFERRED or REQUIRES REVIEW. The new defect is V-31's unsourced "validated" (finding 3).
12. **FIXED.** D-71 is now INFERRED and points to D-57 instead of duplicating it.
13. **FIXED.** All 19 specifications that gained Part 3 requirements now name Part 3 in their status lines (one trivial gap: finding 7).
14. **FIXED.** The registry column is "Default stage" with the authority note. All 111 new IDs are placed in the roadmap table; GOV-018 is "not in any stage". (Leftover wording: finding 4.)
15. **FIXED.** Tested in the scratch copy:
    - **Stale generated files:** `--check-only` exits 1 on each of six cases: a title change, a hand edit of the registry, a stale part-3 column, a stale part-2 column, a stale coverage table, and a trailing newline. It exits 0 when clean.
    - **Idempotent:** regenerating produces files identical to the working tree.
    - **Continuation lines (comparison):** `--strict` reports RSK-015 as changed when a continuation line is edited, deleted, or separated by a blank line.
    - **No false positive:** re-indenting a continuation line reports no change.
    - **Scope:** RSK-015 is the only requirement with continuation lines.
    - **Docs:** finding 5.
16. **FIXED.** The covered-by notes for §422, §441, §517 and §521 now cite PLT-025, CAP-046 with RDY-024, and CAP-035 with RDY-024. DUP-37 and DEC-031 are updated.

**Gate 3 re-run: PASS.** There are no blocking findings, but fix 7 is incomplete and the record's description of it is currently inaccurate. Fix findings 1 and 2 before the checkpoint commit so that the claims are accurate.
```

## Launches that stopped before reporting

- First review, first attempt: launched 2026-09-30, 23:25 UTC; it stopped at the session usage limit before it reported, so no report exists.
