---
layout: default
title: HCA to SCEA Guide
parent: SOPs
last_modified_date: 23/12/2020
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# HCA to SCEA Guide
{: .no_toc }

_Please note: this is not a tool to generate a perfect set of SCEA idf and sdrf files automatically. It speeds up the process by part automation but manual curation is an important part of the process._

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Useful documents 

<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2020-10-07T14:41:24.371Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36\&quot; etag=\&quot;v8oPzvuX1tBEvZB6g7rV\&quot; version=\&quot;13.7.5\&quot; type=\&quot;google\&quot;&gt;&lt;diagram id=\&quot;FsEeLdDOj7soeLvYh2q5\&quot; name=\&quot;Page-1\&quot;&gt;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&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>

[Modify this diagram here](https://app.diagrams.net/?src=about#G1bP1jg52KXeVmd6HGmXxXRjfT2uEZtPDr)

## Before you begin

### Checking suitability for SCEA

Please refer to the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2) for information on dataset suitability for SCEA.

As part of this suitability criteria, there are also guidelines on how HCA datasets should be split into separate SCEA projects, if needed.

You can also check the SCEA team's [`data suitability guidelines`](https://github.com/ebi-gene-expression-group/expression-atlas-curation-guide/blob/master/pages/inclusion_criteria.md) document more thoroughly.

Once you think that the dataset is suitable or if you have any doubts, double-check with the SCEA team on the AIT slack channel `#hca-to-scea`

## Converting HCA spreadsheets to SCEA MAGE-TAB

Login to the wrangler EC2 and follow the guide to running the hca-to-scea tool in the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2)

_While not recommended, if you would like to install locally, see [Installing on your local machine](installing-on-your-local-machine)_

## Refining the metadata outputs

Please follow the guide to post-processing curation of the output MAGE-TAB files, an idf file and an sdrf file, in the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2)

## Incorporating cell type annotations

UNDER REVIEW
{: .label .label-yellow }

Information about the cell type annotations can usually be found in the paper's supplementary materials or by contacting the author directly. They can be in a variety of formats or embedded within matrix files.  

