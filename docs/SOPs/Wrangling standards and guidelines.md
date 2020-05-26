# Wrangling standards and guidelines

> This document describes wrangling standards and guidelines.

## Definitions

### Primary (responsible) wrangler

Wrangler assigned to a dataset for ingest and monitoring of the status in the HCA

### Secondary (buddy) wrangler

The second wrangler assigned to a dataset for an end-to-end review of the dataset at the beginning of the wrangling process.

### Submitting wrangler

Usually the primary wrangler (even in the case when the actual submission is made by a secondary wrangler due to lack of capacity of the primary wrangler), or secondary wrangler when the primary wrangler permanently hands off the dataset due to lack of capacity - this change has to be doncumented in GitHub issue.

### Expertise wrangler 

Wrangler who has expertise in a particular field to review some tabs in the spreadsheet related to this field after the primary reviewer. Does not have to be assigned, there can be multiple expertise reviewers for one dataset. 

#### Examples:

* Chris: large file transfers, immune
* Dani: ontologies, coding, tool development, protein markers
* Paris: cell lines, stem cells, organoids, MIBI, CODEX, FACS, development, mouse, protocols.io
* Will: 10x, cell-hashing strategies, breast, liver
* Zina: imaging, spatially-resolved transcriptomics, electrophysiology, brain, mouse
* Enrique: tools, ATAC-seq, development
* Marion: sequencing 

Topics to re-assign: 
- bundle structure, linking, library preparation

## Responsibilities

### Responsibilities of the Primary Wrangler

