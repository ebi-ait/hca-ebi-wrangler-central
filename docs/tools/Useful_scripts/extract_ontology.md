---
layout: default
title: Extract all text to ontology mappings
parent: Useful scripts
grand_parent: Tools
---
# Extract all text to ontology mappings from one or more submissions in ingest

## Pre-requisites and installation

- python 3
- pip
- python requests module (install via `pip install requests` - only needed once!)

## Reasoning
Extracts all ontology text and the applied ontology for all entities of project(s) and produces a tsv output in the following format:
| STUDY | BIOENTITY | PROPERTY_TYPE | PROPERTY_VALUE | SEMANTIC_TAG | 
| - | - | - | - | - |
| StudyLabel | project | project_role | Principal Investigator | http://www.ebi.ac.uk/efo/EFO_0009736 | 
| StudyLabel | donor_organism | diseases | normal | http://purl.obolibrary.org/obo/PATO_0000461 |

This can be used to investigate mappings that have been done and also different mappings across projects that might be useful to standardise.

## Usage

Run the script in the command line using

```
python3 ontology_mappings_extractor.py -p <project-uuid(s)> -t <ingest-token>
```

Once the output file has been generated, remove duplicate entries from the file by running

```
sort all_mappings.txt | uniq > all_mappings_unique.txt
```
