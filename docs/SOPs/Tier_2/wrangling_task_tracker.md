# Task Tracker
[Task Tracker](https://docs.google.com/spreadsheets/d/1Zl4lQlkxjouD4ybu_7UtRwtzndmooWS9AZRjsmmGaIc/edit?gid=0#gid=0)
This is the "enhanced" version of the HCA Atlas Tracker information with ingest and azul data pulled from ingest api and azul api to get the most updated status report, with our internal systems.

We use this to keep track of what projects need to be wrangled, and how close to the wrangling deliverables we are. 
### How to read
You should focus on the first tab only task_list. This is the output of HCA Atlas Tracker in task_list!A:L (see comment in A1 for when it was updated), plus information from ingest api, and azul api. The extra columns are:
* UUID: project_uuid
* gh_ticket: wrangling github ticket at ebi wrangling repo
* in_lists: was the project in the lists of studies we had for wrangling? or added later?
* doi url: link to the DOI of the publication if applicable
* ingest url: link to the project page of ingest
* wrangling state: wrangling state value of project in ingest
* STATE: state of project taking info from ingest & azul (in case it’s published by lattice)
* azup shortname: project short name
* azul fastq: does this project have fastqs in azul?
* Notes: manual notes written in column task_uuid_map!D, is raw managed access?
* Accession: list of the accessions we’ve tagged in ingest
* ingest data: ingest data access value (All open/ all managed access/ mixed/ it’s complicated) - this is only about data submitted to ingest. There might be more data that should be MA but not submitted to ingest
* ingest data notes: notes on the previous field pulled from ingest
* ingest wrangling notes: admin tab wrangling notes pulled from ingest
* metadata spreadsheet: link to published metadata tab in data platform
There are various questions that we can answer using this data, some of them are listed in the 
### How to update
There are 3 places we need to update here.
1. tracker values in task_list!A:L
We provide these values and all other values are calculated based on the configuration tab task_uuid_map where mappings between ingest and task tracker is done.
    1. download updated TSV file from HCA Atlas Tracker reports page. Be sure to filter out tasks non relevant to HCA Repo ingestion (filtered here).
    1.reorder columns to match columns in sheet
    1. paste values over the previous data. Data will be pulled from ingest and azul automatically.
    1. add date in A1 comment for reference
1. New additions to the tracker
If a new dataset is added in the sheet, we would see that Study Name is not matching in task_uuid_map!A:A . We have to add columns A, B, C in this task_uuid_map tab
    1. Add study name and DOI in task_uuid_map tab in col A, B below last entry.
    1. Add project uuid
        1. Search for the project in ingest with DOI, Study name, Collaborator or any other way to make sure the project was not added in ingest before. Find project UUID
        1. If project’s not in ingest, create a project for DOI.
    1. Extend functions in cols F, H, J-T
1. api backup results
Making all those calls to APIs takes time, and sometimes the custom ImportJSON function timesout. Thus, we’ve a backup table to show if API does not return anything (ImportJSON gives #N/A). Columns task_uuid_map!Y:AC
These backup values are updated regularly to represent the current wrangling state of the tracker. To update you need to re-run a script that inputs uuids, requests from apis and print results.
1. Select uuids to use (if it’s possible keep same ordering, by copying from column C)
1. Run script and provide uuids and ingest token to pull data from there
1. Paste result into columns task_uuid_map!Y:AC

