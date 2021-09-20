import requests as rq
import os
import sys
import glob
import shutil
import argparse
import re

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
    while files_page.get('_links').get('next'):
        files_page = rq.get(files_page.get('_links').get('next').get('href')).json()
        files.extend(files_page.get('_embedded').get('files'))

    files = [file for file in files if file.get('validationErrors')]
    filenames_list = [file['fileName'] for file in files]
    with open('report_files.txt', 'w') as f:
        f.write('\n'.join(filenames_list))


    # Move invalid fastq files into a new 'filtered' folder to enable new download of files which were invalid into the current directory.
    # The invalid files in the 'filtered' folder can then be optionally deleted.

    os.mkdir('filtered')

    with open('report_files.txt') as f:
        mylist = f.read().splitlines()

    fastq = glob.glob("*.fastq.gz")

    for line in mylist:
            if str(line) in fastq:
                    shutil.move(line, os.path.join('filtered',line))
            else:
                    continue
