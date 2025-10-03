STANDART_DEOXYRIBONUCLEOTIDES = {"A", "C", "G", "T", "a", "c", "g", "t"}
STANDART_RIBONUCLEOTIDES = {"A", "C", "G", "U", "a", "c", "g", "u"}
COMPLEMENT_DNA = {
    "A": "T",
    "a": "t",
    "G": "C",
    "g": "c",
    "C": "G",
    "c": "g",
    "T": "A",
    "t": "a",
}
COMPLEMENT_RNA = {
    "A": "U",
    "a": "u",
    "G": "C",
    "g": "c",
    "C": "G",
    "c": "g",
    "U": "A",
    "u": "a",
}


def is_dna(sequence):
    return set(sequence) <= STANDART_DEOXYRIBONUCLEOTIDES


def is_rna(sequence):
    return set(sequence) <= STANDART_RIBONUCLEOTIDES


def is_nucleic_acid(sequence):
    return is_dna(sequence) or is_rna(sequence)


def transcribe(sequence):
    return sequence.replace("T", "U").replace("t", "u")


def reverse(sequence):
    return sequence[::-1]


def complement_nucleic_acid(sequence, complement_nuc):
    return "".join([complement_nuc[nucleotide] for nucleotide in sequence])


def complement(sequence):
    if is_rna(sequence):
        complement_seq = "".join([COMPLEMENT_RNA[nucleotide] for nucleotide in sequence])
    if is_dna(sequence):
        complement_seq = "".join([COMPLEMENT_DNA[nucleotide] for nucleotide in sequence])
    return complement_seq


def reverse_complement(sequence):
    return reverse(complement(sequence))