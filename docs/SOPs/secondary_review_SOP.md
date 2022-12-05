---
layout: default
title: Secondary review
parent: SOPs
---

# Secondary wrangler review

Secondary review should be requested once the submission is metadata and graph valid in ingest. This makes the review process much easier, but in certain cases, like a contributor working on a tight schedule, you can request a review before that. The instructions included here to manually check the linking and files are useful in those cases. 

End-to-end review includes, but is not limited to, performing the following:

## Reconstruct experiment based on spreadsheet

Wrangler should be able to generate a graph (by hand or using graph tool) of the experimental design using the HCA metadata model based on the information in the spreadsheet. This includes reconstructing the linking between file and biomaterial entities (the graph "spine") and identifying where the protocols are used. The thing being checked here is that the linking between entities is correct and that all donors/samples are accounted for.
The ingest graph validation ([IGV](https://github.com/ebi-ait/ingest-graph-validator)) step helps ensure that all biomaterials are linked continuously from donor to analysis of sequence file, however the IGV can't detect conceptual errors like an enrichment protocol that is applied to wrong cell suspension, which is why reviewing is very valuable.

Wrangler should be able to account for every biomaterial, file, and protocol entity in the spreadsheet. For example, are all the cell suspensions listed in the Cell suspension tab represented in the linking field of the Sequence file tab? Are there any donors listed in the Donor tab that do not have any associated sequencing or imaging files? The thing being checked here is that every biomaterial, file, and protocol entity in the spreadsheet ends up in an exported bundle.

> One way to do this manually is to copy the first column in one tab and the associated linking column in another tab (e.g. the biomaterial_id in column A of the donor tab and the corresponding biomaterial_id column in the linking column of the specimen tab), paste each column in a new tab, remove duplicate values in each column separately, sort each column separately, and then use Excel's EXACT function to compare row-by-row. If any of those functions returns FALSE, you know there are IDs missing or possibly named differently.

Wrangler should be able to identify whether the same library preparation was sequenced more than once. If the primary wrangler can't confirm this, s/he should check with the data contributor. If the secondary wrangler can't confirm this, s/he should check with the primary wrangler. If either wrangler can confirm this and the answer is yes, wrangler should confirm that the `library_preparation_id` field is filled in correctly. The thing being checked here is whether data consumers will be able to identify which sequencing files came from the same library preparation so they can be analyzed together.

## Confirm files are uploaded to s3

Wrangler should be able to confirm that every sequencing, imaging, and supplementary file listed in the spreadsheet is located in the associated s3 bucket for that project. File names need to match exactly. The thing being checked here is that all relevant files have been submitted.

Wrangler should be able to identify if there are any extra files in the s3 bucket that are not represented in the spreadsheet. If there are such files, primary wrangler should confirm with contributor (secondary wrangler should confirm with primary wrangler) whether these files are:
 
 1. Misnamed in the spreadsheet. If so, update spreadsheet to the correct name.
 1. Extra files that are not needed for the submission. If so, wrangler should remove them from the s3 bucket.
 1. Extra files that are needed for the submission. If so, wrangler should request contributor to add them to the spreadsheet.
 
 The thing being checked here is that all relevant files are recorded in the spreadsheet.
 
 > One way to do this to list the files in the s3 (aws s3 ls), copy the filenames to a new Excel tab, then copy all the filenames from the metadata spreadsheet into another column in the new tab, sort each column separately, and then use Excel's EXACT function to compare row-by-row. If any of those functions returns FALSE, you know there are files missing from the s3 bucket or the spreadsheet. 

## Confirm correct ontologies are used

Wrangler should be able to confirm that the correct `ontology` and `ontology_label` fields are filled in for all ontologized `text` fields that have been filled in by contributor. If the contributor has not filled in `ontology` and `ontology_label` fields, the wrangler should do this. If these fields have been filled in by contributor, another wrangler, review them to make sure they accurately describe what the contributor has filled in for the `text` field.

If after consulting with the other wranglers, no appropriate ontology term can be found, wrangler should request an update to the ontology and link the ontology ticket in the project ticket. The thing being checked here is that all ontologized fields are mapped to the correct ontology term.

**All `ontology` and `ontology_label` fields need to be reviewed by contributor when they are asked to do a final review of their submission.**

## Suggest optional fields that could be filled

Wrangler should review missing metadata fields and identify any that could be filled in by the wrangler or could easily be requested from the contributor. Typically, the Primary Wrangler should do most of the requesting of additional fields from contributor as s/he is the main person in contact. Some examples of optional fields that might be requested or suggested include:

- Is the read length in the Sequencing file tab missing? Wrangler can calculate this from the submitted files.
- Does the project have a publication or pre-print that the contributor did not record? Wrangler can fill this in.
- Did the contributor reference a published protocol but did not fill out some optional fields for the protocol, like the primer used during library preparation? Wrangler can fill this in.
- Is the data already archived by the contributor did not fill in some of the accessions? Wrangler can do this.
- Did the contributor do a 10x experiment but did not fill in any of the 10x-specific fields? Wrangler can ask the contributor whether they can fill these fields in.

The thing being checked here is that wrangler-led submissions are high-quality. Wranglers should use their own judgement here regarding how many optional fields to request from a contributor or fill in themselves. Wranglers should strive to ingest high-quality examples of metadata in order to set a high standard for future contributors as well as test the DCP infrastructure and the HCA metadata standard. 

**All fields added by a wrangler need to be reviewed by contributor when they are asked to do a final review of their submission.**
