"""Repository test: no secret-like file or value can be committed (SEC-005).

Scans every file git tracks or would add (tracked files, plus untracked files that are not
ignored) for file names that hold secrets and for values that look like credentials, and every
TOML file among them for a secret declaration that is not a name and a kind as the
configuration reads them (U4: a declaration never holds a value). It reads the files as they
are in the working tree; the machine checks run it on exactly the pushed commit. The scanner
is itself tested on planted samples, assembled at run time so that this file never contains
one.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tomllib
from collections.abc import Callable, Iterable
from pathlib import Path

import pytest
from hypothesis import event, given
from hypothesis import strategies as st

from atp.config import SecretDeclaration
from atp.contracts import ContractError

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]

# File names that hold secrets, credentials, or local environments. Public keys (*.pub) are
# allowed.
SECRET_FILE_NAMES = frozenset(
    {
        ".env",
        ".envrc",
        ".git-credentials",
        ".netrc",
        ".npmrc",
        ".pgpass",
        ".pypirc",
        "credentials",
        "credentials.json",
        "id_dsa",
        "id_ecdsa",
        "id_ed25519",
        "id_rsa",
        "keystore.json",
        "secrets.json",
        "secrets.toml",
        "secrets.yaml",
        "secrets.yml",
        "wallet.dat",
    }
)
SECRET_FILE_SUFFIXES = frozenset(
    {".env", ".jks", ".kdbx", ".key", ".keystore", ".p12", ".pem", ".pfx", ".ppk"}
)

# Names of settings that hold credentials, for the assignment patterns below.
_CREDENTIAL_NAME = (
    rb"(?:api[_-]?key|api[_-]?secret|secret[_-]?access[_-]?key|secret[_-]?key"
    rb"|access[_-]?key|signing[_-]?key|encryption[_-]?key|client[_-]?secret"
    rb"|access[_-]?token|auth[_-]?token|private[_-]?key|password|passwd|passphrase"
    rb"|credentials?|secret|token)"
)

# Values that look like credentials: the published formats of their issuers, credentials in a
# URL or an HTTP authorization header, and a credential-named setting assigned a value. A
# credential name may carry a prefix and a suffix (BINANCE_API_SECRET, DB_PASSWORD_PROD), and
# be assigned in a subscript (os.environ["API_SECRET"] = ...), with :=, or as an f-string. A
# setting's value, quoted or not, is reported only if it contains both a letter and a digit, so
# these are not reported, because they are not credentials: type names, file paths, numbers,
# enum values, masked values ("****"), and environment-variable names, from which a secret is
# read. Nor are a value with spaces or in angle brackets (a placeholder), or a template or
# variable reference ({password}, ${DB_PASSWORD}), in a setting or a URL. Lines may end in LF or
# CRLF. What the patterns leave out on purpose is in the stage record ("Checkpoint C: the
# carried items").
SECRET_VALUE_PATTERNS: dict[str, re.Pattern[bytes]] = {
    "private key block": re.compile(rb"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY"),
    "AWS access key ID": re.compile(rb"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(rb"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_\w{22,})"),
    "GitLab token": re.compile(rb"\bglpat-[A-Za-z0-9_-]{20,}"),
    "PyPI token": re.compile(rb"\bpypi-AgE[A-Za-z0-9_-]{50,}"),
    "npm token": re.compile(rb"\bnpm_[A-Za-z0-9]{36}\b"),
    "Slack token": re.compile(rb"\b(?:xox[abposre]|xapp)-[A-Za-z0-9-]{10,}"),
    "Slack webhook": re.compile(
        rb"hooks\.slack\.com/services/T[A-Z0-9]+/B[A-Z0-9]+/[A-Za-z0-9]{20,}"
    ),
    "Stripe live key": re.compile(rb"\b[rs]k_live_[A-Za-z0-9]{20,}"),
    "Google API key": re.compile(rb"\bAIza[0-9A-Za-z_-]{35}"),
    "SendGrid key": re.compile(rb"\bSG\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9_-]{43}\b"),
    "Telegram bot token": re.compile(rb"\b[0-9]{8,10}:AA[A-Za-z0-9_-]{33}\b"),
    "sk- API key": re.compile(rb"\bsk-[A-Za-z0-9_-]{20,}"),
    "JSON web token": re.compile(
        rb"\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"
    ),
    "credentials in a URL": re.compile(
        rb"\b[a-z][a-z0-9+.-]*://[^\s/?#:@\"'<>{}$%]*:[^\s/?#@\"'<>{}$%]{3,}@",
        re.IGNORECASE,
    ),
    "authorization header": re.compile(
        rb"(?i)\bauthorization[\"']?\s*:\s*[\"']?(?:basic|bearer)[ \t]+"
        rb"(?=[A-Za-z0-9+/=._~-]*[0-9])(?=[A-Za-z0-9+/=._~-]*[A-Za-z])[A-Za-z0-9+/=._~-]{8,}"
    ),
    "credential assignment": re.compile(
        rb"(?i)(?<![a-z0-9])"
        + _CREDENTIAL_NAME
        + rb"[a-z0-9_-]*[\"']?\]?\s*(?::=|[:=])\s*(?:[bruf]{1,2})?[\"']{1,3}"
        + rb"(?![$%]?\{)(?!(?-i:[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+)[\"'])"
        + rb"(?=[^\"'\s]*[0-9])(?=[^\"'\s]*[A-Za-z])[^\"'\s]{8,}[\"']"
    ),
    "unquoted credential assignment": re.compile(
        rb"(?m)^[ \t]*(?:export[ \t]+)?[A-Z0-9_]*"
        rb"(?:KEY|SECRET|TOKEN|PASSWORD|PASSWD|PASSPHRASE|CREDENTIAL)"
        rb"[A-Z0-9_]*[ \t]*=[ \t]*(?=\S*[0-9])(?=\S*[A-Za-z])[A-Za-z0-9/+=_.~-]{8,}"
        rb"[ \t]*(?:#[^\r\n]*)?\r?$"
    ),
    "unquoted credential setting": re.compile(
        rb"(?mi)^[ \t]*(?:-[ \t]+)?[a-z0-9_-]*"
        + _CREDENTIAL_NAME
        + rb"[a-z0-9_-]*[ \t]*:[ \t]+"
        rb"(?=\S*[0-9])(?=\S*[A-Za-z])[A-Za-z0-9/+=_.~-]{12,}[ \t]*\r?$"
    ),
}


def is_secret_file_name(path: Path) -> bool:
    """Whether a file's name marks it as one that holds secrets or a local environment."""
    name = path.name
    return (
        name in SECRET_FILE_NAMES
        or name.startswith(".env.")
        or path.suffix.lower() in SECRET_FILE_SUFFIXES
    )


