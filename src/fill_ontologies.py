#!/usr/bin/env python3

"""
Requirements

hca-ingest==0.6.11
xlrd>=1.0.0
pandas
openpyxl

Instructions of use and main algorithm

1. Algorithm

    a. Load the workbook with openpyxl tools. Name will be the arg passed as argv[1]
    b. Load a SchemaTemplate object (Takes a while, but necessary)
    c. Parse each cell of the workbook below row 5
    d. When an ontology property is found (Row 4.endswith("text"), load the schema from the full qualified key to apply
    DB restrictions
    e. Query the OLS/HCAO with database restrictions
    f. Return ontologies that match the search and ask the user which one is correct.
    g. Save spreadsheet with the same name + _ontologies

1. Instruction of use

    **Install requirements** first (See above)

    ```
    cd src/
    python3 fill_ontologies.py -s <path_to_spreadsheet>
    ```
    The script takes some time to get started (It's loading a SchemaTemplate object). After approx 30 secs/1 min, it
    will begin the search, with the following possible outputs:
    - `Found exact match for term 'x' (Ontology: 'y')`: The program has found an ontology that matches perfectly the
    spreadsheet value
    - `Ontology with label 'x' ('y') has been found (<spreadsheet text value>). Is this the term that you were looking
    for? [Y/n/m/multi]:
        - Input 'Y', 'y', 'yes', 'Yes', '': The tool will fill the spreadsheet with that ontology.
        - Input 'm': You'll be prompted to introduce the term that you want to look for
        - Input 'multi': You'll be prompted to introduce the terms, one by one, and then introduce break.
        - Any other input: Next term in the list of ontologies found for the term
    - No ontology was found for this term. Please input it manually: Input the term that you want to search. Can also
    type "none".
"""

import requests as rq
import argparse
import openpyxl
from ingest.template.schema_template import SchemaTemplate
from openpyxl.utils import get_column_letter
import pickle
import re
import os

def define_parser():
    parser = argparse.ArgumentParser(description="Parser for the arguments")
    parser.add_argument("--spreadsheet", "-s", action="store", dest="wb_path", type=str, help="Input spreadsheet name")
    parser.add_argument("--api", "-a", action="store", dest="api", type=str, default="ols", choices=["ols", "zooma"],
                        help="What api to use for searching, one of 'ols' or 'zooma'")
    return parser


def get_iri(classes, iri={}):
    for ontology_class in classes:
        ontology_name = ontology_class.split(":")[0]
        if ontology_name in iri:
            continue
        else:
            request = rq.get("https://www.ebi.ac.uk/ols/api/terms?id={}".format(ontology_class))
            response = request.json()
            iri[ontology_name] = "/".join(response["_embedded"]["terms"][0]["iri"].split("/")[:-1])
    return iri


def get_ontology_schemas(key, json_schemas):
    key = key.split(".")
    try:
        for schema in json_schemas:
            if "name" not in schema:
                continue
            elif key[0] == schema["name"]:
                key.pop(0)
                while len(key) > 1:
                    if schema["properties"][key[0]]["type"] == "array":
                        if isinstance(schema["properties"][key[0]]["items"], list):
                            response = rq.get(schema["properties"][key[0]]["items"][0]["$ref"])
                        else:
                            response = rq.get(schema["properties"][key[0]]["items"]["$ref"])
                    else:
                        response = rq.get(schema["properties"][key[0]]["$ref"])
                    schema = response.json()
                    key.pop(0)
                return schema
    except KeyError as e:
        print(e)
        print("Could not find key: {} in schemas. Try updating your pickle by deleting pickled_schemas.pkl".format(key))


def search_child_term(term, key, json_schemas, iri={}):
    search_schema = get_ontology_schemas(key, json_schemas)
    search_ontologies = search_schema["properties"]["ontology"]["graph_restriction"]["ontologies"]
    classes = search_schema["properties"]["ontology"]["graph_restriction"]["classes"]

    ontologies = ",".join([ontology.split(":")[1] for ontology in search_ontologies]).lower()
    ontology_response = []

    include_self = search_schema["properties"]["ontology"]["graph_restriction"]["include_self"]

    request_query = "https://ontology.archive.data.humancellatlas.org/api/search?q=" if "hcao" in ontologies else \
                    "http://www.ebi.ac.uk/ols/api/search?q="
    if include_self:
        for ontology_class in classes:
            request = rq.get("http://www.ebi.ac.uk/ols/api/terms?id={}".format(ontology_class))
            response = request.json()
            if response["_embedded"]["terms"][0]["label"] == term:
                return response["_embedded"]["terms"], iri

    iri = get_iri(classes, iri)
    iri_query = ",".join([iri[ontology_class.split(":")[0]] + "/" + ontology_class.replace(":", "_") for ontology_class in classes])
    request = request_query + "{}&ontology={}&allChildrenOf={}".format(term, ontologies, iri_query)
    response = rq.get(request).json()
    if response["response"]["numFound"] != 0:
        ontology_response.extend(response["response"]["docs"])
    else:
        term = input("Term '{}' was not found (Property = {}).\nPlease input it manually:".format(term, key))
        if "none" in term.lower():
            return [{"obo_id": "", "label": ""}], iri
        return search_child_term(term, key, json_schemas, iri)
    return ontology_response, iri


