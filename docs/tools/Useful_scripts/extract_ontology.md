---
layout: default
title: Extract all text to ontology mappings
parent: Useful scripts
grand_parent: Tools
---
# Extract all text to ontology mappings from one or more submissions in ingest

TODO: Check if this will work for current ingest or how to modify to make it work

## Pre-requisites and installation

- python 3
- pip
- python requests module (install via `pip install requests` - only needed once!)

## Usage

Edit the script by putting the submission envelope IDs for the submissions you want to extract mappings from into the empty array at the very bottom of the script:

```
# -----> PUT YOUR ENVELOPE IDs IN HERE <---------
    envelope_ids = []
```

If you don't want the output file to have the default file name, you can also edit this.

Run the script in the command line using

```
python3 ontology_mappings_extractor.py
```

Once the output file has been generated, remove duplicate entries from the file by running

```
sort all_mappings.txt | uniq > all_mappings_unique.txt
```
