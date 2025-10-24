---
layout: default
title: Wrangling Process Diagram
nav_order: 2
parent: SOPs
has_children: true
---

As of 2025, once a dataset has been selected to be wrangled, the wrangling process starts from defining the consent type.
> For a version with clickable document links, visit the GitHub site https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/docs/SOPs/Introduction/wrangling_process_diagram.md
> 
> Github Pages does not allow `mermaid` clickable links

```mermaid
flowchart TD
    subgraph first [first contact]
    P1["Published/ Unpublished<br>contribution"]
    end

    subgraph dca ["Consent type"]
    MA["Managed Access (MA) DCA"]
    OA["Open Access (OA) DCA"]
    end
    
    subgraph metadata [gather metadata]
    HMS("HCA Metadata spreadsheet")
    P1--"fill spreadsheet"-->HMS
    end

    subgraph proj ["project managment"]
    D1["Create github ticket"]
    D2["Create ingest project"]
    end

    subgraph data [gather data]
    C1["Archives"]
    C2["Contributor"]
    C3["hca-util upload area"]
    C1 --> C3
    C2 --> C3
    end

    subgraph ingest [ingest submission process]
    I1["Create submission"]
    I2["Validate data/ metadata"]
    I3["Validate graph"]
    I4["Secondary review"]
    I5["Export"]
    HMS --> I1
    I1 --> I2
    I2 --> I3 --> I4 --> I5 
    I4 --> I2
    end

    subgraph import [staging area]
    M1["Import form filled"]
    M2["Monitor TDR validation"]
    I5 --> M1
    end

    C3 --sync--> I2
    first --> dca
    dca --dca signed--> proj --> data
    proj --> metadata

    click MA href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#consent-type" "Consent type"
    click proj href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/wrangling_project_management.html" "Project managment"
    click C1 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#gathering-data" "Gathering data"
    click C2 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/dataset_wrangling_SOP.html#data-upload-contributor" "Data upload contributor"
    click C3 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/tools/Accessing_upload_area/hca_util.html)" "hca-util"
    click M2 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/access_tera.html" "Access TDR SOP"
```

