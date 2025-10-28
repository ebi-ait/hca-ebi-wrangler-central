---
layout: default
title: Wrangling Project Management
parent: Introduction
grand_parent: SOPs
has_children: false
nav_order: 1
last_modified_date: 23/10/2025
---

# Wrangling Project Management

When working with new projects we need to be sure that we track progress in a consistent way, so all team members can review a project's status. Two main tracking systems exist:
1. Ingest project
    1. Add the project to Ingest 
        * Change `wrangling status` to 'in progress'
        * Ensure you are listed as the `primary_wrangler`
1. Github project issue
    1. Create a [project tracker ticket](https://github.com/ebi-ait/hca-ebi-wrangler-central/issues/new?template=published_project_tracker.md) to track dataset progress should be created in the `hca-ebi-wrangler-central` repo 
        * Add \[uuid\]\(ingest_project_link\) in the project ticket
    1. Create a new folder to store the project metadata in the [Brokering drive](https://drive.google.com/drive/folders/118kh4wiHmn4Oz9n1-WZueaxm-8XuCMkA)
        * Add link to Brokering folder in the project ticket
    1. Add additional links:
        * If project is related to a published manuscript (pre-print or peer-reviewed), add the manuscript __DOI__ and/or a link to any previously __archived data__
        * If project is coming from Integration teams' Tier 1 metadata collection, add the __study name__ as listed in the HCA Altas Tracker

## Tracking wrangling progress

Wrangling progress is tracked primarily through movement of the `project tracker ticket` through the status on the [Dataset wrangling status](https://github.com/orgs/ebi-ait/projects/12/) Github Projects Board. 

| Status            | When                                   | Explanation                                                                                                                                 |
|:---------------------|:----------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| Todo      | When created or if project needs update          | Issues should be placed here when they are created but before a wrangler actively starts working on it or if project requires some kind of update |
| Stalled             | If project becomes stuck               | If project spends more than 2 weeks with no progress, the ticket should be moved here and label applied to indicate reason  |
| Wrangling           | When in progress                       | The primary wrangler moves the tracker ticket here when they have started working on it |
| Review | When review starts                     | The secondary wrangler moves the tracker ticket here when they start reviewing |
| Verify            | When finished                          | The primary wrangler moves the ticket here to indicate the project is exported to the DCP and is waiting to be verified.  |
| Done | When project has been verified in the data browser | The primary wrangler moves the ticket here to indicate that it has been verified in the data browser. |


[Labels](https://github.com/ebi-ait/hca-ebi-wrangler-central/labels) are also applied to tickets to provide further information about the ticket. Definitions for each label and when they should be applied can be [found here](https://github.com/ebi-ait/hca-ebi-wrangler-central/labels).


## Updating project
Once the wrangling is proceeding:
- tick the boxes in the github issue
- add wrangling notes as comments in ticket, recording errors encountered or modeling choices and their explanation
- move ticket in appropriate status
- update labels in ticket
- update `Wrangler Notes` in Admin tab in ingest

When submission is completed, add appropriate __Release label__ in github issue (for example [release 55](https://github.com/ebi-ait/hca-ebi-wrangler-central/issues?q=state%3Aopen%20label%3A%22Release%2055%22)) so you can easily retrieve all dataset issues for each release.

### Note
If project is Managed Access avoid adding sensitive (meta)data and links (hca-util upload area `uuid`) in the (public) github repository. 

Instead record the hca-util `uuid` in a Google document in the Brokering [folder](https://drive.google.com/drive/folders/118kh4wiHmn4Oz9n1-WZueaxm-8XuCMkA) and allow only authorised users to view it.