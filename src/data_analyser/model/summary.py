"""Compute statistical description of datasets."""

from typing import Any

from multimethod import multimethod
from tqdm import tqdm
from visions import VisionsTypeset

from data_analyser.config import Settings
from data_analyser.model.summarizer import BaseSummarizer


@multimethod
def describe_1d(
    config: Settings,
    series: Any,
    summarizer: BaseSummarizer,
    typeset: VisionsTypeset,
) -> dict:
    raise NotImplementedError()


@multimethod
def get_series_descriptions(
    config: Settings,
    df: Any,
    summarizer: BaseSummarizer,
    typeset: VisionsTypeset,
    pbar: tqdm,
) -> dict:
    raise NotImplementedError()
