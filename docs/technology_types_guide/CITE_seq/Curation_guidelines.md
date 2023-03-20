---
layout: default
title: How to curate CITE-seq Gene Expression & Surface Protein Data
parent: CITE-Seq
grand_parent: Technology Types Guide
nav_order: 1
---

# How to curate CITE-seq Gene Expression & Surface Protein Data

## Overview

This guide is intended to hightlight the ***required metadata*** for CITE-seq data. Optional metadata fields should be evaluated on an individual
project basis given the experimental design and available metadata.

**Required metadata includes:**

(1) ontology terms: library construction method, sequencing method

(2) analysis file types that we require based on our review of CITE-seq technology/publications (not evaluated during metadata schema validation)

(3) sequence file types that we require based on our review of CITE-seq technology/publications (not evaluated during metadata schema validation)

## (1) Ontology terms

- See [technology type table](https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/docs/technology_types_guide/technology_types_table.md)

## (2) Analysis file(s)

### CITE-seq (cell surface protein profiling) EFO:0030008 ###

- gene expression matrix for scRNA-seq data
- list of antibody derived tags (ADT): barcode sequence and name
- counts matrix for antibody derived tag (ADT) library

### CITE-seq (sample multiplexing) EFO:0030009 ###

- gene expression matrix for scRNA-seq data
- list of hashtag oligos (HTO): barcode sequence and name
- counts matrix for hashtag oligo (HTO) library

### CITE-seq (cell surface protein profiling) EFO:0030008 & CITE-seq (sample multiplexing) EFO:0030009 ###

- gene expression matrix for scRNA-seq data
- list of antibody derived tags (ADT): barcode sequence and name
- counts matrix for antibody derived tag (ADT) library
- list of hashtag oligos (HTO): barcode sequence and name
- counts matrix for hashtag oligo (HTO) library

## (3) Sequence file(s)

### CITE-seq (cell surface protein profiling) EFO:0030008 ###

- raw sequencing fastq: scRNA-seq data
- raw sequencing fastq: ADT barcodes

*n.b. a separate cell suspension id should be created for each library type*

### CITE-seq (sample multiplexing) EFO:0030009 ###

- raw sequencing fastq: scRNA-seq data
- raw sequencing fastq: HTO barcodes

*n.b. a separate cell suspension id should be created for each library type*

### CITE-seq (cell surface protein profiling) EFO:0030008 & CITE-seq (sample multiplexing) EFO:0030009 ###

- raw sequencing fastq: scRNA-seq data
- raw sequencing fastq: ADT barcodes
- raw sequencing fastq: HTO barcodes

*n.b. a separate cell suspension id should be created for each library type*
