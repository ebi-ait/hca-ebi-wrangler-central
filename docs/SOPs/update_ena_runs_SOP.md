---
layout: default title: Archiving SOP parent: SOPs
---

## Table of contents

{: .no_toc .text-delta }

1. TOC {:toc}
## Overview
This is the SOP for fixing datasets in the issue: ebi-ait/hca-ebi-wrangler-central#250

## Requirements
1. Gain access to the EBI cluster
 ```
   ssh ebi-cli.ebi.ac.uk
```
2. Install gsutil/awscli in your environment in the EBI cluster
3. Get webin [credentials](https://console.aws.amazon.com/secretsmanager/home?region=us-east-1#!/secret?name=ingest%2Fwebin-creds). (Only an ingest developer has access to this atm)

## Steps

1. Get the list of sequencing runs to be suppressed. This can be downloaded as TSV/JSON from the ENA Browser. 
   
2. Make sure
   that the metadata in Ingest contains sequencing experiment accessions. The submitter script will raise an error if
   any of the assay processes has no accession. The assay processes in the submission should have the following
   property:

    ```json
    
    "insdc_experiment": {
      "insdc_experiment_accession": "ERX4319109"
    }
    ```

2. Clear the sequencing run accessions in file metadata 
    ```json
    "insdc_run_accessions": [
      "ERR6449905"
    ]
    ```

    Use script from the [ingest-archiver](https://github.com/ebi-ait/ingest-archiver.git) repo:
    ```bash
    ena/clear_run_accession_from_files.py
    ```

4. Download all files from Ingest / Terra upload area to any directory inside `/nfs/production/hca/` in the EBI cluster.
   The files may also be in the hca-util upload area but we should make sure they're valid. Using Ingest/Terra upload area means the files have already been validated before.
   Please prefer downloading the Terra upload area as downloading from Ingest upload area will incur cost to our AWS account.

5. Checksum all the files.
    ``` 
    $ cd to directory where you've downloaded the files 
    $ md5sum * > <insert-filename>.txt
    ```
6. Upload the files to Webin FTP upload area (could be in parallel with checksumming)
   ```
   lftp webin2.ebi.ac.uk -u <webin-user>
   # input webin-password
   ```   
   Please refer to [ENA documentation](https://ena-docs.readthedocs.io/en/latest/update/metadata/programmatic-read.html) for more details
7. Run the submitter script. The receipt.xml and report.json file should be available after running the script.
   ```json
   python submit_10x_fastq_files.py <submission-uuid> <md5-file> <token> [--ftp_dir <dir-name>]
   ```
8. Verify that the new runs were submitted. They should be visible in the Webin Portal but it may take 48 hours before they become available in the ENA browser

