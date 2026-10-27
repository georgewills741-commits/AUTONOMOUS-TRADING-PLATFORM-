"""Generate and check the documentation indexes.

Reads the specifications under docs/ and the requirement markers of the code, the tests, and
the documents (markers.py), and (re)writes:
  - docs/requirements/registry.md                 (fully generated)
  - docs/traceability/handoff-coverage.md         (generated; the hand-written tail from "## §100 questions" is kept)
  - docs/traceability/part-2-reconciliation.md    (the "New requirements" column is generated; every
  - docs/traceability/part-3-reconciliation.md     other column and section is hand-written and kept)
  - docs/traceability/verification-matrix.md      (fully generated)
and checks cross-references, links, handoff coverage, the System Rules Register, the markers,
that every requirement of the Stage 1 plan's section 3.1 has an implementation and a test or
check, that the preserved verbatim texts are unchanged, and that no document is orphaned.
With --check-only it writes nothing and also fails if any generated file is out of date.
See tools/docs/README.md, DEC-025, DEC-031, and DEC-033.

Requirements: ARCH-032 (the consistency checker), ARCH-030 (the registry's fields), ARCH-031
and ARCH-040 (the verification matrix: requirement, rule, system, interface, implementation,
test, verification), ARCH-013 (each feature's chain from its owner to the test that verifies
it), ARCH-029 and GOV-017 (a marker naming a requirement that is not approved is refused).

Usage: python3 tools/docs/build_index.py [--check-only]
Standard library only.
"""

import collections
import hashlib
import os
import re
import sys
from typing import Any

from code_blocks import code_lines  # the rule both tools use for code blocks
from markers import (  # the requirement markers of the verification matrix
    ID,
    comment_text,
    html_comments,
    keyword_markers,
    module_docstring,
    pytest_markers,
    top_level_ids,
)

ROOT = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
)
CHECK_ONLY = "--check-only" in sys.argv
DOCS = os.path.join(ROOT, "docs")
EXCLUDE_DIRS = {os.path.join(DOCS, "builder"), os.path.join(DOCS, "handoffs")}
REGISTRY = os.path.join(DOCS, "requirements", "registry.md")
COVERAGE1 = os.path.join(DOCS, "traceability", "handoff-coverage.md")
RECON2 = os.path.join(DOCS, "traceability", "part-2-reconciliation.md")
RECON3 = os.path.join(DOCS, "traceability", "part-3-reconciliation.md")
RULES = os.path.join(DOCS, "requirements", "system-rules-register.md")
PRESERVED = os.path.join(ROOT, "tools", "docs", "preserved-texts.sha256")
MATRIX = os.path.join(DOCS, "traceability", "verification-matrix.md")
PLAN1 = os.path.join(DOCS, "roadmap", "stage-01-foundation-plan.md")
STAGE1 = os.path.join(DOCS, "traceability", "stage-01-foundation.md")
GENERATED = {REGISTRY, COVERAGE1, MATRIX}
STATIC1_HEADING = "## §100 questions"

CLASSES = [
    "CONFIRMED REQUIREMENT",
    "CONFIRMED ARCHITECTURAL PRINCIPLE",
    "CONSTRAINT",
    "SYSTEM REQUIREMENT",
    "PROPOSED",
    "FUTURE",
    "PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION",
    "DEPRECATED / REPLACED",
    "IMPLEMENTATION CHOICE",
]
NOT_APPROVED = {
    "PROPOSED": "Not approved (proposal)",
    "FUTURE": "Not approved (future)",
    "PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION": "Awaiting owner confirmation",
    "DEPRECATED / REPLACED": "Withdrawn (replaced)",
}
LINE_RE = re.compile(
    r"^- \*\*(?P<id>[A-Z]{2,4}-\d{3})\*\* (?P<title>[^·]+?) · (?P<cls>[A-Z /]+?) · "
    r"(?P<src>(?:P[23])?§[0-9§P,–\- ]+?|DEC-\d{3}) — (?P<text>.+)$"
)

