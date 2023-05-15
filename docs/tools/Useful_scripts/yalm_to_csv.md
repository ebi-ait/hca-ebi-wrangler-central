---
layout: default
title: Converting yaml to csv
parent: Useful scripts
grand_parent: Tools
---

# Converting yaml to csv: generic_yaml2csv.py

## Pre-requisites and installation

- python3
- python packages: yaml, argparse, csv, sys, pandas

## Usage

This script converts any yaml file into csv format. The default file to convert is the potential_datasets.yaml file, but any file path can be provided. For guidance on how to use the tool, run the script with `--help`:

```
$ python3 generic_yaml2csv.py --help
usage: generic_yaml2csv.py [-h] [--yaml_file YAML_FILE] [--csv_file CSV_FILE]

Throw away script potential_datasets.yaml to csv

optional arguments:
  -h, --help            show this help message and exit
  --yaml_file YAML_FILE, -i YAML_FILE
                        yaml file name
  --csv_file CSV_FILE, -o CSV_FILE
                        csv output file name
```
