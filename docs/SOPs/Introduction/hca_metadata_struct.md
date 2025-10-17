---
layout: default
title: HCA metadata structure
parent: Introduction
grand_parent: SOPs
nav_order: 4
---

# HCA metadata schema

HCA Data Repository and HCA Data Platform, uses the [HCA metadata schema](https://github.com/HumanCellAtlas/metadata-schema/tree/master/json_schema). You can read more about it in [HCA metadata structure](https://github.com/HumanCellAtlas/metadata-schema/blob/master/docs/structure.md).

# Tier-ed metadata schema
Other HCA parts however, are using a different metadata schema, the Tiered schema. This include 3 different groups of metadata fields, Tier 1, Tier 2 and Tier 2 (CAP) metadata.

## Tier 1 metadata schema
[definitions document](https://docs.google.com/spreadsheets/d/13oqRLh1awe7bClpX617_HQaoS8XPZV5JKPtPEff8-p4/edit?gid=1404414727#gid=1404414727), [data dictionary](https://data.humancellatlas.org/metadata/tier-1)

Tier 1 metadata fields provide the foundational information used to build tissue and organ atlases.

Tier 1 metadata fields are required to:
-  Help identify samples or datasets included in integration
-  Help identify and explain technical batch effects 
-  Help qualify or disqualify datasets for inclusion in atlases
-  Understanding the factors that can cause batch effects is vital to ensure that when the datasets are combined into an atlas, they have not been over-corrected (i.e., masking true biological variation between cells) or under-corrected (e.g., resulting in the same cell types appearing as distinct from one another).

## Tier 2 metadata schema
The Tier 2 metadata provides richer donor- and sample-level context, such as `age`, `clinical phenotype`, `treatment`, and similar fields, used in downstream analysis. Because some fields may be identifying, Tier 2 metadata are collected and distributed under managed access. The Biological Networks group is finalizing the field list; drafts are in the [HCA Tier 2 Metadata Definitions](https://drive.google.com/drive/folders/1ngcIgKBV9OUM1pPO-CDRH6ZIpyiSpamu) folder.

Tier 2 metadata are defined and collected by our team in collaboration with each bionetwork. More on this in the dedicated [SOP](/hca-ebi-wrangler-central/SOPs/tier2_definitions.md)

## Tier 3 / CAP metadata schema
Cell‑annotation metadata standardizes cell‑type labels. Stored on the [Cell Annotation Platform](https://celltype.info/) (CAP), the schema records each cell’s ontology term, synonyms, and parent category. See the CAP AnnData schema for additional details.