def is_declaration(item: object) -> bool:
    """Whether an item of a `secrets` array is a secret declaration as the configuration reads
    one (`atp.config.SecretDeclaration`): a valid name and kind, and nothing else. An item that
    cannot even be written as JSON (a date, an integer too long, nesting too deep) is not one."""
    try:
        SecretDeclaration.from_json(json.dumps(item))
    except (ContractError, TypeError, ValueError, RecursionError):
        return False
    return True


def declaration_findings(relative: Path, content: bytes) -> list[str]:
    """In a TOML file, every `secrets` key must hold an array of secret declarations: a value
    written beside a name, in place of a kind, or in place of a name unless it has a name's
    shape, or secrets written as a table or as plain values, is reported. A file that
    cannot be read as TOML is reported too, since its declarations cannot be checked."""
    try:
        document = tomllib.loads(content.decode("utf-8"))
    except (ValueError, RecursionError):
        # Not UTF-8, not valid TOML, an integer too long to read, or nested too deeply.
        return [
            f"{relative}: not readable as TOML, so its secret declarations are unchecked"
        ]
    findings: list[str] = []
    pending: list[object] = [document]
    while pending:
        value = pending.pop()
        if isinstance(value, list):
            pending.extend(value)
        elif isinstance(value, dict):
            for key, item in value.items():
                if key == "secrets" and not (
                    isinstance(item, list)
                    and all(is_declaration(declaration) for declaration in item)
                ):
                    findings.append(
                        f"{relative}: secrets are declared only by name and kind"
                    )
                pending.append(item)
    return findings


