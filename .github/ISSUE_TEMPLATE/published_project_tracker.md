---
name: Wrangling Project Tracker
about: Create a ticket for tracking key events of an in-progress project.
title: ''
labels: dataset,publication
assignees: ''
projects: 'ebi-ait/12'

---

<!--Set Primary Wrangler as assignee and set project when issue is created. Title should contain an accession-->

### Project short name:

### Primary Wrangler:

### Secondary Wrangler:

<!--Link to associated files-->

### Internal links

* Google Drive:
* Ingest uuid:

### Study links

* Paper:
* Accessioned data:
* Atlas Tracker Study name:


### Key Events

- [ ] Confirm the consent type of project
- [ ] Collect any files according to consent type
- [ ] Populate the HCA metadata spreadsheet to meet HCA metadata standard
- [ ] Upload sheet to create submission and validate metadata
- [ ] Transfer files to ingest via [hca-util](https://github.com/ebi-ait/hca-util) to validate data files (`Metadata valid` state)
- [ ] Check linking using ingest graph validator (`Graph valid` state)
- [ ] Ask the Secondary Wrangler for an end-to-end review of the project, apply comments and validate again (`Graph valid` state)
- [ ] Submit dataset to Production (`Submitted` state)
- [ ] Check export is completed (`Exported` state)
- [ ] Complete the Export SOP