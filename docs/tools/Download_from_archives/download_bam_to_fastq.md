---
layout: default
title: Downloading 10x files from archives
parent: Download from archives
grand_parent: Tools
has_children: false
nav_order: 1
---
# Downloading 10x files from archives

These instructions are for getting BAM files of primary sequence data from the ENA that represent 10X sequencing data and converting them to the original I1, R1, and R2 files using the 10X `bamtofastq` tool. Please note that this tool only works for 10X data, and even then only for data processed with CellRanger and LongRagner. See the [10X website](https://support.10xgenomics.com/docs/bamtofastq) for more information about what data can be converted with this tool.

## Pre-requisites and installation

- wget
- bamtofastq

If you don't have `wget` installed on the machine where you want to download the files (it is on the EC2 already), you can find instructions how to install it with Homebrew for Mac [here](https://www.cyberciti.biz/faq/howto-install-wget-om-mac-os-x-mountain-lion-mavericks-snow-leopard/).

To "install" `bamtofastq`, go to [10X’s website](https://support.10xgenomics.com/docs/bamtofastq) and click "Download bamtofastq [VERSION_NUMBER]" to download the executable file to your local machine. There is no need to compile the tool. Simply move or copy the file to the machine where you want to use it (e.g. your home directory on the EC2) and run the command `chmod 700 bamtofastq-<VERSION_NUMBER>`, making sure to put it somewhere on your `$PATH` if you want to be able to call it from any folder.

## Usage

1. Find the project of interest in the ENA (can search by PRJN or SRP accession from GEO).
2. From the "Study" view showing all the experiments, copy the ftp URL to the "BAM File 1" for the run you want from the "Submitted files (FTP)" column. **Pro-tip: right-click "BAM File 1" and select "Copy link address" to get the URL**.
3. From wherever you want to temporarily store the files (e.g. EC2, another server), use `wget` to download the BAM file.

```
wget <paste ftp URL>
```

1. After the BAM file has been downloaded, convert to fastq files using the `bamtofastq` tool.
```
bamtofastq <downloaded_bam>.bam <name of a folder to put fastqs in>
```

2. By default, fastq files are generated with a max of 50M reads per file. If there are more reads, the files will be split across multiple sets of fastqs. It is recommended to avoid this (it means you'll have to concatenate them later) by using the `--reads-per-fastq` parameter. Below, the max reads per file is set to 500M: 
```
bamtofastq --reads-per-fastq=500000000 <downloaded_bam>.bam <name of a folder to put fastqs in>
```
3. Bask in the joy of being able to get R1, R2, AND I1 files from BAMs