def secret_findings(root: Path, paths: Iterable[Path]) -> list[str]:
    """One message per secret-like file name or value under root; never the value itself."""
    findings: list[str] = []
    for relative in sorted(paths):
        if is_secret_file_name(relative):
            findings.append(f"{relative}: secret-like file name")
        file = root / relative
        if not file.is_file():
            continue
        content = file.read_bytes()
        for label, pattern in SECRET_VALUE_PATTERNS.items():
            for match in pattern.finditer(content):
                line = content.count(b"\n", 0, match.start()) + 1
                findings.append(f"{relative}:{line}: secret-like value ({label})")
        if relative.suffix == ".toml":
            findings.extend(declaration_findings(relative, content))
    return findings


def _git(root: Path, *arguments: str) -> bytes:
    """Run git on the repository at root only, whatever repository variables are set."""
    git = shutil.which("git")
    if git is None:
        pytest.fail("git is needed to list the repository's files")
    environment = {
        key: value
        for key, value in os.environ.items()
        if key not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"}
    }
    result = subprocess.run(  # noqa: S603 - fixed arguments, no shell, no outside input
        [git, "-C", str(root), *arguments],
        check=True,
        capture_output=True,
        env=environment,
    )
    return result.stdout


def committable_files(root: Path) -> list[Path]:
    """Files git tracks, plus untracked files git would add (not ignored)."""
    listing = _git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard")
    return [Path(name.decode()) for name in listing.split(b"\0") if name]


def test_repository_has_no_secret_like_file_or_value() -> None:
    files = committable_files(REPOSITORY_ROOT)
    assert Path("pyproject.toml") in files, (
        "the scan does not cover the repository root"
    )
    assert secret_findings(REPOSITORY_ROOT, files) == []


def test_committable_files_lists_what_git_would_commit(tmp_path: Path) -> None:
    _git(tmp_path, "init", "-q")
    (tmp_path / ".gitignore").write_text("ignored.txt\nforced.txt\n", encoding="utf-8")
    for name in ("tracked.txt", "untracked.txt", "ignored.txt", "forced.txt"):
        (tmp_path / name).write_text("text\n", encoding="utf-8")
    _git(tmp_path, "add", "tracked.txt")
    _git(tmp_path, "add", "--force", "forced.txt")
    assert sorted(committable_files(tmp_path)) == [
        Path(".gitignore"),
        Path("forced.txt"),
        Path("tracked.txt"),
        Path("untracked.txt"),
    ]


def _assembled(*parts: str) -> str:
    return "".join(parts)


# Documents the property test of the declaration check tries: one or two secret declarations,
# each with a name and a kind, either missing, valid or not; after the first, one more line, or
# none: a table too deep to convert to JSON, or a key `z` that the declaration's contract refuses,
# whose value the conversion to JSON refuses (a date, a time, an integer too long in another
# base), the reading refuses (an integer too long, nesting too deep), or neither (`inf`); first
# and last lines of other kinds, the first with a `secrets` key of its own, in another table.
_NAMES = ['"ATP_X"', '"ATP_Y"', '"lower"', "1", '["ATP_X"]']
_KINDS = ['"ai"', '"server"', '"trading"', '"transfer"', "{a = 1}"]
# A table 10,000 deep in the declaration before it: too deep to write as JSON (the encoder takes
# 5,000 levels), also while Hypothesis raises the recursion limit for a test.
_DEEP_TABLE = "[secrets." + ".".join(["a"] * 10000) + "]"
_FAILING_LINES = [
    "",
    "z = 1979-05-27",
    "z = 07:32:00",
    "z = 0x" + "f" * 4000,
    "z = 0o" + "7" * 5000,
    _DEEP_TABLE,
    "z = 1" + "0" * 5000,
    "z = " + "[" * 3000 + "]" * 3000,
    "z = inf",
]
_FIRST_LINES = [
    "",
    "x = 1",
    "[other]\nsecrets = []",
    "[other]\nsecrets = 1",
    '[other]\nsecrets = [{name = "ATP_X"}]',
]
_LAST_LINES = ["", "[t]", "x = 2"]


def _secrets_document(
    first: str, declarations: list[dict[str, str]], failing: str, last: str
) -> str:
    lines = [first]
    for number, declaration in enumerate(declarations):
        lines.append("[[secrets]]")
        lines.extend(f"{key} = {value}" for key, value in declaration.items())
        if number == 0:
            lines.append(failing)
    lines.append(last)
    return "\n".join(lines) + "\n"


