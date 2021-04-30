

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


def extract_mappings(uuid, api):

    project_json = requests.get("{}projects/search/findByUuid?uuid={}".format(api, uuid)).json()
    project_content = project_json['content']
    project_name = project_content['project_core']['project_short_name']

    submissions_link = project_json['_links']['submissionEnvelopes']['href']
    submissions_json = requests.get(submissions_link).json()
    for submission in submissions_json['_embedded']['submissionEnvelopes']:
        biomaterials_link = submission['_links']['biomaterials']['href']
        biomaterials_mapping_list = process_json(biomaterials_link, 'biomaterials', file, project_name)
        biomaterials_df = pd.DataFrame(biomaterials_mapping_list,
                                   columns=['STUDY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG'])

        protocols_link = submission['_links']['protocols']['href']
        protocols_mapping_list = process_json(protocols_link, 'protocols', file, project_name)
        protocols_df = pd.DataFrame(protocols_mapping_list,
                                    columns=['STUDY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG'])

        files_link = submission['_links']['files']['href']
        files_mapping_list = process_json(files_link, 'files', file, project_name)
        files_df = pd.DataFrame(files_mapping_list,
                                columns=['STUDY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG'])

    # TODO: Process Analysis entities

    dataframe = pd.concat([biomaterials_df, protocols_df, files_df], ignore_index=True)

    return dataframe


def process_json(link, schema_type, file, project_name):
    done = False
    mapping_list = []
    while not done:
        entries = requests.get(link).json()
        for entry in entries['_embedded'][schema_type]:
            mapping_list.extend(read_properties(entry['content'], file, project_name))
        if 'next' in entries['_links']:
            link = entries['_links']['next']['href']
        else:
            done = True
    return mapping_list


# this function recursively reads through an entire json doc to find all the instances of ontology mappings
def read_properties(data, file, project_name, property_list=[], root=None):
    for k, v in data.items():
        if isinstance(v, dict):
            if "ontology" in v:
                ontology = v['ontology'].strip()
                text = v['text'].strip()

                # WARNING: Comment the next line out if you don't want constant feedback on the running of the script!
                # print(project_name + "\t" + k + "\t" + text + "\t" + ontology)
                file.write(project_name + "\t" + k + "\t" + text + "\t" + ontology + "\n")
                property_list.append([project_name, k, text, ontology])
            else:
                read_properties(v, file, project_name, property_list, k)

        elif isinstance(v, list):
            for index, e in enumerate(v):
                if isinstance(e, dict):
                    if "ontology" in e.keys():
                        ontology = e['ontology'].strip()
                        text = e['text'].strip()

                        # print(project_name + "\t" + k + "\t" + text + "\t" + ontology)
                        file.write(project_name + "\t" + k + "\t" + text + "\t" + ontology + "\n")
                        property_list.append([project_name, k, text, ontology])
                    else:
                        read_properties(e, file, project_name, property_list, k)
    return property_list


def main(project_uuids, unique, api):
    all_mappings = pd.DataFrame(columns=['STUDY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG'])

    for uuid in project_uuids:
        print("Processing " + uuid)
        project_df = extract_mappings(uuid, api)
        if unique:
            project_df = project_df.drop_duplicates()
        all_mappings = pd.concat([all_mappings, project_df], ignore_index=True)
    all_mappings.to_csv("all_mappings.tsv", sep="\t", index=False)
    print("Saved output to all_mappings.tsv")
    sys.exit(0)


if __name__ == "__main__":
    parser = define_parser()
    args = parser.parse_args()
    if args.uuid_list:
        id_list = args.uuid_list.split(",")
    elif args.file_path:
        id_list = []
        with open(args.file_path, "r") as input_file:
            for line in input_file:
                stripped = line.strip()
                id_list.append(stripped)
    main(id_list, args.unique, args.ingest_api_url)
