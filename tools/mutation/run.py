"""Check 7: apply each mutation of `mutations.py` to a copy of the repository, one at a time;
each must make its check fail (DEC-045, decision 6).

Run from the repository root with the project's Python, giving a git clone of the repository to
mutate (the repository test for secrets lists files with git):

    uv run --locked python tools/mutation/run.py <clone> [--only PREFIX,...] [--slice K/N]

`--only` keeps the mutations whose names start with one of the prefixes; `--slice K/N` keeps
every N-th mutation from the K-th (counting from 0), so that N runs on N clones cover the list.
For each mutation the runner checks that its text occurs exactly once (else SKIPPED), writes
it, checks that a Python file still compiles and a TOML file still parses (else INVALID: such a
file would fail every check and look caught; another file, such as a document, is not checked),
runs the mutation's check in the clone, and restores the file.
KILLED means the check failed, SURVIVED that it passed, TIMEOUT that it ran past the time
limit. Last, the unmutated clone must pass every check the mutations used. The exit status is
0 only when every mutation is KILLED and that run passes.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

from mutations import MUTATIONS, SCANNER, SELFTEST, TESTS, TYPES, Mutation

_TIME_LIMIT = 900  # seconds per check run

_PYTEST = ["pytest", "-q", "-x", "-p", "no:cacheprovider"]
CHECKS: dict[str, list[str]] = {
    TESTS: [*_PYTEST, "--ignore=tests/repository/test_no_secrets.py"],
    TYPES: ["mypy", "--no-incremental"],
    SCANNER: [*_PYTEST, "tests/repository/test_no_secrets.py"],
    SELFTEST: ["python", "tools/docs/selftest.py"],
}


def _uv() -> str:
    uv = shutil.which("uv")
    if uv is None:
        sys.exit("uv is needed to run the checks")
    return uv


def _check(clone: Path, check: str) -> str:
    """Run one check in the clone: 'passed', 'failed', or 'timeout'."""
    try:
        result = subprocess.run(  # noqa: S603 - fixed arguments, no shell
            [_uv(), "run", "--locked", *CHECKS[check]],
            cwd=clone,
            capture_output=True,
            text=True,
            timeout=_TIME_LIMIT,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "timeout"
    return "passed" if result.returncode == 0 else "failed"


def _apply(clone: Path, mutation: Mutation) -> str:
    path = clone / mutation.path
    original = path.read_text(encoding="utf-8")
    found = original.count(mutation.old)
    if found != 1:
        return f"SKIPPED (found {found} times)"
    mutated = original.replace(mutation.old, mutation.new)
    try:
        if path.suffix == ".toml":
            tomllib.loads(mutated)
        elif path.suffix == ".py":
            compile(mutated, str(path), "exec")
    except tomllib.TOMLDecodeError:
        return "INVALID (does not parse)"
    except SyntaxError:
        return "INVALID (does not compile)"
    path.write_text(mutated, encoding="utf-8")
    try:
        outcome = _check(clone, mutation.check)
    finally:
        path.write_text(original, encoding="utf-8")
    return {"failed": "KILLED", "passed": "SURVIVED", "timeout": "TIMEOUT"}[outcome]


def _selected(only: str | None, part: str | None) -> list[Mutation]:
    selected = list(MUTATIONS)
    if only:
        prefixes = tuple(only.split(","))
        selected = [m for m in selected if m.name.startswith(prefixes)]
    if part:
        start, step = (int(number) for number in part.split("/"))
        selected = selected[start::step]
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("clone", type=Path, help="a git clone of the repository")
    parser.add_argument("--only", help="comma-separated prefixes of mutation names")
    parser.add_argument(
        "--slice", dest="part", help="K/N: every N-th mutation from the K-th"
    )
    options = parser.parse_args()
    if sys.version_info < (3, 12):  # noqa: UP036 - a script may be run by any Python
        sys.exit(
            "run with the project's Python: uv run --locked python tools/mutation/run.py"
        )
    clone = options.clone.resolve()
    here = Path(__file__).resolve().parents[2]
    if clone == here or not (clone / ".git").exists():
        sys.exit("give a git clone of the repository, not the repository itself")
    selected = _selected(options.only, options.part)
    results = []
    for mutation in selected:
        result = _apply(clone, mutation)
        results.append(result)
        print(f"{result.split(' ')[0]:<9}{mutation.name}", flush=True)
    killed = results.count("KILLED")
    print(f"{killed} of {len(selected)} mutations killed")
    checks = sorted({mutation.check for mutation in selected})
    sane = all(_check(clone, check) == "passed" for check in checks)
    print("unmutated clone:", "PASS" if sane else "FAIL")
    return 0 if killed == len(selected) and sane else 1


if __name__ == "__main__":
    sys.exit(main())
