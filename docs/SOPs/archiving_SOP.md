---
layout: default
title: Archiving SOP
parent: SOPs
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# Archiving instructions
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


## Submit for Archiving

1. Once the data files are uploaded the submission should be listed as **Valid.**
2. On the Submit Tab, click the Submit Button.
3. The submission will be marked as **Processing** as it maps the experimental graph.
4. One finished the submission with be marked as: **Archiving**
    1. **Please now poke your #hca-operations buddies to continue the process below by Archiving the Metadata to DSP.**


## Step 1 of 3 - Archiving Metadata to DSP

### Before using the service 

Please note when using the documentation below:


*   There is a difference between **api**.ingest… and **archiver**.ingest…
    * API -> **ingest_submission_uuid**
    * Archiver -> **dsp_submission_uuid**
*   Obtain and replace `{archiver_api_key}` with the key obtained by running the following cmd (replace `dev` with `staging` or `prod` depending on the environment):
    *   `aws --region us-east-1 secretsmanager get-secret-value --secret-id ingest/dev/secrets --query SecretString --output text | jq -jr .archiver_api_key`
    *   If you can't retrieve the archiver service api key using this command, it is likely because you do not have the required permissions. Ask a dev or wrangler to obtain the key


### Archiver endpoints
There are currently 3 environments that you can use for the archiver:

1. `https://archiver.ingest.dev.archive.data.humancellatlas.org`: Corresponding to **DSP test environment**
1. `https://archiver.ingest.staging.archive.data.humancellatlas.org`: Corresponding to **DSP test environment**
1. `https://archiver.ingest.archive.data.humancellatlas.org`: Corresponding to **DSP production environment**

Please make sure you are using the proper endpoint when archiving (Instruction and examples written for the staging environment)


### Using the service

Once a submission is ready in ingest (`Archiving` status after hitting submit), you need to follow the next steps:

1. Open a terminal

1. Create a DSP submission given an ingest submission UUID with a POST request
   ```
   curl -X POST https://archiver.ingest.staging.archive.data.humancellatlas.org/archiveSubmissions -H 'Content-Type: application/json' -H 'Api-Key: {archiver_api_key}' -d '{"submission_uuid": "{ingest_submission_uuid}", "alias_prefix": "HCA"}'
   ```
   Please note this is an async request and even if it's successfully triggered (You will get a response saying that), it may take a while to create the submission.
   
1. Retrieve the DSP submission UUID via the ingest submission UUID
   ```
   curl -X GET  -H 'Api-Key: {archiver_api_key}' https://archiver.ingest.staging.archive.data.humancellatlas.org/latestArchiveSubmission/<ingest_submission_uuid>
   ```
   This request should give you the UUID in the json response

#### Useful requests to check DSP submission

*  **Check validation errors**
   ```
   curl -X GET https://archiver.ingest.staging.archive.data.humancellatlas.org/archiveSubmissions/<dsp_submission_uuid>/validationErrors -H 'Api-Key: {archiver_api_key}' 
   ```

*  **Check any submission blockers**
   ```
   curl -X GET https://archiver.ingest.staging.archive.data.humancellatlas.org/archiveSubmissions/<dsp_submission_uuid>/blockers -H 'Api-Key: {archiver_api_key}' 
   ```