def search_zooma(term, key, json_schemas, multi_flag=False):
    if re.search("\|\|", term) and not multi_flag:
        print("Multiple terms detected for term: {} in field {}.".format(term, key))
        multi_ontology = []
        terms_to_search = term.split("||")
        for each_term in terms_to_search:
            multi_ontology.append(search_zooma(each_term, key, json_schemas, True))
        return multi_ontology
    search_schema = get_ontology_schemas(key, json_schemas)
    search_ontologies = search_schema["properties"]["ontology"]["graph_restriction"]["ontologies"]
    classes = search_schema["properties"]["ontology"]["graph_restriction"]["classes"]

    ontologies = ",".join([ontology.split(":")[1] for ontology in search_ontologies]).lower()

    include_self = search_schema["properties"]["ontology"]["graph_restriction"]["include_self"]
    query = "http://snarf.ebi.ac.uk:8580/spot/zooma/v2/api/services/annotate?filter=preferred:[hca]&ontologies:[{}]&propertyValue={}".format(ontologies, term)
    zooma_response = rq.get(query)
    if zooma_response:
        response_json = zooma_response.json()
        annotation_list = []
    else:
        print("No Zooma curations found, continuing to OLS search.")
        return None

    for annotation in response_json:
        if annotation['provenance']['evidence'] == 'ZOOMA_INFERRED_FROM_CURATED':
            ols_response = rq.get('http://www.ebi.ac.uk/ols/api/terms?iri={}'.format(annotation['semanticTags'][0]))
            zooma_annotation = {}
            try:
                ols_json = ols_response.json()
                zooma_annotation['label'] = ols_json['_embedded']['terms'][0]['label']
                zooma_annotation['obo_id'] = ols_json['_embedded']['terms'][0]['obo_id']
                zooma_annotation['confidence'] = annotation['confidence']
                zooma_annotation['source'] = annotation['derivedFrom']['provenance']['source']['name']
                annotation_list.append(zooma_annotation)
            except KeyError as e:
                print(e)
                print("Failed to retrieve information from zooma.")
                return None
    i = 1
    if len(annotation_list) > 0:
        for ann in annotation_list:
            if term.lower() == ann['label'].lower():
                print("Found exact match {} - {} for text input {}.".format(ann['obo_id'], ann['label'], term))
                return ann
            elif len(annotation_list) == 1 and ann['confidence'] == 'HIGH' and ann['source'] == 'HCA':
                print("Found HIGH confidence HCA single match, using {} - {} for text input {}.".format(ann['obo_id'],
                                                                                                        ann['label'],
                                                                                                        term))
                return ann
            if i == 1:
                print("\nFound the matches below using ZOOMA for text input '{}':\n".format(term))
            print("{}. {} - {} with confidence level: '{}' from source '{}'".format(str(i), ann['obo_id'],
                                                                                    ann['label'], ann['confidence'],
                                                                                    ann['source']))
            i += 1
        answer = input("\nPlease enter the number of the preferred term as an integer.\nIf no appropriate match enter 'n' to search the OLS\n")
        try:
            return annotation_list[int(answer)-1]
        except ValueError as e:
            "No appropriate annotation found, trying normal OLS search"
            return None
    else:
        return None


def select_term(ontologies_list, term, key, json_schemas, known_iri={}, multi_flag=False):
    if ontologies_list and ontologies_list[0]["label"].lower() == term.lower():
        print("Found exact match for term {} (Ontology: {})".format(term, ontologies_list[0]["obo_id"]))
        return ontologies_list[0], known_iri
    else:
        if not ontologies_list:
            term = input("No ontologies were found for the term (Cell value = {}, Key = {}). Please input it manually: "
                         .format(term, key))
            ontologies_list, known_iri = search_child_term(term, key, json_schemas, known_iri)
            return select_term(ontologies_list, term, key, json_schemas, known_iri)
        if re.search("\|\|", term) and not multi_flag:
            print("Multiple terms detected for term: {} in field {}.".format(term, key))
            multi_ontology = []
            terms_to_search = term.split("||")
            for each_term in terms_to_search:
                ontologies_list, known_iri = search_child_term(each_term, key, json_schemas, known_iri)
                # TODO: extend only ontologies, not known iri
                multi_ontology.extend(select_term(ontologies_list, each_term, key, json_schemas, known_iri, multi_flag=True))
            return multi_ontology, known_iri
        print("{} matches found for your search term '{}' for field {}.".format(len(ontologies_list), term, key))
        i = 1
        for ontology in ontologies_list:
            if "obo_id" not in ontology.keys():
                continue
            print("{}. {} - {}".format(i, ontology["label"], ontology["obo_id"]))
            i += 1
        answer = input("Enter the appropriate number or m for manual input\n".format(ontology["label"],ontology["obo_id"], term, key))
        if answer.lower() == "multi" and not multi_flag:
            multi_ontology = []
            terms_to_search = []
            n = 1
            while True:
                term = input(
                    "Please input term number {} or 'break' to indicate that there are no more terms: ".format(n))
                if "break" in term.lower():
                    break
                terms_to_search.append(term)
                n += 1
            for term in terms_to_search:
                ontologies_list, known_iri = search_child_term(term, key, json_schemas, known_iri)
                # TODO: extend only ontologies, not known iri
                multi_ontology.extend(select_term(ontologies_list, term, key, json_schemas, known_iri, multi_flag=True))
            return multi_ontology, known_iri
        elif answer.lower() == 'm':
            term = input("Please input the term manually: ")
            ontologies_list, known_iri = search_child_term(term, key, json_schemas, known_iri)
            return select_term(ontologies_list, term, key, json_schemas, known_iri)
        else:
            return ontologies_list[int(answer)-1], known_iri


