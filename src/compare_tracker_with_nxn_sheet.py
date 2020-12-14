# coding=utf-8
"""
Script that compares the HCA dataset tracking sheet
(https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0) with Valentine
Svensson's curated single cell database (http://www.nxn.se/single-cell-studies) or searches for duplicates in the
tracking sheet.

The output is a formatted list that can be copied over to the dataset tracking sheet or a tab-separated list of
duplicated entries


Usage: python3 compare_tracker_with_nxn_sheet.py [-cd]
Last time updated:
2020-12-14T14:55:11.520002Z
"""

import argparse
import itertools
import os
import re
import requests as rq
import collections
from datetime import datetime

import pandas as pd
import Levenshtein


"""
Map between Data Tracking sheet headers and the desired input. 
Every value gets passed to eval_value(), which will return the desired formatted output.
There are 3 main types of input:
- None: No way of extracting this value. Returns empty string
- Starts with "==": The value returned should be mapped to valentine's database and returned as a literal string. 
                    e.g. "==https://doi.org/{DOI}" will return "https://doi.org/<value_of_DOI_in_row>"
- Starts with "=": The value will be evaluated and the result of the evaluation will be returned as a string.
                   e.g. "=set_organ('{Tissue}\t{Cell source}')" will call the function set_organ() with the row values
                   of {Tissue} and {Cell source} and return the value of that function.
                    
"""
map = {
    "dcp_id" : None,
    "project_short_name": None,
    "data_accession": "Data location",
    "contributor_involved": "==no",
    "hca_status": "==acknowledged",
    "date_added": "=str(datetime.today()).split(' ')[0]",
    "access_permission": None,
    "organism": "=set_organism('{Organism}')",
    "sample_type": "=set_tissue('{Tissue}')",
    "health_status": None,
    "phenotype": None,
    "assay_type": "='{Technique}'.replace(' & ', ',')",
    "organ": "=set_organ('{Tissue}\t{Cell source}')",
    "cell_count_estimate": "Reported cells total",
    "living_eu_donors": None,
    "nucleic_acid_source": None,
    "data_available": "='yes' if '{Data location}' else 'no'",
    "technical_benchmarking": None,
    "broker_to_archives": None,
    "broker_to_scea": None,
    "primary_wrangler": None,
    "pub_title": "Title",
    "hca_pub": None,
    "pub_link": "==https://doi.org/{DOI}",
    "pmid": "=set_pmid('{Title}')",
    "doi": "DOI",
    "scea_accession": None,
    "github_link": None,
    "ingest_project_uuid": None,
    "comments": "=={Cell source} {Developmental stage}"
}

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--compare", action="store_true", help="Compare dataset tracking sheet with valentines Database for new entries")
    parser.add_argument("-d", "--duplicates", action="store_true", help="Detect duplicates in the tracking sheet.")

    return parser.parse_args()

def set_organism(organisms):
    organisms = sorted([organism.strip() for organism in organisms.split(',')])
    return "&".join(organisms).lower()

def set_pmid(title):
    search_url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22{title}%22&resultType=lite&cursorMark=*&pageSize=25&format=json"
    response = rq.get(search_url)
    response_json = response.json()
    result_list = response_json['resultList']['result']
    result_list = [result for result in result_list if result['pubType'] != 'preprint']
    response_json['resultList']['result'] = result_list
    response_json['hitCount'] = len(result_list)
    return response_json['resultList']['result'][0]['pmid'] if response_json['hitCount'] == 1 else ""



def set_tissue(value):
    if not value:
        return ""
    tissue_source_list = []
    for tissue in value.split(','):
        if "culture" in tissue.lower():
            tissue_source_list.append("Cell line")
        elif "organoid" in tissue.lower():
            tissue_source_list.append('Organoid')
        else:
            tissue_source_list.append('Primary')
    tissue_source_list = list(set(tissue_source_list))
    return ','.join(tissue_source_list)


def set_organ(value):
    if not value:
        return ""
    value = value.split('\t')
    return value[0] if value[0] else value[1]


def find_header_index(matrix: [[]], value: str, header_row_index: int = 0):
    header_row = matrix[header_row_index]
    index_value = header_row.index(value)
    return index_value

