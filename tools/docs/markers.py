"""Requirement markers: where code, tests, and documents name the requirements they serve.

The verification matrix (U7 of the Stage 1 plan; docs/traceability/verification-matrix.md) is
generated from these markers by build_index.py. They are read as text, not with `ast`, so that
the documentation tools keep running on Python 3.10 while the platform's code uses Python 3.12
syntax. tools/docs/README.md describes each form.

  - A paragraph that begins "Requirements:" names the requirements an artifact implements: in a
    Python module's docstring, in a "#" comment of a TOML or YAML file, or in an HTML comment
    ("<!-- Requirements: ... -->") of a Markdown document.
  - A paragraph that begins "Verifies:" names the requirements a check verifies that is not a
    pytest test: in the docstring of a module under tools/, or in an HTML comment of a document
    under docs/traceability/ (the tools, and the verification records).
  - `@pytest.mark.req("ID", ...)`, written on one line as a decorator of a module-level test
    function in a test module, names the requirements that test verifies.

A marker names the IDs written outside parentheses: a parenthesis explains, it does not mark.
"""

import re

ID = r"[A-Z]{2,4}-\d{3}"
KEYWORDS = ("Requirements", "Verifies")

_DOCSTRING = re.compile(
    r'\A(?:[ \t]*(?:#[^\n]*)?\n)*[ \t]*[rRuU]?("""|\'\'\')(.*?)\1', re.S
)
_REQ_DECORATOR = re.compile(r"^(\s*)@pytest\.mark\.req\((.*)\)\s*(?:#.*)?$")
_TEST_DEF = re.compile(r"^(\s*)(?:async\s+)?def\s+(test_\w*)\s*\(")
_STRING = re.compile(r'"([^"\\]*)"')


def top_level_ids(text: str) -> list[str]:
    """The requirement IDs written outside parentheses, in order, without repeats."""
    depth, kept = 0, []
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif depth == 0:
            kept.append(ch)
    out: list[str] = []
    for found in re.findall(rf"\b({ID})\b", "".join(kept)):
        if not found.startswith("DEC-") and found not in out:
            out.append(found)
    return out


def _paragraph(text: str, start: int) -> str:
    """The marker's text from `start` to its first sentence end outside parentheses, or to the
    end of its paragraph (a blank line), whichever comes first."""
    depth = 0
    for i in range(start, len(text)):
        ch = text[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif depth == 0 and ch == "." and (i + 1 == len(text) or text[i + 1].isspace()):
            return text[start:i]
        elif text.startswith("\n\n", i) or text.startswith("\n \n", i):
            return text[start:i]
    return text[start:]


def keyword_markers(text: str, keyword: str) -> list[tuple[int, list[str]]]:
    """Each paragraph of `text` that begins with `keyword:` at the start of a line: the line it
    begins on (1-based, within `text`) and the IDs it names."""
    out = []
    for m in re.finditer(rf"(?m)^[ \t]*{keyword}:", text):
        body = _paragraph(text, m.end())
        out.append((text.count("\n", 0, m.start()) + 1, top_level_ids(body)))
    return out


def module_docstring(text: str) -> str | None:
    """A Python module's docstring, read as text: the string that is its first statement."""
    m = _DOCSTRING.match(text)
    return m.group(2) if m else None


def comment_text(text: str) -> str:
    """The text of the "#" comments of a TOML or YAML file, one comment block per paragraph;
    the comment sign is removed, and any other line ends the block."""
    out = []
    for line in text.split("\n"):
        stripped = line.strip()
        out.append(stripped[1:].strip() if stripped.startswith("#") else "")
    return "\n".join(out)


def html_comments(text: str) -> str:
    """The text of a Markdown document's HTML comments, each followed by a blank line."""
    return "\n\n".join(
        m.group(1).strip() for m in re.finditer(r"<!--(.*?)-->", text, re.S)
    )


def pytest_markers(
    text: str,
) -> tuple[list[tuple[int, str, list[str]]], list[tuple[int, str]], list[str]]:
    """The req markers of a test module, the misuses found, and the test functions it defines.

    Returns (markers, problems, tests): each marker as (line, test name, IDs); each problem as
    (line, description); and the names of the module's functions named test_... at module
    level, the only ones a marker can name. The module is read as text: pytest is not run
    (tools/docs/README.md lists what this does not catch)."""
    lines = text.split("\n")
    markers: list[tuple[int, str, list[str]]] = []
    problems: list[tuple[int, str]] = []
    tests = [m.group(2) for m in map(_TEST_DEF.match, lines) if m and not m.group(1)]
    decorator_lines = set()
    for n, line in enumerate(lines):
        m = _REQ_DECORATOR.match(line)
        if not m:
            continue
        decorator_lines.add(n)
        indent, inner = m.group(1), m.group(2)
        ids = _STRING.findall(inner)
        rest = _STRING.sub("", inner).replace(",", "").strip()
        if not ids or rest:
            problems.append(
                (n + 1, "a req marker takes only requirement IDs, written as strings")
            )
            continue
        if indent:
            problems.append(
                (n + 1, "a req marker must decorate a test function at module level")
            )
            continue
        target = None
        for k in range(n + 1, len(lines)):
            nxt = lines[k]
            if not nxt.strip():
                continue
            cur = len(nxt) - len(nxt.lstrip())
            if cur > len(indent):
                continue  # a line of a decorator written on several lines
            if nxt.lstrip().startswith("@") or nxt.lstrip()[:1] in ")]":
                continue
            d = _TEST_DEF.match(nxt)
            if d and len(d.group(1)) == len(indent):
                target = d.group(2)
            break
        if target is None:
            problems.append((n + 1, "a req marker must decorate a test function"))
            continue
        markers.append((n + 1, target, ids))
    for n, line in enumerate(lines):
        if (
            "mark.req" in line
            and n not in decorator_lines
            and not line.lstrip().startswith("#")
        ):
            problems.append(
                (
                    n + 1,
                    "a req marker must be written on one line, as a decorator of a test function",
                )
            )
    return markers, problems, tests
