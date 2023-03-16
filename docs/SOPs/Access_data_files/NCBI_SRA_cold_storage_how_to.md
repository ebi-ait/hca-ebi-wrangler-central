---
layout: default
title: NCBI cloud delivery SOP
parent: Access data files
grand_parent: SOPs
nav_order: 2
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

Data transfer from NCBI cold storage buckets using SRA cloud data delivery service
==================================================================================
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


Usually you can download sequence data files from the [ENA](https://www.ebi.ac.uk/ena/) Data Warehouse with the help of the script <https://github.com/ebi-ait/hca-ebi-wrangler-central/blob/master/src/move_data_from_insdc.py>.

If the data is not available from ENA, and you still need the original sequence data files (e.g. fastq files) submitted to the Sequence Read Archive (SRA), then you can try to use the SRA cloud data delivery service to obtain the source files from [NCBI cold storage buckets to HCA AWS buckets.](https://www.ncbi.nlm.nih.gov/sra/docs/data-delivery/)

You need to have your own [MyNCBI account](https://www.ncbi.nlm.nih.gov/myncbi/)
to use the SRA cloud delivery service. You can use your EBI email and Google account to set it up and sign in to your [MyNCBI account](https://www.ncbi.nlm.nih.gov/myncbi/).

There are limits of how much data you can request within a 30-day period from NCBI:
* Cold storage retrieval 30-day rolling window limit: 5.0 TB
* Cloud bucket delivery 30-day rolling window limit: 20.0 TB

### A. Create a destination bucket to receive data from NCBI cold storage

You need to set up a destination bucket (if it does not exist already) to receive data from the NCBI cloud delivery service.
First, log in to the **wrangler EC2 instance** via `ssh`.

* Create an AWS S3 destination bucket named `hca-ncbi-cloud-data` that you will need in step **D.2.**:

```
aws s3api create-bucket --bucket hca-ncbi-cloud-data --region us-east-1
```
You can check if the `s3://hca-ncbi-cloud-data` bucket exists and its content:
```
aws s3 ls --human-readable --summarize --recursive s3://hca-ncbi-cloud-data
```

### B. Log in to your MyNCBI account
The subsequent steps assume that you are logged in into your [MyNCBI account.](https://www.ncbi.nlm.nih.gov/myncbi/)
### C. Use the SRA Run Selector to find the study
Input an appropriate study accession (e.g. GEO) and [click search.](https://www.ncbi.nlm.nih.gov/Traces/study/)
Select the appropriate sequencing `Run` check boxes (e.g. all) in the leftmost column.
Under the `Cloud Data Delivery` section click `Deliver Data`.

You should be redirected to <https://www.ncbi.nlm.nih.gov/Traces/cloud-delivery/>.

### D. Initiate [cloud data delivery](https://www.ncbi.nlm.nih.gov/sra/docs/data-delivery/)

#### 1. Check if the list shows the desired runs.

#### 2. Choose destination bucket.
* Cloud provider: `AWS`
* Bucket name: `hca-ncbi-cloud-data`
* In the browser window, click `Copy` policy. Paste the copied json into a file named `policy.json`.
You need to add the new policy to bucket `s3://hca-ncbi-cloud-data`. To do that, first you need to `ssh` into the **wrangler EC2 instance**. You also need the new `policy.json` file on the EC2 in your working directory. You can create the `policy.json` file on the EC2 or transfer it there, whichever way you find it more convenient.
*
    - **in an EC2 terminal**: Add the policy to bucket `s3://hca-ncbi-cloud-data` using the command below:
```
aws s3api put-bucket-policy --bucket hca-ncbi-cloud-data --policy file://policy.json
```
*
    - **in an EC2 terminal**: You can check the bucket policy with this command:
```
aws s3api get-bucket-policy --bucket hca-ncbi-cloud-data --query Policy
```
* Go back to the **web interface** in a browser window and click `Add bucket` after you have added the access policy to the destination bucket.

#### 3. Select one or more source file types:
* Select the check-box for **FASTQ**

#### 4. Review, agree the terms and conditions and submit request.

* You should receive a confirmation email from NCBI with subject line *Processing your request to deliver XXX GB of data to hca-ncbi-cloud-data*.
    It may take up to 48 hours for SRA to deliver the data to our destination bucket. 

### E. File transfer
* You will receive an email *Completed your request to deliver XXX GB of data to hca-ncbi-cloud-data* upon data delivery.
* It is worth checking if NCBI transferred all the files that you expect. On the EC2 instance, check the number of transferred `fastq` files:

```
aws s3 ls --human-readable --summarize --recursive s3://hca-ncbi-cloud-data | grep -c fastq
```

### F. Move your files from the `hca-ncbi-cloud-data` bucket to the wrangler/contributor upload area

The `hca-ncbi-cloud-data` bucket is meant to be just a temporary staging area for the data files from NCBI. It is not safe to store your data there.
You need to set up a storage area for the transferred files using [hca-util](https://pypi.org/project/hca-util/).

The NCBI SRA cloud data delivery service will create directories in the `hca-ncbi-cloud-data` bucket named after SRA runs. You can parse the SRA Run identifiers from the NCBI service provided `sra_metadata.*.csv` file that came with the data files in the same bucket and use them as the DIRECTORYNAME in the following command to copy the files without the SRR directory structure:

```
aws s3 sync s3://hca-ncbi-cloud-data/DIRECTORYNAME s3://hca-util-upload-area/UUID
```

The UUID is the upload area uuid that you created for the files using [hca-util](https://pypi.org/project/hca-util/).

* Before clean-up, **please check if other people have data files in the area, so that you do not remove them accidentally**. To remove EVERY FILE in the `hca-ncbi-cloud-data` bucket you can use (**with care**) the following command:

```
aws s3 rm s3://hca-ncbi-cloud-data/ --recursive
```
The command above shall not remove the empty bucket and that is fine. However, you can not expect the bucket to persist, because S3 buckets believed to be non-essential are regularly deleted by dev operations during clean-ups.

* You can remove directories or files individually as follows:

```
aws s3 rm s3://hca-ncbi-cloud-data/directory_name --recursive
aws s3 rm s3://hca-ncbi-cloud-data/filename
```

* You can remove directories or files that follow a wildcard pattern as follows:

```
aws s3 rm s3://hca-ncbi-cloud-data/ --recursive --exclude * --include wildcard
```

   An example of this last operation would be:
   ```
   aws s3 rm s3://hca-ncbi-cloud-data/ --recursive --exclude "*" --include "SRR818047*"
   ```
   Which will delete all files that are in directories under the SRA run accession SRR818047* (In this case, deleted all the files for runs SRR8180470, SRR8180471, SRR8180472 and SRR8180473). 

