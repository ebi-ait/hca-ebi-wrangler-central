import re
import argparse
import requests
import hashlib
import urllib.parse
from pathlib import Path

from tqdm import tqdm

def define_parser():
    parser = argparse.ArgumentParser(description="Parser for the arguments")
    parser.add_argument("-d", "--dataset_doi", action="store",
                        type=str, required=True,
                        help="Dataset DOI")
    parser.add_argument("-a", "--dryad_api", action="store",
                        type=str, required=False, default="https://datadryad.org/",
                        help="Dryad API URL (default: https://datadryad.org/)")
    parser.add_argument("-o", "--output_dir", action="store",
                        type=str, required=False, default="out",
                        help="Output directory")
    return parser


def getDryadDatasetFileManifest(dataset_doi_url_format, dryad_api_url):
    "Given the url-doi for a Dryad dataset return the filenames and download urls"
    print("Downloading file manifest...")
    #### Get the dataset version
    dataset_url = f"{dryad_api_url}api/v2/datasets/{dataset_doi_url_format}"
    contents = requests.get(dataset_url, timeout=10)
    dataset_record = contents.json()
    dataset_version_id_address = dataset_record["_links"]["stash:version"]["href"]
    # print(dataset_version_id_address)

    #### Get the file manifest page
    dataset_files_url = f"{dryad_api_url}{dataset_version_id_address}/files"
    file_page = requests.get(dataset_files_url, timeout=10)

    ### Paginate file manifest and extract filename + url
    page = file_page.json()
    file_manifest = []
    files_total = page.get("total")
    file_counter = 0

    while page["_links"]:
        files = page["_embedded"]["stash:files"]
        # print(len(files), file_counter)

        ### Get filename + url
        for file_metadata in files:
            file_download_url = f"{dryad_api_url}{file_metadata["_links"]["stash:download"]["href"]}"
            file_correct_name = file_metadata["path"]
            file_manifest.append([file_download_url,file_correct_name])
            file_counter = file_counter + 1
        if file_counter > files_total:
            raise ValueError(f"Total files {file_counter} exceeded the expected value {files_total}")
        if "next" in page["_links"]:
            next_file_page = requests.get(f"{dryad_api_url}{page["_links"]["next"]["href"]}", timeout=10)
            page = next_file_page.json()
        else:
            break

    # print("Manifest length matches the expected length: ",file_counter==files_total)
    return file_manifest

def saveDryadFileManifest(dataset_doi,file_manifest, output_dir):
    "Given a Dryad file manifest and its doi save the manifest to a file named after the doi"
    dataset_doi_url_format = urllib.parse.quote(dataset_doi, safe='')
    manifest_file_name = f"{dataset_doi_url_format}_file_manifest.txt"
    manifest_file_path = output_dir / manifest_file_name
    with open(manifest_file_path, "w") as f:
        for file_data in file_manifest:
            download_url, file_name = file_data
            f.write(f"{download_url} {file_name}\n")
    print(f"File manifest saved: {manifest_file_path}")

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

def convert_doi_to_url(dataset_doi):
    dryad_doi_prefix_pattern = r"^doi:10\.5061/dryad\.[A-Z0-9]+"
    dryad_doi_pattern = r"^10\.5061/dryad\.[A-Z0-9]+"
    # according to crossref documentation https://www.crossref.org/blog/dois-and-matching-regular-expressions/
    general_doi_pattern = r'^10\.\d{4,9}/[-._;()/:A-Z0-9]+$'
    if re.match(dryad_doi_prefix_pattern, dataset_doi, re.IGNORECASE):
        return urllib.parse.quote(dataset_doi, safe='')
    if re.match(dryad_doi_pattern, dataset_doi, re.IGNORECASE):
        return urllib.parse.quote(f"doi:{dataset_doi}", safe='')
    if re.match(general_doi_pattern, dataset_doi, re.IGNORECASE):
        raise ValueError(f"DOI: {dataset_doi} does not follow the Dryad DOI pattern '10.5061/dryad.<a-zA-Z0-9>")
    return ValueError(f"DOI: {dataset_doi} is not in a DOI format")

def main(dataset_doi, dryad_api, output_dir):

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Convert doi to url format
    dataset_doi_url_encoded = convert_doi_to_url(dataset_doi)

    # Get dataset's file manifest
    dataset_file_manifest = getDryadDatasetFileManifest(dataset_doi_url_encoded, dryad_api)

    # Save file manifest
    saveDryadFileManifest(dataset_doi,dataset_file_manifest, output_dir)

    # Convert
    # Download each file in the dataset manifest
    n_all = len(dataset_file_manifest)
    for n, file_data in enumerate(dataset_file_manifest):
        file_download_url, file_name = file_data
        file_path = output_dir / file_name
        # Stream file
        response = requests.get(file_download_url, stream=True, timeout=10)
        with open(file_path, mode="wb") as file:
            for chunk in tqdm(response.iter_content(chunk_size=10 * 1024), unit='chunks', desc=f"Downloading file {file_name} {n}/{n_all}"):
                file.write(chunk)

        # Check file integrity
        sha256 = sha256File(file_path)
        if sha256 != response.headers.get("x-amz-meta-sha256"):
            raise ValueError(f"Invalid sha256 value for file {file_name}\nActual: {sha256}\nExpected: {response.headers.get("x-amz-meta-sha256")}")
        print(f"{file_path} downloaded")

if __name__ == "__main__":
    args = define_parser().parse_args()
    main(dataset_doi=args.dataset_doi, dryad_api=args.dryad_api, output_dir=args.output_dir)