# prefix -> (owner, stage)
OWNERS = collections.OrderedDict(
    [
        ("PLT", ("Platform (product level)", "— (platform-wide)")),
        (
            "MODE",
            ("Operating modes (Policy System, POL-008)", "CORE TRADING FOUNDATION"),
        ),
        ("ARCH", ("Platform architecture (cross-cutting)", "FOUNDATION")),
        ("TEC", ("Technology stack", "FOUNDATION")),
        ("RMP", ("Roadmap", "FOUNDATION")),
        ("EXA", ("SYS-01 Exchange Adapter Layer", "DATA FOUNDATION")),
        ("MKD", ("SYS-02 Market-Data Infrastructure", "DATA FOUNDATION")),
        ("QNT", ("SYS-03 Quantitative Engine", "DATA FOUNDATION")),
        ("RGM", ("SYS-04 Market Regime Engine", "DATA FOUNDATION")),
        (
            "OPP",
            (
                "SYS-05 Opportunity Detection Engine",
                "DATA FOUNDATION (Opportunity Database: CORE TRADING FOUNDATION)",
            ),
        ),
        (
            "TNP",
            (
                "SYS-06 True Net-Profit Engine",
                "CORE TRADING FOUNDATION (+ ARBITRAGE cost components)",
            ),
        ),
        ("CAP", ("SYS-07 Global Capital Authority", "CORE TRADING FOUNDATION")),
        ("PRT", ("SYS-08 Portfolio Management", "CORE TRADING FOUNDATION")),
        ("RSK", ("SYS-09 Risk Engine", "CORE TRADING FOUNDATION")),
        ("EXE", ("SYS-10 Execution Engine", "CORE TRADING FOUNDATION")),
        (
            "REC",
            (
                "SYS-11 Recovery and Reconciliation",
                "CORE TRADING FOUNDATION / OPERATIONALIZATION",
            ),
        ),
        ("POL", ("SYS-12 Policy System", "CORE TRADING FOUNDATION")),
        ("NLP", ("SYS-13 Natural Language Policy Interface", "AI INTELLIGENCE")),
        ("STR", ("SYS-14 Strategy Management", "DIRECTIONAL TRADING")),
        ("BKT", ("SYS-15 Backtesting", "DIRECTIONAL TRADING")),
        ("PAP", ("SYS-16 Paper Trading", "DIRECTIONAL TRADING")),
        ("DIR", ("SYS-17 Directional Trading System", "DIRECTIONAL TRADING")),
        ("XAR", ("SYS-18 Cross-Exchange Arbitrage System", "ARBITRAGE")),
        ("TAR", ("SYS-19 Triangular Arbitrage System", "ARBITRAGE")),
        ("ARB", ("SYS-20 Arbitrage Intelligence", "ARBITRAGE")),
        (
            "PFC",
            (
                "SYS-21 Performance Controller",
                "DIRECTIONAL TRADING (core); ARBITRAGE (arbitrage tracking)",
            ),
        ),
        ("AIL", ("SYS-22 AI Intelligence Layer", "AI INTELLIGENCE")),
        (
            "AIV",
            ("SYS-22 AI Intelligence Layer (output validation)", "AI INTELLIGENCE"),
        ),
        ("AGT", ("SYS-23 AI Agents", "AI INTELLIGENCE")),
        ("RTR", ("SYS-24 Model Router", "AI INTELLIGENCE")),
        ("COST", ("SYS-25 AI Cost Manager", "AI INTELLIGENCE")),
        ("MEV", ("SYS-26 Model Evaluation", "AI INTELLIGENCE")),
        ("MEM", ("SYS-27 AI Memory / Project Knowledge", "AI INTELLIGENCE")),
        ("MON", ("SYS-28 Monitoring and Observability", "OPERATIONALIZATION")),
        (
            "DSI",
            (
                "SYS-28 Monitoring and Observability (Daily System Intelligence)",
                "OPERATIONALIZATION",
            ),
        ),
        (
            "INC",
            (
                "SYS-28 Monitoring and Observability (Incident Management)",
                "OPERATIONALIZATION",
            ),
        ),
        (
            "HLT",
            ("SYS-29 System Health", "CORE TRADING FOUNDATION / OPERATIONALIZATION"),
        ),
        (
            "AUD",
            (
                "SYS-30 Auditability / Event and Decision History",
                "CORE TRADING FOUNDATION",
            ),
        ),
        ("SEC", ("SYS-31 Security Architecture", "FOUNDATION")),
        ("CUS", ("SYS-32 Platform Account / Custody", "None (FUTURE)")),
        ("LED", ("SYS-33 Trading Ledger", "CORE TRADING FOUNDATION")),
        ("RDY", ("SYS-34 Readiness System", "DIRECTIONAL TRADING")),
        ("PERF", ("Performance (cross-cutting)", "OPERATIONALIZATION")),
        ("OPS", ("Deployment and operational readiness", "OPERATIONALIZATION")),
        (
            "MIG",
            (
                "Hosting, backup, and migration (cross-cutting)",
                "OPERATIONALIZATION (MIG-004, MIG-010 from FOUNDATION)",
            ),
        ),
        (
            "VER",
            (
                "Verification (cross-cutting)",
                "OPERATIONALIZATION (production hardening)",
            ),
        ),
        (
            "GOV",
            (
                "Architecture governance (cross-cutting)",
                "FOUNDATION (applies to every stage)",
            ),
        ),
    ]
)

# Part 1 sections whose content is process/meta rather than requirement lines.
META1 = {
    0: "Builder instructions for this handoff. Applied as process: [project state](../project-state.md), "
    "[DEC-002](../decisions/DEC-002-documentation-structure.md), [DEC-003](../decisions/DEC-003-requirement-ids-and-classification.md), "
    "[DEC-005](../decisions/DEC-005-record-findings-without-resolving.md), [requirements README](../requirements/README.md)",
    99: "Repository organization target. Applied in [DEC-002](../decisions/DEC-002-documentation-structure.md) (with deviations recorded; CF-07)",
    100: 'Completion gate. Answered in the "§100 questions" table below',
    101: "Implementation gate. Recorded in [project state](../project-state.md) and the [roadmap](../roadmap/roadmap.md)",
    102: 'Expected coverage. Checked in the "§102 topics" table below',
    103: "Completion condition. Checked in the [Part 1 verification record](part-1-verification.md)",
}
EXTRA_DOCS1 = {
    94: ["architecture/dependency-map.md"],
    95: ["roadmap/roadmap.md"],
    96: ["requirements/README.md"],
    97: ["conflicts/register.md"],
    98: ["architecture/source-of-truth-map.md"],
    92: ["architecture/system-registry.md"],
    93: ["architecture/system-registry.md"],
}

errors = []


def md_files():
    for dp, dn, fn in os.walk(DOCS):
        if any(dp == e or dp.startswith(e + os.sep) for e in EXCLUDE_DIRS):
            continue
        for f in sorted(fn):
            if f.endswith(".md"):
                yield os.path.join(dp, f)


def parse_src(src):
    """Return a set of (part, section) tuples; empty for decision sources."""
    if src.startswith("DEC-"):
        return set()
    out = set()
    for part in src.split(","):
        part = part.strip()
        m = re.match(r"^P([23])§", part)
        which = int(m.group(1)) if m else 1
        body = re.sub(r"^P[23]§", "", part).replace("§", "")
        m = re.match(r"^(\d+)\s*[–-]\s*(\d+)$", body)
        nums: list[int]
        if m:
            nums = list(range(int(m.group(1)), int(m.group(2)) + 1))
        elif body.isdigit():
            nums = [int(body)]
        else:
            errors.append(f"bad source {src!r}")
            nums = []
        for n in nums:
            out.add((which, n))
    return out


def strip_code(text):
    lines = text.split("\n")
    flags, _ = code_lines(lines)
    return "\n".join(line for line, code in zip(lines, flags) if not code)


