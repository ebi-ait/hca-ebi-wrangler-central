import requests
import hashlib
import urllib.parse


def getDryadDatasetFileManifest(dataset_doi_url_format, dryad_api_url):
    "Given the url-doi for a Dryad dataset return the filenames and download urls"
    #### Get the dataset version
    dataset_url = "{}api/v2/datasets/{}".format(dryad_api_url,dataset_doi_url_format)
    contents = requests.get(dataset_url)
    dataset_record = contents.json()
    dataset_version_id_address = dataset_record["_links"]["stash:version"]["href"]
    # print(dataset_version_id_address)

    #### Get the file manifest page
    dataset_files_url = "{}{}/files".format(dryad_api_url,dataset_version_id_address)
    file_page = requests.get(dataset_files_url)

    ### Paginate file manifest and extract filename + url
    page = file_page.json()
    file_manifest = []
    files_total = page.get("total")
    file_counter = 0

    while page["_links"]:
        files = page["_embedded"]["stash:files"]
        # print(len(files), file_counter)

        ### Get filename + url
        for a_file in files:
            file_download_url = "{}{}".format(dryad_api_url, a_file["_links"]["stash:download"]["href"])
            file_correct_name = a_file["path"]
            file_manifest.append([file_download_url,file_correct_name])
            file_counter = file_counter + 1
        if file_counter > files_total:
            break
        if "next" in page["_links"]:
            next_file_page = requests.get("{}{}".format(dryad_api_url,page["_links"]["next"]["href"]))
            page = next_file_page.json()
        else:
            #print(page["_links"])
            break

    print("Manifest length matches the expected length: ",file_counter==files_total)
    return file_manifest


    file_metadata = files_json["_embedded"]["stash:files"][0]
    file_download_url = "{}{}".format(dryad_api_url,file_metadata["_links"]["stash:download"]["href"])
    file_correct_name = file_metadata["path"]
    print(file_download_url, file_correct_name)

def saveDryadFileManifest(dataset_doi,file_manifest):
    "Given a Dryad file manifest and its doi save the manifest to a file named after the doi"
    dataset_doi_url_format = urllib.parse.quote(dataset_doi, safe='')
    manifest_filename = "{}_file_manifest.txt".format(dataset_doi_url_format)
    with open(manifest_filename, "w") as f:
        for file_data in file_manifest:
            download_url, file_name = file_data
            f.write("{} {}\n".format(download_url, file_name))

def sha256File(file_path):
    "Given the filepath return the sha256"
    # Check that the file is complete
    # BUF_SIZE is arbitary!
    BUF_SIZE = 65536  # let's read stuff in 64kb chunks!
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()

dataset_doi = "doi:10.5061/dryad.8pk0p2ns8"
dryad_api = "https://datadryad.org/"

# Convert doi to url format
dataset_doi_url_encoded = urllib.parse.quote(dataset_doi, safe='')

# Get dataset's file manifest
dataset_file_manifest = getDryadDatasetFileManifest(dataset_doi_url_encoded, dryad_api)

# Save file manifest
saveDryadFileManifest(dataset_doi,dataset_file_manifest)

# Download each file in the dataset manifest
for file_data in dataset_file_manifest:
    file_download_url, file_name = file_data
    # Stream file
    response = requests.get(file_download_url, stream=True)
    with open(file_name, mode="wb") as file:
         for chunk in response.iter_content(chunk_size=10 * 1024):
             file.write(chunk)

    # Check file integrity
    if sha256File(file_name)!=response.headers.get("x-amz-meta-sha256"):
        print(file_name, sha256File(file_name), response.headers.get("x-amz-meta-sha256"))
        break
    else:
        print("{} downloaded".format(file_name))