```
# 1. create dsp submission given an ingest submission uuid (async)
curl -X POST https://archiver.ingest.staging.archive.data.humancellatlas.org/archiveSubmissions -H 'Content-Type: application/json' -H 'Api-Key: {archiver_api_key}' \

 -d '{"submission_uuid": "1a5742a3-ded7-47ba-9e47-51297de33fdd", "alias_prefix": "HCA"}'

# 2. find the dsp submission by ingest submission uuid
curl -X GET  -H 'Api-Key: {archiver_api_key}' https://archiver.ingest.archive.data.humancellatlas.org/latestArchiveSubmission/<ingest_submission_uuid>

# dsp submission uuid should be in the JSON response

# 3. find the archive entities by dsp uuid
curl -X GET https://archiver.ingest.archive.data.humancellatlas.org/archiveSubmissions/<dsp_submission_uuid>/entities -H 'Api-Key: {archiver_api_key}' 

# 4. check validation errors
curl -X GET https://archiver.ingest.archive.data.humancellatlas.org/archiveSubmissions/<dsp_submission_uuid>/validationErrors -H 'Api-Key: {archiver_api_key}' 

# 5. download the file upload plan (could do in EBI cluster)
curl -X GET https://archiver.ingest.archive.data.humancellatlas.org/archiveSubmissions/<dsp_submission_uuid>/fileUploadPlan  -H 'Api-Key: {archiver_api_key}' > FILE_UPLOAD_INFO_<dsp_submission_uuid>.json

```


### Notes
- There is another way to run the archiver, through the CLI. This should be used as a last resort as it's getting deprecated. Please contact a dev to use the CLI instead of the web service.
- Please contact a dev if there is any problem with the metadata. We currently have no way to update it through the UI so it needs to be updated manually in DSP.


## Step 2 of 3 - Archiving Files to DSP

Once the metadata is in DSP, the next step is to upload the files.

### File Upload Info

#### What it is
The file upload info is a JSON file that provides the file archiver component of ingest with the information needed to convert/upload the files from the submission to DSP.

Its structure is:


```
{
    "jobs": [
        {
            "dsp_api_url": "<dsp_api_url>",
            "ingest_api_url": "https://api.ingest[.staging].archive.data.humancellatlas.org",
            "submission_url": "<submission_url_with_id>",
            "dcp_bundle_uuid": "<dcp_bundle_uuid>",
            "files": [
                {
                   "name": "<name_of_output_bamfile>"
                }
            ],
            "manifest_id": "<bundle_manifest_id>",
            "conversion": {
                "output_name": "<name_of_output_bamfile>",
                "schema": "[10xV2, 10xV3]"
                "inputs": [
                    {
                        "name": "<r1_fastq_filename>",
                        "read_index": "read1",
                        "cloud_url": "<complete_s3_read1_url>"
                    },
                    {
                        "name": "<r2_fastq_filename>",
                        "read_index": "read2",
                        "cloud_url": "<complete_s3_read2_url>"
                    },
                    {
                        "name": "<i1_fastq_filename>",
                        "read_index": "index1",
                        "cloud_url": "<complete_s3_index1_url>"
                    }
                ]
            }
        }
    ]
}
```


<**dsp_api_url**>


- https://submission.ebi.ac.uk/api/ -> production

- https://submission-test.ebi.ac.uk/api/ -> staging

<**submission_url_with_id**>

`dsp_api_url>/submissions/&lt;submission_id>`

<**dcp_bundle_uuid**>

This field will only be added when trying to archive a DCP1 dataset.

<**name_of_output_bamfile**>

Free string but usually bundle manifest ID + “.bam”

<**schema**>

	Either 10xV2 or 10xV3

<**rx_fastq_filename**>

Filename of the fastq file

<**complete_s3_xxxx_url**>

