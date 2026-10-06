# Stage 1 — FOUNDATION: Plan

> **Status:** APPROVED by the owner on 2026-10-05, with D1 to D11 as recommended; **Stage 1 implementation is authorized** ("Begin Stage 1", [DEC-038](../decisions/DEC-038-stage-1-plan-approved.md); [owner decisions 6](../handoffs/owner-decisions-06-stage-1-plan.md)). Planning was authorized on 2026-10-03 ([DEC-036](../decisions/DEC-036-owner-decisions-audit-findings.md)). The authorization covers Stage 1 only; it does not approve later architecture changes (constitution Rule 136). Progress is recorded in the stage record, created at the start of checkpoint A.
>
> The fields of constitution Rule 140 (objective, in scope, out of scope, dependencies, outputs, tests, verification, completion criteria) for the first stage of the [master roadmap](roadmap.md). Every choice this plan makes that is not already a requirement or decision was marked **RECOMMENDED — NOT YET APPROVED** (constitution Rule 180) and listed under "Decisions this plan asks for" (D1 to D11); the owner approved all eleven as recommended ([DEC-038](../decisions/DEC-038-stage-1-plan-approved.md)). That record also approves every dependency Stage 1 adds, since adding a dependency not named in the [technology stack](../architecture/technology-stack.md) requires a decision record (constitution Rules 99–101).

## 1. Objective

Turn the approved documentation foundation into the first verified code foundation that every later stage builds on, without building any trading capability:

- a reproducible development environment with pinned tools (constitution Rule 105; TEC-009);
- the shared, cohesive building blocks every system needs from its first line: exact decimal amounts (ARCH-010, TEC-003), the contract kernel for validated, versioned interfaces (ARCH-025, ARCH-026, GOV-006, TEC-004), the result type in which UNKNOWN is never SUCCESS (ARCH-042), idempotency keys (ARCH-041), and validated configuration with a portable and an environment-specific part and secret handling (MIG-004, MIG-010, SEC-005);
- a testing foundation, machine checks of every push, and the first link from requirements to implementation and tests (ARCH-030, ARCH-031, ARCH-040; the verification matrix of the [traceability README](../traceability/README.md));
- the stage record, feature-status recording, and the three gates working on real code.

Systems affected, as the roadmap names them for Stage 1: the documentation set and SYS-31 Security Architecture (its foundation); the new modules are cross-cutting and owned as D2 sets out.

At the end of Stage 1 the platform still cannot connect to an exchange, hold market data, or place an order. That is by design (RMP-002, RMP-011).

## 2. Entry gate (master execution constitution §12)

| Condition | Status | Evidence |
|---|---|---|
| Prerequisite stages complete | Not applicable: Stage 1 is the first stage | [Roadmap](roadmap.md), RMP-002 |
| Required architecture exists | Yes | [Architecture overview](../architecture/overview.md), [system registry](../architecture/system-registry.md), [technology stack](../architecture/technology-stack.md) |
| Required contracts exist | Not needed before Stage 1: Stage 1 creates the contract kernel; system contracts are defined when their stages are planned (ARCH-025; audit finding A-05) | Section 4, U3 |
| Required dependencies exist | Yes: the stack is decided (DEC-009); the documentation tooling exists (DEC-025). The dependencies Stage 1 adds are listed in D11 for the approving decision record | [DEC-009](../decisions/DEC-009-technology-stack.md), [tools/docs](../../tools/docs/README.md) |
| Required decisions approved | Yes, except those this plan asks for (section 10) | [Decision log](../decisions/README.md) |
| Required documentation exists | Yes: the complete documentation review is accepted | [DEC-036](../decisions/DEC-036-owner-decisions-audit-findings.md) |
| Required environment available | Observed in the builder's environment on 2026-10-05: Python 3.12.3, uv 0.8.17, network access to the Python package index. Re-checked and recorded in the stage record when the stage starts | [Stage 1 plan verification](../traceability/stage-01-plan-verification.md), check 7 |

## 3. Requirements and their disposition in Stage 1