def replace_all_values(value, valentines_database, row):
    while value.find('{') != -1:
        start_index = value.find('{')
        end_index = value.find('}')
        valentines_header_value = value[start_index + 1:end_index]
        v_index = find_header_index(valentines_database, valentines_header_value)
        value = value.replace("{" + valentines_header_value + "}", row[v_index])
    return value

def eval_value(value, valentines_database, row):
    if value.startswith('=='):
        value = value[2:]
        return replace_all_values(value, valentines_database, row)
    if value.startswith('='):
        value = value[1:]
        value = replace_all_values(value, valentines_database, row)
        return eval(value)


def reformat_title(title: str) -> str:
    return re.sub("\W", "", title).lower().strip()


def get_distance_metric(title1: str,title2: str):
    if not all([title1, title2]):
        return 0
    max_len = max(len(title1), len(title2))
    dist_metric = 100-(Levenshtein.distance(title1, title2)/max_len)*100
    return dist_metric


def select_unique_studies(valentines_sheet: [[]], tracking_sheet: [[]]) -> [[]]:
    """
    Filter unique studies based on:
        - DOI (DOI; bioRxiv DOI): exact match to the publication or pre-print doi
        - Accession(s) (Data location): exact match to a string in a list of accession(s)
        - Publication title (Title): approximate match (distance metric)

    :param valentines_sheet: [[]]
                             Matrix representing nxn's database
    :param tracking_sheet: [[]]
                           Matrix representing the Dataset Tracking Sheet
    :return:
    """
    # Retrieve the indexes from the headers
    v_doi_index_pub = find_header_index(valentines_sheet, 'DOI')
    v_doi_index_pre = find_header_index(valentines_sheet, 'bioRxiv DOI')
    t_doi_index1 = find_header_index(tracking_sheet, 'doi')
    t_doi_index2 = find_header_index(tracking_sheet, 'pub_link')
    v_data_location_index = find_header_index(valentines_sheet, 'Data location')
    t_data_location_index = find_header_index(tracking_sheet, 'data_accession')
    v_title_index = find_header_index(valentines_sheet, 'Title')
    t_title_index = find_header_index(tracking_sheet, 'pub_title')


    # Retrieve DOIs and adjust them
    valentine_pub_dois = {data[v_doi_index_pub] for data in valentines_sheet[1:]}
    valentine_pre_dois = {data[v_doi_index_pre] for data in valentines_sheet[1:]}

    tracking_sheet_pub_dois = {track[t_doi_index1] for track in tracking_sheet[1:] if track[t_doi_index1]}
    tracking_sheet_pub_links = {track[t_doi_index2] for track in tracking_sheet[1:] if track[t_doi_index2]}
    tracking_sheet_pre_dois = {url.split('doi.org/')[1] for url in tracking_sheet_pub_links if 'doi.org/' in url}

    unregistered_dois = (valentine_pub_dois | valentine_pre_dois) - (tracking_sheet_pub_dois | tracking_sheet_pre_dois)

    # Translate unregistered dois into the table
    unregistered_table = [row for row in valentines_sheet if row[v_doi_index_pub] in unregistered_dois or row[v_doi_index_pre] in unregistered_dois]

    # Retrieve accessions and repeat filtering
    valentine_accessions = set([data[v_data_location_index] for data in unregistered_table if data[v_data_location_index]])
    tracking_sheet_accessions = set([track[t_data_location_index] for track in tracking_sheet[1:] if track[t_data_location_index]])

    #TODO WORK ON THIS
    unregistered_accessions = valentine_accessions - tracking_sheet_accessions

    second_unregistered_table = [row for row in unregistered_table if row[v_data_location_index] in unregistered_accessions or not row[v_data_location_index]]

    # Retrieve titles, format them and repeat filtering with Levenshtein-based distances
    valentine_titles = set([reformat_title(data[v_title_index]) for data in second_unregistered_table if data[v_title_index]])
    tracking_sheet_titles = set([reformat_title(track[t_title_index]) for track in tracking_sheet if track[t_title_index]])

    unregistered_titles = valentine_titles - tracking_sheet_titles
    unregistered_titles = {title for title in unregistered_titles if not any([get_distance_metric(title, tracking_title)
                                                                              >= 97 for tracking_title in tracking_sheet_titles])}

    full_unregistered_table = [row for row in second_unregistered_table if row[v_title_index] in unregistered_titles]

    return full_unregistered_table


