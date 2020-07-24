---
layout: default
title: GEO to HCA Guide
parent: SOPs
nav_exclude: false
---

# GEO to HCA Guide


## Pre-requirements
1. Clone the [Geo to HCA Repo](https://github.com/ebi-ait/geo_to_hca) to your computer
   ```
   git clone https://github.com/ebi-ait/geo_to_hca.git
   ```
1. Go to the root folder and install the requirements
   ```
   cd geo_to_hca
   pip install -r requirements.txt --upgrade
   ```
   Please note that you might need to install with `pip3` instead of `pip` depending on your configuration

## Brief description
This tool was written to assist in the automatic conversion of geo metadata to abide to the HCA metadata standard.

## Usage

The script is stored under the `apps` folder, under the name `geo_to_hca.py`. It takes as input a single GEO accession or a space-delimited list of GEO accessions and a template HCA metadata excel spreadsheet (Included in the repository under the `docs` folder). It returns a pre-filled HCA metadata spreadsheet for each accession given. Each spreadsheet can then be used as an intermediate file for completion by manual curation. Optionally an output log file can also be generated which lists the availability of an SRA study accession and fastq file names for each GEO accession given as input.


```
usage: geo_to_hca.py [-h] [--accession ACCESSION]
                     [--accession_list ACCESSION_LIST]
                     [--input_file INPUT_FILE] [--template TEMPLATE]
                     [--header_row HEADER_ROW] [--input_row1 INPUT_ROW1]
                     [--output_dir OUTPUT_DIR] [--output_log OUTPUT_LOG]
```

### How-to guide
1. Go to the root of the repository and run the script with the accession wanted
    ```
    cd geo_to_hca
    python3 apps/geo_to_hca.py --accession <GEO_accession>
    ```
   While running, it will input a log. Please refer to the [most common warnings](#warnings) section if you don't know what they mean.
   
1. If it can't find the article information in the GEO metadata, it will perform a quick search in europePMC. Just state "y" or "n" when prompted.
1. It will output a small log like this:
```
          All fastq files are available SRA Study available
GSE149689                            no                 yes
```
1. Once it's done, the spreadsheet will be saved under the folder `spreadsheets/` with the name: `<geo_accession>.xlsx`. Another folder can be specified with the `--output_dir` argument.

## Arguments

### Required
1 of the following 3 arguments is required:
1. `--accession`: A string that matches a GSE series accession
1. `--accession_list`: A space-delimited list of accessions
1. `--input_file`: A path (relative or absolute) to a file containing geo accessions. The file should include an "accession" header and have one accession per row.

Please note that if more than one required argument is given, the script will exit.

### Optional

These arguments do not need to be specified.

1. `--template, default="docs/hca_template.xlsx"`

    The default template is an empty HCA metadata spreadsheet in excel format, with the relevant HCA metdata headers in rows 1-5. The default header row with programmatic names is row 4; the default start input row is row 6.
    It is not necessary to specify this argument unless the HCA spreadsheet format changes.

1. `--header_row, type=int, default=4`

    The default header row with programmatic names is row 4. It is not necessary to specify this argument unless the HCA spreadsheet format changes.

1. `--input_row, type=int, default=6`

    The default start input row (The row where it will start writing the output of the script) is row 6.
    It is not necessary to specify this argument unless the HCA spreadsheet format changes.

1. `--output_dir, default="spreadsheets/"`

    An output directory can be specified by it's path. If the path does not already exist, it will be created. If this argument
is not given, the default output directory is "spreadsheets/'"

1. `--output_log, type=bool, default=True`

    An optional arugment to retrieve an output log file stating whether an SRA study id and fastq file names were available for each GEO accession given as input.

## Use cases
1. Get the HCA metadata for 1 GEO accession
    ```
    python apps/geo_to_hca.py --accession GSE97168
    ```
1. Get the HCA metadata for a comma-separated list of GEO accessions
    ```
    python apps/geo_to_hca.py --accession_list GSE97168,GSE124872,GSE126030
    ```
1. Get the HCA metadata for all the accessions listed in a file. The file should have a header `accessions` and contain 1 accession per row. An example can be found in `docs/example_accessions.txt`
    ```
    python apps/geo_to_hca.py --input_file docs/example_accessions.txt
    ```

## Known issues and how to fix them
### Warnings
```
No fastq file name for Run accession: <Run_accession>
```
This means that for the run selected, there was at least 1 fastq for which its filename could not be found. This could be due to either:
1. The run does not have this information
1. The script assumes there are 3 files (R1,R2,I1) but there are only 2 files (R1 and R2)


### Errors
>When running the script, I get a weird xml.Etree error. All my inputs are valid so I don't understand what is happening

Please make sure you are using the option --upgrade when installing the repo requirements. There is a bug in openpyxl 3.0.2+ where this happens quite often. Reverting back to 3.0.1 should fix this error.

>I have an error not addressed here. What should I do?

Please issue a ticket in the [issues section](https://github.com/ebi-ait/geo_to_hca/issues) of the geo_to_hca repository.
