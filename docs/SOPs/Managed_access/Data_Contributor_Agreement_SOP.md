---
layout: default
title: Data Contributor Agreement SOP
parent: Managed access
grand_parent: SOPs
nav_order: 2
last_modified_date: 30/05/2024
---

<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# Data Contributor Agreement SOP

This document explains how a wrangler registers a managed access project and helps fill out the data contributor agreement (DCA). See [here](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Managed_access/Data_Contributor_Agreement_explained.html) if you are unfamiliar with the DCA.

## Create a project in HCA Data Repository Ingest Service 
This step begins once the wranglers receive a submission request in the form of an email from the contributor. The contributor needs to provide the name and email address for the DCA signers.

1. Register a new project in ingest with minimal details. The only metadata needed is:
   1. Primary contact/data contributor information 
   2. Project title. If a title has been provided make sure there is no identifiable information in the project title. If no title was provided use the contributor name and amend with the title provided in the DCA once it’s signed.
   3. Data use restriction. Fill in the data_use_restriction as GRU-NCU, as the stricter of the Managed access options. 
   4. Make sure the project is not displayed on the catalogue.
2. Save the project to generate a project UUID. 
3. Forward the singer’s contact information to the HCA executive office so they can start the signing process
4. Let the contributors know that their details have been forwarded to the executive office and they will receive an email to sign the DCA shortly

## Fill in the DCA agreement
The designated wrangler receives an email to sign the DCA on DocuSign. No account is required for this.
1. Enter the project UUID from the step above
2. Sign as a Data Wrangler

## Complete DCA agreement
Once all parties have signed the DCA agreement, the data wrangler will receive a copy of the signed agreement.
1. Update the project title and data_use_restriction to reflect the DCA

We do not need to keep a signed copy of the DCA, the HCA executive office is keeping records for that.
For next steps of the Managed access submission process see [Managed access dataset - Pre-submission](https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Managed_access/Pre-submission_SOP.html)

