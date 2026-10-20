"""The documentation tools' rule for fenced code blocks, shared by build_index.py and
compare_requirements.py so that both read the same lines as code. Standard library only."""

import re


def code_lines(lines: list[str]) -> tuple[list[bool], bool]:
    """Which lines belong to a fenced code block, fences included, and whether a block is
    still open at the end. A fence opens on a line that starts with three or more backticks
    and closes only on a line of at least as many backticks and nothing else, as CommonMark
    closes a backtick fence, so a longer fence can hold shorter ones (a report quoted with its
    own code blocks). Fences of tildes and indented fences are not recognized."""
    fence = 0
    flags = []
    for line in lines:
        if fence:
            flags.append(True)
            close = re.match(r"^(`{3,})[ \t]*$", line)
            if close and len(close.group(1)) >= fence:
                fence = 0
            continue
        opened = re.match(r"^(`{3,})", line)
        fence = len(opened.group(1)) if opened else 0
        flags.append(bool(opened))
    return flags, fence > 0
