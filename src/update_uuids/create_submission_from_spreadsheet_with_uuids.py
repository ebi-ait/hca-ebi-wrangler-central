"""
This script uses ingest_client components to create a submission with UUIDs that replicate the ones specified in a
spreadsheet. Refer to https://app.zenhub.com/workspaces/operations-5fa2d8f2df78bb000f7fb2b5/issues/gh/ebi-ait/hca-ebi-wrangler-central/1163
for the use case of this script.

The algorithm is as follows:
1. Create an empty submissionEnvelope attached to the project (DONE)
2. Load the spreadsheet as a JSON file, with UUID attached, using the tools in the hca_ingest.importer module
3. Create non-linked processes: Their name will be taken from the JSON file, and for each process, the UUID will be PUT.
4. For each of the entities,ordered by entity type but ALWAYS starting with protocols:
    a. Create an entity of that type in the submission
    b. Get the entity from the submission
    c. Get the UUID from the JSON file from the importer
    d. PUT the file so that the UUID updates
    e. For each process linked:
        i. Get process by process uuid
        ii. Link process
        iii. Link protocols to process


To fix the links, when finished, update through the UI with the spreadsheet
"""
import json
import os

from hca_ingest.api.ingestapi import IngestApi

from hca_ingest.importer.spreadsheet.ingest_workbook import IngestWorkbook
from hca_ingest.importer.conversion import template_manager
from hca_ingest.importer.importer import WorkbookImporter

base_process = {
    "process_core": {
        "process_id": ""
    },
    "schema_type": "process",
    "describedBy": "https://schema.humancellatlas.org/type/process/9.0.0/process"
}

maps = {
    'biomaterial': 'biomaterials',
    'file': 'files'
}

global_uuid_mapping = {'processes': {},
                       'biomaterial': {},
                       'protocol': {},
                       'file': {}}


def link_entities(to_link, from_link, ingest_api):
    ingest_api.headers['Content-Type'] = 'text/uri-list'
    ingest_api.post(to_link, data=from_link)
    ingest_api.headers['Content-Type'] = 'application/hal+json'


def create_submission_link_project(project_uuid, ingest_api):
    # Step 1: Create submission, assign new UUID to that submission, attach to project
    submission = ingest_api.create_submission()

    project = ingest_api.get_project_by_uuid(project_uuid)
    project_submissions_endpoint = ingest_api.get_link_from_resource(project, 'submissionEnvelopes')
    submissions_uri = ingest_api.get_link_from_resource(submission, 'self')
    link_entities(to_link=project_submissions_endpoint, from_link=submissions_uri, ingest_api=ingest_api)

    return submission


def load_spreadsheet_json(spreadsheet_path, ingest_api):
    # Step 2: Load the spreadsheet. We will use and set-up tools from the hca_ingest library

    ingest_workbook = IngestWorkbook.from_file(spreadsheet_path)
    template_mgr = template_manager.build(ingest_workbook.get_schemas(), ingest_api)
    workbook_importer = WorkbookImporter(template_mgr)
    spreadsheet_json, _ = workbook_importer.do_import(ingest_workbook, False, None, False)
    return spreadsheet_json


def create_non_linked_processes(spreadsheet_json, ingest_api, submission):
    submission_url = ingest_api.get_link_from_resource(submission, 'self')

    for entity_type, entity_dict in spreadsheet_json.items():
        for entity_uuid, value in entity_dict.items():
            for i, process_uuid in enumerate(value.get('external_links_by_entity', {}).get('process', [])):
                if process_uuid in global_uuid_mapping['processes']:
                    continue


                print(f"Creating process with uuid {process_uuid}")
                base_process["process_core"]["process_id"] = value['links_by_entity']['process'][i]
                process = ingest_api.create_process(submission_url, base_process)
                global_uuid_mapping['processes'][process_uuid] = process['uuid']['uuid']


def create_rest_entities(spreadsheet_json, ingest_api, submission):
    submission_url = ingest_api.get_link_from_resource(submission, 'self')
    spreadsheet_json = {'protocol': spreadsheet_json['protocol'],
                        'biomaterial': spreadsheet_json['biomaterial'],
                        'file': spreadsheet_json['file']}
    for entity_type, entity_dict in spreadsheet_json.items():
        if entity_type == 'project':
            continue
        for entity_uuid, value in entity_dict.items():
            print(f'Creating {entity_type} {entity_uuid}')
            api_function_to_call = eval(f"ingest_api.create_{entity_type}")
            kwargs = {
                'submission_url': submission_url,
                'content': value.get('content', {})
            }
            if entity_type == 'file':
                kwargs.update({'filename': value.get('content', {}).get('file_core', {}).get('file_name', '')})
            entity = api_function_to_call(**kwargs)
            global_uuid_mapping[entity_type][entity_uuid] = entity['uuid']['uuid']

            for i, process_uuid in enumerate(value.get('external_links_by_entity', {}).get('process', [])):
                process = ingest_api.get_entity_by_uuid('processes', global_uuid_mapping['processes'][process_uuid])
                to_link = ingest_api.get_link_from_resource(process, 'protocols')

                # Linking protocols
                for prot_uuid in value.get('external_links_by_entity', {}).get('protocol', []):
                    protocol = ingest_api.get_entity_by_uuid('protocols', global_uuid_mapping['protocol'][prot_uuid])
                    from_link = ingest_api.get_link_from_resource(protocol, 'self')
                    link_entities(to_link, from_link, ingest_api)

                # Linking derived biomaterials
                to_link = ingest_api.get_link_from_resource(entity, 'derivedByProcesses')
                from_link = ingest_api.get_link_from_resource(process, 'self')
                link_entities(to_link, from_link, ingest_api)

                # Linking input biomaterials
                input_biomaterial = ingest_api.get_entity_by_uuid('biomaterials', global_uuid_mapping['biomaterial'][value['external_links_by_entity']['biomaterial'][i]])
                to_link = ingest_api.get_link_from_resource(input_biomaterial, 'inputToProcesses')
                link_entities(to_link,from_link, ingest_api)


def save_global_mapping():
    with open('uuid_mapping.json', 'w') as f:
        json.dump(global_uuid_mapping, f, indent=4, separators=(', ', ': '))

def main(project_uuid, token, spreadsheet_path):
    ingest_api = IngestApi()
    ingest_api.set_token(token)

    submission = create_submission_link_project(project_uuid, ingest_api)  # Step 1
    spreadsheet_json = load_spreadsheet_json(spreadsheet_path, ingest_api)  # Step 2
    create_non_linked_processes(spreadsheet_json, ingest_api, submission)  # Step 3
    create_rest_entities(spreadsheet_json, ingest_api, submission)  # Step 4
    save_global_mapping()


if __name__ == '__main__':
    project_uuid = os.getenv('PROJECT_UUID')
    token = os.getenv('INGEST_TOKEN')
    spreadsheet_path = os.getenv('SPREADSHEET_PATH')
    if all([project_uuid, token, spreadsheet_path]):
        main(project_uuid, token, spreadsheet_path)
    else:
        print("Please set up the environment variables for 'project_uuid', 'ingest_token' and 'spreadsheet_path'")
