# The code performs pairwise comparisons also known as contrasts in DESEQ2 for different number of samples
# For example if you have 3 samples: A,B,C, it will perform contrast between A vs B, A vs C, and B vs C
# The output will contain CSV files, named as per the samples compared, separated by "_"
# NOTE: A positive log2FoldChange in a file "A_B_.csv" means the gene is overexpressed in sample A
# To run the script type: Rscript scriptname.R args[1] args[2] args[3]
# args[1]: CSV file containing gene count matrix
# args[2]: CSV file containing sample information table
# args[3]: Column header from args[2] file, to be used for sample information

args = commandArgs(trailingOnly=TRUE)

# Perfoming basic DESEQ2 operations

library (DESeq2)
counts <- read.csv(args[1])
info <- read.csv(args[2])
dds <- DESeqDataSetFromMatrix(countData=counts, colData=info,design=formula(paste("~",args[3])), tidy = TRUE)
dds <- DESeq(dds)

# Putting samples into lists

sample_info_column <- info[,args[3]]
sample_definition <- unique(sample_info_column)
sample_length <- length(sample_definition)
number_of_samples <- c(sample_length:1)

# Looping through different samples to perform pairwise comparisons

for ( i in sample_definition) {
  for ( j in number_of_samples){
        if (i==sample_definition[j]){break}
        else {con <- results(dds, contrast = c(args[3],i,sample_definition[j]))
        write.csv(con, file = paste(i,sample_definition[j],".csv", sep="_"))}}}

