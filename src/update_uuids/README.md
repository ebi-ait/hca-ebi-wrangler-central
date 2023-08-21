# Restore submission

## Description of the scripts

These scripts were created to fix the issue described in [dcp1163](https://app.zenhub.com/workspaces/operations-5fa2d8f2df78bb000f7fb2b5/issues/gh/ebi-ait/hca-ebi-wrangler-central/1163)

In short, what they do is:

- Take a spreadsheet with UUIDs and create a submission, with the same content as the original but different UUIDs. The wanted UUIDs are then taken into a mapping file (uuid_mapping.json).
- Connect to the database and modify the records for the UUIDs
- Connect to the Azul to retrieve the `dataFileUuid`s, then connect to the database and modify the records for the files.

## How to run

### Requirements

- python3 (With the libraries from the requirements.txt installed)
- [Kubernetes clusters set-up](https://github.com/ebi-ait/ingest-kube-deployment)
- Spreadsheet with UUIDs

## Step 1: create a submission

For this step, we run the first script:
```
python3 create_submission_from_spreadsheet_with_uuids.py <project_uuid> <token_ingest> <spreadsheet_path> <submission_uuid>
```

The ingest token can be retrieved following [these steps](https://ebi-ait.github.io/hca-ebi-dev-team/operations_tasks/api_token.html)

This step will generate a submission in ingest, under the project specified, and result in a json file called `uuid_mapping.json`

Please note that the project needs to be in an status where new submissions can be made - If not, the script will fail.

Also note that this script is configured for prod: please modify the script for the API url to test it in other environments.


## Step 2: Connect to the MongoDB database

To connect to the mongoDB database, please follow the instructions [here](https://github.com/ebi-ait/ingest-kube-deployment#using-a-mongodb-client)

Please note that if the connection is forwarded to another port, the url needs to be updated in the next step

## Step 3: Modify the UUIDs in the MongoDB database

For this step, we will modify the UUIDs directly in the database.

It is assumed that the connection to the mongoDB database is open, from the previous step.

```bash
python3 modify_uuids_in_db.py 
```

Once it finishes, all the UUIDs will have been modified to their original value in the spreadsheet.

## Step 4: Modify the dataFileUuids in the MongoDB database

Files have their own dataFileUuid, that is used downstream to identify the data file and separate it from the document
that defines the metadata for that file.

If the submission has already been pushed to the Data portal, Azul has a copy of this information and needs to be queried,
as this information does not live in the spreadsheet.

```bash
python3 modify_fileUuids_in_db.py <project_uuid>
```

After this, everything should be set-up and the submission should be ready for file upload.