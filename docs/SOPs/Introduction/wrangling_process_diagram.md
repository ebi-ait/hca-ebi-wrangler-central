---
layout: default
title: Wrangling Process Diagram
nav_order: 2
parent: SOPs
has_children: true
---

# Wrangling Process Diagram

As of 2025, once a dataset has been selected to be wrangled, the wrangling process starts from defining the consent type.
> For a version with clickable document links, visit the GitHub site https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/docs/SOPs/Introduction/wrangling_process_diagram.md
> 
> Github Pages does not allow `mermaid` clickable links

```mermaid
flowchart TD
    subgraph first [first contact]
    P1["Published/ Unpublished<br>contribution"]
    end

    subgraph dca [<a href='https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#consent-type'>consent type</a>]
    MA["Managed Access (MA) DCA"]
    OA["Open Access (OA) DCA"]
    MA ~~~ OA
    end
    
    subgraph proj [<a href='https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/wrangling_project_management.html'>project managment</a>]
    D1["Create github ticket"]
    D2["Create ingest project"]
    D1 ~~~ D2
    end

    subgraph metadata [<a href='https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#gather-metadata'>gather metadata</a>]
    HMS("HCA Metadata spreadsheet")
    end

    subgraph data [<a href='https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#gather-data'>gather data</a>]
    C1["Archives"]
    C2["Contributor"]
    C3["hca-util upload area"]
    C1 --"upload"--> C3
    C2 --"upload"--> C3
    end

    subgraph ingest [<a href='https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#submission-process-in-ingest'>ingest submission process</a>]
    I1["Create submission"]
    I2["Validate data/ metadata"]
    I3["Validate graph"]
    I4["Secondary review"]
    I5["Submit"]
    I1 --> I2
    I2 --> I3 --> I4 --> I5 
    I4 --> I2
    end

    subgraph import [<a href='https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/access_tera.html'>staging area</a>]
    M1["Export"]
    M2["Import form filled"]
    M3["Monitor TDR validation"]
    I5 --> M1
    end

    C3 --sync--> I2
    first --> dca
    dca-->proj--> metadata
    HMS--"fill spreadsheet"--> I1
    proj-->data

    click MA href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Managed_access/Managed_access.html" "Consent type"
    click C1 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#gathering-data" "Gathering data"
    click C2 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#data-upload-contributor" "Data upload contributor"
    click C3 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/tools/Accessing_upload_area/hca_util.html" "hca-util"
    click D1 href "https://github.com/ebi-ait/hca-ebi-wrangler-central/issues" "wrangler repo"
    click D2 href "https://contribute.data.humancellatlas.org/" "ingest site"
    click HMS href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Metadata_spreadsheet/HCA_Metadata_Spreadsheet_Guide_Wranglers.html" "HCA metadata spreadsheet guide"
    click I1 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#create-submission" "Create ingest submission"
    click I2 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#metadata-validation" "Validate data/metadata"
    click I3 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#experimental-graph-validation" "Validate graph"
    click I4 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/secondary_review_SOP.html" "Secondary review SOP"
    click I5 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#completing-the-submission" "Completing the submission SOP"
    click M1 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#export" "Export SOP"
    click M2 href "https://docs.google.com/forms/d/e/1FAIpQLSeokUTa-aVXGDdSNODEYetxezasFKp2oVLz65775lgk5t0D2w/" "Import form"
    click M3 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/access_tera.html" "Access TDR SOP"
```

