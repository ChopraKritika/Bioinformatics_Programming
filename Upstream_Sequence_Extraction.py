#NOTE: This code extracts 1.5kb upstream sequence for a given gene

import pandas as pd
from Bio.SeqIO.FastaIO import SimpleFastaParser

upstream_output = open("Upstream_Extracted_Sequences.fasta", "w")

#NOTE: Your .bed file must contain headers

bedfile = pd.read_table("ENTER_YOUR_BED_FILE_NAME")
with open("ENTER_YOUR_FASTA_FILE_NAME") as fasta_file:
    for identifier, seq in SimpleFastaParser(fasta_file):
        for i in bedfile.index:
            if bedfile.iloc[i,0]==identifier:
                upstream_position = bedfile.iloc[i,1]-1500 
                if int(upstream_position) >= 0 and len(seq[int(upstream_position):int(bedfile.iloc[i,1])]) == 1500:
                    upstream_output.write(">" + str(bedfile.iloc[i,3]) + "  " + str(bedfile.iloc[i,0]) + "  " + str(upstream_position) + "  " + str(bedfile.iloc[i, 1]) + "\n")
                    upstream_output.write(seq[int(upstream_position):int(bedfile.iloc[i, 1])] + "\n")

upstream_output.close()




