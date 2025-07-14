# What does the output of this tool represent, actually?

The main goal of the haplotype viewer tool is to help visualize the structure and relationship between haplotypes at a locus.

What it does:

1. Cluster haplotypes in the region into "haplotype groups"
2. Visualize the genotypes, showing all genotypes from the same group together.
   - It does so in a way that can account for "whole-genome" relatedness that is based on subpopulation classification by admixture.
3. Output total number of varieties and that of each population, for each haplotype group cluster
4. Output some intermediate results useful for QC

What it does not:

1. Report all unique haplotypes in the region. (This task is easier, and may be done using the summary table itself)