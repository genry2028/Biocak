import collections
from typing import Union, Counter, Tuple

type NumericTuple = Tuple[Union[int, float], Union[int, float]]
type Bounds = Union[NumericTuple, int, float]


def is_valid_gc_content(seq: str, gc_bounds: NumericTuple) -> bool:
    """Filters sequences by GС content as a percentage"""
    if type(gc_bounds) is not tuple:
        gc_bounds = (0, gc_bounds)
    content: Counter[str] = collections.Counter(seq.upper())
    gc_seq = (content.get("G", 0) + content.get("C", 0)) / len(seq) * 100
    return gc_bounds[0] <= gc_seq <= gc_bounds[1]


def is_valid_quality(quality: str, quality_threshold: Union[int, float]) -> bool:
    """Filters sequences by average quality"""
    content_quality: Counter[str] = collections.Counter(quality)
    score: Union[int, float] = 0
    for symbol, number in content_quality.items():
        score += (ord(symbol) - 33) * number / len(quality)
    return score > quality_threshold


def is_valid_length(seq: str, length_bounds: NumericTuple) -> bool:
    """Filters sequences by length"""
    if type(length_bounds) is not tuple:
        length_bounds = (0, length_bounds)
    return length_bounds[0] <= len(seq) <= length_bounds[1]


def read_verification(
    seq: str,
    quality: str,
    gc_bounds: Bounds,
    length_bounds: Bounds,
    quality_threshold: Union[int, float],
) -> bool:
    """Checks if the read is valid according to all filtering parameters

    Args:
        seq (str): nucleotide acid sequence
        quality (str): quality sequence of read
        gc_bounds (Bounds): interval for GC content
        length_bounds (Bounds): interval for length of read.
        quality_threshold (Union[int, float]): average read quality threshold.

    Returns:
        bool
    """
    return (
        is_valid_gc_content(seq, gc_bounds)
        and is_valid_quality(quality, quality_threshold)
        and is_valid_length(seq, length_bounds)
    )
