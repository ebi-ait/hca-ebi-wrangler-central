# Tier 2 organising
Here I will describe all the documents that have to do with Tier 2 and a small description of their functionality.
### What is Tier 2
HCA Tier 2 metadata are sets of biological metadata, specific for each bionetwork. Genetic Diversity Tier 2 will be requested by all bionetworks to record the coverage of the atlases and survey the diversity of samples used to build the atlases.
Ingestion of tier 2 is the responsibility of Data Repository (EBI), while HCA Tier 1 metadata that is going to be ingested by Data Repository (Clever Canary). 

### How is Tier 2 defined?
Via communications between EBI team and bionetwork coordinators who suggest relevant metadata. The EBI team is responsible for harmonising and aligning among different bionetworks where similar fields are suggested; and standardising metadata where possible through controlled vocabularies and ontologies.

### What is the format?
We now have various formats for Tier 2 metadata depending on who’s the end user.
* Metadata definitions (example)
* Metadata template (example)
* Metadata recommendations (example)
#### Definitions
Based on the HCA Tier 1 definitions example, we capture all the information needed to describe each metadata field.
This is intended for users who want to review Tier 2 metadata and is also the basis for extending the current HCA json schema.
#### Template
This is the sheet that we will ask contributors to fill in. This can later be integrated with Tier 1 into a full metadata DCP ingestible sheet. 
For help with converting t1 to dcp see https://github.com/ebi-ait/hca-tier1-to-dcp
#### Recommendations
This is a work in progress sheet intended for communications with the bionetwork to prompt them to provide more information beyond just a list of metadata field names. All such sheets are now not in use nor actively updated.

## Tier 2 - Resources
https://github.com/ebi-ait/hca-ebi-wrangler-central/issues/1286
Here we have links for most of the tier 2 organising processes, and a table to record the progress of each bionetwork.
### Finalised Tier 2 google dir
This is a gdrive dir managed by HCA exec team, that is publicly accessible and Clever Canary team is pulling info from there to build the Tier 2 Data Dictionary https://data.humancellatlas.org/metadata/tier-2 . The google drive dir should only contain the finalised and ready to published versions of Tier 2 definitions.
### WIP Tier 2 google dir
This is gdrive managed by the EBI team, that is private to the FG team, and individual sheets are shared with specific coordinators. Communication logs for some of the discussions are also recorded there.

### Cross-Bionetwork Summary sheet
A sheet that pulls all metadata fields from finalised Tier 2 lists, compares between bionetworks and shows which fields are used by which bionetwork.
#### Tabs description:
* *all_tier2*: summary tab with all info regarding the common fields per bionetwork
* *conf_sheet_link*: this is where we add the link for Tier 2 definitions google sheets and specify in which cell the programmatic names are found
* *conf_pull_data*: Bionetwork names are listed in column A. For each bionetwork a formula imports all the fields’ programmatic names into column B.
Make sure to fill the bionetwork name in column A next to all the corresponding  field names in column B. In unified_field (column C) a formula pulls from conf_similar_fields tab a unified field name for fields that are named slightly differently across bionetworks
* *conf_map_dcp*: this maps t2 fields to existing fields in the DCP metadata schema. 
Please add field name in column A and dcp programmatic name in column C.
conf_similar_fields: every new field that has not been used before, needs to be added here in a new row.
Some bionetworks use different names to describe the same fields so if that’s the case, a synonym field should be added next to the appropriate field value (in columns C:F).
You can specify modules to describe what metadata module this field could be added to in the dcp schema. Using more descriptive groupings of the metadata helps to make the long list more readable, but serves no other functionality.

#### How to update
To link a new finalised t2 sheet:
1. Update the conf_sheet_link tab with the correct link - it cannot be .xlsx format, in order to be accessible with importrange functions, it has to be a google sheet. Specify the cell where programmatic field names are found in the finalised sheet. 
1. In conf_pull_data write the bionetwork name in column A, copy the function to pull data from cell B2 and paste it at the end of the current fields.
If there is not enough space for all metadata fields, an error will appear so make sure you have enough space to pull everything. Drop down the functions for all other columns C:F and see what fields need to be added in the conf_map_dcp and conf_similar_fields. Follow the instructions below to add new t2 fields
1. In the conf_map_dcp tab, sort by column A to keep consistency. 

To add a new t2 field:
1. New field will be automatically be pulled from the definitions spreadsheet defined in conf_sheet_link
1. If #REF is shown in conf_sheet_link make sure there is enough space after query-importrange function for the bionetwork, if no, add rows and extend functions
1. Check if the field should be matched to a similar field in conf_similar_fields
    1. If yes, add field in the next empty column of the appropriate row of conf_similar_fields!C:F
    1. If not, add field in a new row in conf_similar_fields!B
    1. Ideally, find a relevant group to fit in (conf_similar_fields!G) and add in the same cluster of rows so it appears grouped in all_tier2 tab
    1. find a relevant dcp schema module conf_similar_fields!A
1. Add new fields in conf_map_dcp
    1. Add new field to column A
    1. if the field can be mapped to an existing dcp field, add the dcp field in column B and C, if not leave them empty 
### Tier 2 sheet validator
This is a sheet to make sure that values in definitions and template sheets match.
We have one summary tab called validate and each bionetwork with finalised tier 2 has a separate tab as well.
#### How to read
* In the validate tab check any FALSE values that indicate mismatch between definitions and template sheets, or between bionetwork definitions and Genetic Diversity definitions
* If FALSE values are existent, investigate in the relevant bionetwork tab.
    * We have two tables to compare in each tab: Templates and definitions.
    * Template fields (columns A:E) and Definitions fields (column K:P) are imported directly from the corresponding spreadsheets, specified in validate!B:C.
    * In order to compare we need to align the two table fields, and this is done by matching the programmatic name of in col F. Then in the next columns friendly, description, examples are tested. Comparison results are found in columns F:I and correspond to metadata field from template (column E)
    * If any FALSE values are found in F:I columns address the mismatch
#### How it works
For each bionetwork:
1. pull template and definition sheets with importrange() - neither can be .xlsx format, in order to be accessible with importrange functions, it has to be a google sheet and have permissions to read (and edit?)
1. check if the programmatic and friendly field_name, description and examples are matching between the two sheets
Each bionetwork has a separate tab where definitions and templates are pulled based on the links in the validate tab. In each bionetwork tab then
* we match the fields based on the programmatic field name
* compare friendly, description and examples
    (after removing prefix sentence from template’s examples)
* if mismatch get a FALSE in G,H and I columns for friendly, description, example
A comparison between each bionetwork and Genetic Diversity (GD) fields is done on the right extension of each tab. GD tab has a right extension to compare between definitions among all bionetworks.
We get a summary glimpse of errors in the validate tab where we can see if all is good within each bionetwork and between bionetwork and GD fields.
### Tier 2 collection tracker
This is a sheet to keep track of communication between wranglers and contributors regarding the Tier 2 collection.
Main tracking focus shifted to HCA DCA tracker since signing the DCA is the next part of the collection process, but the collection tracking sheet is used to keep mapping between emails and datasets/study names (when we can).
### HCA DCA tracker
This is a sheet to keep track of communication between wranglers and contributors regarding the singing of DCA. 

### Task Tracker
This is the "enhanced" version of the HCA Atlas Tracker information with ingest and azul data pulled from ingest api and azul api to get the most updated status report, with our internal systems.

We use this to keep track of what projects need to be wrangled, and how close to the wrangling deliverables we are. 
#### How to read
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
#### How to update
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

