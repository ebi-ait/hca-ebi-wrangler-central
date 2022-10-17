---
layout: default
title: Wrangling best practices
parent: SOPs
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

* <span style="color:red">**VERY IMPORTANT**</span>: Do not use “||” in the project spreadsheet apart from when used for linking entities. It should not end up in the metadata of any of the entities.
* **Always** have someone review your dataset before submission
* Look for examples to model after if it’s a cell line dataset or one with a unique experimental design
* Use the [assay cheat sheet](https://docs.google.com/spreadsheets/d/1H9i1BK-VOXtMgGVv8LJZZZ9rbTG4XCQTBRxErdqMvWk/edit#gid=0) for existing, standard assays so that we stay consistent across Lattice, EBI and UCSCwrangling teams



## Project

### General

* Fill the following from the main project page **in ingest UI**:
    * Cell count
    * Technology
    * Species
    * Organ
    * Accessions
    * Estimated cell count
  
(Some guidelines can be found [here](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/dataset_acknowledgement_SOP.html#manual-curation-after-addition))
* Fill out the admin area, this helps other people when using ingest as a backoffice
* Project shortname → should be more descriptive than IDs (_For example: CoolOrganProject._)


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
* If it is a fetal donor age should be gestational age
* Use HSAPDV for human-specific development stages. Avoid using over-specific ontologies for non-fetal donors, as we have the "age" field for that, favouring ontologies such as “child stage” or “human adult stage”.
  * Use EFO for humans only when<span style="color:red"> age is not publicly available for GDPR-affected donors</span> (Living individuals)
* If donors are alive at the time of biomaterial collection, **you shouldn’t ask for extra metadata to the authors**. This is to maintain consistency with our GDPR guidelines, that state that for living organisms, we wrangle data that is publicly available (Diagram here [https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/GDPR_Guidelines.html](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/GDPR_Guidelines.html))
* Donor organism name can match the description
* If the dataset is curated from publicly available sources, chances are the donor **organism does not have an accession.** Sample accessions are usually generated automatically by ENA/SRA when archiving, and usually scientists take samples as the input to the sequencing processes.
* Genus species is required even though it's not schema required
* Donors of organs that were given to them via transplant are still the primary donors, the transplant part could be captured in the donor description:
  * “56YO Latin female with a heart transplant”
  * Example dataset: [KidneybiopsyscRNA-seq](https://contribute.data.humancellatlas.org/projects/detail?uuid=027c51c6-0719-469f-a7f5-640fe57cbece)
* In **xenograft** experiments:
  * The donor is the one that the sample comes from, not the one that the sample is grafted inside. Think of the grafted individual as a "glorified petri dish"
  * Xenograft would be mentioned in the cell suspension section, under growth environment or free text description
  * Example dataset: transplantedHumanIsletsNuclei

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
    * Cell suspension (WIP; please see this [ticket](https://app.zenhub.com/workspaces/operations-5fa2d8f2df78bb000f7fb2b5/issues/ebi-ait/hca-ebi-wrangler-central/927))
    
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
* It’s helpful to use the Visium Spatial Gene Expression ontology term as the library preparation protocol to generate the Visium fastq files
* FFPE vs Fresh-Frozen information can be stored in the `preservation method` term
* Add the `permeabilization time` to the imaging_preparation_protocol

## Files

### All files

* Always fill up the `file source`. This helps the downstream components to identify the CGMs.
  * <span style="color:red">Do not use DCP/2 Ingest</span>. That term is reserved for the spreadsheet generated by ingest.
* Always include ontologies for `content description`
  * If there is a zip file, list multiple ontologies as an array

### Image File

* All image files **and** files related to analyzing, understanding, processing the image files should be in this tab
* This includes .csv files containing spatial barcodes, and files which link the annotations of the image file image coordinates
* The JSON files containing the spot diameter and scale factors for the image acquisition are important for the reusability of the data. These should be included, and the recommended ontology term for their content description is `data:3546`: `Image metadata`.
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

<table>
  <tr>
   <td>
<strong>Field</strong>
   </td>
   <td><strong><a href="https://www.ebi.ac.uk/ols/ontologies">Ontology</a></strong>
   </td>
   <td><strong>url</strong>
   </td>
  </tr>
  <tr>
   <td>species
   </td>
   <td>NCBITaxon
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/ncbitaxon">NCBITaxon</a>
   </td>
  </tr>
  <tr>
   <td>ethnicity
   </td>
   <td>HANCESTRO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/hancestro">HANCESTRO</a>
   </td>
  </tr>
  <tr>
   <td>developmental stage
   </td>
   <td>HsapDv (for human), EFO (for mouse)
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/hsapdv">HSAPDV</a>
   </td>
  </tr>
  <tr>
   <td>disease
   </td>
   <td>MONDO, PATO (if normal)
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/mondo">MONDO</a>
   </td>
  </tr>
  <tr>
   <td>units of measurement
   </td>
   <td>UO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/uo">UO</a>
   </td>
  </tr>
  <tr>
   <td>enrichment method
   </td>
   <td>EFO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/efo">EFO</a>
   </td>
  </tr>
  <tr>
   <td>dissociation method
   </td>
   <td>EFO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/efo">EFO</a>
   </td>
  </tr>
  <tr>
   <td>collection method
   </td>
   <td>EFO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/efo">EFO</a>
   </td>
  </tr>
  <tr>
   <td>library preparation method
   </td>
   <td>EFO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/efo">EFO</a>
   </td>
  </tr>
  <tr>
   <td>sequencing approach
   </td>
   <td>EFO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/efo">EFO</a>
   </td>
  </tr>
  <tr>
   <td>organ & organ_part
   </td>
   <td>UBERON
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/uberon">UBERON</a>
   </td>
  </tr>
  <tr>
   <td>cell type
   </td>
   <td>CL
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/cl">CL</a>
   </td>
  </tr>
  <tr>
   <td>biological macromolecule
   </td>
   <td>OBI, CHEBI
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/obi">OBI</a> <a href="https://www.ebi.ac.uk/ols/ontologies/chebi">CHEBI</a>
   </td>
  </tr>
  <tr>
   <td>library pre/amplification
   </td>
   <td>OBI, EFO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/obi">OBI</a>, <a href="https://www.ebi.ac.uk/ols/ontologies/efo">EFO</a>
   </td>
  </tr>
  <tr>
   <td>sequencing instrument
   </td>
   <td>EFO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/efo">EFO</a>
   </td>
  </tr>
  <tr>
   <td>file content description
   </td>
   <td>data (EDAM)
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/edam/terms?iri=http%3A%2F%2Fedamontology.org%2Fdata_0867">EDAM</a>
   </td>
  </tr>
  <tr>
   <td>project role
   </td>
   <td>EFO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/efo">EFO</a>
   </td>
  </tr>
  <tr>
   <td>mouse strain
   </td>
   <td>EFO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/efo">EFO</a>
   </td>
  </tr>
  <tr>
   <td>cell cycle
   </td>
   <td>GO
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/ontologies/go">GO</a>
   </td>
  </tr>
</table>

## Archiving

Once the submission has been successfully archived, accessions should be communicated back to the contributor. If there is a risk that the deadline the contributor gave will not be met, the contributor should be contacted to inform them of the risk and offer alternatives or workarounds. The project level accessions should be provided within the main body of the email.

By default, the release date will be set up to 2 years from the moment the submission is archived. This date can be changed to an earlier date (Provided by the contributor) but we won't hold the data for more than 2 years. After 2 years the data will be made public. 