_SECRETS_DOCUMENTS = st.builds(
    _secrets_document,
    st.sampled_from(_FIRST_LINES),
    st.lists(
        st.fixed_dictionaries(
            {},
            optional={"name": st.sampled_from(_NAMES), "kind": st.sampled_from(_KINDS)},
        ),
        min_size=1,
        max_size=2,
    ),
    st.sampled_from(_FAILING_LINES),
    st.sampled_from(_LAST_LINES),
)


# (label, sample) pairs: each sample must be reported under its label.
PLANTED_VALUES: list[tuple[str, Callable[[], str]]] = [
    (
        "private key block",
        lambda: _assembled("-----BEGIN ", "RSA PRIVATE KEY-----\nabc\n"),
    ),
    ("AWS access key ID", lambda: _assembled("key_id: AKIA", "Q" * 16)),
    ("AWS access key ID", lambda: _assembled("temporary: AS", "IA", "R" * 16)),
    ("GitHub token", lambda: _assembled("ghp", "_", "a1" * 18)),
    ("GitHub token", lambda: _assembled("gh", "s_", "b2" * 18)),
    ("credential assignment", lambda: _assembled("tok", "en = ", '"', "v4" * 6, '"')),
    (
        "unquoted credential assignment",
        lambda: _assembled("BINANCE_API", "_SECRET=", "q9" * 8, "\r"),
    ),
    (
        "unquoted credential setting",
        lambda: _assembled("  api", "_secret: ", "r4" * 8, "\r"),
    ),
    ("GitLab token", lambda: _assembled("glp", "at-", "d4" * 10)),
    ("PyPI token", lambda: _assembled("py", "pi-AgE", "e5" * 30)),
    ("npm token", lambda: _assembled("np", "m_", "f6" * 18)),
    ("Slack token", lambda: _assembled("xox", "b-", "1234567890-abcdef")),
    ("Slack token", lambda: _assembled("xa", "pp-", "1-A2B3C4D5E6-7890")),
    (
        "Slack webhook",
        lambda: _assembled(
            "https://hooks.", "slack.com/services/", "T0", "/B0/", "g7" * 12
        ),
    ),
    ("Stripe live key", lambda: _assembled("sk", "_live_", "a" * 24)),
    ("Google API key", lambda: _assembled("AI", "za", "b" * 35)),
    ("SendGrid key", lambda: _assembled("S", "G.", "h" * 22, ".", "i" * 43)),
    ("Telegram bot token", lambda: _assembled("123456", "789:", "AA", "j" * 33)),
    ("sk- API key", lambda: _assembled("s", "k-", "c" * 24)),
    (
        "JSON web token",
        lambda: _assembled("ey", "J", "k" * 12, ".ey", "J", "l" * 12, ".", "m" * 12),
    ),
    (
        "credentials in a URL",
        lambda: _assembled("postgresql://trader", ":", "n8" * 5, "@db/x"),
    ),
    (
        "credential assignment",
        lambda: _assembled("pass", "word = ", '"', "x7" * 6, '"'),
    ),
    (
        "credential assignment",
        lambda: _assembled("BINANCE_API", "_SECRET = ", '"', "q9" * 8, '"'),
    ),
    (
        "credential assignment",
        lambda: _assembled("DB_PASS", "WORD=", '"', "w8" * 6, '"'),
    ),
    (
        "credential assignment",
        lambda: _assembled("exchange_api", "_key: ", '"', "k7" * 6, '"'),
    ),
    ("credential assignment", lambda: _assembled('"sec', 'ret": ', '"', "z6" * 6, '"')),
    (
        "credential assignment",
        lambda: _assembled("AWS_SECRET_ACCESS", "_KEY = ", '"', "a9" * 10, '"'),
    ),
    (
        "credential assignment",
        lambda: _assembled("ENCRYPTION", "_KEY = ", '"', "e3" * 8, '"'),
    ),
    ("credential assignment", lambda: _assembled("SIGNING", "_KEY='", "s2" * 8, "'")),
    (
        "credential assignment",
        lambda: _assembled("API_SEC", "RET = b", '"', "b1" * 8, '"'),
    ),
    ("credential assignment", lambda: _assembled("api_sec", "ret = r'", "c3" * 8, "'")),
    (
        "credential assignment",
        lambda: _assembled("SECRET", '_KEY = """', "t5" * 8, '"""'),
    ),
    (
        "credentials in a URL",
        lambda: _assembled("redis://", ":", "u6" * 4, "@cache:6379/0"),
    ),
    (
        "unquoted credential assignment",
        lambda: _assembled("BINANCE_API", "_SECRET=", "q9" * 8),
    ),
    (
        "unquoted credential assignment",
        lambda: _assembled("export OKX_PASS", "PHRASE=", "p5" * 6, " # live"),
    ),
    ("unquoted credential setting", lambda: _assembled("  api", "_secret: ", "r4" * 8)),
    # Decided at checkpoint C (the stage record, "Checkpoint C: the carried items").
    ("Slack token", lambda: _assembled("xo", "xe-", "1-A2B3C4D5E6-7890")),
    (
        "authorization header",
        lambda: _assembled("Authori", "zation: Bearer ", "t7" * 10),
    ),
    (
        "authorization header",
        lambda: _assembled('"Authori', 'zation": "Basic ', "dXNlcjpwYTU1d29yZA==", '"'),
    ),
    (
        "credential assignment",
        lambda: _assembled("DB_PASS", "WORD_PROD = ", '"', "x8" * 4, '"'),
    ),
    (
        "credential assignment",
        lambda: _assembled('os.environ["API_SEC', 'RET"] = ', '"', "q7" * 5, '"'),
    ),
    (
        "credential assignment",
        lambda: _assembled("(pass", "word := ", '"', "w5" * 4, '")'),
    ),
    (
        "credential assignment",
        lambda: _assembled("tok", "en = f", '"', "a1b2" * 3, '"'),
    ),
    (
        "unquoted credential setting",
        lambda: _assembled("  - api", "_secret: ", "r4" * 8),
    ),
    # The configuration's own name for a secret (atp.config: ATP_EXAMPLE_SERVER_CREDENTIAL).
    (
        "credential assignment",
        lambda: _assembled("server_creden", "tial = ", '"', "x7" * 6, '"'),
    ),
    (
        "unquoted credential assignment",
        lambda: _assembled("ATP_EXAMPLE_SERVER_CREDEN", "TIAL=", "q9" * 8),
    ),
]


