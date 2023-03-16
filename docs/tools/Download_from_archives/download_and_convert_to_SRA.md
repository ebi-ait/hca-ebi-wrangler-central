---
layout: default
title: Downloading and converting SRA objects from SRA
parent: Download from archives
grand_parent: Tools
nav_order: 2
---
# Downloading and converting SRA objects from SRA

Sometimes when converting published datasets from GEO, there are only single fastq files available for download when there should be two (R1/R2) or three files (I1/R1/R2) per run depending on the type of sequencing.

## Prerequisites
- `virtualenv`
- `python3`
- `sratoolkit` 
    - [Download and install (Ubuntu version if on EC2)](https://github.com/ncbi/sra-tools/wiki/02.-Installing-SRA-Toolkit#the-installation-processes-for-mac-os-x-and-the-two-linux-distributions-are-roughly-identical)

## To download all sra objects from a project with pysradb

[pysradb](https://saket-choudhary.me/pysradb/) is a convenient way to `prefetch` all runs from a given project accession. Example usage to download all runs from an SRP accession

1. Activate your desired virtualenv
1. Install pysradb with `pip install pysradb`
1.

```
pysradb download -y -t 3 --out-dir ./pysradb_downloads -p SRP063852
```

This command saves sra object files in a folder structure of `SRP`/`SRX`/`SRR`.

To convert each SRR sra object to separate fastqs, we need to use the [`fastq-dump`](https://ncbi.github.io/sra-tools/fastq-dump.html) command in the sratoolkit

```
fastq-dump --split-files <path to file/accession>
```

You can use a bash for loop to iterate over all the runs that were downloaded.

It may be possible to also use [`fasterq-dump`](https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump), but we haven't tried this yet. Feel free to try it and expand this snippet.

