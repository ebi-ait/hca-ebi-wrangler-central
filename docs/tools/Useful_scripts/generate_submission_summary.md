---
layout: default
title: Generate submission summary report
parent: Useful scripts
grand_parent: Tools
---
# Generating submission summary report: generate_summary.py

TODO: see if this is still useful to wranglers

This tool generates two summary metadata reports for a submission/project. The first report counts the number specific entities in the submission/project. Currently, the entities counted is hard-coded and not complete. The second report contains a summary of other useful metadata pieces that can be used to populate projects pages. It is also not complete.

## Pre-requisites and installation

- python3
- git
- requirements of the repo

To install the tool, clone the [ingest-broker repository](https://github.com/ebi-ait/ingest-broker).

## Usage

Move to the ingest broker directory.

```
cd ingest-broker
```

Install the requirements of the package or run in docker (instructions for how to do this in the main README)

```
pip install -r requirements.txt

```

Check out the usage of `generate_summary.py` by using `--help`:

```
mfreeberg$ python generate_summary.py --help
usage: generate_summary.py [-h] H T U O

Process some integers.

positional arguments:
  H           the url of the ingest API (e.g
              http://api.ingest.dev.data.humancellatlas.org)
  T           the type of summary (project or submission)
  U           the uuid of the project/submission
  O           summary output format

optional arguments:
  -h, --help  show this help message and exit
```

Run the `generate_summary.py` script supplying the ingest API url, the type of summary (project or submission), the (project or submission envelope, respectively) UUID, and the desired output format (json or tsv). If you choose json, the report will be printed to the screen. If you choose tsv, the report be written to `report.tsv`.

```
mfreeberg$ python3 generate_summary.py http://api.ingest.dev.data.humancellatlas.org project 763e071c-34ed-4db5-9006-8929ccdf5b26 tsv
mfreeberg$ cat report.tsv
entity	count
dissociation_protocol	1
enrichment_protocol	1
library_preparation_protocol	1
sequencing_protocol	1
process	5096
donor_organism	8
specimen_from_organism	8
cell_suspension	2544
sequence_file	5088

```

Also generated is a file `scrape.tsv` which contains a bit more key pieces of metadata that can be useful to fill out project pages.

```
mfreeberg$ cat scrape.tsv
cell_type	['pancreatic A cell', 'acinar cell', 'type B pancreatic cell', 'pancreatic D cell', 'pancreatic ductal cell', 'mesenchymal cell']
num_total_estimated_cells	2544
organ	['pancreas', 'islet of Langerhans']
organoid_organ_model	[]
genus_species	['Homo sapiens']
num_donors	8
num_specimens	8
num_cell lines	0
num_organoids	0
num_cell suspension	2544
library_construction_approach	['Smart-seq2']
num_fastqs	5088
project_title	['Single cell transcriptome analysis of human pancreas reveals transcriptional signatures of aging and somatic mutation patterns.']
contact_names/emails	['Martin, Enge', 'Laura,,Huerta', 'Matthew,,Green', 'martin.enge@gmail.com', 'lauhuema@ebi.ac.uk', 'hewgreen@ebi.ac.uk']
```

If you would like additional metadata reported by this tool, please make a request via a GitHub issue in the ingest-central repository.
