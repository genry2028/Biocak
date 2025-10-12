import os.path
from pathlib import Path
import re


def convert_multiline_fasta_to_oneline(input_file: str, output_file: str = "") -> None:
    """Сonverting multi-line fasta to single-line fasta

    Args:
        input_file (str): path to input fasta file.
        output_file (str, optional): path to output fasta file. Defaults to "".
    """
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"{input_file} file not found!")
    if not output_file:
        output_file = os.path.join(
            os.path.dirname(input_file), Path("output_" + os.path.basename(input_file))
        )
    with open(input_file, "r") as fasta, open(output_file, "w") as fasta_out:
        line1 = fasta.readline()
        fasta_out.write(line1)
        for line in fasta:
            if line[0] == ">":
                fasta_out.write("\n" + line)
                continue
            fasta_out.write(line.strip())


def parse_blast_output(input_file: str, output_file: str = "") -> None:
    """Selects proteins from the "Description" column

    Args:
        input_file (str): txt file from BLAST
        output_file (str, optional): path to output file. Defaults to "".
    """
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"{input_file} file not found!")
    if not output_file:
        output_file = os.path.join(
            os.path.dirname(input_file), Path("output_" + os.path.basename(input_file))
        )
    with open(input_file, "r") as blast_result, open(output_file, "w") as output_file:
        result: list = []
        for line in blast_result:
            if "Sequences producing significant alignments:" in line:
                blast_result.readline()
                blast_result.readline()
                for line2 in blast_result:
                    if "Alignments" in line2:
                        break
                    col1_line = re.match(
                        r"^(.+?)(?=\s+[A-Z][a-z]+(?:\s+[a-z]+)*\s*\.\.\.)", line2
                    )
                    if col1_line:
                        col1_line = col1_line.group()
                        result.append(col1_line + "\n")
        result.sort()
        output_file.write("".join(result))
