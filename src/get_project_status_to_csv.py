import requests
import tqdm
import pandas as pd
from hca_ingest.api.ingestapi import IngestApi

INGEST_API_URL = "https://api.ingest.archive.data.humancellatlas.org/"
ACCESSION_FIELDS = ['insdc_project_accessions', 'ega_accessions', 'dbgap_accessions', 'geo_series_accessions', 'array_express_accessions', 'insdc_study_accessions', 'biostudies_accessions']

def get_valid_api(token=None):
    """Get a valid Ingest API client. Request a new token if the current one is invalid."""
    if not token:
        token = input("Please provide a valid token:").strip()
    api = IngestApi(INGEST_API_URL)
    api.set_token(f"Bearer {token}")
    response = requests.get(f"{INGEST_API_URL}/submissionEnvelopes/", headers=api.get_headers())
    while response.status_code != 200:
        token = input("Please provide a valid token:").strip()
        api.set_token(f"Bearer {token}")
        response = requests.get(f"{INGEST_API_URL}/submissionEnvelopes/", headers=api.get_headers())
        print("Invalid token.")
    return api

def input_multiple_lines():
    """Get multiple lines of input from the user."""
    print("Please enter the project UUIDs, one per line (add empty line to finish):")
    uuid_lines = []
    while True:
        try:
            line = input()
            if not line.strip():
                break
            uuid_lines.append(line.strip())
        except EOFError:
            break
    return uuid_lines

def get_azul_fields(azul):
    return {
        "shortname": azul.json().get('projects', [{}])[0].get('projectShortname'),
        "fastq": any(file['format'] in ['fastq', 'fastq.gz'] for file in azul.json().get('fileTypeSummaries', [])),
        "accessions": '; '.join([acc['accession'] for acc in azul.json().get('projects', [{}])[0].get('accessions', [])])
    }

def get_proj_fields(proj):
    return {
        "wrangling_state": proj.get('wranglingState'),
        "accessions": '; '.join(['; '.join(proj['content'][a]) for a in ACCESSION_FIELDS if a in proj['content']])
    }

def get_subm_envs_fields(subm_envs):
    return {
        "submission_states": ', '.join([subm_env.get('submissionState') for subm_env in subm_envs['_embedded']['submissionEnvelopes']]) if '_embedded' in subm_envs else None
    }

def save_to_csv(proj_status, csv_path='project_status.csv'):
    df = pd.DataFrame.from_dict(proj_status, orient='index')
    df.rename(columns={'index': 'uuid'}, inplace=True)
    df.to_csv(csv_path)
    print(f"Project status csv saved to {csv_path}")

def main():
    api = get_valid_api()
    uuids = input_multiple_lines()

    # initialise project status dictionary
    proj_status = {}

    for uuid in tqdm.tqdm(uuids, unit="uuid"):
        azul = requests.get("https://service.azul.data.humancellatlas.org/index/projects/" + uuid)
        proj_status[uuid] = get_azul_fields(azul)
        # get azul project information
        try:
            proj = api.get_entity_by_uuid('projects', uuid)
            subm_envs = api.get(proj['_links']['submissionEnvelopes']['href']).json()
            proj_status[uuid].update(get_proj_fields(proj))
            proj_status[uuid].update(get_subm_envs_fields(subm_envs))
        except:
            if azul.ok:
                proj_status[uuid].update({
                    "wrangling_state": None,
                    "submission_states": None
                })
            else:
                print(f"{uuid}\tconnection problems")
                break
    save_to_csv(proj_status)

if __name__ == "__main__":
    main()