# ---------- collect requirements ----------
reqs: "collections.OrderedDict[str, dict[str, Any]]" = collections.OrderedDict()
for path in md_files():
    if path in GENERATED:
        continue
    rel = os.path.relpath(path, DOCS)
    last = None  # requirement whose indented continuation lines (e.g. RSK-015's levels) belong to its text
    lines = open(path, encoding="utf-8").read().splitlines()
    for n, (line, in_code) in enumerate(zip(lines, code_lines(lines)[0]), 1):
        if in_code:
            last = None
            continue
        if last and line.startswith("  ") and line.strip():
            reqs[last]["text"] += " " + line.strip()
            continue
        last = None
        if re.match(r"^- \*\*[A-Z]{2,4}-\d{3}\*\*", line):
            m = LINE_RE.match(line)
            if not m:
                errors.append(f"{rel}:{n}: malformed requirement line")
                continue
            d: dict[str, Any] = dict(m.groupdict())
            if d["id"] in reqs:
                errors.append(
                    f"duplicate ID {d['id']} in {rel} and {reqs[d['id']]['doc']}"
                )
            if d["cls"] not in CLASSES:
                errors.append(f"{d['id']}: unknown class {d['cls']!r}")
            if d["id"].split("-")[0] not in OWNERS:
                errors.append(f"{d['id']}: unknown prefix")
            d["doc"] = rel
            d["secs"] = parse_src(d["src"])
            reqs[d["id"]] = d
            last = d["id"]

order = {p: i for i, p in enumerate(OWNERS)}
ids = sorted(reqs, key=lambda i: (order.get(i.split("-")[0], 99), int(i.split("-")[1])))
byp = collections.defaultdict(list)
for i in ids:
    byp[i.split("-")[0]].append(int(i.split("-")[1]))
for p, nums in byp.items():
    if nums != list(range(1, len(nums) + 1)):
        errors.append(f"prefix {p} not sequential: {nums}")


# ---------- handoff section titles ----------
def titles_of(path, pat):
    txt = open(path, encoding="utf-8").read()
    return {int(m.group(1)): m.group(2) for m in re.finditer(pat, txt, re.M)}


titles1 = titles_of(
    os.path.join(DOCS, "handoffs", "part-1-core-platform-features.md"),
    r"^## (\d{2,3}) — (.+)$",
)
titles2 = titles_of(
    os.path.join(DOCS, "handoffs", "part-2-consolidated-additional-systems.md"),
    r"^## (\d{1,3}) — (.+)$",
)
if sorted(titles2) != list(range(1, 351)):
    errors.append("Part 2 historical copy does not have sections 1..350")
titles3 = titles_of(
    os.path.join(DOCS, "handoffs", "part-3-consolidated-autonomy-capital-scaling.md"),
    r"^## (\d{3}) — (.+)$",
)
if sorted(titles3) != list(range(351, 551)):
    errors.append("Part 3 historical copy does not have sections 351..550")
TITLES = {1: titles1, 2: titles2, 3: titles3}
PREFIX = {1: "§", 2: "P2§", 3: "P3§"}

sec_ids: dict[int, "collections.defaultdict[int, list[str]]"] = {
    1: collections.defaultdict(list),
    2: collections.defaultdict(list),
    3: collections.defaultdict(list),
}
for i in ids:
    for part, s in reqs[i]["secs"]:
        sec_ids[part][s].append(i)
        if s not in TITLES[part]:
            errors.append(f"{i}: source {PREFIX[part]}{s} does not exist")
for s in sorted(titles1):
    if not sec_ids[1].get(s) and s not in META1:
        errors.append(f"§{s:02d} has no requirement and no meta mapping")

# ---------- decisions ----------
decs = {
    m.group(1)
    for f in os.listdir(os.path.join(DOCS, "decisions"))
    for m in [re.match(r"^(DEC-\d{3})-", f)]
    if m
}
decided_by = {}
for m in re.finditer(
    r"^\| \[(DEC-\d{3})\]\([^)]+\) \| [^|]+ \| ([^|]+) \|",
    open(os.path.join(DOCS, "decisions", "README.md"), encoding="utf-8").read(),
    re.M,
):
    decided_by[m.group(1)] = m.group(2).strip()
for dec in sorted(decs):
    if dec not in decided_by:
        errors.append(f"{dec} missing from decisions/README.md")


def approval(r):
    if r["cls"] in NOT_APPROVED:
        return NOT_APPROVED[r["cls"]]
    if r["src"].startswith("DEC-"):
        who = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", decided_by.get(r["src"], "?"))
        return f"Decided by: {who}"
    part = {"P2": "Handoff Part 2", "P3": "Handoff Part 3"}.get(
        r["src"][:2], "Handoff Part 1"
    )
    return part + " — reviewed (DEC-036)"


# ---------- Part 2 and Part 3 reconciliations: read the hand-written columns ----------
ROW_RE = re.compile(
    r"^\| (?P<key>\d{1,3}|—) \| (?P<title>[^|]+) \| (?P<new>[^|]*) \| (?P<notes>[^|]*) \|$"
)
recon_texts = {}
for part, path, name in (
    (2, RECON2, "part-2-reconciliation"),
    (3, RECON3, "part-3-reconciliation"),
):
    recon_rows = collections.OrderedDict()
    recon_text = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    recon_texts[part] = recon_text
    if not recon_text:
        errors.append(f"{name}.md is missing")
        continue
    for line in recon_text.splitlines():
        m = ROW_RE.match(line)
        if m:
            recon_rows[m.group("key")] = m.groupdict()
    for s in sorted(TITLES[part]):
        row = recon_rows.get(str(s))
        if not row:
            errors.append(f"{name}: no row for {PREFIX[part]}{s}")
            continue
        if not sec_ids[part].get(s) and row["notes"].strip() in ("", "—"):
            errors.append(f"{PREFIX[part]}{s}: no new requirement and no disposition")
        if row["title"].strip() != TITLES[part][s]:
            errors.append(f"{PREFIX[part]}{s}: title mismatch in reconciliation")

# ---------- cross-reference checks ----------
defined_findings = set()
for reg in ("conflicts/register.md", "open-questions/register.md"):
    txt = open(os.path.join(DOCS, reg), encoding="utf-8").read()
    defined_findings |= set(re.findall(r"^### (CF-\d{2}) ", txt, re.M))
    defined_findings |= set(re.findall(r"^\| ((?:DUP|OQ|TC)-\d{2}) \|", txt, re.M))
