import itertools
import Levenshtein
import requests
import re
import json
import submit_project_from_doi
from ingest.api.ingestapi import IngestApi

#  to do
# add checks to code
# clean up code
# set up logging
# make env configurable

# INGEST_URL = "https://api.ingest.archive.data.humancellatlas.org/"
INGEST_URL = "http://localhost:8080/"
# INGEST_PROJECT_URL = "https://api.ingest.archive.data.humancellatlas.org/projects/"
INGEST_PROJECT_URL = "http://localhost:8080/projects"
NXN_URL = "http://www.nxn.se/single-cell-studies/data.tsv"
EUROPE_PMC_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

#  taken from https://github.com/ebi-ait/hca-ebi-dev-team/blob/f441b517e4e06ca989f3b1866cbdd1bdb10434f2/scripts/project-catalogue/convert/tracker.py#L7
ACCESSION_PATTERNS = {
    "insdc_project_accessions": "^[D|E|S]RP[0-9]+$",
    "ega_accessions": "EGA[DS][0-9]{11}",
    "dbgap_accessions": "phs[0-9]{6}(\\.v[0-9])?(\\.p[0-9])?",
    "geo_series_accessions": "^GSE.*$",
    "array_express_accessions": "^E-....-.*$",
    "insdc_study_accessions": "^PRJ[E|N|D][a-zA-Z][0-9]+$",
    "biostudies_accessions": "^S-[A-Z]{4}[0-9]+$"
}