@pytest.mark.parametrize(
    ("label", "sample"),
    PLANTED_VALUES,
    ids=[f"{label}-{index}" for index, (label, _) in enumerate(PLANTED_VALUES)],
)
def test_scanner_finds_planted_value(
    tmp_path: Path, label: str, sample: Callable[[], str]
) -> None:
    planted = Path("notes.txt")
    (tmp_path / planted).write_text(f"line one\n{sample()}\n", encoding="utf-8")
    findings = secret_findings(tmp_path, [planted])
    assert f"notes.txt:2: secret-like value ({label})" in findings


@pytest.mark.parametrize(
    "name",
    [
        ".env",
        ".env.production",
        ".envrc",
        "binance.env",
        ".pgpass",
        "credentials",
        "secrets.yaml",
        "wallet.dat",
        "id_rsa",
        "deploy.pem",
        "client.KEY",
        "store.p12",
    ],
)
def test_scanner_finds_secret_like_file_name(tmp_path: Path, name: str) -> None:
    (tmp_path / name).write_text("placeholder\n", encoding="utf-8")
    assert secret_findings(tmp_path, [Path(name)]) == [f"{name}: secret-like file name"]


def test_scanner_reports_no_value_text(tmp_path: Path) -> None:
    secrets = [sample() for _, sample in PLANTED_VALUES]
    (tmp_path / "settings.txt").write_text("\n".join(secrets) + "\n", encoding="utf-8")
    findings = secret_findings(tmp_path, [Path("settings.txt")])
    assert len(findings) >= len(secrets)
    kinds = "|".join(map(re.escape, SECRET_VALUE_PATTERNS))
    report = re.compile(rf"settings\.txt:[0-9]+: secret-like value \((?:{kinds})\)")
    assert all(report.fullmatch(finding) for finding in findings), findings