sysreg = open(
    os.path.join(DOCS, "architecture", "system-registry.md"), encoding="utf-8"
).read()
defined_sys = set(re.findall(r"^\| (SYS-\d{2}) \|", sysreg, re.M))

# ---------- System Rules Register (ARCH-038) ----------
RULE_RE = re.compile(
    r"^\| (SR-\d{2}) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| "
    r"([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$"
)
defined_rules = []
rules_of: "collections.defaultdict[str, list[str]]" = collections.defaultdict(list)
rules_text = open(RULES, encoding="utf-8").read() if os.path.exists(RULES) else ""
if not rules_text:
    errors.append("system-rules-register.md is missing")
for line in rules_text.splitlines():
    if line.startswith("| SR-"):
        m = RULE_RE.match(line)
        if not m:
            errors.append(f"system-rules-register: malformed row {line[:40]!r}")
            continue
        rid, canon, cls = m.group(1), m.group(3), m.group(4).strip()
        defined_rules.append(rid)
        canon_ids = re.findall(r"\b[A-Z]{2,4}-\d{3}\b", canon)
        for i in canon_ids:
            rules_of[i].append(rid)
        if not canon_ids:
            errors.append(f"{rid}: no canonical requirement")
        elif canon_ids[0] in reqs and reqs[canon_ids[0]]["cls"] != cls:
            errors.append(
                f"{rid}: classification {cls!r} is not the class of {canon_ids[0]} ({reqs[canon_ids[0]]['cls']})"
            )
        for i in canon_ids:
            if i in reqs and reqs[i]["cls"] in NOT_APPROVED:
                errors.append(
                    f"{rid}: canonical requirement {i} is not approved ({reqs[i]['cls']})"
                )
if defined_rules != [f"SR-{n:02d}" for n in range(1, len(defined_rules) + 1)]:
    errors.append(
        f"system-rules-register: SR IDs not unique and sequential: {defined_rules}"
    )

refs: "collections.Counter[str]" = collections.Counter()
for path in md_files():
    rel = os.path.relpath(path, DOCS)
    raw = open(path, encoding="utf-8").read()
    if code_lines(raw.split("\n"))[1]:
        errors.append(f"{rel}: code fence opened and never closed")
    txt = strip_code(raw)
    for tok in re.findall(r"\b((?:CF|DUP|OQ|TC)-\d{2})\b", txt):
        refs[tok] += 1
        if tok not in defined_findings:
            errors.append(f"{rel}: reference to undefined finding {tok}")
    for tok in re.findall(r"\b(DEC-\d{3})\b", txt):
        if tok not in decs:
            errors.append(f"{rel}: reference to undefined decision {tok}")
    for tok in re.findall(r"\b(SYS-\d{2})\b", txt):
        if tok not in defined_sys:
            errors.append(f"{rel}: reference to undefined system {tok}")
    for tok in re.findall(r"\b(SR-\d{2})\b", txt):
        if tok not in defined_rules:
            errors.append(f"{rel}: reference to undefined system rule {tok}")
    for tok in re.findall(r"\b([A-Z]{2,4}-\d{3})\b", txt):
        if not tok.startswith("DEC-") and tok not in reqs:
            errors.append(f"{rel}: reference to undefined requirement {tok}")
    for link in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", txt):
        if re.match(r"^[a-z]+://", link):
            continue
        if not os.path.exists(
            os.path.normpath(os.path.join(os.path.dirname(path), link))
        ):
            errors.append(f"{rel}: broken link {link}")
for link in re.findall(r"\]\(\.\./([^)]+)\)", sysreg):
    if not os.path.exists(os.path.join(DOCS, link.split("#")[0])):
        errors.append(f"system-registry link missing: {link}")
for i in ids:
    if reqs[i]["src"].startswith("DEC-") and reqs[i]["src"] not in decs:
        errors.append(f"{i}: source {reqs[i]['src']} is not a decision record")


# ---------- requirement markers (U7: the verification matrix; tools/docs/README.md) ----------
SKIP_DIRS = {
    "__pycache__",
    ".hypothesis",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
}


def files_under(rel):
    """The files under a directory of the repository, or the file itself, in a stable order."""
    base = os.path.join(ROOT, rel)
    if os.path.isfile(base):
        yield base
        return
    for dp, dn, fn in os.walk(base):
        dn[:] = sorted(d for d in dn if d not in SKIP_DIRS)
        for f in sorted(fn):
            yield os.path.join(dp, f)


def repo_rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


# requirement -> the artifacts that implement it, the checks that are not pytest tests, and
# the tests (test file -> test functions) that verify it
implemented: "collections.defaultdict[str, list[str]]" = collections.defaultdict(list)
checked_by: "collections.defaultdict[str, list[str]]" = collections.defaultdict(list)
tested: "collections.defaultdict[str, dict[str, list[str]]]" = collections.defaultdict(
    dict
)
test_counts: "collections.OrderedDict[str, tuple[int, int]]" = collections.OrderedDict()


def marked_ids(where, keyword, found):
    """The marker's IDs that name an approved requirement; the others are errors."""
    if not found:
        errors.append(f"{where}: a {keyword} marker names no requirement")
    ok = []
    for i in found:
        if i not in reqs:
            errors.append(f"{where}: marker names unknown requirement {i}")
        elif reqs[i]["cls"] in NOT_APPROVED:
            errors.append(
                f"{where}: marker names {i}, which is not approved ({reqs[i]['cls']}; ARCH-029, GOV-017)"
            )
        else:
            ok.append(i)
    return ok


def collect(rel, text):
    for keyword, into in (("Requirements", implemented), ("Verifies", checked_by)):
        for _line, found in keyword_markers(text, keyword):
            for i in marked_ids(rel, keyword, found):
                if rel not in into[i]:
                    into[i].append(rel)


