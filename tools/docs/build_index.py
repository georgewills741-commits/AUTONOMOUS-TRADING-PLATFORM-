"""Generate and check the documentation indexes.

Reads the specifications under docs/ and (re)writes:
  - docs/requirements/registry.md                 (fully generated)
  - docs/traceability/handoff-coverage.md         (generated; the hand-written tail from "## §100 questions" is kept)
  - docs/traceability/part-2-reconciliation.md    (the "New requirements" column is generated; every
  - docs/traceability/part-3-reconciliation.md     other column and section is hand-written and kept)
and checks cross-references, links, handoff coverage, and the System Rules Register.
With --check-only it writes nothing and also fails if any generated file is out of date.
See tools/docs/README.md, DEC-025, and DEC-031.

Usage: python3 tools/docs/build_index.py [--check-only]
Standard library only.
"""
import collections
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
CHECK_ONLY = "--check-only" in sys.argv
DOCS = os.path.join(ROOT, "docs")
EXCLUDE_DIRS = {os.path.join(DOCS, "builder"), os.path.join(DOCS, "handoffs")}
REGISTRY = os.path.join(DOCS, "requirements", "registry.md")
COVERAGE1 = os.path.join(DOCS, "traceability", "handoff-coverage.md")
RECON2 = os.path.join(DOCS, "traceability", "part-2-reconciliation.md")
RECON3 = os.path.join(DOCS, "traceability", "part-3-reconciliation.md")
RULES = os.path.join(DOCS, "requirements", "system-rules-register.md")
GENERATED = {REGISTRY, COVERAGE1}
STATIC1_HEADING = "## §100 questions"

CLASSES = ["CONFIRMED REQUIREMENT", "CONFIRMED ARCHITECTURAL PRINCIPLE", "CONSTRAINT",
           "SYSTEM REQUIREMENT", "PROPOSED", "FUTURE", "PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION",
           "DEPRECATED / REPLACED", "IMPLEMENTATION CHOICE"]
NOT_APPROVED = {"PROPOSED": "Not approved (proposal)", "FUTURE": "Not approved (future)",
                "PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION": "Awaiting owner confirmation",
                "DEPRECATED / REPLACED": "Withdrawn (replaced)"}
LINE_RE = re.compile(r"^- \*\*(?P<id>[A-Z]{2,4}-\d{3})\*\* (?P<title>[^·]+?) · (?P<cls>[A-Z /]+?) · "
                     r"(?P<src>(?:P[23])?§[0-9§P,–\- ]+?|DEC-\d{3}) — (?P<text>.+)$")

