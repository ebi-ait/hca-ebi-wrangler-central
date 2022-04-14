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


## Steps

![Archiving steps](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/ebi-ait/hca-ebi-wrangler-central/ops-485_update-archiving-sop/assets/plantuml_diagrams/archiving_sop.diag)


### Step 1: Submit for Archiving

1. Once the data files are uploaded and the submission has been validated, the submission should be listed as **Graph Valid.**
2. On the _Submit_ tab, click the Submit Button.
3. The submission will be marked as **Processing** as it maps the experimental graph
4. Once finished, the submission will be marked as: **Archiving**
    1. **Please now poke your #hca-operations buddies to continue the process below by Archiving the Metadata to DSP.**
    
### Step 2 - Submit project, study, samples and sequencing experiments using the Archiver and DSP service

#### Before using the Archiver service 

Please note when using the documentation below:

*   There is a difference between **api**.ingest… and **archiver**.ingest…
    * API -> **ingest_submission_uuid**
    * Archiver -> **dsp_submission_uuid**
*   Obtain and replace `{archiver_api_key}` with the key obtained by running the following cmd (replace `dev` with `staging` or `prod` depending on the environment):
    *   specify if prod/staging/dev
        ```
         aws --region us-east-1 secretsmanager get-secret-value --secret-id ingest/archiver/wrangler/secrets --query SecretString --output text | jq -jr .prod_archiver_api_key
        ``` 
    *   If you can't retrieve the archiver service api key using this command, it is likely because you do not have the required permissions. Ask a dev or wrangler to obtain the key


#### Archiver endpoints
There are currently 3 environments that you can use for the archiver:

1. `https://archiver.ingest.dev.archive.data.humancellatlas.org`: Corresponding to **DSP test environment**
1. `https://archiver.ingest.staging.archive.data.humancellatlas.org`: Corresponding to **DSP test environment**
1. `https://archiver.ingest.archive.data.humancellatlas.org`: Corresponding to **DSP production environment**

Please make sure you are using the proper endpoint when archiving (Instruction and examples written for the staging environment)

#### Using the Archiver service

Once a submission is ready in ingest (`Archiving` status after hitting submit), you need to follow the next steps:

1. Open a terminal
1. Create a DSP submission given an ingest submission UUID with a POST request
   ```
   curl -X POST https://archiver.ingest.staging.archive.data.humancellatlas.org/archiveSubmissions -H 'Content-Type: application/json' -H 'Api-Key: {archiver_api_key}' -d '{"submission_uuid": "{ingest_submission_uuid}", "alias_prefix": "HCA", "exclude_types": ["sequencingRun"] }'
   ```
   Please note this is an async request and even if it's successfully triggered (You will get a response saying that), it may take a while to create the submission.
1. Retrieve the DSP submission UUID via the ingest submission UUID

   ```
   curl -X GET  -H 'Api-Key: {archiver_api_key}' https://archiver.ingest.staging.archive.data.humancellatlas.org/latestArchiveSubmission/<ingest_submission_uuid>
   ```
   This request should give you the UUID in the json response

1. Check if submission is submittable

    *  **Check validation errors**
       ```
       curl -X GET https://archiver.ingest.staging.archive.data.humancellatlas.org/archiveSubmissions/<dsp_submission_uuid>/validationErrors -H 'Api-Key: {archiver_api_key}' 
       ```
    
    *  **Check any submission blockers**
       ```
       curl -X GET https://archiver.ingest.staging.archive.data.humancellatlas.org/archiveSubmissions/<dsp_submission_uuid>/blockers -H 'Api-Key: {archiver_api_key}' 
       ```

1. Once the archive metadata entities are validated, to finish the submission, just run the following request to complete the submission:
```
curl -X POST https://archiver.ingest.staging.archive.data.humancellatlas.org/archiveSubmissions/<dsp_submission_uuid>/complete -H 'Api-Key: {archiver_api_key}' 
```

### Step 3 - Submit sequencing runs directly to ENA

Follow Step 3 (Submit new sequencing runs) of "Update ENA runs SOP" page.