for root in ("src", "tools"):
    for path in files_under(root):
        if path.endswith(".py"):
            doc = module_docstring(open(path, encoding="utf-8").read())
            if doc:
                collect(repo_rel(path), doc)
for root in ("pyproject.toml", os.path.join(".github", "workflows")):
    for path in files_under(root):
        if path.endswith((".toml", ".yml", ".yaml")):
            collect(repo_rel(path), comment_text(open(path, encoding="utf-8").read()))
for path in md_files():
    if path not in GENERATED:
        collect(
            repo_rel(path),
            html_comments(strip_code(open(path, encoding="utf-8").read())),
        )
for path in files_under("tests"):
    if not path.endswith(".py"):
        continue
    rel = repo_rel(path)
    found, problems, test_names = pytest_markers(open(path, encoding="utf-8").read())
    for problem_line, problem in problems:
        errors.append(f"{rel}:{problem_line}: {problem}")
    marked = set()
    for marker_line, test, test_ids in found:
        marked.add(test)
        for i in marked_ids(f"{rel}:{marker_line}", "req", test_ids):
            names = tested[i].setdefault(rel, [])
            if test not in names:
                names.append(test)
    if test_names:
        test_counts[rel] = (len(test_names), len(marked))

# The interfaces: each committed contract, by the package of the platform that defines it.
contract_package: "dict[str, str]" = {}
if os.path.isdir(os.path.join(ROOT, "contracts")):
    sources = {
        repo_rel(p): open(p, encoding="utf-8").read()
        for p in files_under("src")
        if p.endswith(".py")
    }
    for cid in sorted(os.listdir(os.path.join(ROOT, "contracts"))):
        for rel, text in sources.items():
            if f'contract_id = "{cid}"' in text or f'("{cid}",' in text:
                contract_package[cid] = rel.rsplit("/", 1)[0]


def section_text(text, heading_re):
    """The text under the first heading matching heading_re, up to the next heading."""
    m = re.search(heading_re, text, re.M)
    if not m:
        return ""
    rest = text[m.end() :]
    n = re.search(r"^#{1,3} ", rest, re.M)
    return rest[: n.start()] if n else rest


def table_rows(text):
    """The cells of each row of the first table in text, without its header and separator."""
    rows = []
    for line in text.split("\n"):
        if line.startswith("|") and not re.match(r"^\|[\s:|-]+\|$", line):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows[1:]


# The Stage 1 plan's section 3: what Stage 1 delivers (3.1, with the unit of each), starts (3.2),
# applies as design rules (3.3), leaves to later stages (3.4), and does not build (3.5).
plan_text = open(PLAN1, encoding="utf-8").read() if os.path.exists(PLAN1) else ""
if not plan_text:
    errors.append("roadmap/stage-01-foundation-plan.md is missing")
scope: "collections.OrderedDict[str, tuple[str, Any]]" = collections.OrderedDict()
delivers: "dict[str, str]" = {}  # what Stage 1 delivers of each, with its row's note if any
for cells in table_rows(section_text(plan_text, r"^### 3\.1 ")):
    for i in top_level_ids(cells[0]):
        scope[i] = ("3.1", re.findall(r"\bU\d\b", cells[-1]))
        note = " — the plan's row: " + cells[0] if "(" in cells[0] else ""
        delivers[i] = cells[1] + note
for cells in table_rows(section_text(plan_text, r"^### 3\.2 ")):
    for i in top_level_ids(cells[0]):
        scope.setdefault(i, ("3.2", "started in Stage 1; completed in " + cells[-1]))
DESIGN_RULE = "applied as a design rule to Stage 1's own work, verified in Gate 2"
s33 = section_text(plan_text, r"^### 3\.3 ")
for a, b in re.findall(rf"\b({ID}) to ({ID})\b", s33):
    if a.split("-")[0] == b.split("-")[0]:
        for n in range(int(a.split("-")[1]), int(b.split("-")[1]) + 1):
            scope.setdefault(f"{a.split('-')[0]}-{n:03d}", ("3.3", DESIGN_RULE))
for i in top_level_ids(s33):
    scope.setdefault(i, ("3.3", DESIGN_RULE))
for cells in table_rows(section_text(plan_text, r"^### 3\.4 ")):
    for i in top_level_ids(cells[0]):
        scope.setdefault(i, ("3.4", "applied in a later stage: " + cells[-1]))
for i in top_level_ids(section_text(plan_text, r"^### 3\.5 ")):
    scope.setdefault(i, ("3.5", "not built"))
delivered = [i for i, (sec, _d) in scope.items() if sec == "3.1"]
if plan_text and not delivered:
    errors.append(
        "roadmap/stage-01-foundation-plan.md: section 3.1 lists no requirement"
    )

# The stage record's checkpoints: the units each built, whether it is done, and its record.
stage_text = open(STAGE1, encoding="utf-8").read() if os.path.exists(STAGE1) else ""
unit_checkpoint: "dict[str, tuple[str, bool, str | None]]" = {}
for cells in table_rows(section_text(stage_text, r"^## Checkpoints\s*$")):
    if len(cells) >= 4:
        record = re.search(r"\]\(([^)]+)\)", cells[3])
        for u in re.findall(r"\bU\d\b", cells[1]):
            unit_checkpoint[u] = (
                cells[0],
                cells[2].startswith("Done"),
                record.group(1) if record else None,
            )

# U7's acceptance as a check: every requirement Stage 1 delivers is implemented and tested.
for i in delivered:
    if not implemented.get(i):
        errors.append(
            f"verification matrix: {i} (Stage 1 plan, section 3.1) has no implementation marker"
        )
    if not tested.get(i) and not checked_by.get(i):
        errors.append(
            f"verification matrix: {i} (Stage 1 plan, section 3.1) has no test or check marker"
        )
    for u in scope[i][1]:
        if u not in unit_checkpoint:
            errors.append(
                f"verification matrix: unit {u} of {i} is in no checkpoint of the stage record"
            )


