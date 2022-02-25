---
layout: default
title: Dataset Suitability
parent: SOPs
---

# HCA Dataset Eligibility criteria 

## Purpose of this document
As wranglers, our current method of tracking new, in-progress (wrangling) and complete datasets is by indicating their wrangling status, priority and release in Ingest. When new datasets are added, we need to assess whether they are eligible for HCA. There are specific eligibility criteria that we use to decide whether a dataset is eligible or not. It is important that this information is available so that time is not wasted on wrangling datasets that are not eligible for HCA and/or cannot be ingested in our system. The purpose of this document is to list the specific criteria we use to assess dataset eligibility and our general approach to implement these. Any feedback on this process is very welcome and should be added to this document; please make it clear that it is feedback.

### HCA Eligibility

We consider three main categories of data to be eligible for the Human Cell Atlas.

**Directly contributed data**. 
To be eligible for this category, datasets must:
- Be contributed to the Human Cell Atlas Data Coordination Platform(1) by the data owner, with support of DCP data wranglers
- Have either a pre-print publication referencing data that meets the criteria for published data, or else a supporting justification as to why it should be included in the HCA

**Data from official Human Cell Atlas publications**. 
To be eligible for this category, datasets must:
- Support a publication that has been reviewed by the HCA publication committee and added to the official HCA publications list (2)

**Published Data**. 
To be eligible for this category, datasets must:
- Be referenced in a peer-reviewed journal or be available as pre-print
- Contain at least some samples derived from healthy human donors. 
- Be derived from a recognised single cell technology

(1)  https://contribute.data.humancellatlas.org/
(2)  https://www.humancellatlas.org/publications/

This criteria means a huge number of datasets are eligible and there needs to be a prioritisation approch in order to understand order datasets should be wrangled. See [HCA dataset triage SOP](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/dataset_triage_SOP.html)


### Note

It is easiest/most productive to apply this to a list of datasets that have already been prioritised by the species, health status and sample type. Previously, I grouped all ‘unassessed’ datasets by species, health status and sample type, labelled their priority, ordered them by priority, and then assessed the suitability of the set of highest priority datasets.

## Assess data availability

Check the type of consent: if the data is open, this is suitable. If the data is managed access, has living European donors, unavailable or cannot be found, the dataset can now be included if there are publically sharable contributor generated matrices. If there is no sharable data the dataset should be down prioritised or possibly considered ineligible.

Check that the sequence data is available (similar to the above). If the sequence data is fully available in fastq format, this is suitable. If the sequence data cannot be found or is not in fastq format, then the dataset can still be included if there are publically sharable contributor generated matrices. If there is no sharable data in the form of fastq files or a gene expression matrix, the dataset should be down prioritised or possibly considered ineligible.

Check that the sequence data is available in a valid format: i.e. fastq format and both Read1 and Read2 are available.

Check if the data requires demultiplexing. If the experimental design involves multiple samples which are pooled before library preparation, the resulting fastq files should be demultiplexed by the sample barcode before uploaded to ingest. If the samples are not able to be be demultiplexed, for example, if samples are not barcoded before being pooled, then the raw fastq file data is not suitable. However, a gene expression matrix can still be uploaded in this case.

## Assess Technology

Is the technology supported by our defined HCA metadata schema? If we can’t capture the information appropriately, then the dataset is blocked until the schema chnages can be made to support the technology, but does not make it ineligible. (see [HCA dataset triage SOP](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/dataset_triage_SOP.html)).

## Other

Scan the publication title and abstract to check for any signs that the dataset may be unsuitable due to unsupported experiment designs. For example, a xenograft or genetically modified organism are difficult to model using our current HCA metadata schema. This may also be indicated in the ‘HCA priority’ column by indicating that the datasets ‘requires discussion’ by the team. 
