import collections


def gc_filter(seq):
    content = collections.Counter(seq.upper())
    return (content.get("G", 0) + content.get("C", 0)) / len(seq) * 100


def length_filter(seq):
    return len(seq)


def quality_filter(quality):
    content_quality = collections.Counter(quality)
    score = 0
    for symbol, number in content_quality.items():
        score += (ord(symbol) - 33) * number / len(quality)
    return score


def is_seq_validate(seq, quality, gc_bounds, length_bounds, quality_threshold):
    if gc_filter(seq) >= gc_bounds[1] or gc_filter(seq) <= gc_bounds[0]:
        return False
    if length_filter(seq) >= length_bounds[1] or length_filter(seq) <= length_bounds[0]:
        return False
    if quality_filter(quality) < quality_threshold:
        return False
    return True
