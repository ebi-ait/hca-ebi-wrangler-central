import requests as rq
uuid = '20f37aaf-caa1-40e6-9123-be6ce8feb2d6'
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
