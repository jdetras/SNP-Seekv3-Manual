# What exactly am I downloading when I use Sequence Download Feature?

The FASTA formatted file you get from this tool is what may be called a "pseudo-sequence"; it is a result of *in silico* replacing reference bases at variant positions with the variant bases found in VCF. It is not a biologically validated sequence, and in many cases it won't be faithful to the actual DNA sequence. One reason for that is that the SNPs present in the VCFs do not exhaust all sequence variants - the indels and larger structural variants are all missing from this.

If your region under study is longer than, say 150 nt, there is a very high chance that in the 3000 samples there are variants in this region missing from VCFs and unaccounted for in this tool.

Thus, proceed with caution, and do not expect this output to represent actual DNA data of varieties. The output may be acceptable for some population-genetic analyses that are tolerant to some degree of omission, but it is not guaranteed to work for analyses requiring precise sequence such as primer design.