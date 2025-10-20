---
layout: default
title: Pre-submission SOP
parent: Managed access
grand_parent: SOPs
nav_order: 3
last_modified_date: 28/08/2024
---

<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# Managed access project - Pre-submission SOP
Refer to this guide to prepare for the ingestion of a managed access project once the DCA has been signed.

## Register the project in DUOS system

A copy of the managed access project will have to be created in [DUOS](https://duos.org/) to control access to the data once it’s available on the HCA Data Portal.

1. Email the DUOS representative (Jonathan at jlawson@broadinstitute.org) with the [DUOS project information fields](https://docs.google.com/document/d/18pzeKafFQZ0rhqrb2DLOCciHUu4On4g2rtgnqygIfTE/edit#heading=h.674bm0dao5mr), using the information from the DCA agreement. This is mainly project metadata, the only personal data shared with the Broad is the PI’s name.
2. Register in the HCA Data Repository Ingest Service the project’s DUOS id provided by the DUOS representative

[Template email](#email-template---registration-to-duos){: .btn .btn-blue }


## Send instructions to contributor
Send an email to the data contributor with instructions on next steps*

Send to the contributor, with the wrangler email in CC
1. An outline of next steps
2. The metadata spreadsheet guide
3. A metadata spreadsheet template
4. A reminder to not share any sensitive data or metadata via email or other means of communication. 

[Template email](#email-template---instructions-for-the-contributor){: .btn .btn-blue }

If data contributor will just contribute Tier 2 metadata (and FASTQ files), an alterned doc should be shared:

[Tier 2 template email](#)

## Prepare a secure storage area
Prepare a secure storage area in AWS for the projects’ data and metadata. 
1. Create a storage area using the project's uuid as name \
`$ hca-util create <uuid-of-project>` 
2. The contributor needs a set of credentials (AWS access key and AWS secret key) to be able to upload data to the AWS secure storage area.
Ask a developer to follow [these instructions](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#aws-user-for-contributors) to create the credentials. The only information needed is the contributor’s name and email address. 



For next steps see [Managed access project - Data Transfer SOP](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Managed_access/Data_Transfer_SOP.html)

### Email template - Registration to DUOS

> Hi Jonathan,
> Can you please register this project in DUOS?
> Please let me know if you need more information on any of the fields.
> 
> ### Study Name
> \<PROJECT TITLE>
> ### Study Description
> \<PROJECT DESCRIPTION>
> ### Data Types
> \<Fastqs and cell count matrix>
> ### Principal Investigator Name
> \<PI full name>
> ### Public Visibility
> Please select one of the following data use permissions for your dataset
> - Yes, I want my dataset info to be visible and available for requests
> - No, I do not want my dataset info to be visible and available for requests
> ## Data Access Governance (for individual datasets)
> ### Consent Group (Dataset) Name
> \<PROJECT TITLE>
> ### Primary Data Use Terms
> General Research Use
> ### Secondary Data Use Terms
> Non-Commercial Use / None
> ### Data Location
> Terra Data Repository
> ### Phenotype
> Healthy/ Diseased
> ### \# of Participants
> \<n> donors

Best,
<wrangler>

### Email template - Instructions for the contributor

> Dear [name/s of contributor/s],
>
> Thank you for signing the Data Contributor Agreement.
> The next steps are:
> 1. Assemble your metadata to meet the HCA standard \
> Attached to this email you will find a metadata spreadsheet where you can fill in all the details of your experimental metadata. A guide to help in this process can be found here: [Spreadsheet Quick Guide](https://ebi-ait.github.io/hca-metadata-community/contributing/spreadsheet-guide.html) \
> If you’ve used organoid or cell line samples or you’ve performed spatial transcriptomics experiments please let me know so I can send you additional information. It’s possible to customise the spreadsheet to better fit your experiment design, so please get in touch if this is something I can help with.
> 2. Upload your data and metadata to our secure cloud space \
> I am preparing a secure storage area specific for your project where you can upload your data files and the filled-in spreadsheet. I'll send you the details of this upload area and instructions on next steps in a separate email to keep the credentials secure. \
> **In order to avoid circulating any potentially sensitive data over unencrypted channels, please refrain from sending any data or metadata via email.** This includes filled-in or partially completed copies of the spreadsheet. 
> 3. Review and Export \
> The HCA data wrangling team will take care of reviewing and validating the data and metadata once you upload it. If anything needs to be adjusted, I’ll update you in due course. In general we aim to complete the review in 7 business days.
> 4. Publish the project \
>Once everything is reviewed and ready, I’ll update you with a possible release date so you can confirm if you’re ready to proceed with publishing the project under managed access.
>
> Do not hesitate to get back in touch if you have any issues with any part of the process. I would also like to suggest a Zoom call to walk you through the metadata spreadsheet once you have taken an initial look at it. Please let me know what times might be suitable for you.
>
> Warm regards, \
> [primary wrangler name]
> 
> On behalf of the HCA Data Platform - Data Wrangling Team

### Tier 2 email template - Instructions for the contributor
> Dear <name>,
> Thank you for signing the Data Contributor Agreement, all parties have now signed. You should have received an email with a copy of the Agreement document, let me know if you haven't received that so I can share it with you.
> The next steps are:
> 1. Assemble your Tier 2 metadata & File manifest in the HCA standards
> Attached to this email, you will find a spreadsheet template where you can fill all the Tier 2 metadata for this Lung project. Please use the same donor_IDs as those you've provided for Tier 1 metadata before. Remember, you don't have to fill all the Tier 2 fields just what you have in place.
> Attached is also a file manifest, to enable us mapping library_ID with each FASTQ file along with read_index, lane_number and file_format of each file.
> 2. Upload your data and metadata to our secure cloud space
> I am preparing a secure storage area specific for your project where you can upload your data files and the filled-in spreadsheet. I’ll send you the details of this upload area and instructions on next steps in a separate email to keep the credentials secure.
> In order to avoid circulating any potentially sensitive data over unencrypted channels, please refrain from sending any data or metadata via email. This includes filled-in or partially completed copies of the spreadsheet.
> 3. Review and Export
> The HCA data wrangling team will take care of reviewing and validating the data and metadata once you upload it. If anything needs to be adjusted, I’ll update you in due course. In general we aim to complete the review in 7 business days.
> 4. Publish the project
> Once everything is reviewed and ready, I’ll update you with a possible release date so you can confirm if you’re ready to proceed with publishing the project under managed access.
> Do not hesitate to get in touch if you have any issues with any part of the process. We are able to arrange a Zoom call to help you out if you need any help filling the spreadsheets or uploading files.
>
> Warm regards,
> Arsenios & Ida
> On behalf of HCA Data Repository - Data Wrangling Team
