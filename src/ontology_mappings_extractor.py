

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
from datetime import datetime
import re


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
    parser.add_argument("--iri_replace", "-i", action="store", dest="iri_replace",
                        help="Path to a file where there are obo ids in column named 'SEMANTIC_TAG' and replace these "
                             "with full iris. All other arguments ignored.")
    return parser


def extract_mappings(uuid, api, unique, file_string):
    project_json = requests.get("{}projects/search/findByUuid?uuid={}".format(api, uuid)).json()
    project_content = project_json['content']
    project_name = project_content['project_core']['project_short_name']
    if re.search("Integration Test", project_name):
        return
    project_mapping_list = read_properties(project_content, 'project', project_name, property_list=[])
    save_df(project_mapping_list, unique, file_string)
    submissions_link = project_json['_links']['submissionEnvelopes']['href']
    submissions_json = requests.get(submissions_link).json()
    for submission in submissions_json['_embedded']['submissionEnvelopes']:
        biomaterials_link = submission['_links']['biomaterials']['href']
        biomaterials_mapping_list = process_json(biomaterials_link, 'biomaterials', project_name)
        save_df(biomaterials_mapping_list, unique, file_string)

        protocols_link = submission['_links']['protocols']['href']
        protocols_mapping_list = process_json(protocols_link, 'protocols', project_name)
        save_df(protocols_mapping_list, unique, file_string)

        files_link = submission['_links']['files']['href']
        files_mapping_list = process_json(files_link, 'files', project_name)
        save_df(files_mapping_list, unique, file_string)
    # TODO: Process Analysis entities


def process_json(link, schema_type, project_name):
    done = False
    mapping_list = []
    while not done:
        entries = requests.get(link).json()
        try:
            for entry in entries['_embedded'][schema_type]:
                bioentity = entry['content']['describedBy'].split('/')[-1]
                mapping_list.extend(read_properties(entry['content'], bioentity, project_name, property_list=[]))
            if 'next' in entries['_links']:
                link = entries['_links']['next']['href']
            else:
                done = True
        except KeyError:
            print("Error retrieving metadata from {}. Probably no submission metadata. Skipping...".format(link))
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


def save_df(type_mapping_list, unique, file_string, write_mode='a', head=False):
    column_names = ['STUDY', 'BIOENTITY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG']
    property_df = pd.DataFrame(type_mapping_list, columns=column_names)
    if unique:
        property_df = property_df.drop_duplicates()
    property_df.to_csv(file_string, sep="\t", index=False, mode=write_mode, header=head)


def get_full_iri(obo_id):
    try:
        ols_response = requests.get('http://www.ebi.ac.uk/ols/api/terms?obo_id={}'.format(obo_id))
        ols_json = ols_response.json()
        return ols_json['_embedded']['terms'][0]['iri']
    except KeyError:
        print('http://www.ebi.ac.uk/ols/api/terms?id={}'.format(obo_id))
        print("Could not find {}.".format(obo_id))
        return obo_id


def replace_obo_ids(property_df):
    obo_ids = list(set(property_df['SEMANTIC_TAG']))
    print("Found {} obo_ids to search and replace.".format(len(obo_ids)))
    obo_dict = {obo_id: get_full_iri(obo_id) for obo_id in obo_ids}
    property_df["SEMANTIC_TAG"].replace(obo_dict, inplace=True)
    return property_df


def main(project_uuids, unique, api, iri_replace):
    if iri_replace:
        print("Getting full iris")
        mappings_df = pd.read_csv(iri_replace, sep="\t")
        mappings_df = replace_obo_ids(mappings_df)
        mappings_df.to_csv(iri_replace, sep="\t", index=False)
        print("Saved output to {}".format(iri_replace))
        sys.exit(0)
    today = datetime.now()
    today_str = today.strftime("%Y-%m-%d_%H-%M")
    file_name = "outputs/{}_property_mappings.tsv".format(today_str)
    pd.DataFrame(columns=['STUDY', 'BIOENTITY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG']).to_csv(file_name, sep="\t", index=False)
    total_projects = len(project_uuids)
    print("Found {} project uuids to process.".format(total_projects))
    print("Saving results to {}.".format(file_name))
    i = 1
    for uuid in project_uuids:
        print("Processing {}, project {} of {}.".format(uuid, i, total_projects))
        extract_mappings(uuid, api, unique, file_name)
        i += 1
    print("Getting full iris")
    with open(file_name) as mappings_file:
        property_df = pd.read_csv(mappings_file, sep="\t")
        property_df = replace_obo_ids(property_df)
        property_df.to_csv(file_name, sep="\t", index=False)
    print("Saved output to {}".format(file_name))
    sys.exit(0)


if __name__ == "__main__":
    parser = define_parser()
    args = parser.parse_args()
    if not args.uuid_list and not args.file_path and not args.iri_replace:
        print("Either -p or -f or -i must be specified.")
        sys.exit()
    if args.uuid_list:
        uuid_list = args.uuid_list.split(",")
    if args.file_path:
        file_id_list = pd.read_csv(args.file_path, sep="\t", header=None)[0].to_list()
    if args.uuid_list and args.file_path:
        id_list = list(set(uuid_list.append(file_id_list)))
    elif args.file_path:
        id_list = file_id_list
    elif args.uuid_list:
        id_list = uuid_list
    else:
        id_list = []
    main(id_list, args.unique, args.ingest_api_url, args.iri_replace)
