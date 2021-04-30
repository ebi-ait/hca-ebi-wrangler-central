import requests

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

all_mappings = {}

# hard-coded prod ingest API URL - change if you need a different environment
INGEST_API_URL = 'http://api.ingest.archive.data.humancellatlas.org/submissionEnvelopes/'


def define_parser():
    parser = argparse.ArgumentParser(description="Parser for the arguments")
    parser.add_argument("--subs_txt", "-st", action="store", dest="sub_path", type=str,
                        help="Path to a text file with submission envelope mongo ids, e.g. 5cdbdd7dd96dad0008592f28.")
    parser.add_argument("--submission", "-s", action="store", dest="sub_list", type=str,
                       help="Single or comma-delimited list of mongo submission envelope ids, e.g. 5cdbdd7dd96dad0008592f28.")
    return parser


def extract_mappings(envelope_id, file):
    # get the submission envelope json
    jsonRaw = requests.get(INGEST_API_URL + envelope_id).json()

    # get the project links, then pull in the project json and extract the project name
    projects_link = jsonRaw['_links']['projects']['href']
    project_json = requests.get(projects_link).json()
    project_content = project_json['_embedded']['projects'][0]['content']
    project_name = project_content['project_core']['project_short_name']

    # process all the biomaterials
    biomaterials_link = jsonRaw['_links']['biomaterials']['href']
    process_json(biomaterials_link, 'biomaterials', file, project_name)

    # process all the protocols
    protocols_link = jsonRaw['_links']['protocols']['href']
    process_json(protocols_link, 'protocols', file, project_name)

# TO DO: process, file and analysis aren't currently processed - add in files once format/type are routinely ontologised!


def process_json(link, type, file, project_name):
    done = False
    while not done:
        entries = requests.get(link).json()

        for entry in entries['_embedded'][type]:
            read_properties(entry['content'], file, project_name)

        if 'next' in entries['_links']:
            link = entries['_links']['next']['href']
        else:
            done = True


# this function recursively reads through an entire json doc to find all the instances of ontology mappings
def read_properties(data, file, project_name, root=None):
    for k, v in data.items():
        if isinstance(v, dict):
            if "ontology" in v:
                ontology = v['ontology'].strip()
                text = v['text'].strip()

                # WARNING: Comment the next line out if you don't want constant feedback on the running of the script!
                # print(project_name + "\t" + k + "\t" + text + "\t" + ontology)
                file.write(project_name + "\t" + k + "\t" + text + "\t" + ontology + "\n")

            else:
                read_properties(v, file, project_name, k)

        elif isinstance(v, list):
            for index, e in enumerate(v):
                if isinstance(e, dict):
                    if "ontology" in e.keys():
                        ontology = e['ontology'].strip()
                        text = e['text'].strip()

                        # print(project_name + "\t" + k + "\t" + text + "\t" + ontology)
                        file.write(project_name + "\t" + k + "\t" + text + "\t" + ontology + "\n")

                    else:
                        read_properties(e, file, project_name, k)


def main(submission_ids):
    file = open("all_mappings.txt", "w")
    file.write("STUDY\tPROPERTY_TYPE\tPROPERTY_VALUE\tSEMANTIC_TAG\n")

    for eid in submission_ids:
        print("Processing " + eid)
        extract_mappings(eid, file)
    file.close()


if __name__ == "__main__":
    parser = define_parser()
    args = parser.parse_args()
    if args.sub_list:
        id_list = args.sub_list.split(",")
    elif args.sub_path:
        id_list = []
        with open(args.sub_path, "r") as input_file:
            for line in input_file:
                stripped = line.strip()
                id_list.append(stripped)
    main(id_list)
