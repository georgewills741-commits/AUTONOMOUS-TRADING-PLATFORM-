# Developer Guide

> **Status:** ACTIVE — how to install, check, and test the platform from a clean clone (TEC-001, TEC-009, GOV-023; the [Stage 1 plan](roadmap/stage-01-foundation-plan.md), U1 and U6, location set by its decision D2), and how its configuration is written and checked (U4). It describes the repository as it is; the rules for working in it are in `CLAUDE.md` and the texts it loads, and where the project stands is in the [project state](project-state.md).

<!-- Requirements: GOV-023 (every check, and how to run it, without Claude Code), GOV-012 (the test conventions); the verification matrix reads this marker -->

## Prerequisites

- **git.**
- **uv 0.12.23.** `pyproject.toml` requires exactly this version (`required-version`), so another version refuses to run. It is the version the lockfile was made with and the one the machine checks install. To install it from the Python package index, run, outside the repository, `uv tool install uv==0.12.23` or `pipx install uv==0.12.23`.
- **Python 3.12** (TEC-001; V-21). `.python-version` asks for 3.12; uv uses a Python 3.12 it finds on the machine, or installs one if it can.
- Network access to the Python package index for the first install.

## Install

```text
uv sync --locked
```

This creates `.venv/` and installs exactly the versions in `uv.lock`, the development tools included. With `--locked` it fails instead of changing anything if `uv.lock` does not match `pyproject.toml`.

## Checks

Every check below passes before a checkpoint commit, and the machine checks run the same commands, except `uv build`, on every push. `--locked` makes each command fail if the lockfile is out of date.

```text
uv run --locked ruff check                                # lint: src/, tests/, tools/
uv run --locked ruff format --check                       # formatting
uv run --locked mypy                                      # strict types: src/ and tests/
uv run --locked mypy --config-file tools/docs/mypy.ini    # types of the documentation tools
uv run --locked pytest                                    # tests
uv run --locked python tools/docs/build_index.py --check-only   # documentation checker
uv run --locked python tools/docs/selftest.py             # documentation tools' self-test
uv build                                                  # the package builds (output in dist/)
```

At each checkpoint the requirement comparison is also run against the previous checkpoint: `python3 tools/docs/compare_requirements.py <commit> --strict` ([tools README](../tools/docs/README.md)), and check 7, the mutation check, on a clone of the checkpoint's tree ([mutation tooling](../tools/mutation/README.md)).

### What the settings are

| Tool | Settings | Where |
|---|---|---|
| ruff | Python files only (documentation is not linted or formatted as code); ruff's default rules for the locked version, plus the whole security family (`S`) and the private-member rule (`SLF001`: no reading another object's `_members`, which keeps an outcome readable only through its `fold`); tests may use `assert` | `pyproject.toml` |
| mypy | Strict, for `src/`, `tests/`, and the mutation tooling (`tools/mutation/`), with the extra error codes `truthy-bool`, `truthy-iterable`, `ignore-without-code`, `possibly-undefined`, `redundant-expr` and unreachable-code warnings | `pyproject.toml` |
| pytest | Unknown markers and configuration keys are errors; warnings are errors; an expected failure that passes is an error | `pyproject.toml` |
| Hypothesis | Every run, local or on the machine checks, uses Hypothesis's built-in `ci` profile, set with the pytest option `--hypothesis-profile=ci`: derandomized, so every run tries the same examples and a failure reproduces; no time limit per example; no local example database; a failing example is printed so it can be replayed. Hypothesis still keeps a cache in `.hypothesis/`, which excludes itself from git | `pyproject.toml` (pytest's options) |
| The documentation tools | They keep the rule set and type-check level they were written to, for Python 3.10, the oldest version they support | `tools/docs/ruff.toml`, `tools/docs/mypy.ini` |

## Machine checks

`.github/workflows/checks.yml` runs the checks above, except `uv build`, on every push and pull request, on GitHub's Ubuntu 24.04 runner (GOV-023: they keep running without Claude Code). The job:

- has read-only repository permissions and does not keep the checkout's credentials;
- references no repository secret and deploys nothing;
- installs uv 0.12.23, verified against its published sha256 checksum, then `uv sync --locked`;
- uses two actions, `actions/checkout` and `astral-sh/setup-uv`, each pinned to a commit hash ([DEC-038](decisions/DEC-038-stage-1-plan-approved.md)).

## Repository layout

