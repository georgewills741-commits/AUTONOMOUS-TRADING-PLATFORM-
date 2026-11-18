"""Exact statistics of measured samples (PERF-010; the Stage 2 plan's U3)."""

from __future__ import annotations

import pytest
from hypothesis import given
from hypothesis import strategies as st

from atp.measurement import PERCENTILES, Summary, percentile, statistics_of, summarize
from atp.numeric import amount


@pytest.mark.req("PERF-010")
def test_known_samples_give_exact_figures() -> None:
    assert summarize(list(range(1000, 0, -1))) == Summary(
        count=1000, p50=500, p95=950, p99=990, p99_9=999, maximum=1000
    )
    assert summarize([5, 1, 3, 3, 9, 7, 7, 7, 2, 10]) == Summary(
        count=10, p50=5, p95=None, p99=None, p99_9=None, maximum=10
    )


@pytest.mark.parametrize(
    ("name", "too_few", "enough"),
    [("p50", 1, 2), ("p95", 19, 20), ("p99", 99, 100), ("p99.9", 999, 1000)],
)
@pytest.mark.req("PERF-010")
def test_a_percentile_needs_enough_samples(
    name: str, too_few: int, enough: int
) -> None:
    share = dict(PERCENTILES)[name]
    assert percentile(list(range(too_few)), share) is None
    # With just enough samples, one sample is beyond the percentile: it is the second
    # largest.
    assert percentile(list(range(enough)), share) == enough - 2


@pytest.mark.req("PERF-010")
def test_no_samples_give_no_figure() -> None:
    assert summarize([]) == Summary(
        count=0, p50=None, p95=None, p99=None, p99_9=None, maximum=None
    )
    assert summarize([42]).maximum == 42


@given(
    st.lists(
        st.integers(min_value=-(2**63), max_value=2**63 - 1), min_size=1, max_size=400
    )
)
@pytest.mark.req("PERF-010")
def test_each_percentile_is_the_nearest_rank(values: list[int]) -> None:
    ordered = sorted(values)
    count = len(values)
    for _name, share in PERCENTILES:
        figure = percentile(ordered, share)
        if count * (1000 - share) < 1000:
            assert figure is None
            continue
        assert figure in values
        # At least the share of the samples is at or below it, and less than the share below it.
        assert sum(value <= figure for value in values) * 1000 >= share * count
        assert sum(value < figure for value in values) * 1000 < share * count


@pytest.mark.req("PERF-010")
def test_jitter_is_the_distribution_of_differences_between_consecutive_samples() -> (
    None
):
    result = statistics_of([10, 13, 9, 9, 20])
    assert result.samples.maximum == 20
    assert result.jitter == Summary(
        count=4, p50=3, p95=None, p99=None, p99_9=None, maximum=11
    )
    assert statistics_of([7]).jitter.count == 0


@pytest.mark.parametrize("value", [amount("1.5"), 1.5, True, "1"])
@pytest.mark.req("TEC-003")
def test_only_whole_numbers_are_summarized_never_an_amount(value: object) -> None:
    with pytest.raises(TypeError, match="whole numbers"):
        summarize([1, value])  # type: ignore[list-item]


@pytest.mark.parametrize("share", [0, 1000, -1, 500.0, True])
def test_a_percentile_is_strictly_between_none_and_all(share: object) -> None:
    with pytest.raises(ValueError, match="thousandths"):
        percentile([1, 2, 3], share)  # type: ignore[arg-type]
