import os
import re
import json
import ftplib
import string
import requests
from tqdm import tqdm

FTP_SERVER = 'ftp.ebi.ac.uk'
BASE_PATH = '/pub/databases/microarray/data/atlas/experiments/'
# BASE_PATH = '/pub/databases/microarray/data/atlas/sc_experiments/'
FTP_DIR = 'gxa_idf_files'
# FTP_DIR = 'scea_idf_files'

def download_idf_from_ftp(output_dir = FTP_DIR,
                     ftp_server = FTP_SERVER, 
                     base_path = BASE_PATH):
    os.makedirs(output_dir, exist_ok=True)
    missing_dirs = [] # btw we can check dirs that are files in the ftp
    with ftplib.FTP(ftp_server) as ftp:
        ftp.login()
        ftp.cwd(base_path)
        items = ftp.nlst()
        for item in tqdm(items):
            # if filename has dot it's not an accession but likely a file, thus skip
            if '.' in item:
                continue
            if f"{item}.idf.txt" in os.listdir(output_dir):
                continue
            try:
                ftp.cwd(base_path + item)
            except Exception:
                missing_dirs.append(item)
            files = ftp.nlst()
            idf_files = [f for f in files if f.endswith("idf.txt")]
            # unlikely but if we have multiple idf.txt files, we download all of them (we didn't have)
            for f in idf_files:
                local_path = os.path.join(output_dir, f"{f}")
                if not os.path.exists(local_path):
                    with open(local_path, "wb") as fp:
                        ftp.retrbinary(f"RETR {f}", fp.write)
                # print(f"Downloaded {item}/{f} -> {local_path}")
    print(f"Following accessions in FTP were not folders and IDF could not be accessed: {missing_dirs}")

def clean_doi(dirty_doi):
    """removing redundant prefix in DOI like 'doi: ' or 'https://doi.org/'"""
    if not dirty_doi:
        return ""    
    match = re.search(r'10\.\d{4,9}/\S+', dirty_doi)
    return match.group(0) if match else dirty_doi

def get_doi_from_idf(output_dir, idf_file):
    with open(f"{output_dir}/{idf_file}", "r", encoding="utf-8") as file:
        dois = []
        for line in file:
            if 'Publication DOI' in line:
                dois = [clean_doi(doi) for doi in line.removeprefix("Publication DOI\t").rstrip().split("\t")]
    return dois

def fix_json_dois(jd):
    ab = list(string.ascii_lowercase)
    new_jd = {}
    for key, value in jd.items():
        if not value:
            continue
        elif not any(v.startswith('10') for v in value):
            print(f"DOI missing: {key}-> {value}")
            continue
        elif len(value) == 1:
            new_jd[key] = value[0]
        elif len(value) > 1:
            for i, v in enumerate(value):
                new_jd[f"{key}_{ab[i]}"] = v
    return new_jd

def main():
    acc_dict = {}
    download_idf_from_ftp()
    for d in tqdm(os.listdir(FTP_DIR)):
        scea_acc = d.removesuffix(".idf.txt")
        try:
            dois = get_doi_from_idf(FTP_DIR, d)
        except Exception as e:
            print(f"Error reading file {d}: {e}")
        acc_dict[scea_acc] = None
        if not dois:
            continue
        dois = [doi for doi in dois if doi != '']
        acc_dict[scea_acc] = dois
    
    acc_dict = fix_json_dois(acc_dict)
    with open(f'{FTP_DIR.replace("files", "doi")}.json', 'w', encoding='utf-8') as f:
        json.dump(acc_dict, f)


if __name__ == "__main__":
    main()