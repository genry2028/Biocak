from biocak import Nucleotide
from typing import Optional


STANDART_DEOXYRIBONUCLEOTIDES: Nucleotide = {"A", "C", "G", "T", "a", "c", "g", "t"}
STANDART_RIBONUCLEOTIDES: Nucleotide = {"A", "C", "G", "U", "a", "c", "g", "u"}
COMPLEMENT_DNA: Nucleotide = {
    "A": "T",
    "a": "t",
    "G": "C",
    "g": "c",
    "C": "G",
    "c": "g",
    "T": "A",
    "t": "a",
}
COMPLEMENT_RNA: Nucleotide = {
    "A": "U",
    "a": "u",
    "G": "C",
    "g": "c",
    "C": "G",
    "c": "g",
    "U": "A",
    "u": "a",
}


def is_dna(seq: str) -> bool:
    """Checking if a DNA sequence is

    Args:
        seq (str): nucleotide acide sequence

    Returns:
        bool: True, if sequence is DNA
              False, if sequence is not DNA
    """
    return set(seq) <= STANDART_DEOXYRIBONUCLEOTIDES


def is_rna(seq: str) -> bool:
    """Checking if a RNA sequence is

    Args:
        seq (str): nucleotide acide sequence

    Returns:
        bool: True, if sequence is RNA
              False, if sequence is not RNA
    """
    return set(seq) <= STANDART_RIBONUCLEOTIDES


def is_nucleic_acid(seq: str) -> bool:
    """Checking if a nucleotide acide (NA) sequence is

    Args:
        seq (str): nucleotide acide sequence

    Returns:
        bool: True, if sequence is NA
              False, if sequence is not NA
    """
    return is_dna(seq) or is_rna(seq)


def transcribe(seq: str) -> Optional[str]:
    """Transcribes DNA sequence to RNA sequence

    Args:
        seq (str): nucleotide acide sequence

    Returns:
        str: if seq is DNA, returns RNA sequence, else - None
    """
    if is_dna(seq):
        return seq.replace("T", "U").replace("t", "u")
    return


def reverse(seq: str) -> str:
    """Get reverse nucleotide acide sequence

    Args:
        seq (str): nucleotide acide sequence

    Returns:
        str: reverse nucleotide acide sequence
    """
    return seq[::-1]


def complement(seq: str) -> str:
    """Get a complementary sequence

    Args:
        seq (str): nucleotide acide sequence

    Returns:
        str: complementary nucleotide acide sequence
    """
    if is_rna(seq):
        complement_seq = "".join([COMPLEMENT_RNA[nucleotide] for nucleotide in seq])
    if is_dna(seq):
        complement_seq = "".join([COMPLEMENT_DNA[nucleotide] for nucleotide in seq])
    return complement_seq


def reverse_complement(seq: str) -> str:
    """Get a reverse complementary sequence

    Args:
        seq (str): nucleotide acide sequence

    Returns:
        str: reverse complementary nucleotide acide sequence
    """
    return reverse(complement(seq))
