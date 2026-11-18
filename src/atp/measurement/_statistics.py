"""Exact statistics of measured samples (U3 of the Stage 2 plan; PERF-010).

Every figure is one of the samples, or the difference of two, so it is exact: a percentile is
the nearest-rank percentile (the smallest sample with at least that share of the samples at or
below it), computed on integers only. This module divides only integers, to find a rank, and is
listed for that in the structure test's `INTEGER_DIVISION_ALLOWED` (numerical policy, N4); it
refuses any value that is not a whole number, so it never divides or converts an amount.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from itertools import pairwise
from typing import Final

PERCENTILES: Final = (("p50", 500), ("p95", 950), ("p99", 990), ("p99.9", 999))
"""The percentiles of PERF-010, in thousandths."""


@dataclass(frozen=True, slots=True)
class Summary:
    """A distribution's size, its percentiles, and its maximum. A figure the samples are too few
    for is `None`, reported as "insufficient": a percentile needs at least one sample beyond it,
    so p50 needs 2 samples, p95 20, p99 100, and p99.9 1,000; the maximum needs one."""

    count: int
    p50: int | None
    p95: int | None
    p99: int | None
    p99_9: int | None
    maximum: int | None


@dataclass(frozen=True, slots=True)
class Statistics:
    """The statistics of one point's samples, in the order they were recorded: the samples'
    distribution, and their jitter, the distribution of the absolute differences between
    consecutive samples (the delay variation of RFC 3393)."""

    samples: Summary
    jitter: Summary


def percentile(ordered: Sequence[int], thousandths: int) -> int | None:
    """The nearest-rank percentile of sorted samples, or `None` when they are too few."""
    count = len(ordered)
    if type(thousandths) is not int or not 0 < thousandths < 1000:
        msg = "a percentile is between 0 and 1,000 thousandths, both excluded"
        raise ValueError(msg)
    if count * (1000 - thousandths) < 1000:
        return None
    # The smallest rank r with r * 1000 >= thousandths * count: a ceiling, exact on integers.
    rank = -((-thousandths * count) // 1000)
    return ordered[rank - 1]


def summarize(values: Sequence[int]) -> Summary:
    """The summary of a sequence of whole numbers; anything else raises `TypeError`."""
    for value in values:
        if type(value) is not int:
            msg = "statistics are computed on whole numbers of nanoseconds only"
            raise TypeError(msg)
    ordered = sorted(values)
    figures = {name: percentile(ordered, share) for name, share in PERCENTILES}
    return Summary(
        count=len(ordered),
        p50=figures["p50"],
        p95=figures["p95"],
        p99=figures["p99"],
        p99_9=figures["p99.9"],
        maximum=ordered[-1] if ordered else None,
    )


def statistics_of(values: Sequence[int]) -> Statistics:
    """The statistics of one point's samples, given in the order they were recorded."""
    summary = summarize(values)
    differences = [abs(after - before) for before, after in pairwise(values)]
    return Statistics(summary, summarize(differences))
