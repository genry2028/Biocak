from moduls.dna_rna_modul import (
    is_nucleic_acid,
    transcribe,
    reverse,
    complement,
    reverse_complement,
)
from moduls.filter_fastq_module import is_seq_validate

OPERATION = {
    "is_nucleic_acid": is_nucleic_acid,
    "transcribe": transcribe,
    "reverse": reverse,
    "complement": complement,
    "reverse_complement": reverse_complement,
}


def run_dna_rna_tools(*args: str):
    if len(args) <= 1:
        raise KeyError(f"False input: {args}")
    *seqs, operation = args
    result = []
    if operation not in OPERATION.keys():
        raise KeyError(f"Unknown operation: {operation}")
    try:
        for seq in seqs[: len(seqs)]:
            if operation == "is_nucleic_acid":
                result.append(OPERATION[operation](seq))
            else:
                if is_nucleic_acid(seq):
                    result.append(OPERATION[operation](seq))
                else:
                    print(f"Sequence {seq} not is nucleotide acid")
                    result.append(None)
    except Exception:
        print(f"Processing error: {Exception}")
    if len(result) == 1:
        return result[0]
    return result


def filter_fastq(
    reads, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0
):
    if not reads:
        raise KeyError("Input is empty!")
    if type(gc_bounds) is not tuple:
        gc_bounds = (0, gc_bounds)
    if type(length_bounds) is not tuple:
        length_bounds = (0, length_bounds)
    seqs_filtered = {}
    for name, read in reads.items():
        seq, quality = read[0], read[1]
        if is_seq_validate(seq, quality, gc_bounds, length_bounds, quality_threshold):
            seqs_filtered[name] = read
    return seqs_filtered