def parse_wb(file_path, wb, schema, api):
    known_terms = []
    known_ontologies = {}
    # Really ugly nested fors to parse for each cell in the WorkBook
    for sheet in wb:
        for row in sheet.rows:
            # Don't check rows below number 5
            if list(row)[0].row < 5:
                continue
            for cell in row:
                # If "X"4 cell exists, ends with value text and there is a value in the current cell:
                if sheet["{}4".format(get_column_letter(cell.column))].value and sheet["{}4".format(get_column_letter(cell.column))].value.endswith(".text") and cell.value:
                    # If we already know the term, fill and skip to go faster
                    if cell.value in known_terms:
                        sheet["{}{}".format(get_column_letter(cell.column + 1), cell.row)].value = known_ontologies[cell.value]["obo_id"]
                        sheet["{}{}".format(get_column_letter(cell.column + 2), cell.row)].value = known_ontologies[cell.value]["label"]
                        continue
                    # Search for the ontologies that match the ontology restriction of their schema

                    if api == "zooma":
                        zooma_annotation = search_zooma(cell.value, sheet["{}4".format(get_column_letter(cell.column))].value, schema)
                        if zooma_annotation:
                            if isinstance(zooma_annotation, list):
                                ontologies = {}
                                ontologies["obo_id"] = "||".join(
                                    [ontology_element["obo_id"] for ontology_element in zooma_annotation if "obo_id" in ontology_element])
                                ontologies["label"] = "||".join(
                                    [ontology_label["label"] for ontology_label in zooma_annotation if"obo_id" in ontology_label])
                                zooma_annotation = ontologies
                            sheet["{}{}".format(get_column_letter(cell.column + 1), cell.row)].value = zooma_annotation["obo_id"]
                            sheet["{}{}".format(get_column_letter(cell.column + 2), cell.row)].value = zooma_annotation["label"]
                            known_terms.append(cell.value)
                            known_ontologies[cell.value] = zooma_annotation
                        else:
                            ontologies_list, known_iri = search_child_term(cell.value, sheet[
                                "{}4".format(get_column_letter(cell.column))].value, schema)
                            # Select the correct ontology from the list and write it to excel
                            if ontologies_list:
                                ontology, known_iri = select_term(ontologies_list, cell.value, sheet["{}4".format(get_column_letter(cell.column))].value, schema, known_iri)
                                known_terms.append(cell.value)
                                if isinstance(ontology, list):
                                    ontologies = {}
                                    ontologies["obo_id"] = "||".join([ontology_element["obo_id"] for ontology_element in ontology if "obo_id" in ontology_element])
                                    ontologies["label"] = "||".join([ontology_label["label"] for ontology_label in ontology if "obo_id" in ontology_label])
                                    ontology = ontologies
                            known_ontologies[cell.value] = ontology

                    sheet["{}{}".format(get_column_letter(cell.column + 1), cell.row)].value = \
                    known_ontologies[cell.value]["obo_id"]
                    sheet["{}{}".format(get_column_letter(cell.column + 2), cell.row)].value = \
                    known_ontologies[cell.value]["label"]
    split_path = os.path.split(file_path)
    wb_name = split_path[-1]
    wb_dir = split_path[0]
    output_name = "".join(wb_name.split(".")[:-1]) + "_ontologies.xlsx"
    wb.save(os.path.join(wb_dir, output_name))


def main(args):
    wb = openpyxl.load_workbook(args.wb_path)
    try:
        with open('pickled_schemas.pkl', 'rb') as input:
            json_schemas = pickle.load(input)
    except FileNotFoundError:
        schema = SchemaTemplate(ingest_api_url="http://api.ingest.staging.archive.data.humancellatlas.org")
        with open('pickled_schemas.pkl', 'wb') as output:
            pickle.dump(schema.json_schemas, output)
        json_schemas = schema.json_schemas
    parse_wb(args.wb_path, wb, json_schemas, args.api)


if __name__ == "__main__":
    parser = define_parser()
    args = parser.parse_args()
    main(args)
