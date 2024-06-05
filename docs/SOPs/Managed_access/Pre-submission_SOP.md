---
layout: default
title: Pre-submission SOP
parent: Managed access
grand_parent: SOPs
nav_order: 3
last_modified_date: 05/06/2024
---

<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# Managed access project - Pre-submission SOP
Refer to this guide to prepare for the ingestion of a managed access project once the DCA has been signed.

## Register the project in DUOS system

A copy of the managed access project will have to be created in [DUOS](https://duos.org/) to control access to the data once it’s available on the HCA Data Portal.

1. Email the DUOS representative (Jonathan at jlawson@broadinstitute.org) with the [DUOS project information fields](https://docs.google.com/document/d/18pzeKafFQZ0rhqrb2DLOCciHUu4On4g2rtgnqygIfTE/edit#heading=h.674bm0dao5mr), using the information from the DCA agreement. This is mainly project metadata, the only personal data shared with the Broad is the PI’s name.
2. Register in the HCA Data Repository Ingest Service the project’s DUOS id provided by the DUOS representative

## Send instructions to contributor
Send an email to the data contributor with instructions on next steps*

Send to the contributor, with the wrangler email in CC
1. An outline of next steps
2. The metadata spreadsheet guide
3. A metadata spreadsheet template
4. A reminder to not share any sensitive data or metadata via email or other means of communication. 

[Template email](#email-template---instructions-for-the-contributor){: .btn .btn-blue }


## Prepare a secure storage area
Prepare a secure storage area in AWS for the projects’ data and metadata. 
1. Create a storage area using the project's uuid as name \
`$ hca-util create <uuid-of-project>` 
2. The contributor needs a set of credentials (AWS access key and AWS secret key) to be able to upload data to the AWS secure storage area.
Ask a developer to follow [these instructions](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#aws-user-for-contributors) to create the credentials. The only information needed is the contributor’s name and email address. 



For next steps see [Managed access project - Data Transfer SOP](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Managed_access/Data_Transfer_SOP.html)

### Email template - Instructions for the contributor

> Dear [name/s of contributor/s],
>
> Thank you for signing the Data Contributor Agreement.
> The next steps are:
> 1. Assemble your metadata to meet the HCA standard \
> Attached to this email you will find a metadata spreadsheet where you can fill in all the details of your experimental metadata. A guide to help in this process can be found here: [Spreadsheet Quick Guide](https://ebi-ait.github.io/hca-metadata-community/contributing/spreadsheet-guide.html) \
> If you’ve used organoid or cell line samples or you’ve performed spatial transcriptomics experiments please let me know so I can send you additional information. It’s possible to customise the spreadsheet to better fit your experiment design, so please get in touch if this is something I can help with.
> 2. Upload your data and metadata to our secure cloud space \
> I am preparing a secure storage area specific for your project where you can upload your data files and the filled-in spreadsheet. Please let me know once you are happy you have filled out the spreadsheet and are ready to upload your data and metadata files, and I'll send you the details of this upload area and instructions on next steps. \
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

