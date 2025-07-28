# Locus Naming Convention

**Reference genomes gene locus names**

We used the gene models published with each of the genomes. These models use the name originally provided by their respective gene prediction/curation pipelines. To avoid displaying these cryptic names in the viewers and queries, we define a naming convention for rice gene models for any newly sequenced reference genome.

1.	Collect all gene (locus) features from the original source.
2.	Sort all loci by chromosome and start and end positions.
3.	Gene names start with “Os” for Oryza sativa, and the next five characters define the variety: “Nippo” (Nipponbare), “9311_” (93-11), “Kasal” (Kasalath), “DJ123” (DJ 123) and “IR64_” (IR 64).
4.	Assign chromosome or contig number:
a.	If there is chromosome assembly, the next 2 digits are the chromosome number (“01”-“12”).
b.	If there is no chromosome assembly, then the next 5 digits are the contig number. The contig number is a rank given to the contigs sorted by decreasing length, where the longest is assigned “00001”. If contigs are of the same length, they are sorted by the sequence in alphabetical order.
5.	The next character is “g”, which stands for genomic DNA.  Instead of “g”, it can be “m” for mitochondrial or “c” for chloroplast DNA.
6.	With genes sorted by start and then by end positions, the next 6 digits are the gene number in the chromosome or contig with an increment of 50. The first gene is assigned number “010050”, the second “010100”, the third “010150”, etc. Gene names in the chromosomes will be preserved in future versions of annotations. Gene names in scaffolds/contigs are for temporary use.
7.	Each locus is also referenced back to their original ID as provided by the source in the Dbxref attribute. If available, synonyms and Ontology terms (GO, PO, TO) are also added to the created locus in the Alias and Ontology term attributes.
8.	Alternatively spliced gene models or different versions of the same gene prediction are distinguished by a number added at the end of the gene after the dot. Here are some examples: “OsNippo01g210150.1”, “OsIR64_00342g210150.1”, “Os9311_11g210150.1”, “OsDJ12_00342g210150.1”.
9.	Each mRNA has its own list of features (CDS, exon, 3’-UTR and 5’-UTR) collected from the original annotation source, with descriptors following the transcript name.  The transcript name is followed by “:” (colon), then the feature type using Sequence Ontology terms (“cds”, “exon”, “five_prime_UTR”, “three_pime_UTR”), a “.” (dot), and the last two digits are the order number. Examples are:  “OsNippo01g210150.1:cds.01” and “Os9311_11g210150.2:exon.01”.

