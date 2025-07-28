# How to use the GWAS SNP dataset in TASSEL?

The PLINK files available from the Downloads page are in "binary PLINK" format (`bed`, `bim`, `fam`).  
To use with TASSEL, one needs a "text PLINK" format (`ped`, `map`).

Here is how to do it on Windows:

1. Download PLINK 1.90 from https://www.cog-genomics.org/plink2/ (choose for your OS).
2. Unpack the archive.
3. Create a folder on your desktop named `plinkdata`
4. Put `plink.exe` and the dataset into this folder. Example dataset files:
   - `pruned_v2.1.bed`
   - `pruned_v2.1.bim`
   - `pruned_v2.1.fam`
5. Open PowerShell and run:

```powershell
cd Desktop
cd plinkdata
ls
.\plink --bfile pruned_v2.1 --recode tab --out 1Mdata