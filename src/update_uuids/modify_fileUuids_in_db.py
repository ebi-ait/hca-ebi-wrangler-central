import json
import pymongo
import requests as rq
import sys
import uuid


def find_file_ids(project_uuid):
    uuid_to_fileuuid = {}
    azul_url = "https://service.azul.data.humancellatlas.org/index/files"
    params = {"catalog": "dcp29",
              "filters": json.dumps({
                                    "projectId": {'is': [project_uuid]}
                                    }),
              "size": 20}
    page = rq.get(azul_url, params=params).json()
    for hit in page['hits']:
        uuid_to_fileuuid[hit['entryId']] = hit['files'][0]['uuid']
    while page.get('pagination', {}).get('next'):
        page = rq.get(page['pagination']['next']).json()
        for hit in page['hits']:
            uuid_to_fileuuid[hit['entryId']] = hit['files'][0]['uuid']
    return uuid_to_fileuuid


def load_map_files(map_json_path):
    with open(map_json_path, 'r') as f:
        map_json = json.load(f)

    return map_json['file']

def set_fileuuid(collection, document_uuid, file_uuid):
    entity = collection.update_one({'uuid': {'uuid': uuid.UUID(document_uuid)}}, update={'$set': {'dataFileUuid': uuid.UUID(file_uuid)}})


def main(project_uuid='577c946d-6de5-4b55-a854-cd3fde40bff2', mongodb_uri = 'mongodb://localhost:27017/admin', map_json_path='uuid_mapping.json'):
    reverse_map = load_map_files(map_json_path)
    uuid_to_fileuuid = find_file_ids(project_uuid)
    final_map = {u: value for u, value in uuid_to_fileuuid.items() if u in reverse_map}
    db = pymongo.mongo_client.MongoClient(mongodb_uri, uuidRepresentation='javaLegacy') # we should really document this, it was a nightmare
    collection = db['admin']['file']
    for uuid, fileUuid in final_map.items():
        print(f'Changing datafileUUID for document with uuid {uuid} to {fileUuid}')
        set_fileuuid(collection, uuid, fileUuid)
    db.close()


if __name__ == '__main__':
    main(sys.argv[1])