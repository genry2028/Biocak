import os.path
from pathlib import Path
import re


def convert_multiline_fasta_to_oneline(input_file, output_file=""):
    if not output_file:
        output_file = os.path.join(os.path.dirname(input_file),
                                   Path("output_" + os.path.basename(input_file)))
    with open(input_file, "r") as fasta, open(output_file, "w") as fasta_out:
        line1 = fasta.readline()
        fasta_out.write(line1)
        for line in fasta:
            if line[0] == ">":
                fasta_out.write("\n"+line)
                continue
            fasta_out.write(line.strip())


convert_multiline_fasta_to_oneline("/Users/alisasenko/Desktop/HW_python/Biocak/example/example_multiline_fasta.fasta")