# prefix -> (owner, stage)
OWNERS = collections.OrderedDict([
    ("PLT", ("Platform (product level)", "— (platform-wide)")),
    ("MODE", ("Operating modes (Policy System, POL-008)", "CORE TRADING FOUNDATION")),
    ("ARCH", ("Platform architecture (cross-cutting)", "FOUNDATION")),
    ("TEC", ("Technology stack", "FOUNDATION")),
    ("RMP", ("Roadmap", "FOUNDATION")),
    ("EXA", ("SYS-01 Exchange Adapter Layer", "DATA FOUNDATION")),
    ("MKD", ("SYS-02 Market-Data Infrastructure", "DATA FOUNDATION")),
    ("QNT", ("SYS-03 Quantitative Engine", "DATA FOUNDATION")),
    ("RGM", ("SYS-04 Market Regime Engine", "DATA FOUNDATION")),
    ("OPP", ("SYS-05 Opportunity Detection Engine", "DATA FOUNDATION (Opportunity Database: CORE TRADING FOUNDATION)")),
    ("TNP", ("SYS-06 True Net-Profit Engine", "CORE TRADING FOUNDATION (+ ARBITRAGE cost components)")),
    ("CAP", ("SYS-07 Global Capital Authority", "CORE TRADING FOUNDATION")),
    ("PRT", ("SYS-08 Portfolio Management", "CORE TRADING FOUNDATION")),
    ("RSK", ("SYS-09 Risk Engine", "CORE TRADING FOUNDATION")),
    ("EXE", ("SYS-10 Execution Engine", "CORE TRADING FOUNDATION")),
    ("REC", ("SYS-11 Recovery and Reconciliation", "CORE TRADING FOUNDATION / OPERATIONALIZATION")),
    ("POL", ("SYS-12 Policy System", "CORE TRADING FOUNDATION")),
    ("NLP", ("SYS-13 Natural Language Policy Interface", "AI INTELLIGENCE")),
    ("STR", ("SYS-14 Strategy Management", "DIRECTIONAL TRADING")),
    ("BKT", ("SYS-15 Backtesting", "DIRECTIONAL TRADING")),
    ("PAP", ("SYS-16 Paper Trading", "DIRECTIONAL TRADING")),
    ("DIR", ("SYS-17 Directional Trading System", "DIRECTIONAL TRADING")),
    ("XAR", ("SYS-18 Cross-Exchange Arbitrage System", "ARBITRAGE")),
    ("TAR", ("SYS-19 Triangular Arbitrage System", "ARBITRAGE")),
    ("ARB", ("SYS-20 Arbitrage Intelligence", "ARBITRAGE")),
    ("PFC", ("SYS-21 Performance Controller", "DIRECTIONAL TRADING (core); ARBITRAGE (arbitrage tracking)")),
    ("AIL", ("SYS-22 AI Intelligence Layer", "AI INTELLIGENCE")),
    ("AIV", ("SYS-22 AI Intelligence Layer (output validation)", "AI INTELLIGENCE")),
    ("AGT", ("SYS-23 AI Agents", "AI INTELLIGENCE")),
    ("RTR", ("SYS-24 Model Router", "AI INTELLIGENCE")),
    ("COST", ("SYS-25 AI Cost Manager", "AI INTELLIGENCE")),
    ("MEV", ("SYS-26 Model Evaluation", "AI INTELLIGENCE")),
    ("MEM", ("SYS-27 AI Memory / Project Knowledge", "AI INTELLIGENCE")),
    ("MON", ("SYS-28 Monitoring and Observability", "OPERATIONALIZATION")),
    ("DSI", ("SYS-28 Monitoring and Observability (Daily System Intelligence)", "OPERATIONALIZATION")),
    ("INC", ("SYS-28 Monitoring and Observability (Incident Management)", "OPERATIONALIZATION")),
    ("HLT", ("SYS-29 System Health", "CORE TRADING FOUNDATION / OPERATIONALIZATION")),
    ("AUD", ("SYS-30 Auditability / Event and Decision History", "CORE TRADING FOUNDATION")),
    ("SEC", ("SYS-31 Security Architecture", "FOUNDATION")),
    ("CUS", ("SYS-32 Platform Account / Custody", "None (FUTURE)")),
    ("LED", ("SYS-33 Trading Ledger", "CORE TRADING FOUNDATION")),
    ("RDY", ("SYS-34 Readiness System", "DIRECTIONAL TRADING")),
    ("PERF", ("Performance (cross-cutting)", "OPERATIONALIZATION")),
    ("OPS", ("Deployment and operational readiness", "OPERATIONALIZATION")),
    ("MIG", ("Hosting, backup, and migration (cross-cutting)", "OPERATIONALIZATION (MIG-004, MIG-010 from FOUNDATION)")),
    ("VER", ("Verification (cross-cutting)", "OPERATIONALIZATION (production hardening)")),
    ("GOV", ("Architecture governance (cross-cutting)", "FOUNDATION (applies to every stage)")),
])