| Path | What it holds |
|---|---|
| `src/atp/` | The platform's Python package, `atp` (D1) |
| `tests/` | Tests. Tests of a module mirror its path under `src/atp/`; tests of the repository as a whole (secrets, structure) are in `tests/repository/`. `tests/conftest.py` configures the decimal context once for the test session, as a process does at start |
| `contracts/` | The committed JSON schema of each contract version ([contract conventions](architecture/contracts.md)) |
| `config/examples/` | The example configuration, placeholders only ("Configuration" below) |
| `tools/docs/` | The documentation tooling ([README](../tools/docs/README.md)) |
| `tools/mutation/` | Check 7's mutations and their runner ([README](../tools/mutation/README.md)) |
| `docs/` | The project's knowledge base ([index](README.md)) |
| `pyproject.toml`, `uv.lock`, `.python-version` | Project definition, locked versions, Python version |
| `.github/workflows/` | The machine checks |

Which module owns what, and where its tests and documentation are: the [architecture-to-repository map](architecture/source-of-truth-map.md#architecture-to-repository).

## Rules the code follows

- **Amounts:** built only with `atp.numeric.amount`, rounded only with `atp.numeric.quantize`; the decimal context is set once at process start with `configure_decimal_context()` ([numerical policy](architecture/numerical-policy.md)).
- **Contracts:** written on `atp.contracts.Contract`, adding only what the kernel lists (field constraints written with `Field`, `AfterValidator`, field validators in after mode); input from outside validated only with `from_python` or `from_json`, never the constructor; refusals rendered only through `validation_error_details`; validators that only check, returning the value they were given unchanged; written only with `to_json()` (all four caught in review, not by a check) ([contract conventions](architecture/contracts.md)).
- **Configuration:** read only through `atp.config` (GOV-014), which a process calls at start: `configure_process()`, then `load_configuration(...)` ("Configuration" above). The command-line module, `atp.cli`, imports only `atp.config`, and no module imports it.
- **Structure:** `tests/repository/test_structure.py` enforces the import directions between modules, however written (`from atp import contracts` and `atp.contracts.X` after `import atp` count), and that no module imports another package's private modules or names (a private name reached through a name bound to a package, `from atp import numeric` then `numeric._context`, is found by ruff's SLF001 instead); that no amount is built, and the decimal context is not touched, outside `atp.numeric`; that nothing rounds or converts to float silently (`round`, `to_integral`, `float`, the `math` module, integer division, and the others the [numerical policy](architecture/numerical-policy.md) lists); that TOML is read with `parse_float`, JSON with `parse_float` and `parse_constant`, and no amount is built from a value's text; that no outcome's private members are read outside `atp.contracts`; and that outside `atp.contracts` Pydantic is imported only as `Field`, `AfterValidator`, `field_validator`, `ValidationInfo`, and `ValidationError`, and no Pydantic model, dataclass, or validation method bypasses the contract kernel. Each rule is run on planted samples too. A new module needs its entry in the test's `ALLOWED_IMPORTS` and its row in the [architecture-to-repository map](architecture/source-of-truth-map.md#architecture-to-repository); a module that divides only integers, or needs floats, gets its entry in `INTEGER_DIVISION_ALLOWED` or `FLOAT_ALLOWED` by a reviewed change ([numerical policy](architecture/numerical-policy.md), N4).

### Writing a new contract version's schema

The tests fail when a contract's schema is not committed or differs from the committed file of its version. After adding a contract, or giving one a new version, write the new file and commit it:

```text
uv run --locked python -c "from pathlib import Path; from atp.numeric import configure_decimal_context; configure_decimal_context(); from atp.contracts import write_schema_files; print(write_schema_files(Path('contracts')))"
```

It never overwrites a committed version whose content differs: such a change needs a new version.

## Configuration

The platform's settings have one source, `atp.config` (GOV-014): a configuration directory, given to the process, never assumed (MIG-004), that holds two parts (MIG-010):

- `platform.toml`, the portable part, which moves with the platform from one environment to another;
- `environments/<environment>.toml`, one environment-specific file for each environment the platform runs in.

`config/examples/` holds one of each, for the six environments of OPS-004, with placeholder values only (GOV-017).

| Setting | Canonical source | Owner | Default | Allowed values | Validation | Security classification | When it changes | Tests |
|---|---|---|---|---|---|---|---|---|
| `platform_id` | `platform.toml`, the portable part: every environment | Hosting, backup, and migration (MIG-010, MIG-027) | None: required | Lowercase letters and digits, in parts joined by hyphens, starting with a letter | Contract `atp.config.portable` | An identifier, not secret | It names the platform instance (MIG-027): a different value is a different instance | `tests/config/test_settings.py`, `tests/config/test_load.py` |
| `environment` | `environments/<environment>.toml`, the environment-specific part: that environment | Deployment and operational readiness (OPS-004) | None: required | `development`, `testing`, `research`, `paper`, `staging`, `production` | Contract `atp.config.environment`; it must be the environment the process is run for | Not secret; it decides whether a trading-enabled credential may be declared | It is the file's identity: a file is for one environment | As above |
| `environment_id` | As `environment` | Hosting, backup, and migration (MIG-027) | None: required | As `platform_id` | Contract `atp.config.environment` | An identifier, not secret | It names this environment's instance (MIG-027) | As above |
| `secrets` | As `environment` | SYS-31 Security Architecture (SEC-005) | None declared | Tables of `name` (the process environment variable that holds the value: capital letters, digits, and underscores, starting with a letter) and `kind` (`server`, `ai`, or `trading`); a name declared once; `trading` only in `production` (MODE-006, SEC-004) | As above; each value read from the process environment | A declaration names a secret and is not secret; the value is secret: held as `atp.config.Secret`, never written in output, errors, or logs | Adding one makes the environment need its value; a value is changed in the process environment, never in a file | As above, `tests/config/test_secrets.py`, `tests/cli/test_cli.py` |

