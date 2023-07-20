# This code identifies the Up-regulated genes from multiple files generated through pairwise comparisonsor say contrsts of multiple samples in DESEQ2
# The code read all the contrasts files and extract overexpressed genes at the specified threshold of log2Foldchange, pvalue and minimum number of comparisons in which the genes must be expressed 
# To run the script type: python scriptname.py sys.argv[1] sys.argv[2] sys.argv[3]
# sys.argv[1]: should be a positive number defining threshold for log2Foldchange
# sys.argv[2]: should be a number defining threshold for pvalue
# sys.argv[3]: should be a number defining minimum number of samples/contrasts in which your genes must be expressing. This should be equal to or less than the number of contrast files generated 
# An input like:"python Identify_DEGs_DESEQ2.py 2 0.01 15" means the script will yield the list of up-regulated genes at log2Foldchange >2, pvalue of <0.01 and expressing in atleast 15 samples
import pandas as pd
import sys
print ("Identifying Upregulated genes at log2 foldchange:",sys.argv[1],", pvalue:",sys.argv[2],"for",sys.argv[3],"number of comparisons")
import os
import glob
path = os.getcwd()
allFiles = glob.glob(path + "/*_.csv")
list = []
count = 0
gene_list = []
for file_ in allFiles:
    list.append(file_)
    print(file_)
    df = pd.read_csv(file_)
    for i in df.index:
        if df.iloc[i,2]>float(sys.argv[1]) and df.iloc[i,6]<float(sys.argv[2]):
            count += 1
            gene_list.append(df.iloc[i,0])

dup_genes = {}
for i in gene_list:
    dup_genes[i] = gene_list.count(i)

def filtering_function(pair):
    key, value = pair
    if value >= int(sys.argv[3]):
        return True  
    else:
        return False 

filtered_genes = dict(filter(filtering_function, dup_genes.items()))

fg_dataframe = pd.DataFrame.from_dict(filtered_genes, orient='index', columns=['number_of_contrasts'])
fg_dataframe.to_csv("Up_regulated_genes.csv")
print(len(fg_dataframe.index),"number of Up-regulated genes identified")