# Part 1 sections whose content is process/meta rather than requirement lines.
META1 = {
    0: "Builder instructions for this handoff. Applied as process: [project state](../project-state.md), "
       "[DEC-002](../decisions/DEC-002-documentation-structure.md), [DEC-003](../decisions/DEC-003-requirement-ids-and-classification.md), "
       "[DEC-005](../decisions/DEC-005-record-findings-without-resolving.md), [requirements README](../requirements/README.md)",
    99: "Repository organization target. Applied in [DEC-002](../decisions/DEC-002-documentation-structure.md) (with deviations recorded; CF-07)",
    100: "Completion gate. Answered in the \"§100 questions\" table below",
    101: "Implementation gate. Recorded in [project state](../project-state.md) and the [roadmap](../roadmap/roadmap.md)",
    102: "Expected coverage. Checked in the \"§102 topics\" table below",
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
        if m:
            nums = range(int(m.group(1)), int(m.group(2)) + 1)
        elif body.isdigit():
            nums = [int(body)]
        else:
            errors.append(f"bad source {src!r}")
            nums = []
        for n in nums:
            out.add((which, n))
    return out


def strip_code(text):
    return re.sub(r"(?ms)^```.*?^```", "", text)


# ---------- collect requirements ----------
reqs = collections.OrderedDict()
for path in md_files():
    if path in GENERATED:
        continue
    rel = os.path.relpath(path, DOCS)
    in_code = False
    last = None  # requirement whose indented continuation lines (e.g. RSK-015's levels) belong to its text
    for n, line in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
        if line.startswith("```"):
            in_code = not in_code
            last = None
            continue
        if in_code:
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
            d = m.groupdict()
            if d["id"] in reqs:
                errors.append(f"duplicate ID {d['id']} in {rel} and {reqs[d['id']]['doc']}")
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

titles1 = titles_of(os.path.join(DOCS, "handoffs", "part-1-core-platform-features.md"), r"^## (\d{2,3}) — (.+)$")
titles2 = titles_of(os.path.join(DOCS, "handoffs", "part-2-consolidated-additional-systems.md"), r"^## (\d{1,3}) — (.+)$")
if sorted(titles2) != list(range(1, 351)):
    errors.append("Part 2 historical copy does not have sections 1..350")
titles3 = titles_of(os.path.join(DOCS, "handoffs", "part-3-consolidated-autonomy-capital-scaling.md"), r"^## (\d{3}) — (.+)$")
if sorted(titles3) != list(range(351, 551)):
    errors.append("Part 3 historical copy does not have sections 351..550")
TITLES = {1: titles1, 2: titles2, 3: titles3}
PREFIX = {1: "§", 2: "P2§", 3: "P3§"}

sec_ids = {1: collections.defaultdict(list), 2: collections.defaultdict(list), 3: collections.defaultdict(list)}
for i in ids:
    for part, s in reqs[i]["secs"]:
        sec_ids[part][s].append(i)
        if s not in TITLES[part]:
            errors.append(f"{i}: source {PREFIX[part]}{s} does not exist")
for s in sorted(titles1):
    if not sec_ids[1].get(s) and s not in META1:
        errors.append(f"§{s:02d} has no requirement and no meta mapping")

# ---------- decisions ----------
decs = {m.group(1) for f in os.listdir(os.path.join(DOCS, "decisions"))
        for m in [re.match(r"^(DEC-\d{3})-", f)] if m}
decided_by = {}
for m in re.finditer(r"^\| \[(DEC-\d{3})\]\([^)]+\) \| [^|]+ \| ([^|]+) \|", 
                     open(os.path.join(DOCS, "decisions", "README.md"), encoding="utf-8").read(), re.M):
    decided_by[m.group(1)] = m.group(2).strip()
for d in sorted(decs):
    if d not in decided_by:
        errors.append(f"{d} missing from decisions/README.md")


def approval(r):
    if r["cls"] in NOT_APPROVED:
        return NOT_APPROVED[r["cls"]]
    if r["src"].startswith("DEC-"):
        who = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", decided_by.get(r["src"], "?"))
        return f"Decided by: {who}"
    part = {"P2": "Handoff Part 2", "P3": "Handoff Part 3"}.get(r["src"][:2], "Handoff Part 1")
    return part + " — pending documentation review"


# ---------- Part 2 and Part 3 reconciliations: read the hand-written columns ----------
ROW_RE = re.compile(r"^\| (?P<key>\d{1,3}|—) \| (?P<title>[^|]+) \| (?P<new>[^|]*) \| (?P<notes>[^|]*) \|$")
recon_texts = {}
for part, path, name in ((2, RECON2, "part-2-reconciliation"), (3, RECON3, "part-3-reconciliation")):
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
sysreg = open(os.path.join(DOCS, "architecture", "system-registry.md"), encoding="utf-8").read()
defined_sys = set(re.findall(r"^\| (SYS-\d{2}) \|", sysreg, re.M))

# ---------- System Rules Register (ARCH-038) ----------
RULE_RE = re.compile(r"^\| (SR-\d{2}) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| "
                     r"([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$")
defined_rules = []
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
        if not canon_ids:
            errors.append(f"{rid}: no canonical requirement")
        elif canon_ids[0] in reqs and reqs[canon_ids[0]]["cls"] != cls:
            errors.append(f"{rid}: classification {cls!r} is not the class of {canon_ids[0]} ({reqs[canon_ids[0]]['cls']})")
        for i in canon_ids:
            if i in reqs and reqs[i]["cls"] in NOT_APPROVED:
                errors.append(f"{rid}: canonical requirement {i} is not approved ({reqs[i]['cls']})")
if defined_rules != [f"SR-{n:02d}" for n in range(1, len(defined_rules) + 1)]:
    errors.append(f"system-rules-register: SR IDs not unique and sequential: {defined_rules}")

refs = collections.Counter()
for path in md_files():
    rel = os.path.relpath(path, DOCS)
    txt = strip_code(open(path, encoding="utf-8").read())
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
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), link))):
            errors.append(f"{rel}: broken link {link}")
