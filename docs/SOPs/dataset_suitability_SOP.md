---
layout: default
title: Dataset Suitability
parent: SOPs
---

# HCA Dataset Eligibility criteria 

## Purpose of this document
As wranglers we track new, in-progress (wrangling) and complete datasets by adding them as projects in ingest. You can [add a project](https://contribute.data.humancellatlas.org/projects/register/autofill) automatically with a doi or an accession, or you can register one manually.
Additionally, datasets are automatically added every month by our [script] (https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/dataset_acknowledgement_SOP.html#populate-ingest-from-nxnse-single-cell-database).

When we register a new project we need to indicate its priority, eligibility, status and other key information in ingest (see the dataset [acknowledgment SOP](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/dataset_acknowledgement_SOP.html#manual-curation-after-addition)). Having all this information helps the wranglers to quickly select the projects to wrangle, rejecting datasets that are not eligible for the HCA.

The purpose of this document is to list the specific criteria we use to assess dataset eligibility and our general approach to implement these. Any feedback on this process is very welcome and should be added to this document; please make it clear that it is feedback. In the longer term we are aiming for a software focused solution to this task.

_In the past we used a spreadsheet to keep track of the projects we were working on. If you are working on an old project and want to check for useful comments you can find the dataset tracking sheet [here](https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0)._

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
- Be derived from a recognised single cell technology

(1)  https://contribute.data.humancellatlas.org/
(2)  https://www.humancellatlas.org/publications/

This criteria means a great number of datasets are eligible, and we need rules to assign priority. See [HCA dataset triage SOP](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/dataset_triage_SOP.html) for more information.


### Note

It is easiest/most productive to apply this to a list of datasets that have already been prioritised by the species, health status and sample type. Previously, I grouped all ‘unassessed’ datasets by species, health status and sample type, labelled their priority, ordered them by priority, and then assessed the suitability of the set of highest priority datasets.

## Assess data availability

Check the type of consent: 
- Open: **suitable**. 
- Managed/Controlled access: Needs to at least have **publicly accessible count matrices**. If there is no shareable data the dataset should be down prioritised or possibly considered ineligible.

Additionally, GDPR is in consideration; if the dataset contains samples from living donors, no externally obtained data or metadata can be added. We consider externally obtained data any type of information that is not obtained from public sources (e.g. the manuscript or archives such as GEO).

Check that the sequence data is available (similar to the above). If the sequence data is fully available in fastq format, this is suitable. If the sequence data cannot be found or is not in fastq format, then the dataset can still be included if there are publically sharable contributor generated matrices. If there is no sharable data in the form of fastq files or a gene expression matrix, the dataset should be down prioritised or possibly considered ineligible.

Check that the sequence data is available in a valid format: i.e. fastq format and both Read1 and Read2 are available. If bam files are available they can be converted to fastq.

_**Demultiplexing**: In the past if the experimental design involved multiple samples which were pooled before library preparation, the resulting fastq files had to be demultiplexed by the sample barcode before being uploaded to ingest. This was required by the pipelines team, but this is no longer necessary and we can ingest multiplexed data._

## Assess Technology

Is the technology supported by our defined HCA metadata schema? If we can’t capture the information appropriately, then the dataset is blocked until the schema changes can be made to support the technology, but this does not make it ineligible. (see [HCA dataset triage SOP](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/dataset_triage_SOP.html)).

## Other

Scan the publication title and abstract to check for any signs that the dataset may be unsuitable due to unsupported experiment designs. This may also be indicated in the ‘HCA priority’ column by indicating that the datasets ‘requires discussion’ by the team.

