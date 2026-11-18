"""The canonical market-data contracts (EXA-013, MKD-005, MKD-010, HLT-014; the Stage 2 plan's U2)."""

from __future__ import annotations

import json

import pytest

from atp.contracts import Contract, ContractError
from atp.marketdata import (
    BookSnapshot,
    BookUpdate,
    FundingRate,
    MarketMetadata,
    MarketRef,
    OhlcvBar,
    QualityAssessment,
    QuarantineCause,
    QuarantineRecord,
    Ticker,
    Trade,
    UntranslatableInput,
    VenueState,
)

EVIDENCE = "4f" * 32
LINEAGE = {
    "source": "GET /api/v1/ticker",
    "adapter": "atp.exchange.example",
    "adapter_version": "1.0",
}
SPOT = {"venue": "example", "base": "BTC", "quote": "USDT", "instrument_type": "spot"}
PERPETUAL = {
    "venue": "example",
    "base": "BTC",
    "quote": "USDT",
    "instrument_type": "perpetual",
    "settle": "USDT",
}
EVENT_TIME = 1_763_400_000_123_000_000
RECEIVE_TIME = 1_763_400_000_125_431_007


def _item(**fields: object) -> dict[str, object]:
    return {
        **fields,
        "event_time_ns": EVENT_TIME,
        "event_time_resolution": "millisecond",
        "receive_time_ns": RECEIVE_TIME,
        "evidence_id": EVIDENCE,
        "lineage": LINEAGE,
    }


VALID: dict[type[Contract], dict[str, object]] = {
    MarketMetadata: _item(
        market=SPOT,
        venue_symbol="BTCUSDT",
        status="trading",
        price_increment="0.01",
        quantity_increment="0.00001",
        minimum_quantity="0.00001",
        minimum_notional="5",
    ),
    Ticker: _item(
        market=SPOT,
        bid="64000.01",
        bid_size="0.5",
        ask="64000.02",
        ask_size="1.25",
        last="64000.01",
        base_volume_24h="12345.678",
    ),
    Trade: _item(
        market=SPOT,
        price="64000.01",
        quantity="0.001",
        taker_side="buy",
        venue_trade_id="5091223",
    ),
    BookSnapshot: _item(
        market=SPOT,
        bids=[{"price": "64000.01", "quantity": "0.5"}],
        asks=[{"price": "64000.02", "quantity": "1.25"}],
        sequence=1001,
    ),
    BookUpdate: _item(
        market=SPOT,
        bids=[{"price": "64000.01", "quantity": "0"}],
        asks=[],
        first_sequence=1002,
        last_sequence=1004,
        previous_sequence=1001,
    ),
    OhlcvBar: _item(
        market=SPOT,
        interval_seconds=60,
        open_time_ns=1_763_399_940_000_000_000,
        open="64010.5",
        high="64020",
        low="63990.25",
        close="64000.01",
        base_volume="12.5",
        quote_volume="800000.125",
        closed=True,
    ),
    FundingRate: _item(
        market=PERPETUAL,
        rate="0.0001",
        funding_time_ns=1_763_424_000_000_000_000,
        interval_seconds=28_800,
    ),
    VenueState: _item(venue="example", status="unavailable", cause="region-refused"),
    QualityAssessment: {
        "evidence_id": EVIDENCE,
        "assessed_time_ns": RECEIVE_TIME,
        "freshness": "valid",
        "age_ns": 2_431_007,
        "score": 100,
        "rule_version": "1.0",
    },
    QuarantineRecord: {
        "evidence_id": EVIDENCE,
        "venue": "example",
        "market": SPOT,
        "stream": "ticker",
        "cause": "impossible-price",
        "quarantined_time_ns": RECEIVE_TIME,
        "rule_version": "1.0",
    },
    UntranslatableInput: {
        "venue": "example",
        "stream": "ticker",
        "lineage": LINEAGE,
        "receive_time_ns": RECEIVE_TIME,
        "cause": "amount-not-text",
        "content_sha256": EVIDENCE,
        "content_length": 512,
    },
}

# Each contract's amounts, and where they are inside it.
AMOUNTS: dict[type[Contract], tuple[tuple[str | int, ...], ...]] = {
    MarketMetadata: (
        ("price_increment",),
        ("quantity_increment",),
        ("minimum_quantity",),
        ("minimum_notional",),
    ),
    Ticker: (("bid",), ("bid_size",), ("ask",), ("ask_size",), ("last",)),
    Trade: (("price",), ("quantity",)),
    BookSnapshot: (("bids", 0, "price"), ("asks", 0, "quantity")),
    BookUpdate: (("bids", 0, "price"), ("bids", 0, "quantity")),
    OhlcvBar: (("open",), ("high",), ("low",), ("close",), ("base_volume",)),
    FundingRate: (("rate",),),
}

