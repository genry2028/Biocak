import sys 
from typing import Union, Tuple, Dict, Callable
from moduls.dna_rna_modul import (
    is_nucleic_acid,
    transcribe,
    reverse,
    complement,
    reverse_complement,
)
from moduls.filter_fastq_module import is_seq_valid

type NumericTuple = Tuple[Union[int, float], Union[int, float]]
type Bounds = Union[NumericTuple, int, float]
type Reads = Dict[str, Tuple[str, str]]
type Nucleotide = Dict[str, str]

OPERATION: Dict[str, Callable[[str], Union[list[str], str]]] = {
    "is_nucleic_acid": is_nucleic_acid,
    "transcribe": transcribe,
    "reverse": reverse,
    "complement": complement,
    "reverse_complement": reverse_complement,
}


def run_dna_rna_tools(*args: str) -> Union[list[str], str]:
    """Nuceic acid processing

    Args:
        Any number of DNA/RNA sequences and type of operation.

    Raises:
        KeyError: if length of input is less than 1
        KeyError: if the operation type is not included in the list of acceptable

    Returns:
        List with modifated sequences, if number of sequences input is greater than 1
        String with modifated sequence, if number of sequences input is 1
    """
    if len(args[0]) <= 1:
        raise KeyError(f"False input: {args}")
    *_, args = args
    *seqs, operation = args
    result: list[str] = []
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
                    print(f"Sequence {seq} is not nucleotide acid")
                    result.append(None)
    except Exception:
        print(f"Processing error: {Exception}")
    if len(result) == 1:
        return result[0]
    return result


def filter_fastq(
    reads: Reads,
    gc_bounds: Bounds = (0, 100),
    length_bounds: Bounds = (0, 2**32),
    quality_threshold: Union[int, float] = 0,
) -> Reads:
    """filtering  FASTQ reads by specified parameters

    Args:
        reads (Reads): dict whit nucleotide sequences and quality.
        gc_bounds (Bounds, optional): interval for GC content. Defaults to (0, 100).
        length_bounds (Bounds, optional): interval for length of read. Defaults to (0, 2**32).
        quality_threshold (Union[int, float], optional): average read quality threshold. Defaults to 0.

    Raises:
        Raises exception if input dict (reads) is empty.

    Returns:
        Dict with filtered sequences.
    """
    if not reads:
        raise KeyError("Input reads is empty!")
    if type(gc_bounds) is not tuple:
        gc_bounds = (0, gc_bounds)
    if type(length_bounds) is not tuple:
        length_bounds = (0, length_bounds)
    seqs_filtered: Reads = {}
    for name, read in reads.items():
        seq, quality = read[0], read[1]
        if is_seq_valid(seq, quality, gc_bounds, length_bounds, quality_threshold):
            seqs_filtered[name] = read
    return seqs_filtered


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        print("Не передано название метода. Пример: python main.py function arg1 arg2")
        exit(1)
    func = args[0] # функция (filter_fastq, run_dna_rna_tools)
    # Передаваемые к ней аргументы записываются в переменную func_args
    func_args = args[1:]
    # result = globals()["run_dna_rna_tools"]("ATTG", "AAyya", "Atguc", "aaugc", "is_nucleic_acid")
    result = globals()[func](func_args)
    print(result)
