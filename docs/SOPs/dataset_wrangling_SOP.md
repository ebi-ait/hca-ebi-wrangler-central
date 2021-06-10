---
layout: default
title: Wrangling datasets SOP
parent: SOPs
has_children: false
last_modified_date: 22/03/2020
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>
# Wrangling Datasets SOP
{: .no_toc }

## Background
{: .no_toc }

This SOP document aims to describe the process of receiving new datasets from contributors and uploading their metadata and data to ingest for archiving in EBI archives and submission to DCP2.0.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Project Management

There are some general project management tasks when working with new datasets to ensure all team members can track their status.

New contributors will almost always contact us via the wranglers email list. When we work with them to get their projects submitted, the wranglers email list should be copied into all emails.
1. Create a [project tracker ticket](https://github.com/ebi-ait/hca-ebi-wrangler-central/issues/new?assignees=&labels=dataset&template=project_tracker.md&title= ) to track dataset progress should be created in the `hca-ebi-wrangler-central` repo 
2. Add the dataset to the [dataset tracker sheet](https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0) 
  * Change `hca_status` to 'in progress'
  * Ensure all required fields are filled out
  * Ensure you are listed as the `primary_wrangler`
3. Create a new folder to store the dataset metadata in the [Brokering drive](https://drive.google.com/drive/folders/118kh4wiHmn4Oz9n1-WZueaxm-8XuCMkA) 

### Tracking wrangling progress

Wrangling progress is tracked primarily through movement of the `project tracker ticket` through the pipelines on the [Dataset wrangling status](https://github.com/ebi-ait/hca-ebi-wrangler-central#workspaces/dataset-wrangling-status-5f994cb88e0805001759d2e9/board?repos=261790554) Zenhub Board. 

| Pipeline            | When                                   | Explanation                                                                                                                                 |
|---------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| New Issues          | Auto-placed                            | This pipeline is where issues automatically end up but issues shouldn't stay here for long |
| Queued for Wrangling      | When created                           | Issues should be placed here when they are created but before a wrangler actively starts working on it |
| Wrangling           | When in progress                       | The primary wrangler moves the tracker ticket here when they have started working on it |
| Secondary reviewing | When review starts                     | The secondary wrangler moves the tracker ticket here when they start reviewing |
| Archiving           | When archiving process starts          | The primary wrangler moves the tracker ticket here when Archiving starts (if required), if already archived would skip to ready for export |
| Ready for export          | When ready to be exported              | The primary wrangler moves the tracker ticket here when all that is left is to hit submit|
| AE/SCEA brokering   | When ready to be converted to MAGE-TAB | The primary wrangler moves the tracker ticket here when it is ready to be converted to MAGE-TAB to give to ArrayExpress of SCEA if suitable |
| Needs update        | If project needs an update             | A wrangler moves the tracker ticket here if the project requires some kind of update |
| Stalled             | If project becomes stuck               | If project spends more than 2 weeks with no progress, the ticket should be moved here and label applied to indicate reason  |
| Finished            | When finished                          | The primary wrangler moves the ticket here to indicate all work is complete. The ticket should be closed at the end of the sprint. |

[Labels](https://github.com/ebi-ait/hca-ebi-wrangler-central/labels) are also applied to tickets to provide further information about the ticket. Definitions for each label and when they should be applied can be [found here](https://github.com/ebi-ait/hca-ebi-wrangler-central/labels).

**If you are wrangling a dataset from a published project, click [here](#for-published-datasets-only). If not, continue reading the following directions.** 

## Early contact with contributors

The wranglers and managers are first notified of a new contributor by email to a team-wide email list and as a team they decide who will be responsible for the new dataset. Work is divided between EBI and UCSC wranglers based on convenience, time zones, current workload and existing relationships. Generally speaking, UCSC wranglers are responsible for contributor relationships from Central USA, Central America and the Pacific rim region, whereas EBI wranglers are responsible for Europe, Africa, Central Asia, Eastern USA and most of South America. 

Once a primary wrangler is assigned, they will communicate with the contributor via email and set up virtual or in-person meetings to discuss their project needs. Specific guidance on how to communicate with contributors can be found in the [Contributor communication SOP](contributor_communication_SOP).

### Finding out about the dataset

If nothing is known about the project, the first step is to find out enough information in order to create a customised spreadsheet template for the contributor to fill in. This can be done either by:

1. Sending the contributor the [HCA Dataset Questionnaire form](https://docs.google.com/forms/d/e/1FAIpQLSdjPk2Z6xYozds53ycvXo57PvFsyqOF6XMpSWCVNTpQYalZzQ/viewform?usp=sf_link) 

[suggested template email](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/contributor_communication_SOP#first-contact---data-questionnaire){: .btn .btn-blue }

2. Setting up an in-person or video call. The questions in the HCA Dataset Questionnaire form can be used as guide to know what questions to ask of the contributor

If you already have some information about the dataset and don’t need the contributor to fill in the entire Dataset Questionnaire it is still important to find out answers to the following questions:

- Does your team have consent for public release for all the raw sequencing data included in this dataset?

- Do you have a specific release date or any publication embargo requirements?

### Terms and conditions form

Before metadata and data can be received from contributors they are required to fill in a terms and conditions agreement form which confirms open consent to their data and other agreements ([Terms and conditions form](https://docs.google.com/forms/d/e/1FAIpQLScYrxmDb9rD38J7k0lmfhM7JKmKgSaXegx7Imlbecsu4vNrcg/viewform)). This can be sent to them either straight away or after asking them and confirming that they do have full consent for public release. 

Set of Template emails: 

[Template Emails](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/contributor_communication_SOP#template-emails){: .btn .btn-blue }

*What do I do if a contributor’s data is not fully consented for public release?*

Currently the HCA DCP cannot accept datasets without full open consent for public release. We are currently working on a solution to help contributors make their data and metadata accessible via managed access. See [Contributor Communication SOP](contributor_communication_SOP) for further guidance on how to respond to these enquiries.

## Gathering data & metadata

### For published datasets only 

With a published dataset, there is no requirement for the terms and conditions form or template emails to send to the contributor. First, start by getting some initial information about the dataset from reading the published paper, and checking if there is data that is publicly available. 

Once you have an understanding of which biomaterials, protocols, and processes are used, it is time to generate a metadata spreadsheet. As below, the spreadsheet can be generated using the  [`schema-template-generator`](https://github.com/HumanCellAtlas/schema-template-generator)but as there is no contributor involved, do make the spreadsheet as comprehensive as you think is necessary. 

Instead of the iterative process of the contributor filling in what they can, the wrangler reviewing, curating, and asking questions, there is only you (the wrangler) working with the spreadsheet. It is easy to get stuck, so don’t forget that you’re working as a team and get a second opinion if necessary! 

After generating the spreadsheet, we move onto raw data upload. There is no contributor to upload their data manually, so we must take on that role and: 
* Create an upload area
* Upload files to the upload area. 

There is a useful [script](https://ebi-ait.github.io/hca-ebi-wrangler-central/tools/handy_snippets.html#uploading-files-to-an-s3-bucket-from-the-archives) for uploading files to an s3 bucket, which can speed up the process tremendously. Note that this step does not need to be completed now, and can wait until after the metadata spreadsheet has been gathered. 

Then move onto the [‘curating metadata’](#curating-metadata) section. 

### Spreadsheet template generation

Once the terms and conditions form has been submitted, and you have some initial information about the dataset from the questionnaire or meeting, it is time to generate a spreadsheet for the contributor to fill in. The spreadsheet is generated using the [`schema-template-generator`](https://github.com/HumanCellAtlas/schema-template-generator) repo that can be cloned and run locally, see README for install and usage instructions.

The spreadsheet should be as simple as possible for the given experiment so that it is more easily understandable for the contributor so only select schema and properties that are relevant to their experiment.

After the spreadsheet is generated some manual steps can help contributors understand the spreadsheet including:
- Ordering of tabs and ordering protocols between biomaterials can help contributors understand our graphical experiment model
- Ordering of columns: Move linking columns e.g. `INPUT DONOR ORGANISM` to be in the first few columns of the sheet to be more visible
- Ensure every tab that requires a link has a linking column (these are easy to miss)
- Delete or hide columns that you know aren’t relevant (if you forgot to uncheck during initial generation)
- Pre-fill any metadata you already know (optional): if the dataset has a publication it is normally possible to gain information from the publication and prefill it into the spreadsheet

Once you have a customised and potentially pre-filled spreadsheet it can be sent to the contributor along with the contributor spreadsheet guide. It is generally an iterative process of the contributor filling in what they can, the wrangler reviewing, curating and asking questions before further curation until the metadata is complete. 

## Raw Data (fastq) and Processed Data Upload  

### AWS User for Contributors

In order for a contributor to upload their data, they would need their own AWS user that is assigned to the hca-contributor group.

A request for an account should be filed as [a new ticket](https://github.com/ebi-ait/hca-ebi-wrangler-central/issues/new?assignees=&labels=operations&template=new-contributor-account.md&title=contributor+account+for%3A+%3Ccontributor-name%3E) for the ingest team. The board is monitored regularly so the new ticket would be picked up within the day.

_**This is done by a team member with a developer role.**_

1. Create an AWS user
   
   Use the name part of the email address for the account name.
  
```shell
# to add user walter.white@example.com as a contributor
aws iam create-user --user-name walter.white --tags Key=project,Value=hca Key=owner,Value=tburdett Key=service,Value=ait
aws iam add-user-to-group --group hca-contributor --user-name walter.white
# generate secrets 
aws iam create-access-key --user-name walter.white 
```

2. The developer need to send the generated access key in an email to the person (usually a wrangler) who requested the account for the contributor.  

### Data upload Procedure

_**This is done by a wrangler.**_ 

1. Obtain the access key from a developer ([previous step](https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/docs/SOPs/dataset_wrangling_SOP.md#aws-user-for-contributors))
2. Create an upload area using the guide: [how to create an upload area for the contributors using the hca-util tool]( https://github.com/ebi-ait/hca-documentation/wiki/How-to-administrate-upload-areas-and-transfer-data-using-hca-util)
3. Get the UUID from the created upload area
Send these two sets of information separately to the contributor to minimise the chance of them falling into the wrong hands and being misused.

* **Contributor AWS Access keys** are not considered secure and can be sent in the main `wrangler-team` email thread, usually in the same email with the first spreadsheet and [upload instructions](https://github.com/ebi-ait/hca-documentation/wiki/How-to-upload-data-to-an-upload-area-using-hca-util).
* **Upload area UUID** is a secure piece of information that should be shared in a separate email with only the contributor and primary wrangler 

## Curating metadata

### Ontology curation

For ontologised fields, wranglers need to assign an ontology term that best suits the text provided by the contributor. The ontologised fields must be present within the latest version of the HCAO and meet the graph restriction present in the schema. The [ontology filler tool](https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/src/fill_ontologies.py) can help with this process, but should be reviewed once complete. 

If a wrangler cannot find an accurate ontology term and believes a term should be added to the relevant ontology, they should follow the [Request ontology terms SOP](request_ontology_terms).

### General metadata curation tips

Wranglers should endeavour to fill in as much metadata as is possible. We have a fairly minimal set of required fields but we should seek to provide as much detail as possible. 

Examples of metadata that we strive for even if it is not strictly required:
General demographics - Age, weight, ethnicity for human donors
Basic medical info - cause of death, smoking status, alcohol status

If donors are from CBTM or HDBR we have direct routes of obtaining more detailed metadata if it hasn’t been provided by the contributor.

- `organ` or `model_organ` should be the broad major organ type, not a system
- The `organ_part` or `model_organ_part` should be the most specific organ part available
- `biomaterial_id`s should be either consistent with the publication or the tissue provider to allow identification of biomaterials with shared donors
- Try to encourage the contributor to provide a meaningful identifier, not just a single digit

## Contributor Matrix and cell types SOP 
For each project, wranglers should endeavour to find an expression matrix and if not embedded within that matrix, a listing of cell type annotations. These are generally linked from a publication, present as a supplementary file on the publication, GEO or ArrayExpress submission.

The preferred formats for matrix files are:
* `loom`
* `h5ad`
* RObj?

Where either the expression matrix or cell type annotations cannot be found, the primary wrangler should write an email to the contributor/author asking for them to provide the appropriate files in the preferred format. If the contributors cannot provide in the preferred format, we will take whatever is available. It is important to be able to link the cell type annotations to the cell suspensions and/or cell barcodes provided in the metadata.

### Filling in metadata about the files

For each expression matrix or cell type annotation file that is found, a row needs to be filled in the metadata spreadsheet, in the ‘Analysis file’ tab. Analysis files can be linked to sequence files or biomaterial entities via processes; This is done in the spreadsheet in the same way that other entities are linked. Information related to the analysis protocol is captured in the Analysis_protocol entity (See the Analysis protocol tab) linked to the process

The best practice is to link the analysis files to sequence file entities, if possible. Alternatively, you can also link the analysis files to cell suspension entities. This is currently done by adding the ‘Input Cell Suspension ID’ column to the ‘Analysis File’ tab and adding the linked cell suspensions to the cell.

The gene expression matrix and cell annotations files should be added to the S3 bucket in the ingest-area together with raw data files, for instructions on how to use hca-util to do this, see ['here'](https://github.com/ebi-ait/hca-documentation/wiki/How-to-upload-data-to-an-upload-area-using-hca-util)

![image](https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/docs/SOPs/Cgms_screenshot.png?raw=true)


## Metadata Validation
Once the spreadsheet is considered complete by the primary wrangler, there are two phases of metadata validation that can be completed.

### Spreadsheet and JSON schema validation
The primary wrangler should upload the spreadsheet to the [ingest production ui](https://contribute.data.humancellatlas.org/) to check the validity of the spreadsheet.

This can be done in one of two ways

#### 1. Full spreadsheet with project metadata

To create a new project from a full spreadsheet:
1. go to the `ALL SUBMISSIONS` tab then click the `Upload New Submission` button in the top right. 
    1. If all the metadata is valid, you can move on to uploading the fastq files data. 
    1. If any metadata is invalid,  you will need to resolve any errors or problems. This can be done directly in the UI or by uploading a new spreadsheet to the existing project. 
1. To Upload a fixed spreadsheet to the project:
    1. Fix the errors in the spreadsheet and return to the existing project in the ui
    1. Click the `3. Upload` tab to view the submissions
    1. Delete the submission with errors by clicking the trash icon next to the submission
    1. Go to the `3. Upload` tab and click the `Submit to Project` button to upload the fixed spreadsheet. If the button doesn't appear try refreshing the page.
    1. repeat these steps until you have a project with valid metadata
1. To edit in the UI
    1. change any fields that need to be edited
    1. click save
1. When all metadata is valid, proceed to upload the required files

#### 2. Pre-registered project that already exists in ingest

If attaching a submission to a project that already exists in the ingest ui: 
1. Go to the project page
1. Click the `Edit project` button 
1. Go to the `3. Upload` tab and click the `Submit to Project` button to upload the spreadsheet
    1. If any metadata is invalid,  you will need to resolve any errors or problems. This can be done directly in the UI or by uploading a new spreadsheet to the existing project. 
1. To upload a fixed spreadsheet to the project:
    1. Fix the errors in the spreadhseet and return to the existing project in the ui
    1. Click the `3. Upload` tab to view the submissions
    1. Delete the submission with errors by clicking the trash icon next to the submission
    1. Go to the `3. Upload` tab and click the `Submit to Project` button to upload the fixed spreadsheet. (If the button doesn't appear try refreshing the page.)
    1. repeat these steps until you have a project with valid metadata
1. To edit directly in the ui, click the pencil symbol to open the editing form
    1. change any fields that need to be edited
    1. click save  
1. proceed to upload the required files

Please note:
{: .label .label-purple }

* When uploading a spreadsheet to an existing project, no project metadata is uploaded or updated, any updates to project metadata including contributors, publications and funders must be edited directly in the UI
* Once a project has been created in the UI, it is best practice to retain the project's unique identifier throughout the submission and validation process, so please only delete the project if there are serious issues with project level metadata that cannot be fixed easily in the UI
* There should never be duplicate projects in the production ui, if you do need to reupload an entire project, please delete the existing project before re-uploading a spreadsheet. To delete a project in the ui:

1. If the project has no submissions:
    1. go to the project page in the ui
    1. Scroll to the bottom of the page and click the trash icon next to the 'Edit Project' button
1. If the project has an unsubmitted submission:
    1. go to the project's page in the ui
    1. go to the `3. Upload` tab
    1. click the trash symbol next to the submission
    1. go to the `1. Project` tab
    1. scroll down and click the trash icon next to the 'Edit Project' button

If any issues are encountered when trying to upload, update or delete projects or submissions in the ui, please post the issue and project uuid in the #dcp-ops channel and tag @ingest-devs

### Experimental graph validation
The ingest graph validator allows wranglers to visualise the experimental graph of the experiment and also performs some tests to check against our current graph assumptions. 

Please follow the documentation in the [ingest graph validator repository](https://github.com/ebi-ait/ingest-graph-validator) to run the current graph validator tests.

## Secondary Review

Once the spreadsheet has passed both phases of validation, the primary wrangler should ask another wrangler in the team to review the spreadsheet and suggest any required edits or updates. Once someone asks for secondary review, they should move the ticket to the `Secondary wrangling` pipeline on the tracking board.

If any edits or updates are made, the existing submission in ingest will need to be deleted and the new spreadsheet uploaded in its place. 

If any changes may have also affected the linking in the spreadsheet it should also be run through the ingest-graph-validator again.

A detailed guide to performing secondary review [can be found here](secondary_review_SOP).

Once both the Primary and Secondary wrangler are happy with the submission and it is valid in ingest, move the dataset tracker ticket to the `Ready to Export` pipeline of the [Dataset wrangling board](https://github.com/ebi-ait/hca-ebi-wrangler-central#workspaces/dataset-wrangling-status-5f994cb88e0805001759d2e9/board?repos=261790554) and change the `hca_status` to 'ready to export' in the [Dataset Tracking Sheet](https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0). The data files can now be moved from the contributor bucket into the ingest upload area.

## Transferring data from `hca-util` upload area to ingest upload area

Once the contributor has uploaded all the data that is specified for the project or you have transferred the raw data files from the archive into an `hca-util` upload area and you have a valid metadata submission in the ingest UI, follow the [hca-util guide](https://github.com/ebi-ait/hca-documentation/wiki/How-to-administrate-upload-areas-and-transfer-data-using-hca-util#sync-data-to-the-ingest-s3-bucket) to sync the data to the `Upload Area Location` that is specified on the submission at the bottom of the `Data` tab. 

## Completing the submission

Once all the files have been validated the project will be ready for submission. 

If wrangling the project with direct input from a contributor, the primary wrangler should [email the contributor](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/contributor_communication_SOP.html#final-confirmation-before-submission) to confirm:
- They are happy with the final spreadsheet and curated ontologies, and 
- The date they have identified for the data and metadata to be released publicly

The path after submission can go one of several ways:
1. the project needs to go to DCP and EBI Archives -> Tick both the `Submit to the EMBL-EBI public archives` and `Submit to the Human Cell Atlas` checkboxes
1. The project needs to go to DCP only -> Tick only `Submit to the Human Cell Atlas` checkbox
1. The project needs to go to EBI archives only (if it can't currently be exported to DCP) -> tick only `Submit to the EMBL-EBI public archives` checkbox

Always untick the `Delete the upload area and data files after successful submission.` checkbox.

### Archiving the submission

If the submission needs to be archived, ensure you have the `Submit to the EMBL-EBI public archives and get accessions...` check box ticked. If not, proceed to [exporting the submission to DCP2](#exporting-the-submission-to-dcp2)

The project should go into `Archiving` status, at this point you need to inform the developer on operations who will assist with the Archiving process, which is currently semi-manual.

Further documentation for the archiving process can be found here: [Ingestion to Archives Instructions](https://docs.google.com/document/d/1S4fyCSqB3nLrCUssNMwSp6ff8tmeipMi_slnXW2Lrq4/edit?pli=1#heading=h.n3qy5yl0auvs)

After the project has been Archived, if the `Submit to the Human Cell Atlas...` checkbox was also ticked, the project should proceed to `Exporting` status and the following steps should be followed from step 2 onwards.

### Exporting the submission to DCP

1. As soon as a dataset is ready for export, the wrangler should hit the submit button in the UI with the `Submit to the Human Cell Atlas...` checkbox ticked to trigger export and note the project UUID.
    1. *`Current mechanism`*: Wrangler retrieves the project UUID from the URL when viewing the project in the ingest browser.
2. The submitting wrangler checks export is complete.
    1. *`Current mechanism`*: wrangler checks status in the UI, will change from exporting to exported. (This will take ~1-4 hours for most projects)
    2. If export is “stuck” in exporting for more than 4 hours, Notify the ingest operations developer via the dcp-ops slack channel notifying (@claire rye who will make a ticket (the slack group doesn't work) and providing the project UUID so they can review the logs and work out what has happened. They will work with the wrangler to resolve this and re-export if necessary.
3. The wrangling team is notified of export
    1.  *Current mechanism*: The submitting wrangler changes the status in the [Dataset Tracking Sheet](https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0) to `exported` and adds the project uuid to the `ingest_project_uuid` field
    2.  *Current mechanism*: The submitting wrangler moves the dataset wrangling ticket either to the `AE/SCEA backlog` (if being brokered to SCEA) or to the `Finished` pipeline
4. The Broad data import team are notified of successful export 
    1. *`Current mechanism`*: The submitting wrangler submits the [HCA Import request for Production Releases](https://docs.google.com/forms/d/e/1FAIpQLSeokUTa-aVXGDdSNODEYetxezasFKp2oVLz65775lgk5t0D2w/viewform?gxids=7628) (see [values below](#import-form-details-for-dcp-data-releases)) the broad import team will automatically be notified on the #dcp-ops Slack channel. 
5. The submitting wrangler is notified that import and snapshot has been successful or if there are issues for EBI to investigate
* *`Current mechanism`*: Broad data import team will notify via slack in the dcp-ops channel slack, notifying @Hannes and @Trevor Heathorn when import and snapshot has been successful or if issues are found and pass on to the browser team.
6. UCSC Browser team will notify submitting wrangler and Broad team when indexed and in the browser or if issues are encountered.
* *`Current mechanism`*: Via slack in the dcp-ops channel notifying (who?) when a dataset is in the browser or if there was any issue with indexing.
7. When a project is available in the browser, a wrangler will do a final check that everything looks ok and notify @here on the data-ops channel. 
8. If issues occur at any point then corrections are made as updates and then re-exported. 
* *`Current mechanism`*: In order to re-export, the wrangler will notify the ingest developer on operations to reset the project state from exported to valid.
* The ingest developer should also delete any contents of the project staging area in the staging bucket from the failed export. 
* Wrangler will trigger export by hitting submit and following steps 2-7 until the project is available and looks ok
9. When the project is available in the browser, the wrangler will [email](https://github.com/ebi-ait/hca-ebi-wrangler-central/issues/233) the contributor or contacts from the publication to inform them of the URL where the project is available
10. The wrangler proceeds with brokering to SCEA or marks the project as `Finished` by updating the `hca_status` in the Dataset Tracking sheet

#### Import Form Details for DCP data releases

| Field                     | Explanation                                                       |
|---------------------------|-------------------------------------------------------------------|
| Email address             | So you can be contacted if any issues with import                 |
| Release #                 | The integer number of the ~monthly release cutoff                 |
| Google storage cloud path | `gs://broad-dsp-monster-hca-prod-ebi-storage/prod/[PROJECT_UUID]` |
| Is this new data, updated data or analysis results? | Choose the appropriate response, 'Brand new data' for a new, never been exported project, or 'An update to data that is already in production' if it is an update. |
| Additional info           | Any other notes you want to communicate to the import team. |
  
#### Import Form Details for DCP testing
  
| Field                     | Explanation                                                       |
|---------------------------|-------------------------------------------------------------------|
| Email address             | So you can be contacted if any issues with import                 |
| Release #                 | `Test export`                                                     |
| Google storage cloud path | `gs://broad-dsp-monster-hca-prod-ebi-storage/staging/[PROJECT_UUID]` |
| Additional info           | Fill in any special instructions such as details like the environment, catalog and dataset ID. If not sure ask import team on slack  |

Notes
{: label label-blue }

* UCSC & EBI will export on demand, and notify the Broad
* Broad will batch import once prior to the monthly release
* Responsibility for who deletes the contents of the staging area is still being decided.
* This is likely to evolve as we go, so please note issues with completing this process so we can improve it.
* [See this sheet](https://docs.google.com/spreadsheets/d/1xApi-qay1H9ef2JQAmPNXH63Xy-0cNYBN4wBaq-YC3U/edit?usp=sharing) for a rolling list of projects where a an import request form has been filled out.

<i class="fas fa-exclamation-triangle"></i> **Warning**: Wranglers should be aware of when prod releases are occurring and not upload/submit until after the release to that environment is completed. Releases do not currently follow a set schedule so stay tuned to updates posted in the `#hca` slack channel in the AIT workspace. See the [Ingest release SOP](https://github.com/HumanCellAtlas/ingest-central/wiki/Ingest-Release-SOP#release-schedule) for more details.

Additionally, move all the corresponding documents to the [finished_projects](https://github.com/HumanCellAtlas/hca-data-wrangling/tree/master/projects/finished_projects) in hca-wrangling repo and to Google Drive/Brokering/[PROJECTS-FINISHED](https://drive.google.com/drive/folders/1FNRVqlhSwwTKoynIHhq5gsILGyRqd6F9)

## Brokering to SCEA

See documentation on the [hca-to-scea repo](https://github.com/ebi-ait/hca-to-scea-tools)
