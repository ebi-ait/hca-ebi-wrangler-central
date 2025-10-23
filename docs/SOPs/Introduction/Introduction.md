---
layout: default
title: Introduction
nav_order: 1
parent: SOPs
has_children: true
---

# Introduction

Welcome to the team! Here you can find some guidelines on how to get started in the wrangling process.  
Be sure to check the [onboarding document](/hca-ebi-wrangler-central/ebi-wrangler-onboarding) first.

As of 2025, the wrangling process starts from defining the consent type.

```mermaid
flowchart TD
    subgraph dca ["Consent type"]
    direction TB
    MA["Managed Access (MA) DCA"]
    OA["Open Access (OA) DCA"]
    end
    
    subgraph metadata [gather metadata]
    direction LR
    P1["Published contribution"]
    P2["Unpublished contribution"]
    P3["Tier 1 metadata"]
    HMS("HCA Metadata spreadsheet")
    P1--"wrangle from publication"-->HMS
    P2--"contributor fills spreadsheet"-->HMS
    P3--"convert tier 1 to dcp spreadsheet"-->HMS
    end

    subgraph proj ["project managment"]
    direction TB
    D1["Create github ticket"]
    D2["Create ingest project"]
    end

    subgraph data [gather data]
    direction RL
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
    C3 --upload--> I2

    subgraph import [staging area]
    M1["Import form filled"]
    M2["Monitor TDR validation"]
    I5 --> M1
    end

    dca --dca signed--> proj --> data
    proj --> metadata

    click M2 href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Introduction/access_tera.html" "Access TDR SOP"
```

