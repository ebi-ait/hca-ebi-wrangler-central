---
name: CellxGene Project Tracker
about: Create a ticket for a cellxgene project
title: ''
labels: cellxgene, dataset
assignees: ''

---

**Collection/dataset this task is for:**
<!--Indicate the name of the group or the dataset this task is for. e.g. Tissue Sensitivity dataset.-->
- file name - 
- [link to existing collection in cellxgene]()
- project uuid - c5f46615-68de-4cf4-bbc2-a0ae10f08243
- [ticket link to DCP wrangling ticket]()
- [link to ingest UI](https://contribute.data.humancellatlas.org/projects/detail?uuid=c5f46615-68de-4cf4-bbc2-a0ae10f08243)

**Relevant People**
- Wrangler
- Contributor
- dev
<!--Set Primary Wrangler as assignee and set project when issue is created. Title should contain an accession-->

### Primary Wrangler:

### Associated files
* [SOP](https://docs.google.com/document/d/1UVGIllybmEI46x22NSDpMNRywT3c8hcGrcw6opiHdbg/edit#)
* [Knowledge Sharing Drive](https://drive.google.com/drive/folders/1cIgfeZZaoo2mFo2mN9iZ00_MZt94mvLv)
*[Ingest-cellxgene-submitter](https://github.com/ebi-ait/ingest-cellxgene-submitter) 
*[Cellxgene-schema](https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/2.0.0/schema.md)
*[Cellxgene-schema-validate](https://github.com/chanzuckerberg/single-cell-curation)
*[Cellxgene-submit-collection](https://cellxgene.cziscience.com/?curator=true)

### Published study links

* Paper:

* Accessioned data:

### Key Events

- [ ] Collect necessary matrix, cell-type annotation, and embedding files
- [ ] Modified var layer to meet cellxgene schema (adding feature_is_filtered)
- [ ] Created/Modified raw.var to meet cellxgene schema
- [ ] Modified obs layer to meet cellxgene schema 
- [ ] Created uns layer to meet cellxgene schema
- [ ] Ensured obsm layer is present
- [ ] Created h5ad with processed component parts using AnnData
- [ ] Created h5ad with raw matrix and raw var using AnnData
- [ ] Filtered ENSEMBL IDs from annotated and raw matrix
- [ ] Combined processed and raw h5ad to one h5ad object
- [ ] Run [cellxgene-schema validate](https://github.com/chanzuckerberg/single-cell-curation)
- [ ] Secondary review (?) 
- [ ] Submitted to collection in [cellxgene](https://cellxgene.cziscience.com/?curator=true)
