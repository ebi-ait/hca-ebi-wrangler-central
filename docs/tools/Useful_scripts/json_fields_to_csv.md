---
layout: default
title: Converting JSON schema properties to csv
parent: Useful scripts
grand_parent: Tools
---
# Converting JSON schema properties to csv: json_fields_to_csv.py

TODO: Check if this is still useful and what it does

## Pre-requisites and installation

- python3
- python packages: json, argparse, os, logging

## Usage

This script converts all properties in the JSON schema files into csv format. A file path to the metadata repo needs to be provided. For guidance on how to use the tool, run the script with `--help`:

```
$ python3 json_fields_to_csv.py --path_to_schemas ../../metadata-schema/json_schema

```
