# Why did my dataset go missing?

We used to provide SNP data for 4 lower-quality references (93-11, Kasalath, IR 64, DJ123).

One problem with that data was that the SNPs were not exhaustive, but incremental relative to other dataset. So that when you need to find all SNPs for a region in 93-11, you would first need to get all SNPs from all aligning subregions in Nipponbare, then get the 93-11 SNPs. We realize this is suboptimal, and adds extra burden on researchers.

As new higher quality references become available, we are preparing new SNP datasets for 3,010 genomes aligned to those references. These will replace the data that was removed. Stay tuned.

If you really need SNP data for the previous references, the original single-sample VCF files are available on Amazon Web Services public 3k dataset.