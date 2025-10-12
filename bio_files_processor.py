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


def parse_blast_output(input_file, output_file=""):
    with open(input_file, "r") as blast_result, open(output_file, "w") as output_file:
        result=[]
        for line in blast_result:
            if "Sequences producing significant alignments:" in line:
                blast_result.readline()
                blast_result.readline()
                for line2 in blast_result:
                    if "Alignments" in line2:
                        break
                    x=re.match(r'^(.+?)(?=\s+[A-Z][a-z]+(?:\s+[a-z]+)*\s*\.\.\.)', line2)
                    if x:
                        x = x.group()
                        result.append(x+"\n")
        result.sort()
        print(result)
        print("".join(result))
        output_file.write("".join(result))
                    
                    
parse_blast_output("/Users/alisasenko/Desktop/HW_python/Biocak/example/example_blast_results.txt", 
                   "/Users/alisasenko/Desktop/HW_python/Biocak/example/out_example_blast_results.txt")