---
layout: default
title: Request ontology terms
parent: SOPs
---

# Request Ontology terms SOP

## Objectives
Outline the process of **requesting ontology terms**, as well as document release dates for the wrangler team.

### Requesting new ontology terms

Ontology requests should be issued as tickets on the relevant repo to that ontology, [see listing below](#ontology-repos).

Please request them using the issue template if provided. 

#### Edits to the Cell Ontology (CL) and UBERON

If it is a Cell Ontology (CL) or UBERON request, please add [@paolaroncaglia](https://github.com/paolaroncaglia) as the assignee, add the `HCA/DCP` label and any other relevant labels such as the priority (if it is an urgent request).

### Request an existing term be added to the HCAO

[Request an HCAO edit](https://github.com/HumanCellAtlas/ontology/issues/new/choose){: .btn .btn-blue }

### Release dates and plan of release
The tickets added to the ontology repository, as posted above, are revised by @zoependlington after tagging. Depending on your request:

- **New term request**: Terms should be requested by the 10th of each month*.
- **Import of terms from other ontologies into HCAO**: Up until the 17th of each month.

*New terms might not be available after each monthly release if requesting to an external database (Not EFO).

Release of databases:
- EFO = ~16th of each month.
- HCAO = ~18-19th of each month.

Once Zoe updates the HCAO it gets automatically released to the [EBI OLS](https://www.ebi.ac.uk/ols/ontologies/hcao). She will usually ping the ingest team to also release the ontology to our environments on:
- [Staging](https://ontology.staging.archive.data.humancellatlas.org/index)
- [Production](https://ontology.archive.data.humancellatlas.org/index)

### Ontology-related questions
For any question, please contact @zoependlington. She is also available on the HCA `data-wrangling-int` slack channel. Please use tickets for complex ontology questions.

Please take in account that she is only working 20% for the HCA, so be patient with your requests.

### Ontology repos

| Field type          | Ontology                       | github repo                                                  |
|---------------------|--------------------------------|-----------------------------------------------------------------|
| Anatomical location | Uber-anatomy ontology ([UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon)) | [obophenotype/uberon](https://github.com/obophenotype/uberon) |
| Cell types          | Cell ontology ([CL](https://www.ebi.ac.uk/ols/ontologies/cl))             | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology)                             |
| Experimental factors & Developmental stage (mouse)| Experimental Factor Ontology ([EFO](https://www.ebi.ac.uk/ols/ontologies/efo))             | [EBISPOT/efo](https://github.com/EBISPOT/efo) |
| Ethnicity           | Human Ancestry Ontology ([HANCESTRO](https://www.ebi.ac.uk/ols/ontologies/hancestro))             | [EBISPOT/ancestro](https://github.com/EBISPOT/ancestro)                                         |
| Developmental stage (human) | Human Developmental Stages ([HSAPDV](https://www.ebi.ac.uk/ols/ontologies/hsapdv))             | [obophenotype/developmental-stage-ontologies](https://github.com/obophenotype/developmental-stage-ontologies)|
| Diseases | Mondo Disease Ontology ([MONDO](https://www.ebi.ac.uk/ols/ontologies/mondo))             | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) |
| File content | Bioinformatics operations, data types, formats, identifiers and topics ([EDAM](https://www.ebi.ac.uk/ols/ontologies/edam))             | [edamontology/edamontology](https://github.com/edamontology/edamontology)|
| Chemicals & Molecules | Chemical Entities of Biological Interest ([CHEBI](https://www.ebi.ac.uk/ols/ontologies/chebi))      | [ebi-chebi/ChEBI](https://github.com/ebi-chebi/ChEBI)|
| Imaging techniques | Biological Imaging Methods Ontology ([FBBI](https://www.ebi.ac.uk/ols/ontologies/fbbi))      | [CRBS/Biological_Imaging_Methods_Ontology](https://github.com/CRBS/Biological_Imaging_Methods_Ontology)|