**How a file is read.** With the standard library's TOML reader, its floats through the amount constructor (`parse_float`), and then validated in its JSON form by the contract's `from_json`, so it is read exactly as the same settings written in JSON would be: an amount is written as a string, and a TOML date, time, or number with a fraction or an exponent is refused, since no setting takes one ([contract conventions](architecture/contracts.md), "Validating input").

**Secrets.** A declaration names a secret and gives its kind; its value is read from the process environment variable of that name, through `atp.config.SecretSource`, the one interface a secret manager can implement later (SEC-005). A declared secret that is not set or is empty, or whose value appears anywhere in either file, comments included, or in a setting's value as read, so that a TOML escape does not hide it, stops the load.

**Fail closed** (constitution Rule 108). A missing file or one that cannot be read, a file larger than V-41 of the [values register](requirements/values-register.md) allows (refused without being read in full: constitution Rule 150), a file that is not UTF-8, not valid TOML, or nested too deeply to read, a missing, unknown, or malformed setting, an unknown environment, a file that declares another environment than the one asked for, a trading-enabled credential outside production, and any of the secret refusals above each stop the load with `atp.config.ConfigurationError`. Its lines name the file, the setting, or the secret, and never hold a secret's value or a refused value: a refused setting is reported as the [contract conventions](architecture/contracts.md) render a refusal, a TOML error only by its position where the reader gives one, and a file that declares another environment by that environment's validated name.

**Checking a configuration.** The `atp` command checks one environment's configuration, reading the declared secrets from the process environment. It prints a summary in which every secret's value is `<redacted>`, and exits with 0 when the configuration is valid, 1 when it is refused (the reasons on standard error), and 2 when the command is used wrongly. To check an example, set its placeholder secret to any value first:

```text
ATP_EXAMPLE_SERVER_CREDENTIAL=<any value> uv run --locked atp config check --env paper --config-dir config/examples
```

**What the rules do not catch.** The configuration reads what is declared: whether a credential really carries trading permission at its venue is outside it, and the real barrier is that no trading credential exists outside production (the [Stage 1 plan](roadmap/stage-01-foundation-plan.md), section 3.2). A secret's value is searched for in the two files as text and in each setting's value as read, so a value written there in another form (encoded otherwise than by a TOML escape, or split) is not found; the repository test for secrets is a second layer for committed files ("Secrets" below). The limit on a file's size bounds the memory and time of reading one by measurement, not by proof: V-41's notes give the worst document found, and a process with less memory free than that document needs fails as at any allocation: with Python's `MemoryError` where its address space is limited, and otherwise it may be stopped by the kernel's out-of-memory killer with no Python error (inferred, not reproduced; [DEC-054](decisions/DEC-054-configuration-size-limit-and-retired-backup-branches.md)).

## Dependencies and versions

- **Adding a dependency, or replacing one, needs a decision record** ([technology stack](architecture/technology-stack.md); constitution Rules 99–101).
- **Where versions are fixed:** the libraries and tools in `uv.lock`; uv and the build backend `uv_build` in `pyproject.toml` (they move together, and the workflow's uv version and checksum with them); the actions, by commit hash, in the workflow.
- **Upgrading a locked version** (`uv lock --upgrade-package <name>`) is a change like any other: it repeats the dependency review (published advisories) and the license check, records both in the checkpoint's verification record, and passes the three gates.

## Secrets

Secrets never enter the repository (SEC-005). `.gitignore` excludes local environment and key files, and `tests/repository/test_no_secrets.py` fails if any file that is tracked, or that git would add, has a secret-like name or contains a credential-like value, or if a TOML file declares a secret otherwise than by a name and a kind as the configuration's own contract reads them (`atp.config.SecretDeclaration`) ("Configuration" above). It reads the files in the working tree, so run it before staging; the machine checks run it on exactly the pushed commit. The test reports where a match is, never the value. If it fails, remove the file or value; never weaken the test to pass (constitution Rule 116).
