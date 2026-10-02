# Documentation tooling

Project tooling, not platform code ([DEC-025](../../docs/decisions/DEC-025-documentation-tooling-in-repository.md); extended for Handoff Part 3 by [DEC-031](../../docs/decisions/DEC-031-part-3-reconciliation.md) and for the master execution constitution by [DEC-033](../../docs/decisions/DEC-033-adopt-master-execution-constitution.md)). It needs only Python 3.10 or later and its standard library (and git, for the comparison and the self-test).

```text
python3 tools/docs/build_index.py              # check everything, then regenerate the indexes
python3 tools/docs/build_index.py --check-only # check only; writes nothing; fails if a generated file is out of date
python3 tools/docs/compare_requirements.py     # requirements added, removed, or changed since HEAD
python3 tools/docs/compare_requirements.py REV --strict  # compare with REV; exit 1 if an existing requirement was removed or changed
python3 tools/docs/compare_requirements.py REV --strict --expect-changed=ID:cls,ID:removed  # the same, when a decision record deliberately changes exactly these, in exactly these fields
python3 tools/docs/selftest.py                 # negative tests: the checker and the comparison must fail on broken input
```

At every checkpoint run the three checking commands (`--check-only`, the comparison with the previous checkpoint, and the self-test) and the code checks below. With the round trip of any newly preserved text, they are Verification 1 until code exists (DEC-033).

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
- **Preserved texts never change:** every file under `docs/handoffs/` and `docs/builder/`, in subdirectories too and of any type, is listed in [`preserved-texts.sha256`](preserved-texts.sha256) with its SHA-256. For a Markdown text the hash covers the title line and everything after the status banner; the banner is the first block of `>` lines after the title, so a `>` line anywhere later is part of the text. Files are read byte-exact, so changed line endings fail too. A changed text, a file not listed, or a listed file that is missing fails. A banner may change by decision; the text never does. A new line is added only when a decision record adds a new preserved text, after its round trip against the text as received.
- **Status banners of preserved texts:** their links resolve (the texts themselves are not checked for references or links: they are kept as received).
- **No orphaned documents** (master execution constitution §71, §73): every document under `docs/` is reachable by links, outside code, from `README.md`, `CLAUDE.md`, `docs/README.md`, or this README. Two documents that link only to each other are orphaned. This checks reachability only; a document's purpose and owner are checked in review.

## Self-test

`selftest.py` copies `docs/`, `tools/`, `README.md`, and `CLAUDE.md` into a temporary directory, breaks one thing at a time, and expects the checker or the comparison to fail with the right message: a broken link, a duplicate or unknown ID, a gap in numbering, a stale generated file, a decision missing from the log, a system rule resting on a proposal, a changed or unlisted preserved text (a changed word, a `>` line added after the banner, a new file in a subdirectory or of another type, changed line endings), an orphaned document (unlinked, linked only from inside code, or linked only by another orphan), and a reworded, reclassified, or removed requirement; with `--expect-changed`, the comparison must accept exactly the listed changes (including a listed class-only change and a listed removal) and reject an extra one, a missing one, a reworded text where only a class change is expected, a removal where only a change is expected, and a duplicated entry. An unmodified copy, and one whose only change is a preserved text's status banner, must pass. It never touches the repository itself. It makes Verification 1's negative tests repeatable (master execution constitution §22).

## Requirement comparison

`compare_requirements.py` parses the requirement lines at a git revision and in the working tree and lists the IDs added, removed, or changed (title, class, source, text, or owning document), with before and after values. It is the check that nothing was dropped or reworded silently (ARCH-033; the owner's checkpoint rule, [DEC-032](../../docs/decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)). Run it before every checkpoint commit.

When a decision record deliberately changes existing requirements, list them with `--expect-changed`: `ID` means changed in any field but not removed; `ID:cls` (or `ID:cls+text`, any of title, cls, src, text, doc) means changed in exactly those fields; `ID:removed` means removed. With `--strict`, the check passes only if exactly the listed requirements changed, exactly as listed; a duplicated or empty entry is refused. The decision record names the command it was checked with.

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
