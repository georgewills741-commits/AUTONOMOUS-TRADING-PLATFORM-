# Documentation tooling

Project tooling, not platform code ([DEC-025](../../docs/decisions/DEC-025-documentation-tooling-in-repository.md); extended for Handoff Part 3 by [DEC-031](../../docs/decisions/DEC-031-part-3-reconciliation.md) for the master execution constitution by [DEC-033](../../docs/decisions/DEC-033-adopt-master-execution-constitution.md), and for Stage 1's verification matrix by U7 of the [Stage 1 plan](../../docs/roadmap/stage-01-foundation-plan.md), approved with its decision D10 by [DEC-038](../../docs/decisions/DEC-038-stage-1-plan-approved.md)). It needs only Python 3.10 or later and its standard library (and git, for the comparison and the self-test).

```text
python3 tools/docs/build_index.py              # check everything, then regenerate the indexes and the verification matrix
python3 tools/docs/build_index.py --check-only # check only; writes nothing; fails if a generated file is out of date
python3 tools/docs/compare_requirements.py     # requirements added, removed, or changed since HEAD
python3 tools/docs/compare_requirements.py REV --strict  # compare with REV; exit 1 if an existing requirement was removed or changed
python3 tools/docs/compare_requirements.py REV --strict --expect-changed=ID:cls,ID:removed  # the same, when a decision record deliberately changes exactly these, in exactly these fields
python3 tools/docs/selftest.py                 # negative tests: the checker and the comparison must fail on broken input
```

The checker and the comparison import [`code_blocks.py`](code_blocks.py) from their own directory, so they run as scripts, as above, not with `python3 -I` or `-P`, or with `PYTHONSAFEPATH` set, which leave that directory off the import path. Python may leave its cache of that module in `tools/docs/__pycache__/`, which git ignores; apart from it, `--check-only` writes nothing.

At every checkpoint run the three checking commands (`--check-only`, the comparison with the previous checkpoint, and the self-test) and the code checks below. With the round trip of any newly preserved text, they are part of Verification 1 (DEC-033; what each gate covers now: [DEC-039](../../docs/decisions/DEC-039-adopt-quality-and-correction-directive.md)), together with the checks of the code in the [developer guide](../../docs/development.md).

## What it generates

| File | What is generated |
|---|---|
| `docs/requirements/registry.md` | The whole file, from the requirement lines in the specifications |
| `docs/traceability/handoff-coverage.md` | The section and decision tables. The hand-written tables from "## §100 questions" onward are kept |
| `docs/traceability/part-2-reconciliation.md` | The "New requirements" column. Every other column and section is hand-written and kept |
| `docs/traceability/part-3-reconciliation.md` | The same, for Part 3 |
| `docs/traceability/verification-matrix.md` | The whole file, from the requirement markers (below), the registry, the System Rules Register, the Stage 1 plan's section 3, and the stage record's checkpoints |

## What it checks

- **Requirement lines** follow the format in [`docs/requirements/README.md`](../../docs/requirements/README.md): known class, known prefix, a valid source (`§NN`, `P2§N`, `P3§N`, or `DEC-NNN`) that names an existing section. IDs are unique and numbered without gaps.
- **References:** every requirement, finding, decision, system, and system-rule (SR-nn) ID mentioned in `docs/` (outside code blocks and the historical handoffs) is defined.
- **Links:** every relative link resolves.
- **Code blocks:** a code block opens on a line that starts with three or more backticks and closes only on a line of at least as many backticks and nothing else, as CommonMark closes a backtick fence, so a longer fence can hold shorter ones, such as a report quoted with its own code blocks; a block left open fails. Fences of tildes and indented fences are not recognized; no document uses them. Requirement lines, references, and links, those that make a document reachable included, are read only outside code blocks. The rule is in [`code_blocks.py`](code_blocks.py), which `compare_requirements.py` uses too, so both read the same lines as code.
- **Part 1 coverage:** every section of Part 1 has a requirement or a stated process mapping.
- **Part 2 coverage:** every section of Part 2 (§1 to §350) has a row in the reconciliation, with either a new requirement or a disposition, and its title matches the historical copy.
- **Part 3 coverage:** the same for every section of Part 3 (§351 to §550).
- **System Rules Register:** rule IDs are unique and numbered without gaps; each row has the ARCH-038 fields; every rule names at least one canonical requirement; its classification is the class of the first one; no rule rests on an unapproved requirement (PROPOSED, FUTURE, REQUIRES CONFIRMATION, DEPRECATED).
- **Decisions:** every decision record is listed in the decision log.
- **Requirement markers** (below): each names at least one requirement, and every requirement it names exists and is approved; a marker that names a PROPOSED, FUTURE, PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION, or DEPRECATED / REPLACED requirement fails (ARCH-029, GOV-017: nothing unapproved is implemented). A `req` marker is written on one line, as a decorator of a test function, and takes only requirement IDs, written as strings.
- **Stage 1's delivered requirements:** every requirement of the Stage 1 plan's section 3.1 has an implementation marker and a test or check marker, and every unit the plan assigns it is in a checkpoint of the [stage record](../../docs/traceability/stage-01-foundation.md) (U7's acceptance, as a check).
- **Generated files are current** (`--check-only`): the generated files are rebuilt in memory and compared with the files on disk; any difference fails.
- **Requirement text** includes indented continuation lines under a requirement line (for example RSK-015's safety levels), in this checker and in `compare_requirements.py`.
- **Preserved texts stay as received:** every file under `docs/handoffs/` and `docs/builder/`, in subdirectories too and of any type, is listed in [`preserved-texts.sha256`](preserved-texts.sha256) with its SHA-256. For a Markdown text the hash covers the title line and everything after the status banner; the banner is the first block of `>` lines after the title, so a `>` line anywhere later is part of the text. Files are read byte-exact, so changed line endings fail too. A changed text, a file not listed, or a listed file that is missing fails. A banner may change by decision; the text never does, except to restore the words as received where a comparison with them shows the copy differs: the restoration is made by a decision, its banner records it, and its line changes then, after the round trip of the restored text ([DEC-047](../../docs/decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 8). A new line is added only when a decision record adds a new preserved text, after its round trip against the text as received. A round trip takes the text as received from the session record, by script, one recorded message at a time, so that turns delivered together stay apart and the client's own prompts stay out, never from a copy written out of the conversation; a text kept in a text block must equal it byte for byte, and a text converted to Markdown must equal it word for word and line for line, as DEC-004 asks: each non-blank line the same once the Markdown the conversion added (heading marks, list markers, emphasis, fences, horizontal rules) and separator lines of ten or more "=" are removed, apart from the changes its formatting note records (DEC-047, decision 8).
- **Status banners of preserved texts:** their links resolve (the texts themselves are not checked for references or links: they are kept as received).
- **No orphaned documents** (master execution constitution §71, §73): every document under `docs/` is reachable by links, outside code, from `README.md`, `CLAUDE.md`, `docs/README.md`, or this README. Two documents that link only to each other are orphaned. This checks reachability only; a document's purpose and owner are checked in review.

## Self-test

`selftest.py` copies `docs/`, `tools/`, `src/`, `tests/`, `contracts/`, `.github/workflows/`, `README.md`, `CLAUDE.md`, and `pyproject.toml` into a temporary directory, breaks one thing at a time, and expects the checker or the comparison to fail with the right message: a broken link, a duplicate or unknown ID, a gap in numbering, a stale generated file, a decision missing from the log, a system rule resting on a proposal, a changed or unlisted preserved text (a changed word, a `>` line added after the banner, a new file in a subdirectory or of another type, changed line endings), an orphaned document (unlinked, linked only from inside code, or linked only by another orphan), a code block never closed, a reference after a longer fence that holds a shorter one, a requirement marker that names no requirement, an unknown one, or a DEPRECATED / REPLACED, PROPOSED, or FUTURE one, a requirement of the Stage 1 plan's section 3.1 left without an implementation or without a test, a unit of that section in no checkpoint of the stage record, a `req` marker that does not decorate a test function, takes something other than requirement IDs, or is written otherwise than as a decorator, a verification matrix edited by hand, and a reworded, reclassified, or removed requirement; with `--expect-changed`, the comparison must accept exactly the listed changes (including a listed class-only change and a listed removal) and reject an extra one, a missing one, a reworded text where only a class change is expected, a removal where only a change is expected, and a duplicated entry. An unmodified copy, one whose only change is a preserved text's status banner, one whose marker names a requirement inside a parenthesis, one with a `req` marker above another decorator written on several lines, and one that quotes IDs and a broken link inside a longer fence's inner block must pass, and the comparison must accept a requirement line quoted there. It never touches the repository itself. It makes Verification 1's negative tests repeatable (master execution constitution §22).

## Requirement comparison

`compare_requirements.py` parses the requirement lines at a git revision and in the working tree and lists the IDs added, removed, or changed (title, class, source, text, or owning document), with before and after values. It is the check that nothing was dropped or reworded silently (ARCH-033; the owner's checkpoint rule, [DEC-032](../../docs/decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)). Run it before every checkpoint commit.

When a decision record deliberately changes existing requirements, list them with `--expect-changed`: `ID` means changed in any field but not removed; `ID:cls` (or `ID:cls+text`, any of title, cls, src, text, doc) means changed in exactly those fields; `ID:removed` means removed. With `--strict`, the check passes only if exactly the listed requirements changed, exactly as listed; a duplicated or empty entry is refused. The decision record names the command it was checked with.

Run `build_index.py` after every documentation change and commit the regenerated files with the change. It reads the code and the tests only for their requirement markers: it does not check the code, schemas, or interfaces themselves, which the code checks of the [developer guide](../../docs/development.md) do. That is the rest of ARCH-032, of which the verification matrix (below) is Stage 1's increment.

## Requirement markers and the verification matrix

The [verification matrix](../../docs/traceability/verification-matrix.md) (U7 of the [Stage 1 plan](../../docs/roadmap/stage-01-foundation-plan.md); master execution constitution §74, §145; ARCH-031, ARCH-040) is generated from markers that name the requirements an artifact implements or a test or check verifies. [`markers.py`](markers.py) reads them as text, not with `ast`, so that the tools keep running on Python 3.10 while the platform's code uses Python 3.12.

| Marker | Where | What it says |
|---|---|---|
| A paragraph that begins `Requirements:` | The docstring of a Python module under `src/` or `tools/`; a block of `#` comments in `pyproject.toml` or in a workflow under `.github/workflows/`; an HTML comment, `<!-- Requirements: ... -->`, in a document under `docs/` (outside the preserved texts, the generated files, and code blocks) | The artifact implements the requirements it names |
| A paragraph that begins `Verifies:` | The same places | A check that is not a pytest test verifies them: a tool's self-test, or a gate or run recorded in a verification record |
| `@pytest.mark.req("ID", ...)` | One line, as a decorator of a test function under `tests/` | The test verifies the requirements it names |

A marker names the requirement IDs written outside parentheses, up to the end of its first sentence or of its paragraph, whichever comes first; a parenthesis explains and marks nothing, so `Requirements: TEC-003 (not ARCH-034).` names TEC-003 only. Decision IDs are never marked. Name a requirement only where the artifact implements it or the test or check proves it: a marker is not evidence by itself, and Gate 3 checks that each marked test exercises the requirement it names (U7's acceptance). The `req` marker is registered in `pyproject.toml`, where pytest's `--strict-markers` refuses a misspelt marker name.

After adding, changing, or removing a marker or a test function, run `build_index.py` and commit the regenerated matrix with the change: the matrix also lists every test module with its number of test functions, so a new test changes it. The matrix's first table and the check of the delivered requirements read the Stage 1 plan only.

## Code checks for the tools

The tools themselves are checked at every checkpoint with the project's linter, formatter, and type checker, ruff and mypy (TEC-009, [DEC-009](../../docs/decisions/DEC-009-technology-stack.md)), and by the machine checks on every push. They are development checks, not dependencies: the scripts still run with Python 3 and its standard library alone.

```text
uv run --locked ruff check tools/docs                     # lint
uv run --locked ruff format --check tools/docs            # formatting
uv run --locked mypy --config-file tools/docs/mypy.ini    # types, including inside functions without annotations
```

The tools keep the rule set and type-check level they were written to: [`ruff.toml`](ruff.toml) selects ruff's former default rules (E4, E7, E9, F) and [`mypy.ini`](mypy.ini) checks the bodies of functions without annotations, both for Python 3.10, the oldest version the tools support. The rest of the repository uses the stricter project settings in `pyproject.toml` ([developer guide](../../docs/development.md)). The tool versions are pinned in `uv.lock` since Stage 1's checkpoint A; until then they were not pinned, and ruff 0.15.8, mypy 1.19.1, and Python 3.11 were last used ([integrity verification of 2026-10-01](../../docs/traceability/integrity-verification-2026-10-01.md)).

## Generated files

- The files in "What it generates" are committed: they are documentation that readers use. Their generated parts are always rebuilt by `build_index.py` and never edited by hand; the hand-written parts named in that table are kept. `--check-only` fails if a generated part is out of date.
- Python bytecode (`__pycache__/`), written for example by `python3 -m py_compile`, is never committed; `.gitignore` excludes it. The ruff and mypy caches (`.ruff_cache/`, `.mypy_cache/`, here and at the repository root) exclude themselves.
