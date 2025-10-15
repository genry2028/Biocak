from pathlib import Path
import os.path
from typing import Union, Tuple, Dict, Callable
from moduls.dna_rna_modul import (
    is_nucleic_acid,
    transcribe,
    reverse,
    complement,
    reverse_complement,
)
from moduls.filter_fastq_module import read_verification

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
    input_fastq: str,
    gc_bounds: Bounds = (0, 100),
    length_bounds: Bounds = (0, 2**32),
    quality_threshold: Union[int, float] = 0,
    output_fastq: str = "",
) -> Reads:
    """Filtering  FASTQ reads by specified parameters

    Args:
        input_fastq (str): path to input fastq file to filter.
        gc_bounds (Bounds, optional): interval for GC content. Defaults to (0, 100).
        length_bounds (Bounds, optional): interval for length of read. Defaults to (0, 2**32).
        quality_threshold (Union[int, float], optional): average read quality threshold. Defaults to 0.
        out_fastq (str): path to file for filtered fastq reads.

    Raises:
        Raises exception if input file not found.
    """
    if not os.path.isfile(input_fastq):
        raise FileNotFoundError(f"{input_fastq} file not found!")
    if not output_fastq:
        output_fastq = os.path.join(
            os.path.dirname(input_fastq),
            Path("output_" + os.path.basename(input_fastq)),
        )
    with open(input_fastq, "r") as input, open(output_fastq, "w") as output:
        current_read = []
        for line in input:
            if len(current_read) == 4:
                seq, quality = current_read[1], current_read[3]
                if read_verification(
                    seq, quality, gc_bounds, length_bounds, quality_threshold
                ):
                    output.write("".join(current_read))
                current_read = []
            current_read.append(line)
