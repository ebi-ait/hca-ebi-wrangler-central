---
layout: default
title: AUDR SOP
parent: SOPs
---

# AUDR simple updates SOP

## Definitions:

*Identifier* - The person who identifies the error that needs to be corrected

*Performer* -  The person who performs the AUDR process

*Simple AUDR* - Currently this process only supports changes to any existing entities except files. 

Things that can be done:
* Fix an error in any existing field 
* Enter information into any blank field in an existing entity

Things that can’t be done:
* Add any new entity
* Edit/update fields in `file` entities
* Delete anything from a submission

### When can I AUDR?
* Non-analysed datasets - No restrictions

* Analysed datasets - Must be coordinated with the Matrix Service/DataOps. There are currently negotiations on how this will work. If a define schedule is decided this documentation will be updated.

## Procedure
1. The identifier of the AUDR issue creates an `hca-data-wrangling` repo ticket using the [AUDR ticket template](https://github.com/HumanCellAtlas/hca-data-wrangling/issues/new?assignees=&labels=AUDR&template=audr_template.md&title=AUDR%3A) to document what needs to be AUDRed as soon as a problem is identified. The ticket should include: 
    1. project full name
    1. project short name 
    1. Project UUID
    1. Original Submission date
    1. Original submission uuid?
    1. Most recent submission date and uuid if different from above
    1. Link to the github wrangler project tracker ticket
    1. Primary wrangler name, (tag if not the identifier)
    1. Changes that need to be addressed. 
    1. Check if affects secondary analysis (fields used, explanation)
    1. Check if affects matrix service metadata (fields used)
    1. Tag `@HumanCellAtlas/data-ops`

1. If the person performing the AUDR is not the primary wrangler, the performer should check-in with the primary wrangler to ensure there are no other outstanding changes that need to be made. If primary wrangler no longer works for the DCP or does not respond after 1 full business day, the performer can proceed.
1. The update process should be done in Staging first to test the submission works. 
    1. If the AUDR performer has the ability to download a spreadsheet from the ingest UI with the appropriate UUIDs, the performer can follow the [ingest guide here](https://github.com/HumanCellAtlas/ingest-central/wiki/Updating-Metadata-through-Spreadsheets)
    1. If the project that requires AUDR was ingested before ingest started storing spreadsheets (~June 2019) then the performer will need to manually retrieve uuids for every entity in the spreadsheet using the ingest API and save them in the spreadsheet with the appropriate column names, e.g. `cell_suspension.uuid`, `donor_organism.uuid`
1. Once successfully completed in Staging, create an [ingest-central ticket](https://github.com/HumanCellAtlas/ingest-central/issues/new/choose) about the AUDR in prod, Copying the same information from the hca-data-wrangling AUDR ticket . 
1. Tag `@HumanCellAtlas/data-ops` in the `ingest-central` ticket
1. Repeat the AUDR process in prod. 
1. Once done in prod, go to the submission view, click  `Download spreadsheet` button to download a copy of the updated spreadsheet that has been updated with metadata UUIDs. Save this copy on Google Drive in the Projects folder with a name containing AUDR and date. You will need this spreadsheet for all subsequent updates. This is a temporary measure.
