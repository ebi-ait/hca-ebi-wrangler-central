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
This document defines the who, when and how to acknowledge datasets as an “up-and-running” operational task. By ‘acknowledgement’, it's meant how to add datasets to Ingest as potential datasets to wrangle and include in the HCA DCP. 

## Who
A wrangler in the operation team, decided at the beginning of the sprint, will be the person responsible for acknowledgement of newly published datasets. The decision is recorded every sprint in the Operations planning notes.

In addition, anyone, at any time, may add published papers/preprints/datasets to Ingest, provided they follow this process and fill in the fields according to the agreed requirements and conventions.

## When
At any point before halfway through the sprint, the wrangler/person responsible needs to run the scripts. This only needs to be done once per sprint.

## How

### Semi-automated dataset mining

#### Requirements

- Python3
- Clone the `hca-ebi-dev-team` repo if you haven’t already and install the requirements:
   ```
   git clone https://github.com/ebi-ait/hca-ebi-dev-team.git
   cd scripts/populate_ingest/
   pip install -r requirements.txt
   ```

#### Populate Ingest from nxn.se single cell database

##### Scope of the script

   This script compares data between ingest and the nxn.se database, using `doi`, `accessions` and `title`, filters
   data using eligible `organisms`, `technologies` and `measurements` and populates ingest with the new entries
   from nxn.se database.
   
   Currently, the script is able to populate the project title, description, publication, funders, contributors,
   accessions, cell count and species.
   The technology, organ, and data access fields have to be manually curated and entered.

##### Running the script

1) Go to the `scripts/populate_ingest/` folder inside your cloned version of the `hca-ebi-dev-team` repository

2) Create a `.env` file in `scripts/populate_ingest/`. Specify the relevant ingest api url and ingest api token in
this file. For example, to run against dev:

    ```
        INGEST_API_URL= https://api.ingest.dev.archive.data.humancellatlas.org
        INGEST_API_TOKEN=<dev authentication token>
    ```
    By default, the script runs against local host

3) Run `python -m populate_ingest.populate_ingest_from_nxn`
    
   The script runs against local host, in dry-run mode by default
   
   To run in write mode, and write to ingest, use the `w` flag, e.g.
   `python -m populate_ingest.populate_ingest_from_nxn.py -w`
   
   
   
   The logs can be found at `scripts/populate_ingest/nxn_db.log`
   
   The uuids of the projects created in ingest can be found at `scripts/populate_ingest/added_uuids.txt`.
   
   The projects that would get created in ingest can be found at `scripts/populate_ingest/projects_to_be_added.json`; 
   this is helpful for checking which projects would get created in ingest, when running the script in dry-run mode
   
   The slice of nxn_db with new, valid projects is also exported as `scripts/populate_ingest/new_nxn_data.tsv`
   
##### Manual curation after addition

1. Find out the datasets that were just added (You can look at the output of the script)
1. Go to the project page, and curate the following from the paper:
   - Technology: Add the library preparation technologies
   - Organ: Add the organs used in the experiment
   - Cell count: Add how many cells were **generated** in the paper
   - Data access: Fill in the type of data access (Managed, open, mix, it's complicated)
   - Release date: Add today's date
   - Publications: Check if it's an HCA paper by looking for the string "Human cell atlas"
   - Contributors/funders: If a required text field is missing, add `unspecified`. This will be curated when working on the project.
   - Accessions: Make sure that all accessions mentioned in the paper are present
   - Status: Change the status to `eligible` or `non-eligible`
   - Priority: Set the priority based on the chart below

**Priority chart**

| Priority number | Requisites (Any/All) |
|----------------|-----------|
| 1 | HCA paper, Contributor |
| 2 | Primary tissue, Human data, literature | 
| 3 | Other |

**Edge case 1 (Reanalysis paper)**: Add everything aside from cell count, set cell count to 0, status "not eligible"

**Edge case 2 (Review paper)**: Add everything aside from cell count and accessions, set cell count to 0, status "not eligible"


#### ENA
[WIP/Need Dev script to parse ENA API]

#### ArrayExpress
[WIP/Need dev script to parse AE API]


### Manual ad-hoc dataset addition

When needed, datasets can also be added manually. First, make sure to check that the dataset is not duplicated by searching in Ingest by DOI or project title. This can be checked too while trying to create a new project based on DOI or GEO accession, as Ingest will search for them in the database to avoid duplication.

When the dataset is not present, please fill in **at least** the following information:
- **Accessions**: If available, add the corresponding data accessions.
- **Data access**: Fill in the type of data access (managed, open, mix, it's complicated). 
- **Organism**: Indicate the organism, generally human.
- **Organs**: Indicate the organs used in the experiment.
- **library preparation**: Indicate the technology used to generate the library preparations.
- **Living eu donors**: When human, indicate if they were living EU citizens when the samples were collected on the admin area, under the notes section) .
- **Cell count**: Add the number of cells sequenced in the experiment, or at least an approximation
- **Broker to archives**: If data comes from contributor and need to broker to ENA, add this also to the notes section at the admin area.
- **Broker to scea**: Based on their guidelines, in case it is needed, indicate it at the notes section of the admin area
- **Contributors**: If available, fill in the contributors section
- **Publications**: If a publication or pre-print is available, fill in the publications section, including the DOI and PMID if available. If it is an offical HCA publication, don't forget to tick the Official HCA Publication checkbox.
- **Admin Area**: Remember to set the wrangling status as elegible, and set the wrangling priority based on the priority chart.
