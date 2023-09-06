import os

import pymongo
import uuid
import json

def load_and_reverse_map(map_json_path):
    with open(map_json_path, 'r') as f:
        map_json = json.load(f)

    reverse_map = {}
    for entity_type, value in map_json.items():
        new_type = entity_type
        if entity_type == 'processes':
            new_type = 'protocol'
        if entity_type == 'submissionEnvelopes':
            new_type = 'submissionEnvelope'
        if new_type not in reverse_map:
            reverse_map[new_type] = {}
        for new_uuid, old_uuid in value.items():
            reverse_map[new_type][old_uuid] = new_uuid
    return reverse_map


def replace_uuids(collection, old_uuid, new_uuid):
    entity = collection.update_one({'uuid': {'uuid': uuid.UUID(old_uuid)}}, update={'$set': {'uuid': {'uuid': uuid.UUID(new_uuid)}}})


def main(mongodb_uri, map_json_path):
    reverse_map = load_and_reverse_map(map_json_path)
    db = pymongo.mongo_client.MongoClient(mongodb_uri, uuidRepresentation='javaLegacy') # we should really document this, it was a nightmare
    admin = db['admin']

    for collection_type, values in reverse_map.items():
        collection = admin[collection_type]
        for old_uuid, new_uuid in values.items():
            print(f'Changing {old_uuid} to {new_uuid}')
            replace_uuids(collection, old_uuid, new_uuid)
    db.close()


if __name__ == '__main__':
    mongodb_uri = os.getenv('MONGODB_URI') or 'mongodb://localhost:27017/'
    map_json_path = os.getenv('MAP_JSON_PATH') or 'uuid_mapping.json'
    main(mongodb_uri, map_json_path)
