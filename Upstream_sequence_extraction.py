# This code will help you extract the upstream sequences from the start site of the genes, for the specified number of basepairs
# The CSV file must contain column values with headers such as chromosome, start, gene_name in any order and case
# To run the code type: python scriptname.py upstreambasepair wholegenome.fasta CSVfile.csv  
# NOTE: if you want to extract 1.5kb upstream region enter 1500 as upstreambasepair

import pandas as pd
from Bio.SeqIO.FastaIO import SimpleFastaParser
import sys

upstream_output = open("upstream_sequences.fasta", "w")

genomefile = pd.read_csv(sys.argv[3])
genomefile.columns = genomefile.columns.str.lower()

with open(sys.argv[2]) as fasta_file:
    for identifier, seq in SimpleFastaParser(fasta_file):
        print(identifier)
        for i in genomefile.index:
            if genomefile.loc[i,"chromosome"]==identifier:
                upstream_position = genomefile.loc[i,"start"]-int(sys.argv[1])
                if int(upstream_position) >= 0 and len(seq[int(upstream_position):int(genomefile.loc[i,"start"])]) == int(sys.argv[1])
                    upstream_output.write(">" + str(genomefile.loc[i,"gene_name") + "  " + str(genomefile.loc[i,"chromosome"]) + "  " + str(upstream_position) + "  " + str(genomefile.loc[i,"start"]) + "\n")
                    upstream_output.write(seq[int(upstream_position):int(genomefile.loc[i,"start"])] + "\n")

upstream_output.close()


