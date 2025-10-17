import os
import tqdm
import json
import requests
import pandas as pd
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

# --- setup robust requests session ---
session = requests.Session()

retries = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retries)
session.mount("http://", adapter)
session.mount("https://", adapter)

def get_gxa_dois():
    with open("gxa_idf_doi.json", "r") as f:
        data = json.load(f)
    return data

def get_scea_dois():
    df = pd.read_csv("scea_dois.csv")
    df = df.set_index('scea_accession').dropna()
    return df.to_dict()['dois']

def get_cxg_dois():
    dois = {}
    print("Fetching collections from CellxGene...")
    response = session.get("https://api.cellxgene.cziscience.com/curation/v1/collections/", timeout=10)
    response.raise_for_status()
    data = response.json()
    for proj in data:
        if proj.get("doi"):
            dois[proj["collection_id"]] = proj["doi"]
    return dois

def get_hca_dois():
    azul_url = 'https://service.azul.data.humancellatlas.org/index/projects/'
    azul_proj = session.get(azul_url).json()
    uuids = [proj['projectId'][0] for proj in azul_proj['termFacets']['project']['terms']]
    dois = {}
    for uuid in tqdm.tqdm(uuids):
        project = session.get(azul_url + uuid, timeout=10).json()
        publ = project['projects'][0].get('publications')
        if not publ:
            print(f"no publications for {uuid}")
            continue
        if len(publ) == 1:
            doi = publ[0].get('doi')
        elif len(publ) > 1 and any('10.1101' in p['doi'] for p in publ):
            doi = next((p['doi'] for p in publ if '10.1101' not in p['doi']), [p['doi'] for p in publ][0])
            print(f"multiple dois in {publ}. selecting {doi}")
        else:
            doi = None
        dois[uuid] = doi
    return dois

def get_grants_by_doi(doi):
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=doi:{doi}&format=json&resultType=core"
    try:
        r = session.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        result = data["resultList"]["result"]
        if result:
            return result[0].get("grantsList", {}).get("grant", [])
    except Exception as e:
        print(f"Error for {doi}: {e}")
    return []

def get_wide_funders(dois):
    rows = []
    for uuid, doi in tqdm.tqdm(dois.items(), desc="Fetching funders from EuropePMC"):
        grants = get_grants_by_doi(doi)
        for g in grants: 
            rows.append({
                "uuid": uuid,
                "doi": doi,
                "funder": g.get('agency').strip() if g.get('agency') else None,
                "grant_id": g.get('grantId').strip() if g.get('grantId') else None
            })
    return rows

def collapse_values(series):
    return "; ".join(series.dropna().unique().astype(str))

def fetch_grant_data(grant_id):
    """Fetch data from UKRI GtR API for a given grant ID."""
    print(grant_id, flush=True)
    url = f"https://gtr.ukri.org/api/projects?ref={grant_id}"
    headers = {"Accept": "application/json"}
    response = session.get(url, headers=headers, timeout=30)
    if response.status_code == 200:
        data = response.json()
        project = data.get("projectOverview", {}).get("projectComposition", {}).get("project", {})
        title = project.get("title", None)
        amount = project.get("fund", {}).get("valuePounds", 0)
        return {"grant_id": grant_id, "title": title, "amount": amount}
    return {"grant_id": grant_id, "title": None, "amount": 0}

def clear_data(df):
    df['grant_id'] = df['grant_id'].str.split(', ')
    df = df.explode('grant_id', ignore_index=True)
    return df

# add wellcome trust grants
def add_wellcome_trust_amounts(df):
    if not os.path.exists("Wellcome-grants-awarded-1-October-2005-to-1-September-2025.xlsx"):
        url = "https://cms.wellcome.org/sites/default/files/2025-09/Wellcome-grants-awarded-1-October-2005-to-1-September-2025.xlsx"
        r = session.get(url, timeout=30)
        with open("Wellcome-grants-awarded-1-October-2005-to-1-September-2025.xlsx", "wb") as f:
            f.write(r.content)
    wellcome_df = pd.read_excel("Wellcome-grants-awarded-1-October-2005-to-1-September-2025.xlsx")
    wellcome_df = wellcome_df[wellcome_df['Recipient Org:Country'] == 'United Kingdom']
    mapping = wellcome_df.set_index('Internal ID')['Amount Awarded']
    df['pounds'] = df['grant_id'].map(mapping).fillna(df['pounds'])
    return df

