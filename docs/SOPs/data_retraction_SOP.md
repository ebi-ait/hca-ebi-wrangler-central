---
layout: default
title: Data retraction SOP
parent: SOPs
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# Data retraction SOP
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Purpose of this document

This document will serve to capture the steps needed to do a full cleanup of a dataset brokered by the Data Wrangling team.

## Overview

\[WIP - Edit [here](https://app.diagrams.net/?src=about#G1dfAwIrcfQhdoGMeXYq9sOeM55f_s0Tsx)]
<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2020-10-26T17:23:25.304Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36\&quot; etag=\&quot;9uHUE6TfoAkgGuvnI5mi\&quot; version=\&quot;13.7.9\&quot; type=\&quot;google\&quot;&gt;&lt;diagram id=\&quot;8CsTAdfkSBbSdxHSXRD7\&quot; name=\&quot;Page-1\&quot;&gt;7Vlbb6M4FP41eeyIe+CxzWVmpb2MlJVW2jeDHfAUMGPMJOmv32MwSYidSboN7U5nW6k1x8bG3/edc3yZuLNi+5GjKvuNYZJPHAtvJ+584jjBNIK/0rDrDK7vd4aUU9yZ7INhRZ+IMlrK2lBM6kFDwVguaDU0JqwsSSIGNsQ52wybrVk+HLVCKdEMqwTluvUvikXWWUNnerB/IjTN+pHtQE24QH1jNZM6Q5htjkzuYuLOOGOiKxXbGckldj0u3XvLM7X7D+OkFNe8gP9+jIqvWf7Fe8Lup82fy28fvTtFxjeUN2rC6mPFrkeAs6bERHZiTdyHTUYFWVUokbUboBxsmShyeLKhWAvOHvdIScua5vmM5Yy3vbnrNQmSZN/yqAZPo9iSQ6hPIlyQ7dm52nsEQXmEFUTwHTRRL3ieAl2pLlSPmwOFe16yI/rc3oiUbNJ91wdkoaDAfQbQtvccpO0bIB3bGK8tE9K2NXUj6PUB5TQtwZaTtbgR8NEQeNvXkbeNyI8F/LNwv4XCsU9C7JlwD53YDYLbAO1YlxXuva7C7Z9C4U5wovDorRVuwj3I5XRjKKTdvDvDmsEkjxkJvjasr7ir2+x7Dw0cr9oeKvtePrO6pjG8CdPzH+Dj0cSfYwT/oEvW8AQStRoIJtKNNRwfzEffdCIOSJCVLFacQU/1ZYHEKHlMW0n90YicluRCykk5whRonlMOSwXKpDA2pBZHVUevzf1FODf6sX0vf8fxY09XkxcY1OSNpSZXU9Pid5AEdGY9ULYSDeBUd8/3nKPdYltxydY5NpMdMIMJd6/gs4sOv8aXCO6EOrd9Q0ywiEsCE2sWCa0w1OKKc6vE5w94dG1DWLANRIZjERncPizYoSks/FIKwkuUv8T3AXhhiv49fyWT5A/IVqY+widEfgYYJI0UFvD3qqKgGMthjOobpv4b6MA98WfbMji0QQajpeXwtWSw2P4vg70MfPc/JoNIk8GdjOAFeoI0CBxA2LfiJnkkYp/DY97zJJsuZvJ9WqYyYcpCLVAJGP4MS7xrNzH+aEs867IXz3LWYOi9JhxmX1/lby8gy/lXZI3BjmHJZGRnvJ2PY3SulUAp+IsckRP0fmOdc3LY4hhi3SsToi9iz7nLO3US7Rzm7Z1EP2qUTjKffdaPCV7uGioZvK1jaCQEb07C9LJjLApE5SIOFRKUMq6rFg1LN2nPV+zxNfc4JlltGYttKu8SPqxztkkyxMWHoskFvcMsaYoWeyN/39vDayFzhES0P+G5RO90NHpNi/0z+3Kqdm0rwXh7B3IpsrVXOu2Wu73LaUvD0Ih4oi5wzNvsk0gYRcvlbGYmbt3+nDmzKRmXfY7BoXHbbuJwtPMXW1+prypYP+A6I0S831XE6cbZdXyNiVfdMTlXrLl/2FipkW/wQfDORbQcJxWOGSvh8XCr2tYdXU27i38A&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>

## Before you start
Please open a ticket with the template named as `Dataset Retraction`.

## Internal
Data and metadata that is stored within our immediate reach and deleting that data would not cause any consequence downstream.

### Amazon buckets/EC2 instance
Currently, we store contributor data in the cloud **before** and **while** brokering it. The places it needs to be retracted from are:

1. **HCA-util contributor areas**: Locate the area and delete it
    ```
    hca-util list -b
    hca-util upload select <area>
    hca-util delete -d
    ```
    
1. **Ingest upload area**: Go to the submission, locate the upload area and delete it
    ```
    aws s3 rm -r <full_s3_path_to_area>
    ```
    **Example**: `aws s3 rm -r s3://org-hca-data-archive-upload-prod/779ecf45-e930-459e-b87b-c89d3c4546c7/`
    
    <span style="color:red">**IMPORTANT NOTE**</span>: Please ensure the path you introduced points out to the specific area and not to the bucket, as you might risk deletion of all the upload areas otherwise. If you are unsure, please contact a dev and they will do it for you.
    
1. **EC2 instance**: If this data has been downloaded to the EC2 for some reason (e.g. validation), please make sure to remove it.

1. **Staging area**: 

### EBI Cluster

When archiving, if the data needed to be converted to bam files, it will be saved in the folder used for that purpose. To delete this data:
```
ssh noah-login
rm -r /nfs/production3/hca/<name_of_the_folder/
```

### Staging area

1. Run the script [here](https://github.com/ebi-ait/hca-ebi-dev-team/tree/master/scripts/map_ingest_uuid_to_staging_area) to get a mapping between the uuid of the entities in ingest and the file path in the staging area.
1. Use that file as the input for the following commands:
   ```
   cat <name_of_mapping_file> |  grep -E -o "gs:.*\.json" > file_paths.txt
   cat file_paths.txt | gsutil -m rm -I
   ```
   
   This will delete all the files in the staging area related to this dataset. Depending on how many there are, it may take up to an hour, so be patient. If, for any reason, it gets interrupted, it can be re-triggered with the same command, and it will just ignore the files that do not exist.
   

### Spreadsheet

The metadata spreadsheet can be in many different locations. Please make sure you delete each and every copy that you have:

1. Google drive folder: Locate the project folder under `brokering` and delete it in google drive.
1. Email
   1. Head to the [Wrangler team Google group](https://groups.google.com/a/data.humancellatlas.org/g/wrangler-team) and delete any email thread that may contain the spreadsheet.
   1. Send an email to the <a href="mailto:wrangler-team@data.humancellatlas.org?subject=[URGENT]%20Dataset%20retraction&body=To%20whom%20it%20may%20concern%2C%0A%0AWe%20have%20been%20warned%20about%20the%20retraction%20of%20the%20dataset%20%22%3Cshortname_of_dataset%3E%22.%20%0A%0AI%20kindly%20ask%20everyone%20in%20this%20group%20to%20delete%20their%20own%20copy%20of%20the%20following%20emails%3A%0A%0A-%20%3Ctitle_of_email_thread%3E%0A%28more%20if%20necessary%29%0A%0AAnd%20any%20local%20copy%20they%20might%20have%20of%20the%20metadata%20spreadsheet%0A%0AMany%20thanks%20for%20your%20cooperation%0A%0ABest%20regards%2C%0A%0A%3CWrangler%20name%3E">wrangler team</a>
   1. Delete your own local copies of the thread in your mail apps.
1. Please ask for a dev to delete the **copy of the spreadsheet associated with the submission** in the ingest database.

### Ingest UI

Metadata and data can be found in the ingest submission. If following the steps, the data and the metadata spreadsheet should already be removed, but there's still the metadata in the database.

**Before deleting the submission**, please remember to retrieve the following:
- BioStudies accession
- ENA study/project accession
- Ingest project/submission UUID
- DSP submission UUID

Once these have been retrieved, you can proceed to ask a dev to delete the submission and the project, where applicable.

### Ingest metadata archiver
[WIP - Need dev input on this one, not sure how to delete the metadata here (Although I am not sure if it needs to be deleted as it's not publicly accessible)]


### DSP
While not completely internal, we have the ability to update the BioSamples submission within DSP.

The steps are:
1. Locate the DSP submission UUID following the instructions on point three of [this document's section](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/archiving_SOP.html#using-the-service)
1. Remove all metadata within the BioSamples entities. Just leave the description field with an update:
   ```
   Unfortunately, this metadata can't be reached as it has been withdrawn from public domain.
   ```
   And update the release date for 100 years into the future.
1. Update the submission.

[SCRIPT NEEDED TO DO THIS]

Submission information does not need to be removed from here as it's not publicly accessible.

## External
Depending on the route the dataset took on the system, there might be data and metadata that needs to be retracted from sources external to the ingestion team.

### DCP2

- **Pipelines team**

- **Terra repository**

- **Data browser**

Please contact them following <a href="mailto:dcp@data.humancellatlas.org?subject=[URGENT]%20Dataset%20retraction&body=Dear%20all%2C%0A%0AWe%20have%20been%20warned%20about%20the%20following%20dataset%20being%20retracted%20from%20public%20access%3A%20%22%3Cshortname_of_dataset%22%2C%20with%20project%20UUID%20%22%3Cproject_uuid%3E%22.%0A%0APlease%20delete%20any%20copies%20of%20the%20data%20and%20metadata%20that%20you%20might%20have%20on%20your%20system.%0A%0ADon%27t%20hesitate%20contacting%20the%20wrangler%20team%20if%20you%20have%20any%20further%20questions.%0A%0ABest%20regards%2C%0A%0A%3CWrangler%20name%3E">this email template</a>

### Archives
With the following procedures on archiving, the dataset might be in many different places:

- **ENA**: Please use the <a href="mailto:ena-helpdesk@ebi.ac.uk?subject=ENA%20Dataset%20retraction&body=To%20whom%20it%20may%20concern%2C%0A%0AWe%20have%20been%20warned%20about%20the%20following%20dataset%20being%20retracted%20from%20public%20access%3A%20%22%3CENA_study_accession%3E%22%0A%0AWe%20were%20responsible%20for%20brokering%20the%20dataset%20into%20the%20ENA%20database%2C%20so%20we%20are%20kindly%20asking%20if%20you%20could%20delete%20the%20data%20and%20metadata%20pertaining%20to%20this%20study%20from%20your%20end.%0A%0AWe%20have%20cc%27ed%20the%20original%20author%28s%29%20in%20this%20email.%0A%0ABest%20regards%2C%0A%0A%3CWrangler%20name%3E">email template provided</a> to contact ENA helpdesk. When possible, please CC the contributor that asked for the retraction of the dataset.
- **ArrayExpress**: Please use the <a href="mailto:arrayexpress@ebi.ac.uk?subject=AE%20Dataset%20retraction&body=To%20whom%20it%20may%20concern%2C%0A%0AWe%20have%20been%20warned%20about%20the%20following%20dataset%20being%20retracted%20from%20public%20access%3A%20%22%3CArraExpress_project_accession%3E%22%0A%0AWe%20were%20responsible%20for%20brokering%20the%20dataset%20into%20ArrayExpress%2C%20so%20we%20are%20kindly%20asking%20if%20you%20could%20delete%20the%20data%20and%20metadata%20pertaining%20to%20this%20study%20from%20your%20end.%0A%0AWe%20have%20cc%27ed%20the%20original%20author%28s%29%20in%20this%20email.%0A%0ABest%20regards%2C%0A%0A%3CWrangler%20name%3E">email template provided</a> to contact AE directly. If this dataset has been included in SCEA, please also add a line for them to contact SCEA.
- **BioSamples**: Please ask a dev to remove all the metadata from the BioSamples entities associated with this project.
- **BioStudies**: Usually the project-level metadata is not restricted, but there might be cases where the contributor may want to get everything wiped out from the public domain. In that case, please contact BioStudies Helpdesk with the <a href="mailto:biostudies@ebi.ac.uk?subject=BioStudies%20Dataset%20retraction&body=To%20whom%20it%20may%20concern%2C%0A%0AWe%20have%20been%20warned%20about%20the%20following%20dataset%20being%20retracted%20from%20public%20access%3A%20%22%3CBioStudies_project_accession%3E%22%0A%0AWe%20were%20responsible%20for%20brokering%20the%20dataset%20into%20BioStudies%2C%20so%20we%20are%20kindly%20asking%20if%20you%20could%20delete%20the%20metadata%20pertaining%20to%20these%20donors%2Fsamples%20on%20your%20end.%0A%0AWe%20have%20cc%27ed%20the%20original%20author%28s%29%20in%20this%20email.%0A%0ABest%20regards%2C%0A%0A%3CWrangler%20name%3E">email template provided</a>

## Other

### Email templates
Please modify the templates with the dataset-specific details before sending it.

#### Wrangler-team email
Click on the following link to send the email: <a href="mailto:wrangler-team@data.humancellatlas.org?subject=[URGENT]%20Dataset%20retraction&body=To%20whom%20it%20may%20concern%2C%0A%0AWe%20have%20been%20warned%20about%20the%20retraction%20of%20the%20dataset%20%22%3Cshortname_of_dataset%3E%22.%20%0A%0AI%20kindly%20ask%20everyone%20in%20this%20group%20to%20delete%20their%20own%20copy%20of%20the%20following%20emails%3A%0A%0A-%20%3Ctitle_of_email_thread%3E%0A%28more%20if%20necessary%29%0A%0AAnd%20any%20local%20copy%20they%20might%20have%20of%20the%20metadata%20spreadsheet%0A%0AMany%20thanks%20for%20your%20cooperation%0A%0ABest%20regards%2C%0A%0A%3CWrangler%20name%3E">Email the wrangler team</a>

```
To whom it may concern,

We have been warned about the retraction of the dataset "<shortname_of_dataset>". 

I kindly ask everyone in this group to delete their own copy of the following emails:

- <title_of_email_thread>
(more if necessary)

And any local copy they might have of the metadata spreadsheet

Many thanks for your cooperation

Best regards,

<Wrangler name>
```

#### DCP team
Click on the following link to send the email: <a href="mailto:dcp@data.humancellatlas.org?subject=[URGENT]%20Dataset%20retraction&body=Dear%20all%2C%0A%0AWe%20have%20been%20warned%20about%20the%20following%20dataset%20being%20retracted%20from%20public%20access%3A%20%22%3Cshortname_of_dataset%22%2C%20with%20project%20UUID%20%22%3Cproject_uuid%3E%22.%0A%0APlease%20delete%20any%20copies%20of%20the%20data%20and%20metadata%20that%20you%20might%20have%20on%20your%20system.%0A%0ADon%27t%20hesitate%20contacting%20the%20wrangler%20team%20if%20you%20have%20any%20further%20questions.%0A%0ABest%20regards%2C%0A%0A%3CWrangler%20name%3E">Email the DCP</a>
```
Dear all,

We have been warned about the following dataset being retracted from public access: "<shortname_of_dataset", with project UUID "<project_uuid>".

Please delete any copies of the data and metadata that you might have on your system.

Don't hesitate contacting the wrangler team if you have any questions.

Best regards,

<Wrangler name>
```

### ENA
Click on the following link to send the email: <a href="mailto:ena-helpdesk@ebi.ac.uk?subject=ENA%20Dataset%20retraction&body=To%20whom%20it%20may%20concern%2C%0A%0AWe%20have%20been%20warned%20about%20the%20following%20dataset%20being%20retracted%20from%20public%20access%3A%20%22%3CENA_study_accession%3E%22%0A%0AWe%20were%20responsible%20for%20brokering%20the%20dataset%20into%20the%20ENA%20database%2C%20so%20we%20are%20kindly%20asking%20if%20you%20could%20delete%20the%20data%20and%20metadata%20pertaining%20to%20this%20study%20from%20your%20end.%0A%0AWe%20have%20cc%27ed%20the%20original%20author%28s%29%20in%20this%20email.%0A%0ABest%20regards%2C%0A%0A%3CWrangler%20name%3E">Email ENA</a>
```
To whom it may concern,

We have been warned about the following dataset being retracted from public access: "<ENA_study_accession>"

We were responsible for brokering the dataset into the ENA database, so we are kindly asking if you could delete the data and metadata pertaining to this study from your end.

We have cc'ed the original author(s) in this email.

Best regards,

<Wrangler name>
```

### ArrayExpress
Click on the following link to send the email: <a href="mailto:arrayexpress@ebi.ac.uk?subject=AE%20Dataset%20retraction&body=To%20whom%20it%20may%20concern%2C%0A%0AWe%20have%20been%20warned%20about%20the%20following%20dataset%20being%20retracted%20from%20public%20access%3A%20%22%3CArraExpress_project_accession%3E%22%0A%0AWe%20were%20responsible%20for%20brokering%20the%20dataset%20into%20ArrayExpress%2C%20so%20we%20are%20kindly%20asking%20if%20you%20could%20delete%20the%20data%20and%20metadata%20pertaining%20to%20this%20study%20from%20your%20end.%0A%0AWe%20have%20cc%27ed%20the%20original%20author%28s%29%20in%20this%20email.%0A%0ABest%20regards%2C%0A%0A%3CWrangler%20name%3E">Email AE</a>

```
To whom it may concern,

We have been warned about the following dataset being retracted from public access: "<ArraExpress_project_accession>"

We were responsible for brokering the dataset into ArrayExpress, so we are kindly asking if you could delete the data and metadata pertaining to this study from your end.

We have cc'ed the original author(s) in this email.

Best regards,

<Wrangler name>
```

### BioStudies
Click on the following link to send the email: <a href="mailto:biostudies@ebi.ac.uk?subject=BioStudies%20Dataset%20retraction&body=To%20whom%20it%20may%20concern%2C%0A%0AWe%20have%20been%20warned%20about%20the%20following%20dataset%20being%20retracted%20from%20public%20access%3A%20%22%3CBioStudies_project_accession%3E%22%0A%0AWe%20were%20responsible%20for%20brokering%20the%20dataset%20into%20BioStudies%2C%20so%20we%20are%20kindly%20asking%20if%20you%20could%20delete%20the%20metadata%20pertaining%20to%20these%20donors%2Fsamples%20on%20your%20end.%0A%0AWe%20have%20cc%27ed%20the%20original%20author%28s%29%20in%20this%20email.%0A%0ABest%20regards%2C%0A%0A%3CWrangler%20name%3E">Email BioStudies</a>

```
To whom it may concern,

We have been warned about the following dataset being retracted from public access: "<BioStudies_project_accession>"

We were responsible for brokering the dataset into BioStudies, so we are kindly asking if you could delete the metadata pertaining to these donors/samples on your end.

We have cc'ed the original author(s) in this email.

Best regards,

<Wrangler name>
```