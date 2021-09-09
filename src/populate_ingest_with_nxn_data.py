import itertools
import Levenshtein
import requests
import re

INGEST_URL = "https://api.ingest.archive.data.humancellatlas.org/projects/"
NXN_URL = "http://www.nxn.se/single-cell-studies/data.tsv"

nxn_data_header_map ={}

def load_ingest_data():
    # get ingest data as json
    ingest_data = requests.get(INGEST_URL,
                               params={"page": 0, "size": 1000}).json()["_embedded"]["projects"]
    ingest_data = [data.get("content") for data in ingest_data]
    return ingest_data

def load_nxn_data():
    # Get nxn's database as tsv and transform it into a matrix
    nxn_data = requests.get(NXN_URL, headers={'Cache-Control': 'no-cache'})
    nxn_data.encoding = 'utf-8'  # Avoid issues with special chars
    nxn_data = nxn_data.text.splitlines()
    nxn_data = [data.split("\t") for data in nxn_data]
    return nxn_data

def reformat_title(title: str) -> str:
    return re.sub("\W", "", title).lower().strip()

def get_distance_metric(title1: str,title2: str):
    if not all([title1, title2]):
        return 0
    max_len = max(len(title1), len(title2))
    dist_metric = 100-(Levenshtein.distance(title1, title2)/max_len)*100
    return dist_metric

# try to refactor later
def get_new_nxn_data(ingest_data, nxn_data):
    nxn_pub_doi_index = nxn_data_header_map['DOI']
    nxn_pre_doi_index = nxn_data_header_map['bioRxiv DOI']
    nxn_data_location_index = nxn_data_header_map['Data location']
    nxn_title_index = nxn_data_header_map['Title']

    # Get sets of pre-publication and published doi, from nxn data
    nxn_pub_doi = {data[nxn_pub_doi_index] for data in nxn_data[1:]}
    nxn_pre_doi = {data[nxn_pre_doi_index] for data in nxn_data[1:]}

    ingest_data_publications = list(itertools.chain.from_iterable([data.get("publications") for data in ingest_data if data.get("publications")]))
    ingest_data_pub_doi = {pub.get("doi") for pub in ingest_data_publications if pub.get("doi")}
    ingest_data_pub_urls = {pub.get("url") for pub in ingest_data_publications if pub.get("url")}
    ingest_data_pre_doi = {url.split('doi.org/')[1] for url in ingest_data_pub_urls if 'doi.org/' in url}


    new_doi = (nxn_pub_doi | nxn_pre_doi) - (ingest_data_pub_doi | ingest_data_pre_doi)

    # getting nxn data corresponding to new dois
    new_data = [row for row in nxn_data if row[nxn_pub_doi_index] in new_doi or row[nxn_pre_doi_index] in new_doi]

    # Getting set of accessions, from nxn data
    nxn_accessions = set([data[nxn_data_location_index] for data in new_data if data[nxn_data_location_index]])

    ingest_data_accessions = set(itertools.chain.from_iterable([data.get("insdc_project_accessions") for data in ingest_data if data.get("insdc_project_accessions")] +
                             [data.get("geo_series_accessions") for data in ingest_data if data.get("geo_series_accessions")] +
                             [data.get("ega_accessions") for data in ingest_data if data.get("ega_accessions")] +
                             [data.get("dbgap_accessions") for data in ingest_data if data.get("dbgap_accessions")] +
                             [data.get("array_express_accessions") for data in ingest_data if data.get("array_express_accessions")] +
                             [data.get("biostudies_accessions") for data in ingest_data if data.get("biostudies_accessions")] +
                             [data.get("insdc_study_accessions") for data in ingest_data if data.get("insdc_study_accessions")]))

    new_accessions = nxn_accessions - ingest_data_accessions

    new_data = [row for row in new_data if row[nxn_data_location_index] in new_accessions or not row[nxn_data_location_index]]

    # Retrieve titles, format them and repeat filtering with Levenshtein-based distances
    nxn_titles = set([reformat_title(data[nxn_title_index]) for data in new_data if data[nxn_title_index]])
    ingest_data_titles = set([reformat_title(pub.get("title")) for pub in ingest_data_publications if pub.get("title")])

    new_titles = nxn_titles - ingest_data_titles
    new_titles = {title for title in new_titles if not any([get_distance_metric(title, tracking_title)
                                                                              >= 97 for tracking_title in ingest_data_titles])}

    new_data = [row for row in new_data if reformat_title(row[nxn_title_index]) in new_titles]

    return new_data

def filter_nxn_data(new_nxn_data, nxn_data):
    """
    Filter the table based on organism/technology criteria
    :param valentines_table:
    :param full_database:
    :return:
    """
    organism_index = nxn_data_header_map['Organism']
    technique_index = nxn_data_header_map['Technique']
    measurement_index = nxn_data_header_map['Measurement']

    filtered_table = [row for row in new_nxn_data if row[organism_index].lower() in ['human', 'human, mouse', 'mouse, human']]
    filtered_table = [row for row in filtered_table if
                      any([tech.strip() in ["chromium", "drop-seq", "dronc-seq", "smart-seq2", "smarter", "smarter (C1)"] for tech in row[technique_index].lower().split("&")])]
    filtered_table = [row for row in filtered_table if row[measurement_index].lower() == 'rna-seq']
    return filtered_table

def get_nxn_data_header_mapping(nxn_data_header):
    return {k: v for v, k in enumerate(nxn_data_header)}

def main():
    print("loading ingest data")
    ingest_data = load_ingest_data()

    print("loading nxn data")
    nxn_data = load_nxn_data()

    nxn_data_header_map = get_nxn_data_header_mapping(nxn_data[0])

    print("comparing and fetching new nxn data")
    new_data = get_new_nxn_data(ingest_data, nxn_data)
    new_data = filter_nxn_data(new_data, nxn_data)
    print(f"found {len(new_data)} new entries in nxn data")

    print("populating ingest with the new entries from nxn data")



if __name__ == '__main__':
    main()
