---
layout: default
title: Contributor dataset SOP
parent: SOPs
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>
# Wrangling Contributor’s Datasets SOP
{: .no_toc }

## Background
{: .no_toc }

This SOP document aims to describe the process of receiving new datasets from contributors and uploading their metadata and data to ingest for archiving in EBI archives and submission to DCP2.0. This SOP was last updated on 2020-06-11 and is subject to change as the AIT HCA team software evolves. It will be updated to reflect changes.

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
| New Issues          | Auto-placed                            | This pipeline is where issues automatically end up but issues shouldn't stay here for long                                                  |
| To be wrangled      | When created                           | Issues should be placed here when they are created but before a wrangler actively starts working on it                                      |
| Wrangling           | When in progress                       | The primary wrangler moves the tracker ticket here when they have started working on it                                                     |
| Secondary reviewing | When review starts                     | The secondary wrangler moves the tracker ticket here when they start reviewing                                                              |
| Archiving           | When archiving process starts          | The primary wrangler moves the tracker ticket here when Archiving starts (if required)                                                      |
| Exporting           | When ready to be exported              | The primary wrangler moves the tracker ticket here when it is ready to be exported                                                          |
| AE/SCEA brokering   | When ready to be converted to MAGE-TAB | The primary wrangler moves the tracker ticket here when it is ready to be converted to MAGE-TAB to give to ArrayExpress of SCEA if suitable |
| Needs update        | If project needs an update             | A wrangler moves the tracker ticket here if the project requires some kind of update                                                        |
| Stalled             | If project becomes stuck               | If project spends more than 2 weeks with no progress, the ticket should be moved here and label applied to indicate reason                  |
| Finished            | When finished                          | The primary wrangler moves the ticket here to indicate all work is complete. The ticket should be closed at the end of the sprint.          |

[Labels](https://github.com/ebi-ait/hca-ebi-wrangler-central/labels) are also applied to tickets to provide further information about the ticket. Definitions for each label and when they should be applied can be [found here](https://github.com/ebi-ait/hca-ebi-wrangler-central/labels).


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

## Raw data upload (fastq)

In order for a contributor to upload their data, you will need to provide them with a data upload area UUID as well as a set of contributor AWS access keys. 

These two sets of information need to be sent separately to minimise the chance of them falling into the wrong hands and being misused.

* **Contributor AWS Access keys** are not considered secure and can be sent in the main `wrangler-team` email thread, usually in the same email with the first spreadsheet and [upload instructions](https://github.com/ebi-ait/hca-documentation/wiki/How-to-upload-data-to-an-upload-area-using-hca-util).
* **Upload area UUID** is a secure piece of information that should be shared in a separate email with only the contributor and primary wrangler 

### Transferring a contributor's raw data to ingest UI using `hca-util sync`

In order to create the upload area, follow the instructions on [how to create an upload area for the contributors using the hca-util tool]( https://github.com/ebi-ait/hca-documentation/wiki/How-to-administrate-upload-areas-and-transfer-data-using-hca-util). These instructions will guide you to create an upload area for a contributor to upload their data, but also how to then transfer that data once uploaded to the ingest production s3 bucket using the same tool.

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

## Metadata Validation
Once the spreadsheet is considered complete by the primary wrangler, there are two phases of metadata validation that can be completed.

### Experimental graph validation
The ingest graph validator allows wranglers to visualise the experimental graph of the experiment and also performs some tests to check against our current graph assumptions. 

Please follow the documentation in the [ingest graph validator repository](https://github.com/ebi-ait/ingest-graph-validator).

### Spreadsheet and JSON schema validation
The primary wrangler should also upload the spreadsheet to the [ingest production ui](https://ui.ingest.archive.data.humancellatlas.org/) to check the validity of the spreadsheet.

To create a new submission from a spreadsheet, go to the `ALL SUBMISSIONS` tab then click the `Upload New Submission` button in the top right. If the metadata is valid, you can move on to uploading the fastq files data. If it is invalid, you will need to resolve any errors or problems and re-upload the metadata sheet again and repeat this process until it is valid.

## Secondary Review

Once the spreadsheet has passed both phases of validation, the primary wrangler should ask another wrangler in the team to review the spreadsheet and suggest any required edits or updates. Once someone asks for secondary review, they should move the ticket to the `Secondary wrangling` pipeline on the tracking board.

If any edits or updates are made, the existing submission in ingest will need to be deleted and the new spreadsheet uploaded in its place. 

If any changes may have also affected the linking in the spreadsheet it should also be run through the ingest-graph-validator again.

A detailed guide to performing secondary review [can be found here](secondary_review_SOP).

Once both the Primary and Secondary wrangler are happy with the submission and it is valid in ingest, the data files can be moved from the contributor bucket into the ingest upload area.

## Completing the submission

Once all the files have been validated the project will be ready for submission. Before hitting submit, the primary wrangler should email the contributor to confirm:
They are happy with the final spreadsheet and curated ontologies
The date they have identified for the data and metadata to be released publicly

<i class="fas fa-exclamation-triangle"></i> **Warning**: Wranglers should be aware of when prod releases are occurring and not upload/submit until after the release to that environment is completed. Releases do not currently follow a set schedule so stay tuned to updates posted in the `#hca` slack channel in the AIT workspace. See the [Ingest release SOP](https://github.com/HumanCellAtlas/ingest-central/wiki/Ingest-Release-SOP#release-schedule) for more details.

Once you hit submit the project should go into ‘Archiving’ status. The precise process for identifying which of the paths the dataset will take after submission is currently being formalised by ingest. Until then the wrangler needs to inform the ingest team manually.

The path after submission can go one of several ways:
1. the project needs to go to DCP2 and EBI Archives
1. The project needs to go to DCP2 only
1. The project needs to go to EBI archives only 

 <i class="fas fa-exclamation-triangle"></i> **Warning** as at 15/12/2020 we are not currently following paths 1 & 2 because we can't currently export to DCP2, hopefully this will be resolved in early 20221

Further documentation for this process can be found here: [Ingestion to Archives Instructions](https://docs.google.com/document/d/1S4fyCSqB3nLrCUssNMwSp6ff8tmeipMi_slnXW2Lrq4/edit?pli=1#heading=h.n3qy5yl0auvs)



