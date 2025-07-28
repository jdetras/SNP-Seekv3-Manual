# Steps in SNP Query

The SNP Query interface has two functionalities, to compare alleles between two specified varieties, and to compare multiple varieties with a reference genome. In both either case, the query region can be specified either by chromosomal region, by gene locus, or by a list of positions.

**Steps to query SNPs**


1.	Specifiy varieties
a.	To compare alleles between two varieties - in the two pairwise boxes, type or select from the drop-down list the varieties to compare. The text boxes have auto-completion feature so you only need to type the first few characters then select from the drop-down list. The choice items and recognized terms can be the variety name or accession based on the selected button at the right.
b.	To compare the reference with a subpopulation - select the subpopulation from the listbox. Some items in a choices is a group of more than one subpopulation, all indica (ind1,ind2,ind3,indx), all japonica (temp,trop,temp/trop,trop/temp) and  all varieties
c.	To compare reference with a list of varieties - select the variety list name in My Variety List, which are defined in My Lists.


2.	Specify genome region
a.	Select the Reference Genome - select among the five sequenced rice genomes to use as reference genome (Japonica Nipponbare, 93-11, IR64-21, DJ123, Kasalath). The chromosome/scaffold and gene locus selections depends on the selected reference genome.
b.	Check Show all reference alleles – to display the alleles of all 5 reference genomes for each SNP position. The alleles and position conversions between reference genomes are based on pairwise alignment results.
c.	To sepecify Chromosome/Scaffold region - select the chromosome/scaffold name, type the start and end base positions. Chromosome is avaiable when a fully assembled genome (Nipponbare, Kasalath) is selected, otherwise (IR64-21, DJ123) scaffold is used. 93-11 has both chromosomes and scaffolds.
d.	To specify Gene locus - type the Gene locus name in the text box. For Nipponbare, we are using the MSUv7 (LOC_OSXXgYYYYYY), RAP (OsXXgYYYYYY), and our merged MSUv71,RAP,FGenesh++ (OsNippoXXgYYYYYY) gene loci names described in NAR Supplementary Materials.  For the other 4 reference genomes, we are proposing a new locus naming convention also described below. The gene text box also has auto-completion feature. When a locus is selected, the chromosomal position boxes are automatically filled with the selected gene's region.
e.	To use a list of SNP positions, select the SNP List previously defined.
f.	To use a list of gene loci, select the Locus List previously defined.
g.	A genotype can be defined from a SNP List with allele value for each position. You can Match Genotype between this list and all varieties in the selected dataset. The resulting varieties are ranked by the number of matches with the SNP List. Instead of providing a SNP Liist, the genotype could be that of the selected Variety at the specified region.  


3.	Set options
a.	Include indels - include indels in the query
b.	Show phenotype - include the values of the selected phenotype in the results table
c.	Dataset - select the dataset to query (3kRGP, HDRA, both). If both is selected, there is addition option to use either the union or intersection of the SNP positions.
d.	SNP coloring determines the color of alleles as displayed in the table and in the Genome Browser. Options are:
i.	Reference mismatch – SNPs which have polymorphism with the reference are colored red, while the rest is white.
ii.	Nucleotide – SNPs are colored based on the base nucleotide: A green, T red, G orange, C blue. This follows the JBrowse color code.
e.	3k SNP Set - select the subset of the 3kRGP SNPs to query (All 32M, Base 18M, Filtered 4.8M, Core 400k). The subsetting criteria is described below.
f.	Mismatch Only -- if checked, only SNPs having allele mismatches are fetched in the pairwise comparison, or having mismatch with the reference in the multiple comparison.
g.	Include SNPs -- select to include/exclude/highlight Non-synonymous SNPs.
h.	Missing allele - specify how missing allele is to be counted (ignore means 0 match, 0 mismatch; or 0.5 match 0.5 mismatch)


1.	Search - to perform query and display the result in a Table, or view in JBrowse or a Tree
For queries above 50kb region, or 5000 SNPs, or 10 gene loci, the results are not displayed but available for download only.
Maximum allowed queries are 5Mb region, or 500k SNPs, or 1000 gene loci.


1.	Reset -  clear all input fields.

