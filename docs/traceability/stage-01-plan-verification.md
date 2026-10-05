# Stage 1 Plan — Verification Record

> **Status:** ACTIVE record of the checkpoint that adds the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md), written for the owner's approval after the owner authorized Stage 1 planning ([DEC-036](../decisions/DEC-036-owner-decisions-audit-findings.md)). Format: [traceability README](README.md). Made under the three-gate procedure of [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md). This is not the stage record: that is created when the stage starts, after the owner's approval.

## Identity

- **Date:** plan first written 2026-10-03; revised, checked, and verified 2026-10-05
- **Stage:** FOUNDATION — Stage 1 planning (before implementation)
- **Starts from:** commit `bb19a60`. This record's own commit is entered in the [project state](../project-state.md)'s checkpoint log by the next checkpoint.

## Scope

| Change | Files |
|---|---|
| The Stage 1 plan (PROPOSED): objective, entry gate, the disposition of every FOUNDATION requirement, work units U1 to U8 in checkpoints A to D, out of scope, outputs, tests, verification, completion criteria, decisions D1 to D11, sequence, risks | [Stage 1 plan](../roadmap/stage-01-foundation-plan.md) |
| Links and project memory | [Roadmap](../roadmap/roadmap.md) (header, Rule 140 note, FOUNDATION status); [project state](../project-state.md) (current stage, gate table, objective, continuation contract, the "Stage 1 planning" row of the owner-decisions table, completed work, in-progress work, recent changes, next step, checkpoint log); [documentation index](../README.md); [traceability README](README.md) |

Out of scope: any implementation (none is authorized); any requirement or decision change. The plan's decisions D1 to D11 are recommendations until the owner approves them.

## Checks

Run on 2026-10-05 on the final tree.