# Each contract's times.
TIMES: dict[type[Contract], tuple[str, ...]] = {
    MarketMetadata: ("event_time_ns", "receive_time_ns"),
    Ticker: ("event_time_ns", "receive_time_ns"),
    Trade: ("event_time_ns", "receive_time_ns"),
    BookSnapshot: ("event_time_ns", "receive_time_ns"),
    BookUpdate: ("event_time_ns", "receive_time_ns"),
    OhlcvBar: ("open_time_ns", "event_time_ns", "receive_time_ns"),
    FundingRate: ("funding_time_ns", "event_time_ns", "receive_time_ns"),
    VenueState: ("event_time_ns", "receive_time_ns"),
    QualityAssessment: ("assessed_time_ns", "age_ns"),
    QuarantineRecord: ("quarantined_time_ns",),
    UntranslatableInput: ("receive_time_ns",),
}


def _with(data: dict[str, object], path: tuple[str | int, ...], value: object) -> str:
    """The data, as JSON, with the value at the path replaced."""
    copy = json.loads(json.dumps(data))
    target = copy
    for step in path[:-1]:
        target = target[step]
    target[path[-1]] = value
    return json.dumps(copy)


def _types(error: pytest.ExceptionInfo[ContractError]) -> list[str]:
    return [detail.type for detail in error.value.details]


@pytest.mark.parametrize("contract", list(VALID), ids=lambda c: c.__name__)
@pytest.mark.req("EXA-013")
def test_each_market_data_contract_reads_its_own_written_form(
    contract: type[Contract],
) -> None:
    item = contract.from_json(json.dumps(VALID[contract]))
    assert contract.from_json(item.to_json()) == item


@pytest.mark.parametrize("contract", list(VALID), ids=lambda c: c.__name__)
@pytest.mark.req("EXA-013")
def test_an_unknown_field_is_refused(contract: type[Contract]) -> None:
    with pytest.raises(ContractError) as error:
        contract.from_json(_with(VALID[contract], ("unexpected",), "x"))
    assert _types(error) == ["extra_forbidden"]


@pytest.mark.parametrize(
    ("contract", "path"),
    [(contract, path) for contract, paths in AMOUNTS.items() for path in paths],
    ids=lambda value: (
        value.__name__ if isinstance(value, type) else ".".join(map(str, value))
    ),
)
@pytest.mark.parametrize("number", [1, 0.5, 64000.01])
@pytest.mark.req("TEC-003", "EXA-013")
def test_an_amount_given_as_a_json_number_is_refused(
    contract: type[Contract], path: tuple[str | int, ...], number: float
) -> None:
    with pytest.raises(ContractError) as error:
        contract.from_json(_with(VALID[contract], path, number))
    assert _types(error) == ["amount_type"]


@pytest.mark.req("TEC-003", "EXA-013")
def test_an_amount_given_as_a_float_from_python_is_refused() -> None:
    valid = Trade.from_json(json.dumps(VALID[Trade]))
    data = {name: getattr(valid, name) for name in Trade.model_fields}
    assert Trade.from_python(data) == valid
    data["price"] = 64000.01
    with pytest.raises(ContractError) as error:
        Trade.from_python(data)
    assert _types(error) == ["amount_type"]


@pytest.mark.parametrize(
    ("contract", "field"),
    [(contract, field) for contract, fields in TIMES.items() for field in fields],
    ids=lambda value: value if isinstance(value, str) else value.__name__,
)
@pytest.mark.parametrize("bad", [-1, 2**63, 1.5, "1763400000123000000", True])
@pytest.mark.req("HLT-014")
def test_a_time_is_a_whole_number_of_nanoseconds_in_range(
    contract: type[Contract], field: str, bad: object
) -> None:
    with pytest.raises(ContractError):
        contract.from_json(_with(VALID[contract], (field,), bad))


@pytest.mark.req("HLT-014")
def test_the_largest_time_a_signed_64_bit_integer_holds_is_accepted() -> None:
    data = _with(VALID[Trade], ("receive_time_ns",), 2**63 - 1)
    assert Trade.from_json(data).receive_time_ns == 2**63 - 1


@pytest.mark.req("HLT-014")
def test_an_event_time_and_its_resolution_are_given_together() -> None:
    without_resolution = _with(VALID[Ticker], ("event_time_resolution",), None)
    without_time = _with(VALID[Ticker], ("event_time_ns",), None)
    with pytest.raises(ContractError) as error:
        Ticker.from_json(without_resolution)
    assert _types(error) == ["event_time_resolution"]
    with pytest.raises(ContractError) as error:
        Ticker.from_json(without_time)
    assert _types(error) == ["event_time_resolution"]
    neither = json.loads(without_time)
    neither["event_time_resolution"] = None
    assert Ticker.from_json(json.dumps(neither)).event_time_ns is None