# ---------- preserved verbatim texts (docs/handoffs/, docs/builder/) ----------
def preserved_paths() -> list[str]:
    """Every file under docs/handoffs/ and docs/builder/, in subdirectories too, of any type."""
    out = []
    for d in sorted(EXCLUDE_DIRS):
        for dp, dn, fn in os.walk(d):
            dn.sort()
            out += [os.path.join(dp, f) for f in sorted(fn)]
    return out


def split_preserved(path: str) -> tuple[list[str], list[str]]:
    """(banner, body) of a preserved Markdown text, read without newline translation.
    The banner is the first block of '>' lines after the title (only blank lines may come
    between). The body is the title line plus everything after that block, blank lines and
    any later '>' line included. A banner may change by decision; the body changes only by a
    recorded restoration of the words as received (DEC-047, decision 8)."""
    lines = open(path, encoding="utf-8", newline="").read().split("\n")
    i = 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    j = i
    while j < len(lines) and lines[j].startswith(">"):
        j += 1
    return lines[i:j], [lines[0]] + lines[j:]


expected: dict[str, str] = {}
if os.path.exists(PRESERVED):
    for n, line in enumerate(open(PRESERVED, encoding="utf-8").read().splitlines(), 1):
        if not line or line.startswith("#"):
            continue
        pm = re.match(r"^([0-9a-f]{64})  (docs/(?:handoffs|builder)/\S+)$", line)
        if not pm:
            errors.append(f"preserved-texts.sha256:{n}: malformed line")
            continue
        expected[pm.group(2)] = pm.group(1)
else:
    errors.append("tools/docs/preserved-texts.sha256 is missing")
preserved_md = []
for path in preserved_paths():
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    if path.endswith(".md"):
        preserved_md.append(path)
        banner, body = split_preserved(path)
        digest = hashlib.sha256("\n".join(body).encode("utf-8")).hexdigest()
        if "\r" in "\n".join(body):
            errors.append(f"{rel}: preserved text has CR line endings")
        for link in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", "\n".join(banner)):
            if not re.match(r"^[a-z]+://", link) and not os.path.exists(
                os.path.normpath(os.path.join(os.path.dirname(path), link))
            ):
                errors.append(f"{rel}: broken link in status banner {link}")
    else:
        digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
    if rel not in expected:
        errors.append(
            f"{rel}: preserved text not listed in tools/docs/preserved-texts.sha256 (hash {digest})"
        )
    elif expected[rel] != digest:
        errors.append(
            f"{rel}: preserved text changed (hash now {digest}); a verbatim text changes only "
            "by a recorded restoration, with its manifest line"
        )
for rel in sorted(expected):
    if not os.path.exists(os.path.join(ROOT, rel)):
        errors.append(f"preserved-texts.sha256: {rel} does not exist")


# ---------- orphaned documents (master execution constitution §71, §73) ----------
def doc_links(path: str) -> list[str]:
    """Targets of the relative links in a Markdown file, outside code blocks and inline code."""
    text = re.sub(r"`[^`\n]*`", "", strip_code(open(path, encoding="utf-8").read()))
    out = []
    for link in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
        if not re.match(r"^[a-z]+://", link):
            out.append(os.path.normpath(os.path.join(os.path.dirname(path), link)))
    return out


# Every document must be reachable by links from the entry points, not merely linked from
# some other document (two documents linking only to each other are still orphaned).
roots = [
    os.path.join(ROOT, x)
    for x in ("README.md", "CLAUDE.md", "docs/README.md", "tools/docs/README.md")
]
reached = set()
todo = [os.path.normpath(r) for r in roots if os.path.exists(r)]
while todo:
    cur = todo.pop()
    if cur in reached:
        continue
    reached.add(cur)
    if cur.endswith(".md") and os.path.isfile(cur):
        todo += [t for t in doc_links(cur) if t not in reached and os.path.isfile(t)]
for path in list(md_files()) + preserved_md:
    if os.path.normpath(path) not in reached:
        errors.append(
            f"{os.path.relpath(path, DOCS)}: not reachable by links from README.md, CLAUDE.md, "
            "docs/README.md, or tools/docs/README.md (orphaned)"
        )

if errors:
    print("ERRORS:")
    for e in errors:
        print("  " + e)
    sys.exit(1)

cls_count = collections.Counter(reqs[i]["cls"] for i in ids)
n_p1 = sum(1 for i in ids if reqs[i]["src"].startswith("§"))
n_p2 = sum(1 for i in ids if reqs[i]["src"].startswith("P2"))
n_p3 = sum(1 for i in ids if reqs[i]["src"].startswith("P3"))
dec_ids = collections.defaultdict(list)
for i in ids:
    if reqs[i]["src"].startswith("DEC-"):
        dec_ids[reqs[i]["src"]].append(i)
n_dec = sum(map(len, dec_ids.values()))
print(
    f"requirements: {len(ids)} (Part 1: {n_p1}, Part 2: {n_p2}, Part 3: {n_p3}, decisions: {n_dec}); prefixes: {len(byp)}; "
    f"findings: {len(defined_findings)}; decisions: {len(decs)}; systems: {len(defined_sys)}; system rules: {len(defined_rules)}"
)
print("by class:", dict(cls_count))
print(
    "findings never referenced outside their register:",
    sorted(defined_findings - set(refs)),
)
print(
    f"Part 2 sections with new requirements: {len([s for s in titles2 if sec_ids[2].get(s)])} of 350"
)
print(
    f"Part 3 sections with new requirements: {len([s for s in titles3 if sec_ids[3].get(s)])} of 200"
)
OUT = collections.OrderedDict()  # path -> generated content

# ---------- registry.md ----------
L = [
    "# Requirements Registry",
    "",
    "> **Index only.** Requirement text lives in the linked specification (DEC-003). This file is generated by "
    "[`tools/docs/build_index.py`](../../tools/docs/README.md) from the specifications; do not edit it by hand. "
    "Conventions: [README](README.md).",
    ">",
    f"> **Sources:** Handoff Part 1 ({n_p1}), Handoff Part 2 ({n_p2}), Handoff Part 3 ({n_p3}), decision records ({n_dec}) · "
    f"**Status of every entry:** DOCUMENTED — not implemented, not verified · **Total:** {len(ids)} requirements",
    "",
    "## Summary by class",
    "",
    "| Class | Count |",
    "|---|---|",
]
for c in CLASSES:
    if cls_count.get(c):
        L.append(f"| {c} | {cls_count[c]} |")
