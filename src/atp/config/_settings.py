"""The settings, as contracts (MIG-010, MIG-027, MIG-034, OPS-004, MODE-006, SEC-004, SEC-005).

The portable part names the platform and, from Stage 2, the market data it monitors: venues and
instrument types (the Stage 2 plan's D1), their published fee schedules (D8), and the regime
timeframes (D9). The environment-specific part names the environment, declares the secrets it
needs, each by name and kind, never by value, and, from Stage 2, gives its database and its
archive directory. A secret's value comes only from the process environment
(`atp.config.ProcessEnvironment`). Each setting's record (MIG-034) is in docs/development.md,
"Configuration".
"""

from __future__ import annotations

import datetime
import enum
from typing import Annotated, Final

from pydantic import Field, ValidationInfo, field_validator

from atp.contracts import Amount, Contract, ContractVersion, PydanticCustomError
from atp.marketdata import VENUE_PATTERN, InstrumentType

# An identifier (MIG-027): lowercase letters and digits, in parts joined by hyphens, starting
# with a letter. `$` ends the text in the validator's regular expressions and in JSON Schema's,
# so a final line break is refused.
_IDENTIFIER: Final = r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$"
# A secret's name is the name of the process environment variable that holds its value.
_VARIABLE_NAME: Final = r"^[A-Z][A-Z0-9_]*$"
# A date written YYYY-MM-DD; that it exists is checked by a validator.
_DATE: Final = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
# A document's name or address: printable ASCII, so that no control character reaches a log.
_TEXT: Final = r"^[\x20-\x7e]{1,300}$"
# A host name or an IPv4 address, in labels of letters, digits, and hyphens (RFC 1123).
_HOST: Final = (
    r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*$"
)
# A PostgreSQL name written without quotes: lowercase, at most 63 characters.
_SQL_NAME: Final = r"^[a-z_][a-z0-9_]{0,62}$"
# An absolute path, in printable ASCII.
_ABSOLUTE_PATH: Final = r"^/[\x20-\x7e]{0,1023}$"
# A count of seconds that fits a signed 64-bit integer.
_SECONDS = Annotated[int, Field(gt=0, le=2**63 - 1)]


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


class FeeSchedule(Contract):
    """A venue's published fee schedule for one instrument type, at its base tier: the maker and
    taker rates, as fractions of the notional (0.001 is 0.1%), the document they are taken from,
    and the date it was read. A maker rate below zero is a rebate."""

    contract_id = "atp.config.fee-schedule"
    contract_version = ContractVersion(1, 0)
    instrument_type: InstrumentType
    maker: Amount = Field(gt=-1, lt=1)
    taker: Amount = Field(ge=0, lt=1)
    source: str = Field(pattern=_TEXT)
    as_of: str = Field(pattern=_DATE)

    @field_validator("as_of")
    @classmethod
    def _check_date(cls, as_of: str) -> str:
        try:
            datetime.date.fromisoformat(as_of)
        except ValueError:
            raise PydanticCustomError(
                "date_invalid", "a date that exists, written YYYY-MM-DD"
            ) from None
        return as_of


class VenueSettings(Contract):
    """A venue whose public market data is monitored: its identifier, the instrument types
    monitored there, each once, and its published fee schedules, at most one per type monitored."""

    contract_id = "atp.config.venue"
    contract_version = ContractVersion(1, 0)
    venue: str = Field(pattern=VENUE_PATTERN)
    instrument_types: tuple[InstrumentType, ...] = Field(min_length=1)
    fees: tuple[FeeSchedule, ...] = ()

    @field_validator("instrument_types")
    @classmethod
    def _check_types(
        cls, instrument_types: tuple[InstrumentType, ...]
    ) -> tuple[InstrumentType, ...]:
        if len(set(instrument_types)) != len(instrument_types):
            raise PydanticCustomError(
                "duplicate_instrument_type", "an instrument type is listed once"
            )
        return instrument_types

    @field_validator("fees")
    @classmethod
    def _check_fees(
        cls, fees: tuple[FeeSchedule, ...], info: ValidationInfo
    ) -> tuple[FeeSchedule, ...]:
        kinds = [fee.instrument_type for fee in fees]
        if len(set(kinds)) != len(kinds):
            raise PydanticCustomError(
                "duplicate_fee_schedule", "an instrument type has one fee schedule"
            )
        monitored = info.data.get("instrument_types")
        if monitored is not None and any(kind not in monitored for kind in kinds):
            raise PydanticCustomError(
                "fee_schedule_not_monitored",
                "a fee schedule is for an instrument type monitored at the venue",
            )
        return fees


