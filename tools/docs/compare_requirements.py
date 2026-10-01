"""Compare the requirements in the working tree with those at a git revision.

Lists every requirement that was added, removed, moved to another document, or whose title, class,
source, or text changed. Use it after any documentation change to confirm that only the intended
requirements changed and nothing was dropped silently (ARCH-033; owner's checkpoint rule, DEC-032).

Usage: python3 tools/docs/compare_requirements.py [REV] [--strict]
  REV       git revision to compare against (default: HEAD)
  --strict  exit with status 1 if any requirement that exists at REV was removed or changed
Standard library only. Reads docs/**/*.md except docs/builder/ and docs/handoffs/, like build_index.py.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
EXCLUDE = ("docs/builder/", "docs/handoffs/")
GENERATED = {"docs/requirements/registry.md", "docs/traceability/handoff-coverage.md"}
LINE_RE = re.compile(r"^- \*\*(?P<id>[A-Z]{2,4}-\d{3})\*\* (?P<title>[^·]+?) · (?P<cls>[A-Z /]+?) · "
                     r"(?P<src>[^—]+?) — (?P<text>.+)$")

args = [a for a in sys.argv[1:] if not a.startswith("--")]
REV = args[0] if args else "HEAD"
STRICT = "--strict" in sys.argv


def parse(files):
    """files: {relative path: content}. Returns {id: dict}."""
    out = {}
    for path, content in files.items():
        in_code = False
        last = None  # indented continuation lines (e.g. RSK-015's levels) are part of the requirement's text
        for line in content.splitlines():
            if line.startswith("```"):
                in_code = not in_code
                last = None
                continue
            if in_code:
                continue
            if last and line.startswith("  ") and line.strip():
                out[last]["text"] += " " + line.strip()
                continue
            last = None
            m = LINE_RE.match(line)
            if m:
                d = m.groupdict()
                d["doc"] = path
                out[d["id"]] = d
                last = d["id"]
    return out


def wanted(path):
    return path.startswith("docs/") and path.endswith(".md") and not path.startswith(EXCLUDE) and path not in GENERATED


def git(*a):
    return subprocess.run(["git", "-C", ROOT, *a], check=True, capture_output=True, text=True).stdout


old_files = {}
for path in git("ls-tree", "-r", "--name-only", REV, "docs").splitlines():
    if wanted(path):
        old_files[path] = git("show", f"{REV}:{path}")
new_files = {}
for dp, _, fn in os.walk(os.path.join(ROOT, "docs")):
    for f in fn:
        path = os.path.relpath(os.path.join(dp, f), ROOT).replace(os.sep, "/")
        if wanted(path):
            new_files[path] = open(os.path.join(ROOT, path), encoding="utf-8").read()

old, new = parse(old_files), parse(new_files)
added = sorted(set(new) - set(old))
removed = sorted(set(old) - set(new))
changed = []
for i in sorted(set(old) & set(new)):
    diffs = [k for k in ("title", "cls", "src", "text", "doc") if old[i][k] != new[i][k]]
    if diffs:
        changed.append((i, diffs))

print(f"compared with {REV}: {len(old)} requirements before, {len(new)} now")
print(f"added ({len(added)}): {', '.join(added) if added else '—'}")
print(f"removed ({len(removed)}): {', '.join(removed) if removed else '—'}")
print(f"changed ({len(changed)}):" + ("" if changed else " —"))
for i, diffs in changed:
    print(f"  {i}: {', '.join(diffs)}")
    for k in diffs:
        print(f"    - {k} before: {old[i][k]}")
        print(f"    + {k} now:    {new[i][k]}")
if STRICT and (removed or changed):
    sys.exit(1)