- Maintain contact with the data contributor, cc all emails to wrangler-team@data.humancellatlas.org
- Send and receive [T&C form](https://docs.google.com/forms/d/1qeEgA-B7uhuF34YM1E0vY_2ZXkjQeyWl4f3Zmld_qWI/viewform?edit_requested=true#response=ACYDBNjwU62Otj18nhgVkwiA1U6UCWjXde450SBMpba8FJK4h4oIQUyAtniGUk0) filled out by at least 1 representative of the group/project prior to sending metadata spreadsheet or s3 bucket credentials
- Create a [Github Issue](https://github.com/HumanCellAtlas/hca-data-wrangling/issues/new/choose) for dataset in the hca-wrangling repo and a markdown file in the [in_progress_projects](https://github.com/HumanCellAtlas/hca-data-wrangling/tree/master/projects/in_progress_projects) folder
- Update markdown file when new information comes in
- Keep track of the wrangling process in the Github Issue (date sending/receiving emails, data upload, metadata-schema Github issues creasted for this dataset)
- Create custom metadata spreadsheet for the contributor and do prep-work of renaming the fields that are unclear (Biomaterial ID in Donor, Sprecimen, Cell suspension, etc)
- Keep the most recent version of the spreadsheet in the corresponding Folder in the Google Drive/Brokering/[PROJECTS-IN PROGRESS](https://drive.google.com/drive/folders/118kh4wiHmn4Oz9n1-WZueaxm-8XuCMkA)
- [Create upload area](https://github.com/HumanCellAtlas/hca-data-wrangling/blob/master/docs/SOP_docs/creating_using_upload_areas.md) for the contributor
- Send the custom metadata spreadsheet to the contributor with the [quick guide](https://github.com/HumanCellAtlas/hca-data-wrangling/blob/master/docs/data_contributors_spreadsheet_quick_guide.pdf) and [instructions for data upload](https://github.com/HumanCellAtlas/dcp-cli/blob/mf-submitter-doc/docs/data_submission_guide.md)
- Create Google sheet for the data contributor (if requested) in the Google Drive/Brokering/[PROJECTS-IN PROGRESS](https://drive.google.com/drive/folders/118kh4wiHmn4Oz9n1-WZueaxm-8XuCMkA)
- Maintain communication with the data contributor and reply to any queries - cc all emails to wrangler-team@data.humancellatlas.org
- Receive data from the contributor
- Track errors made by contributor when filling in the spreadsheet, questions to clarify the metadata, etc (for example, in a Google doc in the project's folder in the Google Drive/Brokering/[PROJECTS-IN PROGRESS](https://drive.google.com/drive/folders/118kh4wiHmn4Oz9n1-WZueaxm-8XuCMkA) or elsewhere where the rest of the wranglers can see it) - to be sent to contributor for clarifications
- Curate metadata spreadsheet with [ontologies](http://ontology.staging.data.humancellatlas.org/search?q=&groupField=iri&start=0&ontology=hcao)
- Ask the Secondary Wrangler for an end-to-end review of the project
- Ask the Expertise Wrangler to review specific tabs if needed
- Upload the spreadsheet to validate metadata in [staging](http://ui.ingest.staging.data.humancellatlas.org/)
- Check linking 
- Validate data files - [tools](https://github.com/HumanCellAtlas/hca-data-wrangling/blob/master/docs/wrangler_tool_survey.adoc)
- Submit dataset to [staging](http://ui.ingest.staging.data.humancellatlas.org/)
- If submitting check that the dataset correctly triggers or doesn't trigger secondary analysis - [dcp-diag](https://github.com/HumanCellAtlas/hca-data-wrangling/blob/master/docs/wrangler_tool_survey.adoc#diagnosing-submission-dcp-diag) or in the tracker once it works in staging
- If submitting check that the data is correctly represented in the [Data Browser](http://dss.staging.data.humancellatlas.org) 
- Get final approval of submission including metadata spreadsheet and data files from contributor via email
- Submit dataset to [production](http://ui.ingest.data.humancellatlas.org/)
- Monitor the status of submitted dataset in the [data tracker](https://tracker.data.humancellatlas.org/) notifying corresponding Release engineer for a relevant box in case of any problems. Release engineers for the week can be found in the #dcp-ops Slack channel. 
- Inform data contributor that the dataset is in the queue for submittion to the HCA and that we will send a link to when the datasetis publically available.
- Inform data contributor of successful submission and send link to the submission.
- Move all the corresponding documents to the [finished_projects](https://github.com/HumanCellAtlas/hca-data-wrangling/tree/master/projects/finished_projects) in hca-wrangling repo and to Google Drive/Brokering/[PROJECTS-FINISHED](https://drive.google.com/drive/folders/1FNRVqlhSwwTKoynIHhq5gsILGyRqd6F9)

### Responsibilities of the Secondary Wrangler

- Perform end-to-end review (see below) of the project.
- Keep track of any comments, questions, and suggestions in the GitHub issue Project tracker.
- Ask the Expertise Wrangler to review specific spreadsheet content, if needed.
- Take up wrangling of the project in case of Primary Wrangler not being able to do due to limited capacity, sickness, etc.
- Upload the spreadsheet as new submission to validate metadata in staging
- Upload data files to submission to validate data files and file metadata (also in staging)

### Responsibilities of the Expertise Wrangler

- Review specific tabs of the spreadsheet if asked by either Primary or Secondary Wrangler.

## End-to-end review

End-to-end review includes, but is not limited to, performing the following:

#### Reconstruct experiment based on spreadsheet

Wrangler should be able to generate a graph (by hand or using graph tool) of the experimental design using the HCA metadata model based on the information in the spreadsheet. This includes reconstructing the linking between file and biomaterial entities (the graph "spine") and identifying where the protocols are used. The thing being checked here is that the linking between entities is correct.

Wrangler should be able to account for every biomaterial, file, and protocol entity in the spreadsheet. For example, are all the cell suspensions listed in the Cell suspension tab represented in the linking field of the Sequence file tab? Are there any donors listed in the Donor tab that do not have any associated sequencing or imaging files? The thing being checked here is that every biomaterial, file, and protocol entity in the spreadsheet ends up in an exported bundle.

> One way to do this manually is to copy the first column in one tab and the associated linking column in another tab (e.g. the biomaterial_id in column A of the donor tab and the corresponding biomaterial_id column in the linking column of the specimen tab), paste each column in a new tab, remove duplicate values in each column separately, sort each column separately, and then use Excel's EXACT function to compare row-by-row. If any of those functions returns FALSE, you know there are IDs missing or possibly named differently.

Wrangler should be able to identify whether the same library preparation was sequenced more than once. If the primary wrangler can't confirm this, s/he should check with the data contributor. If the secondary wrangler can't confirm this, s/he should check with the primary wrangler. If either wrangler can confirm this and the answer is yes, wrangler should confirm that the `library_preparation_id` field is filled in correctly. The thing being checked here is whether data consumers will be able to identify which sequencing files came from the same library preparation so they can be analyzed together.

#### Confirm files are uploaded to s3

Wrangler should be able to confirm that every sequencing, imaging, and supplementary file listed in the spreadsheet is located in the associated s3 bucket for that project. File names need to match exactly. The thing being checked here is that all relevant files have been submitted.

Wrangler should be able to identify if there are any extra files in the s3 bucket that are not represented in the spreadsheet. If there are such files, primary wrangler should confirm with contributor (secondary wrangler should confirm with primary wrangler) whether these files are:
 
 1. Misnamed in the spreadsheet. If so, update spreadsheet to the correct name.
 1. Extra files that are not needed for the submission. If so, wrangler should remove them from the s3 bucket.
 1. Extra files that are needed for the submission. If so, wrangler should request contributor to add them to the spreadsheet.
 
 The thing being checked here is that all relevant files are recorded in the spreadsheet.
 
 > One way to do this to list the files in the s3 (aws s3 ls), copy the filenames to a new Excel tab, then copy all the filenames from the metadata spreadsheet into another column in the new tab, sort each column separately, and then use Excel's EXACT function to compare row-by-row. If any of those functions returns FALSE, you know there are files missing from the s3 bucket or the spreadsheet. 

#### Confirm correct ontologies are used

Wrangler should be able to confirm that the correct `ontology` and `ontology_label` fields are filled in for all ontologized `text` fields that have been filled in by contributor. If the contributor has not filled in `ontology` and `ontology_label` fields, the wrangler should do this (ask Dani for help if needed). If these fields have been filled in by contributor, another wrangler, or Dani, review them to make sure they accurately describe what the contributor has filled in for the `text` field.

If after consulting with Dani, no appropriate ontology term can be found, wrangler should request an update to the ontology and indicate in the project markdown file that this was needed in order to ingest this project. The thing being checked here is that all ontologized fields are mapped to the correct ontology term.

**All `ontology` and `ontology_label` fields need to be reviewed by contributor when they are asked to do a final review of their submission.**

#### Suggest optional fields that could be filled

Wrangler should review missing metadata fields and identify any that could be filled in by the wrangler or could easily be requested from the contributor. Typically, the Primary Wrangler should do most of the requesting of additional fields from contributor as s/he is the main person in contact. Some examples of optional fields that might be requested or suggested include:

- Is the read length in the Sequencing file tab missing? Wrangler can calculate this from the submitted files.
- Does the project have a publication or pre-print that the contributor did not record? Wrangler can fill this in.
- Did the contributor reference a published protocol but did not fill out some optional fields for the protocol, like the primer used during library preparation? Wrangler can fill this in.
- Is the data already archived by the contributor did not fill in some of the accessions? Wrangler can do this.
- Did the contributor do a 10x experiment but did not fill in any of the 10x-specific fields? Wrangler can ask the contributor whether they can fill these fields in.

The thing being checked here is that wrangler-led submissions are high-quality. Wranglers should use their own judgement here regarding how many optional fields to request from a contributor or fill in themselves. Wranglers should strive to ingest high-quality examples of metadata in order to set a high standard for future contributors as well as test the DCP infrastructure and the HCA metadata standard. 

**All fields added by a wrangler need to be reviewed by contributor when they are asked to do a final review of their submission.**
