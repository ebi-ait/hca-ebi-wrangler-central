---
layout: default
title: Contributor communication
parent: SOPs
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>
# Contributor communication SOP
{: .no_toc }

## Background
{: .no_toc }

While wrangling a dataset from a contributor a wrangler needs to be in contact with the contributor in order to get the required metadata and data for a submission. This document provides guidance on how communication with contributors should be approached.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## General guidelines

<i class="fa fa-reply-all" aria-hidden="true"></i> **CC the wrangler-team email** in all communications with contributors so that the team is aware of the current status and can pick up on communications if the primary wrangler is unavailable.

<i class="fa fa-comments-o" aria-hidden="true"></i> <i class="fa fa-github-alt" aria-hidden="true"></i> **Record key communication events** in the related github project tracker ticket by ticking the relevant box or making a comment if more detail is useful. 

<i class="fa fa-pencil-square-o" aria-hidden="true"></i> Keep emails **clear**, **concise** and to the point 

<i class="fa fa-info-circle" aria-hidden="true"></i> Ensure the **most important information is first** - expect that the reader could lose interest at any moment

<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Make the subject line **capture attention**, including HCA/Human Cell Atlas is useful

<i class="fa fa-smile-o" aria-hidden="true"></i> Be **gracious, polite and friendly** 

<i class="fa fa-phone-square" aria-hidden="true"></i> Always leave the option of a **meeting to chat** if things seem to be getting complicated

