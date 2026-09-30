# Documentation tooling

Project tooling, not platform code ([DEC-025](../../docs/decisions/DEC-025-documentation-tooling-in-repository.md)). It needs only Python 3 and its standard library.

```text
python3 tools/docs/build_index.py              # check everything, then regenerate the indexes
python3 tools/docs/build_index.py --check-only # check only; writes nothing
```

## What it generates

| File | What is generated |
|---|---|
| `docs/requirements/registry.md` | The whole file, from the requirement lines in the specifications |
| `docs/traceability/handoff-coverage.md` | The section and decision tables. The hand-written tables from "## §100 questions" onward are kept |
| `docs/traceability/part-2-reconciliation.md` | The "New requirements" column. Every other column and section is hand-written and kept |

## What it checks

- **Requirement lines** follow the format in [`docs/requirements/README.md`](../../docs/requirements/README.md): known class, known prefix, a valid source (`§NN`, `P2§N`, or `DEC-NNN`). IDs are unique and numbered without gaps.
- **References:** every requirement, finding, decision, and system ID mentioned in `docs/` (outside code blocks and the historical handoffs) is defined.
- **Links:** every relative link resolves.
- **Part 1 coverage:** every section of Part 1 has a requirement or a stated process mapping.
- **Part 2 coverage:** every section of Part 2 (§1 to §350) has a row in the reconciliation, with either a new requirement or a disposition, and its title matches the historical copy.
- **Decisions:** every decision record is listed in the decision log.

Run it after every documentation change and commit the regenerated files with the change. It does not check code, schemas, interfaces, or tests, which do not exist yet. That is the rest of ARCH-032.
