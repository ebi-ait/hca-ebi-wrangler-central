---
layout: default
title: Update Zooma Data source
parent: Update schema & ontology
grand_parent: SOPs
nav_order: 3
last_modified_date: 13/05/2020
---

## Updating the ZOOMA datasource
{: .no_toc .text-delta }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Background

"ZOOMA is an application for discovering optimal ontology mappings, developed by the Samples, Phenotypes and Ontologies Team at EBI. It can be used to automatically annotate "properties" (plain text, descriptive values about biological entities) with "semantic tags" (ontology classes)." - [ZOOMA about page](https://www.ebi.ac.uk/spot/zooma/about)

By generating a ZOOMA data source from our ontology curations, we can save the work we do to manually curate ontology terms so that our manual curation work can be used to automate curations.

The ZOOMA data source is a large tab-delimited text file that contains ontology curations from all the studies in ingest. Ontology curations should be de-duplicated per project so there is a one-to-one mapping between an ontology term and the text value that was entered for a particular metadata field.

The columns in the file are:

| Column name    | Description                                                   |
|----------------|---------------------------------------------------------------|
| STUDY          | project.project_core.project_short_name                       |
| BIOENTITY      | the 'type' of metadata entity, e.g. donor_organism, cell_line |
| PROPERTY_TYPE  | the specific field, e.g. organ, unit, genus_species           |
| PROPERTY_VALUE | the 'text' term entered into ingest for the ontologised field |
| SEMANTIC_TAG   | the full iri of the ontology id entered into ingest           |

In order to keep the ZOOMA data source up-to-date, scripts have been written to automate harvesting the ontology curations from ingest and create the text file that is used as a data source. When this updated source is pushed to the github repo, it is automatically picked up and used when the ZOOMA database is updated.

Current challenges in this approach include:
- if incorrect ontology curations exist in ingest, they may leak into our data source and perpetuate automated incorrect curations
- if a particular entity gets updated, does the old entity still exist and we end up with both the old and new curation?

For any help with ZOOMA data source stuff, please reach out to the SPOT team, specifically Henriette Harmes or James McLaughlin.

## How to run the scripts

### Prerequisites

* Python 3+
* local copy of `ebi-ait/hca-ebi-wrangler-central`
* python 3 virtualenv with `ebi-ait/hca-ebi-wrangler-central/src/requirements.txt` installed

### Step by step process

1. Go to your local `ebi-ait/hca-ebi-wrangler-central/src` repo and pull the latest version

```
cd /path/to/repo/hca-ebi-wrangler-central/src
```

1. Activate your virtualenv with the `ebi-ait/hca-ebi-wrangler-central/src/requirements.txt` installed

#### Searching for projects after a certain date

This method should be useful to run after each release.

1. Get an authorisation token from ingest
    1. Go to ingest ui [https://contribute.data.humancellatlas.org/projects](https://contribute.data.humancellatlas.org/projects)
    1. Right click anywhere on page and select 'Inspect'
    1. In the inspect console, click 'Network'
    1. Click one of the lines that begins projects? 
    1. Scroll until you see the `Authorization: Bearer` in the Request headers and copy the large string of numbers, letters and symbols `ey....`
1. Run the `harvest_ontologies.py` script with entering the date when it was last run and an authorisation token from ingest.

```
python harvest_ontologies.py -d YYYY-MM-DD -t AUTH_TOKEN
```

The script first searches all projects in ingest that were submitted after the given date that have either `Exported` or `Completed` status, and saves project uuids into a file called `outputs/YYYY-MM-DD_project_uuids.txt`. 

It then uses the list of project uuids to search all ontology curations in these projects and saves them to a file called `YYYY-MM-DD_HH-mm_property_mappings.tsv`. 

Finally it joins the latest found property mappings with the ZOOMA source file `current_zooma_import.txt`.

#### Getting ontologies from a list of project uuids

If you already have a list of project uuids you wish to harvest ontology curations from and add to the ZOOMA data source, an ingest token is not required. 

Expected file input is a tab delimited text file with no header where the first column contains project uuids. 

```
python harvest_ontologies.py -f uuid_file.txt
```

To see other optional flags, use
```
python harvest_ontologies.py -h
```

#### Review the Ontologies reports

To view some summarised tables of curations from the Data source run:

```
python generate_ontology_curation_reports.py
```

This script creates a web app with interactive tables that can be filtered and searched to help with detecting ontology curation errors.

The tables generated are:
##### Summarised table of curations from most recent harvest per project

This table summarises the count of ontology curations per ontology term per project for the most recent ontology harvest, then sorts them in descending order by curation count. 

The idea being that if there are many curations for a single ontology term, that there may have been an error. These terms may also indicate that more specific terms need to be added to the underlying ontology to better capture the specified text.

##### Summarised table of curations from most recent harvest

This table summarises the count of ontology curations per ontology term across all projects that were imported in the latest harvest.

##### Summarised table of curations from full ZOOMA file

The same summary as above but for all curations in the zooma file, rather than the most recent harvest.

##### Full table of curations from most recent harvest

Non-summarised view of the most recent run of the harvest script. (Same as opening the `src/outputs/YYYY-mm-dd_HH_MM_property_mappings.tsv` in excel)

##### Full table of curations from full ZOOMA data source

Non-summarised view of the full ZOOMA data source. (Same as opening the `src/outputs/current_zooma_import.txt` in excel)

Reviewing the tables in this report can help with detecting ontology curation errors before they are made a part of the ZOOMA data source.

#### Push to github

Once you have reviewed the ontologies and are happy for the ontology curations to be added to our ZOOMA datasouce, push the changes to master.

Each Sunday, ZOOMA will automatically be rebuilt with the `current_zooma_import.txt` file. 

### Outline of script algorithm

Attempt at english words to describe scripts. Also see docstrings.

#### harvest_ontologise.py

`search_ingest` method
If `update date` specified:
- search ingest using the sorted projects endpoint
Iterate over each project in ingest
If a project has an `update_date` before the specified date:
  get the submissions envelopes for the project
  For each submission envelope
    If the submission envelope was updated before the `update_date`:
      If the submission has status 'Exported' or 'Complete'
        add the project to the list and save to a file of uuids
When you get to a project past the `update_date`, stop searching

`get_ontology_mappings`
wrapper around the `ontology_mappings_extractor.py` script, uses a file of uuids to extract the ontology mappings.

Once ontology mappings have been extracted, concatenate the most recent `_property_mappings.tsv` file to the `current_zooma_import.txt` file.

#### ontology_mappings_extractor.py

Given a list of project uuids
For each project uuid:
    For each submission in the project:
        For each biomaterial, protocol and file entity:
            For each field:
                If its an ontology field:
                    Save the field, text and ontology information to file
