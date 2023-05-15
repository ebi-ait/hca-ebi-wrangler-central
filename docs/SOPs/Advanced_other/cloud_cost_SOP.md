---
layout: default
title: Cloud cost report
parent: Advanced & other SOPs
grand_parent: SOPs
last_modified_date: 19/01/2020
---

# Purpose of this document

This document describes how to generate/update up-to-date cloud cost reports for DCP2 and how to interpret the pre-rendered plots. 

These reports only take in account the cost of a dataset going through the wrangling process, only apply to EBI's ingest service and **do not** take in account the monthly cost of the infrastructure.

# Generating cloud cost reports

## Requirements

1. Access to the [cloud costs spreadsheet](https://docs.google.com/spreadsheets/d/1oZ-6KHyyccktTCVij5udfOqJAo-kXPyiS1qrXtAJTUA/edit#gid=1651740430). If you don't have access, please ask for access to the rest of the wranglers

1. Access to the Ingest EC2 instance or Wrangler AWS credentials in local machine. These are mandatory to update the google sheet, as it requires manual input to get the size of the datasets. If you don't have access, please ask a developer in the team to give you either the credentials or access to the EC2.

## Definitions
**Path**: In the context of data flow into/out of the ingest database, path is referred as what databases will the data be brokered to. 

Currently we only allow 2 paths: Exporting and Archiving

## How to fill the spreadsheet
The first 2 tabs of the spreadsheet (`General estimations` and `Over time`) **remain static**. The summary table (last tab) is updated automatically once new information is added to the `DCP2 Costs` tab.


### Updating the DCP2 Costs tab
Updating the DCP2 costs tab is a semi-automatic process. To run this process, you just need to press the "Update Datasets" button on the UI and click on "Run", as shown in the image below:

![cloud costs](https://github.com/ebi-ait/hca-ebi-wrangler-central/raw/master/assets/images/cloud_cost_screenshots/GUI.png)

As long as the dataset tracking sheet is updated with the latest information, it will only ask to run an aws command (Provided to you) to get the size of the dataset.

Only datasets that comply with these conditions will be added:
- Project shortname does not already exist in the cost sheet
- Project has an hca_status of `finished`

Once the script has finished (Might take a couple of seconds), if new datasets have been added, please fill in the last 2 columns by dragging down from the upper rows.

Currently there is no way to automatically add information **after** a dataset is added to the sheet. If the dataset needs to be updated (e.g. it was exported post-adding to the sheet), please fill the data manually.


# What information can I extract from the spreadsheet

## “General estimations” tab
This data was generated with examples of datasets that have been ingested into the HCA already. Data here is pretty generic and, while it may have some potential at calculating average costs, should be taken with a grain of salt.

There are 3 tables, each showing (In descending order):
1. Total cost of projects based on size by path followed. Average was calculated by doing the average mean of 17 datasets.
1. Total cost of 10x projects based on number of cells by path followed. This was calculated by using real example datasets. It also features the cost per cell.
1. Total cost of SS2 projects based on number of cells by path followed, similar to table above

From these tables, the following plots were generated (From left to right):

1. Cost of exporting/archiving a dataset based on size (in GB)
1. Average cost per path and project by technology

To better understand the data, a diagram of the overall flow of data has been included in the bottom, as well as assumptions about storage and movement of data. These assumptions apply to all the tabs.

## “Over time” tab
This tab exists to show the number of aggregated projects and cell count estimates, integrating DCP1 and DCP2 MVP. 

There are 2 tables, each showing (In descending order):
1. Summary table of projects up to the data added for the DCP2 MVP (45 projects)
1. Summary table of the aggregated number of cells up to DCP2 MVP

From these tables, the following plots were generated (Descending order):
1. Timeline on the number of projects
1. Timeline on the number of cells


Currently there is no automatic integration, so the data here remains static.

## “DCP2 costs” tab
This data summarises the cloud costs of the datasets pushed for DCP2. This tab does contain automatically integrated data, and can be updated manually if needed.

This sheet only contains a table, with the following columns:
1. `project_short_name`: Shortname of the project
1. `submission_date`: Submission date of the dataset, as indicated in the `submissionEnvelope` entity in ingest for that project.
1. `total_size`: Total size of the dataset in GB
1. `path`: Path followed by the dataset. A = Archive, E = Export
1. `size_exported`: Size of the dataset that was exported, in GB
1. `size_archived`: Size of the dataset that was archived, in GB
1. `total_cost`: cost calculated based on size and path that the dataset followed (as well as storage)

And the rest are calculations based on that data. From this table, the following plots were generated (Left to right):
1. Average of cell number by project over time
1. Number of projects over time
1. Number of cells over time


## “Summary table (DCP2)” tab
This data is generated as a summary of the previous tab. It contains a table with the following information:
- Total cost of all the projects in DCP2 in dollars
- Average cost per project in DCP2
- Average size per project in DCP2
- Average number of cells per project in DCP2

This tab gets updated automatically when data is added to the `DCP2 costs`.
