---
layout: default
title: Request ontology terms
parent: SOPs
---

# Request Ontology terms SOP
{: .no_toc }

1. TOC
{:toc}

## Objectives
Outline the process of **requesting ontology terms**, as well as document release dates for the wrangler team.

### Requesting new ontology terms

The way to request an ontology term depends on the type of term and whether it already exists in another ontology. A decision tree to guide you on the method for requesting a term can be found here: [Ontology requests decision tree](#decision-tree).

In general you should try to include as much information as possible when requesting a term. Specific cases are provided below.

#### General guidance for all ontologies

* Indicate your use case
* Indicate the evidence for your term such as a publication or link to description
* tag [@zoependlington](https://github.com/zoependlington) in the ticket and label the ticket with `HCA` if possible
* Indicate priority if urgent
* Use the applicable issue template

Ontology requests should be issued as tickets on the relevant repo to that ontology, [see listing below](#ontology-repos).

If you aren't sure about what to do or have an ontology question, [create a ticket](https://github.com/HumanCellAtlas/ontology/issues) in the HCAO ontology repo.

#### For Cell type (CL) and Anatomical (UBERON) terms

As above [for all ontology terms](#general-guidance-for-all-ontology-terms) plus:
* Check whether the term exists in [FMA](https://www.ebi.ac.uk/ols/ontologies/fma), if so, please include the FMA ID in the definition section of the issue template
* Quote a publication or literature and evidence to support the term
* tag [@zoependlington](https://github.com/zoependlington) in the ticket
* Indicate any known taxon restrictions i.e. is the term only applicable to mammals? Quote literature if possible

[Request UBERON term](https://github.com/obophenotype/uberon/issues/new?labels=new+term+request&template=a_adding_term.md){: .btn .btn-blue }

[Request CL term](https://github.com/obophenotype/cell-ontology/issues/new?assignees=nicolevasilevsky%2C+dosumis%2C+addiehl&labels=new+term+request&template=a_adding_term.md&title=%5BNTR%5D){: .btn .btn-green }

#### For Experimental Factor (EFO) terms

As above [for all ontology terms](#general-guidance-for-all-ontology-terms) plus:
* Check whether the term exists in [BAO](https://www.ebi.ac.uk/ols/ontologies/bao), if so, please include the BAO ID in the definition section of the issue template
* Include a link to the literature if possible

### Requesting an existing term be added to the HCAO

If the term already exists in an ontology that can be imported into the HCAO, make a ticket directly in the HCAO repo.

[Request an HCAO edit](https://github.com/HumanCellAtlas/ontology/issues/new/choose){: .btn .btn-blue }

### Release dates and plan of release
The tickets added to the ontology repository, as posted above, are revised by @zoependlington after tagging. Depending on your request:

- **New term request**: Terms should be requested by the 10th of each month*.
- **Import of terms from other ontologies into HCAO**: Up until the 17th of each month.

*New terms might not be available after each monthly release if requesting to an external database (Not EFO).

Release of databases:
- EFO = ~15-18th of each month.
- HCAO = ~20th of each month.

Once Zoe updates the HCAO it gets automatically released to the [EBI OLS](https://www.ebi.ac.uk/ols/ontologies/hcao). She will usually ping the ingest team to also release the ontology to our environments on:
- [Staging](https://ontology.staging.archive.data.humancellatlas.org/index)
- [Production](https://ontology.archive.data.humancellatlas.org/index)

### Ontology-related questions
For any question, please contact @zoependlington or @paolaroncaglia. [Tickets in the HCAO repo](https://github.com/HumanCellAtlas/ontology/issues/new?assignees=paolaroncaglia%2C+zoependlington&labels=question&template=general_ontology_enquiry.md&title=%5BENQ%5D+) are preferred for complex ontology questions.

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

<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2020-12-22T13:33:12.071Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36\&quot; etag=\&quot;UxqkR7P7JDqvpgtyy4YD\&quot; version=\&quot;14.0.5\&quot;&gt;&lt;diagram id=\&quot;C5RBs43oDa-KdzZeNtuy\&quot; name=\&quot;Page-1\&quot;&gt;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&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>