| # | Check | Command or method | Result |
|---|---|---|---|
| 1 | References, links, coverage, preserved texts, orphans; generated files current | `python3 tools/docs/build_index.py --check-only` | PASS (exit 0): 734 requirements, 99 findings, 36 decisions |
| 2 | No requirement changed | `python3 tools/docs/compare_requirements.py bb19a60 --strict` | PASS: 0 added, 0 removed, 0 changed |
| 3 | The tools still fail on broken input; code checks | `python3 tools/docs/selftest.py`; `ruff check tools/docs`; `ruff format --check tools/docs`; `mypy --check-untyped-defs tools/docs` | PASS: 34 cases; clean |
| 4 | Every requirement and rule the plan cites says what the plan says it does | Each cited constitution rule and master execution constitution section compared with its heading by script; each cited requirement read in its specification | PASS: 29 constitution rules and 17 master execution constitution sections cited, each matching its heading; a bare §95 is Handoff Part 1 §95 |
| 5 | The plan stays inside Stage 1 and drops nothing | Script: every requirement whose registry default stage is FOUNDATION, and every requirement a FOUNDATION row of the roadmap names, compared with the plan's section 3; each later-stage placement checked against the roadmap's rows | PASS: every requirement has exactly one disposition (RSK-049 is also named in section 3.5 only as RSK-048's replacement); the only non-FOUNDATION requirements in section 3 are OPS-004, MODE-006, MIG-027 (prepared, not delivered) and PLT-029 (platform-wide) |
| 6 | Every choice beyond an existing requirement or decision is marked RECOMMENDED — NOT YET APPROVED and listed among D1 to D11 | Reading of the plan | PASS (Gate 3 runs 3 and 4 found the remaining unmarked choices, now in D2, D3, D4, D8, D11) |
| 7 | The environment and technical claims are true | `python3.12 --version`; `uv --version`; `uv init --lib --build-backend uv` and `uv build` in a scratch directory; the decimal behaviours of U2 and the mypy behaviours of U3 reproduced in a scratch directory | PASS: Python 3.12.3; uv 0.8.17; `uv_build` builds an sdist and a wheel; the decimal context reaches new threads and asyncio tasks when its fields are set in place, not when the name is rebound; `quantize` raises under a trapped `Inexact`; a rounded quotient can round 9.899…9 (34 digits) down to 9.9 for an increment of 0.3, `divmod` gives 9.6; Hypothesis decimals raise under a trapped `Inexact` with limits alone, not with `places=`; Pydantic's `errors()` and `json()` keep input unless `include_input=False`; the mypy behaviours of U3 as stated |
| 8 | Hygiene | `git diff --check` (new files included); `git status --short --ignored`; scan for secrets, local paths, model identifiers | PASS: whitespace clean (new files included); only intended files and ignored caches; nothing found |

Environment: Python 3.11 (documentation tools) and Python 3.12.3 (the plan's technical claims), uv 0.8.17, ruff 0.15.8, mypy 1.19.1, Pydantic 2.13.5 and Hypothesis 6.168.4 in a scratch environment (not added to the repository), git.

## Three gates

| Gate | Result |
|---|---|
| 1 — Implementation / technical | PASS: checks 1 to 8 |
| 2 — Architecture / consistency | PASS: see below |
| 3 — Independent end-to-end / failure audit | PASS on run 4, after runs 2 and 3 failed and were fixed (run 1 stopped on a usage limit); see below |

### Gate 3 — independent review

**Run 1:** the reviewer stopped on the account's usage limit before reporting. It changed nothing; its partial work was not used.

**Run 2: FAIL** (a separate agent that did not write the plan; read-only on the repository, experiments on a copy; repository status unchanged). Four blocking findings, each reproduced by the builder and fixed by rewriting the plan:

| # | Finding | Fix |
|---|---|---|
| B1 | The plan let a dependency be added "with a justification", where the technology stack requires a decision record; the build backend, the workflow's actions, the contract conventions, the deployment-definition location, and the Rule 15 map file were choices not marked as recommendations | D11 lists every dependency for the approving decision record; D2 (locations), D3 (build backend), D4 (actions pinned by commit hash), and D8 (contract conventions) added; OPS-010 stays a design rule with no location fixed in Stage 1 |
| B2 | OPS-004 and MODE-006 were listed as Stage 1 requirements, though the registry and roadmap place them later; TEC-009 included testcontainers | Section 3 gives every FOUNDATION requirement an explicit disposition (3.1 to 3.5); OPS-004, MODE-006, SEC-004, and MIG-027 are "prepared, not delivered", the guard defence in depth only; testcontainers deferred to storage |
| B3 | Trapping `FloatOperation` was presented as enough to refuse floats; the reviewer showed seven ways a float still gets through (explicit conversions, equality, threads, Pydantic lax and strict JSON, JSON schemas, TOML) | One amount constructor; float conversions banned in `src/` by a repository test; the context set as current and default context; `Inexact` trapped; JSON amounts as strings only; TOML read with `parse_float=Decimal`; tests for a thread, an asyncio task, and a JSON number |
| B4 | The type checker would not enforce handling all four outcomes, and a test file meant to fail type checking contradicted strict mypy over `tests/` | An exhaustive `fold`; a `__bool__` hidden from the type checker so `truthy-bool` still reports truth-value use; negative type tests as `# type: ignore[<code>]` lines that strict mypy reports when unused |

Its non-blocking findings were also addressed: an explicit list instead of a catch-all row (finding 5); the matrix columns of §145 and a Gate 3 check that marked tests prove their requirement (6); D5 and D6 narrowed, and their relation to TC-10 stated (7); configuration failure modes (8); actions pinned, dependency review, the workflow-push risk, an import-direction test, `contracts/` created with its first schemas, wording (9); this record's date and scope, the project state's wording, and the PLT-029 citation (10).

**Run 3: FAIL.** A new independent reviewer confirmed B1 to B4 fixed and reproduced their technical claims (decimal behaviour in threads and tasks, the mypy behaviours, `uv_build`), and found:

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | The project state still described eight decisions (D1 to D8) in six places, and the next step would have recorded only those; the plan's entry gate pointed to "D1 to D3" for the dependencies | BLOCKING | "D1 to D11" and "eleven decisions" everywhere; the entry gate points to D11 |
| 2 | `hide_input_in_errors` hides input only from an error's string form; `errors()` and `json()` still contain it (reproduced by the builder with Pydantic 2.13.5) | BLOCKING | Errors are rendered and logged only through one function using `include_input=False`; validators never put input in messages; the acceptance test checks the string form, `errors()`, `json()`, and captured logs |
| 3 | Rebinding `decimal.DefaultContext` has no effect on new threads (reproduced) | Non-blocking | The plan says the fields are set in place |
| 4 | With `Inexact` trapped, `quantize` raises even with a rounding mode (reproduced), and unbounded Hypothesis decimal strategies raise | Non-blocking | Rounding functions use a local context with `Inexact` untrapped; bounded Hypothesis strategies (both made precise after run 4: exact `divmod` steps, and `places=`, since limits alone still raise) |
| 5 | `bool(o)` is not a type error, and a public kind would let callers bypass `fold` | Non-blocking | "Most truth-value uses"; kind and value not public, enforced by ruff's SLF001 and the structure test |
| 6 | `uv sync --frozen` ignores a stale lockfile | Non-blocking | `uv sync --locked` in the clean-clone check and the workflow |
| 7 | A coverage tool was implied but not listed | Non-blocking | No coverage tool; the public-function check is done in Gate 2 against the matrix |
| 8 | "Portable configuration never holds policy content" contradicted MIG-010; host paths cited MIG-004 | Non-blocking | The source-of-truth map's reading (policies are portable configuration that live only in the Policy System's store, POL-009, MIG-008); MIG-010 for host paths, MIG-004 for code |
| 9 | The trading-credential guard had nothing to inspect | Non-blocking | Secret declarations carry a kind from a closed set; example files hold placeholders only (GOV-017) |
| 10 | GOV-023 had two dispositions | Non-blocking | Removed from section 3.3 |
| 11 | The traceability acceptance could not hold for SEC-001, GOV-023, ARCH-032 | Non-blocking | U7 names the artifact and check that count for each |
| 12 | The new modules' owners, the relation to MIG-011, and the matrix location were not stated | Non-blocking | Added to D2 |
| 13 | OPS-010 and TEC-013 placements were imprecise | Non-blocking | "With the first deployable service"; the lease in CORE TRADING FOUNDATION, supervision in OPERATIONALIZATION |
| 14 | This record lacked "Failures and fixes" and "Environment" | Non-blocking | Added |
| 15 | Stale dates; the security architecture's "Threat model" line not in the completion criteria | Non-blocking | Project state dated 2026-10-05, the plan's dates include the revision; criterion 5 names that line |

**Run 4: PASS, no blocking finding.** A fourth independent reviewer (same conditions) confirmed both blocking findings of run 3 fixed and all thirteen non-blocking ones fixed (two partly), reproduced their technical claims, re-ran the scope check by script and every tool, and found ten non-blocking points, all fixed before the commit:

| # | Finding | Fix |
|---|---|---|
| 1 | Rounding to an increment through a rounded quotient can move a value the wrong way (reproduced by the builder); an over-long amount was accepted and failed only later | Intermediate steps stay exact under the trapped context (`divmod`); `Inexact` is untrapped only for the final `quantize`; the constructor refuses more digits than the precision; full-precision boundary cases in the property tests |
| 2 | Hypothesis decimal strategies still raise with limits alone (reproduced) | "Always given `places=`"; the run-3 row above corrected |
| 3 | Checkpoint A had no real test, so `pytest` would exit 5 | The repository test for secrets moves to checkpoint A (U1); U5 extends it |
| 4 | An error's location keeps input-derived keys even without input | The error function also redacts input-derived location parts; the acceptance test covers a secret used as a key |
| 5 | The risk table still said "until DATA FOUNDATION" | "Until the first deployable service" |
| 6 | Sections 7 and 8 disagreed on the public-function check and the structure rules | Gate 2 lists the check; the structure row lists every rule of U1 to U3 |
| 7 | The command line could not render errors without importing `atp.contracts`; `parse_float=Decimal` built a `Decimal` outside `atp.numeric` | `atp.config` hands the command line already-rendered errors; TOML numbers go through the amount constructor |
| 8 | The build backend is not recorded in the lockfile | It is pinned to one exact version in `pyproject.toml` (constitution Rule 102) |
| 9 | A requirement marker naming a PROPOSED or FUTURE requirement would pass | The checker refuses those too (ARCH-029, GOV-017) |
| 10 | Wording: the project state's "authorized" read as plan approval; tool versions; GOV-023's evidence; systems affected not named | "Planning authorized"; Hypothesis 6.168.4 added below; GOV-023's evidence includes the developer guide and the clean-clone run; the systems the roadmap names are stated in the plan's objective |

**Builder's own separate pass** (after these fixes): checks 1 to 8 re-run on the final tree; the rounding and Hypothesis claims reproduced again; the plan's sections 3, 4, 7, 8, 9, and 10 re-read against each other.

### Gate 2 — architecture and consistency (builder)

- **Inside Stage 1, nothing dropped:** every requirement the registry or the roadmap places in FOUNDATION has one disposition; later-stage requirements appear only as later or as prepared, never as delivered (check 5).
- **No silent decision:** every choice beyond an approved requirement or decision is one of D1 to D11, marked RECOMMENDED — NOT YET APPROVED; no requirement or decision changed (check 2).
- **No speculative structure:** each directory is created at the checkpoint that first puts a real artifact in it (constitution Rules 9–12); no new tool beyond those the stack names, except the build backend and the two actions, which are listed for a decision record (D11).
- **Project memory:** the project state, roadmap, and indexes say the plan is PROPOSED, awaiting the owner, with eleven decisions; nothing says implementation is authorized.

## Failures and fixes

| # | Failure | Cause | Fix | Re-run |
|---|---|---|---|---|
| 1 | Gate 3 run 2: four blocking findings | The plan described the intended protections at the level of mechanisms, without testing that each mechanism actually stops what it is meant to stop, and grouped requirements instead of checking each one's stage | Plan rewritten; every technical claim reproduced in a scratch environment before it was written; the scope checked by script | Gate 3 run 3 |
| 2 | Gate 3 run 3: two blocking findings | The project memory was not re-read after the plan's decision list changed; one round-2 fix (`hide_input_in_errors`) was adopted from the review without testing it | Project memory swept for every count and range; every technical claim of the round-2 and round-3 fixes reproduced | Gate 3 run 4 |

## Final status

**PASS.** All three gates passed (Gate 3 on run 4, after two failed runs whose findings are all fixed). The Stage 1 plan is PROPOSED and awaits the owner's decision: approve it, with or without changes to D1 to D11, and authorize implementation, or ask for changes. No requirement or decision changed; no code was written; implementation is not authorized.
