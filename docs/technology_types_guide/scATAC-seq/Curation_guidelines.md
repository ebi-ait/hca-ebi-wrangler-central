---
layout: default
title: How to curate scATAC-seq Data
parent: scATAC-seq
grand_parent: Technology Types Guide
nav_order: 1
---

# How to curate scATAC-seq Data

### Overview

This guide is intended to hightlight the ***required metadata*** for scATAC-seq data. Optional metadata fields should be evaluated on an individual project basis given the experimental design and available metadata.

The ***required metadata*** includes:

(1) ontology terms: library construction method, sequencing method

(2) analysis file types that we require based on our review of scATAC-seq technology/publications (not evaluated during metadata schema validation)

### (1) Ontology terms

- See [technology type table](https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/docs/technology_types_guide/technology_types_table.md)

### (2) Analysis file(s)

- Raw DNA sequencing data derived from sequencing of scATAC-seq libraries.

- A "peaks" file containing the genomic coordinates corresponding to scATAC-seq peak identification. There is no strict format requirement. The peaks might be recorded in a bed file or a simple txt file, for example.

# Barcodes

The cell barcode read and umi barcode read should be double-checked on a dataset basis, as this might change depending on whether 10X is used, and also how the user names their files. This [link](https://divingintogeneticsandgenomics.rbind.io/post/understand-10x-scrnaseq-and-scatac-fastqs/) describes the barcode reads and lengths for 10X scATAC-seq.