def filter_table(valentines_table, full_database):
    """
    Filter the table based on organism/technology criteria
    :param valentines_table:
    :param full_database:
    :return:
    """
    organism_index = find_header_index(full_database, 'Organism')
    technique_index = find_header_index(full_database, 'Technique')
    measurement_index = find_header_index(full_database, 'Measurement')

    filtered_table = [row for row in valentines_table if row[organism_index].lower() in ['human', 'human, mouse', 'mouse, human']]
    filtered_table = [row for row in filtered_table if
                      any([tech.strip() in ["chromium", "drop-seq", "dronc-seq", "smart-seq2", "smarter", "smarter (C1)"] for tech in row[technique_index].lower().split("&")])]
    filtered_table = [row for row in filtered_table if row[measurement_index].lower() == 'rna-seq']
    return filtered_table


def print_output(filtered_table, full_database, full_tracking_sheet):
    t_header_length = len(full_tracking_sheet[0])

    table_final = []

    for row in filtered_table:
        tracking_sheet_row = [""] * t_header_length
        for key, value in map.items():
            if not value:
                continue
            tracking_sheet_index = find_header_index(full_tracking_sheet, key)
            if not value.startswith("="):
                valentines_index = find_header_index(full_database, value)
                tracking_sheet_row[tracking_sheet_index] = row[valentines_index]
            else:
                tracking_sheet_row[tracking_sheet_index] = eval_value(value, full_database, row)

        table_final.append(tracking_sheet_row)

    for r in table_final:
        print("\t".join(r))


"""
REFACTORING FUNCTION TO FIND DUPLICATES; CURRENTLY UNDER DEVELOPMENT.
"""
def find_dup(tracking_sheet):
    pmid_index = find_header_index(tracking_sheet, 'pmid')
    doi_index = find_header_index(tracking_sheet, 'doi')
    pub_link_index = find_header_index(tracking_sheet, 'pub_link')
    accessions_index = find_header_index(tracking_sheet, 'data_accession')
    pub_title_index = find_header_index(tracking_sheet, 'pub_title')

    [tracking_sheet[i].append(reformat_title(tracking_sheet[i][pub_title_index])) for i in range(len(tracking_sheet))]
    indices = set()

    # Pmid
    seen = set()
    indices |= set(index for index, value in enumerate(tracking_sheet) if
                   value[pmid_index].strip() and value[pmid_index].strip() in seen or seen.add(
                       value[pmid_index].strip()))

    # Doi
    print(indices)
    seen = set()
    indices |= set(index for index, value in enumerate(tracking_sheet) if
                   value[doi_index].strip() and value[doi_index] != '10.1038/NA' and value[doi_index].strip() in seen
                   or seen.add(value[doi_index].strip()))

    # Doi in pub_links
    """
    seen = set()
    indices |= set(index for index, value in enumerate(tracking_sheet[1:]) if
                   value[pub_link_index].strip() and value[pub_link].strip() in seen or seen.add(
                       value[pmid_index].strip()))
    """
    # Accessions
    print(indices)
    seen = set()
    accessions = [accession[accessions_index].split(',') for accession in tracking_sheet]
    indices |= set(index for index, accession in enumerate(accessions) for i in range(len(accession)) if accession[i]
                   and accession[i] in seen or seen.add(accession[i]))

    # Publication title (formatted)
    seen = set()

    indices |= set(index for index_comp in range(len(tracking_sheet)) for index, value in enumerate(tracking_sheet)
                   if index > index_comp and value[-1] and tracking_sheet[index_comp][-1] and get_distance_metric(value[-1], tracking_sheet[index_comp][-1]) >= 97 and value[-1] in seen
                   or seen.add(value[-1].strip()))

    return list(indices)


