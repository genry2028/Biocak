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