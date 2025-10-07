# Update corrupted files in TDR

Here is a guide on how to update files published in Terra Data Repository that have been identified as corrupted. 

# Context
Use case issue: #1396
UCSC team performs checks on the integrity of the data in order to be mirrored to AWS Open Data. During such check, they might identify mismatches in the checksum of files in TDR. 

In such cases, uncorrupted data should be re-submitted by wranglers. One option would be to re-export data from ingest. However, upload api doesn't allow us to re-upload files that have previously been deleted.
A workaround is to override ingest and update file directly in the staging area. In order for TDR to allow overwritting the previous file, we should update the file version.

# process
1. identify the corrupted files in database (uuid)
2. identify and download correct file to re-download from archives
3. calculate sha256 checksum hash
4. get json metadata/ descriptor for files
5. amend json files according to [dcp2 SOP](https://github.com/HumanCellAtlas/dcp2/blob/main/docs/dcp2_system_design.rst#442update-a-data-file)
6. ensure staging area is cleaned
7. populate staging area:
	1. `/data` with correct files
	2. `/metadata/*file` with amended json
	3. `/descriptors/*file` with amended json
8. import form

### 1. identify the corrupted files in database
In order to identify the file in ingest database, you would need to query ingest with the following command or script for scale.

```bash
curl --request POST \
  --url 'https://api.ingest.archive.data.humancellatlas.org/files/query?operator=AND' \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '[
	{
		"field": "content.file_core.file_name",
		"operator": "IS",
		"value": "<file_name>"
	}
]'
```
or
```python
from hca_ingest.api.ingestapi import IngestApi
api = IngestApi(url="https://api.ingest.archive.data.humancellatlas.org/")
api.set_token(f"Bearer {<token>}")
query = [{'field': 'content.file_core.file_name', 
		  'operator': 'IS', 
		  'value': '<file_name>'}]
response = api.post('https://api.ingest.archive.data.humancellatlas.org/files/query?operator=AND', json=query)
```

#### Note:
First, verify that project is not Managed Access. If it's managed access, we should reach out to contributor to provide file again and make sure that file is not downloaded locally at any time. Descriptors and metadata should be fine to have locally.

From the output, identify the file `uuid`, and information that would help to identify file in the archive. For example, if it's `sequence_file` we could look for `insdc_run_accession`, `insdc_experiment_accession`, `read_index` and `lane_index`.

## 2. identify and download correct file to re-download from archives
Using information from step 1, we will try to identify the file in the archives. If we know that file was not accessed from archive but from contributor see note above.
If file is fastq derived from BAM file, take advantage of the complementary read_index to identify the library that was specified in tha bamtofastq argument.

## 3. calculate sha256 checksum hash
Here we want to verify that the substitution we are attemting makes sense. 
Use command `sha256` or equivalent to get the hash of the file, compare the sha256 with the "corrupted" file and the metadata hash value.

If the corruption occured after deposition in staging area, the sha256 value should match the value in the metadata. If values doesn't match but we are sure that this is the correct file to have in place, we can proceed. 

## 4. get json metadata/ descriptor for files
Check if staging area for project is still filled, with the following command:
```bash
gsutil ls gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<project-uuid>/metadata/<entity_type>
```
and identify the file with the file <uuid> in the file_name prefix.

Download locally the `/metadata` file and the `/descriptors` file. Both have the same file_name so make sure to download in different directories.
Ideally, use the same hierahical folder structure with this command.
```shell
gsutil -m cp -r gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<project-uuid>/metadata <path/to/download/metadata>
gsutil -m cp -r gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<project-uuid>/descriptors <path/to/download/descriptors>
```

If staging area is cleaned up and no such file exist there, ask the import team or indexing team to share these json files.

## 5. amend json files according to dcp2 SOP
[dcp2 SOP](https://github.com/HumanCellAtlas/dcp2/blob/main/docs/dcp2_system_design.rst#442update-a-data-file)

We want to edit the files so that TDR will understand that these are separate **versions**. We might also need to update all the **checksum** as well. 

Higher version means most recent update-date. It doesn't have to be an actual date of update. 

The changes for TDR to understand that this file should be updated are the following:
- `metadata` file:
	- `provenance.update_date` to any more recent date in the format ([ISO_8601](https://en.wikipedia.org/wiki/ISO_8601) is used, for example: `2025-08-07T16:15:39.822Z`)
	- update the **metadata** file file_name suffix with the same most recent date. 
		For example:
		`aaaaaaaa-5258-aaaa-84f3-aaaaaaaaaaaa_2025-08-22T13:43:40.996000Z.json` should be updated with `aaaaaaaa-5258-aaaa-84f3-aaaaaaaaaaaa_2025-09-23T14:45:40.996000Z.json`
		Note: trailing digits after decimal point compared to ISO_8601.
- `descriptor` file:
	- `file_version` to any more recent date in the format ([ISO_8601](https://en.wikipedia.org/wiki/ISO_8601) is used, for example: `2025-08-07T16:15:39.822Z`)
	- make sure that `size`, `sha1`, `sha256` and `crc32c` are updated as well (check script bellow)
	- update the **descriptor** file file_name suffix with the same most recent date.
		For example:
		`aaaaaaaa-5258-aaaa-84f3-aaaaaaaaaaaa_2025-08-22T13:43:40.996000Z.json` should be updated with `aaaaaaaa-5258-aaaa-84f3-aaaaaaaaaaaa_2025-09-23T14:45:40.996000Z.json`
		Note: trailing digits after decimal point compared to ISO_8601.

<details><summary>script to edit descriptor contents</summary>

If the documents is structured in a hierahical way as it is in staging area you could use the following script:
(Update `today` variable with the desired update-date, or update the entity_type if file is not sequence file)

```python
import os
import json
import hashlib
import google_crc32c

proj_uuids = [proj for proj in os.listdir() if os.path.isdir(proj)]
# get filenames
filenames = []
for proj in proj_uuids:
	filenames.extend([proj + '/data/' + f for f in os.listdir(proj + '/data/')])

# get hashes
hashes = {}
for filename in filenames:
	hashes[filename] = {}
	with open(filename, "rb") as file:
		while (byte:= file.read()):
			hashes[filename]['sha1'] = hashlib.sha1(byte).hexdigest()
			hashes[filename]['sha256'] = hashlib.sha256(byte).hexdigest()
			hashes[filename]['crc32c'] = f'{google_crc32c.value(byte):02x}'.zfill(8)
			hashes[filename]['size'] = os.path.getsize(filename)

# get descriptors filenames
descriptors = []
for proj in proj_uuids:
	descriptors.extend([proj + '/descriptors/sequence_file/' + f for f in os.listdir(proj + '/descriptors/sequence_file/')])

today = '2025-07-16T13:33'
for descriptor in descriptors:
	proj = descriptor.split('/')[0]
	with open(descriptor, 'r') as file:
		d = json.load(file)
		d['file_version'] = today + d['file_version'][16:]
		seq_file = proj + '/data/' + d['file_name'].split("/")[1]
		d.update(hashes[seq_file])
	os.remove(descriptor)
	descriptor = descriptor[0:100] + today + descriptor[116:]
	with open(descriptor, 'w') as file:
		json.dump(d, file)
```
</details>

## 6. ensure staging area is cleaned

Make sure that staging area has been cleared from other files that might cause validation to fail. If you are SURE that the contents of staging area for this project can be repopulated use the following command
```shell
gsutil -m rm -r gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<project-uuid>
```

## 7. populate staging area
Next step is to upload files into the staging area.

### 1. `/data`
Upload correct files into the staging area with the command:
```shell
gsutil cp <path/to/file> gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<project-uuid>/data
```
### 2. `/metadata/*file`
Upload amended metadata json files. Careful not to upload the descriptor file that share the same name.
```shell
gsutil cp <path/to/metadata_file> gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<project-uuid>/metadata/<entity_name>/
```
### 3. `/descriptors/*file`
The same with amended descriptor json. Again be careful not to upload metadata file that share the same name.
```shell
gsutil cp <path/to/descriptor_file> gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<project-uuid>/descriptors/<entity_name>/
```

## 8. import form
As a final step, don't forget to let the import team to import the dataset for the next release using the import form.
