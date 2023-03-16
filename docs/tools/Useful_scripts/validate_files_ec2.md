---
layout: default
title: Validate files in ec2 
parent: Useful scripts
grand_parent: Tools
---

__Consider other option [check_fastq.py](https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/src/check_fastq.py)__

# Validating files on the ec2: fastq_info

TODO: Check whether we can do the syncing to ec2 currently

This is only needed if you need to validate the files manually for some reason, generally this should occur automatically once files are uploaded to the ingest upload bucket.

## Pre-requisites and installation

- fastq_info

Run the following command after ssh-ing into the EC2 instance:

```
export PATH=$PATH:/home/ubuntu/fastq_utils/bin
```

## Usage

Sync the files stuck in VALIDATING status from their S3 bucket to their corresponding folder on the EC2. 

```
aws s3 sync <s3 bucket URI> /data/<data-folder>/
```

Include only certain files using `--exclude` and `--include`:

```
aws s3 sync <s3 bucket URI> /data/<data-folder>/ --exclude "*" --include "SRR43*.fastq.gz"
```

Run `fastq_info` for a particular file:

```
fastq_info -r -s </path/to/fastq-file-name>
```

Response like this means that the file is valid:

```
zperova@ip-172-31-3-111:/data/zperova-fetal-heart-10x-staging-0$ fastq_info -r -s 10X109_2_S4_L001_I1_001.fastq.gz
fastq_utils 0.19.2
Skipping check for duplicated read names
CASAVA=1.8
410700000
------------------------------------
Number of reads: 410725632
Quality encoding range: 35 70
Quality encoding: 33
Read length: 9 9 9
OK
```

If the response contains the word ERROR, the file is unvalid.