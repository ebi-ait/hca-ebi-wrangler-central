---
layout: default
title: Data and metadata review and export SOP
parent: Managed access
grand_parent: SOPs
nav_order: 5
last_modified_date: 04/06/2024
---

<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# Managed access project - Data and metadata review and export SOP
Once the the wrangler has verified that the data and metadata files were transferred correctly to the hca-util are they can  proceed with submission creation and validation

## Submission review and validation
Data and metadata in a managed access submission are considered sensitive information and must be kept encrypted. Unlike in the case of open access projects, review for a managed access project must be done without ever downloading the metadata spreadsheet - or the data - to a non-encrypted location, like a laptop.
1. Once the metadata spreadsheet is uploaded to the hca-util area a lambda function will automatically trigger the upload of the spreadsheet to the project in ingest.
2. If the upload fails because ingest cannot process the spreadsheet, get in touch with the contributor to review their submission in a call. The contributor should share their screen and walk through the spreadsheet.
3. Review the submission for metadata errors and communicate with the contributor to fix them. Ask the contributor to upload the improved spreadsheet to the hca-util area and repeat from step 1. 
4. Sync data files directly from hca-util to ingest staging bucket \
`$ hca-util sync s3://org-hca-data-archive-upload-prod/<submission-uuid>`
5. Add ontology terms were necessary, for example for methods, species and developmental stage.
6. Validate experimental design with the graph validation step. If there are any errors communicate with the contributor so that they can amend the metadata spreadsheet and upload the improved version to the hca-util area

## Confirm Project data release

Once the Validation for the Project submission is complete:
1. Notify the data contributor that the data submission is complete
2. Confirm that they’re happy to proceed to publishing the Project under Managed access
3. If the contributor wishes to hold the Project private for a period of time, confirm the desired release date and put a reminder in the calendar for that date
4. If the Project is to be published with the first available release, give an estimate of when they can expect to see the project live on the HCA Data Portal.

## Export

Within the timeframe agreed for the data release: 
1. Export the project by clicking Export on Project in [HCA Data Repository Ingest service backoffice](https://contribute.data.humancellatlas.org/) and select ‘Export files and metadata’
2. Once the export is complete, fill out the usual [Data release import form](https://docs.google.com/forms/d/e/1FAIpQLSeokUTa-aVXGDdSNODEYetxezasFKp2oVLz65775lgk5t0D2w/viewform?gxids=7628).

## Verify

Once the project is live on the HCA Data Portal: 
1. Verify that the project is displayed correctly
2. Send a link to the data contributor so that they may reference it in their publications.