L += [
    "",
    "FUTURE entries are recorded but not built. Each DEPRECATED / REPLACED entry names its replacement in its "
    "specification. LED-001 stays conditional on a user-facing platform, which the platform currently is not (DEC-006). "
    "Conflicts and open questions that affect requirements are in the [findings register](../conflicts/register.md) and the "
    "[open-question register](../open-questions/register.md). Concrete values used by requirements are classified in the "
    "[values register](values-register.md). Enforceable behavioral rules are indexed in the "
    "[System Rules Register](system-rules-register.md).",
    "",
    "**Approval** says where the requirement's authority comes from: a handoff section, reviewed in the complete documentation "
    "review before implementation (handoff §101), which the owner accepted ([DEC-036](../decisions/DEC-036-owner-decisions-audit-findings.md)); "
    "or a decision record and who decided it. PROPOSED, FUTURE, and "
    "REQUIRES CONFIRMATION entries are not approved (ARCH-029). **Dependencies** are recorded between systems in the "
    "[dependency map](../architecture/dependency-map.md); **verification methods** are assigned when each stage is planned (ARCH-030). "
    "**Default stage** is the owning system's stage; where the [roadmap](../roadmap/roadmap.md) places an individual "
    'requirement in another stage (its "additions by stage" tables), the roadmap is authoritative.',
    "",
    "## Registry",
    "",
    "| ID | Title | Class | Source | Owner | Specification | Default stage | Approval |",
    "|---|---|---|---|---|---|---|---|",
]
for i in ids:
    r = reqs[i]
    owner, stage = OWNERS[i.split("-")[0]]
    L.append(
        f"| {i} | {r['title'].strip()} | {r['cls']} | {r['src'].strip()} | {owner} | "
        f"[{r['doc']}](../{r['doc']}) | {stage} | {approval(r)} |"
    )
OUT[REGISTRY] = "\n".join(L) + "\n"

# ---------- handoff-coverage.md (Part 1) ----------
old = open(COVERAGE1, encoding="utf-8").read()
static = old[old.index(STATIC1_HEADING) :].rstrip("\n")
C = [
    "# Handoff Coverage — Part 1",
    "",
    "> Where every section of [Handoff Part 1](../handoffs/part-1-core-platform-features.md) now lives. "
    "The section table and the decision table are generated by [`tools/docs/build_index.py`](../../tools/docs/README.md) "
    "from requirement sources; the §100 and §102 tables were written by hand and checked. A section with no requirement IDs "
    "is process/meta content, and its mapping is stated. Handoff Part 2 is traced in the "
    "[Part 2 reconciliation](part-2-reconciliation.md) and Handoff Part 3 in the "
    "[Part 3 reconciliation](part-3-reconciliation.md).",
    "",
    "## Section → canonical location",
    "",
    "| § | Handoff section | Canonical document(s) | Requirement IDs |",
    "|---|---|---|---|",
]
for s in sorted(titles1):
    got = sec_ids[1].get(s, [])
    docs = []
    for i in got:
        if reqs[i]["doc"] not in docs:
            docs.append(reqs[i]["doc"])
    for extra in EXTRA_DOCS1.get(s, []):
        if extra not in docs:
            docs.append(extra)
    if got or docs:
        C.append(
            f"| {s:02d} | {titles1[s]} | {'; '.join(f'[{d}](../{d})' for d in docs)} | {', '.join(got) if got else '—'} |"
        )
    else:
        C.append(f"| {s:02d} | {titles1[s]} | {META1[s]} | — |")
C += [
    "",
    "## Requirements created by decisions",
    "",
    "These did not come from a handoff section. Each cites the decision record that created it.",
    "",
    "| Decision | Requirement IDs |",
    "|---|---|",
]
for dec in sorted(dec_ids):
    f = [
        x
        for x in os.listdir(os.path.join(DOCS, "decisions"))
        if x.startswith(dec + "-")
    ][0]
    C.append(f"| [{dec}](../decisions/{f}) | {', '.join(dec_ids[dec])} |")
C += ["", static]
OUT[COVERAGE1] = "\n".join(C) + "\n"

# ---------- part-2 and part-3 reconciliations: regenerate the "New requirements" column ----------
for part, path in ((2, RECON2), (3, RECON3)):
    out = []
    for line in recon_texts[part].splitlines():
        m = ROW_RE.match(line)
        if m and m.group("key").isdigit():
            s = int(m.group("key"))
            new = ", ".join(sec_ids[part].get(s, [])) or "—"
            line = f"| {s} | {TITLES[part][s]} | {new} | {m.group('notes').strip()} |"
        out.append(line)
    OUT[path] = "\n".join(out).rstrip("\n") + "\n"


# ---------- verification-matrix.md (U7) ----------
def file_link(rel):
    return f"[`{rel}`](../../{rel})"


def tests_cell(i):
    cells = [
        file_link(f) + ": " + ", ".join(f"`{t}`" for t in names)
        for f, names in tested.get(i, {}).items()
    ]
    cells += [file_link(f) for f in checked_by.get(i, [])]
    return "; ".join(cells) or "—"


def interfaces_cell(i):
    packages = {
        f.rsplit("/", 1)[0] for f in implemented.get(i, []) if f.startswith("src/")
    }
    return (
        ", ".join(f"`{c}`" for c, pkg in contract_package.items() if pkg in packages)
        or "—"
    )


def requirement_cell(i):
    return f"[{i}](../{reqs[i]['doc']}) {reqs[i]['title'].strip()}"


