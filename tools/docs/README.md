# Documentation tooling

Project tooling, not platform code ([DEC-025](../../docs/decisions/DEC-025-documentation-tooling-in-repository.md); extended for Handoff Part 3 by [DEC-031](../../docs/decisions/DEC-031-part-3-reconciliation.md)). It needs only Python 3 and its standard library.

```text
python3 tools/docs/build_index.py              # check everything, then regenerate the indexes
python3 tools/docs/build_index.py --check-only # check only; writes nothing; fails if a generated file is out of date
python3 tools/docs/compare_requirements.py     # requirements added, removed, or changed since HEAD
python3 tools/docs/compare_requirements.py REV --strict  # compare with REV; exit 1 if an existing requirement was removed or changed
```

## What it generates

| File | What is generated |
|---|---|
| `docs/requirements/registry.md` | The whole file, from the requirement lines in the specifications |
| `docs/traceability/handoff-coverage.md` | The section and decision tables. The hand-written tables from "## §100 questions" onward are kept |
| `docs/traceability/part-2-reconciliation.md` | The "New requirements" column. Every other column and section is hand-written and kept |
| `docs/traceability/part-3-reconciliation.md` | The same, for Part 3 |

## What it checks

- **Requirement lines** follow the format in [`docs/requirements/README.md`](../../docs/requirements/README.md): known class, known prefix, a valid source (`§NN`, `P2§N`, `P3§N`, or `DEC-NNN`) that names an existing section. IDs are unique and numbered without gaps.
- **References:** every requirement, finding, decision, system, and system-rule (SR-nn) ID mentioned in `docs/` (outside code blocks and the historical handoffs) is defined.
- **Links:** every relative link resolves.
- **Part 1 coverage:** every section of Part 1 has a requirement or a stated process mapping.
- **Part 2 coverage:** every section of Part 2 (§1 to §350) has a row in the reconciliation, with either a new requirement or a disposition, and its title matches the historical copy.
- **Part 3 coverage:** the same for every section of Part 3 (§351 to §550).
- **System Rules Register:** rule IDs are unique and numbered without gaps; each row has the ARCH-038 fields; every rule names at least one canonical requirement; its classification is the class of the first one; no rule rests on an unapproved requirement (PROPOSED, FUTURE, REQUIRES CONFIRMATION, DEPRECATED).
- **Decisions:** every decision record is listed in the decision log.
- **Generated files are current** (`--check-only`): the generated files are rebuilt in memory and compared with the files on disk; any difference fails.
- **Requirement text** includes indented continuation lines under a requirement line (for example RSK-015's safety levels), in this checker and in `compare_requirements.py`.

## Requirement comparison

`compare_requirements.py` parses the requirement lines at a git revision and in the working tree and lists the IDs added, removed, or changed (title, class, source, text, or owning document), with before and after values. It is the check that nothing was dropped or reworded silently (ARCH-033; the owner's checkpoint rule, [DEC-032](../../docs/decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)). Run it before every checkpoint commit.

Run `build_index.py` after every documentation change and commit the regenerated files with the change. It does not check code, schemas, interfaces, or tests, which do not exist yet. That is the rest of ARCH-032.

## Code checks for the tools

The tools themselves are checked at every checkpoint with the project's linter, formatter, and type checker, ruff and mypy (TEC-009, [DEC-009](../../docs/decisions/DEC-009-technology-stack.md)). They are development checks, not dependencies: the scripts still run with Python 3 and its standard library alone.

```text
ruff check tools/docs                    # lint
ruff format --check tools/docs           # formatting (ruff's default style)
mypy --check-untyped-defs tools/docs     # types, including inside functions without annotations
```

The versions are not pinned yet: TEC-009's lockfile comes with the development environment at Stage 1. Versions last used: ruff 0.15.8, mypy 1.19.1, Python 3.11 ([integrity verification of 2026-10-01](../../docs/traceability/integrity-verification-2026-10-01.md)).

## Generated files

- The files in "What it generates" are committed: they are documentation that readers use. Their generated parts are always rebuilt by `build_index.py` and never edited by hand; the hand-written parts named in that table are kept. `--check-only` fails if a generated part is out of date.
- Python bytecode (`__pycache__/`), written for example by `python3 -m py_compile`, is never committed; `.gitignore` excludes it. The ruff and mypy caches (`.ruff_cache/`, `.mypy_cache/`) exclude themselves.