def test_scanner_passes_ordinary_text(tmp_path: Path) -> None:
    text = (
        "Secrets come only from the runtime environment (SEC-005).\n"
        'password = "<from the environment>"\n'
        "API_KEY=<your key>\n"
        "MAX_TOKENS=4096\n"
        "token_count: 3\n"
        "Connect to postgresql://<user>:<password>@<host>/db, or https://example.com:8080/x.\n"
        "The task-scheduler and risk-adjusted returns are not keys; 12:34:56 is a time.\n"
        "id_rsa.pub holds a public key.\n"
        'DSN = f"postgresql://{user}:{password}@{host}/atp"\n'
        "DATABASE_URL=postgresql://atp:${ATP_DB_PASSWORD}@db:5432/atp\n"
        "See http://localhost:8000?email=ops@example.com for the console.\n"
        "api_secret: pydantic.SecretStr\n"
        "token: IdempotencyKey\n"
        "secret: RedactedString\n"
        "API_KEY_FILE=/run/secrets/exchange\n"
        "password_file: /run/secrets/exchange\n"
        "secret_source: process_environment\n"
        "token_type: bearer_token\n"
        "TOKEN_BUDGET=100000000\n"
        "SECRET_KEY_LENGTH = 32\n"
        "token_budget: 100000000000\n"
        'PASSWORD = "${DB_PASSWORD}"\n'
        'password: "${ATP_DB_PASSWORD}"\n'
        'POSTGRES_PASSWORD: "${POSTGRES_PASSWORD:?required}"\n'
        'password = "{password}"\n'
        'password: "SecretStr"\n'
        'private_key = "/run/secrets/exchange"\n'
        'token = "12345678"\n'
        'EXCHANGE_API_KEY = "exchange_api_key"\n'
        'binance_api_secret = "trading_credential"\n'
        'password = "**********"\n'
        'password = "${DB_PASSWORD_2}"\n'
        'api_key = "BINANCE_API_KEY_2"\n'
        'api_key = "BINANCE_API_KEY"\n'
        '{"api_secret": "ATP_BINANCE_API_SECRET"}\n'
        "Authorization: Bearer <token>\n"
        "Authorization: Basic placeholder\n"
        "Bearer tokens and Basic authentication are refused by the gateway.\n"
        'token_type = "bearer"\n'
        'password_file_path = "/run/secrets/exchange"\n'
        'os.environ["ATP_DB_PASSWORD"] = "${ATP_DB_PASSWORD}"\n'
        "- token_budget: 100000000000\n"
    )
    (tmp_path / "guide.md").write_text(text, encoding="utf-8")
    (tmp_path / "id_rsa.pub").write_text("ssh-ed25519 AAAA public\n", encoding="utf-8")
    assert secret_findings(tmp_path, [Path("guide.md"), Path("id_rsa.pub")]) == []


# The example configuration (config/examples/, U4 and U5 of the Stage 1 plan).

EXAMPLES = Path("config") / "examples"


def _example_files() -> list[Path]:
    return sorted(
        path for path in committable_files(REPOSITORY_ROOT) if EXAMPLES in path.parents
    )


def test_the_example_configuration_is_scanned_and_holds_no_secret() -> None:
    examples = _example_files()
    assert EXAMPLES / "platform.toml" in examples
    assert len([path for path in examples if path.parent.name == "environments"]) == 6
    assert secret_findings(REPOSITORY_ROOT, examples) == []


def _copy_of_examples(tmp_path: Path) -> list[Path]:
    examples = _example_files()
    for relative in examples:
        (tmp_path / relative).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPOSITORY_ROOT / relative, tmp_path / relative)
    return examples


@pytest.mark.parametrize(
    ("added", "finding"),
    [
        # A value written beside the declaration's name (the last table of the file).
        (
            lambda: _assembled('value = "', "v4" * 6, '"\n'),
            "secrets are declared only by name and kind",
        ),
        (
            lambda: _assembled(
                "ATP_EXAMPLE_SERVER_CREDEN", "TIAL = ", '"', "q9" * 8, '"\n'
            ),
            "secrets are declared only by name and kind",
        ),
        (
            lambda: _assembled("api", "_secret", ' = "', "z6" * 6, '"\n'),
            "secret-like value (credential assignment)",
        ),
    ],
)
def test_a_secret_planted_in_a_copy_of_an_example_is_found(
    tmp_path: Path, added: Callable[[], str], finding: str
) -> None:
    examples = _copy_of_examples(tmp_path)
    assert secret_findings(tmp_path, examples) == []
    for relative in examples:
        if relative.parent.name != "environments":
            continue
        with (tmp_path / relative).open("a", encoding="utf-8") as file:
            file.write(added())
        findings = secret_findings(tmp_path, [relative])
        assert any(finding in line for line in findings), (relative, findings)
        assert all(relative.as_posix() in line for line in findings)


