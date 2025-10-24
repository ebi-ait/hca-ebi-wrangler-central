---
layout: default
title: hca-util tool
nav_order: 1
parent: Accessing upload area
grand_parent: Tools
---

EBI team has created a very handy aws-wrapper cli tool to upload data into the appropriate bucket called [hca-util](https://github.com/ebi-ait/hca-util). 

Using this we can:
- create an hca-util upload area
- upload files into an upload area
- list existing files of an upload area
- delete files from an upload area
- download files from an upload area
- sync files to a submission upload area

You should have a wrangler account for AWS, but if you don't please ask a developer to create one for you.

In order to use `hca-util` as an admin please use the following [guide](https://github.com/ebi-ait/hca-documentation/wiki/How-to-administrate-upload-areas-and-transfer-data-using-hca-util).

Contributors are also able to upload data using `hca-util` via this [guide](https://ebi-ait.github.io/hca-metadata-community/contributing/uploading-data.html).