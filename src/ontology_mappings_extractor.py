

"""
Script to extract all existing ontology annotations in HCA Ingest for a given set of projects.

The script takes a list of project UUIDs and extracts the corresponding ontology annotations from the ingest API (prod).

Project UUIDs can be specified as a comma delimited list or as a text file.

You can run the script in your favourite IDE (eg Pycharm) or via the command line using `python3 ontology_mappings_extractor.py`

The script generates a file called YYYY-mm-dd_HH-MM_property_mappings.tsv, which contains every single free-text to ontology term mapping in every biomaterial or protocol in every submission requested. To get a list of unique mappings by project, use the -u flag

Improvement suggestion: read all mappings into a dictionary first, then save/print only unique ones. 

Warning - this script takes a while (10s of mins to a couple of hours!) to run for large submissions or if you give it many in one go!

Copied from HumanCellAtlas/data-wrangling 30/04/2021. Original Author Dani Welter
Updated/refactored by Marion Shadbolt in April/May 2021.
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
    """
    Method to iterate over project metadata as well as the entities in all submissions in a project and save progress to
    file.
    :param uuid: project uuid
    :type uuid: string
    :param api: string of ingest api to search
    :type api: string
    :param unique: Toggle to collapse duplicate curations
    :type unique: bool
    :param file_string: Path to file to save extracted mappings
    :type file_string: str
    """
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
    """
    Iterate through all pages of entities for a particular schema type in a particular submission.
    :param link: Link to the submission entities to request
    :type link: string
    :param schema_type: which type to return, one of biomaterials, files, protocols
    :type schema_type: string
    :param project_name: The short name of the projects
    :type project_name: string
    :return mapping_list: List of curation mappings
    :rtype mapping_list: list
    """
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
    """
    Recursively read through all properties of each json entity and retrieve ontology curations.
    :param data: Content from api request
    :type data: dict
    :param bioentity: The schema type of the content, fills the 'BIOENTITY' field in output
    :type bioentity: string
    :param project_name: The shortname of the project, fills the 'STUDY' field in output
    :type project_name: string
    :param property_list: The list of properties and curations in a dictionary for each property
    :type property_list: list of dicts
    :param root:
    :type root:
    :return: property_list - the list of property curations
    :rtype: list of dicts
    """
    for k, v in data.items():
        if isinstance(v, dict):
            if "ontology" in v:
                ontology = v['ontology'].strip()
                if ontology != "":
                    text = v['text'].strip()
                    property_list.append([project_name, bioentity, k, text, ontology])
            else:
                read_properties(v, bioentity, project_name, property_list, k)

        elif isinstance(v, list):
            for index, e in enumerate(v):
                if isinstance(e, dict):
                    if "ontology" in e.keys():
                        ontology = e['ontology'].strip()
                        if ontology != "":
                            text = e['text'].strip()
                            property_list.append([project_name, bioentity, k, text, ontology])
                    else:
                        read_properties(e, bioentity, project_name, property_list, k)
    return property_list


def save_df(type_mapping_list, unique, file_string, write_mode='a', head=False):
    """
    Save curation dataframe to file.
    :param type_mapping_list: The list of property curations
    :type type_mapping_list: list of dicts
    :param unique: Whether to collapse unique curations
    :type unique: bool
    :param file_string: The path to where to save the curations
    :type file_string: string
    :param write_mode: The write mode to use, append by default
    :type write_mode: string
    :param head: Whether to print the header of the dataframe
    :type head: bool
    """
    column_names = ['STUDY', 'BIOENTITY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG']
    property_df = pd.DataFrame(type_mapping_list, columns=column_names)
    if unique:
        property_df = property_df.drop_duplicates()
    property_df.to_csv(file_string, sep="\t", index=False, mode=write_mode, header=head)


def get_full_iri(obo_id):
    """
    Given an ontology id of the form X:01234, look up the full iri using the ebi ols
    :param obo_id: ontology identifier, e.g. HsapDv:0000087
    :type obo_id: string
    :return: full iri for the term, e.g. http://purl.obolibrary.org/obo/HsapDv_0000087
    :rtype: string
    """
    try:
        ols_response = requests.get('http://www.ebi.ac.uk/ols/api/terms?obo_id={}'.format(obo_id))
        ols_json = ols_response.json()
        return ols_json['_embedded']['terms'][0]['iri']
    except KeyError:
        print('http://www.ebi.ac.uk/ols/api/terms?id={}'.format(obo_id))
        print("Could not find {}.".format(obo_id))
        return None


def replace_obo_ids(property_df):
    """
    Given a pandas DataFrame with the column 'SEMANTIC_TAG' filled with ontology ids of the form X:01234, replace those
    ontology ids with the full iris
    :param property_df: A pandas dataframe with column 'SEMANTIC_TAG' filled with obo_ids
    :type property_df: DataFrame
    :return: The updated DataFrame
    :rtype: DataFrame
    """
    obo_ids = list(set(property_df['SEMANTIC_TAG']))
    print("Found {} obo_ids to search and replace.".format(len(obo_ids)))
    obo_dict = {obo_id: get_full_iri(obo_id) for obo_id in obo_ids}
    property_df["SEMANTIC_TAG"].replace(obo_dict, inplace=True)
    return property_df


def main(project_uuids, unique, api, iri_replace):
    """
    The main method of the program that calls other methods and iterates over the specified project uuids.
    :param project_uuids: A list of project uuids from which to retrieve ontology curations
    :type project_uuids: list of strings
    :param unique: Toggle to indicate whether to collapse duplicate curations within a project
    :type unique: bool
    :param api: The ingest api to search
    :type api: string
    :param iri_replace: Toggle to indicate whether to replace obo ids with full iris
    :type iri_replace: bool
    """
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
        property_df = property_df.dropna()
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
