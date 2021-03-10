---
layout: default
title: Exporting SOP
parent: Wrangling datasets SOP
grand_parent: SOPs
last_modified_date: 13/01/2020
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>
# Exporting Datasets SOP
{: .no_toc }

## Background
{: .no_toc }

This SOP aims to describe exporting.

## Table of contents
{: .no_toc .text-delta }

This describes the process for exporting completed projects or updated projects to the DCP

## Table of contents
{: .no_toc .text-delta }


1. As soon as a dataset is ready for export the wrangler should hit the submit button in the UI to trigger export and note the project UUID.
* Current mechanism: Wrangler retrieves the project UUID from the URL when viewing the project in the ingest browser.
2. The submitting wrangler checks export is complete.
* Current mechanism: wrangler checks status in the UI, will change from exporting to exported. (This will take ~1-4 hours for most projects)
* If export is “stuck” in exporting for more than 4 hours, Notify the ingest operations developer via the dcp-ops slack channel notifying (@hca-ingest-dev) and providing the project UUID so they can review the logs and work out what has happened. They will work with the wrangler to resolve this and re-export if necessary.
3. The Broad data import team are notified of successful export 
* Current mechanism: The submitting wrangler submits the [request for import form] (https://docs.google.com/forms/d/e/1FAIpQLSeokUTa-aVXGDdSNODEYetxezasFKp2oVLz65775lgk5t0D2w/viewform) and notifies the import team by messaging @monster-ops in the #dcp-ops Slack channel.
4. The submitting wrangler is notified that import and snapshot has been successful or if there are issues for EBI to investigate
* Current mechanism: Broad data import team will notify via slack in the dcp-ops channel slack, notifying @Hannes and @Trevor Heathorn when import and snapshot has been successful or if issues are found and pass on to the browser team.
5. UCSC Browser team will notify submitting wrangler and Broad team when indexed and in the browser or if issues are encountered.
* Current mechanism: Via slack in the dcp-ops channel notifying (who?) when a dataset is in the browser or if there was any issue with indexing.
6. When a dataset is available in the browser, the wrangler will do a final check that everything looks ok and notify @here on the data-ops channel. 
7. If issues occur at any point then corrections are made as updates and then re-exported. 
* Current mechanism: In order to re-export, the wrangler will notify the ingest developer on operations to reset the dataset state from exported to valid.
* The ingest developer should also delete any contents of the project staging area in the staging bucket from the failed export. 
8. Wrangler will trigger export by hitting submit and following steps 2-7

This is likely to evolve as we go, so please note issues with completing this process so we can improve it.
