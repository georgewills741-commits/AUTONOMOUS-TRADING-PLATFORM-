# Stage 1 — FOUNDATION: Stage Record

> **Status:** ACTIVE stage record (master execution constitution §142; format: [traceability README](README.md)). Created at the start of checkpoint A on 2026-10-06 and updated at each checkpoint. The plan is the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md), approved by the owner with the authorization to implement Stage 1 only ([DEC-038](../decisions/DEC-038-stage-1-plan-approved.md)). Each feature's lifecycle state is in the roadmap's [feature-status table](../roadmap/roadmap.md#feature-status); each checkpoint's gate evidence is in its own verification record.

## Stage

| Field (§142) | Now |
|---|---|
| Stage ID | 1 — FOUNDATION (RMP-001, RMP-002) |
| Purpose | The plan's section 1: the first verified code foundation, with no trading capability |
| Dependencies | None: the first stage. Entry gate re-checked below |
| Requirements | The plan's section 3: delivered (3.1), started (3.2), applied as design rules (3.3), applied in later stages (3.4), not built (3.5) |
| Systems affected | The documentation set; SYS-31 Security Architecture (its foundation); the new cross-cutting modules, owned as the plan's D2 sets out |
| Files | Checkpoint A: see its [verification record](stage-01-checkpoint-a-verification.md), "Scope" |
| Implementation status | U1 and U6 built (checkpoint A); U8 started (this record, the feature-status table); U2 to U5 and U7 not started |
| Test status | 52 tests, all passing: the repository test for secrets, the test of its file listing, and the scanner's own tests (checkpoint A) |
| Verification 1, 2, 3 | Per checkpoint, in its verification record: checkpoint A passed all three. The whole stage passes them again at checkpoint D |
| Security status | No secret in the repository; the repository test for secrets runs on every push; the machine checks run read-only, with no repository secret; the dependency review found no published advisory (below) |
| Performance status | No hot path exists; no performance claim is made (the plan, section 5) |
| Documentation status | The [development guide](../development.md) written (checkpoint A); the numerical policy, contract conventions, threat model, and architecture-to-repository map come at checkpoints B to D |
| Traceability status | The verification matrix comes at checkpoint D (U7); until then the plan's section 3 and this record trace the requirements |
| Git commit | Each checkpoint's commit is in the [project state](../project-state.md)'s checkpoint log |
| Blockers | None |
| Next stage | DATA FOUNDATION, only after this stage's completion certificate and the owner's approval to proceed (the plan's completion criterion 8; §143, §156) |

## Checkpoints

| Checkpoint | Units | Status | Verification record |
|---|---|---|---|
| A | U1 development environment; U6 testing foundation and machine checks | Done: built; three gates passed (commit `f2e4046`); the machine checks pass on GitHub and fail on a deliberately broken check ("Machine checks on GitHub" below) | [Checkpoint A](stage-01-checkpoint-a-verification.md) |
| B | U2 exact amounts; U3 contract kernel | Not started | — |
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

Versions are fixed in `uv.lock`, `pyproject.toml`, and the workflow ([development guide](../development.md)); this table is the evidence of the review at checkpoint A, not a second list to maintain.

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
| The feature-status table's state for later stages | APPROVED, from the owner's acceptance of the complete documentation review (DEC-036), which the registry's Approval column records as "reviewed (DEC-036)". Under D6, a feature from APPROVED onward is ACTIVE in GOV-009's terms | The requirements of those stages are accepted; APPROVED is a lifecycle state, not an authorization to implement (the table says so). The owner may decide otherwise |
| The repository test for secrets, beyond the plan's minimum | 18 value patterns (issuers' token formats, credentials in a URL, quoted and unquoted credential-named settings, prefixed names such as `BINANCE_API_SECRET` included) and a list of secret-like file names; a test of the file listing itself. A setting's value, quoted or not, is reported only if it contains both a letter and a digit; templates, variable references, placeholders, and environment-variable names given as values are not reported; lines may end in LF or CRLF | The three Gate 3 runs found credential shapes missed and ordinary text wrongly reported, the third that the earlier fixes had covered samples rather than whole classes; U5 at checkpoint C extends the test to the example configuration files ("Carried to checkpoint C") |

## Carried to checkpoint B

The plan's technical claims for U2 and U3 (the decimal context and its traps, Hypothesis's decimal strategies, Pydantic's error rendering, and mypy's `truthy-bool` and unused-ignore behavior) were tested on 2026-10-05 with mypy 1.19.1, Pydantic 2.13.5, and Hypothesis 6.168.4 ([Stage 1 plan verification](stage-01-plan-verification.md), "Environment"). The locked versions are mypy 2.4.0, Pydantic 2.13.5, and Hypothesis 6.168.5, so checkpoint B re-tests each claim on them before relying on it; the move to mypy 2 matters most.

Also for checkpoint B: U3 relies on ruff's private-member rule SLF001, which is not among the rules enabled at checkpoint A (ruff's defaults plus `S`); checkpoint B enables it with the code it protects. And U6's Hypothesis setting ("builder details and plan wording" above).

## Carried to checkpoint C

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
