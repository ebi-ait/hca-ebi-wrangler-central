---
layout: default
title: GDPR_Guidelines
parent: Triage
grand_parent: SOPs
nav_order: 4
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# GDPR_Guidelines
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Purpose of this document

This document will serve to display our guidelines for GDPR and data protection restrictions when wrangling. 

## Summary diagram

```mermaid
graph TD
    A[What is the source of the project?]
    A -->|Published Paper| B{Does the project<br>have living donors?}
    A -->|Contributor<br>Communications| C{Is the project<br>archived?}
    C -->|Yes| B
    C -->|No| G{Does the project<br>have living donors?}
 
    B -->|Yes| E{"Is the data and metadata<br>open access in the public domain?<br>(ENA, AE, publication)"}
    B -->|No| F[We can curate it<br>with no worries]
    
    E -->|Yes| H[We can curate<br>whatever is in the public domain]
    E -->|No| R{Ask contributor<br>about consent they hold}
    
    R -->|Must be open acccess<br>with only these data?| I[Wrangle<br>only the open access<br>data & metadata:<br>project-level data<br>analysis protocols<br>and analysis files]
    R -->|consent<br>for more open data?| J[Contributor<br>can provide written consent<br>to release metadata<br>as open access]
    R -->|Must be managed access?| K[Follow the<br>Managed Access route<br>to archive<br>with controlled access]

    H --> L[Be aware of obtaining<br>extra metadata or data<br>on existing living donors<br>not publicly available<br>as that may be subject<br>to data protection]
    H -->|consent<br>for more open data?| J[Contributor<br>can provide written consent<br>to release metadata<br>as open access]
    
    G -->|Yes| M[Subject to GDPR/<br>data restrictions]
    G -->|No| N[Recommend ENA.<br>We can curate with no worries.]
    N -->C
    
    M --> O{Has the contributor explicitly<br>instructed us to archive<br>in open access database?}
    O -->|Yes| P[Confirm that the data<br>they are providing is open access,<br>then recommend ENA]
    O -->|No| Q[Recommend contributor<br>submits to EGA]

    P -->C
    Q -->C
    click K href "https://ebi-ait.github.io/hca-ebi-wrangler-central/SOPs/Managed_access/Managed_access.html" "MA SOP"
```

## Specific guidelines

GDPR concerns arise when dealing with living donors, as HCA sticks to a strict interpretation of the regulations. One of the first assessments a wrangler has to do when wrangling a dataset (contributor-led or publication-led) is to determine whether there are living donors or not, to comply with our GDPR restrictions. Those donors alive at the moment of sample collection are subjected to GDPR restrictions. Thus, deceased and pre-natal donors can be wrangled without taking these GDPR guidelines into consideration.

### Data 
When wrangling any kind of data or metadata related to living donors, wranglers can only ingest into the system data that is already in the public domain. Wranglers shoud **never ask for extra data**. Here by data we specifically refer to:

- Raw fastq files
- Raw gene expression matrices (TBD - discussion with Tony)
- Processed gene expression matrices (TBD - discussion with Tony)

When wrangling **contributor led** publications, wranglers cannot recommend or suggest the contributors to archive their data in an open database if living donors are involved. Wranglers are also not allowed to state to the contributors that they could take the data and metadata from an open database once it's published there, as it might lead the contributors to make their data publicly available. **HCA recommendation when dealing with living donors should always be managed access**

### Metadata
When wrangling from already **published projects**, wranglers should **never ask for extra donor metadata** if it involves living donors. Wranglers are allowed to take the information that the authors have made already of **public domain**. Wranlger may include previously unreleased metadata provided by the author only if the author gave  **written consent** for its public release as open access. ~~Moreover, to prevent low *k-anonymity* [^1] levels, wranglers should **avoid wrangling donor metadata when the project includes less than 5 living donors**. ~~

[^1]: A release of data is said to have the k-anonymity property if the information for each person contained in the release cannot be distinguished from at least k - 1 individuals whose information also appear in the release.
