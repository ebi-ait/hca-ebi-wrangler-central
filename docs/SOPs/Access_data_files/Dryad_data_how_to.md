---
layout: default
title: Download Data from Dryad SOP
parent: Access data files
grand_parent: SOPs
nav_order: 4
---

# Downloading data from Dryad

[Dryad](https://datadryad.org/) is a generalist archive for scientific data that allows users to upload data, organised in projects, and make it available for download. It is similar to Zenodo, however there are important limitations in the dowload:
1. The maximum size for dowload from the ui is 11GB
2. The files must be selected one by one for dowload
3. There is no file manifes accessible from the ui

If your dataset is smaller than 11GB you can dowload the whole dataset in one click

If your dataset is bigger than 11GB you can use [get_dryad_dataset](https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/iz-data-from-dryad/src/get_dryad_dataset.py) script to dowload the whole dataset taking advantage of dryad's api

#### Requirements:
The script only requires the dataset's doi which can be found in the url or the ui page \
Example: the doi for this [dataset](https://datadryad.org/dataset/doi:10.5061/dryad.j1fd7) is `doi:10.5061/dryad.j1fd7`

The doi must include **doi:**

#### Explanation:
1. The script will use the dataset's doi to get the id for the current version of the dataset.
1. Based on the current version id the script will get the file manifest
1. For each file the script will get the dowload link and dowload the file
1. After dowloading each file the script will compare the file's checksum with the checksum from the api

