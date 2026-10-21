"""The settings of Stage 1, as contracts (MIG-010, MIG-027, OPS-004, MODE-006, SEC-004, SEC-005).

The portable part names the platform; the environment-specific part names the environment and
declares the secrets the environment needs, each by name and kind, never by value. A secret's
value comes only from the process environment (`atp.config.ProcessEnvironment`).
"""

from __future__ import annotations

import enum
from typing import Final

from pydantic import Field, ValidationInfo, field_validator

from atp.contracts import Contract, ContractVersion, PydanticCustomError

# An identifier (MIG-027): lowercase letters and digits, in parts joined by hyphens, starting
# with a letter. `$` ends the text in the validator's regular expressions and in JSON Schema's,
# so a final line break is refused.
_IDENTIFIER: Final = r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$"
# A secret's name is the name of the process environment variable that holds its value.
_VARIABLE_NAME: Final = r"^[A-Z][A-Z0-9_]*$"


class Environment(enum.Enum):
    """The six environments of OPS-004."""

    DEVELOPMENT = "development"
    TESTING = "testing"
    RESEARCH = "research"
    PAPER = "paper"
    STAGING = "staging"
    PRODUCTION = "production"


# TRADING is a trading-enabled exchange credential (SEC-004, SEC-006's trading authority,
# MODE-006), declared only in production. AI is an AI provider's credential, held by the AI
# gateway (SEC-004, AIL-006). SERVER is a credential of a service the platform runs on, such as
# a database (MIG-010's server credentials; OPS-004). A transfer credential (SEC-006, SEC-007) is
# added with its own rule when the ARBITRAGE stage needs one; the platform holds no withdrawal
# or custody credential (SEC-006). A contract's docstrings are its committed schema's
# descriptions, so the reasons are kept in comments.
class SecretKind(enum.Enum):
    """What a declared secret is, from a closed set."""

    TRADING = "trading"
    AI = "ai"
    SERVER = "server"


class SecretDeclaration(Contract):
    """A secret the environment needs: its name and kind, never its value."""

    contract_id = "atp.config.secret-declaration"
    contract_version = ContractVersion(1, 0)
    name: str = Field(pattern=_VARIABLE_NAME)
    kind: SecretKind


class PortableConfiguration(Contract):
    """The part that moves with the platform between environments (MIG-010)."""

    contract_id = "atp.config.portable"
    contract_version = ContractVersion(1, 0)
    platform_id: str = Field(pattern=_IDENTIFIER)


class EnvironmentConfiguration(Contract):
    """The part that belongs to one environment (MIG-010): its identity and its secrets."""

    contract_id = "atp.config.environment"
    contract_version = ContractVersion(1, 0)
    environment: Environment
    environment_id: str = Field(pattern=_IDENTIFIER)
    secrets: tuple[SecretDeclaration, ...] = ()

    @field_validator("secrets")
    @classmethod
    def _check_secrets(
        cls, secrets: tuple[SecretDeclaration, ...], info: ValidationInfo
    ) -> tuple[SecretDeclaration, ...]:
        names = [declaration.name for declaration in secrets]
        if len(set(names)) != len(names):
            raise PydanticCustomError(
                "duplicate_secret_name", "a secret is declared once"
            )
        # Defence in depth (constitution Rules 109, 111): the barrier is that no trading
        # credential exists outside production. An environment that failed validation is
        # absent here, and is not production either.
        if info.data.get("environment") is not Environment.PRODUCTION and any(
            declaration.kind is SecretKind.TRADING for declaration in secrets
        ):
            raise PydanticCustomError(
                "trading_credential_outside_production",
                "a trading-enabled credential is declared only in production",
            )
        return secrets
