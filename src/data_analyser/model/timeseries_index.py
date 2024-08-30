"""Compute statistical description of datasets."""

from typing import Any

from multimethod import multimethod

from data_analyser.config import Settings


@multimethod
def get_time_index_description(
    config: Settings,
    df: Any,
    table_stats: dict,
) -> dict:
    raise NotImplementedError()
