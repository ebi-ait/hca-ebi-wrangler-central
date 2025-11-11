---
layout: default
title: Wrangling best practices
parent: Metadata spreadsheet
grand_parent: SOPs
nav_order: 2
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# Guidelines
{: .no_toc .text-delta }

## Table of contents

{: .no_toc .text-delta }

1. TOC {:toc}

## Purpose of the document
As wranglers come and go, we have generated over the years a set of best practices to be maintained for the sake of the FAIRness of our data.

As such, this document should be an updated **living document** containing the best practices, historical and new, that arise from wrangling datasets.

## General Best Practices

* <span style="color:red">**VERY IMPORTANT**</span>: Do not use “\|\|” in the project spreadsheet apart from when used for linking entities. It should not end up in the metadata of any of the entities.
* **Always** have someone review your dataset before submission
* Look for examples to model after if it’s a cell line dataset or one with a unique experimental design
* Use the [assay cheat sheet](https://docs.google.com/spreadsheets/d/1H9i1BK-VOXtMgGVv8LJZZZ9rbTG4XCQTBRxErdqMvWk/edit#gid=0) for existing, standard assays so that we stay consistent across Lattice and EBI wrangling teams



## Project

### General

* Fill the following from the main project page **in ingest UI**:
    * Cell count
    * Technology
    * Species
    * Organ
    * Accessions
    * Estimated cell count
* Fill out the admin area, this helps other people when using ingest as a backoffice
* Project shortname → should be more descriptive than IDs (_For example: CoolOrganProject or RandomTissueTechnologyAuthor._)


### Project - Contributors

* Don’t forget to add yourself as a contributor!
    * _EBI-Specific:_ Your institution is `EMBL-EBI`
    * Your role should be `data curator` (This ensures that you appear as a data curator in the browser)
* Try to add the email address for the corresponding contributor(s) (Usually available). This will help the scientists trying to re-use the data contact the authors or someone that can point them in the right direction

### Project - Funders

* If the ID of the grant is unknown, use the term `unspecified`, lowercase. This helps maintain consistency.
* Seed Network funded datasets should be wrangled by the lattice team; when in doubt, please contact them.

## Biomaterials

### All biomaterials

* Use a human-readable and nice description/name when possible
* Use the term `normal` for disease if the donor does not have any disease stated (as opposed to leaving it blank) 
* <span style="color:red">When assessing the ID of the biomaterials</span>:
  * If the contributor listed an ID that looks like a patient number, remove it and give unique ID
  * Scan for information that may have been accidentally shared with us and could jeopardise patient privacy

### Donor organism

* Fetal samples are their own donors
* If it is a fetal donor gestational age should be filled instead of organism age
* Use HSAPDV for human-specific development stages. Avoid using over-specific ontologies for non-fetal donors, as we have the "age" field for that, favouring ontologies such as “child stage” or “human adult stage”.
  * Use EFO for humans only when<span style="color:red"> age is not publicly available for GDPR-affected donors</span> (Living individuals)
* If an open access DCA has been signed, you should validate the metadata that the authors provide and **you shouldn’t ask for extra metadata to the authors**. 
* Donor organism name can match the description
* If the dataset is curated from publicly available sources, chances are the donor **organism does not have an accession.** Sample accessions are usually generated automatically by ENA/SRA when archiving, and usually scientists take samples as the input to the sequencing processes.
* Genus species is required even though it's not schema required
* Donors of organs that were given to them via transplant are still the primary donors, the transplant part could be captured in the donor description:
  * “56YO Latin female with a heart transplant”
  * Example dataset: [KidneybiopsyscRNA-seq](https://contribute.data.humancellatlas.org/projects/detail?uuid=027c51c6-0719-469f-a7f5-640fe57cbece)
* In **xenograft** experiments:
  * The donor is the one that the sample comes from, not the one that the sample is grafted inside. Think of the grafted individual as a "glorified petri dish"
  * Xenograft would be mentioned in the cell suspension section, under growth environment or free text description
  * Example dataset: [transplantedHumanIsletsNuclei](https://contribute.data.humancellatlas.org/projects/detail?uuid=a991ef15-4d4a-4b80-a93e-c538b4b54127)

__Wrangler note__: field `specimen_from_organism.transplant_organ` is for the case where a specimen had been extracted for transplant but ultimately was not transplanted to a recipient

### Specimen from organism

* For the organ, be as general as possible; for the organ part, be as specific as possible. When we integrate ontology expansion, this information can help create a very detailed map of the organ sampled.
* Disease here is almost more important than the donor level disease. Make sure to include information.
    * Donor could have HepC, but the specimen they donate is still `normal`
* Some specimens are better listed as systems, instead of organs
    * Some datasets in the dcp label organ = bone marrow and others use organ=hematopoietic system/organ_part = bone marrow

### Cell Suspension

* For SS2 datasets, set the `estimated cell count` to 1 for each cell suspension
    * Well and plate number are nice to have for QC purposes
* The input biomaterial can be any of the following depending on the experiment:
    * Specimen (single cell/nuclei OR bulk)
    * Cell line
    * Organoid
    * Cell suspension
    
### Organoids

* Some are made via differentiation protocols, others are made by growing multipotent cells together which signal differentiation without an applied protocol
    * Example datasets
        * Differentiation included: [HumanCerebralOrganoidsFetalNeocortex](https://contribute.data.humancellatlas.org/projects/detail?uuid=d2111fac-3fc4-4f42-9b6d-32cd6a828267)
* Input biomaterial can be:
    * Specimen
    * Cell line
    
### Cell line

* Cell lines should always have information about the donor in the `Donor organism` tab.
    * Example dataset: [pyleSkeletalMuscle](https://contribute.data.humancellatlas.org/projects/detail?uuid=4037007b-0eff-4e6d-b7bd-8dd8eec80143)
* A cell line can make another cell line (also the input)
    * Example dataset: [iPSCderivedTenocyte](https://contribute.data.humancellatlas.org/projects/detail?uuid=78d7805b-fdc8-472b-8058-d92cf886f7a4)
* If the cell line was purchased, please use the name listed here: [Cellosaurus](https://web.expasy.org/cellosaurus). This helps with consistency within the database.
* Organ model - for embryonic and pluripotent stem cells this is not ideal, but you can list `embryo` or `whole body` 
* If it’s an embryonic cell line, the donor would be the female that donates the embryonic tissue.

### Imaging

* Visium Datasets are modelled with the following subgraphs:
    * Donor_organism → specimen_from_organism → imaged_specimen → …
    * Imaged_specimen → image_file
    * Imaged_specimen → sequence_file
    * Imaged_specimen → analysis_file
* It’s helpful to use the Visium Spatial Gene Expression ontology term as the library preparation protocol to generate the Visium fastq files
* FFPE vs Fresh-Frozen information can be stored in the `preservation method` term
* Add the `permeabilization time` to the imaging_preparation_protocol

## Files

### All files

* Always fill up the `file source`. This helps the downstream components to identify the CGMs.
  * <span style="color:red">Do not use DCP/2 Ingest</span>. That term is reserved for the spreadsheet generated by ingest.
* Always include ontologies for `content description`
  * If there is a zip file, unzip it or if not possible list multiple ontologies as an array

### Image File

* All image files **and** files related to analyzing, understanding, processing the image files should be in this tab
* This includes .csv files containing spatial barcodes, and files which link the annotations of the image file image coordinates
* The JSON files containing the spot diameter and scale factors for the image acquisition are important for the reusability of the data. These should be included, and the recommended ontology term for their content description is `EDAM:3546`: `Image metadata`.
* Obtain <span style="color:red">HIGH RESOLUTION</span> images if possible. Low resolution images are not useful for analysis.

### Sequence File

* Remember to always fill out the process IDs; one per run (Multiple FASTQs may be grouped together by this method).
  * If there are multiple sets (R1, R2, I1...) of FASTQs per run (e.g. technical replicas), please give each of them a different `lane index`.
* Library IDs, with the same information as above.
* Input biomaterial is <span style="color:red">**always**</span> a cell suspension or an imaged specimen.

### Analysis files

* [Analysis files content description cheat sheet](https://docs.google.com/spreadsheets/d/1X-lDkdykICWsCXEBYov4-FiwSdzR6czxN4uVk8RA9gg/edit?pli=1#gid=0) should contain the needed values for the content description field. Open for discussion!
    * There’s also some discussion [here](https://docs.google.com/document/d/1YlQf7iVcm16tP3JWBNQxQVZeOEbSk_MTniql-rMjJE8/edit?pli=1#)
* Inputs to analysis_files should always be cell_suspensions rather than sequence_files. Reasons for this modelling decision:
    * Tricky to model file &rarr; file relationships.
    * Fewer linkings for cell_suspension to analysis_file, as generally there are many sequence_files generated from one cell_suspension.
* Differential gene expression files can be included in the dcp if the following information is known:
    * Required: The groups compared can be clearly identified. This information should be included in the description field
    * Optional but very appreciated:
        * Software
        * Covariates

      This information should be included in the analysis protocol. The ontology term for this protocol should be [analysis of matrices](https://ontology.archive.data.humancellatlas.org/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0030024) (EFO:0030024)

## Protocols

### Dissociation

* No dissociation protocol for blood and other fluids
* Dissociation is applied to a solid specimen that need to be broken down into smaller pieces before split into cell suspensions.

## Enrichment

* Not ideal, but you can use this schema to capture nuclei isolation from cells for snRNA-seq

## Differentiation

* Applicable to cell lines or organoids
* Example: H1 cell line was differentiated into a cardiomyocyte cell line which was then dissociated and processed into a cell suspension
    * Input biomaterial for H1 cell line would be an embryo specimen
    * Input biomaterial for cardiomyocyte would be a H1 cell line
    * Input biomaterial for cell suspension would be a cardiomyocyte cell line
    
## IPSC induction

* Applied only to a cell line

## Library Prep

* Source of truth for existing assays: [https://docs.google.com/spreadsheets/d/1H9i1BK-VOXtMgGVv8LJZZZ9rbTG4XCQTBRxErdqMvWk/edit#gid=0](https://docs.google.com/spreadsheets/d/1H9i1BK-VOXtMgGVv8LJZZZ9rbTG4XCQTBRxErdqMvWk/edit#gid=0)
    * Modified versions of assays need to be double checked

| Field | [Ontology](https://www.ebi.ac.uk/ols/ontologies) |
| ----- | -------- |
| species | [NCBITaxon](https://www.ebi.ac.uk/ols/ontologies/NCBITaxon) |
| ethnicity | [HANCESTRO](https://www.ebi.ac.uk/ols/ontologies/HANCESTRO) |
| developmental stage | [HsapDv (for human)](https://www.ebi.ac.uk/ols/ontologies/HSAPDV) ; [EFO (for mouse)](https://www.ebi.ac.uk/ols/ontologies/EFO) |
| disease | [MONDO](https://www.ebi.ac.uk/ols/ontologies/MONDO) ; [normal (from PATO)](https://www.ebi.ac.uk/ols4/ontologies/pato/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPATO_0000461) |
| units of measurement | [UO](https://www.ebi.ac.uk/ols/ontologies/UO) |
| enrichment method | [EFO](https://www.ebi.ac.uk/ols/ontologies/EFO) |
| dissociation method | [EFO](https://www.ebi.ac.uk/ols/ontologies/EFO) |
| collection method | [EFO](https://www.ebi.ac.uk/ols/ontologies/EFO) |
| library preparation method | [EFO](https://www.ebi.ac.uk/ols/ontologies/EFO) |
| sequencing approach | [EFO](https://www.ebi.ac.uk/ols/ontologies/EFO) |
| organ & organ_part | [UBERON](https://www.ebi.ac.uk/ols/ontologies/UBERON) |
| cell type | [CL](https://www.ebi.ac.uk/ols/ontologies/CL) |
| biological macromolecule | [OBI](https://www.ebi.ac.uk/ols/ontologies/OBI); [CHEBI](https://www.ebi.ac.uk/ols/ontologies/CHEBI) |
| library pre/amplification | [OBI](https://www.ebi.ac.uk/ols/ontologies/OBI); [EFO](https://www.ebi.ac.uk/ols/ontologies/EFO)|
| sequencing instrument | [EFO](https://www.ebi.ac.uk/ols/ontologies/EFO) |
| file content description | [EDAM](https://www.ebi.ac.uk/ols/ontologies/EDAM) |
| project role | [EFO](https://www.ebi.ac.uk/ols/ontologies/EFO) |
| mouse strain | [EFO](https://www.ebi.ac.uk/ols/ontologies/EFO) |
| cell cycle | [GO](https://www.ebi.ac.uk/ols/ontologies/GO) |

