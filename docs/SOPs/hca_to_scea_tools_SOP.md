---
layout: default
title: HCA to SCEA Guide
parent: SOPs
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

## Pre-requisites

### Python3
- Install from [Python's webpage](https://www.python.org/downloads/)

### HCA-to-SCEA-tools

1. Clone the repository
   ```
   git clone https://github.com/ebi-ait/hca-to-scea-tools.git
   cd hca-to-scea-tools/
   ```
1. Make sure you have installed [npm](https://www.npmjs.com/), [pip](https://pypi.org/project/pip/) and the pip package [virtualenv](https://virtualenv.pypa.io/en/latest/)

1. Install the application by running
   ```
   cd hca2scea-backend
   ./install.sh
   ```

## How-to

### Before proceeding with the submission to SCEA

Please make sure that the dataset is ready for SCEA. Check their [`data suitability guidelines`](https://github.com/ebi-gene-expression-group/expression-atlas-curation-guide/blob/master/pages/inclusion_criteria.md) document thoroughly. All datasets must be split by:
- Species
- Technology 
    - 10x: Only 3' accepted (Mixing chemistries is OK)
    
Currently this splitting operation has to be done by manually creating as many spreadsheets as technologies the project has. **Each spreadsheet will have a different accession number**.

Once the suitability has been assessed, please contact an SCEA curator via slack (#hca_to_scea chanel) and ask them to confirm the SCEA suitability/assess priority for this dataset in the [data tracking sheet](https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0)

### Running the converter

1. Run the tool
   ```
   cd hca-to-scea-tools
   npm start
   ```

1. Go to the following URI
   ```
   http://127.0.0.1:5000/
   ```

1. You should see a webpage which looks like the following:

   ![Base webpage](https://github.com/ebi-ait/hca-ebi-wrangler-central/raw/master/assets/images/scea_screenshots/base_web.png)

   2. Upload the spreadsheet file as indicated. Note that if your spreadsheet has multiple technologies that you will need to upload a separate spreadsheet per technology.

   2. Enter an accession id number in the ‘E-HCAD-” box. The E-HCAD accession series is specifically for HCA metadata which has been converted to SCEA standard. The next number should be chosen based on the latest dataset uploaded in [SCEA's gitlab](https://gitlab.ebi.ac.uk/ebi-gene-expression/scxa-metadata/-/tree/master/HCAD).

   2. Enter the curator’s initials (1 wrangler per box). There is an option to click the “-” button to remove the 2nd box. Default values are AD and JFG.

   2. Once you are happy with this, click on ‘process!’.

   2. A new step will appear: “Force a Project UUID”. You can either enter a uuid or click “Fill in project details manually”. **For now, always click `Fill in project details manually`**. This will ensure the correct information is added to the idf and sdrf files.


3. You should now see a webpage like the following:
    
   ![protocol matching](https://github.com/ebi-ait/hca-ebi-wrangler-central/raw/master/assets/images/scea_screenshots/protocol_matching.png)
   
   You can edit the text inside the protocol descriptions and merge the protocols into 1 by dropping and dragging. The idea is to keep duplication across protocols as minimal as possible. If there are no values in the protocol descriptions, they will be filled with `nan`. Please fill in a brief description.

4. You should also see the following on the same webpage:
   
   ![pre filled values](https://github.com/ebi-ait/hca-ebi-wrangler-central/raw/master/assets/images/scea_screenshots/pre_filled_values.png)
    
   These are pre-filled values for the sequencing protocol that is specified in the HCA metadata spreadsheet. Currently, if ‘10X v2 sequencing’ is specified, these fields are pre-filled. You can then manually edit them. If another technology is specified, these fields are not pre-filled and you need to enter the information here manually. SCEA requires that datasets are split by technology, so you should only have 1 technology type in your HCA metadata file.

5. Click `this looks alright`. An idf and sdrf file will be generated in a newly created folder inside the ‘spreadsheets’ folder in your local repository directory.

### Section B: Refining the metadata outputs

#### idf file

1. Any fields which need to be filled manually will be indicated in the file by <fill this>:

   Some are straight-forward:

    *   `Public Release Date`: when was the data publicly released? It needs to be in this format to pass validation: YYYY-MM-DD 
    *   `Comment[EAExpectedClusters]`: this can be left blank
    
    *   `Comment[HCALastUpdateDate]`: when was the HCA spreadsheet last updated?
    
    *   `Comment[SecondaryAccession]`: tab-separated list of secondary accesions: HCA uuid; other secondary accessions (e.g. GEO,AE) 

    Others need a bit more work:

    *   `Comment[EAAdditionalAttributes]`: which attributes in the sdrf file do you think would be useful attributes to display visually when a user hovers over the cell clusters? Please give a tab-separated list. Factor values are automatically displayed so do not include  these.
    
    *   `Comment[EAExperimentType]`: how would you describe the experiment: baseline or differential? An example of baseline would be sequencing kidney cells to map the normal kidney. An example of differential would be sequencing kidney cells to map the normal versus disease kidney.
    
    *   We will come back to `Experimental Factor Name` and `Experimental Factor Type` later in this document.

An example screenshot to illustrate the above points:

![refining fields](https://github.com/ebi-ait/hca-ebi-wrangler-central/raw/master/assets/images/scea_screenshots/refining_fields.png)

2. You can further edit the list of Protocol Name, Protocol Type and Protocol Description in the idf file if you need to:
*   Each Name, Type and Description must be tab-separated.
*   The Name should be ordered by number.
*   The Type and Description order must reflect the Name orderhttps://github.com/ebi-gene-expression-group/atlas-fastq-provider.
*   Protocol Types have to be 1 of: ‘sample collection protocol’,’treatment protocol’,’enrichment protocol’,’nucleic acid library construction protocol’,’nucleic acid sequencing protocol’.
*   SCEA dissociation protocols are labelled as “enrichment protocol”.
*   The Protocol Name is used in the sdrf file to detail which protocols are applied in which experiments. It is worth checking these are all correct in the sdrf.
*   If the experimental design consists of a treatment, a stimulus, or some other protocol which you believe is not reflected by HCA protocol names, you can add a new protocol Name, Type and Description in the idf file. You would need to then modify the number order of all protocol Names and the associated Type and Descriptions. The sdrf protocol REF fields would need to reflect these changes.


#### sdrf file

*   You will need to check that the number and name of the protocol REF ids in the idf file (e.g. P-HCADX-1,P-HCADX-2) matches correctly with the experiment rows in the sdrf files, based on the experimental design. The automatic conversion should be correct but this is a good check to do.
*   You will need to fill cells consisting of <FILL THIS> or if no relevant information is available, you can leave these blank.
*   Material Type is currently set to “whole organism” by default (hca-to-scea-tools script needs updating). Please change to “organism part” if the sample is an organ/tissue specimen or “cell” if the sample was an organoid or cell line culture.
*   The last columns in the sdrf file should be Factor Value fields. They are not automatically generated. It is good to add these where you can identify a factor which may be useful to the user to reflect potential differential groups. These should be selected from the `Characteristic` fields. For example, you might choose to add `Factor Value[organism part]` or `Factor Value[disease]` if they are variable. You can also add additional Characteristic fields such as `Characteristic[immunophenotype]` or `Characteristics[stimulus]`. These can then be used as a Factor Value field such as `Factor Value[stimulus]`.
*   Controlled vocabulary is applicable in certain sdrf fields: please see the shared documents from Silvie found here: [SCEA controlled vocabulary](https://drive.google.com/drive/folders/1GHaqpQsz4CY6_KkBTTXHJo69J4FXMNcw)
*   Make sure you save the sdrf file as a tab-delimited .txt file: beware of excel changing your time unit ranges to a date format and of empty rows/lines at the bottom of the file. Empty rows/lines will cause errors in validation.
*   Once this is all complete, go back to the idf file and fill these fields: ‘Experimental Factor Name’ and ‘Experimental Factor Type’ with a tab-separated list of the Factor values you had chosen to add in the sdrf file. See below screenshot as an example:


![sdrf refining](https://github.com/ebi-ait/hca-ebi-wrangler-central/raw/master/assets/images/scea_screenshots/sdrf_refining.png)



### Section C: Validation of idf and sdrf files**

_There are 2 validation steps for SCEA: a python validator and perl validator. In Silvie’s words: “the perl script checks the mage-tab format in general (plus some curation checks etc) and the the python script mainly checks for single-cell expression atlas specific fields and requirements”._

#### Python Validator

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

#### Perl validator

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

### Section D: SCEA file upload

#### SDRF and IDF upload

1.   Create a new branch in the Gitlab gene-expression-atlas HCAD repository directory: [https://gitlab.ebi.ac.uk/ebi-gene-expression/scxa-metadata/tree/master/HCAD](https://gitlab.ebi.ac.uk/ebi-gene-expression/scxa-metadata/tree/master/HCAD)
1.   Upload your validated SCEA files to this branch.
1.   Submit a merge request and select ‘requires approval’.
1.   Your SCEA files will then be reviewed for merging to the Master directory.

#### Sequence file handing

[WIP]

### Section E: Extra notes

#### Detailed column mapping

This table shows the source of the columns generated in the MAGE-TAB file.


| Column in MAGE-TAB SDRF file              | Source                   | Description                                                               | Default      |
|---|---|---|---|
| `Source Name`                              | Selectable from          | Any column ending with `biomaterial_id` or `biosamples_accession`         |              |
| `Characteristics[organism]`                | Column                   | `donor_organism.genus_species.ontology_label`                             |              |
| `Characteristics[individual]`              | Column                   | `donor_organism.biomaterial_core.biomaterial_id`                          |              |
| `Characteristics[sex]`                     | Column                   | `donor_organism.sex`                                                      |              |
| `Characteristics[age]`                     | Column                   | `donor_organism.organism_age`                                             |              |
| `Unit [time unit]`                         | Column                   | `donor_organism.organism_age_unit.text`                                   |              |
| `Characteristics[developmental stage]`     | Column                   | `donor_organism.development_stage.text`                                   |              |
| `Characteristics[organism part]`           | Column                   | `specimen_from_organism.organ.ontology_label`                             |              |
| `Characteristics[sampling site]`           | Column                   | `specimen_from_organism.organ_parts.ontology_label`                       |              |
| `Characteristics[cell type]`               | Column                   | `cell_suspension.selected_cell_types.ontology_label`                      |              |
| `Characteristics[disease]`                 | Column                   | `donor_organism.diseases.ontology_label`                                  |              |
| `Characteristics[organism status]`         | Column                   | `donor_organism.is_living`                                                |              |
| `Characteristics[cause of death]`          | Column                   | `donor_organism.death.cause_of_death`                                     |              |
| `Characteristics[clinical history]`        | Column                   | `donor_organism.medical_history.test_results`                             |              |
| `Description`                              | Column                   | `specimen_from_organism.biomaterial_core.biomaterial_description`         |              |
| `Material Type` (first instance)           | Fill cells with one of   | `whole organism`, `organism part`, `cell`                                 |              |
| `Protocol REF` (first group of instances)  | Special protocol columns | Includes collection/dissociation/enrichment/library prep protocols        |              |
| `Extract Name`                             | Selectable from          | Any column ending with `biomaterial_id` or `biosamples_accession`         |              |
| `Material Type` (second instance)          | Fill cells with value    | `RNA`                                                                     |              |
| `Comment[library construction]`            | Column                   | `library_preparation_protocol.library_construction_method.ontology_label` |              |
| `Comment[input molecule]`                  | Column                   | `library_preparation_protocol.input_nucleic_acid_molecule.ontology_label` |              |
| `Comment[primer]`                          | Fill cells with value    | `oligo-DT`                                                                |              |
| `Comment[end bias]`                        | Column                   | `library_preparation_protocol.end_bias`                                   |              |
| `Comment[umi barcode read]`                | Column or default        | `library_preparation_protocol.umi_barcode.barcode_read`                   | `read1`      |
| `Comment[umi barcode offset]`              | Column or default        | `library_preparation_protocol.umi_barcode.barcode_offset`                 | `16`         |
| `Comment[umi barcode size]`                | Column or default        | `library_preparation_protocol.umi_barcode.barcode_length`                 | `10`         |
| `Comment[cell barcode read]`               | Column or default        | `library_preparation_protocol.cell_barcode.barcode_read`                  | `read1`      |
| `Comment[cell barcode offset]`             | Column or default        | `library_preparation_protocol.cell_barcode.barcode_offset`                | `0`          |
| `Comment[cell barcode size]`               | Column or default        | `library_preparation_protocol.cell_barcode.barcode_length`                | `16`         |
| `Comment[sample barcode read]`             | Empty                    |                                                                           |              |
| `Comment[sample barcode offset]`           | Fill cells with value    | `0`                                                                       |              |
| `Comment[sample barcode size]`             | Fill cells with value    | `8`                                                                       |              |
| `Comment[single cell isolation]`           | Fill cells with value    | `magnetic affinity cell sorting`                                          |              |
| `Comment[cDNA read]`                       | Fill cells with value    | `read2`                                                                   |              |
| `Comment[cDNA read offset]`                | Fill cells with value    | `0`                                                                       |              |
| `Comment[cDNA read size]`                  | Fill cells with value    | `98`                                                                      |              |
| `Comment[LIBRARY_STRAND]`                  | Column                   | `library_preparation_protocol.strand`                                     |              |
| `Comment[LIBRARY_LAYOUT]`                 | Fill cells with value    | `PAIRED`                                                                  |              |
| `Comment[LIBRARY_SOURCE]`                 | Fill cells with value    | `TRANSCRIPTOMIC SINGLE CELL`                                              |              |
| `Comment[LIBRARY_STRATEGY]`               | Fill cells with value    | `RNA-Seq`                                                                 |              |
| `Comment[LIBRARY_SELECTION]`              | Fill cells with value    | `cDNA`                                                                    |              |
| `Protocol REF (second group of instances)`  | Special protocol columns | Includes sequencing protocol                                              |              |
| `Assay Name`                               | Column                   | `specimen_from_organism.biomaterial_core.biomaterial_id`                  |              |
| `Technology Type`                          | Fill cells with value    | `sequencing assay`                                                        |              |
| `Scan Name`                                | Selectable from          | Any column ending with `biomaterial_id` or `biosamples_accession`         |              |
| `Comment[RUN]`                             | Selectable from          | Any column ending with `biomaterial_id` or `biosamples_accession`         |              |
| `Comment[read1 file]`                      | Column                   | `sequence_file.file_core.file_name_read1`                                 |              |
| `Comment[read2 file]`                      | Column                   | `sequence_file.file_core.file_name_read2`                                 |              |
| `Comment[index1 file]`                     | Column                   | `sequence_file.file_core.file_name_index`                                 |              |