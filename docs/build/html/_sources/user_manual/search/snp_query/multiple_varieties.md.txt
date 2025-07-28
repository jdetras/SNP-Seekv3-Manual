# Multiple varieties result

All Varieties result views

Several views are available for SNP query results:

**Table**  - this view displays the Alleles for each variety in a row, for all SNP positions within  the specified region or gene. The color is based on SNP coloring selected. The varieties are sorted by decreasing number of allele mismatches by default. The resulting table can be filtered using any of the column values, and sorted based on any column value by clicking  the column header.
To download the result, click the **CSV**, **Tab**, **Plink** or **Flapjack** button to get the given format.

At the bottom of the table is the plot showing the allele/genotype frequencies/counts for all SNP positions in the queried region.

**JBrowse** – the JBrowse genome browser lays out the SNP genotyping result in the SNP Genotyping track. Each variety is represented as a thin row in the track, and sorted in the same order as in the table. This track is dynamically generated from the query result, and covers only the queried region or locus. Zooming out from the initial region gives empty rows at both sides. To view a wider region, do a query again specifying the new wider region. Unlike in the Table view where results are displayed in several pages, Jbrowse displays all varieties having allele mismatch in the queried region at once.

**PhyloTree** -- Using the number of allele mismatches between varieties within the queried region or gene to compute for distance, the phylogenetic tree is constructed by Neighbor-Joining alorithm. Note that this operation takes some time (~5 minutes for a typical gene length).


**Compare genomes** -- Displays the alignment of the selected reference and region with the 4 other reference genomes in Vista.

**Alignment** – view the results in the familiar multiple sequence alignment format. But not that the positions here are not contiguous. It uses the JSAV library.