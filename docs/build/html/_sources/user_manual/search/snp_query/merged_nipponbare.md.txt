# Merged Nipponbare gene models

Four major annotations for Nipponbare – MSU v7 (16), RAP-representative, RAP-predicted (17) and Fgenesh++ (18) – were added as tracks in JBrowse (https://snp-seek.irri.org/_jbrowse.zul). To facilitate curating results, we merged these four annotations into one set of loci. Having a single set of loci simplifies query and analysis of genome and variant features, like non-synonymous SNPs. 

The strategy for merging gene loci is:
1.	Collect all gene (locus) features from all 4 annotations.
2.	Sort all loci by chromosome and by start and end positions.
3.	Determine loci that have at least 50% overlap for the coding region (CDS) and merge those from the same strand into a common, new locus.
4.	The merged locus is named using the convention described in Supplement II with the form OsNippo{YY}g{NNNNNN}, where YY is the chromosome number (01-12), and NNNNNN is the locus count for the chromosome, starting from 10050, with increment of 50. Each locus is also referenced back to their original ID using the Dbxref attribute. Synonyms and Ontology terms (GO, PO, TO) collected from Oryzabase (21) are also added to the created locus in the Alias and Ontology term attributes. These synonyms and ontology attributes are loaded in the CHADO database. The gene function from MSU7 is used for the merged locus, unless it is ‘hypothetical’, ‘unknown’, or ‘expressed’.  For these cases, the functional annotation from RAP is used.