def load_ingest_data():
    # get ingest data as json
    ingest_data = requests.get(INGEST_PROJECT_URL,
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
def get_new_nxn_data(ingest_data, nxn_data, nxn_data_header_map):

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

def filter_nxn_data(new_nxn_data, nxn_data_header_map):
    """
    Filter the table based on organism/technology criteria
    :param valentines_table:
    :param full_database:
    :return:
    """
    organism_index = nxn_data_header_map["Organism"]
    technique_index = nxn_data_header_map["Technique"]
    measurement_index = nxn_data_header_map["Measurement"]

    filtered_table = [row for row in new_nxn_data if row[organism_index].lower() in ["human", "human, mouse", "mouse, human"]]
    filtered_table = [row for row in filtered_table if
                      any([tech.strip() in ["chromium", "drop-seq", "dronc-seq", "smart-seq2", "smarter", "smarter (C1)"] for tech in row[technique_index].lower().split("&")])]
    filtered_table = [row for row in filtered_table if row[measurement_index].lower() == 'rna-seq']
    return filtered_table

def get_nxn_data_header_mapping(nxn_data_header):
    return {k: v for v, k in enumerate(nxn_data_header)}

# adapted/taken from: https://github.com/ebi-ait/hca-ebi-dev-team/blob/f441b517e4e06ca989f3b1866cbdd1bdb10434f2/scripts/project-catalogue/convert/tracker.py#L63
def get_accessions(data_accessions: str) -> dict:
    accessions = {}
    for accession in data_accessions.split(','):
        accession = accession.strip()
        for key, pattern in ACCESSION_PATTERNS.items():
            regex = re.compile(pattern)
            if regex.match(accession):
                accessions.setdefault(key, []).append(accession)
    return accessions

def populate_ingest_with_nxn_data(nxn_data, nxn_data_header_map):
    for data in nxn_data:
        create_ingest_project(data, nxn_data_header_map)
        break

def create_ingest_project(nxn_data, nxn_data_header_map):
    # hca_status, DOI (to complete: publication_title and project description), cell count, species, accessions -->

    #  ask: how do we split accessions (Data location)? --> comma separated string  --> done

    # other compulsory UI fields are:
    # Organism the samples were generated from / identifyingOrganisms: [] --> done
    # What organs were used in your experiment? / organ: {}  --> leaving for now
    # Do the data require controlled access? / dataAccess: {} --> done
    # What library preparation and/or imaging technique/s did you use to generate the data? / technology : {} --> leaving for now
    # Date for release of the data for this project / releaseDate  --> ask

    # stuff in the project json structure:
    # publicationsInfo -- ?? --> we need to be running a periodic script for this --> added here
    # isInCatalogue --> set to true
    # "cataloguedDate"  --> gets set in ingest service
    # "dcpVersion" ?? --> don't need to populate, as per Alegria
    #  firstDcpVersion ?? --> don't need to populate, as per Alegria
    # latest_project_schema = ingest_api.get_schemas(high_level_entity="type",
    #                                                domain_entity="project",
    #                                                concrete_entity="project")[0]['_links']['json-schema']['href']
    #  need try block for this
    publications_info = submit_project_from_doi.get_pub_info("10.1016/j.cell.2017.09.004")
    # publications_info = submit_project_from_doi.get_pub_info(nxn_data[nxn_data_header_map["DOI"]])
    ingest_api = IngestApi(INGEST_URL)
    ingest_schema = submit_project_from_doi.get_ingest_schema(ingest_api)
    ingest_project_json = submit_project_from_doi.construct_project_json(publications_info, ingest_schema)
    # decide what to fix releaseDate as
    ingest_project_json["releaseDate"] = None
    ingest_project_json["cellCount"] = nxn_data[nxn_data_header_map["Reported cells total"]]
    ingest_project_json["identifyingOrganisms"] = [organism.strip() for organism in nxn_data[nxn_data_header_map["Organism"]].split(',')]
    ingest_project_json["dataAccess"] = None
    ingest_project_json["isInCatalogue"] = True
    # setting accessions:
    ingest_project_json["content"].update(get_accessions(nxn_data[nxn_data_header_map['Data location']]))
    # setting publicationsInfo, so that this works with Project Catalogue
    publicationInfo = {k: ingest_project_json["content"]["publications"][0][k]
                       for k in set(ingest_project_json["content"]["publications"][0].keys()) - {"pmid"}}
    publicationInfo["journalTitle"] = nxn_data[nxn_data_header_map["Journal"]]
    ingest_project_json["publicationsInfo"] = [publicationInfo]
    print(ingest_project_json)
    auth_token = "eyJraWQiOiJyc2ExIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkN2I1OGNjZmRiYjFmNWVhNjFlMjU5ZmQ1N2M2YjhiZDg2OTc2MDk2QGVsaXhpci1ldXJvcGUub3JnIiwiYXpwIjoiZTIwNDFjMmQtOTQ0OS00NDY4LTg1NmUtZTg0NzExY2ViZDIxIiwic2NvcGUiOiJlbWFpbCBvcGVuaWQgcHJvZmlsZSIsImlzcyI6Imh0dHBzOlwvXC9sb2dpbi5lbGl4aXItY3plY2gub3JnXC9vaWRjXC8iLCJleHAiOjE2MzE1MTg4ODEsImlhdCI6MTYzMTUxNTI4MSwianRpIjoiMzQ0YjQxN2QtMjYxNi00Y2JlLWE1NTctNmExYzU2MjY4NDg3In0.V0CNfCLsr477DTwm2mW5r9wMA101VfRjmxgAVEQsQjIE3xAgWJlbJfWsGUpaNDhGJQDhlH06m8sHLdW3BLf-ojAu6JZo8SRmRx6j6Tm3kz_ifi25cGqVoufbunHBx8UpUpe54OyT_dCM22Y9aUP-OSi0av8qiL2SU_11i2wvpR12u-LUxI6DHUDUohMZBxDVtjnZEmUUg7sPwAkJw4caPWZ8FlBfbIhYzV5muxaVYOn84qms5hRtLv22MgWlVJ_PsArwQxDO5Gv9brk8w_ZDRlGH5oD4BreYu6jT13_5qT1IZoiY70d6sTap1WqWylGEqzEK-RvwixEK_JF7alyqMQ"
    submission_headers = {'Authorization': 'Bearer {}'.format(auth_token),
                          'Content-Type': 'application/json'}

    response = requests.post(INGEST_PROJECT_URL,
                       data=json.dumps(ingest_project_json),
                       headers=submission_headers)
    print(response.json()['uuid']['uuid'])

def main():
    print("loading ingest data")
    ingest_data = load_ingest_data()

    print("loading nxn data")
    nxn_data = load_nxn_data()

    nxn_data_header_map = get_nxn_data_header_mapping(nxn_data[0])

    print("comparing and fetching new nxn data")
    new_data = get_new_nxn_data(ingest_data, nxn_data, nxn_data_header_map)
    new_data = filter_nxn_data(new_data, nxn_data_header_map)

    print(f"found {len(new_data)} new entries in nxn data")

    print("populating ingest with the new entries from nxn data")
    populate_ingest_with_nxn_data(new_data, nxn_data_header_map)

if __name__ == '__main__':
    main()
