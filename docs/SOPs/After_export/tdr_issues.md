---
layout: default
title: Resolve TDR issues
parent: After export
grand_parent: SOPs
nav_order: 3
last_modified_date: 28/10/2025
---

# Resolve TDR issues

After exporting the submission into Terra Data Repository staging area, we might come into validation errors. We (wranglers) are responsible to help resolving them.

A very detailed description of the Terra Data Repository system can be found [here](https://github.com/HumanCellAtlas/dcp2/blob/main/docs/dcp2_system_design.rst).

In this document, we are going to attempt a slimmer version of that document, focusing mainly on how to fix validation errors. Keep in mind that understanding how the dcp2 system is designed would help fixing most of the errors that occur.

We are going to attempt a shortcut here, but before we jump into the steps let's dive into the staging area project folder structure.

## staging area project structure

While in ingest, we have metadata entities and data files only, in staging we end up with the following directories per project
- `data` actual data files
- `metadata` each entity instance has their own metadata file (processes are separate entities)
- `descriptors` file metadata need to have a descriptor to map between the metadata and the actual data file
- `links` starting from higher level biomaterial (usually donor_organism) we follow the steps until we reach each data file. Each data file has a separate links file to describe the experimental graph.

Note that the generated metadata spreadsheet is considered a Supplementary file, and therefore we have metadata/ descriptors/ links for that.

We are allowed to have multiple versions of the same file. Each version is described by the date of file generation/update that is printed into the filename. <br>If we need to update a file, it would only work if we have a newer version of the file in staging area.

## validator

TDR validator:
1. validates the fields that exist in the staging area in terms of JSON integrity, schema validity and completeness
1. compares with previously deposited data/metadata in their infastructure
1. imports files from staging to prod TDR only if a newer version is in staging

Therefore, if staging area has a sequence_file metadata file that is not assigned to any file or descriptor, validator will fail 1. This is the most common place that errors occure.

## FSE: frequently seen errors
In most cases, safest solution would be to clear up staging area and re-export.
```bash
gsutil -m rm gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<proj-uuid>/*
```
However, sometimes re-exporting the whole project is not possible (i.e. we no longer have the data files in ingest, or we don't want to add redundant transfer of data that is not updated). Therefore we will have to see more hacky solutions.

Some common errors are shown [here](https://docs.google.com/presentation/d/1S3YRzpOo2ZUdgYGkWJBNpcqpnTKqpbBJQ8uByqRVcyU/edit?slide=id.g2ec95778594_0_74#slide=id.g2ec95778594_0_74).

### 1. metadata only export includes file metadata
One of the most common errors that we come up with is when we want to export metadata only. In ingest, the difference between `export all` and `export metadata only` is that in `metadata only` the data files are not exported.

Those files will be described in the metadata/ descriptors/ links, but then TDR validator expects to see the data files there as well, which is not the case.


#### error message
We might find errors like:

> ERROR:hca.staging_area_validator:File error: 
```json
{'name': {'prod/b176d756-62d8-4933-aaaa-8b026380262f/metadata/sequence_file/0c6dfd26-1785-4198-aaaa-23ece6b5c70d_2021-05-10T16:46:45.655000Z.json'}, 'entity_id': '0c6dfd26-1785-4198-aaaa-23ece6b5c70d', 'entity_type': 'sequence_file', 'metadata_versions': {'2021-05-10T16:46:45.655000Z'}, 'descriptor_versions': {'2021-05-10T16:46:45.655000Z'}, 'project': {'b176d756-62d8-4933-aaaa-8b026380262f'}, 'category': {'output'}, 'found_metadata': True, 'data_file_name': 'file.fastq.gz', 'found_data_file': False, 'crc32c': '14a366ae'}
```

#### solution
The hacky solution to that problem is to remove all unnessesary json files from staging area manually. 

For example, if we've done a metadata update and we want to keep only the generated spreadsheet file and that's the only supplementary file of the project, then we are removing all other files:
```bash
# thanks Enrique Sapena Ventura for the quick snippets
gsutil ls gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<proj_uuid>/metadata/ | grep file | grep -v supplementary_file | xargs -I{} sh -c "gsutil -m rm -r {}" 
gsutil ls gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<proj_uuid>/descriptors/ | grep file | grep -v supplementary_file | xargs -I{} sh -c "gsutil -m rm -r {}" 
```
And then check the link file that describes the metadata spreadsheet:
```bash
gsutil ls gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<proj_uuid>/metadata/supplementary_file
```
Get the `<file_name>` of the most recent metadata spreadsheet file and paste it in the `<file_name>` in the following command
```bash
gsutil ls gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<proj_uuid>/links/ | grep -v "<file_name>" | xargs -I{} sh -c "gsutil -m rm -r {}" 
```

This will remove all metadata/ descriptors/ links from the project's staging area (except the generated spreadsheet file) and validator should be fine now.

### 2. partial export
We've come up to a submission not being correctly exported, and thus a JSON file is corrupted (slack discussion [here](https://embl-ebi-ait.slack.com/archives/C9XD6L0AD/p1759263970325189?thread_ts=1758904556.385449&cid=C9XD6L0AD)). 

#### Error message
> hca_orchestration.solids.load_hca.data_files.load_data_metadata_files.NullFileIdException: File metadata with null file ID detected, will not ingest. Check crc32c and target_path [table=supplementary_file]

#### Solution
1. Identify the invalid file that is duplicated, and check which might be corrupted (compare checksums with ingest values):
```bash
gsutil ls gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<proj_uuid>/metadata/<any_entity>
```
1. Keep the `<file_name>`, and remove the invalid and additional data file and metadata/ descriptor/ links related to this.
```bash
gsutil rm gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<proj_uuid>/metadata/<any_entity>/<file_name>
gsutil rm gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<proj_uuid>/descriptors/<any_entity>/<file_name>
gsutil rm gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<proj_uuid>/links/<file_name>_-project_uuid-.json
```