M = [
    "# Verification Matrix",
    "",
    "> **Generated** by [`tools/docs/build_index.py`](../../tools/docs/README.md) from the requirement markers of the code, "
    "the tests, and the documents, the [requirements registry](../requirements/registry.md), the "
    "[System Rules Register](../requirements/system-rules-register.md), the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md)'s "
    "section 3, and the [stage record](stage-01-foundation.md)'s checkpoints; do not edit it by hand. The markers and how to "
    "write them are described in the [documentation tools](../../tools/docs/README.md). `build_index.py --check-only` fails "
    "when this file is out of date, when a marker names an unknown requirement or one that is not approved (ARCH-029, "
    "GOV-017), and when a requirement of the plan's section 3.1 has no implementation or no test or check.",
    ">",
    "> **What it connects** (master execution constitution §145; ARCH-031, ARCH-040): requirement, system rule, owning system, "
    "interface, implementation, test, verification, and status. The commit of each verification is that of its record, in "
    "the [project state](../project-state.md)'s checkpoint log: a generated file cannot hold its own commit. The links of "
    "[owner decisions 14](../handoffs/owner-decisions-14-company-grade-order-and-traceability.md)'s §31 chain are reached "
    "here and in the registry, without a second registry ([DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md), "
    "decision 4): the requirement ID (here, linked to its specification); the decision (the registry's Source and Approval "
    "columns); the owner and the system (the owning system, the registry's Owner column, repeated here); the implementation, "
    "the test, and the verification (here); the roadmap stage (the registry's Default stage, repeated here; the "
    "[roadmap](../roadmap/roadmap.md) is authoritative where it places a requirement elsewhere); and the status (here).",
    ">",
    "> **Columns.** *Interface*: the committed contracts (`contracts/`) defined by a package that implements the requirement. "
    "*Implementation*: the artifacts whose `Requirements:` marker names it. *Tests and checks*: the test functions whose "
    "`pytest.mark.req` marker names it, and the checks that are not pytest tests whose `Verifies:` marker names it. "
    "*Verification*: the checkpoint that built each unit the plan assigns to the requirement, and its verification record. "
    "*Status*: that of what Stage 1 delivers of the requirement, the second column, not of the whole requirement, which "
    "is implemented in full only when each part of it is built, in the stages that build them (the "
    '[requirements README](../requirements/README.md), "Status"): VERIFIED when it is implemented and tested and each of '
    "those checkpoints passed its three gates; otherwise "
    "IMPLEMENTED AND TESTED, with the checkpoint whose gates are pending. A marker added after a checkpoint is checked by the "
    "gates of the change that adds it, recorded in its verification record, and the whole stage again by its own gates at "
    "its exit (the stage record's X2).",
    "",
    "## Requirements delivered by Stage 1 (the plan's section 3.1)",
    "",
    "| Requirement | What Stage 1 delivers (the plan's section 3.1) | Owner (system) | Default stage | System rule | Interface "
    "| Implementation | Tests and checks | Verification | Status |",
    "|---|---|---|---|---|---|---|---|---|---|",
]
for i in delivered:
    owner, stage = OWNERS[i.split("-")[0]]
    checkpoints = []
    for u in scope[i][1]:
        cp = unit_checkpoint.get(u)
        if cp and cp not in checkpoints:
            checkpoints.append(cp)
    verification = (
        "; ".join(
            f"checkpoint {letter}" + (f" ([record]({record}))" if record else "")
            for letter, _done, record in checkpoints
        )
        or "—"
    )
    traced = bool(implemented.get(i)) and bool(tested.get(i) or checked_by.get(i))
    pending = [letter for letter, done, _record in checkpoints if not done]
    if not traced:
        status = "GAP"
    elif pending:
        status = (
            "IMPLEMENTED AND TESTED; the gates of checkpoint "
            + ", ".join(pending)
            + " pending"
        )
    else:
        status = "VERIFIED"
    M.append(
        f"| {requirement_cell(i)} | {delivers[i]} | {owner} | {stage} | {', '.join(rules_of.get(i, [])) or '—'} | "
        f"{interfaces_cell(i)} | "
        + "; ".join(file_link(f) for f in implemented.get(i, []))
        + f" | {tests_cell(i)} | {verification} | {status} |"
    )
others = [
    i
    for i in ids
    if i not in delivered and (implemented.get(i) or tested.get(i) or checked_by.get(i))
]
M += [
    "",
    "## Other requirements named by a marker",
    "",
    "Requirements that Stage 1's code, tests, or documents name, outside the plan's section 3.1: each keeps the disposition "
    "the plan's section 3 gives it, shown here.",
    "",
    "| Requirement | Owner (system) | Default stage | Stage 1 plan, section 3 | Implementation | Tests and checks |",
    "|---|---|---|---|---|---|",
]
for i in others:
    owner, stage = OWNERS[i.split("-")[0]]
    sec, detail = scope.get(i, ("", ""))
    plan_cell = f"{sec}: {detail}" if sec else "Not in the plan's section 3"
    M.append(
        f"| {requirement_cell(i)} | {owner} | {stage} | {plan_cell} | "
        + ("; ".join(file_link(f) for f in implemented.get(i, [])) or "—")
        + f" | {tests_cell(i)} |"
    )
M += [
    "",
    "## Tests and the requirements they name",
    "",
    "Every test module, with its test functions and how many of them name a requirement. A test that names none still "
    "runs at every checkpoint and on every push; a marker names the requirement a test is evidence for.",
    "",
    "| Test module | Test functions | Naming a requirement | Naming none |",
    "|---|---|---|---|",
]
for rel, (count, marked_count) in test_counts.items():
    M.append(
        f"| {file_link(rel)} | {count} | {marked_count} | {count - marked_count} |"
    )
OUT[MATRIX] = "\n".join(M) + "\n"


if CHECK_ONLY:
    stale = [
        os.path.relpath(p, ROOT)
        for p, c in OUT.items()
        if not os.path.exists(p) or open(p, encoding="utf-8").read() != c
    ]
    if stale:
        print("ERRORS:")
        for p in stale:
            print(f"  {p} is out of date: run python3 tools/docs/build_index.py")
        sys.exit(1)
    sys.exit(0)
for p, c in OUT.items():
    open(p, "w", encoding="utf-8").write(c)
print("wrote " + ", ".join(os.path.basename(p) for p in OUT))
