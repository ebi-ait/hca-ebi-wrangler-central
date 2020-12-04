---
layout: default
title: Request ontology terms
parent: SOPs
---

UNDER REVIEW
{: .label .label-yellow }

This process is currently under review as at 4/12/2020, please double check if anything is unclear.

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

### Decision tree

<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2020-12-04T17:37:02.588Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36\&quot; etag=\&quot;H50wsLuLHWExEvALcQzu\&quot; version=\&quot;13.10.4\&quot; type=\&quot;google\&quot;&gt;&lt;diagram id=\&quot;C5RBs43oDa-KdzZeNtuy\&quot; name=\&quot;Page-1\&quot;&gt;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&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>
