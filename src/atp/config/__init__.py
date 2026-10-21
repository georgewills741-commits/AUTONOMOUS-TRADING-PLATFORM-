"""Configuration: the one validated source of the platform's settings.

Requirements: MIG-010 (a portable and an environment-specific part), MIG-027 (the platform and
environment identifiers), OPS-004 (the six environments), SEC-005 (secrets only from the runtime
environment, never shown), MIG-004 (no code assumes a host: the configuration directory is
given), MODE-006 and SEC-004 (a trading-enabled credential is refused outside production, as
defence in depth), GOV-014 (no second configuration source). The rules, the settings, and the
command that checks a configuration are in docs/development.md, "Configuration".

A process calls `configure_process()` at start, then `load_configuration(...)`. Every refusal
raises `ConfigurationError`, whose lines never hold a secret's value or a refused value.
"""

from atp.config._load import (
    ENVIRONMENTS_DIRECTORY,
    PORTABLE_FILE,
    Configuration,
    ConfigurationError,
    configure_process,
    environment_named,
    load_configuration,
    read_toml,
    summary,
)
from atp.config._secrets import REDACTED, ProcessEnvironment, Secret, SecretSource
from atp.config._settings import (
    Environment,
    EnvironmentConfiguration,
    PortableConfiguration,
    SecretDeclaration,
    SecretKind,
)

__all__ = [
    "ENVIRONMENTS_DIRECTORY",
    "PORTABLE_FILE",
    "REDACTED",
    "Configuration",
    "ConfigurationError",
    "Environment",
    "EnvironmentConfiguration",
    "PortableConfiguration",
    "ProcessEnvironment",
    "Secret",
    "SecretDeclaration",
    "SecretKind",
    "SecretSource",
    "configure_process",
    "environment_named",
    "load_configuration",
    "read_toml",
    "summary",
]
