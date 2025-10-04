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


def is_dna(seq):
    return set(seq) <= STANDART_DEOXYRIBONUCLEOTIDES


def is_rna(seq):
    return set(seq) <= STANDART_RIBONUCLEOTIDES


def is_nucleic_acid(seq):
    return is_dna(seq) or is_rna(seq)


def transcribe(seq):
    return seq.replace("T", "U").replace("t", "u")


def reverse(seq):
    return seq[::-1]


def complement_nucleic_acid(seq, complement_nuc):
    return "".join([complement_nuc[nucleotide] for nucleotide in seq])


def complement(seq):
    if is_rna(seq):
        complement_seq = "".join([COMPLEMENT_RNA[nucleotide] for nucleotide in seq])
    if is_dna(seq):
        complement_seq = "".join([COMPLEMENT_DNA[nucleotide] for nucleotide in seq])
    return complement_seq


def reverse_complement(seq):
    return reverse(complement(seq))
