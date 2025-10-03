
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
    *sequences, operation = args
    result = []
    if operation not in OPERATION.keys():
        raise KeyError(f"Unknown operation: {operation}")
    try:
        for sequence in sequences[: len(sequences)]:
            if operation == "is_nucleic_acid":
                result.append(OPERATION[operation](sequence))
            else:
                if is_nucleic_acid(sequence):
                    result.append(OPERATION[operation](sequence))
                else:
                    print(f"Sequence {sequence} not is nucleotide acid")
                    result.append(None)
    except Exception as ae:
        print(f"Processing error: {ae}")
    if len(result) == 1:
        return result[0]
    return result