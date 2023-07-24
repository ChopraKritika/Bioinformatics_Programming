# This code reads all the contrast or pairwise comparison files generated through DESEQ2 and extracts the log2Foldchange values for the specific list of up-regulated genes 
# This code can be further manilupated to extract similar type of values from different files for a prticular list of common column values
# The code will produce an output with first column of gene ids of specified upregulated genes and subsequent columns of their log2Foldchange values from all the files of pairwise comparisons 
import pandas as pd
import os
import glob
path = os.getcwd()
allFiles = glob.glob(path + "/*_.csv")
up_regulated_file = pd.read_csv("up_regulated_file.csv")
list = []

values = []
for i in up_regulated_file.index:
    values.append(up_regulated_file.iloc[i,0])

df3 = pd.DataFrame()

for file_ in allFiles:
    file_name = file_.replace(path , "").replace("/" , "").replace(".csv" , "")
    list.append(file_)
    print(file_)
    df = pd.read_csv(file_)
    df2 = df.query(f'`Unnamed: 0`=={values}')
    df3['gene_name'] = df2['Unnamed: 0'].values
    df3[file_name] = df2['log2FoldChange'].values
    
print (df3)
print(len(df2.index))
df3.to_csv("output.csv", index=False)
