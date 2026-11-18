"""Evidence identifiers (MKD-005; the Stage 2 plan's D5)."""

from __future__ import annotations

import hashlib
import json

import pytest

from atp.marketdata import EVIDENCE_FORM, MarketRef, Stream, Trade, evidence_id

SPOT = MarketRef.from_json(
    '{"venue":"example","base":"BTC","quote":"USDT","instrument_type":"spot"}'
)
PERPETUAL = MarketRef.from_json(
    '{"venue":"example","base":"BTC","quote":"USDT","instrument_type":"perpetual",'
    '"settle":"USDT"}'
)
BOOK = '{"bids":[["64000.01","0.5"]]}'
EVENT_TIME = 1_763_400_000_123_000_000


def _by_key(
    *,
    venue: str = "example",
    stream: Stream = Stream.TRADES,
    market: MarketRef | None = SPOT,
    venue_key: str | None = "5091223",
    content: str | None = None,
    event_time_ns: int | None = None,
) -> str:
    return evidence_id(
        venue=venue,
        stream=stream,
        market=market,
        venue_key=venue_key,
        content=content,
        event_time_ns=event_time_ns,
    )


def _by_content(*, content: str = BOOK, event_time_ns: int | None = EVENT_TIME) -> str:
    return evidence_id(
        venue="example",
        stream=Stream.BOOK,
        market=SPOT,
        content=content,
        event_time_ns=event_time_ns,
    )


@pytest.mark.req("MKD-005")
def test_the_same_item_gets_the_same_identifier_from_its_venue_key() -> None:
    assert _by_key() == _by_key()
    # The venue's key identifies the item; the time it is seen at does not.
    assert _by_key(event_time_ns=1) == _by_key(event_time_ns=2)


@pytest.mark.req("MKD-005")
def test_an_item_without_a_venue_key_gets_its_identifier_from_time_and_content() -> (
    None
):
    assert _by_content() == _by_content()
    assert _by_content(content='{"bids":[["64000.02","0.5"]]}') != _by_content()
    assert _by_content(event_time_ns=EVENT_TIME + 1) != _by_content()
    assert _by_content(event_time_ns=None) != _by_content()


@pytest.mark.req("MKD-005")
def test_each_identifying_part_changes_the_identifier() -> None:
    variants = [
        _by_key(venue="other"),
        _by_key(stream=Stream.TICKER),
        _by_key(market=PERPETUAL),
        _by_key(market=None),
        _by_key(venue_key="5091224"),
    ]
    assert _by_key() not in variants
    assert len(set(variants)) == len(variants)


@pytest.mark.req("MKD-005")
def test_a_venue_key_and_content_are_not_confused() -> None:
    assert _by_key(venue_key="5091223") != _by_key(venue_key=None, content="5091223")


def test_exactly_one_of_a_venue_key_and_content_is_given() -> None:
    with pytest.raises(ValueError, match="exactly one"):
        _by_key(content=BOOK)
    with pytest.raises(ValueError, match="exactly one"):
        _by_key(venue_key=None)
    with pytest.raises(ValueError, match="not empty"):
        _by_key(venue_key="")


@pytest.mark.req("MKD-005")
def test_the_identifier_is_the_documented_digest() -> None:
    form = json.dumps(
        [
            EVIDENCE_FORM,
            "example",
            "trades",
            ["spot", "BTC", "USDT", None],
            "key",
            "5091223",
        ],
        ensure_ascii=True,
        separators=(",", ":"),
    )
    assert _by_key() == hashlib.sha256(form.encode("ascii")).hexdigest()
    # Fixed when the form was written: a change to the form, or to how it is written, changes
    # every identifier, so it needs a new form version.
    assert EVIDENCE_FORM == "atp.evidence/1"
    assert (
        _by_key() == "858b4325c67dead1c328315e6d1e11d177880f729c929fd43328a54208b53792"
    )


@pytest.mark.req("MKD-005")
def test_an_identifier_is_a_valid_evidence_identifier_of_the_contracts() -> None:
    data = {
        "market": json.loads(SPOT.to_json()),
        "price": "64000.01",
        "quantity": "0.001",
        "receive_time_ns": EVENT_TIME,
        "evidence_id": _by_key(),
        "lineage": {
            "source": "ws trades",
            "adapter": "atp.exchange.example",
            "adapter_version": "1.0",
        },
    }
    assert Trade.from_json(json.dumps(data)).evidence_id == _by_key()
