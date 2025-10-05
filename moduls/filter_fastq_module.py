import collections
from typing import Union, Counter, Tuple

type NumericTuple = Tuple[Union[int, float], Union[int, float]]


def get_gc_content(seq: str) -> Union[int, float]:
    """Calculates the GС content as a percentage

    Args:
        seq (str): nucleotide acide sequence

    Returns:
        Union[int, float]: GС content in percent
    """
    content: Counter[str] = collections.Counter(seq.upper())
    return (content.get("G", 0) + content.get("C", 0)) / len(seq) * 100


def get_quality(quality: str) -> Union[int, float]:
    """Сalculates the average quality of the read

    Args:
        quality (str): quality sequence

    Returns:
        Union[int, float]: quality value
    """
    content_quality: Counter[str] = collections.Counter(quality)
    score: Union[int, float] = 0
    for symbol, number in content_quality.items():
        score += (ord(symbol) - 33) * number / len(quality)
    return score


def is_seq_valid(
    seq: str,
    quality: str,
    gc_bounds: NumericTuple,
    length_bounds: NumericTuple,
    quality_threshold: Union[int, float],
) -> bool:
    """Checks if the read is valid according to all filtering parameters

    Returns:
        bool: True, if read is valid
              False, if read is invalid
    """
    if get_gc_content(seq) > gc_bounds[1] or get_gc_content(seq) < gc_bounds[0]:
        return False
    if len(seq) > length_bounds[1] or len(seq) < length_bounds[0]:
        return False
    if get_quality(quality) < quality_threshold:
        return False
    return True
