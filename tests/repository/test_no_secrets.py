"""Repository test: no secret-like file or value can be committed (SEC-005).

Scans every file git tracks or would add (tracked files, plus untracked files that are not
ignored) for file names that hold secrets and for values that look like credentials. It reads
the files as they are in the working tree; the machine checks run it on exactly the pushed
commit. The scanner is itself tested on planted samples, assembled at run time so that this
file never contains one.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
from collections.abc import Callable, Iterable
from pathlib import Path

import pytest

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
    rb"|secret|token)"
)

# Values that look like credentials: the published formats of their issuers, credentials in a
# URL, and a credential-named setting assigned a value. A credential name may carry a prefix
# (BINANCE_API_SECRET, DB_PASSWORD). A setting's value, quoted or not, is reported only if it
# contains both a letter and a digit, so these are not reported, because they are not
# credentials: type names, file paths, numbers, enum values, masked values ("****"), and
# environment-variable names, from which a secret is read. Nor are a value with spaces or in
# angle brackets (a placeholder), or a template or variable reference ({password},
# ${DB_PASSWORD}), in a setting or a URL. Lines may end in LF or CRLF.
SECRET_VALUE_PATTERNS: dict[str, re.Pattern[bytes]] = {
    "private key block": re.compile(rb"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY"),
    "AWS access key ID": re.compile(rb"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(rb"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_\w{22,})"),
    "GitLab token": re.compile(rb"\bglpat-[A-Za-z0-9_-]{20,}"),
    "PyPI token": re.compile(rb"\bpypi-AgE[A-Za-z0-9_-]{50,}"),
    "npm token": re.compile(rb"\bnpm_[A-Za-z0-9]{36}\b"),
    "Slack token": re.compile(rb"\b(?:xox[abposr]|xapp)-[A-Za-z0-9-]{10,}"),
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
    "credential assignment": re.compile(
        rb"(?i)(?<![a-z0-9])"
        + _CREDENTIAL_NAME
        + rb"[\"']?\s*[:=]\s*(?:[bru]{1,2})?[\"']{1,3}"
        + rb"(?![$%]?\{)(?!(?-i:[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+)[\"'])"
        + rb"(?=[^\"'\s]*[0-9])(?=[^\"'\s]*[A-Za-z])[^\"'\s]{8,}[\"']"
    ),
    "unquoted credential assignment": re.compile(
        rb"(?m)^[ \t]*(?:export[ \t]+)?[A-Z0-9_]*(?:KEY|SECRET|TOKEN|PASSWORD|PASSWD|PASSPHRASE)"
        rb"[A-Z0-9_]*[ \t]*=[ \t]*(?=\S*[0-9])(?=\S*[A-Za-z])[A-Za-z0-9/+=_.~-]{8,}"
        rb"[ \t]*(?:#[^\r\n]*)?\r?$"
    ),
    "unquoted credential setting": re.compile(
        rb"(?mi)^[ \t]*[a-z0-9_-]*" + _CREDENTIAL_NAME + rb"[a-z0-9_-]*[ \t]*:[ \t]+"
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
    )
    (tmp_path / "guide.md").write_text(text, encoding="utf-8")
    (tmp_path / "id_rsa.pub").write_text("ssh-ed25519 AAAA public\n", encoding="utf-8")
    assert secret_findings(tmp_path, [Path("guide.md"), Path("id_rsa.pub")]) == []
