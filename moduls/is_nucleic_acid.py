# from moduls.is_nucleic_acid  import STANDART_DEOXYRIBONUCLEOTIDES, STANDART_RIBONUCLEOTIDES
# from constants import STANDART_DEOXYRIBONUCLEOTIDES, STANDART_RIBONUCLEOTIDES

def is_dna(sequence):
    return set(sequence) <=  STANDART_DEOXYRIBONUCLEOTIDES


def is_rna(sequence):
    return set(sequence) <= STANDART_RIBONUCLEOTIDES


def is_nucleic_acid(sequence):
    return is_dna(sequence) or is_rna(sequence)