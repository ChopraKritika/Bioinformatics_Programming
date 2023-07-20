# This script reads all the pairwise comparison or contrast files from DESEQ2 and help visualize the up-regulated genes from all the comparisons as 0 and 1 matrix
# A value of "1" for a particular gene for the stated comparison means the gene is up-regulated at specified threshold in the reference sample whereas "0" means it doesn't meet the threshold requirements for the sample
# To run the script type: python scriptname.py sys.argv[1] sys.argv[2]
# sys.argv[1]: specifies the threshold value for log2Foldchange, greater than or equal to that the gene will be considered up-regulated
# sys.argv[2]: specifies the threshold value for pvalue, less than that the genes will be considered for their expression 

import os
import sys
import glob
path = os.getcwd()
allFiles = glob.glob(path + "/*_.csv") #"_.csv" can be replaced acc to your file naming
list = []
df2 = pd.DataFrame()
arr1 = []
for file_ in allFiles:
    file_name = file_.replace(path , "").replace("\\" , "").replace(".csv" , "") #"\\" can be substituted with single forward or backward slash or any other symbol, based on the path and filename etc.
    list.append(file_name)
    print(file_)
    df = pd.read_csv(file_)
    for i in df.index:
        if df.iloc[i,2]>=float(sys.argv[1]) and df.iloc[i,6]<float(sys.argv[2]):
            arr1.append("1")

        else:
            arr1.append("0")

    df2[file_name] = arr1
    arr1 = []
    df2.set_index([df.iloc[:,0]], inplace=True)

df2.to_csv("output.csv")
print(df2)

