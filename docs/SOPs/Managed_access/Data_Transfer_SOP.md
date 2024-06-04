---
layout: default
title: Data Transfer SOP
parent: Managed access
grand_parent: SOPs
nav_order: 4
last_modified_date: 04/06/2024
---

<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# Managed access project - Data Transfer SOP
Once the data contributor has notified the HCA data wrangler that they have completed the  metadata spreadsheet, the wrangler can give them access to hca-util area

## Data and metadata upload prerequisites
To upload data to hca-util contributors need credentials and their project’s area uuid. Credentials for hca-util must be zipped and password protected. 
1. Send an email addressed just to the contributor containing the area’s uuid and instructions on how to upload files to hca-util*
2. Send an email addressed just to the contributor containing the zipped credentials**
3. Send an email addressed just to the contributor containing the password for the*** credentials

[Template emails](#Email-templates){: .btn .btn-blue }

## Data and Metadata Upload
1. Send the contributor [these instructions](https://github.com/ebi-ait/hca-documentation/wiki/How-to-upload-data-to-an-upload-area-using-hca-util), explaining how to securely transfer their data to their assigned private upload area, using the template below. 
2. Ask the contributor to email the helpdesk advising when they have successfully uploaded data and metadata to their secure area

## Verify Upload
Once the contributors have notified the wrangler that the upload is complete:
1. Check the contents of the hca-util area - make sure the spreadsheet is there
2. Confirm with the contributor the name of the metadata spreadsheet and the number of files uploaded

If the hca-util area contains the expected files proceed to the [Managed access project - Data and metadata review and export SOP](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Managed_access/Review_and_export_SOP.html)
)


### Email templates
>Dear < Contributor Name >
>
>The upload area UUID for your project is: <uuid>
>To upload files to the cloud area please refer to this guide. You should receive the credentials needed to access the secure area soon, if you have any issues please let me know.
>Please let me know when you’ve completed the upload of data and metadata so that we can proceed with the submission.
>
>Best regards
>< Your Name >

>Dear < Contributor Name >
>
>Attached at the end of the email you will find a zip file with the credentials you need for the hca-util tool to upload your data. I will send you a separate email for the password of the zip file.
>Please treat these credentials securely and do not share them with anyone. 
>
>Best regards
>< Your Name >


>Dear < Contributor Name >
>
>The password to open the credentials zip file is: < password >
>
>Best Regards
>< Your Name >
