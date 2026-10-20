# Stage 1 plan verification — Gate 3 Reports

> **Status:** REFERENCE (evidence) — the reports of the independent Gate 3 reviews of the change whose record is [Stage 1 Plan — Verification Record](stage-01-plan-verification.md), committed so that what the record says of each run can be checked against what the reviewer reported ([DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md), decision 5; [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 3). Each is reproduced in a text block exactly as given, except that local paths are shown as placeholders (`<scratchpad>`, `<repository>`). The sha256 of each report is stated as given and, where anything was replaced, as shown; the text it covers is the block's lines joined by line breaks, with a final line break where the entry says the report ends with one. It defines nothing; the record is the account of the reviews. The headings use the record's names for the runs.

## Run 2

- **Reviewer:** a fresh-context subagent, launched 2026-10-05, 17:52 UTC; report given 2026-10-05, 18:03 UTC
- **sha256:** `f7739da45828d0677fa336b01b75792e959d814ce56df725d02865d36d787aad`, as given and as shown

```text
Overall verdict: FAIL

Four BLOCKING findings: two are scope and labelling errors, two are technical claims I disproved by testing. All are cheap to fix in the plan's text. The tooling checks and project memory are clean, and nothing says implementation is authorized.

## Findings

**1. BLOCKING: the plan weakens the technology-stack rule for adding dependencies, and choices that bind later stages are not flagged.**
- `stage-01-foundation-plan.md:58` says: "No other dependency is added without a justification under constitution Rule 99, recorded in the stage record."
- `technology-stack.md:5` says: "Adding a dependency not listed here requires a decision record (constitution Rules 99–101)."
- Dependencies the plan needs but never names:
  - a build backend, needed for `uv build` (plan:175), the `atp` command of D1, and installing `src/atp`;
  - the third-party GitHub Actions the D3 workflow needs (plan:64–65).
- Other choices that are not D-items:
  - The contract conventions at plan:84–85: strict, frozen, unknown fields refused, decimals as strings, and a "major version" compatibility scheme. Together these set the versioning model for every future interface (ARCH-026).
  - The deployment-definition location: plan:44 says it "is fixed", but no unit, output, or D-item fixes it.
  - The file for the Rule 15 mapping (plan:122 says "system registry or source-of-truth map").
- So the plan's own claim at plan:5 is false: "Every choice this plan makes that is not already a requirement or decision is marked RECOMMENDED — NOT YET APPROVED … and listed".
- **Fix:**
  - Reword plan:58 to require a decision record; the decision record that approves this plan can list the Stage 1 additions.
  - Add D-items for the build backend, the CI actions (pinned by commit SHA), the contract conventions and versioning scheme, and the deployment-definition location.
  - Name the file for the Rule 15 mapping.

**2. BLOCKING: OPS-004 and MODE-006 are listed as Stage 1 requirements, but the registry and roadmap place them later.**
- plan:40 lists them under "Requirements in this stage".
- The registry's default stage is OPERATIONALIZATION for OPS-004 (`registry.md:684`) and CORE TRADING FOUNDATION for MODE-006 (`registry.md:62`). No FOUNDATION row of the roadmap moves them (`roadmap.md:48, 60, 72, 84`).
- Stage 1 cannot meet them:
  - OPS-004 requires each environment to have "its own configuration, database, and credentials".
  - MODE-006 requires the non-production environments to be "technically unable to place real orders".
  - U4 delivers only a configuration guard keyed on a declared environment name (plan:97, 100).
- Completion criterion 3 (plan:185) still requires every section 3 requirement to be "traced to implementation and tests … or recorded as met". That would force a false trace.
- The same, smaller: TEC-009 is listed (plan:36) without testcontainers, which belongs with storage.
- **Fix:**
  - Move OPS-004 and MODE-006 into a "prepared, not delivered" group, with their real stages.
  - Justify the U4 guard by constitution Rules 109 and 111 and the §95 "Configuration" item.
  - State that the guard is defence in depth only. The real barrier is that no credentials exist outside production (SEC-004), which later stages build.
  - Note that testcontainers is deferred to the storage stage.

**3. BLOCKING: the float-refusal mechanism in U2 and D7 is technically wrong, and the acceptance tests would not catch it.**
- plan:73 says: "a float is refused (the decimal context traps `FloatOperation`, so mixing floats in is an error, not a silent conversion)".
- plan:204 (D7) says: "Makes TEC-003 enforceable by the runtime".
- What I tested (Python 3.12.3, pydantic 2.13.5, with the trap set):
  - `Decimal.from_float(0.1)` and `ctx.create_decimal_from_float(0.1)` are allowed.
  - `Decimal('0.1') == 0.1` silently returns False; equality comparisons are never trapped.
  - A new thread does not get the trap: `Decimal(0.1)` succeeds there, because threads start from `DefaultContext`.
  - `Decimal(True)`, `Decimal('NaN')` and `Decimal('Infinity')` are all accepted.
  - Pydantic in lax mode converts 0.1 to `Decimal('0.1')` regardless of the trap.
  - Pydantic in strict mode accepts a JSON number and loses precision: `{"amount": 0.12345678901234567890123}` becomes `Decimal('0.12345678901234568')`.
  - The generated JSON schema for a Decimal advertises `{"anyOf":[{"type":"number"},…]}`, which invites JSON numbers.
  - With D8's TOML, `tomllib.loads("fee = 0.1")` returns a float unless `parse_float=Decimal` is passed.
- **Fix:**
  - Describe the trap as one layer only.
  - Add one amount constructor that accepts only `str`, `int` (not `bool`) and `Decimal`, and refuses non-finite values.
  - Ban `from_float` and `create_decimal_from_float` with a lint rule or a test.
  - Set both `decimal.DefaultContext` and the current context at process start.
  - Accept amounts in JSON only as strings, refuse JSON numbers, and make the committed schema say so.
  - Read TOML with `parse_float=Decimal`.
  - Add an acceptance test for each, including a new thread, an asyncio task, and a JSON-number input.
  - Say which traps D7 sets (for example `Inexact`); plan:77 depends on it.

**4. BLOCKING: the type checker does not enforce outcome exhaustiveness, and the negative type test as written contradicts U1.**
- plan:86 says: "code that handles an outcome must handle all four, which the type checker enforces".
- plan:88 says: "a test file that must fail type checking is part of the suite".
- plan:58–59 requires strict mypy over `tests/`, with "`uv run mypy` … pass".
- What I tested with `mypy 1.19.1 --strict`:
  - `if o is Outcome.SUCCESS: … return "other"` passes.
  - A `match` that leaves out TIMEOUT and UNKNOWN passes unless it ends with `assert_never`.
  - `if o:` passes unless the `truthy-bool` error code is enabled.
- A file that must fail type checking, placed in `tests/`, makes `uv run mypy` fail.
- **Fix:**
  - Use an API that requires all four handlers, for example `fold(on_success=…, on_failure=…, on_timeout=…, on_unknown=…)`, or require `match` with `assert_never` and check that convention.
  - Make `__bool__` raise, and enable `truthy-bool`.
  - Write the negative test as `# type: ignore[<code>]` on the line that must error. Strict mode's `warn_unused_ignores` then fails if the error ever disappears; I checked that this works. Alternatively, run the file through `mypy.api` from pytest and exclude it from the main mypy run.

**5. Non-blocking: the catch-all row at plan:46 ("the rest of the FOUNDATION set") is inaccurate.**
- It sweeps in requirements that are not "already met by documentation":
  - ARCH-034 is PROPOSED and "Not in any stage" (`roadmap.md:92`).
  - SEC-003 is DEPRECATED.
  - TEC-005, TEC-011 and TEC-012 are decided but applied later.
  - TEC-013 is placed in OPERATIONALIZATION (`roadmap.md:54`).
  - SEC-006 to SEC-009 are placed later by the roadmap.
- plan:48 says "OPS-007 to OPS-017" stay later, which includes OPS-010, taken into Stage 1 at plan:44.
- **Fix:** list these requirements explicitly with their real disposition, and write "OPS-007 to OPS-009, OPS-011 to OPS-017".

**6. Non-blocking: the verification matrix is narrower than §145 and the traceability README.**
- plan:116 gives "(requirement, system, implementation, tests, status)".
- §145 and `docs/traceability/README.md:52` also require verification, evidence, and commit/version. ARCH-040, cited at plan:114, adds rule and interface.
- plan:117 can be satisfied by putting a marker on a weak test.
- **Fix:** add the missing columns, and a Gate 3 check that each marked test really exercises its requirement (DEC-032: "tests that pass without actually proving the required behavior").

**7. Non-blocking: the meanings in D5 and D6, and their overlap with TC-10.**
- D5 (plan:202) records a feature's state in the stage record of the stage that builds it. Once that record is closed, later GOV-024 states (CANARY, PRODUCTION) have no current home (§109).
- D6 (plan:203) makes ACTIVE mean "any GOV-024 state before DEPRECATED", which includes IDEA and PROPOSED (see ARCH-029).
- D6, U3's UNKNOWN and U4's environment names settle names listed in TC-10 (`open-questions/register.md:56`), yet plan:137 puts TC-10 out of scope.
- The four-value outcome cannot represent EXE-009's "pending" transfer state.
- **Fix:**
  - Narrow ACTIVE, for example to APPROVED through PRODUCTION.
  - Say that D6 partly decides TC-10, and update the register and glossary when it is approved (§36).
  - State where a feature's state lives after its stage closes.
  - Say how operation-specific states such as "pending" map onto the four outcomes.

**8. Non-blocking: the configuration source and its failure modes.**
- Portable TOML configuration (plan:98) must never hold policy content. POL-009 says "No repository document holds policy content" (`systems/policy/policy-system.md:34`; `source-of-truth-map.md:145`).
- **Fix:**
  - State that exclusion, and list the concrete Stage 1 settings.
  - Say where the process's environment identity comes from.
  - Pydantic echoes input values in validation errors. I tested an unknown field `api_secret="sk-live-…"` and the error printed `input_value='sk-live-…'`, which breaks plan:99. Require `hide_input_in_errors=True` or `SecretStr`, plus a test that the error does not contain the secret.
  - `frozen=True` does not freeze nested lists (tested); use tuples.
  - Refuse a zero or negative increment.
  - Define rounding for signed values: in `decimal`, ROUND_DOWN rounds toward zero, ROUND_FLOOR toward minus infinity.

**9. Non-blocking: security and structure.**
- Pin the CI actions by commit SHA.
- Review the locked dependencies for known vulnerabilities at checkpoint A (§40).
- Add a risk: pushing `.github/workflows/` may need a token with workflow permission. This is my inference; I did not test it.
- Enforce Gate 2's import directions (plan:176) with a standard-library `ast` test, and place the `atp` command module in that graph.
- `contracts/` (plan:82): at checkpoint B no committed schema exists yet. Say what it holds, or create it when the first schema exists (plan:154; constitution Rules 9–12).
- plan:130: write "database schemas and migrations", since JSON schemas are in scope.
- plan:122: the registry is generated, so its status changes through the generator, not by hand.

**10. Non-blocking: nits in the record and project memory.**
- `stage-01-plan-verification.md:7` is dated 2026-10-03, but its checks are still to be run; today is 2026-10-05. Date the checks when they are actually run.
- Its scope line (line 16) omits two project-state changes: the "Owner decisions on the audit findings" table row and "In-progress work".
- `project-state.md:9` says "documentation initialization." while line 53 says "documentation initialization complete"; align them.
- PLT-029 (plan:63, 200) is about operating the platform, not development checks; GOV-023 alone covers U6.

## What I verified

- **Repository status:** `git status --short` was identical at start and end (four modified files, two untracked: the plan and its record). There was no stash, and HEAD stayed at bb19a60. All experiments ran in `scratchpad/gate3-plan/`.
- **Documentation tools:**
  - `python3 tools/docs/build_index.py --check-only`: exit 0 (734 requirements).
  - `python3 tools/docs/selftest.py`: PASS.
  - `python3 tools/docs/compare_requirements.py bb19a60 --strict`: 0 added, removed or changed; exit 0.
  - `ruff check`, `ruff format --check` and `mypy --check-untyped-defs` on `tools/docs`: all pass.
- **Diff hygiene:**
  - `git diff --check` on a copy with `git add -N` for the new files: exit 0.
  - Exactly six files changed; nothing under `tools/`, `CLAUDE.md` or `.gitignore`.
  - No secrets, local paths or model identifiers in changed or new files.
- **Environment claims:** `python3.12` is 3.12.3 and `uv` is 0.8.17. The package index is reachable: I installed pydantic 2.13.5 into a scratch virtual environment. The default `python3` is 3.11.15.
- **Citations:**
  - Every cited constitution Rule and master execution constitution § matches its use, as do the existence and text of the requirement IDs, except as noted in finding 2.
  - These sources say what the plan claims: A-05 (audit line 157), the DEC-035 CF-19 reading (lines 32–33), the governance "Status vocabularies" note (line 70), the tools README pinning note (line 63), DEC-009, DEC-025, DEC-036, and values register V-21.
- **Roadmap and registry:** every item in the FOUNDATION rows of all four roadmap tables is covered. ARCH-036 and ARCH-037 are covered only through the catch-all row.
- **Project memory:** the checkpoint log has bb19a60 filled in and ends with "The commit that adds this row". The gate table, continuation contract, next step, roadmap, `docs/README.md` and `docs/traceability/README.md` are consistent, and nothing says implementation is authorized.
- **Technical claims:** tested directly in the scratch area, as quoted in findings 3, 4 and 8.
```

## Run 3

- **Reviewer:** a fresh-context subagent, launched 2026-10-05, 18:08 UTC; report given 2026-10-05, 18:20 UTC
- **sha256:** `2d2403bf3afaec9321a7ed6d08b5fd94c680d856549da1d53ae2452607af0a89` as given; `d6ae9f81f5dff5929db058a6704ccd043b92b8b4fe5e2e19c0b139c8a7811613` as shown, with 2 local paths replaced

````text
Overall verdict: FAIL

Two blocking findings remain. The four original blockers (B1–B4) are fixed in substance. One blocker is new: project memory still describes the old 8-decision plan. The other is a security claim in a round-1 non-blocking fix (pydantic echoing input) that the experiment proved false.

## B1–B4

| # | Status | Evidence |
|---|---|---|
| B1 (dependencies and other choices not flagged) | Fixed, with one stale pointer and one small gap | D11 (plan l.240) lists every added dependency for the approving decision record. D2 covers locations, including the Rule 15 map. D3 covers `uv_build`. D4 covers actions pinned by commit hash. D8 covers contract conventions. OPS-010 is a design rule with no location (l.52). **Stale pointer:** the entry-gate row l.25 still says the dependencies are "listed in D1 to D3"; it should say D11 (part of finding 1). **Gap:** a coverage tool is implied but not flagged (finding 7). |
| B2 (later-stage requirements in scope) | Fixed | A script expanded every ID range in section 3 and compared it with the 100 requirements whose registry default stage is FOUNDATION and the 56 IDs named in roadmap FOUNDATION rows. Nothing is missing. The only non-FOUNDATION requirements given Stage 1 work are OPS-004, MODE-006 and MIG-027, all marked "prepared, not delivered". Other later-stage IDs appear only as "completed in" or "applied in" entries. testcontainers is deferred. One residual: GOV-023 is given two dispositions (finding 10). |
| B3 (float protection presented as sufficient) | Fixed; reproduced | python3.12, traps set by mutating `DefaultContext`'s fields: `Decimal(0.1)` → FloatOperation; `1/3` → Inexact; `<` against a float → FloatOperation; `==` against a float and `Decimal.from_float` pass silently, as the plan says. The same held in the main thread, a new thread, `asyncio.to_thread`, and a new asyncio task. `tomllib.loads(..., parse_float=Decimal)` works with FloatOperation trapped. Two caveats: findings 3 and 4. |
| B4 (outcome exhaustiveness not type-enforced) | Fixed; reproduced | mypy 1.19.1 `--strict --enable-error-code truthy-bool`: a `fold` call missing a handler gives `[call-arg]`. With `__bool__` under `if not TYPE_CHECKING:`, `if o:`, `not o`, `o and`, `while o` and `assert o` give `[truthy-bool]`, and `bool(o)` raises at runtime. A `__bool__ -> NoReturn` visible to mypy silences truthy-bool, as the plan says. An unused `# type: ignore[call-arg]` gives `[unused-ignore]`, exit 1. The same holds for a pydantic generic model. One caveat: finding 5. |

## New findings

**1. BLOCKING — project memory still describes the old 8-decision plan.**
- `docs/project-state.md` says "D1 to D8" or "eight decisions" at l.45, 54, 196, 286, 290 and 291. The plan has D1–D11.
- l.291 tells the builder: "record the approval and D1 to D8 in a decision record". That would leave out D9–D11, including D11's dependency list, which is how the B1 fix works.
- Plan l.25 says "listed in D1 to D3".
- This is a memory/consistency defect: master execution constitution §87 and §158, constitution Rule 173.
- Fix: say "D1 to D11" (eleven decisions) at all six places, and change l.25 to "listed in D11".

**2. BLOCKING — `hide_input_in_errors` does not stop errors echoing a secret.**
- Plan l.114 claims "input values hidden from validation errors (`hide_input_in_errors`) so that an error can never echo a secret". D8 (l.237) asks approval for "errors that never echo input". Acceptance at l.118 and l.133 only requires that "an error message" not contain the value.
- Reproduced with pydantic 2.13.5:
  - With `hide_input_in_errors=True`, `str(e)` and `repr(e)` hide the value, but `e.errors()` and `e.json()` still contain it.
  - A custom validator's message (`ValueError(f"... {v}")`) echoes it.
  - `e.errors(include_input=False)` and `e.json(include_input=False)` do hide it.
- With structured JSON logs (TEC-010), the approved design would leak secrets past a test that passes. That breaks SEC-005 and DEC-032's rule against tests that do not prove the behaviour. It is the same pattern as B3.
- Fix: state that `hide_input_in_errors` affects only the string form; validation errors are rendered or logged only through one function using `include_input=False`; validators never put input in messages. The acceptance test should check `str(e)`, `e.errors()`, `e.json()` and captured log output.

**3. Non-blocking — `DefaultContext` must be changed in place (l.103, D7 l.236).**
Rebinding `decimal.DefaultContext = Context(...)` has no effect on new threads under CPython's C decimal: a thread got prec 28 and no traps. Only setting the fields of the existing object works. The planned thread test would catch it. Fix: say "the fields of `decimal.DefaultContext` are set (rebinding the name has no effect)".

**4. Non-blocking — side effects of trapping `Inexact` process-wide (l.103–107; risk row l.259).**
- With `Inexact` trapped, `quantize` raises Inexact even when a rounding mode is given. The named-direction rounding functions must therefore use their own context with `Inexact` untrapped.
- Under the trapped `DefaultContext`, Hypothesis's unbounded `st.decimals()` raised Inexact; bounded or `places=` strategies passed.
- Fix: state both facts in U2.

**5. Non-blocking — B4 claim is slightly too broad (l.116).**
- `bool(o)` is not reported by `truthy-bool`; it only raises at runtime.
- Any public `kind` attribute lets callers bypass `fold`: a test showed `if o.kind is not Kind.FAILURE` letting UNKNOWN through.
- Fix: say "most truth-value uses" are type errors; keep the outcome's kind and value non-public; enforce with a lint rule such as ruff SLF001 or the structure test.

**6. Non-blocking — `uv sync --frozen` ignores a stale lockfile (l.88, l.197; the U6 workflow).**
Tested: after adding a dependency to pyproject without relocking, `--frozen` exits 0 and `--locked` exits 1. Fix: use `uv sync --locked` (or `uv lock --check`) in the clean-clone check and in CI.

**7. Non-blocking — a coverage tool is implied but not flagged (l.201).**
"The coverage that is measured is recorded" needs coverage.py or pytest-cov. Neither is in TEC-009 or D11. Fix: add it to D11, or state it is run once outside the project like the vulnerability scanner (l.87), or drop the measurement.

**8. Non-blocking — wording contradicts MIG-010 (l.127).**
"Portable configuration never holds policy content" conflicts with MIG-010, which lists policies as portable configuration. Fix: use the source-of-truth map's reading (l.145): the repository's portable configuration files hold no policy content; policies, which are portable configuration under MIG-010, live only in the Policy System's store (POL-009) and move with the platform state (MIG-008). Also cite MIG-010, not MIG-004, for "host paths and addresses".

**9. Non-blocking — the trading-credential guard has nothing to inspect (l.127, l.130, l.194).**
The Stage 1 settings list (platform ID, environment name and ID, secret names) has no attribute marking a credential as trading-enabled, so the guard and its negative test have nothing to check. Fix: define each secret declaration as a name plus a kind, and state that example files hold placeholders only, with no real venue credential names (GOV-017).

**10. Non-blocking — GOV-023 has two dispositions.**
It is "delivered" in 3.1 (l.44) and also a design rule in 3.3, through the range "GOV-019 to GOV-024" (l.58). Fix: write "GOV-019 to GOV-022, GOV-024" in 3.3.

**11. Non-blocking — the traceability acceptance cannot be met as worded (U7 l.147; criterion 3 l.217).**
"Every requirement of section 3.1 has at least one implementing module and one test" cannot hold for SEC-001 (a threat-model document), GOV-023 (a workflow file) or ARCH-032 (tested by `selftest.py`, not pytest markers). Fix: say which kinds of artifact count as implementation and test for those.

**12. Non-blocking — owners of the new modules are not named.**
- The plan never says which entry owns `atp.numeric`, `atp.contracts` and `atp.config`. Gate 2 requires "one owner" (l.208) and the matrix has a system column.
- It does not say how `atp.config` relates to the later configuration compiler (MIG-011) without becoming a second configuration source (GOV-014).
- Fix: name the Rule 15 map rows in D2. The registry's owner column already gives "Platform architecture (cross-cutting)", "Technology stack", "Hosting, backup, and migration" and SYS-31. State the MIG-011 relation, and put the matrix file location in D2.

**13. Non-blocking — two later-stage placements are imprecise (l.52, l.68, l.163).**
- "DATA FOUNDATION (first service)" for OPS-010 is a placement the roadmap does not make. Better: "with the first deployable service".
- TEC-013's execution lease is built in CORE TRADING FOUNDATION with REC-013 (roadmap stage row 3), not only in OPERATIONALIZATION.

**14. Non-blocking — the verification record is missing two required sections.**
`docs/traceability/stage-01-plan-verification.md` has no "Failures and fixes" or "Environment" section, both required by the traceability README format. The failed first Gate 3 round (B1–B4 and its non-blocking items, each with its fix) must be recorded (§19, DEC-032).

**15. Non-blocking — dates are stale.**
- `project-state.md` l.5 still reads "Last updated: 2026-10-03".
- l.195 and l.286 date the plan 2026-10-03 only; the record says it was revised on 2026-10-05.
- `docs/security/security-architecture.md` l.50 still lists "Threat model" as not yet specified. Completion criterion 5 should include updating it.

Checked and found correct:
- Every constitution Rule and master execution constitution § the plan cites matches its heading. That covers 18 rule groups and 18 sections; §95 is Handoff Part 1.
- A-05, DUP-32, CF-19 (DEC-035 l.32–33), the "fixed when Stage 1 is planned" reading in Architecture governance, and TC-09/TC-10 are all real and correctly described.
- Entry gate (§12), the Rule 140 fields and §142 are all covered.
- No contradiction with TEC-001–013, SEC-001/004/005/006, POL-009, ARCH-018/026, GOV-014 or OPS-010, apart from finding 8.
- Every directory is created at the checkpoint that first puts a real file in it; no speculative structure found (Rules 9–14; GOV-020).
- Nothing says implementation is authorized.
- The checkpoint log has bb19a60 filled in and ends with "The commit that adds this row".
- `docs/README.md` and `docs/traceability/README.md` link the new files, and the roadmap header, Rule 140 note and FOUNDATION status are consistent.

## What I verified

All experiments ran in a copy at `<scratchpad>/gate3-plan2/` (`repo/`, `exp/`, plus `scope.py`).

**Environment:** python3.12 3.12.3 (note: `python3` is 3.11.15); uv 0.8.17; mypy 1.19.1; ruff 0.15.8; PyPI reachable (HTTP 200); pydantic 2.13.5 and hypothesis installed in a scratch venv. The plan's environment claims are true.

**Tools and hygiene (all on the copy):**

| Command | Result |
|---|---|
| `python3 tools/docs/build_index.py --check-only` | exit 0; 734 requirements |
| `python3 tools/docs/compare_requirements.py bb19a60 --strict` | exit 0; 0 added, 0 removed, 0 changed |
| `python3 tools/docs/selftest.py` | PASS |
| `ruff check tools/docs`; `ruff format --check tools/docs`; `mypy --check-untyped-defs tools/docs` | all pass |
| `git add -N` on the two new files, then `git diff --check` | exit 0 |
| Scan of changed and new files for secrets, local paths, model identifiers | nothing found |

**Technical experiments:**
- Decimal behaviour in main thread, new thread, `to_thread` and asyncio task, with the context's fields set versus the name rebound.
- tomllib with `parse_float=Decimal` while FloatOperation is trapped.
- `quantize` with Inexact trapped.
- mypy: missing fold handler, hidden `__bool__` with truthy-bool, visible NoReturn `__bool__`, unused `type: ignore`; also on a pydantic generic model.
- `uv init --lib --build-backend uv` then `uv build`: built sdist and wheel; pyproject requires `uv_build>=0.8.17,<0.9.0`.
- `uv sync --frozen` versus `--locked` on a stale lockfile.
- pydantic `hide_input_in_errors`, `errors()`/`json()` with and without `include_input=False`, and strict-mode JSON decimals: JSON numbers are accepted by plain `Decimal`, so the custom amount type the plan describes is needed.
- Scripted section-3 scope check.

**Repository status (in `<repository>`, HEAD bb19a60):** identical at start and end, no stash created.
```
 M docs/README.md
 M docs/project-state.md
 M docs/roadmap/roadmap.md
 M docs/traceability/README.md
?? docs/roadmap/stage-01-foundation-plan.md
?? docs/traceability/stage-01-plan-verification.md
```
````

## Run 4

- **Reviewer:** a fresh-context subagent, launched 2026-10-05, 18:22 UTC; report given 2026-10-05, 18:34 UTC
- **sha256:** `ffc116620137797675124e6e27730919b9496bd9e3a3a1b6d29803c7d86b0c2a` as given; `38ce1862eecf85779a53f0c2542f8fed9b2e6de51077ab1ac5e33f267d03ab7c` as shown, with 2 local paths replaced

```text
Overall verdict: PASS

The checkpoint has no blocking findings. Both blocking findings from run 3 are fixed, and their technical claims hold when reproduced. All 13 non-blocking findings from run 3 are fixed, with two partial residues listed below (4 and 13). I also found 10 new non-blocking findings.

## Run-3 findings

| # | Status | Evidence |
|---|---|---|
| 1 (BLOCKING) | Fixed | grep finds no "D1 to D8", "eight decisions" or "D1 to D3" anywhere. Project state lines 45, 54, 196, 286, 290–291 say "D1 to D11" / "eleven decisions". Plan line 25 points to D11. |
| 2 (BLOCKING) | Fixed, and correct | Pydantic 2.13.5 with `hide_input_in_errors=True`: the input is hidden from `str(e)` and `repr(e)` but still present in `errors()` and `json()`. With `include_input=False` it is gone. A validator whose `ValueError` message contains the input leaks it in every form, so line 114's rule ("no validator puts an input value into its message") is needed. Residue: new finding 4. |
| 3 | Fixed, correct | Rebinding `DefaultContext` leaves a new thread at prec 28 with no traps. Changing the fields in place carries into both threads and asyncio tasks. |
| 4 | Partly fixed | `quantize(..., ROUND_DOWN)` raises `Inexact` while `Inexact` is trapped; a local context with `Inexact` untrapped works. The Hypothesis wording is wrong (new finding 2), and the local-context mechanism is not enough for increments (new finding 1). |
| 5 | Fixed, correct | mypy 1.19.1 and 2.4.0, strict plus `truthy-bool`: `if`, `while`, `not`, `and`, `or`, `assert`, ternaries and comprehension conditions are all reported. `bool(o)` is not reported but raises at runtime. A visible `__bool__ -> NoReturn` silences the check and also makes the code after it unreachable, so the missing-handler error disappeared. A missing `fold` handler is reported as `[call-arg]`. Unused ignores are reported as `[unused-ignore]`. Ruff SLF001 flags `o._kind`. |
| 6 | Fixed, correct | With a stale lockfile, `uv sync --locked` exits 1 and leaves the lock unchanged. `uv sync --frozen` exits 0 and silently omits the new dependency. |
| 7 | Fixed | Plan line 201. Section 8 does not repeat the check (new finding 6). |
| 8 | Fixed | Line 127 matches the source-of-truth map's line 145 and MIG-010, POL-009 and MIG-008. |
| 9 | Fixed | Lines 127 and 130 add a closed set of kinds and placeholder-only example files. |
| 10 | Fixed | A script shows GOV-023 has exactly one disposition (section 3.1). |
| 11 | Fixed | Line 147. |
| 12 | Fixed | D2 (line 231); owners match the registry's Owner column. |
| 13 | Partly fixed | Lines 52 and 68 are fixed, but the risk table at line 262 still says "until DATA FOUNDATION" (new finding 5). |
| 14 | Fixed | The record has a "Failures and fixes" section; Environment is a paragraph at line 35. |
| 15 | Fixed | Project state is dated 2026-10-05; criterion 5 (line 219) names the security architecture's "Not yet specified" line (security-architecture.md:50). |

## New findings (all non-blocking)

1. **Rounding to an increment can move a value the wrong way** (plan lines 102–105). "Their own local context with `Inexact` untrapped" lets the division step round silently. In practice, at prec 34, x = `9.899999999999999999999999999999999` (34 digits) with increment `0.3`: `(x/inc).to_integral_value(ROUND_FLOOR)*inc` gives `9.9`, which is above x. `divmod` gives the correct `9.6`. Separately, the constructor and Pydantic accept a 41-digit amount, which then raises only later, inside arithmetic.
   - Fix: compute the quotient and remainder exactly (`divmod` or `%`, which fail closed under the trapped context), and untrap `Inexact` only for the final `quantize`.
   - Have the constructor refuse more significant digits than the precision.
   - Add full-precision, near-boundary cases to the property tests.
2. **The Hypothesis claim at line 104 is wrong.** It says strategies are bounded "with `places=` or limits". In practice `st.decimals(min_value=..., max_value=...)` without `places=` raised `Inexact` in 5 of 5 runs, for both (-1, 1) and (0, 100). With `places=`, with or without limits, it raised 0 of 5. Fix: "with `places=`; limits alone still raise". Correct record line 67 to match.
3. **Checkpoint A has no real test.** pytest returns exit code 5 when it collects no tests, so U1's "`uv run pytest` pass" (line 88) and the U6 workflow fail at checkpoint A, unless a placeholder test is written, which is not allowed. Fix: name the first real test at A, for example by moving U5's repository secret test to checkpoint A, or state that pytest joins the workflow at B.
4. **Error locations can still carry input** (lines 114, 118). The `loc` field contains keys taken from the input: unknown field names and mapping keys. It keeps them even with `include_input=False` and `hide_input_in_errors`. In practice `M.model_validate({"n":1,"s":"x", SECRET: 1})` puts the secret into `str(e)`, `errors(include_input=False)`, `json(include_input=False)` and the logs. Fix: the error function also redacts `loc` segments that come from the input, and the acceptance test covers a secret used as a key.
5. **Leftover stage name at line 262.** It says "OPS-010 has no content until DATA FOUNDATION", while lines 52 and 163 say "the first deployable service". Fix: "until the first deployable service".
6. **Sections 7 and 8 do not match.** Line 201 says the check that every public function has a test is done in Gate 2, but Gate 2 (line 208) does not list it. Fix: add it to the Gate 2 bullet. The Structure row (line 196) leaves out two of U2's repository-test rules: no `Decimal(...)` outside `atp.numeric`, and no `create_decimal_from_float`. It also leaves out U3's private-member check. Fix: list them in that row.
7. **Two module boundaries conflict** (line 208 against lines 114 and 106). The command-line module "imports only `atp.config`", but errors may be rendered only through one function, which presumably lives in `atp.contracts`. Fix: say that `atp.config` returns already-rendered errors, or allow the command line to import `atp.contracts`. Also, `parse_float=Decimal` in `atp.config` builds a Decimal outside `atp.numeric`. Fix: use the `atp.numeric` constructor as `parse_float`.
8. **The build backend is not in the lockfile** (line 86 says "All versions pinned in the lockfile"). In practice the generated `uv.lock` has no `uv_build` entry; `pyproject.toml` has `uv_build>=0.8.17,<0.9.0`. D11 (line 240) states this correctly. Fix: reword U1, or pin `uv_build==<x>` exactly for reproducibility (Rule 102).
9. **Marker checker scope** (line 146). It refuses unknown and replaced IDs, but a marker naming a PROPOSED or FUTURE requirement, such as ARCH-034, would pass. Fix: refuse those too (ARCH-029, GOV-017).
10. **Minor wording and completeness**
    - project-state.md:195 "Stage 1 plan (…; authorized by DEC-036)" reads as if the plan itself were approved. Fix: "planning authorized by DEC-036".
    - Record line 35 lists the tool versions but leaves out the Hypothesis version (6.168.4 in the scratch environment); the same environment also has mypy 2.4.0.
    - For GOV-023, U7 (line 147) names only the workflow as evidence. Fix: add U1's developer guide and the clean-clone run.
    - The plan never names the systems affected (the roadmap gives "Documentation set; SYS-31"). §142 asks for them in the stage record; noting them now would help.

## What I verified

- **Status:** `git status --short` was identical at start and end (` M docs/README.md`, ` M docs/project-state.md`, ` M docs/roadmap/roadmap.md`, ` A docs/roadmap/stage-01-foundation-plan.md`, ` M docs/traceability/README.md`, ` A docs/traceability/stage-01-plan-verification.md`). The intent-to-add entries were left alone; no stash was made; HEAD is still bb19a60. Code checks and experiments ran on a copy in `scratchpad/gate3-plan4/`.
- **Documentation tools:**
  - `build_index.py --check-only`: exit 0 (734 requirements).
  - `compare_requirements.py bb19a60 --strict`: 0 added, 0 removed, 0 changed.
  - `selftest.py`: PASS.
  - `git diff --check`: exit 0, also with `--cached`.
  - No trailing whitespace or tabs in the new files.
  - On the copy: ruff check and format on `tools/docs` are clean; `mypy --check-untyped-defs tools/docs` passes.
- **Hygiene:** I scanned the added lines and the new files for local paths, model names, API-key and token patterns. The only hits were "RSK-0xx" IDs.
- **Scope, by script:** all 76 registry FOUNDATION requirements, the 24 "applies to every stage" ones, MIG-004 and MIG-010, and every ID in the roadmap's FOUNDATION rows each have exactly one disposition in section 3. RSK-049 also appears in section 3.5, but only as the replacement for RSK-048. The only extras are MIG-027, MODE-006 and OPS-004 (all "prepared, not delivered") and PLT-029 (platform-wide). Nothing from a later stage is in section 3.1, and every later-stage placement matches the roadmap rows.
- **Citations:** every constitution Rule and master execution constitution § cited matches its heading. Bare §95 means Handoff Part 1 §95. I read each cited requirement in its specification, along with DEC-035 and DEC-036, A-05, the source-of-truth map and the values register. I found no contradiction with any approved requirement. Choices beyond requirements are marked and listed in D1–D11; the exact interpreter 3.12 is unmarked but sits within TEC-001 and V-21.
- **Plan completeness:** the Rule 140 fields, the §12 entry gate and the stage-record fields are covered. No speculative structure: each directory is created with its first artifact.
- **Environment claims:** Python 3.12.3, uv 0.8.17, network access to the package index. `uv init --lib --build-backend uv` produced `uv_build`, and `uv build` built both an sdist and a wheel.
- **Other technical claims:**
  - The `FloatOperation` trap stops `Decimal(0.1)` and `<` against a float, but not `==` or `from_float`.
  - `tomllib` with `parse_float=Decimal` works; `inf` becomes `Decimal('Infinity')`.
  - Strict Pydantic accepts JSON numbers for `Decimal`, and its default schema allows `number`; a custom string-only type refuses numbers and its schema says string.
- **Project memory:** project state, roadmap, `docs/README.md` and `docs/traceability/README.md` agree with each other, and none says implementation is authorized. The checkpoint log has bb19a60 filled in and ends with "The commit that adds this row". The verification record follows the README's format, and its account of runs 1–3 is accurate; its checks, gates and final status are still placeholders, as expected.

Everything I created is in `<scratchpad>/gate3-plan4/` (in `exp/`: `pyd.py`, `pyd2.py`, `pyd3.py`, `dec1-3.py`, `hyp.py`, `hyp2.py`, `mypyt/`, `uvt/`, `emptyt/`; the repository copy in `repo/`). The scope script is at `<scratchpad>/scope.py`.
```

## Launches that stopped before reporting

- Run 1: launched 2026-10-03, 01:14 UTC; it stopped at the weekly usage limit before it reported, so no report exists.