A detailed guide on how to curate ontologised cell types from the author provided cell types can be found here: [SCEA curating cell types guide](https://github.com/ebi-gene-expression-group/expression-atlas-curation-guide/blob/master/pages/inferred_cell_type.md)

### Incorporating into sdrf

For Smart-seq 2 experiments (where there is one cell per row of the sdrf), the cell types should be incorporated directly into the sdrf file.

For experiments where one row of the sdrf file is equivalent to one cell, the authors' cell type annotations should be incorporated into the sdrf file. The following columns need to be added to the sdrf file

| Column name                                                      | description                                                                         | how to make                                                                       |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Factor Value[inferred cell type - authors labels]                | Reformatted author provided text that is displayed as an option in the SCEA browser | Usually derived from authors supplementary files                                  |
| Factor Value Ontology Term[inferred cell type - authors labels]  | The uri for the assigned ontology term from authors labels ?                        | eg. `http://purl.obolibrary.org/obo/CL_0000084` Is this generated automatically?  |
| Factor Value[inferred cell type - ontology labels]               | The ontology label for the curated ontology term                                    | is this generated automatically? e.g. `macrophage`                                |
| Factor Value Ontology Term[inferred cell type - ontology labels] | The uri for the curated ontology term                                               | e.g. `http://purl.obolibrary.org/obo/CL_0000084` is this generated automatically? |
| Comment[submitted inferred cell type] | The exact cell type as submitted by the author | directly from supplemental materials. |


### cells.txt file

For droplet type experiments (where there >1 cells for a single row in the sdrf), a `cells.txt` file needs to be created to match author assigned cell types to the outputs generated by the SCEA.

The `cells.txt` file is not generated by the process above, it needs to be manually/semi automatically created by the wrangler. The format of the file is a tab-delimited text file saved as `E-HCAD-XX.cells.txt`. The following columns need to be included:

| Column name                          | description                                                                         | how to make                                                             |
|--------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| cell ID                              | A unique identifier for each cell in the experiment                                 | `Comment[RUN]-barcode`, e.g.`4834STDY7002875_S1_L001-AAAGCAATCCATGAGT`. If there are technical replicates run ID should be replaced with the value in the technical replicate group column    |
| Comment[RUN]                         | The run identifier, must match with the AssayName in the sdrf file                  | `Comment[RUN]`                                                          |
| barcode                              | The oligonucleotide identifier                                                      | Usually derived from authors supplementary files eg. `AAAGCAATCCATGAGT` |
| Comment[AUTHOR IDENTITY]             | The exact text that the author used to describe the cell type                       | Usually derived from authors supplementary files                        |
| inferred cell type - author labels   | Reformatted author provided text that is displayed as an option in the SCEA browser | Derived by formatting `Comment[AUTHOR IDENTITY]`                        |
| inferred cell type - ontology labels | The closest ontologised cell type that is available, needs to be found in EFO       | manually curated (?) Zooma (?)                                          |

[SCEA documentation about the cells.txt file](https://github.com/ebi-gene-expression-group/expression-atlas-curation-guide/blob/master/pages/single_cell_curation_guide.md#cell-level-metadata-for-droplet-based-experiments) (scroll to bottom of page)

## Section D: Validation of idf and sdrf files**

_There are 2 validation steps for SCEA: a python validator and perl validator. In Silvie’s words: “the perl script checks the mage-tab format in general (plus some curation checks etc) and the the python script mainly checks for single-cell expression atlas specific fields and requirements”._

### Python Validator

Please note: there is a ticket to get the validation tools installed on EC2. This should be available soon, as of 17/03/2021. For now, please install and run locally, following the instructions below.

A MAGE-TAB pre-validation module for running checks that guarantee the experiment can be processed for SCEA. You can clone the repository and run the script locally:

[Atlas metadata validator](https://github.com/ebi-gene-expression-group/atlas-metadata-validator)

To run, from the directory:
```
python atlas_validation.py path/to/test.idf.txt
```
<span style="text-decoration:underline;">Useful HCA-specific and single-cell specific command:</span>

```
python atlas_validation.py path/to/test.idf.txt -sc -hca -v
```

*   The SDRF file is expected in the same directory as the IDF file. If this is not the case, the location of the SDRF and other data files can be specified with -d PATH_TO_DATA option.
*   The script guesses the experiment type (sequencing, microarray or single-cell) from the MAGE-TAB. If this was unsuccessful the experiment type can be set by specifying the respective argument -seq, -ma or -sc.
*   The data file and URI checks may take a long time. Hence there is an option to skip these checks with -x.
*   Verbose logging can be activated with -v.
*   Special validation rules for HCA-imported experiments can be invoked with -hca option. The validator will otherwise guess if the experiment is an HCA import based on the HCAD accession code in the ExpressionAtlasAccession field.

An example of a successful validation looks like this:

![validation](https://github.com/ebi-ait/hca-ebi-wrangler-central/raw/master/assets/images/scea_screenshots/validation.png)

### Perl validator

1.   Install Anaconda if you don’t have it already and the Anaconda directory to your path
1.   Configure conda by typing the following at the terminal:
     ```
     conda config --add channels defaults
     conda config --add channels bioconda
     conda config --add channels conda-forge
     ```
1.   Install the perl atlas module in a new environment: 
     ```
     conda create -n perl-atlas-test -c ebi-gene-expression-group perl-atlas-modules
     ```
1.   Activate the environment:
     ```
     conda activate perl-atlas-test
     ```
1.   Download the validate_magetab.pl_ _perl script from here: [https://drive.google.com/drive/folders/1Ja2NKtHkDh2YIvUhNa1mpivL-UjCsmbR](https://drive.google.com/drive/folders/1Ja2NKtHkDh2YIvUhNa1mpivL-UjCsmbR))
1.   Execute the script (with idf and sdrf files in the same directory)
     ```
     perl path-to/validate_magetab.pl -i <idf-file>
     ```
     (You can ignore ArrayExpress errors)

## SCEA file upload

### SDRF and IDF upload (and cells.txt if present)

1.   Create a new branch in the Gitlab gene-expression-atlas HCAD repository directory: [https://gitlab.ebi.ac.uk/ebi-gene-expression/scxa-metadata/tree/master/HCAD](https://gitlab.ebi.ac.uk/ebi-gene-expression/scxa-metadata/tree/master/HCAD)
1.   Upload your validated SCEA files to this branch.
1.   Submit a merge request and select ‘requires approval’.
1.   Your SCEA files will then be reviewed for merging to the Master directory.

## Appendix

### Installing on your local machine

You will need python3 installed, if you don't have it, install from [Python's webpage](https://www.python.org/downloads/)

To install the tool on your local machine:

1. Clone the repository
   ```
   git clone https://github.com/ebi-ait/hca-to-scea-tools.git
   cd hca-to-scea-tools/

1. Install the application by running
   ```
   cd hca2scea-backend
   ./install.sh
   ```
Then once installed:

1. Run the tool: run the command-line tool with at least the minimum required arguments as described in the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2). The tool should be run locally just as it would on EC2.