for link in re.findall(r"\]\(\.\./([^)]+)\)", sysreg):
    if not os.path.exists(os.path.join(DOCS, link.split("#")[0])):
        errors.append(f"system-registry link missing: {link}")
for i in ids:
    if reqs[i]["src"].startswith("DEC-") and reqs[i]["src"] not in decs:
        errors.append(f"{i}: source {reqs[i]['src']} is not a decision record")

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
print(f"requirements: {len(ids)} (Part 1: {n_p1}, Part 2: {n_p2}, Part 3: {n_p3}, decisions: {n_dec}); prefixes: {len(byp)}; "
      f"findings: {len(defined_findings)}; decisions: {len(decs)}; systems: {len(defined_sys)}; system rules: {len(defined_rules)}")
print("by class:", dict(cls_count))
print("findings never referenced outside their register:", sorted(defined_findings - set(refs)))
print(f"Part 2 sections with new requirements: {len([s for s in titles2 if sec_ids[2].get(s)])} of 350")
print(f"Part 3 sections with new requirements: {len([s for s in titles3 if sec_ids[3].get(s)])} of 200")
OUT = collections.OrderedDict()  # path -> generated content

# ---------- registry.md ----------
L = ["# Requirements Registry", "",
     "> **Index only.** Requirement text lives in the linked specification (DEC-003). This file is generated by "
     "[`tools/docs/build_index.py`](../../tools/docs/README.md) from the specifications; do not edit it by hand. "
     "Conventions: [README](README.md).",
     ">",
     f"> **Sources:** Handoff Part 1 ({n_p1}), Handoff Part 2 ({n_p2}), Handoff Part 3 ({n_p3}), decision records ({n_dec}) · "
     f"**Status of every entry:** DOCUMENTED — not implemented, not verified · **Total:** {len(ids)} requirements",
     "", "## Summary by class", "", "| Class | Count |", "|---|---|"]
for c in CLASSES:
    if cls_count.get(c):
        L.append(f"| {c} | {cls_count[c]} |")
