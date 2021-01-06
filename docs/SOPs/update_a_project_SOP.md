---
layout: default
title: Update a project SOP
parent: SOPs
last_modified_date: 23/12/2020
---

UNDER REVIEW 
{: .label .label-yellow }

*Process is under review until full update process is established and tested.*

# How to Update a Project

## Definitions:

*Update* - Any edit to a project, could include editing a typo, adding/deleting metadata or data, changing how entities are linked

*Identifier* - The person who identifies the error that needs to be corrected

*Performer* -  The person who performs the AUDR process

Things that can be done: (?)
* Fix an error in any existing field 
* Enter information into any blank field in an existing entity

Things that can’t be done: (?)
* Add any new entity
* Edit/update fields in `file` entities
* Delete anything from a submission

### When can I update a project?

* Non-analysed datasets - No restrictions

* Analysed datasets - Must be coordinated with the Matrix Service/DataOps. There are currently negotiations on how this will work. If a define schedule is decided this documentation will be updated.

## Procedure
1. The identifier of the issue reopens the project tracker ticket for that project if it has been closed and moves it to the 'Needs Update' pipeline of the [`Dataset wrangling status`](https://github.com/ebi-ait/hca-ebi-wrangler-central#workspaces/dataset-wrangling-status-5f994cb88e0805001759d2e9/board?repos=261790554) Zenhub board and makes a comment that contains the following information, (if not already specified in the ticket body)
    1. project full name
    1. project short name 
    1. Project UUID
    1. Original Submission date
    1. Original submission uuid?
    1. Most recent submission date and uuid if different from above
    1. Primary wrangler name, (tag if not the identifier)
    1. Changes that need to be addressed. 
    1. Check if affects secondary analysis (fields used, explanation)

1. If the person performing the update is not the primary wrangler, the performer should check-in with the primary wrangler to ensure there are no other outstanding changes that need to be made. If primary wrangler no longer works for the DCP or does not respond after 1 full business day, the performer can proceed.

## Updating the project in ingest and DCP


### Using a spreadsheet

1. If the performer has the ability to download a spreadsheet from the ingest UI with the appropriate UUIDs, the performer can follow the [ingest guide here](https://github.com/HumanCellAtlas/ingest-central/wiki/Updating-Metadata-through-Spreadsheets)
1. If the project that requires AUDR was ingested before ingest started storing spreadsheets (~June 2019) then the performer will need to manually retrieve uuids for every entity in the spreadsheet using the ingest API and save them in the spreadsheet with the appropriate column names, e.g. `cell_suspension.uuid`, `donor_organism.uuid` (do we have a script for this?)
1. Once completed, go to the submission view, click  `Download spreadsheet` button to download a copy of the updated spreadsheet that has been updated with metadata UUIDs. Save this copy on Google Drive in the Projects folder with a name containing AUDR and date. You will need this spreadsheet for all subsequent updates. This is a temporary measure.

### Using the UI

Small changes can be fixed in the UI. Project metadata can only be updated in the UI (true?)

## Updating the project in the Archives

*Need to figure this out*

formerly known as AUDR
