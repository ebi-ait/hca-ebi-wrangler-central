---
layout: default
title: Update a project
parent: After export
grand_parent: SOPs
nav_order: 3
last_modified_date: 31/03/2020
---

UNDER REVIEW 
{: .label .label-yellow }

*Process is under review until full update process is established and tested.*

# How to Update a Project

## Definitions:

*Update* - Any edit to a project, could include editing a typo, adding/deleting metadata or data, changing how entities are linked

*Identifier* - The person who identifies the error that needs to be corrected

*Performer* -  The person who performs the update process

Things that can be done: 
* Fix an error in any existing field 
* Enter information into any blank field in an existing entity
* Add new metadata entities and sequence files 

Things that can’t be done: (?)
* Change the 'DescribedBy' field
* Delete anything from a submission

### When can I update a project?

* Non-analysed datasets - No restrictions
* Analysed datasets - OPEN QUESTION: Should be coordinated with the Matrix Service/DataOps?

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

1. If the project is already in the 'Needs Update' piepeline, then assign yourself to the project and follow the steps below to make the necessary changes. Refer to the primary wrangler to ensure there are no other outstanding changes that need to be made.

## Updating a project in ingest and DCP
Note that Adding Metadata Entities and Sequence Files can only be done using a spreadsheet, and requires a new submission. 

### Updating Project Metadata (UI Only) 
To edit Project Metadata, use the 'Edit Project' button on the Project tab for the specific project. After finishing making the specific changes and saving, the latest submission should move from an 'Exported' state back to a 'Valid' state, which allows for re-exporting the submission with the updated project metadata. 

If the latest submission does not move to a 'Valid' state, then the workaround is to make an edit to the metadata in the submission (see below). This will move the submission from the 'Exported' state to the 'Valid' state and allow reexporting the submission with updated metadata. 

If there are no necessary metadata updates to make in the submission, the workaround is to make an edit to the metadata in the submission, and then edit the submission once again to change the metadata to its original state. The metadata is therefore unchanged, but the submission will now be in the 'Valid' state, allowing export of updated metadata. See 'here'

### Updating metadata entities in a submission
To edit metadata entities in a submission, select the desired submission. There is an 'edit' button for each row of metadata in the submission, and selecting this 'edit' button will allow one to make changes to the submission metadata. 

After saving the changes, the submission state should move from 'Exported' back to 'Valid'. You can then 'Submit' the submission once more, taking care to uncheck the option to delete the upload area, unless you are certain this is the final update. This will export the submission to the downstream components. See the '[Exporting SOP](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Exporting_SOP.html)' for more details. 

### Updating / Adding links between metadata entities

NOT CURRENTLY SUPPORTED DOWNSTREAM OF INGEST
{: .label .label-yellow }

We are also now able to remove or create links between metadata entities. This can be done from the Process Tab of a submission. Expand the specific process that needs to be edited, and there are three columns: Inputs, Protocols, and Outputs. 

From this screen, we can remove or add new inputs, new protocols, and new outputs to be linked to this specific process. There is a search field for searching through entities, but this currently searches through all entities in the entire environment (not restricted to this project). One workaround to find the specific entity may be to rename the entity in the Ingest-UI, allowing it to be found easier. 

### Adding New Entities (Using Spreadsheet Only) 
We now have the ability to add new metadata entities and sequence files to the project. This can only be done by creating a new spreadsheet and making additional submissions. 

The spreadsheet only requires the tabs which contain the entities which are new, and only requires the new rows. For example, adding a new cell suspension linked to an already existing specimen_from_organism only requires the cell suspension tab and information. 

New entities can be linked to existing entities in previous submissions using the specific uuids for each existing entity. These uuids can be obtained from downloading the metadata spreadsheet for that submission. 

In the previous example, if I wanted to link a new cell suspension to an already existing specimen_from_organism, instead of the 'Input specimen_from_organism ID' column in the spreadsheet, we would create a new 'specimen_from_organism uuid' column, with the programmatic name (Row 4 of spreadsheet) of 'specimen_from_organism.uuid' and input the uuid of the specimen_from_organism in that cell. 

Once the spreadsheet is completed, then create a new submission to the project using the spreadsheet. If there are any sequence files that are part of this addition, then those sequence files should be synced to the submission upload area for the new submission. 

Now you will be able to export the submission to the downstream components. See '[here](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Exporting_SOP.html)'. 

## Exporting a submission to downstream components
There is a fantastic SOP [here](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/dataset_wrangling_SOP.html#exporting-the-submission-to-dcp). 

When filling in the import request form for export of an update submission, please specify in the 'Additional info' section that it is an update so that the import team is aware.

Not functional: 
1. If the performer has the ability to download a spreadsheet from the ingest UI with the appropriate UUIDs, the performer can follow the [ingest guide here](https://github.com/HumanCellAtlas/ingest-central/wiki/Updating-Metadata-through-Spreadsheets)
1. If the project that requires AUDR was ingested before ingest started storing spreadsheets (~June 2019) then the performer will need to manually retrieve uuids for every entity in the spreadsheet using the ingest API and save them in the spreadsheet with the appropriate column names, e.g. `cell_suspension.uuid`, `donor_organism.uuid` (do we have a script for this?)
1. Once completed, go to the submission view, click  `Download spreadsheet` button to download a copy of the updated spreadsheet that has been updated with metadata UUIDs. Save this copy on Google Drive in the Projects folder with a name containing AUDR and date. You will need this spreadsheet for all subsequent updates. This is a temporary measure.



## Updating the project in the Archives

*Need to figure this out*

formerly known as AUDR
