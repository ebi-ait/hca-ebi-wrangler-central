---
layout: default
title: HCA to SCEA Guide
parent: SOPs
last_modified_date: 23/12/2020
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# HCA to SCEA Guide
{: .no_toc }

_Please note: this is not a tool to generate a perfect set of SCEA idf and sdrf files automatically. It speeds up the process by part automation but manual curation is an important part of the process._

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Useful documents 

<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2020-10-07T14:41:24.371Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36\&quot; etag=\&quot;v8oPzvuX1tBEvZB6g7rV\&quot; version=\&quot;13.7.5\&quot; type=\&quot;google\&quot;&gt;&lt;diagram id=\&quot;FsEeLdDOj7soeLvYh2q5\&quot; name=\&quot;Page-1\&quot;&gt;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&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>

[Modify this diagram here](https://app.diagrams.net/?src=about#G1bP1jg52KXeVmd6HGmXxXRjfT2uEZtPDr)

### Checking suitability for SCEA

Please refer to the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2) for information on dataset suitability for SCEA. As part of this suitability criteria, there are also guidelines on how HCA datasets should be split into separate SCEA projects, if needed. You can also check the SCEA team's [`data suitability guidelines`](https://github.com/ebi-gene-expression-group/expression-atlas-curation-guide/blob/master/pages/inclusion_criteria.md) document more thoroughly. Once you think that the dataset is suitable or if you have any doubts, double-check with the SCEA team on the AIT slack channel `#hca-to-scea`

## Converting HCA spreadsheets to SCEA MAGE-TAB

Please refer to the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2) for information on running the tool on the wrangler EC2 and on refining the tool outputs (idf and sdrf files).

## Validation of idf and sdrf files

Please refer to the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2) for information on validation of the idf and sdrf files.

## Appendix

### Installing on your local machine

You will need python3 installed, if you don't have it, install from [Python's webpage](https://www.python.org/downloads/)

To install the tool on your local machine:

1. Clone the repository
   ```
   git clone https://github.com/ebi-ait/hca-to-scea-tools.git
   cd hca-to-scea-tools/

1. Install the application by running
   ```
   cd hca2scea-backend
   ./install.sh
   ```
Then once installed:

1. Run the tool: run the command-line tool with at least the minimum required arguments as described in the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2). The tool should be run locally just as it would on EC2.
