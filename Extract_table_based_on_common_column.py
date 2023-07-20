# The code extracts a table from a file based on the common column values from the other file
# For example: if you have two files as:
# File2:  col1  col2  col3
#         gene1	TF1   123
#	  gene2 TF2   234
#	  gene3 TF3   345
#	  gene4 TF4   456
#         gene5	TF5   567

# File1:  col1  col2  
#	  rna1  gene2
#	  rna2  gene4

# Now you want to obtain a table having row values from File2 corresponding to the col2 from File1 such as:
# Output: col1  col2  col3
#         gene2 TF2   234
#         gene4 TF4   456

# Based on above example, run the script as:"python scriptname.py File1.csv File2.csv col2 col1"

import pandas as pd
import sys

small_file = pd.read_csv(sys.argv[1])
big_file = pd.read_csv(sys.argv[2])

values = []
for i in small_file.index:
    values.append(small_file.loc[i,sys.argv[3]])

df = big_file[sys.argv[4]].isin(values)

big_file[df].to_csv("output.csv",index=False)
