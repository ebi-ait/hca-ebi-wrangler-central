---
layout: default
title: Update ENA runs SOP
parent: SOPs
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
2. Install `gsutil` in your environment in the EBI cluster and log in using your EMBL-EBI google account.
   You could follow instructions from https://cloud.google.com/storage/docs/gsutil_install to install `gs_util`. 
   See more details [here](https://ebi-ait.github.io/hca-ebi-dev-team/admin_setup/Setting-up-access-to-Terra-staging-area.html#using-your-google-account) about setting up your access to Terra staging area.
3. Get DSP's Webin [credentials](https://console.aws.amazon.com/secretsmanager/home?region=us-east-1#!/secret?name=ingest%2Fwebin-creds). (Only an ingest developer has access to this atm)
4. Clone the [ingest-archiver](https://github.com/ebi-ait/ingest-archiver) repository. The scripts that will be used is in `ena` directory of that repo.
   ```
   git clone https://github.com/ebi-ait/ingest-archiver.git
   pip install -r requirements.txt
   ```
5. Get your JWT Token from Ingest UI.
   1. Log in in Ingest UI https://contribute.data.humancellatlas.org/login using the account which has the WRANGLER role.
   1. In Chrome, right click and select _Inspect_ to open the developer console. Select the Network tab.
   1. Refresh the page, `https://contribute.data.humancellatlas.org/home`
   1. Check the _Authorization_ in headers of the request to `https://api.ingest.archive.data.humancellatlas.org/auth/account`
   1. Copy the token after _Bearer_ prefix: 
      ```
      Authorization: Bearer <copy the very long string of random characters>
      ```
   1. That token has 1 hr validity. The token will be needed in the submitter script later.
## Steps

1. Get the list of sequencing runs to be suppressed. This can be downloaded as TSV/JSON from the ENA Browser. 
   
2. Make sure
   that the metadata in Ingest contains sequencing experiment accessions. The submitter script will raise an error if
   any of the assay processes has no accession. The assay processes in the submission should have the following
   property:

    ```
    "insdc_experiment": {
      "insdc_experiment_accession": "ERX4319109"
    }
    ```

2. Clear the sequencing run accessions in file metadata. The following should not be in the file metadata json:
    ```
    "insdc_run_accessions": [
      "ERR6449905"
    ]
    ```
   
   Update clear_run_accession_from_files.py to have a jwt token from the Ingest UI then run the following: 
    ```
    python clear_run_accession_from_files.py <submission-uuid>
    ```

4. Download all files from Ingest / Terra upload area to any directory inside `/nfs/production/hca/` in the EBI cluster.
   [gsutil](https://cloud.google.com/storage/docs/downloading-objects) can be used for downloading the files
   The files may also be in the hca-util upload area but we should make sure they're valid. Using Ingest/Terra upload area means the files have already been validated before.
   Please prefer downloading the Terra upload area as downloading from Ingest upload area will incur cost to our AWS account.

5. Checksum all the files.
    ``` 
    gsutil hash -hm gs://broad-dsp-monster-hca-prod-ebi-storage/prod/<project_uuid>/data/* | grep -A1 "hex" | awk -F"/" '{printf $4 $1}' | awk -F"--" '{for (i=1;i<NF;i++)print $i}' | awk -F":" '{print $1 $3}' > <md-filename>.txt
    ```
6. Upload the files to Webin FTP upload area (could be in parallel with checksumming)
   ```
   $ cd <directory where you downloaded the files>
   $ lftp webin2.ebi.ac.uk -u <webin-user>
   $ > # input webin-password
   $ mkdir parent-dir
   $ cd parent-dir
   $ mput *
   ```   
   Please refer to [ENA documentation](https://ena-docs.readthedocs.io/en/latest/update/metadata/programmatic-read.html) for more details
7. Run the submit_10x_fastq_files.py script. The `receipt.xml` and `report.json` file should be available after running the script.
   The `receipt.xml` will contain the ENA REST API response. The `report.json` will contain some report on which files were updated with the run accessions from ENA response.
   ```bash
   python submit_10x_fastq_files.py <submission-uuid> <md5-filename> <jwt-token-from-ingest-ui> [--ftp_dir <parent-dir>]
   ```
8. Verify that the new runs were submitted. They should be visible in the Webin Portal but it may take 48 hours before they become available in the ENA browser

9. File a ticket via [ENA helpdesk](https://www.ebi.ac.uk/ena/browser/support) to suppress the old sequencing runs.
   Guide on answering the form questions:
   ```
   Submitter: Broker
   Query is related to: Suppression
   I work on: Humans
   Organisms classification: Not applicable
   The work is: Other/not sure (Raw sequencing reads)
   ```
