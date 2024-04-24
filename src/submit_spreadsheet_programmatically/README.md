# Submit spreadsheets from an hca-util upload area

This script can be used to submit spreadsheets from an hca-util upload area (aka, any spreadsheet within the bucket
`hca-util-upload-area`). 

Please have python 3.6+ and the requirements in the `requirements.txt` installed in your computer

In order to submit, you need previously:
- A pre-created project in Ingest (It can be an empty one, as it can be updated). Annotate the UUID.
- A token from an account with enough authorization to create a submission (AKA, wrangler+ permits).
- An hca-util upload area (Could be any other one - But you'd need to modify the code) with the spreadsheet uploaded.

Please note that your "default" profile for the aws tooling needs to be set up with enough permits (Read/Download access needed). 
To know if you have enough permissions:
```shell
cat ~/aws/credentials # You should see a default profile.If not, copy your wrangler credentials and post them like below
[default]
aws_access_key_id = <AWS access key>
aws_secret_access_key = <AWS secret access key>

aws s3 ls --profile default s3://hca-util-upload-area/ # You should be able to see all the available upload areas
aws s3 cp --profile default s3://hca-util-upload-area/<upload_area_uuid>/<spreadsheet_name> . # You should be able to download the spreadsheet
```

Once that's ready, you can execute the script. The script provides with help if executing with the -h flag:
```
python3 submit_spreadsheet_programmatically.py -h
usage: submit_spreadsheet_programmatically.py [-h] -u UPLOAD_AREA -s SPREADSHEET_NAME -t TOKEN -p PROJECT_UUID [-e {dev,staging,prod}] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -u UPLOAD_AREA, --upload-area UPLOAD_AREA
                        HCA-Util upload area UUID
  -s SPREADSHEET_NAME, --spreadsheet-name SPREADSHEET_NAME
                        Name of the spreadsheet in the HCA-util area
  -t TOKEN, --token TOKEN
                        JWT token to authorize submission creation
  -p PROJECT_UUID, --project-uuid PROJECT_UUID
                        Project UUID to attach the submission to
  -e {dev,staging,prod}, --environment {dev,staging,prod}
                        Ingest environment. Defaults to staging.
  -d, --update-project  Wether to update project with spreadsheet
```

An example execution:

```shell
python3 bypass_download_submit.py -u "907d5566-6533-41ef-8198-a1582ef11b8e" -s "eQTL_OA2_ontologies.xlsx" \
-t "eyJWTOKEN" \
-p 49b71044-9510-47f9-a9cc-6acb9c202412 -d
```

This will take the spreadsheet named `eQTL_OA2_ontologies.xlsx` from the hca-util area and it will stream it to the 
broker endpoint, assigning the resulting submission to the project with uuid `49b71044-9510-47f9-a9cc-6acb9c202412` and
modifying the project metadata in the process (`-d` flag)
