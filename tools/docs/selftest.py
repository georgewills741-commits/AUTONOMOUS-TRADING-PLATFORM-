"""Negative tests for the documentation tools: they must fail on broken input.

Each case copies the repository's docs/, tools/, README.md, and CLAUDE.md into a temporary
directory, breaks one thing there, and expects build_index.py --check-only (or
compare_requirements.py --strict) in the copy to fail with a matching message. An unmodified
copy must pass. The real repository is never modified.

Usage: python3 tools/docs/selftest.py
Standard library and git only. See tools/docs/README.md and DEC-033 (Verification 1).
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Callable

ROOT = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
)
RISK = "docs/risk/risk-engine.md"
GLOSSARY = "docs/glossary.md"


def copy_repo(dest: str) -> None:
    shutil.copytree(os.path.join(ROOT, "docs"), os.path.join(dest, "docs"))
    shutil.copytree(
        os.path.join(ROOT, "tools"),
        os.path.join(dest, "tools"),
        ignore=shutil.ignore_patterns("__pycache__"),
    )
    for f in ("README.md", "CLAUDE.md"):
        shutil.copy(os.path.join(ROOT, f), os.path.join(dest, f))


def edit(dest: str, rel: str, fn: Callable[[str], str]) -> None:
    """Apply fn to a file of the copy (created empty if missing), byte-exact newlines."""
    path = os.path.join(dest, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        open(path, "w", encoding="utf-8").close()
    before = open(path, encoding="utf-8", newline="").read()
    after = fn(before)
    if after == before:
        raise SystemExit(f"selftest: the mutation of {rel} had no effect")
    open(path, "w", encoding="utf-8", newline="").write(after)


def run(dest: str, *args: str) -> tuple[int, str]:
    r = subprocess.run(
        [sys.executable, "-B", *args], cwd=dest, capture_output=True, text=True
    )
    return r.returncode, r.stdout + r.stderr


def drop_line(prefix: str) -> Callable[[str], str]:
    def fn(s: str) -> str:
        return "\n".join(x for x in s.split("\n") if not x.startswith(prefix))

    return fn


# (name, file to break, how, message the checker must print)
CHECKER_CASES: list[tuple[str, str, Callable[[str], str], str]] = [
    (
        "broken link",
        GLOSSARY,
        lambda s: s + "\n[x](no-such-file.md)\n",
        r"broken link no-such-file\.md",
    ),
    (
        "duplicate requirement ID",
        RISK,
        lambda s: s.replace("- **RSK-048** ", "- **RSK-001** ", 1),
        r"RSK-001",
    ),
    (
        "unknown class",
        RISK,
        lambda s: re.sub(
            r"(- \*\*RSK-001\*\* [^·]+ · )[A-Z /]+?( · )",
            r"\1MAYBE REQUIRED\2",
            s,
            count=1,
        ),
        r"RSK-001: unknown class",
    ),
    (
        "undefined finding",
        GLOSSARY,
        lambda s: s + "\nSee CF-99.\n",
        r"undefined finding CF-99",
    ),
    (
        "undefined decision",
        GLOSSARY,
        lambda s: s + "\nSee DEC-999.\n",
        r"undefined decision DEC-999",
    ),
    (
        "undefined system rule",
        GLOSSARY,
        lambda s: s + "\nSee SR-99.\n",
        r"undefined system rule SR-99",
    ),
    (
        "undefined requirement",
        GLOSSARY,
        lambda s: s + "\nSee RSK-999.\n",
        r"undefined requirement RSK-999",
    ),
    (
        "gap in requirement numbering",
        RISK,
        drop_line("- **RSK-047** "),
        r"prefix RSK not sequential",
    ),
    (
        "stale generated registry",
        "docs/requirements/registry.md",
        lambda s: s + "\nextra\n",
        r"registry\.md is out of date",
    ),
    (
        "decision missing from the log",
        "docs/decisions/README.md",
        drop_line("| [DEC-034]"),
        r"DEC-034 missing from decisions/README\.md",
    ),
    (
        "system rule resting on a proposal",
        "docs/requirements/system-rules-register.md",
        lambda s: s.replace(
            "| SR-47 | No unsafe fast path | PERF-023, RSK-034 |",
            "| SR-47 | No unsafe fast path | PERF-023, RSK-034, GOV-018 |",
            1,
        ),
        r"SR-47: canonical requirement GOV-018 is not approved",
    ),
    (
        "preserved text changed",
        "docs/builder/master-execution-constitution.md",
        lambda s: s.replace(
            "The repository is the durable project state.",
            "The repository is a durable project state.",
            1,
        ),
        r"master-execution-constitution\.md: preserved text changed",
    ),
    (
        "preserved text not listed",
        "tools/docs/preserved-texts.sha256",
        lambda s: "\n".join(
            x
            for x in s.split("\n")
            if not x.endswith("verification-and-platform-independence-directive.md")
        ),
        r"verification-and-platform-independence-directive\.md: preserved text not listed",
    ),
    (
        "orphaned document",
        "docs/orphan.md",
        lambda s: s + "# Orphan\n",
        r"orphan\.md: not reachable by links",
    ),
]

MEC = "docs/builder/master-execution-constitution.md"
DIRECTIVE = "docs/builder/verification-and-platform-independence-directive.md"

# Cases that edit several files, and cases that must pass (expected message None).
MULTI_CASES: list[tuple[str, list[tuple[str, Callable[[str], str]]], str | None]] = [
    (
        "a '>' line added to a preserved text after its banner",
        [
            (
                MEC,
                lambda s: s.replace(
                    "\n\n```text\nSTATUS:",
                    "\n\n> NOTE: §52 no longer applies.\n\n```text\nSTATUS:",
                    1,
                ),
            )
        ],
        r"master-execution-constitution\.md: preserved text changed",
    ),
    (
        "a file added in a subdirectory of docs/builder/",
        [("docs/builder/extra/override.md", lambda s: s + "# Override\n")],
        r"docs/builder/extra/override\.md: preserved text not listed",
    ),
    (
        "a non-Markdown file added to docs/builder/",
        [("docs/builder/override.txt", lambda s: s + "override\n")],
        r"docs/builder/override\.txt: preserved text not listed",
    ),
    (
        "a preserved text converted to CR LF line endings",
        [(DIRECTIVE, lambda s: s.replace("\n", "\r\n"))],
        r"verification-and-platform-independence-directive\.md: preserved text (changed|has CR)",
    ),
    (
        "two documents that link only to each other",
        [
            ("docs/pair-a.md", lambda s: s + "# A\n\n[B](pair-b.md)\n"),
            ("docs/pair-b.md", lambda s: s + "# B\n\n[A](pair-a.md)\n"),
        ],
        r"pair-a\.md: not reachable by links",
    ),
    (
        "a document linked only inside inline code",
        [
            ("docs/coded.md", lambda s: s + "# Coded\n"),
            (GLOSSARY, lambda s: s + "\nSee `[coded](coded.md)`.\n"),
        ],
        r"coded\.md: not reachable by links",
    ),
    (
        "a status-banner-only change to a preserved text (must pass)",
        [
            (
                MEC,
                lambda s: s.replace(
                    "> **Status:** ACTIVE —",
                    "> **Status:** ACTIVE (banner edited) —",
                    1,
                ),
            )
        ],
        None,
    ),
]


def checker_cases() -> bool:
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        control = os.path.join(tmp, "control")
        copy_repo(control)
        code, out = run(control, "tools/docs/build_index.py", "--check-only")
        passed = code == 0
        ok &= passed
        print(
            f"{'PASS' if passed else 'FAIL'}  control: an unmodified copy passes (exit {code})"
        )
        if not passed:
            print(out[-2000:])
        for n, (name, rel, fn, pattern) in enumerate(CHECKER_CASES):
            dest = os.path.join(tmp, f"case{n}")
            copy_repo(dest)
            edit(dest, rel, fn)
            code, out = run(dest, "tools/docs/build_index.py", "--check-only")
            passed = code != 0 and re.search(pattern, out) is not None
            ok &= passed
            print(
                f"{'PASS' if passed else 'FAIL'}  checker rejects: {name} (exit {code})"
            )
            if not passed:
                print(out[-2000:])
        for n, (name, edits, expect) in enumerate(MULTI_CASES):
            dest = os.path.join(tmp, f"multi{n}")
            copy_repo(dest)
            for rel, fn in edits:
                edit(dest, rel, fn)
            code, out = run(dest, "tools/docs/build_index.py", "--check-only")
            if expect is None:
                passed = code == 0
                verdict = "accepts"
            else:
                passed = code != 0 and re.search(expect, out) is not None
                verdict = "rejects"
            ok &= passed
            print(
                f"{'PASS' if passed else 'FAIL'}  checker {verdict}: {name} (exit {code})"
            )
            if not passed:
                print(out[-2000:])
    return ok


def comparison_cases() -> bool:
    """compare_requirements.py --strict must fail on a reworded, reclassified, or removed requirement."""
    ok = True
    cases: list[tuple[str, Callable[[str], str], str]] = [
        (
            "reworded requirement",
            lambda s: re.sub(
                r"(- \*\*RSK-001\*\* [^\n]*?)\.\n", r"\1 (edited).\n", s, count=1
            ),
            r"changed \(1\)",
        ),
        (
            "reclassified requirement",
            lambda s: re.sub(
                r"(- \*\*RSK-002\*\* [^·]+ · )[A-Z /]+?( · )",
                r"\1PROPOSED\2",
                s,
                count=1,
            ),
            r"changed \(1\)",
        ),
        ("removed requirement", drop_line("- **RSK-048** "), r"removed \(1\)"),
    ]
    with tempfile.TemporaryDirectory() as tmp:
        copy_repo(tmp)
        git = [
            "git",
            "-C",
            tmp,
            "-c",
            "user.name=selftest",
            "-c",
            "user.email=selftest@localhost",
        ]
        for cmd in (["init", "-q"], ["add", "-A"], ["commit", "-q", "-m", "baseline"]):
            subprocess.run(git + cmd, check=True, capture_output=True)
        code, out = run(tmp, "tools/docs/compare_requirements.py", "HEAD", "--strict")
        passed = code == 0
        ok &= passed
        print(
            f"{'PASS' if passed else 'FAIL'}  comparison control: no change passes (exit {code})"
        )
        original = open(os.path.join(tmp, RISK), encoding="utf-8").read()
        for name, fn, pattern in cases:
            edit(tmp, RISK, fn)
            code, out = run(
                tmp, "tools/docs/compare_requirements.py", "HEAD", "--strict"
            )
            passed = code != 0 and re.search(pattern, out) is not None
            ok &= passed
            print(
                f"{'PASS' if passed else 'FAIL'}  comparison rejects: {name} (exit {code})"
            )
            if not passed:
                print(out[-2000:])
            open(os.path.join(tmp, RISK), "w", encoding="utf-8").write(original)
    return ok


if __name__ == "__main__":
    results = [checker_cases(), comparison_cases()]
    print("selftest:", "PASS" if all(results) else "FAIL")
    sys.exit(0 if all(results) else 1)
