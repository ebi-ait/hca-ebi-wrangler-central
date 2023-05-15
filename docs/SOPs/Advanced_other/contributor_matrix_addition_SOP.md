---
layout: default
title: Contributor matrix and cell types
parent: Advanced & other SOPs
grand_parent: SOPs
nav_order: 2
---
# __DEPRECATED?__

# Contributor matrix and cell type annotations

{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Getting contributor matrix files

For each project, wranglers should endeavour to find an expression matrix and if not embedded within that matrix, a listing of cell type annotations. These are generally linked from a publication, present as a supplementary file on the publication, GEO or ArrayExpress submission.

The preferred formats for matrix files are:
* `loom`
* `h5ad`
* `RData`
* `RDS`

Where either the expression matrix or cell type annotations cannot be found, the primary wrangler should write an email to the contributor/author asking for them to provide the appropriate files in the preferred format. If the contributors cannot provide in the preferred format, we will take whatever is available. It is important to be able to link the cell type annotations to the cell suspensions and/or cell barcodes provided in the metadata.

## Filling in metadata about the files

For each expression matrix or cell type annotation file that is found, a row needs to be filled in the metadata spreadsheet, in the ‘Analysis file’ tab. Analysis files can be linked to sequence files or biomaterial entities via processes; This is done in the spreadsheet in the same way that other entities are linked. Information related to the analysis protocol is captured in the Analysis_protocol entity (See the Analysis protocol tab) linked to the process

The best practice is to link the analysis files to sequence file entities, if possible. Alternatively, you can also link the analysis files to cell suspension entities. This is currently done by adding the ‘Input Cell Suspension ID’ column to the ‘Analysis File’ tab and adding the linked cell suspensions to the cell.

The gene expression matrix and cell annotations files should be added to the S3 bucket in the ingest-area together with raw data files, for instructions on how to use hca-util to do this, see ['here'](https://github.com/ebi-ait/hca-documentation/wiki/How-to-upload-data-to-an-upload-area-using-hca-util)

![image](https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/assets/images/matrices_screenshots/cgms_screenshot.png?raw=true)






The following process here is outdated, but kept for recording: 
For each file that is found, a row needs to be filled in the [`contributor_matrices_metadata`](https://docs.google.com/spreadsheets/d/1m9tXswoNAEYJDVlCKqc9L6p0c7hbOwddkQxdqxXydqY/edit#gid=0) found in the [Contributor Matrices folder](https://drive.google.com/open?id=1FMjJwYamMyuCtNJoTiA30kM3vsL6Q8LD) in the Brokering folder.



| Field                       | Definition                                                                                                                   |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------|
| date_added                  | the date the row was added to the sheet in YYYY-MM-DD format.                                                                |
| project_uuid                | the uuid of the project                                                                                                      |
| project_shortname           | the shortname of the project                                                                                                 |
| gex matrix                  | Y/N whether the file is a count matrix                                                                                       |
| cell type                   | Y/N whether the file contains cell type annotations                                                                          |
| other                       | Y/N whether the file is some other kind of file                                                                              |
| file_name                   | name of the file, unchanged from where it was sourced                                                                        |
| file_source                 | Where the file was sourced from: contributor/geo/arrayexpress [any other categories needed here?]                            |
| genusSpecies                | the species in that file, usually Homo sapiens or Mus musculus                                                               |
| developmentStage            | the developmental stage present in the matrix, if more than one species, need to specify which stage goes with which species |
| organ                       | the organ present in the matrix, if multiple other fields, need to deconvolute                                               |
| libraryConstructionApproach | the ontology label of the `library_preparation_method` used to generate the matrix/file, if multiple, need to unambiguously deconvolute            |
| uploaded                    | Whether it has been uploaded into the google bucket for matrices                                                             |
| date_imported               | the date the file was imported by UCSC in YYYY-MM-DD format (filled in by UCSC when import is performed)                     |

If there are multiple values in one cell, they need to be delimited with comma

## Uploading the files to the google bucket

Files need to be uploaded to the [google bucket](https://console.cloud.google.com/storage/browser/hca-prod-ebi-matrices)

Files from the same project are put into a folder `[project_uuid]-[project_shortname]`

If you can't access the bucket in the console link above, you need to request access from the UCSC browser team. Also check whether you have the option to upload/download/delete.

### Uploading through the console

1. Go to the console website https://console.cloud.google.com/storage/browser/hca-prod-ebi-matrices
1. Select either `UPLOAD FILES` or `UPLOAD FOLDER` and choose the files/folder to upload
1. Don't navigate away from the page until the upload is complete
1. Once files are confirmed as uploaded, mark in the spreadsheet that they are uploaded

### Uploading through `gsutil` cli tool

1. Install Google Cloud SDK https://cloud.google.com/sdk/docs/install
1. Authorise with your google account https://cloud.google.com/sdk/gcloud/reference/auth/login 
1. Use [`gsutil cp`](https://cloud.google.com/storage/docs/gsutil/commands/cp) to copy files to the bucket, something like:

```
# to copy a file
gsutil cp <name of file> gs://hca-prod-ebi-matrices/<name of folder>
# to copy a directory of files
gsutil cp -r <name of directory> gs://hca-prod-ebi-matrices/
```

for more gsutil actions see: https://cloud.google.com/storage/docs/gsutil
