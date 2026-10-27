"""The `atp` command: `atp config check` (D1, U4 of the Stage 1 plan; SEC-005)."""

from __future__ import annotations

import importlib.metadata
import subprocess
import sys
from pathlib import Path

import pytest

from atp.cli import main
from atp.config import MAXIMUM_DOCUMENT_SIZE, REDACTED, Environment

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = REPOSITORY_ROOT / "config" / "examples"
EXAMPLE_VARIABLE = "ATP_EXAMPLE_SERVER_CREDENTIAL"

# Assembled at run time so that no file holds a credential-shaped sample.
SECRET = "sk" + "_live_" + "Q7x9Z2" + "secretvalue"


def _check(capsys: pytest.CaptureFixture[str], *arguments: str) -> tuple[int, str, str]:
    status = main(["config", "check", *arguments])
    captured = capsys.readouterr()
    return status, captured.out, captured.err


@pytest.mark.parametrize("environment", [e.value for e in Environment])
@pytest.mark.req("MIG-004", "MIG-010")
def test_every_example_environment_checks(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    environment: str,
) -> None:
    monkeypatch.setenv(EXAMPLE_VARIABLE, SECRET)
    status, out, err = _check(
        capsys, "--env", environment, "--config-dir", str(EXAMPLES)
    )
    assert status == 0
    assert err == ""
    assert out.splitlines() == [
        "configuration valid:",
        "  platform_id: example-platform",
        f"  environment: {environment}",
        f"  environment_id: example-{environment}",
        f"  secret {EXAMPLE_VARIABLE} (server): {REDACTED}",
    ]
    assert SECRET not in out


def _broken(tmp_path: Path, portable: str, paper: str) -> Path:
    (tmp_path / "platform.toml").write_text(portable, encoding="utf-8")
    (tmp_path / "environments").mkdir()
    (tmp_path / "environments" / "paper.toml").write_text(paper, encoding="utf-8")
    return tmp_path


PAPER = (
    'environment = "paper"\nenvironment_id = "example-paper"\n'
    f'[[secrets]]\nname = "{EXAMPLE_VARIABLE}"\nkind = "server"\n'
)


@pytest.mark.parametrize(
    ("portable", "paper", "reason"),
    [
        ("", PAPER, "platform.toml: input refused by contract atp.config.portable:"),
        (
            'platform_id = "example-platform"\n',
            PAPER.replace('"paper"', '"staging"', 1),
            "environments/paper.toml: declares the environment staging, not paper",
        ),
        (
            'platform_id = "example-platform"\n',
            PAPER.replace('"server"', '"trading"'),
            "environments/paper.toml: input refused by contract atp.config.environment:",
        ),
        (
            f'platform_id = "example-platform"\n# {SECRET}\n',
            PAPER,
            f"platform.toml: holds the value of the secret {EXAMPLE_VARIABLE}",
        ),
        ('platform_id = "example-platform"\n', "environment = ", "not valid TOML"),
        ("platform_id = 1" + "0" * 5000 + "\n", PAPER, "platform.toml: not valid TOML"),
        (
            "platform_id = 0x" + "f" * 4000 + "\n",
            PAPER,
            "platform.toml: not valid TOML",
        ),
        (
            "x = " + "[" * 2000 + "]" * 2000 + "\n",
            PAPER,
            "platform.toml: nested too deeply to read",
        ),
        (
            f'platform_id = "example-platform"\n# {SECRET}\n'
            + "#" * MAXIMUM_DOCUMENT_SIZE,
            PAPER,
            (
                f"platform.toml: larger than {MAXIMUM_DOCUMENT_SIZE} bytes, the most a "
                "configuration file may hold"
            ),
        ),
    ],
)
def test_a_broken_configuration_is_refused(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    tmp_path: Path,
    portable: str,
    paper: str,
    reason: str,
) -> None:
    monkeypatch.setenv(EXAMPLE_VARIABLE, SECRET)
    directory = _broken(tmp_path, portable, paper)
    status, out, err = _check(capsys, "--env", "paper", "--config-dir", str(directory))
    assert status == 1
    assert out == ""
    assert err.startswith("configuration refused:\n")
    assert reason in err
    assert SECRET not in err


@pytest.mark.req("SEC-005")
def test_a_missing_secret_is_refused(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.delenv(EXAMPLE_VARIABLE, raising=False)
    status, out, err = _check(capsys, "--env", "paper", "--config-dir", str(EXAMPLES))
    assert status == 1
    assert out == ""
    assert f"the secret {EXAMPLE_VARIABLE} is not set" in err


def test_an_unknown_environment_is_refused(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setenv(EXAMPLE_VARIABLE, SECRET)
    status, out, err = _check(capsys, "--env", "prod", "--config-dir", str(EXAMPLES))
    assert status == 1
    assert out == ""
    assert "unknown environment" in err


@pytest.mark.parametrize(
    "arguments",
    [
        [],
        ["config"],
        ["config", "check"],
        ["config", "check", "--env", "paper"],
        ["config", "check", "--config-dir", "x"],
        ["config", "lint", "--env", "paper", "--config-dir", "x"],
    ],
)
def test_wrong_use_exits_with_status_2(
    capsys: pytest.CaptureFixture[str], arguments: list[str]
) -> None:
    with pytest.raises(SystemExit) as exit_:
        main(arguments)
    assert exit_.value.code == 2
    assert capsys.readouterr().err.startswith("usage: atp")


def test_the_installed_command_runs_this_module() -> None:
    (entry,) = [
        entry
        for entry in importlib.metadata.entry_points(group="console_scripts")
        if entry.name == "atp"
    ]
    assert entry.value == "atp.cli:run"


def test_the_command_sets_up_its_process_before_reading_numbers(tmp_path: Path) -> None:
    # A new interpreter has Python's default decimal context: without `configure_process`,
    # reading a TOML number would raise instead of refusing the setting.
    directory = _broken(tmp_path, "platform_id = 1.5\n", PAPER)
    result = subprocess.run(  # noqa: S603 - this interpreter, fixed arguments
        [
            sys.executable,
            "-c",
            "from atp.cli import run; run()",
            "config",
            "check",
            "--env",
            "paper",
            "--config-dir",
            str(directory),
        ],
        capture_output=True,
        text=True,
        check=False,
        env={EXAMPLE_VARIABLE: SECRET},
    )
    assert result.returncode == 1
    assert result.stdout == ""
    assert result.stderr == (
        "configuration refused:\n"
        "  platform.toml: a number with a fraction or an exponent is not a setting value; "
        "an amount is written as a string\n"
    )