class MarketDataSettings(Contract):
    """The market data the platform monitors: its venues, each once, and the timeframes, in
    seconds, each once, of the bars the Market Regime Engine classifies. Empty, nothing is
    monitored."""

    contract_id = "atp.config.market-data"
    contract_version = ContractVersion(1, 0)
    venues: tuple[VenueSettings, ...] = ()
    regime_timeframes_seconds: tuple[_SECONDS, ...] = ()

    @field_validator("venues")
    @classmethod
    def _check_venues(
        cls, venues: tuple[VenueSettings, ...]
    ) -> tuple[VenueSettings, ...]:
        names = [settings.venue for settings in venues]
        if len(set(names)) != len(names):
            raise PydanticCustomError("duplicate_venue", "a venue is listed once")
        return venues

    @field_validator("regime_timeframes_seconds")
    @classmethod
    def _check_timeframes(cls, timeframes: tuple[int, ...]) -> tuple[int, ...]:
        if len(set(timeframes)) != len(timeframes):
            raise PydanticCustomError(
                "duplicate_timeframe", "a timeframe is listed once"
            )
        return timeframes


class PortableConfiguration(Contract):
    """The part that moves with the platform between environments (MIG-010)."""

    contract_id = "atp.config.portable"
    contract_version = ContractVersion(1, 1)
    platform_id: str = Field(pattern=_IDENTIFIER)
    market_data: MarketDataSettings = MarketDataSettings()


class DatabaseSettings(Contract):
    """The PostgreSQL database that holds the platform's market data: its host and port, the
    database's name, its user, and the name of the declared server secret that holds the user's
    password, never the password itself."""

    contract_id = "atp.config.database"
    contract_version = ContractVersion(1, 0)
    host: str = Field(pattern=_HOST, max_length=253)
    port: int = Field(ge=1, le=65535)
    name: str = Field(pattern=_SQL_NAME)
    user: str = Field(pattern=_SQL_NAME)
    password_secret: str = Field(pattern=_VARIABLE_NAME)


class EnvironmentConfiguration(Contract):
    """The part that belongs to one environment (MIG-010): its identity, its secrets, its
    database, and the directory of its archive."""

    contract_id = "atp.config.environment"
    contract_version = ContractVersion(1, 1)
    environment: Environment
    environment_id: str = Field(pattern=_IDENTIFIER)
    secrets: tuple[SecretDeclaration, ...] = ()
    database: DatabaseSettings | None = None
    archive_directory: str | None = Field(default=None, pattern=_ABSOLUTE_PATH)

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

    @field_validator("database")
    @classmethod
    def _check_database(
        cls, database: DatabaseSettings | None, info: ValidationInfo
    ) -> DatabaseSettings | None:
        # Secrets that failed validation are absent here: their own refusal is reported.
        secrets = info.data.get("secrets")
        if (
            database is not None
            and secrets is not None
            and not any(
                declaration.name == database.password_secret
                and declaration.kind is SecretKind.SERVER
                for declaration in secrets
            )
        ):
            raise PydanticCustomError(
                "database_secret_undeclared",
                "the database's password is a declared secret of kind server",
            )
        return database
