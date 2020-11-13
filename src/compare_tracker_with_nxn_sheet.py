"""
Little script that compares the HCA dataset tracking sheet
(https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0) with Valentine
Svensson's curated single cell database (http://www.nxn.se/single-cell-studies)

The output is a formatted list that can be copied over to the dataset tracking sheet.

Usage: python3 compare_tracker_with_nxn_sheet.py

Last time updated:
2020-11-13T10:08:36.166251Z
"""

import os
import re
import requests as rq
from datetime import datetime


class ChangedHeaders(Exception):
    def __init__(self, header):
        super().__init__(f"Headers changed, couldn't find {header}")


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
    "contributor_involved": "==No",
    "hca_status": "==acknowledged",
    "date_added": "=str(datetime.today()).split(' ')[0]",
    "access_permission": None,
    "organism": "Organism",
    "sample_type": "=set_tissue('{Tissue}')",
    "health_status": None,
    "phenotype": None,
    "assay_type": "Technique",
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
    if index_value == -1:
        raise ChangedHeaders(value)
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


def select_unique_studies(valentines_sheet: [[]], tracking_sheet: [[]]):
    """
    Filter unique studies based on:
        - DOI
        - Accession
        - Paper title
    :param valentines_sheet: [[]]
                             Matrix representing nxn's database
    :param tracking_sheet: [[]]
                           Matrix representing the Dataset Tracking Sheet
    :return:
    """
    # Retrieve the indexes from the headers
    v_doi_index = find_header_index(valentines_sheet, 'DOI')
    t_doi_index = find_header_index(tracking_sheet, 'doi')
    v_data_location_index = find_header_index(valentines_sheet, 'Data location')
    t_data_location_index = find_header_index(tracking_sheet, 'data_accession')
    v_title_index = find_header_index(valentines_sheet, 'Title')
    t_title_index = find_header_index(tracking_sheet, 'pub_title')


    # Retrieve DOIs and adjust them
    valentine_dois = set([data[v_doi_index] for data in valentines_sheet])
    tracking_sheet_dois = set([track[t_doi_index] for track in tracking_sheet if track[t_doi_index]])
    tracking_sheet_dois = {f"10.{doi.split('doi.org/10.')[-1]}" for doi in tracking_sheet_dois if "doi.org" in doi}

    unregistered_dois = valentine_dois - tracking_sheet_dois

    # Translate unregistered dois into the table
    unregistered_table = [row for row in valentines_sheet if row[v_doi_index] in unregistered_dois]

    # Retrieve accessions and repeat filtering
    valentine_accessions = set([data[v_data_location_index] for data in unregistered_table if data[v_data_location_index]])
    tracking_sheet_accessions = set([track[t_data_location_index] for track in tracking_sheet if track[t_data_location_index]])

    unregistered_accessions = valentine_accessions - tracking_sheet_accessions

    second_unregistered_table = [row for row in unregistered_table if row[v_data_location_index] in unregistered_accessions or not row[v_data_location_index]]

    valentine_titles = set([data[v_title_index].lower() for data in second_unregistered_table if data[v_title_index]])
    tracking_sheet_titles = set([track[t_title_index].lower() for track in tracking_sheet if track[t_title_index]])

    unregistered_titles = valentine_titles - tracking_sheet_titles

    full_unregistered_table = [row for row in second_unregistered_table if row[v_title_index].lower() in unregistered_titles]

    return full_unregistered_table


def filter_table(valentines_table, full_database):
    """
    Filter the table based on organism/technology criteria
    :param valentines_table:
    :return:
    """
    organism_index = find_header_index(full_database, 'Organism')
    technique_index = find_header_index(full_database, 'Technique')
    measurement_index = find_header_index(full_database, 'Measurement')

    filtered_table = [row for row in valentines_table if row[organism_index].lower() in ['human', 'human, mouse', 'mouse, human']]
    filtered_table = [row for row in filtered_table if
                      row[technique_index].lower() in ["chromium", "drop-seq", "dronc-seq", "smart-seq2", "smarter", "smarter (C1)"]]
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


def update_timestamp():
    script_path = os.path.realpath(__file__)
    with open(script_path, 'r') as f:
        script = f.read()

    timestamp = datetime.now()
    timestamp_str = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    script = re.sub('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}Z', timestamp_str, script, count=1)

    with open(script_path, 'w') as f:
        f.write(script)


def main():
    # Get tsv from nxn's database and transform it into a matrix
    valentines_database = rq.get('http://www.nxn.se/single-cell-studies/data.tsv',
                                 headers={'Cache-Control': 'no-cache'})
    valentines_database.encoding = 'utf-8'  # Avoid issues with special chars
    valentines_database = valentines_database.text.splitlines()
    valentines_database = [data.split("\t") for data in valentines_database]

    # Get tracking sheet and transform it into a matrix
    tracking_sheet = rq.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ26K0ZYREykq2kR2HgA3xGol3PfFuwYu"
                            "qNBQCZgi4L7yqF2GZiNdXfQ19FtjxMvCk8IU6S_v6zih9z/pub?gid=0&single=true&output=tsv",
                            headers={'Cache-Control': 'no-cache'}).text.splitlines()
    tracking_sheet = [data.split("\t") for data in tracking_sheet]

    # Compare and filter
    entries_not_registered = select_unique_studies(valentines_database, tracking_sheet)
    filtered_table = filter_table(entries_not_registered, valentines_database)

    # Print output
    print_output(filtered_table, valentines_database, tracking_sheet)

    update_timestamp()


if __name__ == '__main__':
    main()
