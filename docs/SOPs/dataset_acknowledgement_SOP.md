---
layout: default
title: Dataset acknowledgement SOP
parent: SOPs
---

<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# Dataset acknowledgement
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


## Purpose of this document
This document defines the who, when and how to acknowledge datasets as an “up-and-running” operational task. By ‘acknowledgement’, it's meant how to add datasets to the [Dataset Tracking sheet](https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0) as potential datasets to wrangle and include in the HCA DCP. 

## Who
A wrangler in the operation team, decided at the beginning of the sprint, will be the person responsible for acknowledgement of newly published datasets. The decision is recorded every sprint in the Operations planning notes.

In addition, anyone, at any time, may add published papers/preprints/datasets to the dataset tracker sheet, provided they follow this process and fill in the fields according to the agreed requirements and conventions.

## When
At any point before halfway through the sprint, the wrangler/person responsible needs to run the scripts and update the Dataset Tracking Sheet with any new data found. This only needs to be done once per sprint.

## How

### Semi-automated dataset mining

#### Requirements

- Python3
- Clone the `hca-ebi-dev-team` repo if you haven’t already and install the requirements:
   ```
   git clone https://github.com/ebi-ait/hca-ebi-dev-team.git
   cd scripts/populate-ingest/
   pip install -r requirements.txt
   ```

#### nxn.se single cell database

1) Go to the `scripts/populate-ingest/` folder inside your cloned version of the `hca-ebi-dev-team` repository

2) Run `python -m populate_ingest.populate_ingest_from_nxn -tp <path to token file>`
    
   The script runs against local host, in dry-run mode by default
   
   The `-tp` parameter is for the txt file path with the authentication token.
   
   To run against another environment, specify the value of the environment variable `INGEST_API_URL`, 
   for e.g. against the dev env:
   `export INGEST_API_URL=https://dev.contribute.data.humancellatlas.org` 
   
   To run in write mode, and write to ingest, use the `w` flag, e.g.
   `populate_ingest_from_nxn.py -tp token_path.txt -w`
   
   This script compares data between ingest and the nxn.se database, using `doi`, `accessions` and `title`
   and populates ingest with the new entries from nxn.se database.
   
   Currently, the script is able to populate the project title, description, publication, funders, contributors,
   accessions, cell count and species.
   The technology, organ, and data access fields have to be manually curated and entered.
   
   The logs can be found at `scripts/populate-ingest/nxn_db.log`
   The uuids of the projects created in ingest can be found at `scripts/populate-ingest/added_uuids.txt`.
   
#### ENA
[WIP/Need Dev script to parse ENA API]

#### ArrayExpress
[WIP/Need dev script to parse AE API]


### Manual ad-hoc dataset addition

When needed, datasets can also be added manually. First, make sure to check (With ctrl + f) that the dataset is not duplicated by looking at the following fields:
- DOI
- Paper Title
- Accession

If any of those 3 is already in the dataset tracking sheet, it is highly likely the dataset has been already added. If you think the information there is wrong/incomplete, feel free to curate the row.

When the dataset is not present, please fill in **at least** the following columns:
- **data_accession**: Accession for the raw sequencing data. If contributor data to archive, leave blank.
- **contributor_involved**: `no` if dataset from archives/public sources, `yes` if primary contribution
- **hca_status**: `acknowledged`
- **date_added**: The date the dataset is being added, in YYYY-MM-DD format.
- **access_permission**: If dataset requires managed access, indicate here.
- **organism**: Use the dropdown to indicate `mouse`, `human`, or `human&mouse`
- **sample_type**: Indicate the type of sample (Can choose more than one)
- **health_status**: Indicate if `normal`, `not normal` or `both`
- **phenotype**: If the health status is not `normal`, indicate the phenotype here
- **assay_type**: Indicate the technology used to generate the library preparations. If the technology is not listed, please add it to the dropdown
- **organ**: Indicate, with ontology terms from UBERON when possible, the organ where the samples come from.
- **living_eu_donors**: When human, indicate if they were living EU citizens when the samples were collected. When other organism, indicate `no,none`
- **nucleic_acid_source**: Indicate if bulk, single cell or single nucleus
- **data_available**: `yes` if the raw sequencing data is available
- **technical_benchmarking**: Indicate if the dataset is a benchmarking experiment (e.g. how does tissue storage affect library preparation) 
- **broker_to_archives**: Usually `no` if from archives, `yes` if from contributor and need to broker to ENA
- **broker_to_scea**: Based on their guidelines, indicate `yes` or `no`
- **pub_title**: Indicate publication title
- **hca_pub**: Indicate if it's an HCA publication
- **pub_link**: Indicate the link to the publication (Can be any link as long as it resolves to the manuscript in the journal)
- **pmid**: Indicate pmid. An easy way to do it is by using the tracking sheet function `setPmid()` indicating the cell with the title as a parameter
- **doi**: Indicate DOI. Make sure it starts with `10.`.