def find_duplicates(tracking_sheet: pd.DataFrame):
    """
    Find duplicates in tracker sheet based on:
        - DOI (doi; pub_link): exact match to the doi; exact match to a doi within a link
        - Accession(s) (data_accession): exact match to a string in a list of accession(s)
        - Publication title (pub_title): approximate match (distance metric)
        - Publication link (pub_link): exact match to the full publication link
        - pmid: exact match to the pmid
    :param tracking_sheet: pd.DataFrame
                           DataFrame representing the Dataset Tracking Sheet
    :return:
    """
    indices = []
    length = tracking_sheet.shape[0]
    tracking_sheet['reformatted_pub_title'] = [reformat_title(i) for i in tracking_sheet['pub_title']]

    for i, j in itertools.combinations(range(length), 2):
        if list(tracking_sheet['pmid'])[i].strip() in list(tracking_sheet['pmid'])[j].strip() and list(tracking_sheet['pmid'])[i].strip() != '':
            indices.append(i)
        if list(tracking_sheet['doi'])[i].strip() in list(tracking_sheet['doi'])[j].strip() and list(tracking_sheet['doi'])[i].strip() != '' and list(tracking_sheet['doi'])[i].strip() != '10.1038/NA':
            indices.append(i)
        if list(tracking_sheet['doi'])[i].strip() in list(tracking_sheet['pub_link'])[j].strip() and list(tracking_sheet['doi'])[i].strip() != '':
            indices.append(i)

    # Look for exact matches within the list of accessions
        accession1 = list(tracking_sheet['data_accession'])[i]
        accession2 = list(tracking_sheet['data_accession'])[j]
        if ',' not in accession1 and ';' not in accession1:
            if accession1.strip() in accession2 and accession1.strip() != '':
                indices.append(i)
        else:
            if ',' in accession1:
                accessions = accession1.split(',')
            elif ';' in accession1:
                accessions = accession1.split(';')
            else:
                accessions = accession1
            for accession in accessions:
                if accession in accession2:
                    indices.append(i)

    # look for approximate matches to the publication title
        if i > j:
            if list(tracking_sheet['reformatted_pub_title'])[i] != '' and list(tracking_sheet['reformatted_pub_title'])[i] != 'unspecified':
                dist_metric = get_distance_metric(list(tracking_sheet['reformatted_pub_title'])[i],list(tracking_sheet['reformatted_pub_title'])[j])
                if dist_metric >= 97:
                        indices.append(i)

    indices = list(set(indices))
    if indices:
        duplicate_entries = tracking_sheet.iloc[indices]
        return duplicate_entries
    else:
        return None


def update_timestamp():
    script_path = os.path.realpath(__file__)
    with open(script_path, 'r') as f:
        script = f.read()

    timestamp = datetime.now()
    timestamp_str = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    script = re.sub('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}Z', timestamp_str, script, count=1)

    with open(script_path, 'w') as f:
        f.write(script)


def main(c_flag, d_flag):
    # Get tracking sheet and transform it into a matrix
    tracking_sheet = rq.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ26K0ZYREykq2kR2HgA3xGol3PfFuwYu"
                            "qNBQCZgi4L7yqF2GZiNdXfQ19FtjxMvCk8IU6S_v6zih9z/pub?gid=0&single=true&output=tsv",
                            headers={'Cache-Control': 'no-cache'}).text.splitlines()
    tracking_sheet = [data.split("\t") for data in tracking_sheet]

    if c_flag:
        # Get tsv from nxn's database and transform it into a matrix
        valentines_database = rq.get('http://www.nxn.se/single-cell-studies/data.tsv',
                                     headers={'Cache-Control': 'no-cache'})
        valentines_database.encoding = 'utf-8'  # Avoid issues with special chars
        valentines_database = valentines_database.text.splitlines()
        valentines_database = [data.split("\t") for data in valentines_database]

        # Compare and filter
        entries_not_registered = select_unique_studies(valentines_database, tracking_sheet)
        filtered_table = filter_table(entries_not_registered, valentines_database)

        # Print output
        if not filtered_table:
            print("No new datasets found")
            return
        print_output(filtered_table, valentines_database, tracking_sheet)
    if d_flag:
        tracking_sheet = pd.DataFrame(tracking_sheet[1:], columns=tracking_sheet[0])
        duplicate_entries = find_duplicates(tracking_sheet)
        if duplicate_entries.empty:
            print("No duplicate entries found")
            return
        duplicate_entries = duplicate_entries[
                ['data_accession', 'pub_title', 'reformatted_pub_title', 'pub_link', 'pmid', 'doi']]
        duplicate_entries.to_csv("duplicate_entries.txt", sep="\t")

    update_timestamp()


if __name__ == '__main__':
    args = parse_arguments()
    # Check only 1 flag has been selected, not both or none
    if any([all([args.compare, args.duplicates]), not any([args.compare, args.duplicates])]):
        print("No flag or both flags selected. Please ensure you are selecting either -c or -d")
    else:
        main(args.compare, args.duplicates)
