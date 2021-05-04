

"""
Script to extract all existing ontology annotations in HCA Ingest for a given set of submissions.

The script takes a list of submission envelope IDs and extracts the corresponding ontology annotations from the ingest API (prod). The envelope IDs are currently hard-coded but this could easily be updated.

You can run the script in your favourite IDE (eg Pycharm) or via the command line using `python3 ontology_mappings_extractor.py`

The script generates a file called all_mappings.txt, which contains every single free-text to ontology term mapping in every biomaterial or protocol in every submission requested. To get a list of unique mappings by project, run the following prompt in the command lines:
`sort all_mappings.txt | uniq > all_mappings_unique.txt`

Improvement suggestion: read all mappings into a dictionary first, then save/print only unique ones. 

Warning - this script takes a while (10s of mins to a couple of hours!) to run for large submissions or if you give it many in one go!

Copied from HumanCellAtlas/data-wrangling 30/04/2021. Original Author Dani Welter
Updated by Marion Shadbolt in April 2021.
"""

import argparse
import requests
import pandas as pd
import sys
from datetime import date

def define_parser():
    parser = argparse.ArgumentParser(description="Parser for the arguments")
    parser.add_argument("--file", "-f", action="store", dest="file_path", type=str,
                        help="Path to a text file with project uuids.")
    parser.add_argument("--project_uuid", "-p", action="store", dest="uuid_list", type=str,
                       help="Single or comma-delimited list of project uuids.")
    parser.add_argument("--unique", "-u", action="store_true", dest="unique",
                        help="If specified, collapse duplicate curations per project.")
    parser.add_argument("--api", "-a", action="store", dest="ingest_api_url",
                        default="http://api.ingest.archive.data.humancellatlas.org/",
                        help="URL of the api to search, default is current prod api.")
    return parser


def extract_mappings(uuid, api, unique, date_str):
    project_json = requests.get("{}projects/search/findByUuid?uuid={}".format(api, uuid)).json()
    project_content = project_json['content']
    project_name = project_content['project_core']['project_short_name']
    project_mapping_list = read_properties(project_content, 'project', project_name)
    save_df(project_mapping_list, unique, date_str, write_mode='w', head=True)
    submissions_link = project_json['_links']['submissionEnvelopes']['href']
    submissions_json = requests.get(submissions_link).json()
    for submission in submissions_json['_embedded']['submissionEnvelopes']:
        biomaterials_link = submission['_links']['biomaterials']['href']
        biomaterials_mapping_list = process_json(biomaterials_link, 'biomaterials', project_name)
        save_df(biomaterials_mapping_list, unique, date_str)

        protocols_link = submission['_links']['protocols']['href']
        protocols_mapping_list = process_json(protocols_link, 'protocols', project_name)
        save_df(protocols_mapping_list, unique, date_str)

        files_link = submission['_links']['files']['href']
        files_mapping_list = process_json(files_link, 'files', project_name)
        save_df(files_mapping_list, unique, date_str)

    # TODO: Process Analysis entities


def process_json(link, schema_type, project_name):
    done = False
    mapping_list = []
    while not done:
        entries = requests.get(link).json()
        for entry in entries['_embedded'][schema_type]:
            bioentity = entry['content']['describedBy'].split('/')[-1]
            mapping_list.extend(read_properties(entry['content'], bioentity, project_name))
        if 'next' in entries['_links']:
            link = entries['_links']['next']['href']
        else:
            done = True
    return mapping_list


# this function recursively reads through an entire json doc to find all the instances of ontology mappings
def read_properties(data, bioentity, project_name, property_list=[], root=None):
    for k, v in data.items():
        if isinstance(v, dict):
            if "ontology" in v:
                ontology = v['ontology'].strip()
                text = v['text'].strip()
                property_list.append([project_name, bioentity, k, text, ontology])
            else:
                read_properties(v, bioentity, project_name, property_list, k)

        elif isinstance(v, list):
            for index, e in enumerate(v):
                if isinstance(e, dict):
                    if "ontology" in e.keys():
                        ontology = e['ontology'].strip()
                        text = e['text'].strip()
                        property_list.append([project_name, bioentity, k, text, ontology])
                    else:
                        read_properties(e, bioentity, project_name, property_list, k)
    return property_list


def save_df(mapping_list, unique, today_str, write_mode='a', head=False):
    column_names = ['STUDY', 'BIOENTITY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG']
    property_df = pd.DataFrame(mapping_list, columns=column_names)
    if unique:
        property_df.drop_duplicates(inplace=True)
    property_df.to_csv("{}_all_mappings.tsv".format(today_str), sep="\t", index=False, mode=write_mode, header=head)


def get_full_iri(obo_id):
    obo_term = obo_id.replace(":", "_")
    ols_response = requests.get('http://www.ebi.ac.uk/ols/api/terms?id={}'.format(obo_term))
    ols_json = ols_response.json()
    # if "_embedded" not in ols_json.keys():
    #     ols_response = requests.get('http://www.ebi.ac.uk/ols/api/terms?iri={}'.format(obo_term))
    #     ols_json = ols_response.json()
    return ols_json['_embedded']['terms'][0]['iri']


def main(project_uuids, unique, api):
    today = date.today()
    today_str = today.strftime("%Y-%m-%d")
    for uuid in project_uuids:
        print("Processing " + uuid)
        extract_mappings(uuid, api, unique, today_str)
    print("Getting full iris")
    with open("{}_all_mappings.tsv".format(today_str)) as mappings_file:
        property_df = pd.read_csv(mappings_file, sep="\t")
        obo_ids = list(set(property_df['SEMANTIC_TAG']))
        print("Found {} obo_ids to search and replace.".format(len(obo_ids)))
        obo_dict = {obo_id: get_full_iri(obo_id) for obo_id in obo_ids}
        property_df["SEMANTIC_TAG"].replace(obo_dict, inplace=True)
        property_df.to_csv("{}_all_mappings.tsv".format(today_str), sep="\t", index=False)
    print("Saved output to {}_all_mappings.tsv".format(today_str))
    sys.exit(0)


if __name__ == "__main__":
    parser = define_parser()
    args = parser.parse_args()
    if not args.uuid_list and args.file_path:
        print("Either -p or -f must be specified.")
        sys.exit()
    if args.uuid_list:
        uuid_list = args.uuid_list.split(",")
    if args.file_path:
        file_id_list = []
        with open(args.file_path, "r") as input_file:
            for line in input_file:
                stripped = line.strip()
                file_id_list.append(stripped)
    if args.uuid_list and args.file_path:
        id_list = list(set(uuid_list.append(file_id_list)))
    else:
        id_list = uuid_list if uuid_list else file_id_list
    main(id_list, args.unique, args.ingest_api_url)
