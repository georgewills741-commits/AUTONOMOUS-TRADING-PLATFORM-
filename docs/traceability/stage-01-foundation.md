# Stage 1 — FOUNDATION: Stage Record

> **Status:** ACTIVE stage record (master execution constitution §142; format: [traceability README](README.md)). Created at the start of checkpoint A on 2026-10-06 and updated at each checkpoint (checkpoint B: 2026-10-07). The plan is the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md), approved by the owner with the authorization to implement Stage 1 only ([DEC-038](../decisions/DEC-038-stage-1-plan-approved.md)). Each feature's lifecycle state is in the roadmap's [feature-status table](../roadmap/roadmap.md#feature-status); each checkpoint's gate evidence is in its own verification record.

## Stage

| Field (§142) | Now |
|---|---|
| Stage ID | 1 — FOUNDATION (RMP-001, RMP-002) |
| Purpose | The plan's section 1: the first verified code foundation, with no trading capability |
| Dependencies | None: the first stage. Entry gate re-checked below |
| Requirements | The plan's section 3: delivered (3.1), started (3.2), applied as design rules (3.3), applied in later stages (3.4), not built (3.5) |
| Systems affected | The documentation set; SYS-31 Security Architecture (its foundation); the new cross-cutting modules, owned as the plan's D2 sets out |
| Files | Each checkpoint's verification record, "Scope": [checkpoint A](stage-01-checkpoint-a-verification.md), [checkpoint B](stage-01-checkpoint-b-verification.md) |
| Implementation status | U1 built (checkpoint A); U6 built (checkpoint A; its Hypothesis setting at checkpoint B); U2 and U3 built (checkpoint B); U8 started (this record, the feature-status table); U4, U5, and U7 not started |
| Test status | Checkpoint B: 807 tests, all passing: amounts, the decimal context, and rounding (`tests/numeric/`); contracts, refusals, versions, schemas, outcomes, and idempotency keys (`tests/contracts/`); the structure test and the repository test for secrets (`tests/repository/`). Strict mypy also checks the type-test module, whose lines must keep failing. Checkpoint A: 52 |
| Verification 1, 2, 3 | Per checkpoint, in its verification record: checkpoint A passed all three. The whole stage passes them again at checkpoint D |
| Security status | No secret in the repository; the repository test for secrets runs on every push; the machine checks run read-only, with no repository secret; the dependency review found no published advisory (below). From checkpoint B a contract's refusal never carries the input: tested with a secret-like value as a field value, an unknown key, a nested unknown key, and an outcome's tag, in the refusal's text, JSON, details, and captured logs ([contract conventions](../architecture/contracts.md)). No dependency was added at checkpoint B |
| Performance status | No hot path exists; no performance claim is made (the plan, section 5) |
| Documentation status | The [developer guide](../development.md) (checkpoint A, updated at B); the [numerical policy](../architecture/numerical-policy.md), the [contract conventions](../architecture/contracts.md), and the [architecture-to-repository map](../architecture/source-of-truth-map.md#architecture-to-repository) (checkpoint B); V-40 in the [values register](../requirements/values-register.md) (checkpoint B); the threat model comes at checkpoint C |
| Traceability status | The verification matrix comes at checkpoint D (U7); until then the plan's section 3 and this record trace the requirements. Each module's and each test module's docstring names the requirements it serves, and the architecture-to-repository map links each module to its requirements, tests, and documentation |
| Git commit | Each checkpoint's commit is in the [project state](../project-state.md)'s checkpoint log |
| Blockers | None |
| Next stage | DATA FOUNDATION, only after this stage's completion certificate and the owner's approval to proceed (the plan's completion criterion 8; §143, §156) |

## Checkpoints

| Checkpoint | Units | Status | Verification record |
|---|---|---|---|
| A | U1 development environment; U6 testing foundation and machine checks | Done: built, except U6's Hypothesis setting, carried to checkpoint B; three gates passed (commit `f2e4046`); the machine checks pass on GitHub and fail on a deliberately broken check ("Machine checks on GitHub" below) | [Checkpoint A](stage-01-checkpoint-a-verification.md) |
| B | U2 exact amounts; U3 contract kernel | Built; U6's Hypothesis setting written; three gates: see the verification record | [Checkpoint B](stage-01-checkpoint-b-verification.md) |
| C | U4 configuration; U5 security foundation | Not started | — |
| D | U7 verification matrix; U8 stage record and closure | Not started (U8 started at A) | — |

## Entry gate, re-checked on 2026-10-06 (master execution constitution §12)

| Condition | Result |
|---|---|
| Prerequisite stages, architecture, contracts, decisions, documentation | As the plan's section 2 records; nothing has changed since its approval (DEC-038) |
| Python | 3.12.3, the system interpreter. The environment cannot download a managed Python (the release downloads on GitHub are refused by its network policy), so the system interpreter is used |
| uv | 0.8.17 was installed. The project uses uv 0.12.23 (below), installed from the Python package index into a separate tool environment; 0.8.17 refuses to run in the project, as intended |
| Package index | Reachable (pypi.org) |
| Advisory database | The OSV service (api.osv.dev) is refused by the environment's network policy; PyPI's per-release vulnerability data, which PyPI takes from OSV, was used instead |

## Checkpoint A: versions, dependency review, and licenses

Versions are fixed in `uv.lock`, `pyproject.toml`, and the workflow ([developer guide](../development.md)); this table is the evidence of the review at checkpoint A, not a second list to maintain.

**Review method (U1, master execution constitution §40; licenses, DEC-009's consequences and DEC-038):** for each locked package, and for uv and the build backend, PyPI's JSON record of that exact release, read on 2026-10-06 at 02:52 UTC: its published advisories and its declared license (where none is declared, the license file the package ships).

| Package | Version | Use | License | Advisories |
|---|---|---|---|---|
| pydantic | 2.13.5 | Runtime (TEC-004) | MIT | None |
| pydantic-core | 2.46.5 | Runtime, through pydantic | MIT | None |
| annotated-types | 0.8.0 | Runtime, through pydantic | MIT | None |
| typing-inspection | 0.4.4 | Runtime, through pydantic | MIT | None |
| typing-extensions | 4.16.0 | Runtime, through pydantic; mypy | PSF-2.0 | None |
| pytest | 9.1.1 | Development (TEC-009) | MIT | None |
| iniconfig, pluggy, packaging, pygments | 2.3.0, 1.6.0, 26.3, 2.21.0 | Development, through pytest | MIT, MIT, Apache-2.0 OR BSD-2-Clause, BSD-2-Clause | None |
| colorama | 0.4.6 | Development, through pytest, on Windows only | BSD | None |
| hypothesis | 6.168.5 | Development (TEC-009) | MPL-2.0 | None |
| sortedcontainers | 2.4.0 | Development, through hypothesis | Apache-2.0 | None |
| mypy | 2.4.0 | Development (TEC-009) | MIT | None |
| mypy-extensions, librt, ast-serialize | 1.1.0, 0.16.0, 0.12.1 | Development, through mypy | MIT (mypy-extensions: from its license file), MIT, MIT | None |
| pathspec | 1.1.1 | Development, through mypy | MPL-2.0 | None |
| ruff | 0.16.10 | Development (TEC-009) | MIT | None |
| uv | 0.12.23 | Package manager (TEC-009) | MIT OR Apache-2.0 | None |
| uv_build | 0.12.23 | Build backend (D3) | MIT OR Apache-2.0 | None |

**Result:** no published advisory affects a locked version. Every license is permissive except MPL-2.0 for hypothesis and pathspec, a file-level copyleft that applies to changes to those packages' own files; both are development tools, not part of the built package (`uv build` puts only `src/atp/` in it).

**uv's version.** The newest uv for which the pinned `setup-uv` release carries a built-in checksum is 0.12.17, which has a published advisory (GHSA-2cv4-cqwr-gwf7: on Windows, a crafted wheel could write outside the installation prefix; fixed in 0.12.18). The project therefore uses 0.12.23, the current release, with no advisory. The workflow passes its checksum explicitly: the sha256 `9167d72b…fb66d6` of the Linux x86-64 archive, taken from the publisher's version manifest (astral-sh/versions, commit `a3d1b3a6`), whose entry for 0.12.17 matches `setup-uv`'s own built-in checksum.

**Actions (D4), pinned by commit hash, each resolved from its release tag and read at that commit:**

| Action | Release | Commit | Runtime |
|---|---|---|---|
| actions/checkout | v7.0.1 | `3d3c42e5aac5ba805825da76410c181273ba90b1` | node24 |
| astral-sh/setup-uv | v10.2.0 | `c18668ad3cf93ea998bef934396af7bb5c839dc7` | node24 |

The workflow file was also checked once with actionlint 1.7.12 (run with `uvx`, not added to the project): no error. Its shell-script check was not available in this environment.

## Checkpoint A: builder details and plan wording

Choices the plan left to implementation (category 3 of the final decision checkpoint), and one plan item deferred to checkpoint B (U6's Hypothesis setting). None changes a requirement or a decision.

| Item | What was done | Why |
|---|---|---|
| Hypothesis configuration | U6 names "pytest and Hypothesis configuration in `pyproject.toml`". The pytest settings are there. The Hypothesis setting is deferred to checkpoint B: Hypothesis itself reads no configuration file, but its pytest plugin's options (`--hypothesis-profile`, `--hypothesis-seed`, and others) can be set in `pyproject.toml`'s pytest options. Checkpoint B writes the setting there with the first property tests; if it finds that none is needed, it records that in this record as a deviation from U6's file list, for the owner. Until then nothing is needed: when `CI` or `GITHUB_ACTIONS` is set, as on the machine checks, Hypothesis 6.168.5 loads its built-in `ci` profile (derandomized, no deadline, no example database; read in its source, `hypothesis/_settings.py`) | No Hypothesis test exists at checkpoint A, so a setting now would configure nothing that can be checked. The Gate 3 review corrected the first wording, which said the item could not be met |
| uv and Python versions | uv 0.12.23 exactly (`required-version`), the build backend at the same version; Python `3.12` in `.python-version`, patch level as found (3.12.3 here) | See "uv's version" above; a patch-level Python pin would hold back security fixes, and the patch in use is printed by every run of the machine checks |
| ruff rules | ruff's default rules for the locked version plus the whole security family (`S`); `assert` allowed in tests; Python files only | ruff 0.16's defaults are a curated set of 413 rules; the security family fits a financial platform; ruff 0.16 would otherwise format Python examples inside the documentation, including historical records |
| mypy settings | Strict, `truthy-bool` (U1; U3) and four further error codes, unreachable-code warnings | The plan's strict mode, with the checks that catch silent truth-value and ignore mistakes |
| The documentation tools' settings | `tools/docs/ruff.toml` and `tools/docs/mypy.ini` keep the tools at the rule set and type-check level they were written to | ruff 0.16 changed its default rules, and the tools do not meet the new defaults (34 findings) or strict mypy (23); U1's acceptance requires the tools to run unchanged, so their code was not changed. Raising them to the project's settings would be a separate change to the tools |
| Package version | `0.1.0` | A starting version for the package; no release process exists yet |
| `uv build` in the machine checks | Not run by the workflow; run at every gate | The workflow runs the plan's list (U6); the build is in Gate 1 |
| The feature-status table's later stages | One row per later stage, pointing to that stage's items in the roadmap's stage tables, instead of one row per item | Each stage's items get their own rows when the stage is planned, as Stage 1's did; a copied list would be a second list of the same items |
| The feature-status table's state for later stages | APPROVED, from the owner's acceptance of the complete documentation review (DEC-036), which the registry's Approval column records as "reviewed (DEC-036)". Under D6, a feature from APPROVED onward is ACTIVE in GOV-009's terms | The requirements of those stages are accepted; APPROVED is a lifecycle state, not an authorization to implement (the table says so). The owner may decide otherwise. The quality audit of 2026-10-06 put this reading to the owner as OQ-29, because no owner decision states the state and the texts can be read both ways ([quality audit](quality-audit-2026-10-06.md), Q-07); until the answer the table showed REQUIRES OWNER DECISION. Decided by the owner on 2026-10-07: PROPOSED until each stage's plan is approved ([DEC-040](../decisions/DEC-040-later-stage-features-proposed.md)), which replaces this reading |
| The repository test for secrets, beyond the plan's minimum | 18 value patterns (issuers' token formats, credentials in a URL, quoted and unquoted credential-named settings, prefixed names such as `BINANCE_API_SECRET` included) and a list of secret-like file names; a test of the file listing itself. A setting's value, quoted or not, is reported only if it contains both a letter and a digit; templates, variable references, placeholders, and environment-variable names given as values are not reported; lines may end in LF or CRLF | The three Gate 3 runs found credential shapes missed and ordinary text wrongly reported, the third that the earlier fixes had covered samples rather than whole classes; U5 at checkpoint C extends the test to the example configuration files ("Carried to checkpoint C") |

## Carried to checkpoint B

The plan's technical claims for U2 and U3 (the decimal context and its traps, Hypothesis's decimal strategies, Pydantic's error rendering, and mypy's `truthy-bool` and unused-ignore behavior) were tested on 2026-10-05 with mypy 1.19.1, Pydantic 2.13.5, and Hypothesis 6.168.4 ([Stage 1 plan verification](stage-01-plan-verification.md), "Environment"). The locked versions are mypy 2.4.0, Pydantic 2.13.5, and Hypothesis 6.168.5, so checkpoint B re-tests each claim on them before relying on it; the move to mypy 2 matters most.

Also for checkpoint B: U3 relies on ruff's private-member rule SLF001, which is not among the rules enabled at checkpoint A (ruff's defaults plus `S`); checkpoint B enables it with the code it protects. And U6's Hypothesis setting ("builder details and plan wording" above).

**Done at checkpoint B:** every claim was re-tested on the locked versions and holds ("Checkpoint B: the plan's claims re-tested" below); SLF001 is enabled; the Hypothesis setting is written (`--hypothesis-profile=ci` in pytest's options).

## Checkpoint B: the plan's claims re-tested

Re-tested on 2026-10-07 with the locked versions (Python 3.12.3, Pydantic 2.13.5, Hypothesis 6.168.5, mypy 2.4.0), by scripts run in a scratch directory with the project's environment (not added to the repository). Several are also kept by the project's own tests, named in the last column.

| # | Claim (the plan's U2 and U3) | Result | Also kept by |
|---|---|---|---|
| C1 | Setting the fields of `DefaultContext` and of the current context in place reaches new threads and new asyncio tasks; rebinding the name `DefaultContext` does not reach new threads | Holds | `tests/numeric/test_context.py` |
| C2 | With `Inexact` trapped, `quantize` with a rounding mode raises when it has to round | Holds. The built rounding does not use `quantize` (builder details below) | — |
| C3 | At 34 digits, a rounded quotient takes 9.899…9 down to 9.9 for an increment of 0.3; `divmod` gives 9.6 | Holds | `tests/numeric/test_rounding.py` |
| C4 | Hypothesis's decimal strategies raise `Inexact` under the trapped context when given limits alone, not when given `places=` | Holds | The property tests, which use `places=` |
| C5 | The `FloatOperation` trap stops `Decimal(0.1)` and mixed ordering comparisons, not equality comparisons with floats or the explicit conversions | Holds | `tests/numeric/test_context.py`; the structure test for the conversions |
| C6 | `hide_input_in_errors` hides input values only from the error's string form; `errors()` and `json()` keep them unless `include_input=False`; the location keeps an unknown field's name, also without input and in the string form | Holds | `tests/contracts/test_model.py` |
| C7 | Some messages quote the input: `union_tag_invalid` quotes the tag received | Holds (found while building; the plan did not name it) | `tests/contracts/test_model.py` |
| M1 | mypy's `truthy-bool` reports an object whose `__bool__` it cannot see in `if`, `while`, `not`, `and`, `or`, and `assert` | Holds on mypy 2.4.0 | `tests/contracts/type_checks.py` |
| M2 | A `__bool__` visible to mypy, even one declared never to return, silences `truthy-bool` | Holds (mypy then reports the code after it as unreachable instead) | — |
| M3 | Strict mypy reports an ignore comment that silences nothing (`unused-ignore`) | Holds | `tests/contracts/type_checks.py` |
| M4 | Leaving out one of `fold`'s handlers is a type error (`call-arg`) | Holds | `tests/contracts/type_checks.py` |

## Checkpoint B: builder details and plan wording

Choices the plan left to implementation, and the places where the code is stricter than the plan's wording. None changes a requirement or a decision; each is in the [numerical policy](../architecture/numerical-policy.md) or the [contract conventions](../architecture/contracts.md).

| Item | What was done | Why |
|---|---|---|
| Precision | 34 significant digits, V-40 in the values register | The plan leaves the value to implementation, as an IMPLEMENTATION CHOICE with its reason (D7); the reason is in the numerical policy |
| Rounding without untrapping `Inexact` | The plan has each rounding function untrap `Inexact` for its final `quantize` only. The built `quantize` needs no `quantize` call: the integer quotient and remainder from `divmod`, then the quotient times the increment, plus or minus one increment, are all exact under the trapped context, so no step runs with `Inexact` untrapped | Stricter than the plan, with the same results; a result that does not fit raises |
| The amount constructor, beyond the plan | Exact types only (a subclass of `str`, `int`, or `Decimal` is refused); text must have the form `AMOUNT_PATTERN` (Python's `Decimal()` would also accept spaces, underscores, and other scripts' digits); an exponent outside the context's range is refused, including one too large for Python's decimal module, which would otherwise escape as `InvalidOperation` (Gate 3 run 1, finding 2); `amount()` and `quantize()` raise if the context is not configured | Each closes a way a value could enter that the plan's list did not name |
| TOML underscores | `amount_from_toml` removes TOML's digit separators before the constructor, which refuses them | TOML allows `1_000.25`; the constructor's text form does not |
| Division with a named direction | Not provided | No Stage 1 calculation needs it; the first stage that does adds it under the same rules (numerical policy) |
| Refusals | `from_python` and `from_json` raise `ContractError`, which holds only redacted details and is raised after the handler has finished, so it keeps no reference to the original error (Gate 3 run 1, finding 4). The structure test refuses, outside `atp.contracts`, Pydantic's methods that validate without redaction or skip validation (`model_validate*`, `model_construct`, `model_copy`, a `TypeAdapter`'s `validate_*`), and contracts re-validate instances given as input. A location part is kept only if a contract declares it as a name; a message is kept only for error types whose messages never quote input, which no longer includes `value_error`: the kernel's own validators raise their own error types with fixed text | The plan's single rendering function, made the only path for outside input. Keeping only declared names is stricter than redacting the parts known to come from the input; the message rule follows C7 and makes the plan's "no validator puts an input value into its message" hold even for a validator that breaks it |
| Outcomes, beyond the plan | `==` raises and an outcome is not hashable; the class cannot be subclassed; in a contract an outcome instance is validated through its envelope, strictly, so its value and error have the declared types (Gate 3 run 1, finding 1); a Python dump keeps the outcome object and only JSON shows the envelope; copying and pickling rebuild it through its constructors | `==` would test the result outside `fold`; the rest keep the type's guarantees through every path into and out of a contract |
| Idempotency keys | 32 lowercase hexadecimal characters (128 bits), drawn with `secrets` | The plan names the type, not its form |
| Minor versions | Within one major version, a reader accepts data of its own minor version or an earlier one | The plan fixes only that different major versions are never compatible; contracts refuse unknown fields, so a later minor version's data can carry a field an earlier reader would refuse |
| Locked settings and runtime values | What a contract may add is listed, and everything else is refused when the class is defined: its settings are exactly the base's (none changed, none added); field metadata is written only as `Field(...)`, holding the constraints it expresses, and `AfterValidator(...)`, exactly those classes, never a subclass and never a constraint object written directly, at any depth, and a field's other settings only its default, alias, title, description, examples, schema extras, deprecation, and `repr`; field validators run in after mode only; no model validators, serializers, computed fields, version 1 validators, unvalidated defaults, excluded fields, or private attributes of its own; no redefined kernel method (the schema hooks included), in the contract or a mixin before it, and the checks run from the contract's metaclass, so no base class can skip them; `copy.replace` is refused; `Amount` is a `type` alias, which cannot be called, and no other `type` alias is accepted; `json_schema_extra` holds only `x-` extension keys; an amount's bounds are amounts or integers, never floats, text, or bools, and an amount, with or without metadata of its own, is combined in a union only with `None` or a literal of strings; a field's own constraints are checked as Pydantic holds them, not through a rebuilt `Annotated[...]`, so the verdict does not depend on what was evaluated before; a field with an alias is read and written under it. Any other exception a validator raises becomes a `validator_failed` refusal naming only its type, except an unconfigured decimal context (`DecimalContextError`), which propagates. After validation, every value is checked against its field's declared type at any depth (`contract_value_type`); float fields refuse infinities and NaN | Gate 3 run 2 (findings 1, 4, 11): the base's guarantees could be switched off by a subclass. Gate 3 run 3 (finding 1): a float or a JSON number could still reach an `Amount` field through a before, plain, or wrap validator or an unvalidated default; the refusals became a list of what is allowed, and the run-time check checks the declared types rather than immutability alone. Gate 3 run 4 (findings 1 to 5, 7): constraints on an amount written as its default were dropped, a validator's `KeyError` escaped with the input, an aliased contract could not read its own JSON, field settings and mixins were not covered, and `Amount \| float` took a JSON number. Gate 3 run 5 and the builder's own review of its fixes: a mixin's `__pydantic_init_subclass__` would have skipped every check (hence the metaclass), float bounds on optional amounts, `copy.replace`, and the context error reported as refused input. Gate 3 run 6 (findings 1, 7): `Amount` could be called to build a `Decimal` without the amount's checks, and a contract could redefine its JSON schema. Gate 3 run 7 (findings 1, 5, 8): an amount with metadata of its own escaped the union rule, `json_schema_extra` could restate the schema, and text bounds were accepted; the builder's fix of the bound rule found that a rebuilt `Annotated[...]` made the checks depend on earlier contracts, and its review of that fix that a constraint object written directly did too, and that a subclass of `AfterValidator` could read the input first |
| Immutable field types | Every field's type, at any depth, must be built from an allowlist of immutable types (strings, numbers, dates and times, UUIDs, enums whose member values are strings or integers and that read only their own members, literals, `Amount`, idempotency keys, contracts, outcomes, and tuples, frozensets, and unions of these); anything else is refused when the class is defined, as are a plain `Decimal` (amounts are `Amount`), a `type` alias other than `Amount`, and a type that cannot be resolved then. Assigning to or deleting a field raises with fixed text | Makes the plan's "collections held as tuples" a check, not a habit. The first version refused four mutable types and let `Mapping`, `Sequence`, `Any`, and others through (Gate 3 run 1, finding 3); Pydantic's own assignment refusal repeated the value (finding 13). `bytes` was dropped from the list at Gate 3 run 3 (finding 7): JSON has no bytes, and a value that is not UTF-8 could not be written. Gate 3 run 6 (finding 8): an enum member's value could be a list. Gate 3 run 7 (finding 2): an enum's own `_missing_`, or `IntFlag`'s default boundary, read values that are no member as one |
| Contract identities | Lowercase letters and digits in parts joined by dots or hyphens; the kernel's types are `atp.amount`, `atp.idempotency-key`, and `atp.outcome`, each at version 1.0 | The identity names the schema's directory; the form was found missing while writing the conventions and added with its test |
| Committed schemas | `contracts/<identity>/<MAJOR.MINOR>.schema.json`, JSON Schema 2020-12; `write_schema_files` adds a new version's file and never overwrites a changed one; earlier versions' files stay | The plan names the directory and the snapshot test, not the layout |
| Hypothesis setting (U6, carried from checkpoint A) | `--hypothesis-profile=ci` in pytest's options in `pyproject.toml`, so every run, local or on the machine checks, uses the built-in `ci` profile; checked on 2026-10-07: derandomized, no deadline, no example database, failing examples printed | Meets U6's "Hypothesis configuration in `pyproject.toml`"; local runs now try the same examples as the machine checks |
| The type-test module | `tests/contracts/type_checks.py`, never run by pytest; each line that must not type-check is in its own function, and the `and` and `or` lines also name the second error mypy reports | mypy treats an outcome as always true, so a line after a first use would be reported as unreachable instead (M2's note) |
| SLF001 | Enabled for `src/` and `tests/` | Carried from checkpoint A |
| The structure test, beyond the plan | Besides the plan's checks: outside `atp.numeric`, no reference to `Decimal` other than a type hint or a type check (`Decimal`, or `Annotated[Decimal, ...]`, called, subclassed, or assigned to a name is not one; inside another type it is), no star import from `decimal`, no call of a value's own type, and no use of the decimal context; outside `atp.contracts`, Pydantic imported only by name and only `Field`, `AfterValidator`, `field_validator`, `ValidationInfo`, and `ValidationError` (so no model that is not a contract, no Pydantic dataclass in any spelling, `create_model`, `validate_call`, `TypeAdapter`, or `pydantic_core`), and none of Pydantic's non-redacting or validation-skipping methods (version 1 names included); in `src/`, no silent rounding or float conversion (`round`, `to_integral*`, the rounding dunders, `__float__`, and `__int__`, `float` as a converter, the `math`, `cmath`, and `statistics` modules, and integer division, remainder, and `divmod`, in any of their spellings, outside `atp.numeric._rounding`) outside an empty list of modules allowed floats, no TOML read without `parse_float` and no JSON read without `parse_float` and `parse_constant`, no `ast.literal_eval`, and no amount built from a value's text; `Decimal` reached through any module counts, and a call of it is never a type use; no import of another package's private modules or names, and imports from the package root checked as the packages they name; every entry of the scanners' lists has a planted sample of its own | Gate 3 runs 1 to 6 (run 1: findings 5, 10, 11, 18; run 2: findings 2, 3, 6; run 3: findings 2, 3, 4, 5; run 4: findings 6, 8; run 5: findings 2, 10 to 12; run 6: findings 1, 2, 6, 9; run 7: findings 4, 7) showed ways around the plan's checks, each closed with planted samples. At run 3 the Pydantic check became a list of allowed names instead of a list of refused constructs |
| Copying and pickling | Contracts holding outcomes or idempotency keys, and `ContractError`, can be copied, deep-copied, and pickled | They failed with `AttributeError` (Gate 3 run 1, finding 14) |

## Checkpoint B: non-blocking findings

| Finding | Handling |
|---|---|
| Equality between an amount and a float (`price == 0.5`) neither raises nor fails strict mypy (C5; checked on mypy 2.4.0) | Recorded in the numerical policy, "What the rules do not catch"; the constructor refuses a float, and Stage 1's code contains no float. Caught only in review |
| An explicit `bool(outcome)` is caught only when it runs | As the plan states (U3); the contract conventions say so |
| `int(amount)` truncates and formatting to fewer places rounds, both without a signal | Recorded in the numerical policy, "What the rules do not catch"; the scanner cannot tell an amount from an ordinary number there. `round()`, `to_integral*`, `math`, integer division, and the others the numerical policy lists are refused by the structure test |
| A float that became text before it reached `amount()` or a contract's amount field (`Leg(price=str(x))`), a float from dividing two integers (`/`), a reader, an amount builder, or a value's type reached through a variable, a subclass of `JSONDecoder`, a type alias's value (`Amount.__value__`), and a decimal context's `remainder` inside `atp.numeric` | Recorded in the numerical policy, "What the rules do not catch" (Gate 3 run 3, finding 2; run 6, finding 9); text made from a value inside the call to `amount()`, and JSON read without `parse_float`, are refused by the structure test. Caught only in review |
| A frozenset is written in an order that can differ between processes | Recorded in the contract conventions (Gate 3 run 7, finding 6): a contract whose written form must be stable holds a tuple. No contract holds a frozenset yet |
| A validator that gives one of Pydantic's error types a context built from its input, which that type's own message would then show | Recorded in the contract conventions as caught only in review (Gate 3 run 7, finding 3); a listed type raised with a message of its own gets the generic message |
| A `multiple_of` check whose whole quotient has more digits than the precision refuses the value as `validator_failed`, with no location | Recorded in the contract conventions and kept by a test (Gate 3 run 6, finding 9): the value is refused, as it should be, but the refusal does not name the field |
| Python's introspection (`object.__getattribute__`, pickling state) can reach an outcome's private kind and value, and `repr` names the result | Recorded in the contract conventions; caught in review |
| A contract may declare a `float` field | Allowed for values that are not amounts (TEC-003); amounts must be `Amount`, and a plain `Decimal` field is refused. Checked in review |
| A JSON Schema validator built on Python's `re` would accept a final line break in an amount | The code refuses it; JSON Schema's own (ECMAScript) reading does not accept it. Recorded in the contract conventions |
| `Decimal.shift` and `rotate`; reaching `Decimal`, `float`, or a rounding function only dynamically (`getattr`, `importlib`, `eval`) or through a stored list | Recorded in the numerical policy as caught only in review (Gate 3 run 2) |
| A traceback's frames hold the input in local variables; repeated JSON keys keep the last value; a later validator could reuse a kernel error type, whose message is kept; Pydantic's deprecated `validate`; an outcome's result in JSON | Recorded in the contract conventions as limits or as caught in review (Gate 3 run 2); the frame variables are for the observability stage to exclude |

## Carried to checkpoint C

U4 decides how an amount setting written as a TOML integer is read: `tomllib` gives an `int` for `limit = 3`, and a contract's `Amount` field refuses integers, because it refuses JSON numbers (checked on 2026-10-07). It is decided with U4's settings and their tests.

U4 also decides how a parsed TOML document reaches a contract. `from_python` validates strictly, in the contract's own types: TOML's arrays are lists where a contract has tuples, and its strings are not enum members, so a parsed document is refused there wherever the contract has a tuple or an enum (found by Gate 3 run 6, checked on 2026-10-12), while the same data as JSON is accepted by `from_json`. The way chosen (converting the document first, or another reading of it) is decided with U4's settings and their tests ([contract conventions](../architecture/contracts.md)).

U5 extends the repository test for secrets to the example configuration files. Shapes the scanner does not report at checkpoint A, found by the Gate 3 review and accepted until then: lowercase unquoted `name = value` lines (INI files, lowercase dotenv); YAML values shorter than 12 characters or followed by a comment; a YAML list item's first key (`- token: …`); quoted settings whose name carries a suffix after the credential word (`DB_PASSWORD_PROD = "…"`) or is a generic key name (`HMAC_KEY = "…"`); camel-case names with a prefix (`binanceApiSecret = "…"`); values set through a call or a subscript (`monkeypatch.setenv("ATP_DB_PASSWORD", "…")`, `os.environ["API_SECRET"] = "…"`), `f"…"` values, and `:=`; secret values without both a letter and a digit (a letters-only passphrase), the price of not reporting type names, paths, numbers, and enum values; `Authorization: Basic …` and bearer tokens; raw 64-character hexadecimal private keys; Slack `xoxe-` tokens. U5 decides which of these to detect, against the false positives each would bring.

## Machine checks on GitHub (U6 acceptance)

Checkpoint A's push was accepted, the workflow file included, so the plan's risk that a push of a workflow might need further permission did not occur. The first run, and a deliberate negative test (a commit that breaks one check, which must fail the run, then reverted), ran on 2026-10-06. The negative test runs on this branch, the one this work is pushed to; a temporary branch would leave no failing commit in the branch's history, but the builder pushes only to its designated branch without the owner's permission.

| Run | Commit | Result |
|---|---|---|
| First run, [37460824856](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/37460824856) | `f2e4046`, checkpoint A | Success: every step passed (checkout, uv's installation, and the nine steps that run the guide's ten commands), in 20 seconds. The log shows uv 0.12.23 downloaded from the publisher's mirror and installed (the action stops if the checksum does not match), Python 3.12.3 (the runner's system interpreter), 19 packages installed at their locked versions (every locked package except colorama, which is for Windows only, plus the project itself), the self-test's 34 cases, and 52 tests passed |
| Negative test, [37460975992](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/37460975992) | `74ce426`, an unused import added to `src/atp/__init__.py` | Failure, as required: the Lint step failed with ruff's "F401 `os` imported but unused" at `src/atp/__init__.py:5`; the later steps were skipped |
| After the revert, [37461068724](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/37461068724) | `bc6eca5`, which reverts `74ce426`; its files are identical to `f2e4046`'s | Success: every step passed |

U6's acceptance is met: the workflow passes on the branch, and a deliberately broken check makes it fail.

## Transition checklist and completion certificate

Written at checkpoint D (§152, §143).
