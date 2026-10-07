# Developer Guide

> **Status:** ACTIVE — how to install, check, and test the platform from a clean clone (TEC-001, TEC-009, GOV-023; the [Stage 1 plan](roadmap/stage-01-foundation-plan.md), U1 and U6, location set by its decision D2). It describes the repository as it is; the rules for working in it are in `CLAUDE.md` and the texts it loads, and where the project stands is in the [project state](project-state.md).

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

At each checkpoint the requirement comparison is also run against the previous checkpoint: `python3 tools/docs/compare_requirements.py <commit> --strict` ([tools README](../tools/docs/README.md)).

### What the settings are

| Tool | Settings | Where |
|---|---|---|
| ruff | Python files only (documentation is not linted or formatted as code); ruff's default rules for the locked version, plus the whole security family (`S`); tests may use `assert` | `pyproject.toml` |
| mypy | Strict, for `src/` and `tests/`, with the extra error codes `truthy-bool`, `truthy-iterable`, `ignore-without-code`, `possibly-undefined`, `redundant-expr` and unreachable-code warnings | `pyproject.toml` |
| pytest | Unknown markers and configuration keys are errors; warnings are errors; an expected failure that passes is an error | `pyproject.toml` |
| Hypothesis | No project settings yet: when the `CI` or `GITHUB_ACTIONS` environment variable is set, as on the machine checks, Hypothesis loads its built-in `ci` profile (derandomized, so a run is reproducible; no time deadline; no example database). The setting of its pytest plugin is added to `pyproject.toml` with the first property tests (Stage 1, checkpoint B) | Built in |
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
| `tests/` | Tests. Tests of a module mirror its path under `src/atp/`; tests of the repository as a whole are in `tests/repository/` |
| `tools/docs/` | The documentation tooling ([README](../tools/docs/README.md)) |
| `docs/` | The project's knowledge base ([index](README.md)) |
| `pyproject.toml`, `uv.lock`, `.python-version` | Project definition, locked versions, Python version |
| `.github/workflows/` | The machine checks |

The other locations of D2 (`contracts/`, `config/examples/`) are created by the checkpoint that first puts a real artifact in them.

## Dependencies and versions

- **Adding a dependency, or replacing one, needs a decision record** ([technology stack](architecture/technology-stack.md); constitution Rules 99–101).
- **Where versions are fixed:** the libraries and tools in `uv.lock`; uv and the build backend `uv_build` in `pyproject.toml` (they move together, and the workflow's uv version and checksum with them); the actions, by commit hash, in the workflow.
- **Upgrading a locked version** (`uv lock --upgrade-package <name>`) is a change like any other: it repeats the dependency review (published advisories) and the license check, records both in the checkpoint's verification record, and passes the three gates.

## Secrets

Secrets never enter the repository (SEC-005). `.gitignore` excludes local environment and key files, and `tests/repository/test_no_secrets.py` fails if any file that is tracked, or that git would add, has a secret-like name or contains a credential-like value. It reads the files in the working tree, so run it before staging; the machine checks run it on exactly the pushed commit. The test reports where a match is, never the value. If it fails, remove the file or value; never weaken the test to pass (constitution Rule 116).