The roadmap places requirements in Stage 1 through its FOUNDATION rows (Handoff Part 1 §95's items; the Part 2, Part 3, and 2026-10-01 additions) and through the registry's default stage. Where the roadmap places a requirement in a later stage, the roadmap is authoritative ([registry](../requirements/registry.md), "Default stage"). Every requirement whose registry default stage is FOUNDATION, and every requirement a FOUNDATION row of the roadmap names, appears below with what Stage 1 does about it.

### 3.1 Delivered by Stage 1 code

| Requirements | What Stage 1 delivers | Unit |
|---|---|---|
| TEC-001, TEC-008, TEC-009 (testcontainers excepted: it belongs with storage, DATA FOUNDATION) | Project definition, lockfile, pinned lint, format, type, and test tools; one codebase with explicit modules | U1 |
| ARCH-010, TEC-003 | One amount constructor, explicit rounding, the decimal context policy | U2 |
| ARCH-025, ARCH-026, GOV-006, GOV-007, TEC-004 | The contract kernel and its versioning and compatibility rules, with committed JSON schemas | U3 |
| ARCH-041, ARCH-042 (the types; their enforcement in execution, capital, and recovery is CORE TRADING FOUNDATION's, roadmap row 3 of the 2026-10-01 additions) | The idempotency key type and the four-result outcome type | U3 |
| MIG-004, MIG-010, SEC-005, ARCH-018 | Validated configuration split into portable and environment-specific parts; secrets only from the runtime environment; the decimal precision entered in the values register | U2, U4 |
| ARCH-013, ARCH-030, ARCH-031, ARCH-040, ARCH-032 (a further increment of the consistency checker of [DEC-025](../decisions/DEC-025-documentation-tooling-in-repository.md)) | Requirement markers in code and tests; the generated verification matrix; the checker refuses unknown or replaced IDs | U7 |
| GOV-012, GOV-023 | Test layout and conventions; the same checks run by machine on every push | U6 |
| SEC-001 | A design-level threat model over the assets SEC-001 names | U5 |

### 3.2 Started in Stage 1, completed in a later stage

| Requirement | Stage 1 | Completed in |
|---|---|---|
| ARCH-011 | Quantization to an increment with a named rounding direction | DATA FOUNDATION, which supplies each venue's increments |
| OPS-010 | Applied as a design rule: no deployment definition is created anywhere; Stage 1 has nothing deployable, so none is written. The definition's single location is fixed with the first deployable service | The stage that builds the first deployable service; OPERATIONALIZATION (deployment package: OPS-007, OPS-008, OPS-011 to OPS-017; OPS-009 was replaced by OPS-014 to OPS-017) |
| OPS-004, MIG-027 (prepared, not delivered) | The six environment names of OPS-004 and the platform and environment identifiers of MIG-027 exist as validated configuration values | OPS-004's separate configuration, database, and credentials per environment: OPERATIONALIZATION; MIG-027: OPERATIONALIZATION |
| MODE-006, SEC-004 (prepared, not delivered) | Defence in depth only: a configuration that declares trading-enabled credentials is refused unless its environment is production (constitution Rules 109, 111; §95's "Configuration" and "Security foundation"). The real barrier is that no trading credential exists outside production, which no Stage 1 artifact can provide | CORE TRADING FOUNDATION (MODE-006); the stages that first hold credentials (SEC-004) |

### 3.3 Applied as design rules to Stage 1's own work, verified in Gate 2

ARCH-001 to ARCH-009, ARCH-012, ARCH-014 to ARCH-017, ARCH-019 to ARCH-024, ARCH-027 to ARCH-029, ARCH-033, ARCH-035 to ARCH-039; GOV-001 to GOV-005, GOV-008 to GOV-011, GOV-013 to GOV-017, GOV-019 to GOV-022, GOV-024; RMP-001 to RMP-009, RMP-011, RMP-012; RSK-049 (rule precedence; enforced from CORE TRADING FOUNDATION); PERF-023 (no unsafe fast path); PLT-022 to PLT-029. Most of them are already met by the documentation foundation (the [master knowledge-base audit](../traceability/master-knowledge-base-audit-2026-10-02.md)); Stage 1 must not break any of them. GOV-009 and GOV-024 are also the subject of D5 and D6.

### 3.4 Decided, applied in later stages (not built in Stage 1)

| Requirement | Applied in |
|---|---|
| TEC-002 (Rust only after measurement) | When measurement shows a Python bottleneck (PERF-006) |
| TEC-005, TEC-006, TEC-007, TEC-012 | DATA FOUNDATION and later |
| TEC-010 (observability stack) | From the first running service |
| TEC-011 (Docker images, Compose) | From the first deployable service |
| TEC-013 (supervision and execution lease) | The execution lease with REC-013 in CORE TRADING FOUNDATION; 24/7 supervision in OPERATIONALIZATION (roadmap) |
| RMP-010 (production hardening) | OPERATIONALIZATION |
| SEC-002, SEC-008 | AI INTELLIGENCE |
| SEC-006, SEC-007 | ARBITRAGE (transfers) |
| SEC-009 | OPERATIONALIZATION |

### 3.5 Not built

ARCH-034 (PROPOSED, in no stage); SEC-003, GOV-018, and RSK-048 (DEPRECATED / REPLACED; RSK-048, named in the roadmap's FOUNDATION row, was replaced there by RSK-049).

## 4. In scope: work units

Each unit is a coherent, recoverable piece of work (master execution constitution §08) with its own acceptance criteria. Units are grouped into four checkpoints; each checkpoint passes the three gates before its commit (DEC-032, DEC-033).

### U1 — Development environment and repository layout (checkpoint A)

- **Purpose:** anyone can install, check, and test the platform from a clean clone with one documented sequence of commands, and get the same tool versions (constitution Rule 105; TEC-009; GOV-023).
- **Files:** `pyproject.toml`; `uv.lock`; `.python-version`; `src/atp/` (D1); `tests/`; ignore rules in `.gitignore`, including local environment and secret files; the repository test of U5 that fails if a tracked file looks like a secret file or contains a secret-like value, which is the first real test, so `pytest` has something to run from checkpoint A; the developer guide (D2).
- **Content:** Python 3.12, the lowest version TEC-001 allows; runtime dependency Pydantic v2 only (TEC-004); development dependencies pytest, Hypothesis, ruff, mypy (TEC-009); the build backend of D3. The libraries and tools are pinned in the lockfile; the build backend, which the lockfile does not record, is pinned to one exact version in `pyproject.toml` (constitution Rule 102). mypy in strict mode for `src/` and `tests/`, with the `truthy-bool` error code enabled (TEC-001; U3). No other dependency is added without a decision record (the technology stack's rule; constitution Rules 99–101).
- **Dependency review:** the locked dependencies are checked against the published vulnerability advisories (for example with a vulnerability scanner run once, not added to the project), and the result is recorded in the stage record (master execution constitution §40).
- **Acceptance:** `uv sync --locked` from a clean clone installs exactly the lockfile and fails if the lockfile does not match `pyproject.toml`; `uv run ruff check`, `uv run ruff format --check`, `uv run mypy`, and `uv run pytest` pass; `uv build` builds the package; the documentation tools run unchanged. The tool versions are pinned, which closes the [tools README](../../tools/docs/README.md)'s note that they are not pinned yet.

### U6 — Testing foundation and machine checks (checkpoint A)

- **Purpose:** every change is checked the same way, by a machine, whether or not Claude Code is present (GOV-023; master execution constitution §22).
- **Files:** pytest and Hypothesis configuration in `pyproject.toml`; test layout under `tests/` mirroring `src/atp/`; the workflow of D4, `.github/workflows/checks.yml`.
- **Content:** the workflow runs, on every push and pull request: the documentation checker (`build_index.py --check-only`), the tools' self-test, ruff, mypy, and pytest, with the locked dependencies. It installs with `uv sync --locked`, uses no secrets, deploys nothing, and has read-only repository permissions; every action it uses is pinned to a commit hash.
- **Acceptance:** the workflow passes on the branch; a deliberately broken check makes it fail (recorded as a negative test in the stage record).

### U2 — Exact amounts (checkpoint B)

- **Purpose:** one canonical way to create and round financial amounts, so that no later system reimplements it and no float reaches one (master execution constitution §30, §38, §39; ARCH-010; TEC-003).
- **Files:** `src/atp/numeric/`; tests under `tests/numeric/`; the numerical policy (D2).
- **Content (D7):**
  - **One amount constructor.** It accepts only `str`, `int` (not `bool`), and `Decimal`, and refuses NaN, infinities, and values with more significant digits than the context precision, so an over-long amount is refused when it enters, not later inside arithmetic. Code outside `atp.numeric` does not build amounts with `Decimal(...)` directly; a repository test checks this, and also refuses any use of `Decimal.from_float` and `create_decimal_from_float` in `src/`.
  - **Decimal context, set once at process start,** by setting the fields of the current context and of `decimal.DefaultContext` in place (rebinding the name `DefaultContext` has no effect on new threads), so that new threads and asyncio tasks inherit it: the precision (an IMPLEMENTATION CHOICE entered in the [values register](../requirements/values-register.md) with its reason, ARCH-018) and the traps `FloatOperation`, `InvalidOperation`, `DivisionByZero`, `Overflow`, and `Inexact`. The `FloatOperation` trap is one layer only: it stops `Decimal(0.1)` and mixed ordering comparisons, but not equality comparisons with floats or the explicit float conversions, which is why the constructor and the repository test above exist.
  - **Rounding only on request.** Because `Inexact` is trapped, an operation whose exact result does not fit raises instead of rounding silently. Rounding happens only through functions that name the direction: toward zero, away from zero, toward minus infinity, toward plus infinity (the meanings of `decimal`'s `ROUND_DOWN`, `ROUND_UP`, `ROUND_FLOOR`, `ROUND_CEILING`), so the result is defined for negative amounts too. With `Inexact` trapped even `quantize` with a rounding mode raises, so each rounding function untraps `Inexact` in a local context for its final `quantize` only. Every intermediate step stays under the trapped context and is computed exactly: rounding to an increment uses the exact quotient and remainder (`divmod`), never a rounded division, because a rounded quotient can move a value in the wrong direction (for example, at 34 digits, 9.899…9 rounded down to a multiple of 0.3 must give 9.6, not 9.9). The same trap affects tests: Hypothesis's decimal strategies are always given `places=`; limits alone still raise `Inexact`.
  - **Quantization to an increment** (tick size, step size) with a named direction; a zero or negative increment is refused (ARCH-011).
  - **Amounts in text:** in JSON, amounts are strings only; a JSON number is refused and the committed schema says so. In TOML, numbers are read with the `atp.numeric` amount constructor as `parse_float`, so no float is ever produced and no `Decimal` is built outside `atp.numeric`.
- **Acceptance:** property tests (Hypothesis) show: a float, a `bool`, NaN, and an infinity are refused by the constructor; quantizing never moves a value in the opposite of the named direction, never by a full increment or more, and behaves as named for negative values, including at full precision next to an increment boundary; an amount with more digits than the precision is refused; string round trips are exact; an inexact result raises unless a rounding function is used. Unit tests show the context holds in a new thread and in a new asyncio task, that a JSON number for an amount is refused, and that a TOML number becomes a `Decimal`. The repository test fails on a planted `Decimal.from_float` in a copy.

### U3 — Contract kernel, outcomes, idempotency (checkpoint B)

- **Purpose:** the base every interface contract is built on, so that contracts are explicit, validated at every boundary, and versioned (ARCH-025, ARCH-026, GOV-006, GOV-007, TEC-004), and the two design rules every external operation follows from the first stage (ARCH-041, ARCH-042).
- **Files:** `src/atp/contracts/`; tests under `tests/contracts/`; committed JSON schemas under `contracts/` (D2), created with the first schemas at this checkpoint (the amount, outcome, and idempotency-key types; checkpoint C adds the configuration schemas); the contract conventions (D2).
- **Content (D8):**
  - a base contract model: Pydantic v2 in strict mode, immutable, unknown fields refused, collections held as tuples so nested values are immutable too, amounts as strings (U2). Validation errors never carry input values: `hide_input_in_errors` hides them only from an error's string form, while its structured forms (`errors()`, `json()`) still contain them, so errors are rendered or logged only through one function that leaves input out (`include_input=False`) and also redacts every part of an error's location that comes from the input (an unknown field name, a mapping key), since the location keeps those even without input; no validator puts an input value into its message;
  - a contract identity and a version `MAJOR.MINOR` on every contract: a change that can break a consumer needs a new major version; the compatibility check refuses to treat different major versions as compatible (ARCH-026); a committed schema that changes without a version change fails the tests;
  - the outcome type, with exactly the four results ARCH-042 names, SUCCESS, FAILURE, TIMEOUT, and UNKNOWN. It can be consumed only through a `fold` that requires one handler for each of the four, so the type checker rejects code that leaves one out; using an outcome as a truth value raises at runtime, and most such uses (`if`, `while`, `not`, `and`, `or`, `assert`) are also type errors: the runtime check is a `__bool__` that the type checker does not see, so mypy's `truthy-bool` check still reports them (a `__bool__` visible to mypy, even one declared never to return, would silence that check); an explicit `bool(...)` is caught only at runtime. The outcome's kind and value are not public, so no caller can bypass `fold` by testing the kind itself; ruff's private-member rule (SLF001) and the structure test enforce it. The type is the result of one call; states particular to an operation, such as EXE-009's "pending" transfer, belong to that operation's own contract, defined in its stage, and are never mapped to SUCCESS unless the operation is confirmed complete;
  - an idempotency key type carried by every financially significant request contract later (ARCH-041).
- **Acceptance:** contract tests show unknown fields, mutation (including of nested values), wrong types, and float or JSON-number amounts refused; for a secret-like value given as a field value and as an unknown key, neither the error's string form, nor its `errors()` or `json()` form as rendered by the error function, nor captured log output contains it; schema snapshot tests fail when a committed schema changes without a version change; a type-test module contains lines that must not type-check, each marked `# type: ignore[<error code>]`, so that strict mypy (which reports unused ignores) fails if any of those errors ever disappears, for an unhandled outcome and for an outcome used as a truth value.

No system contract (market data, order, position, risk, capital, and so on) is written in Stage 1. Each is written when its stage is planned, on this kernel (ARCH-025; A-05).

### U4 — Configuration (checkpoint C)

- **Purpose:** one validated configuration source, so that later systems never read raw settings (MIG-004, MIG-010, SEC-005; constitution Rules 107–111; GOV-014: no second configuration source).
- **Files:** `src/atp/config/`; tests under `tests/config/`; example configuration files with placeholder values only under `config/examples/` (D2); the command-line entry point `atp config check` (D1).
- **Content (D9):**
  - **Two parts, both contracts (TEC-004):** a portable part and an environment-specific part (MIG-010), read from TOML files (D9). Stage 1's settings are only these: the platform identifier (portable); the environment name, one of OPS-004's six, and the environment identifier (environment-specific, MIG-027); and secret declarations, each a name and a kind from a closed set that includes trading-enabled credentials, never a value. Host paths and addresses may appear only in the environment-specific part (MIG-010), and no code assumes a host (MIG-004). The repository's configuration files hold no policy content: policies are portable configuration under MIG-010, but they live only in the Policy System's store (POL-009) and move with the platform state (MIG-008). Example files hold placeholders only, with no real venue or credential names (GOV-017).
  - **Environment identity** comes from the environment-specific file the process is given; the `--env` the command is run with must match the file's declared environment, or the load fails.
  - **Secrets** come only from the process environment, through one interface that a secret manager can implement later (SEC-005); a secret value found in a configuration file is an error; secrets are held as secret types and never appear in output, errors, or logs.
  - **Defence in depth (constitution Rules 109, 111):** a configuration that declares a secret of the trading-enabled kind is refused unless its environment is production. In Stage 1 no environment has trading credentials at all (section 3.2).
  - **Fail closed** (constitution Rule 108): a missing, unknown, or malformed setting, an unknown environment, or a mismatch between `--env` and the file stops the load with a clear error.
  - No operating value is introduced; where a setting has a value, it comes from the values register (ARCH-018).
- **Acceptance:** negative-path tests for each rule above, including a test that an error message never contains a secret value; `atp config check --env <name>` validates the example configuration for every environment and prints a redacted summary; it exits with an error for each deliberately broken example.

### U5 — Security foundation (checkpoint C)

- **Purpose:** secrets can never reach the repository by accident, and the platform's security design has a written starting point (SEC-001, SEC-005; constitution Rules 110, 151, 153; master execution constitution §40, §42).
- **Files:** the repository test for secrets, written at checkpoint A (U1) and extended here to the example configuration files; the threat model (D2).
- **Content:** the threat model covers the assets of SEC-001, the trust boundaries (the six environments, the AI gateway, exchange credentials, the three credential authorities of SEC-006, the operator interface), and the controls already required, with the gaps each later stage must close. It is design-level only; it adds no requirement (any new requirement it suggests goes through the findings register first).
- **Acceptance:** the repository test passes on the real repository and fails on a planted secret in a copy; the threat model is reviewed in Gate 3.

### U7 — Traceability: the verification matrix (checkpoint D)

- **Purpose:** close the chain source → requirement → rule → system → interface → implementation → test → verification (ARCH-031, ARCH-040; master execution constitution §74, §145; the [traceability README](../traceability/README.md)), so that a requirement without a test, or a test without a requirement, is visible.
- **Files:** an extension of [`tools/docs/`](../../tools/docs/README.md) (standard library only, like the existing tools); the generated matrix (D10), `docs/traceability/verification-matrix.md`.
- **Content:** source modules and tests name the requirements they implement or verify (a module docstring line and a pytest marker, for example `@pytest.mark.req("TEC-003")`); the tool collects them into the matrix with the columns of §145 and the traceability README: requirement; system rule where one exists (System Rules Register); system; interface (contract) where one exists; implementation; tests; verification (the gate and the verification record that checked it); status; evidence; and the checkpoint commit, through that verification record (a generated file cannot contain its own commit). The checker fails on an unknown ID, a DEPRECATED / REPLACED one, or a PROPOSED or FUTURE one (ARCH-029, GOV-017: nothing unapproved is implemented); the self-test gains a case for each.
- **Acceptance:** every requirement of section 3.1 has at least one implementation and one test in the matrix. For most, the implementation is a module and the test a pytest test; for the others, the matrix names the artifact and its check: SEC-001, the threat model, checked in Gate 3; GOV-023, the workflow with its recorded negative run, the developer guide, and the recorded clean-clone run; ARCH-032, the documentation tools, with their self-test cases; Gate 3 checks that each marked test really exercises the requirement it names, not only that a marker exists (DEC-032: no tests that pass without proving the required behavior); the self-test passes, including the new negative cases.

### U8 — Stage record, feature status, closure (checkpoint D)

- **Purpose:** the stage leaves the evidence the governance requires (master execution constitution §142 to §144, §152; constitution Rule 232).
- **Files:** `docs/traceability/stage-01-foundation.md` (the stage record, created when the stage starts and updated at each checkpoint); the feature-status table of D5 in the roadmap; the architecture-to-repository map of constitution Rule 15 in the source-of-truth map (D2); the roadmap's stage status; the project state. The registry is generated and not edited by hand; what Stage 1 adds to traceability is the generated matrix of U7.
- **Content:** the stage record's fields (§142); each Stage 1 feature with its GOV-024 state (D5); the §152 transition checklist with evidence; the completion certificate (§143), whose "approved to proceed" is the owner's.
- **Acceptance:** section 9's completion criteria.

## 5. Out of scope

Everything that belongs to a later stage, even where Stage 1 prepares for it (RMP-011; GOV-017):

- exchange adapters and connectivity, market data, storage and databases, database schemas and migrations, messaging (DATA FOUNDATION and later);
- any trading, paper or live; any trading credential; capital, risk, execution, reconciliation, portfolio, policy (CORE TRADING FOUNDATION and later);
- system contracts (written on the Stage 1 kernel when each stage is planned);
- services, processes, containers, the deployment definition, the configuration compiler (MIG-011), infrastructure as code, the observability stack, deployment of any kind (from the first deployable service; the rest in OPERATIONALIZATION);
- AI of any kind (AI INTELLIGENCE);
- Rust extensions (TEC-002: only after measurement);
- performance budgets and benchmarks (no hot path exists yet; PERF-008 to PERF-010 belong to DATA FOUNDATION);
- the open technical concerns TC-09 and TC-10 (decided when their stages are planned). Stage 1 uses OPS-004's environment names and ARCH-042's result names only inside their own types (an environment, an outcome), so they cannot be confused with the same names in other state machines; that does not decide TC-10. D6 decides one part of it, the relation between GOV-009's and GOV-024's statuses; on approval, the register and the glossary are updated to say so.

## 6. Outputs

| Output | Location | Kind |
|---|---|---|
| Project definition, lockfile, Python version | `pyproject.toml`, `uv.lock`, `.python-version` | Code foundation |
| Package with `numeric`, `contracts`, `config` modules and the `atp` command | `src/atp/` | Implementation |
| Tests | `tests/` | Tests |
| Committed contract schemas | `contracts/` | Contract artifacts |
| Example configuration (placeholders only) | `config/examples/` | Configuration foundation |
| Machine checks | `.github/workflows/checks.yml` | Testing foundation (if D4 is approved) |
| Verification matrix and its generator | `docs/traceability/verification-matrix.md`; `tools/docs/` | Traceability |
| Developer guide, numerical policy, contract conventions, threat model, architecture-to-repository map | The locations of D2 | Documentation |
| Feature-status table | The roadmap (D5) | Project memory |
| Stage record and completion certificate | `docs/traceability/stage-01-foundation.md` | Verification evidence |

Each new directory is created at the checkpoint that first puts a real artifact in it (constitution Rules 9–12); none is created empty for a later stage.

## 7. Tests

| Level | What | Tool |
|---|---|---|
| Unit | Amount construction and rounding, outcome handling, idempotency keys, configuration rules, redaction | pytest |
| Property | Exactness, quantization direction and bound for positive and negative values, string round trips, refusal of floats, booleans, and non-finite values | Hypothesis |
| Contract | Strictness, immutability including nested values, versioning, schema snapshots, JSON amounts as strings | pytest |
| Type | Strict typing of `src/` and `tests/`; the type-test lines of U3 must keep failing | mypy |
| Negative path | Every refusal in U2 to U5: float, `bool`, or non-finite amount; float conversions in `src/`; an inexact result without a rounding function; unknown field; breaking change without a version; secret in a file or echoed in an error; trading credential outside production; missing or malformed setting; unknown environment; `--env` not matching the file | pytest |
| Concurrency of the context | The decimal context in a new thread and a new asyncio task | pytest |
| Structure | Import directions between modules (section 8, Gate 2), checked by a standard-library `ast` test; no `Decimal(...)` outside `atp.numeric`, and no `Decimal.from_float` or `create_decimal_from_float` in `src/` (U2); no access to the outcome's private members outside `atp.contracts` (U3; also ruff SLF001); no secret-like tracked file (U1, U5) | pytest |
| End to end | From a clean clone: `uv sync --locked`, all checks, `uv build`, `atp config check` for every environment, with good and broken configurations | Shell commands recorded in the stage record |
| Documentation and tools | Checker, comparison, self-test (with the new cases) | `tools/docs/` |
| Machine checks | The same checks on every push | The workflow of U6 |

No numerical coverage target is invented (constitution Rules 128–129: claims need evidence), and no coverage tool is added: every public function of the three modules has at least one test, checked in Gate 2 by reading the modules against the matrix.

## 8. Verification (the three gates, applied to Stage 1)

At every checkpoint, and again for the whole stage before closure:

- **Gate 1 — technical:** lint, format, strict typing, all tests, the package builds (`uv build`), the documentation checker and the requirement comparison pass, the matrix is current.
- **Gate 2 — architecture and consistency:** each module has one owner and one responsibility (constitution Rule 83); dependencies point one way, enforced by the structure test: `atp.numeric` imports no other platform module; `atp.contracts` imports only `atp.numeric`; `atp.config` imports only `atp.contracts` and `atp.numeric`; the command-line module imports only `atp.config` and is imported by none, and receives errors from `atp.config` already rendered by the error function of `atp.contracts`. No second configuration source, no float in an amount, no host-specific value in code (GOV-014, TEC-003, MIG-004). Every requirement of section 3.1 traced in the matrix; every public function of the three modules has at least one test (read against the matrix); documentation, roadmap, feature-status table, and project state agree with what was built; no future-stage work slipped in.
- **Gate 3 — independent end-to-end and failure audit:** an independent reviewer works from a fresh clone: installs from the lockfile, runs every check, runs the configuration command against good and broken inputs, tries to make a float, a secret, or a trading credential get through, checks that each requirement-marked test proves its requirement, and checks that a fresh session could continue from the repository alone (master execution constitution §88). Its findings and fixes are recorded.

## 9. Completion criteria

Stage 1 is complete only when all of these hold, each with its evidence in the stage record:

1. U1 to U8 meet their acceptance criteria.
2. The three gates pass for the whole stage, after every fix (DEC-032).
3. Every requirement of section 3.1 is traced to its implementation and test in the matrix, in the forms U7 accepts; those of sections 3.2 to 3.5 keep the disposition section 3 gives them, with no gap left unexplained.
4. No secret, local path, or model identifier is in the repository; the repository test for secrets passes; the dependency review of U1 is recorded.
5. The documentation is updated: developer guide, numerical policy, contract conventions, threat model (and the "Not yet specified" line of the [security architecture](../security/security-architecture.md) that lists it), architecture-to-repository map, feature-status table, roadmap status, project state.
6. The §152 transition checklist is complete with evidence, and the completion certificate is written.
7. Every checkpoint is committed, verified, and pushed.
8. The owner approves proceeding to Stage 2 planning (§143, §156).

## 10. Decisions this plan asks for

Each was RECOMMENDED — NOT YET APPROVED until the owner approved all eleven, as recommended, on 2026-10-05 ([DEC-038](../decisions/DEC-038-stage-1-plan-approved.md)). The table is kept as approved.

| # | Decision | Recommendation | Alternatives | Why |
|---|---|---|---|---|
| D1 | Package and command name | `atp` (autonomous trading platform), installed from `src/atp/`, command `atp` | A longer name such as `trading_platform` | Short, neutral, no product claim; the `src/` layout keeps tests from importing the working copy by accident |
| D2 | New locations | Top level: `src/`, `tests/`, `contracts/` (committed schemas), `config/examples/`. Documentation: the developer guide in `docs/development.md`, linked from the root `README.md`; the numerical policy in `docs/architecture/numerical-policy.md`; the contract conventions in `docs/architecture/contracts.md`; the threat model in `docs/security/threat-model.md`; the architecture-to-repository map as a new section of the [source-of-truth map](../architecture/source-of-truth-map.md), with one owner per module, taken from the registry's owners: `atp.numeric`, `atp.contracts`, and the command-line module → platform architecture (cross-cutting; ARCH-010, ARCH-025); `atp.config` → the hosting, backup, and migration set (cross-cutting; MIG-010), whose configuration compiler (MIG-011, OPERATIONALIZATION) will extend this module rather than add a second configuration source (GOV-014); the generated verification matrix in `docs/traceability/verification-matrix.md` | Schemas and examples inside the package; the conventions and the threat model as sections of existing documents | Each location holds one kind of artifact (constitution Rules 11, 168); none of these topics has a home yet (searched: no numerical policy, contract conventions, threat model, or developer guide exists) |
| D3 | Build backend | `uv_build`, the build backend of the uv tool the stack already uses (TEC-009) | `hatchling` | No second packaging tool family; needed for `uv build`, the `atp` command, and installing `src/atp` |
| D4 | Machine checks on GitHub | A read-only workflow running the same checks on every push and pull request, using `actions/checkout` and `astral-sh/setup-uv`, each pinned to a commit hash | Checks run only by the builder before each commit | Checks keep running without Claude Code (GOV-023); the workflow holds no secrets and deploys nothing |
| D5 | Where each feature's GOV-024 state is recorded | One feature-status table in the master roadmap: each major feature, its stage, and its current GOV-024 state, kept current at every checkpoint, also after the feature's stage closes; stage records link to it | A separate feature registry document; or the stage record only | One place, inside the single master roadmap (RMP-003), so no second source appears next to the requirement classes and the Readiness System's runtime capability registry (DUP-32, GOV-014); the CF-19 reading left this to Stage 1 planning ([DEC-035](../decisions/DEC-035-owner-decisions-part-3-findings.md)) |
| D6 | GOV-009's statuses next to GOV-024 | ACTIVE: a feature or interface from APPROVED to PRODUCTION; SUNSET_PENDING: DEPRECATED with a planned removal date; REPLACED: DEPRECATED or RETIRED, naming its replacement. IDEA and PROPOSED are not ACTIVE (ARCH-029) | Keep the two vocabularies unrelated | Fixes the builder reading in [Architecture governance](../architecture/architecture-governance.md) ("fixed when Stage 1 is planned"), so one feature never carries two contradictory statuses; it decides this part of TC-10 |
| D7 | Amount rules | Section 4, U2: one constructor (`str`, `int` but not `bool`, `Decimal`; finite only); context set once by setting the fields of the current and the default context in place; traps `FloatOperation`, `InvalidOperation`, `DivisionByZero`, `Overflow`, `Inexact`; rounding only through functions that name the direction, exact intermediate steps (`divmod` for increments), `Inexact` untrapped only for the final `quantize`; over-long amounts refused; JSON amounts as strings; TOML numbers read through the amount constructor; the precision an IMPLEMENTATION CHOICE in the values register | Python's default decimal context with review-only discipline | Makes TEC-003 enforceable by code and tests, not only by review, including the paths the `FloatOperation` trap alone misses |
| D8 | Contract conventions and versioning scheme | Section 4, U3: strict, immutable (tuples for collections), unknown fields refused, amounts as strings, errors rendered and logged only through one function that leaves input out; `MAJOR.MINOR` versions with breaking changes only in a new major version; committed schemas as snapshots; outcomes consumed only through an exhaustive `fold` | Lax validation; date-based or single-number versions | Sets the model every later interface follows (ARCH-026, GOV-006), so it is approved now rather than decided silently in code |
| D9 | Configuration format and Stage 1 settings | TOML files read with the standard library (`tomllib`); the settings of U4 only; secrets only from the process environment | YAML or JSON; a settings library | No new dependency (constitution Rule 99); TOML is typed and allows comments; the settings are only those Stage 1 needs, so nothing speculative is configured |
| D10 | How requirements are traced to code and tests | Requirement markers in module docstrings and pytest markers; a generated verification matrix with the columns of U7 | A hand-written matrix | A generated matrix cannot drift; the checker refuses unknown or replaced IDs |
| D11 | Dependencies Stage 1 adds | Runtime: Pydantic v2. Development: pytest, Hypothesis, ruff, mypy. Build: `uv_build` (D3). Machine checks: the two actions of D4. All already named in TEC-004 and TEC-009 except the build backend and the actions; exact versions fixed at checkpoint A: the libraries and tools in the lockfile, the build backend pinned to one exact version in `pyproject.toml` (aligned with U1, DEC-038), the actions by commit hash in the workflow | Others only by a later decision record | The technology stack requires a decision record for any dependency it does not list (constitution Rules 99–101) |

## 11. Sequence and checkpoints

| Checkpoint | Units | Depends on |
|---|---|---|
| A | U1 development environment; U6 testing foundation and machine checks | Owner's approval of this plan, recorded in a decision record |
| B | U2 exact amounts; U3 contract kernel | A |
| C | U4 configuration; U5 security foundation | B (configuration models are contracts; amounts in configuration use U2) |
| D | U7 verification matrix; U8 stage record and closure | A to C |

The stage record is created at the start of checkpoint A. Each checkpoint follows: work → three gates → checkpoint commit → push (DEC-032); a failed gate stops the sequence until it is fixed and re-verified (master execution constitution §19).

## 12. Risks and limits

| Risk | Effect | Handling |
|---|---|---|
| The package index or GitHub Actions is unreachable when the stage runs | U1 or U6 cannot finish | The stage stops at the last verified checkpoint and records the blocker; nothing is faked (constitution Rules 94, 209) |
| Pushing a file under `.github/workflows/` may need a credential with permission to change workflows (not tested) | Checkpoint A's push is refused | Recorded as a blocker for the owner if it happens; the workflow is not dropped silently |
| A library version behaves differently from the plan's assumptions | Rework inside the unit | Versions are fixed in the lockfile at U1 and recorded; any change is a new checkpoint |
| A known vulnerability in a locked dependency | Unsafe foundation | Found by the dependency review of U1; a different version or a recorded exception, decided before the checkpoint commit |
| Scope creep toward DATA FOUNDATION (for example writing a market-data contract "while the kernel is open") | Future work in the current stage (RMP-011) | Gate 2 checks for it; system contracts wait for their stage's plan |
| No deployment definition exists in Stage 1 | OPS-010 has no content until the first deployable service | Stated in section 3.2 and the stage record; OPS-010 stays a design rule until the first deployable service exists |