L += ["",
      "FUTURE entries are recorded but not built. Each DEPRECATED / REPLACED entry names its replacement in its "
      "specification. LED-001 stays conditional on a user-facing platform, which the platform currently is not (DEC-006). "
      "Conflicts and open questions that affect requirements are in the [findings register](../conflicts/register.md) and the "
      "[open-question register](../open-questions/register.md). Concrete values used by requirements are classified in the "
      "[values register](values-register.md). Enforceable behavioral rules are indexed in the "
      "[System Rules Register](system-rules-register.md).",
      "",
      "**Approval** says where the requirement's authority comes from: a handoff section, pending the complete documentation "
      "review before implementation (handoff §101); or a decision record and who decided it. PROPOSED, FUTURE, and "
      "REQUIRES CONFIRMATION entries are not approved (ARCH-029). **Dependencies** are recorded between systems in the "
      "[dependency map](../architecture/dependency-map.md); **verification methods** are assigned when each stage is planned (ARCH-030). "
      "**Default stage** is the owning system's stage; where the [roadmap](../roadmap/roadmap.md) places an individual "
      "requirement in another stage (its \"additions by stage\" tables), the roadmap is authoritative.",
      "", "## Registry", "",
      "| ID | Title | Class | Source | Owner | Specification | Default stage | Approval |",
      "|---|---|---|---|---|---|---|---|"]
for i in ids:
    r = reqs[i]
    owner, stage = OWNERS[i.split("-")[0]]
    L.append(f"| {i} | {r['title'].strip()} | {r['cls']} | {r['src'].strip()} | {owner} | "
             f"[{r['doc']}](../{r['doc']}) | {stage} | {approval(r)} |")
OUT[REGISTRY] = "\n".join(L) + "\n"

# ---------- handoff-coverage.md (Part 1) ----------
old = open(COVERAGE1, encoding="utf-8").read()
static = old[old.index(STATIC1_HEADING):].rstrip("\n")
C = ["# Handoff Coverage — Part 1", "",
     "> Where every section of [Handoff Part 1](../handoffs/part-1-core-platform-features.md) now lives. "
     "The section table and the decision table are generated by [`tools/docs/build_index.py`](../../tools/docs/README.md) "
     "from requirement sources; the §100 and §102 tables were written by hand and checked. A section with no requirement IDs "
     "is process/meta content, and its mapping is stated. Handoff Part 2 is traced in the "
     "[Part 2 reconciliation](part-2-reconciliation.md) and Handoff Part 3 in the "
     "[Part 3 reconciliation](part-3-reconciliation.md).",
     "", "## Section → canonical location", "",
     "| § | Handoff section | Canonical document(s) | Requirement IDs |", "|---|---|---|---|"]
for s in sorted(titles1):
    got = sec_ids[1].get(s, [])
    docs = []
    for i in got:
        if reqs[i]["doc"] not in docs:
            docs.append(reqs[i]["doc"])
    for d in EXTRA_DOCS1.get(s, []):
        if d not in docs:
            docs.append(d)
    if got or docs:
        C.append(f"| {s:02d} | {titles1[s]} | {'; '.join(f'[{d}](../{d})' for d in docs)} | {', '.join(got) if got else '—'} |")
    else:
        C.append(f"| {s:02d} | {titles1[s]} | {META1[s]} | — |")
C += ["", "## Requirements created by decisions", "",
      "These did not come from a handoff section. Each cites the decision record that created it.", "",
      "| Decision | Requirement IDs |", "|---|---|"]
for d in sorted(dec_ids):
    f = [x for x in os.listdir(os.path.join(DOCS, "decisions")) if x.startswith(d + "-")][0]
    C.append(f"| [{d}](../decisions/{f}) | {', '.join(dec_ids[d])} |")
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

if CHECK_ONLY:
    stale = [os.path.relpath(p, ROOT) for p, c in OUT.items() if open(p, encoding="utf-8").read() != c]
    if stale:
        print("ERRORS:")
        for p in stale:
            print(f"  {p} is out of date: run python3 tools/docs/build_index.py")
        sys.exit(1)
    sys.exit(0)
for p, c in OUT.items():
    open(p, "w", encoding="utf-8").write(c)
print("wrote " + ", ".join(os.path.basename(p) for p in OUT))