URL where the archiver can find the file. Has to be an s3 (e.g. s3://mock-upload-area-preffix/abcd-abcd-abcd-abcd/filename.fastq.gz) and you should be able to download files with the credentials that you provide later.


The “conversion” field can be deleted if no bam conversion is needed. It won't be generated unless conversion is needed.


### Using the file archiver service

Make sure that all commands using the File Archiver image is pointing to the latest version of it.
Check latest image version (prod released version will have the tag format `dYYYY-DD-MM.<increment_digit>`) in [quay.io](https://quay.io/repository/ebi-ait/ingest-file-archiver?tab=tags)

#### Using EBI Cluster

As a standard, we run bam conversion in the EBI cluster, as it may need a big chunk of memory and fail when ran in the EC2. Steps to use:

1. Login to VPN if offsite, using pulse secure or other (EBI macbooks have Pulse Secure pre-installed for this)

1. Login to cluster
   ```
   ssh noah-login
   ```

1. Move to the folder you want to run the jobs from and create the folder if necessary
   ```
   cd /nfs/production/hca/<shortname_of_project>/
   ```
   Please note that the archiver service **does not** create the folder for you. The first time you head there you'll need to first create it
   ```
   mkdir /nfs/production/hca/<shortname_of_project>/
   ```
   All fastq files will be downloaded here, and the bams will be generated under this folder as well

1. Make a request to the Archiver service endpoint to retrieve File Upload Info JSON file
   ```
   curl -X GET https://archiver.ingest.staging.archive.data.humancellatlas.org/archiveSubmissions/<dsp_submission_uuid>/fileUploadPlan  -H 'Api-Key: {archiver_api_key}' > /nfs/production/hca/<folder_name>/<file_name>.json
   ```

Once the file_upload_info.json is in the folder, you have 2 options:
1. **Run the job sequentually**: Running the singularity job with 64GB memory (Default is 1GB)
    ```
    bsub -J <job_name> -M 64000 'singularity run -B /nfs/production/hca/<folder_name>:/data docker://quay.io/ebi-ait/ingest-file-archiver:d2020-30-09.1 -d=/data -f=/data/<file_name>.json -l=https://explore.api.aai.ebi.ac.uk/auth -u=<aap-username> -p=<aap-password> -a=<aws-key> -s="<aws-secret>"'
    ```
1. **Run the job in parallel**: Please refer to the [next subsection](#run-parallel-jobs) to run the file archiver in parallel.

##### Run parallel jobs

With only one file_upload_info.json, all jobs are run sequentially. In order to run parallel jobs, you need to use a script to divide the jobs and send each one of the jobs as a different job in the cluster. Assuming you are already logged in the cluster, and in the working directory, the steps are:

1. Verify that you can use python version 3.7 or above
   ```
   python --version
   Python 3.7.8
   ```
   **Note**:If python version is not 3.7, you could use pyenv (you must install it first) to install specific python version
   ```
   pyenv install 3.7.8
   pyenv global 3.7.8
   python --version
   Python 3.7.8
   ```

1. Clone the [repo](https://github.com/ebi-ait/hca-ebi-dev-team) where the batch script is located and setup a virtual env to run the script

   ```
   git clone https://github.com/ebi-ait/hca-ebi-dev-team.git
   cd hca-ebi-dev-team/scripts/batch_file_archiver/
   pip install virtualenv
   virtualenv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```


1. Download the file upload plan if you haven't already

1. Run the python script to batch file archiver jobs. You could do a dry run first and see the bsub job commands to run. Remove the --dry_run flag if you think the bsub commands are correct.

   ```
   python batch_file_archiver.py '<aap-user>' '<aap-password>' '<aws-key>' '<aws-key-secret>'  '/nfs/production/hca/<work-dir>' './FILE_UPLOAD_INFO_953b4f03-f5d3-4a03-ad48-6aa125bacf1f.json' <--dry_run>
   ```

Note: Please make sure the `batch_file_archiver.py` is pointing to the latest version of the File Archiver. (See details [Using the file archiver service](### Using the file archiver service) on how to check latest version)
If not please update the file in github to point to the new version.

#### Using Wrangler EC2

If no BAM conversion is required you can use the wrangler EC2 as follows:



1. Send info file to EC2 home directory

   ```
   scp FILE_UPLOAD_INFO.json <user>@tool.archive.data.humancellatlas.org:./
   ```
   
1. Connect to the wrangler EC2
   ```
   ssh <user>@tool.archive.data.humancellatlas.org
   ```

1. Create a background task screen

   ```
   screen -S <optional_session_name>
   ```
    1. [More info about the screen command](https://linuxize.com/post/how-to-use-linux-screen/#detach-from-linux-screen-session).

1. Run the file archiver

    ```
    docker run \
    -v $PWD:/data \
    --env BASE_DIR=/data \
    --env UPLOAD_PLAN_PATH=/data/FILE_UPLOAD_INFO.json \
    --env AAP_USERNAME=<aap_user> \
    --env AAP_PASSWORD=<aap_password> \
    --env AAP_URL=https://explore.api.aai.ebi.ac.uk/auth \
    --env AWS_ACCESS_KEY_ID=<aws_key> \
    --env AWS_SECRET_ACCESS_KEY=<aws_secret> \
    quay.io/ebi-ait/ingest-file-archiver:d2020-30-09.1
    ```


1. Disconnect from your screen, leaving your session running
    ```
    CTRL+A, CTRL+D
    ```
    1. You can now close your terminal, leaving the upload running
    
    
1. Reconnect to your screen
    ```
    screen -r <optional_session_name>
    ```

#### Checking files have been uploaded

To check if the files have been uploaded:

* **EC2**: Just reconnect to your session and check stdout
* **EBI Cluster**: Check how many jobs you have currently running:
  ```
  bjobs -W
  ```
  This will give you the list of jobs that are currently pending or running. If you have any questions, please contact the devs for a more detailed log.
  
If the file-archiver/all jobs in the cluster have finished, an indirect way to check if everything went correctly is to check for validation errors:
```
curl -X GET https://archiver.ingest.archive.data.humancellatlas.org/archiveSubmissions/<dsp_submission_uuid>/validationErrors -H 'Api-Key: {archiver_api_key}' 
```
Once all the files are uploaded, you should get no validation errors. If there are, please contact a dev to check what happened.


### Example Showing File and Folder Locations

In the above commands, it is recommended that you use `/nfs/production/hca/` as your root folder. Create directories inside of here to manage your uploads to DSP, a directory per HCA project is sufficient and they can be called whatever you want, (often HCA project UUIDs). Using one folder per project means less re-downloading of files since they are cached in the data directory by manifest ID and re-used.

Matching these locations in your commands is really important. In the following example



*   <folder_root> = /nfs/production/hca/
*   <folder_name> = laurenti
*   <file_name> = upload_info.json
*   <dsp_submission_uuid> = 1234
*   <job_name> = laurenti_upload
*   Using the live ingest environment
*   Please note that /data is fixed, in theory you could change it, but please don’t.
*   In theory you could also change the docker image you pull to use specific versions of file archiver but again, please don’t: `docker://quay.io/ebi-ait/ingest-file-archiver:d2020-30-09.1`

Download the the file upload info:


```
curl -X GET https://archiver.ingest.archive.data.humancellatlas.org/archiveSubmissions/1234/fileUploadPlan  -H 'Api-Key: {archiver_api_key}' > /nfs/production/hca/laurenti/upload_info.json
```


Trigger the File Transfer to DSP:


```
bsub -J laurenti_upload -M 64000 'singularity run -B /nfs/production/hca/laurenti:/data docker://quay.io/ebi-ait/ingest-file-archiver:d2020-30-09.1 -d=/data -f=/data/upload_info.json -l=https://api.aai.ebi.ac.uk/auth -u=hca-ingest -p=<aap-password> -a=<aws-key> -s=<aws-secret>'
```


If running parallel jobs, choose different <file_name> / <job_names> because you will have multiple file-upload-infos and multiple jobs, in this case I’ve used the name of the output bam file as the job_name and file_name.

# Step 3 of 3 - Complete DSP Submission

Once the files are uploaded and validated, to finish the submission, just run the following request to complete the submission:
```
curl -X POST https://archiver.ingest.staging.archive.data.humancellatlas.org/archiveSubmissions/<dsp_submission_uuid>/complete -H 'Api-Key: {archiver_api_key}' 
```

## Triggering re-archival of submissions


To trigger the re-archival of submissions, please refer to the proper section in the [Ingestion to archives](https://docs.google.com/document/d/1S4fyCSqB3nLrCUssNMwSp6ff8tmeipMi_slnXW2Lrq4/edit?pli=1#heading=h.wzojhbhfywqr) document

