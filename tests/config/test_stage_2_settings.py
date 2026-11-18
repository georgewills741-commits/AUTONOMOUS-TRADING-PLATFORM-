"""Stage 2's settings: the market data monitored, the database, and the archive (MIG-010,
MIG-034, SEC-005; the Stage 2 plan's U2, D1, D8, D9)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from atp.config import (
    ConfigurationError,
    EnvironmentConfiguration,
    MarketDataSettings,
    PortableConfiguration,
    ProcessEnvironment,
    load_configuration,
    read_toml,
    summary,
)
from atp.contracts import ContractError
from atp.marketdata import InstrumentType

FEE = {
    "instrument_type": "spot",
    "maker": "0.001",
    "taker": "0.001",
    "source": "The venue's published fee schedule",
    "as_of": "2026-11-17",
}
VENUE = {"venue": "example", "instrument_types": ["spot", "perpetual"], "fees": [FEE]}
DATABASE = {
    "host": "db.example.invalid",
    "port": 5432,
    "name": "atp",
    "user": "atp",
    "password_secret": "ATP_DB",
}
SERVER_SECRET = {"name": "ATP_DB", "kind": "server"}


def _market_data(**changes: object) -> str:
    return json.dumps(
        {"venues": [VENUE], "regime_timeframes_seconds": [3600], **changes}
    )


def _venue(**changes: object) -> str:
    return _market_data(venues=[{**VENUE, **changes}])


def _fee(**changes: object) -> str:
    return _venue(fees=[{**FEE, **changes}])


def _environment(**changes: object) -> str:
    return json.dumps(
        {
            "environment": "paper",
            "environment_id": "example-paper",
            "secrets": [SERVER_SECRET],
            "database": DATABASE,
            "archive_directory": "/srv/atp/archive",
            **changes,
        }
    )


def _types(error: pytest.ExceptionInfo[ContractError]) -> list[str]:
    return [detail.type for detail in error.value.details]


@pytest.mark.req("MIG-010", "MIG-034")
def test_the_market_data_settings_are_read() -> None:
    settings = MarketDataSettings.from_json(_market_data())
    (venue,) = settings.venues
    assert venue.venue == "example"
    assert venue.instrument_types == (InstrumentType.SPOT, InstrumentType.PERPETUAL)
    (fee,) = venue.fees
    assert (str(fee.maker), str(fee.taker), fee.as_of) == (
        "0.001",
        "0.001",
        "2026-11-17",
    )
    assert settings.regime_timeframes_seconds == (3600,)


@pytest.mark.req("MIG-010", "MIG-034")
def test_a_stage_1_document_reads_as_monitoring_nothing_with_no_database() -> None:
    # Version 1.1 of each part only adds settings whose defaults keep the meaning of a 1.0
    # document (contract conventions, "Versions and compatibility").
    portable = PortableConfiguration.from_json('{"platform_id":"atp"}')
    assert portable.market_data == MarketDataSettings.from_json("{}")
    assert portable.market_data.venues == ()
    specific = EnvironmentConfiguration.from_json(
        '{"environment":"paper","environment_id":"example-paper"}'
    )
    assert (specific.database, specific.archive_directory) == (None, None)


@pytest.mark.parametrize(
    ("document", "refusal"),
    [
        (_venue(venue="Example"), "string_pattern_mismatch"),
        (_venue(instrument_types=[]), "too_short"),
        (_venue(instrument_types=["spot", "spot"]), "duplicate_instrument_type"),
        (_venue(instrument_types=["spot", "option"]), "enum"),
        (_venue(fees=[FEE, FEE]), "duplicate_fee_schedule"),
        (_venue(instrument_types=["perpetual"]), "fee_schedule_not_monitored"),
        (_market_data(venues=[VENUE, VENUE]), "duplicate_venue"),
        (_market_data(regime_timeframes_seconds=[0]), "greater_than"),
        (_market_data(regime_timeframes_seconds=[60, 60]), "duplicate_timeframe"),
        (_market_data(regime_timeframes_seconds=[2**63]), "less_than_equal"),
        (_market_data(unexpected=1), "extra_forbidden"),
    ],
)
@pytest.mark.req("MIG-034")
def test_each_rule_on_venues_and_timeframes_refuses(
    document: str, refusal: str
) -> None:
    with pytest.raises(ContractError) as error:
        MarketDataSettings.from_json(document)
    assert _types(error) == [refusal]


@pytest.mark.parametrize(
    ("changes", "refusal"),
    [
        ({"maker": "-1"}, "greater_than"),
        ({"maker": "1"}, "less_than"),
        ({"taker": "-0.0001"}, "greater_than_equal"),
        ({"taker": "1"}, "less_than"),
        ({"maker": 0.001}, "amount_type"),
        ({"source": ""}, "string_pattern_mismatch"),
        ({"source": "a\nb"}, "string_pattern_mismatch"),
        ({"source": "x" * 301}, "string_pattern_mismatch"),
        ({"as_of": "2026-1-7"}, "string_pattern_mismatch"),
        ({"as_of": "2026-02-30"}, "date_invalid"),
    ],
)
@pytest.mark.req("MIG-034")
def test_each_rule_on_a_fee_schedule_refuses(
    changes: dict[str, object], refusal: str
) -> None:
    with pytest.raises(ContractError) as error:
        MarketDataSettings.from_json(_fee(**changes))
    assert _types(error) == [refusal]


@pytest.mark.req("MIG-034")
def test_a_maker_rebate_is_accepted() -> None:
    (venue,) = MarketDataSettings.from_json(_fee(maker="-0.0001")).venues
    assert str(venue.fees[0].maker) == "-0.0001"


@pytest.mark.parametrize(
    ("changes", "refusal"),
    [
        ({"database": {**DATABASE, "host": "db_1.example"}}, "string_pattern_mismatch"),
        ({"database": {**DATABASE, "host": "-db.example"}}, "string_pattern_mismatch"),
        ({"database": {**DATABASE, "port": 0}}, "greater_than_equal"),
        ({"database": {**DATABASE, "port": 65536}}, "less_than_equal"),
        ({"database": {**DATABASE, "name": "ATP"}}, "string_pattern_mismatch"),
        ({"database": {**DATABASE, "user": "a" * 64}}, "string_pattern_mismatch"),
        (
            {"database": {**DATABASE, "password_secret": "atp_db"}},
            "string_pattern_mismatch",
        ),
        ({"database": {**DATABASE, "password": "x"}}, "extra_forbidden"),
        ({"archive_directory": "srv/atp/archive"}, "string_pattern_mismatch"),
        ({"archive_directory": "/srv/atp\n"}, "string_pattern_mismatch"),
    ],
)
@pytest.mark.req("MIG-034")
def test_each_rule_on_the_database_and_archive_refuses(
    changes: dict[str, object], refusal: str
) -> None:
    with pytest.raises(ContractError) as error:
        EnvironmentConfiguration.from_json(_environment(**changes))
    assert _types(error) == [refusal]


@pytest.mark.parametrize(
    "secrets",
    [[], [{"name": "ATP_DB", "kind": "ai"}], [{"name": "ATP_OTHER", "kind": "server"}]],
)
@pytest.mark.req("SEC-005", "MIG-034")
def test_the_database_password_is_a_declared_server_secret(
    secrets: list[dict[str, str]],
) -> None:
    with pytest.raises(ContractError) as error:
        EnvironmentConfiguration.from_json(_environment(secrets=secrets))
    assert _types(error) == ["database_secret_undeclared"]


@pytest.mark.req("SEC-005", "MIG-034")
def test_a_refused_secret_declaration_beside_a_database_is_reported_as_itself() -> None:
    # The database's check leaves secrets that were refused to their own refusal.
    declaration = {"name": "atp_db", "kind": "server"}
    with pytest.raises(ContractError) as error:
        EnvironmentConfiguration.from_json(_environment(secrets=[declaration]))
    assert [(detail.location, detail.type) for detail in error.value.details] == [
        (("secrets", 0, "name"), "string_pattern_mismatch")
    ]


@pytest.mark.req("MIG-010")
def test_an_amount_written_as_a_toml_number_is_refused() -> None:
    document = (
        "[[venues]]\n"
        'venue = "example"\n'
        'instrument_types = ["spot"]\n'
        "[[venues.fees]]\n"
        'instrument_type = "spot"\n'
        "maker = 0.001\n"
        'taker = "0.001"\n'
        'source = "The venue\'s published fee schedule"\n'
        'as_of = "2026-11-17"\n'
    )
    with pytest.raises(ConfigurationError, match="an amount is written as a string"):
        read_toml(MarketDataSettings, document, "platform.toml")


@pytest.mark.req("MIG-010", "MIG-034", "SEC-005")
def test_the_summary_shows_the_stage_2_settings_and_no_secret_value(
    tmp_path: Path,
) -> None:
    (tmp_path / "environments").mkdir()
    (tmp_path / "platform.toml").write_text(
        'platform_id = "atp"\n'
        "[market_data]\n"
        "regime_timeframes_seconds = [3600, 86400]\n"
        "[[market_data.venues]]\n"
        'venue = "example"\n'
        'instrument_types = ["spot"]\n'
        "[[market_data.venues.fees]]\n"
        'instrument_type = "spot"\n'
        'maker = "0.0008"\n'
        'taker = "0.001"\n'
        'source = "Example fee schedule"\n'
        'as_of = "2026-11-17"\n',
        encoding="utf-8",
    )
    (tmp_path / "environments" / "paper.toml").write_text(
        'environment = "paper"\n'
        'environment_id = "example-paper"\n'
        'archive_directory = "/srv/atp/archive"\n'
        "[[secrets]]\n"
        'name = "ATP_DB"\n'
        'kind = "server"\n'
        "[database]\n"
        'host = "db.example.invalid"\n'
        "port = 5432\n"
        'name = "atp"\n'
        'user = "atp"\n'
        'password_secret = "ATP_DB"\n',
        encoding="utf-8",
    )
    secret = "pw" + "-Q7x9Z2-" + "value"
    configuration = load_configuration(
        tmp_path, "paper", ProcessEnvironment({"ATP_DB": secret})
    )
    lines = summary(configuration)
    assert lines[:8] == [
        "platform_id: atp",
        "venue example: public market data for spot",
        (
            "venue example fees for spot: maker 0.0008, taker 0.001 "
            "(Example fee schedule, as of 2026-11-17)"
        ),
        "regime timeframes (seconds): 3600, 86400",
        "environment: paper",
        "environment_id: example-paper",
        "database: atp@db.example.invalid:5432/atp, password from the secret ATP_DB",
        "archive directory: /srv/atp/archive",
    ]
    assert all(secret not in line for line in lines)
