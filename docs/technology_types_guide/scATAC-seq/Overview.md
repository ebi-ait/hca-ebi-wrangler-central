---
layout: default
title: scATAC-seq - Single-cell sequencing assay for transposase-accessible chromatin
parent: scATAC-seq
nav_order: 2
grand_parent: Technology Types Guide
---

# scATAC-seq: Single-cell sequencing assay for transposase-accessible chromatin

### Method

scATAC-seq is used for analyzing genome-wide regulatory landscapes in single cells.  Specifically, ATAC-Seq enables the identification of open chromatin regions, which are generally transcriptionally active genes.

The ATAC-Seq method relies on next-generation sequencing (NGS) library construction using the hyperactive transposase Tn5. NGS adapters are loaded onto the transposase, which allows simultaneous fragmentation of chromatin and integration of those adapters into open chromatin regions. The library that is generated can be sequenced by NGS and the regions of the genome with open or accessible chromatin are analyzed using bioinformatics. See **Figure 1** for an illustration of ATAC-seq.

<center><u> Figure 1</u>: Illustration of ATAC-seq</center>


<img src="https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/docs/technology_types_guide/scATAC-seq/visuals/ATAC-seq.png" width="500" height="500">


### Is scATAC-seq a single-cell method?

Yes.

### Aim

ATAC-Seq has become a common first step into epigenomic analysis that opens a lot of hypotheses about the molecular mechanisms responsible for regulating many different cellular processes. The sequencing of open chromatin regions that are being transcribed can lead to the identification of transcription factors that are active in the phenotype or conditions being investigated. ATAC-Seq assays are also powerful because they can be used to determine nucleosome positioning.

### Output (other than standard scRNA-seq data)

- Raw DNA sequencing data derived from sequencing of scATAC-seq libraries.

- A "peaks" file containing the genomic coordinates corresponding to scATAC-seq peak identification. There is no strict format requirement. The peaks might be recorded in a bed file or a simple txt file, for example. See [here](https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/docs/technology_types_guide/scATAC-seq/example_datasets/atac_v1_pbmc_10k_peaks.bed) for an example dataset.

- A peak by cell matrix.

- A peaks annotation file might also be available, but it is not required. It would typically include the name of the gene spanning the peak region and the type of peak (e.g. promoter, distal). See [here](https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/docs/technology_types_guide/scATAC-seq/example_datasets/atac_v1_pbmc_10k_peak_annotation.tsv) for an example dataset.