# cxg
if os.path.exists("cxg_uk_funded_grants_uk.csv"):
    cxg_df = pd.read_csv("cxg_uk_funded_grants_uk.csv", index_col=False)
else:
    dois = get_cxg_dois()
    cxg_dict = get_wide_funders(dois)
    cxg_df = pd.DataFrame(cxg_dict).groupby('grant_id', as_index=False).agg(collapse_values)
    cxg_df.to_csv("cxg_uk_funded_grants.csv", index=False)
    print("Fetching data for grant IDs:")
    print("NOTE: This may take a while.")
    cxg_df['pounds'] = cxg_df['grant_id'].apply(lambda x: fetch_grant_data(x)['amount'] if pd.notna(x) else 0)
cxg_df = clear_data(cxg_df)
cxg_df = add_wellcome_trust_amounts(cxg_df)
cxg_df.to_csv("cxg_uk_funded_grants_uk.csv", index=False)

# hca
if os.path.exists("hca_uk_funded_grants_uk.csv"):
    hca_df = pd.read_csv("hca_uk_funded_grants_uk.csv", index_col=False)
else:
    dois = get_hca_dois()
    hca_dict = get_wide_funders(dois)
    hca_df = pd.DataFrame(hca_dict).groupby('grant_id', as_index=False).agg(collapse_values)
    hca_df.to_csv("hca_uk_funded_grants.csv", index=False)
    print("Fetching data for grant IDs:")
    print("NOTE: This may take a while.")
    hca_df['pounds'] = hca_df['grant_id'].apply(lambda x: fetch_grant_data(x)['amount'] if pd.notna(x) else 0)
hca_df = clear_data(hca_df)
hca_df = add_wellcome_trust_amounts(hca_df)
hca_df.to_csv("hca_uk_funded_grants_uk.csv", index=False)

# scea
if os.path.exists("scea_uk_funded_grants_uk.csv"):
    scea_df = pd.read_csv("scea_uk_funded_grants_uk.csv", index_col=False)
else:
    dois = get_scea_dois()
    scea_dict = get_wide_funders(dois)
    scea_df = pd.DataFrame(scea_dict).groupby('grant_id', as_index=False).agg(collapse_values)
    scea_df.to_csv("scea_uk_funded_grants.csv", index=False)
    print("Fetching data for grant IDs:")
    print("NOTE: This may take a while.")
    scea_df['pounds'] = scea_df['grant_id'].apply(lambda x: fetch_grant_data(x)['amount'] if pd.notna(x) else 0)
    scea_df.to_csv("scea_uk_funded_grants.csv", index=False)
scea_df = clear_data(scea_df)
scea_df = add_wellcome_trust_amounts(scea_df)
scea_df.to_csv("scea_uk_funded_grants_uk.csv", index=False)

# gxa
if os.path.exists("gxa_uk_funded_grants.csv"):
    gxa_df = pd.read_csv("gxa_uk_funded_grants.csv", index_col=False)
else:
    dois = get_gxa_dois()
    gxa_dict = get_wide_funders(dois)
    gxa_df = pd.DataFrame(gxa_dict).groupby('grant_id', as_index=False).agg(collapse_values)
    gxa_df.to_csv("gxa_uk_funded_grants.csv", index=False)
if 'pounds' not in gxa_df.columns:
    print("Fetching data for grant IDs:")
    print("NOTE: This may take a while.")
    gxa_df['pounds'] = gxa_df['grant_id'].apply(lambda x: fetch_grant_data(x)['amount'] if pd.notna(x) else 0)
    gxa_df.to_csv("gxa_uk_funded_grants.csv", index=False)
gxa_df = clear_data(gxa_df)
gxa_df = add_wellcome_trust_amounts(gxa_df)
gxa_df.to_csv("gxa_uk_funded_grants_uk.csv", index=False)