@pytest.mark.parametrize(
    "text",
    [
        '[secrets]\nATP_X = "plain"\n',
        'secrets = ["plain"]\n',
        '[[secrets]]\nname = "ATP_X"\nkind = "server"\nnote = "plain"\n',
        '[nested]\n[[nested.secrets]]\nname = "ATP_X"\nvalue = "plain"\n',
        'secrets = "plain"\n',
        "[secrets]\n",
        '[[groups]]\n[[groups.secrets]]\nname = "ATP_X"\nvalue = "plain"\n',
        # A value in place of a kind, or in place of a name without a name's shape, an unknown
        # kind, or a declaration without one.
        '[[secrets]]\nname = "ATP_X"\nkind = "'
        + _assembled("sk", "_live_", "Q7x9Z2")
        + '"\n',
        '[[secrets]]\nname = "' + _assembled("a1b2", "c3d4e5") + '"\nkind = "server"\n',
        '[[secrets]]\nname = "atp_x"\nkind = "server"\n',
        '[[secrets]]\nname = "ATP_X"\nkind = "transfer"\n',
        '[[secrets]]\nname = "ATP_X"\n',
        '[[secrets]]\nname = "ATP_X"\nkind = 3\n',
    ],
)
def test_secrets_declared_otherwise_than_by_name_and_kind_are_found(
    tmp_path: Path, text: str
) -> None:
    (tmp_path / "settings.toml").write_text(text, encoding="utf-8")
    assert secret_findings(tmp_path, [Path("settings.toml")]) == [
        "settings.toml: secrets are declared only by name and kind"
    ]


@pytest.mark.parametrize(
    "text",
    [
        '[[secrets]]\nname = 1979-05-27\nkind = "ai"\n',
        '[[secrets]]\nname = "ATP_X"\nkind = "ai"\nz = 0x' + "f" * 4000 + "\n",
        '[[secrets]]\nname = "ATP_X"\nkind = "ai"\n[secrets.'
        + ".".join(["a"] * 10000)
        + "]\n",
    ],
    ids=["a date", "an integer too long", "a table nested too deeply"],
)
def test_a_declaration_that_cannot_be_written_as_json_is_found(
    tmp_path: Path, text: str
) -> None:
    (tmp_path / "settings.toml").write_text(text, encoding="utf-8")
    assert secret_findings(tmp_path, [Path("settings.toml")]) == [
        "settings.toml: secrets are declared only by name and kind"
    ]


@given(_SECRETS_DOCUMENTS.map(str.encode) | st.binary(max_size=60))
def test_any_content_is_checked_or_reported(content: bytes) -> None:
    # The check's boundary: whatever a TOML file holds (short of exhausting the process's
    # memory), findings are returned, never raised.
    findings = declaration_findings(Path("settings.toml"), content)
    assert all(finding.startswith("settings.toml: ") for finding in findings)
    for finding in findings or ["no finding"]:
        event(finding.removeprefix("settings.toml: "))


def test_declarations_by_name_and_kind_are_not_findings(tmp_path: Path) -> None:
    text = (
        'environment = "paper"\n[[secrets]]\nname = "ATP_X"\nkind = "server"\n'
        '[[secrets]]\nname = "ATP_Y"\nkind = "ai"\n'
    )
    (tmp_path / "settings.toml").write_text(text, encoding="utf-8")
    (tmp_path / "empty.toml").write_text("secrets = []\n", encoding="utf-8")
    assert secret_findings(tmp_path, [Path("settings.toml"), Path("empty.toml")]) == []


@pytest.mark.parametrize(
    "content",
    [
        b"secrets = = 1\n",
        b'name = "\xff"\n',
        b"count = 1" + b"0" * 5000 + b"\n",
        b"x = " + b"[" * 2000 + b"]" * 2000 + b"\n",
    ],
    ids=["not TOML", "not UTF-8", "integer too long", "nested too deeply"],
)
def test_a_toml_file_that_cannot_be_read_is_found(
    tmp_path: Path, content: bytes
) -> None:
    (tmp_path / "settings.toml").write_bytes(content)
    assert secret_findings(tmp_path, [Path("settings.toml")]) == [
        "settings.toml: not readable as TOML, so its secret declarations are unchecked"
    ]