@pytest.mark.req("HLT-014")
def test_a_refused_event_time_is_reported_as_itself() -> None:
    # The resolution's check leaves an event time that was refused to that time's own refusal.
    with pytest.raises(ContractError) as error:
        Ticker.from_json(_with(VALID[Ticker], ("event_time_ns",), -1))
    assert _types(error) == ["greater_than_equal"]


@pytest.mark.parametrize(
    ("path", "bad"),
    [
        (("market", "venue"), "Example"),
        (("market", "venue"), "ex ample"),
        (("market", "venue"), "-example"),
        (("market", "base"), "btc"),
        (("market", "base"), "BTC-USD"),
        (("market", "quote"), ""),
        (("market", "base"), "B" * 33),
        (("venue_trade_id",), "id\n1"),
    ],
)
@pytest.mark.req("EXA-013")
def test_a_malformed_market_identifier_is_refused(
    path: tuple[str, ...], bad: str
) -> None:
    with pytest.raises(ContractError) as error:
        Trade.from_json(_with(VALID[Trade], path, bad))
    assert _types(error) == ["string_pattern_mismatch"]


@pytest.mark.parametrize("bad", ["4F" * 32, "4f" * 31 + "4", "4f" * 33, "z" * 64, ""])
@pytest.mark.req("MKD-005")
def test_a_malformed_evidence_identifier_is_refused(bad: str) -> None:
    for contract, valid in VALID.items():
        field = "content_sha256" if contract is UntranslatableInput else "evidence_id"
        with pytest.raises(ContractError) as error:
            contract.from_json(_with(valid, (field,), bad))
        assert _types(error) == ["string_pattern_mismatch"]


@pytest.mark.parametrize(
    ("field", "bad"),
    [
        ("source", ""),
        ("source", "GET /xé"),
        ("adapter", "Atp.exchange"),
        ("adapter", "atp..exchange"),
        ("adapter_version", "1"),
        ("adapter_version", "01.0"),
        ("adapter_version", "1.0.0"),
    ],
)
@pytest.mark.req("MKD-010")
def test_malformed_lineage_is_refused(field: str, bad: str) -> None:
    with pytest.raises(ContractError) as error:
        Trade.from_json(_with(VALID[Trade], ("lineage", field), bad))
    assert _types(error) == ["string_pattern_mismatch"]


@pytest.mark.req("EXA-013")
def test_a_perpetual_names_its_settlement_asset_and_no_other_market_does() -> None:
    perpetual = MarketRef.from_json(json.dumps(PERPETUAL))
    assert perpetual.symbol() == "BTC/USDT:USDT"
    assert MarketRef.from_json(json.dumps(SPOT)).symbol() == "BTC/USDT"
    without_settle = {key: value for key, value in PERPETUAL.items() if key != "settle"}
    with pytest.raises(ContractError) as error:
        MarketRef.from_json(json.dumps(without_settle))
    assert _types(error) == ["settle_missing"]
    for kind in ("spot", "margin"):
        with pytest.raises(ContractError) as error:
            MarketRef.from_json(
                json.dumps({**SPOT, "instrument_type": kind, "settle": "USDT"})
            )
        assert _types(error) == ["settle_not_allowed"]


def test_a_book_update_does_not_end_before_it_begins() -> None:
    with pytest.raises(ContractError) as error:
        BookUpdate.from_json(_with(VALID[BookUpdate], ("last_sequence",), 1001))
    assert _types(error) == ["sequence_order"]
    single = _with(VALID[BookUpdate], ("last_sequence",), 1002)
    assert BookUpdate.from_json(single).last_sequence == 1002


@pytest.mark.parametrize(
    ("status", "cause", "refusal"),
    [
        ("unavailable", None, "cause_missing"),
        ("available", "timeout", "cause_not_allowed"),
        ("maintenance", "venue-error", "cause_not_allowed"),
        ("unknown", "rate-limited", "cause_not_allowed"),
    ],
)
def test_only_an_unavailable_venue_has_a_cause(
    status: str, cause: str | None, refusal: str
) -> None:
    data = json.loads(_with(VALID[VenueState], ("status",), status))
    data["cause"] = cause
    with pytest.raises(ContractError) as error:
        VenueState.from_json(json.dumps(data))
    assert _types(error) == [refusal]


@pytest.mark.parametrize("score", [-1, 101])
def test_a_quality_score_is_from_0_to_100(score: int) -> None:
    with pytest.raises(ContractError):
        QualityAssessment.from_json(_with(VALID[QualityAssessment], ("score",), score))


def test_the_quarantine_causes_are_those_of_mkd_013() -> None:
    assert [cause.value for cause in QuarantineCause] == [
        "invalid-timestamp",
        "missing-field",
        "impossible-price",
        "duplicate-event",
        "sequence-gap",
        "exchange-inconsistency",
        "outlier",
        "clock-problem",
    ]
