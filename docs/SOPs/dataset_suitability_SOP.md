---
layout: default
title: Dataset Suitability
parent: SOPs
---

# Dataset Suitability Assessment SOP

## Purpose of this document
As wranglers, our current method of tracking new, in-progress (wrangling) and complete datasets is by indicating their priority and status and other key information about the dataset in a tracker sheet. When new datasets are added to the sheet, we need to assess whether they are suitable for HCA. There are specific suitability criteria that we use to decide whether a dataset is suitable or not. It is important that this information is available so that time is not wasted on wrangling datasets that are not suitable for HCA and/or cannot be ingested in our system. The purpose of this document is to list the specific criteria we use to assess dataset suitability and our general approach to implement these. Any feedback on this process is very welcome and should be added to this document; please make it clear that it is feedback. In the longer term we are aiming for a software focused solution to this task.

[Link to dataset tracking sheet](https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0){: .btn }

### Note
It is easiest/most productive to apply this to a list of datasets that have already been prioritised by the species, health status and sample type. Previously, I grouped all ‘unassessed’ datasets by species, health status and sample type, labelled their priority, ordered them by priority, and then assessed the suitability of the set of highest priority datasets.

## Assess data availability

Check the type of consent: if the data is open, this is suitable. If the data is managed access, unavailable or cannot be found, the dataset is unsuitable.

Check that the sequence data is available (similar to the above). If the sequence data is fully available in fastq format, this is suitable. If the sequence data cannot be found or is not in fastq format, then the dataset is unsuitable.

Check that the sequence data is available in a valid format: i.e. fastq format and both Read1 and Read2 are available.

## Assess Technology

Is the technology supported by our defined HCA metadata schema? If we can’t capture the information appropriately, then the dataset is unsuitable. If the technology data type cannot be supported by our processing pipelines, the dataset is suitable but becomes a lower priority and is indicated by the HCA priority column (see [HCA dataset triage SOP](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/dataset_triage_SOP.html).

## Other

Scan the publication title and abstract to check for any signs that the dataset may be unsuitable due to unsupported experiment designs. For example, a xenograft or genetically modified organism are difficult to model using our current HCA metadata schema. This may also be indicated in the ‘HCA priority’ column by indicating that the datasets ‘requires discussion’ by the team. 
