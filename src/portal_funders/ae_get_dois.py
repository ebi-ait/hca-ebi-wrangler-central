import requests
import re
import gzip
import json
import csv
from time import sleep
from tqdm import tqdm

BASE_API = "https://www.ebi.ac.uk/biostudies/api/v1/search"
BASE_FTP = "https://ftp.ebi.ac.uk/biostudies/fire/E-MTAB-/"

def accession_to_ftp_url(acc):
    """Constructs the FTP URL for a given ArrayExpress accession."""
    last3 = acc[-3:]
    return f"{BASE_FTP}{last3}/{acc}/Files/{acc}.idf.txt"

def fetch_idf_text(acc):
    """
    Try to fetch the IDF text file for a given accession.
    Falls back to .idf.txt.gz if the plain text version is missing.
    Returns file text or None if both fail.
    """
    url_txt = accession_to_ftp_url(acc)
    url_gz = url_txt + ".gz"

    try:
        r = requests.get(url_txt, timeout=10)
        if r.status_code == 200:
            return r.text

        # Try gzipped version if plain text not found
        r = requests.get(url_gz, timeout=10)
        if r.status_code == 200:
            return gzip.decompress(r.content).decode("utf-8", errors="ignore")

        print(f"⚠️  Missing IDF for {acc}")
        return None

    except Exception as e:
        print(f"⚠️  Error fetching IDF for {acc}: {e}")
        return None

def extract_publication_doi(idf_text):
    """
    Extracts the Publication DOI from an IDF file’s text.
    Returns the DOI string or None if not found.
    """
    if not idf_text:
        return None
    match = re.search(r"Publication DOI\s*=\s*(\S+)", idf_text)
    return match.group(1) if match else None

def fetch_accessions():
    """Paginates through BioStudies to get all ArrayExpress accessions."""
    accessions = []
    page = 1
    page_size = 1000

    while True:
        print(f"🔹 Fetching page {page}...")
        url = f"{BASE_API}?source=ArrayExpress&page={page}&pageSize={page_size}"
        r = requests.get(url)
        data = r.json()

        hits = data.get("hits", [])
        if not hits:
            break

        for hit in hits:
            accessions.append(hit["accession"])

        total = data.get("totalHits", 0)
        if page * page_size >= total:
            break

        page += 1
        sleep(0.2)  # be polite to EBI servers

    return accessions

def main():
    accessions = fetch_accessions()
    print(f"✅ Found {len(accessions)} accessions total.\n")
    with open("arrayexpress_accessions.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["accession"])
        for acc in accessions:
            writer.writerow([acc])

    result = {}

    # tqdm progress bar over all accessions
    for acc in tqdm(accessions, desc="Fetching DOIs", unit="study"):
        idf_text = fetch_idf_text(acc)
        doi = extract_publication_doi(idf_text)
        result[acc] = doi
        sleep(0.2)  # rate limiting

    # --- Save as JSON ---
    with open("arrayexpress_dois.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print("\n✅ Finished! Saved results to:")
    print(" - arrayexpress_dois.json")
    print(" - arrayexpress_dois.csv")

if __name__ == "__main__":
    main()