## First contact
The aim of the first contact with a contributor is to find out some key information about the project and ask the contributor to provide more detailed information using the data questionnaire form(https://forms.gle/KFYna7zGdQvwya8b8) or by setting up a meeting in-person or via video chat.

The first contact email should contain:
- Link to register as part of the HCA
- Link to the dataset questionnaire(https://forms.gle/KFYna7zGdQvwya8b8) or an attempt to set up a meeting

[Template email](#first-contact---data-questionnaire){: .btn .btn-blue }

## Follow-up contact
Once the primary wrangler has gained more information about the dataset, a custom spreadsheet can be generated with the relevant tabs and fields for the contributor’s experiment. 

Before any data and metadata can be received, either the contributor or an authorised representative from their lab, must agree to the HCA terms and conditions by completing the HCA terms and conditions form.

The first follow up email should contain:
- Link to terms and conditions form (https://forms.gle/8XW8vapGQJRfKrc36)

[Template email](#terms-and-conditions){: .btn .btn-blue }

Once the terms and conditions form is complete, the metadata spreadsheet and the instructions and credentials for uploading data to their ingest upload area can be provided to the contributor. 

The second follow-up email should contain:
- Custom metadata spreadsheet
- Link to metadata spreadsheet guide
- Reminder that they will get the credentials sent to them shortly (Dev work)
- Link to instructions for how to upload data to an upload area(https://github.com/ebi-ait/hca-documentation/wiki/How-to-upload-data-to-an-upload-area-using-hca-util)

[Template email](#spreadsheet-and-data-upload-instructions){: .btn .btn-blue }

### Frequency of contact

After sending an email, we generally think one week is a reasonable time to respond. If a primary wrangler has not received any response or reason for delay they should send a reminder email after a week.

The reminder email should prompt the contributor to complete the step required to enable the wrangler to continue with their submission. It is nice to offer a call to talk over where the contributor may have been stuck.

If there is no response after a further week, the primary wrangler should send another prompting email.

If after two reminder emails have been sent without a response, the wrangler could consider: 
- CC’ing the PI or project manager of the contributor’s project
- Bringing it to the attention of the Ingest Product Owner/Manager and asking for advice
- For CZI funded projects - Jonah?

## Confirming details, filling gaps
It is normal for some details to be missed by the contributor in the first instance. 

There are some fields that aren’t strictly required but a wrangler should chase if possible:

For CBTM & HDBR donors
 - We have other means of accessing the full set of releasable metadata from these tissue banks so it is a good idea to check our sources to ensure we can include as much information as possible

For developmental donors
- For embryos we ideally want carnegie stage, all HDBR samples should have this
- Post-Conception weeks is a mandatory chase. Based on the survey we sent recently that was the most wanted field by the community.
- genotype/karyotype information

For all experiments
- Ethnicity
- Age
- Estimated number of cells
- **Library preparations**: If more than 1 set of fastq files per library preparation, make sure the approach is properly displayed.
Same library preparation was sequenced several times/produces more than 1 set of fastq files: Fill in the lane_index and communicate with contributors.
Different library preparations come from one cell suspension: Make sure the library preps are separated properly with the proper process.process_core.process_id

It is also common for a wrangler to need to confirm ontology curations. It is possible that a new ontology term will need to be created if an appropriate term doesn’t exist

Only if there are supplementary files: Make sure the files have been input twice in the spreadsheet (In the proper tab and in the `Supplementary files` tab). Once the files are uploaded make sure that they are called exactly the same.

## Final confirmation before submission

Once a submission is 100% valid and has been reviewed, a final confirmation email should be sent to the contributor with the latest spreadsheet attached to confirm they are happy with the curation.

[Template email](#final-confirmation-before-a-submission){: .btn .btn-blue }

## Confirmation of Accessions

Once the submission has been successfully archived, accessions should be communicated back to the contributor. If there is a risk that the deadline the contributor gave will not be met, the contributor should be contacted to inform them of the risk and offer alternatives or workarounds. The project level accessions should be provided within the main body of the email.

By default, the release date will be set up to 2 years from the moment the submission is archived. This date can be changed to an earlier date (Provided by the contributor) but **we won't hold the data for more than 2 years**

Once the dataset is released in an HCA snapshot release, the contributor should be informed and provided with the link to their dataset on the HCA Data Browser.

## Template emails
These templates are considered a guide to provide a skeleton with the required information. The primary wrangler can choose to edit and customise to make it more personal or appropriate for the situation.

### First contact - Data questionnaire

> Dear [name/s of contributor/s],
> 
> Thank you for contacting us regarding your interest in registering your project with the Human Cell Atlas! Below you will find the first steps:
> 
> 1 Register as part of the HCA by filling the following form: https://www.humancellatlas.org/register (if you haven’t already)
> 
> 2 Please fill out the dataset questionnaire (https://forms.gle/HWADhk3Z6hUEbvVh8). The questionnaire asks for information about your experiments. This will help us create a tailor spreadsheet for you to fill out about your project.
>
> Please be aware that as per GDPR guidelines, we are not able to directly wrangle any metadata or data originating from living donors. If your project contains metadata or data originating from living donors, please refrain from sending us that information. 
>
> After filling both forms, we will contact you with the next steps to continue the submission of your metadata collection and data.
> 
> I am happy to set up a meeting or call about any concerns or queries that your team might have.
> 
> Best regards,
> 
> [primary wrangler name]
> 
> On behalf of the HCA DCP Data Wrangling Team

### Terms and Conditions

#### If all data can be released openly:

> Dear [name/s of contributor/s],
> 
> Thank you for registering with the HCA and filling in our Dataset Questionnaire. 
> 
> Can you, or an authorised member of your lab, please officially confirm whether your data are from human research subjects and whether the data requires controlled access? You can do this by agreeing to our terms and conditions via the following form: https://forms.gle/8XW8vapGQJRfKrc36  
> 
> Once you have confirmed we are able to handle your metadata and data and we can share with you the next steps in metadata assembly and data upload.
> 
> We do/don’t think we will be able to provide you with accessions for your dataset by your requested date <enter date here>. 
> 
> *[If we don’t think we can meet the deadline]* 
> The earliest date we can offer would be [enter date here].
> 
> Best regards,
> 
> [primary wrangler name]
> 
> On behalf of the HCA DCP Data Wrangling Team

#### If data is managed access

> Dear <name/s of contributor/s>,
> 
> Thank you for registering with the HCA and filling in our Dataset Questionnaire. 
> 
> Currently we cannot handle raw sequencing data for projects that require controlled access. However, we can help you get your processed data (Gene count matrices, annotation files, etc) and publicly available metadata into the DCP data portal.
> 
> Please confirm if that option is ok with you, and we will proceed to share with you the next steps in metadata assembly and data upload.
> 
> Best regards,
> 
> [primary wrangler name]
> 
> On behalf of the HCA DCP Data Wrangling Team

#### If data has living europeans, i.e. subject to GDPR

Note that this is a constantly changing space, this email was last updated 2020-07-13.

> Dear [name/s of contributor/s],
> 
> Thank you for registering with the HCA and filling in our Dataset Questionnaire. 
> 
> Can you, or an authorised member of your lab, please officially confirm whether your data are from human research subjects and whether the data requires controlled access? You can do this by agreeing to our terms and conditions via the following form: https://forms.gle/8XW8vapGQJRfKrc36   
> 
> Once you have confirmed we are able to handle your metadata and data and we can share with you the next steps in metadata assembly and data upload.
> 
> We can then facilitate submitting your data and metadata to public EBI archives and provide you with accessions for your dataset.  
> 
> Currently the HCA DCP is not accepting data from living donors from European Centres, but we are currently working on supporting this data. By submitting through us with metadata that meets the HCA metadata standard, we will ensure your dataset is incorporated into the HCA DCP once we are able to support it.
> 
> Many thanks,
> 
> [primary wrangler name]
> 
> On behalf of the HCA DCP Data Wrangling Team

### Contributor Matrices and Cell Types 

#### Asking for Matrices from Contributor
 
> Dear [name/s of contributor/s], 
>
> We are also working with CellxGene to wrangle projects with appropriate expression matrices. I was wondering if you would be interested in submitting > your analysis files to the [Cellxgene visualization portal](cellxgene.cziscience.com/)?
>
> We would require the following, and would create an h5ad object meeting Cellxgene's [schema requirements](https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/2.0.0/schema.md).
> Raw count matrix
> Cell type annotation
> Cell-level metadata
> Embedding (Tsne/umap/spatial coordinates) 
> Normalised count matrix (optional) 
> 
> Please let us know and if you are able to provide the above files, we can work on submitting your project to the Cellxgene visualisation platform. 
> Let us know if you have any questions! 
> 
> [primary wrangler name]
>
> On behalf of the HCA DCP 

 
#### Informing Contributor of Project in HCA-DCP being wrangled to CellxGene
 
> Dear [name/s of contributor/s],
>
> I am writing about your paper (Cell Types of the Human Retina and Its Organoids at Single-Cell Resolution) which has been published in the HCA Data Portal. (https://data.humancellatlas.org/explore/projects/1dddae6e-3753-48af-b20e-fa22abad125d) 
>
> We are now wrangling projects with appropriate expression matrices from the HCA DCP to CellxGene. I was wondering if you would be interested in submitting your analysis files to the Cellxgene visualization portal?
>
> If so, we would need to alter the three .h5ad file provided on Mendeley to comply with Cellxgene's schema requirements.
>
> Let me know if you have any questions,
> 
> [primary wrangler name]
>
> On behalf of the HCA DCP 
 
 
#### Informing Contributor of PRoject in HCA-DCP already wrangled to CellxGene

> Dear [name/s of contributor/s],
> 
> I am writing about your paper [Name of Paper] which has been public in our HCA Data Portal. [Link to Paper in Data Portal]
> 
> As a pilot project, we have wrangled your dataset’s expression matrices to a private collection in the Cellxgene visualisation portal. To do this, we have altered your analysis file to comply with Cellxgene’s schema requirements. 
>
> 
> This is the link to the private collection in CellxGene where you can download and explore the h5ad files. Please let us know in the next couple of weeks if there is anything you would like to change or update!
>
> Warm regards,
>
> [primary wrangler name]
>
> On behalf of the HCA DCP 

 
### Spreadsheet and Data upload instructions

> Dear [name/s of contributor/s],
>
> Thank you for filling our terms and conditions form.
> 
> The next steps are:
> 
> 1 Assemble your metadata to meet the HCA standard
> 
> Attached to this email you will find a custom metadata spreadsheet where you can fill in all the details of your experimental metadata. A guide to help in this process can be found here: [Spreadsheet Quick Guide](https://ebi-ait.github.io/hca-metadata-community/contributing/spreadsheet-guide.html)
> 
> 2 Upload your data to our cloud space
> 
> The credentials you will need will be sent separately by a developer in our team.
> 
> Please treat these credentials securely and do not share them with anyone outside of those performing the file upload.
> 
> 3 What’s next?
> 
> After we have put together your data and metadata into a valid submission we will archive your data and metadata in [BioStudies](https://www.ebi.ac.uk/biostudies/), [BioSamples](https://www.ebi.ac.uk/biosamples/) and the [European Nucleotide Archive](https://www.ebi.ac.uk/ena/browser/home) and provide you with accessions for your manuscript. We will also ensure your data and metadata make it into the next HCA DCP snapshot releaserelease/snapshot. As indicated by you, we will ensure no data or metadata is made public until [enter date, 2 years from now]. / we will make the data public as soon as it is submitted.
> 
> [IF DATA RELEASE IS NOT IMMEDIATE] Please note that this is a release date that we set up as default to allow for manuscripts to be reviewed and corrections to be made. If you want this data to be released earlier, please contact us when the data can be openly shared and we will release it immediately.
> 
> Don’t hesitate to get back in touch if you have any issues with any part of the process.
> 
> Kind regards,
> 
> [primary wrangler name]
> 
> On behalf of the HCA DCP Data Wrangling Team


### Final confirmation before a submission

> Dear [name/s of contributor/s],
>
> I am excited to tell you that we are ready to submit your dataset to the HCA DCP!
>
> You will find attached the final metadata spreadsheet that will be submitted. 
>
> [optional] Please check [specific things to check].
>
> We can confirm that we have received your data files and they are valid and match the file metadata provided.
>
> If we don't hear otherwise, we will proceed with submission on <enter date 3 workings days from today> and will make your data and metadata publicly available on [enter date] / immediately. We will get back in touch once we have accessions available for your dataset.
>
> We will also let you know when your data has been made public on the Human Cell Atlas portal as part of the next snapshot release.
>
> Many thanks for your contribution to the Human Cell Atlas.
>
> [primary wrangler name]
> 
> On behalf of the HCA DCP Data Wrangling Team
