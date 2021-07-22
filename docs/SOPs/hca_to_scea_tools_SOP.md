---
layout: default
title: HCA to SCEA Guide
parent: SOPs
last_modified_date: 28/04/2021
---

# HCA to SCEA Guide

_Please note: this is not a tool to generate a perfect set of SCEA idf and sdrf files automatically. It speeds up the process by part automation but manual curation is an important part of the process._

## Checking suitability for SCEA

Please refer to the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2) for information on dataset suitability for SCEA. As part of this suitability criteria, there are also guidelines on how HCA datasets should be split into separate SCEA projects, if needed. You can also check the SCEA team's [`data suitability guidelines`](https://github.com/ebi-gene-expression-group/expression-atlas-curation-guide/blob/master/pages/inclusion_criteria.md) document more thoroughly. Once you think that the dataset is suitable or if you have any doubts, double-check with the SCEA team on the AIT slack channel `#hca-to-scea`

## Converting HCA spreadsheets to SCEA MAGE-TAB

Please refer to the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2) for information on running the tool on the wrangler EC2 and on refining the tool outputs (idf and sdrf files).

## Validation of idf and sdrf files

Please refer to the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2) for information on validation of the idf and sdrf files.

## Handing over files to SCEA team

Please refer to the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2) for information on file handover to the SCEA team.

## Appendix

### Installing on your local machine

You will need python3 installed, if you don't have it, install from [Python's webpage](https://www.python.org/downloads/)

To install the tool on your local machine:

1. Clone the repository
   ```
   git clone https://github.com/ebi-ait/hca-to-scea-tools.git
   cd hca-to-scea-tools/
   ```
1. Install the application by running
   ```
   cd hca2scea-backend
   ./install.sh
   ```
Then once installed:

1. Run the tool: run the command-line tool with at least the minimum required arguments as described in the `hca-to-scea tools` repo [README](https://github.com/ebi-ait/hca-to-scea-tools#setting-the-environment-on-ec2). The tool should be run locally just as it would on EC2.
