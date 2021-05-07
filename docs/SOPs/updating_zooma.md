---
layout: default
title: Update Zooma Data source
parent: SOPs
last_modified_date: 07/05/2020
---

## Updating the ZOOMA datasource


### Prerequisites

* Python 3+
* local copy of `ebi-ait/hca-ebi-wrangler-central`
* python 3 virtualenv with `ebi-ait/hca-ebi-wrangler-central/src/requirements.txt` installed

### Step by step process

1. Go to your local `ebi-ait/hca-ebi-wrangler-central/src` repo and pull the latest version
```
cd /path/to/repo/hca-ebi-wrangler-central/src
```
1. Activate your virtualenv with requirements installed

#### Searching for projects after a certain date
1. Get an authorisation token from ingest
    1. Go to ingest ui [https://contribute.data.humancellatlas.org/projects](https://contribute.data.humancellatlas.org/projects)
    1. Right click anywhere on page and select 'Inspect'
    1. In the inspect console, click 'Network'
    1. Click one of the lines that begins projects? 
    1. Scroll until you see the `Authorization: Bearer` in the Request headers and copy the large string of numbers, letters and symbols
1. Run the `harvest_ontologies.py` script with entering the date when it was last run and a 
```
python3 harvest_ontologies.py -u YYYY-MM-DD -i AUTH_TOKEN
```

The script first searches all projects in ingest and saves found projects into a file called `outputs/YYYY-MM-DD_project_uuids.txt`. 

It then uses the list of project uuids to search all ontology curations in these projects and saves them to a file called `YYYY-MM-DD_HH-mm_property_mappings.tsv`. 

Finally it joins the latest found property mappings with the ZOOMA source file `current_zooma_import.txt`.

#### Getting ontologies from a list of project uuids

If you already have a list of project uuids you wish to harvest ontologies for and add to the ZOOMA data source, an ingest token is not required. 

Expected file input is a tab delimited text file with no header where the first column contains project uuids. 

```
python3 harvest_ontologies.py -f uuid_file.txt
```

#### Review the Ontologies reports

As part of running the harvest_ontologies.py script, two reports will be generated. One provides summary information about the new mappings that were harvested in this iteration of the script. The other provides information about the entire ZOOMA data source.

Reviewing this report can help with detecting ontology curation errors before they are made a part of the ZOOMA data source.

#### Push to github

Once you have reviewed the ontologies and are happy for the ontology curations to be added to our ZOOMA datasouce, push the changes to master.

Each Sunday, ZOOMA will automatically be rebuilt with the `current_zooma_import.txt` file. 
