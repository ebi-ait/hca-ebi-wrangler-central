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
- Clone the `hca-ebi-wrangler-central` repo if you haven’t already and install the requirements:
   ```
   git clone https://github.com/ebi-ait/hca-ebi-wrangler-central.git
   cd hca-ebi-wrangler-central/src/
   pip install -r requirements.txt
   ```

#### nxn.se single cell database

1. Go to the `src/` folder inside the `hca-ebi-wrangling` repository
1. Run `python3 compare_tracker_with_nxn_sheet.py | pbcopy`
   
   This runs the script and copies the output to your clipboard. 

Once complete, paste the results into the leftmost cell under the latest dataset acknowledged. It’s already formatted with the tracker’s format, so it’s just a paste operation

The script updates itself with a timestamp to keep track of when it was last run. After running, push the changes to the repo:
```
git checkout master
git pull
git add compare_tracker
git add compare_tracker_with_nxn_sheet.py
git commit -m "Updated tracker sheet."
git push origin master
```

New publications from the single cell database need an additional step of manual curation to ensure certain fields meet the requirements for prioritisation and suitability. 

The following columns need to be curated:
1. **technology**: 10x is usually abbreviated as “Chromium”, independently of the chemistry or end bias. A more specific term is needed.
1. **health_status**: Need to indicate if normal, not normal or both, and if the 2 latest indicate the phenotype.
1. **access_permission**: if accession is not from EGA/dbGAP,  usually “open”. Otherwise, “managed” or “mix”
1. **living_eu_donors**: If mice, indicate `no,none`. If human, looking at the laboratory location should be enough to fill this.
1. **nucleic_acid_source**: single cell, single nucleus, bulk
1. **technical_benchmarking**: If the dataset is a benchmarking experiment, `yes`. Else, `no` 
1. **broker_to_archives**: Usually `no`, as the data is being extracted from the archives
1. **broker_to_scea**: Based on SCEA’s guidelines, provide with “yes” or “no”. If you have filled everything else, there should be enough information for you to choose one of the two.

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
- **living_eu_donors**: When human, indicate if they are living in EU. When other organism, indicate `no,none`
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
