import requests as rq
import os
import glob
import shutil
import argparse
import re
import pandas as pd

def submission_uuid_is_valid(uuid):
    if not re.match("^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", uuid):
        raise argparse.ArgumentTypeError
    return uuid

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--submission-uuid', help='Submission UUID', required=True, type=submission_uuid_is_valid)
    args = parser.parse_args()

    # List the names of the fastq files that are invalid given a submission uuid.

    uuid = args.submission_uuid
    url = "https://api.ingest.archive.data.humancellatlas.org/submissionEnvelopes/search/findByUuidUuid?uuid="
    submission = rq.get(f"{url}{uuid}").json()
    files_page = rq.get(submission.get('_links').get('files').get('href')).json()
    files = files_page['_embedded']['files']
    rows = []
    for file in files:
        file_name = file['content']['file_core']['file_name']
        state = file.get('validationState')
        rows.append([file_name,state])
df = pd.DataFrame(rows)
df.to_csv("file_states.txt",sep="\t")
