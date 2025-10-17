# Tier 2 definitions
Here we describe all the internal resources that have to do with Tier 2 and a small description of their functionality.
## What is Tier 2
HCA Tier 2 metadata are sets of biological metadata, specific for each bionetwork. Genetic Diversity Tier 2 will be requested by all bionetworks to record the coverage of the atlases and survey the diversity of samples used to build the atlases.
Ingestion of tier 2 is the responsibility of Data Repository (EBI), while HCA Tier 1 metadata that is going to be ingested by Data Repository (Clever Canary). 

## How is Tier 2 defined?
Via communications between EBI team and bionetwork coordinators who suggest relevant metadata. The EBI team is responsible for harmonising and aligning among different bionetworks where similar fields are suggested; and standardising metadata where possible through controlled vocabularies and ontologies.

## What is the format?
We now have various formats for Tier 2 metadata depending on who’s the end user.
* Metadata definitions ([example](https://docs.google.com/spreadsheets/d/1OmpbVgfGvoS79Objur1UhFuddLAC0qcxF80nEbP5b0U/))
* Metadata template ([example](https://docs.google.com/spreadsheets/d/1hR0nWjAT2J4a6-WDMcXT89rBpqkaHU6ZY21wcmwUros/))
* Metadata recommendations ([example](https://docs.google.com/spreadsheets/d/119qDwfQMDbghqSUFobJWSURsG-vPC0e7nP4Aot30XCw/edit?gid=308906633#gid=308906633))
### Definitions
Based on the [HCA Tier 1](https://docs.google.com/spreadsheets/d/13oqRLh1awe7bClpX617_HQaoS8XPZV5JKPtPEff8-p4/edit?gid=1404414727#gid=1404414727) definitions example, we capture all the information needed to describe each metadata field.
This is intended for users who want to review Tier 2 metadata and is also the basis for extending the current HCA json schema.
### Template
This is the sheet that we will ask contributors to fill in. This can later be integrated with Tier 1 into a full metadata DCP ingestible sheet. 
For help with converting t1 to dcp see https://github.com/ebi-ait/hca-tier1-to-dcp
### Recommendations
This is a work in progress sheet intended for communications with the bionetwork to prompt them to provide more information beyond just a list of metadata field names. All such sheets are now not in use nor actively updated.