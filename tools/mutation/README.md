# Mutation tooling (check 7)

Project tooling, not platform code: the list of mutations of check 7 and the script that applies them, kept in the repository from Stage 1's checkpoint C so that any session can repeat the check ([DEC-045](../../docs/decisions/DEC-045-apply-foundation-convergence-audit.md), decision 6; master execution constitution §22).

**The standard (DEC-045, decision 6):** every rule the code enforces has a test that fails when the rule is removed (master execution constitution §148, "What enforcement has no test?"; §76). No score is set. A mutation that survives is analysed: a missing test is added, or the mutation is recorded as having no effect. During a checkpoint's rounds, the mutations of changed code and of rules whose tests changed are run; the full list runs once on the checkpoint's final tree, and the verification record states the result.

| File | What it holds |
|---|---|
| [`mutations.py`](mutations.py) | The list. Each entry names the rule it removes, the file, the text replaced, which must occur exactly once, its replacement, and the check that must then fail: `tests` (the tests, without the repository test for secrets), `types` (the strict type check), or `scanner` (the repository test for secrets). Checkpoints A and B's entries come from the checks as they ran ([Stage 1 mutation checks as run](../../docs/traceability/stage-01-mutation-checks.md)), check 11's twentieth (M21) as an ordinary entry, and one entry's text, "no string prefixes", follows the pattern as checkpoint C changed it; checkpoint C's follow |
| [`run.py`](run.py) | The runner, described in its docstring |

Run it from the repository root with the project's Python, on a git clone of the repository holding the tree to check; it refuses to mutate the repository it is run from:

```text
uv run --locked python tools/mutation/run.py <clone>                          # the whole list
uv run --locked python tools/mutation/run.py <clone> --only "U4 ,U5 "        # names starting with "U4 " or "U5 "
uv run --locked python tools/mutation/run.py <clone> --slice 0/4             # every fourth mutation, from the first
```

Each result line is `KILLED`, `SURVIVED`, `SKIPPED` (its text no longer occurs exactly once: the entry is out of date), `INVALID` (the mutated file does not compile), or `TIMEOUT`. The last lines give the count killed and whether the unmutated clone passes every check used. The exit status is 0 only when every mutation is killed and that run passes. The checks run with the first `uv` on `PATH`, which must be the version `pyproject.toml` requires (`required-version`, in the [developer guide](../../docs/development.md)'s prerequisites): another version refuses to run, so every check fails and every mutation reads `KILLED`, and only the unmutated clone's failure, with the exit status 1, shows that the run proved nothing.

**Keeping it current:** a change that adds or changes a rule adds or updates its entries in the same change, and a change that rewrites the text an entry replaces updates the entry. An entry of checkpoint A or B whose text a later change rewrote keeps its name, so the verification records' results stay traceable.
