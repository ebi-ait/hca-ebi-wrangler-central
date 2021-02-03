---
layout: default
title: Contributor matrix and cell types SOP
parent: SOPs
---

# Attaching Contributor matrix and cell types to projects

{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Getting contributor matrix files

For each project, wranglers should endeavour to find an expression matrix and if not embedded within that matrix, a listing of cell type annotations. These are generally linked from a publication, present as a supplementary file on the publication, GEO or ArrayExpress submission.

Where either the expression matrix or cell type annotations cannot be found, the primary wrangler should write an email to the contributor/author asking for them to provide the appropriate files. It is important to be able to link the cell type annotations to the cell suspensions or cell barcodes provided in the metadata.
(Ami to write email template)

## Filling in metadata about the files

For each file that is found, a row needs to be filled in the `contributor_matrices_metadata_[MM]-[YYYY]` for the appropriate release found in the [Contributor Matrices folder](https://drive.google.com/open?id=1FMjJwYamMyuCtNJoTiA30kM3vsL6Q8LD) in the Brokering folder.

| Field                       | Definition                                                                                                                   |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------|
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

If there are multiple values in one cell, they need to be delimited with comma

## Uploading the files to the google bucket

Files need to be uploaded to the [google bucket](https://console.cloud.google.com/storage/browser/hca-prod-ebi-matrices)

The way we did it last time was to create a folder for each project as `[project_uuid]-[project_shortname]`, then have all the files for that project inside that folder. Worth checking with UCSC browser team if they want this to remain the same.

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

