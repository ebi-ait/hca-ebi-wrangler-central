---
layout: default
title: BAM upload SOP
parent: SOPs
---

# BAM upload SOP

## Purpose of this SOP
Showcase how convert raw data (fastq) into unaligned BAM and submit it through the DSP.

# Table of contents
1. [Setup and requirements](#1)
1. [Converting Fastq files to BAM](#2)
1. [Uploading data to a DSP submission](#3)
   - [Locate the submission ID](#3a)
   - [Upload the files](#3b)
   - [Check on the status of the files](#3c)
   - [Resume file upload](#3d)

# Setup and requirements <a name="1"></a>
- [tus.py](https://github.com/cenkalti/tus.py) installed in the place you want to upload from.
   - In order to install the package in the EC2, please set up a virtual environment first.
- fastq_to_bam conversor from [this repository](https://github.com/HumanCellAtlas/fastq_utils). This utilities are already present in the EC2 instance under the directory `/home/ubuntu/fasq_utils`
- Have set up your [AAP credentials](https://submission.ebi.ac.uk/api/docs/guide_accounts_and_logging_in.html)

# Converting Fastq files to BAM <a name="2"></a>

1. Download the fastq files from the s3 bucket into the folder created for that area.
1. Export the path to the path the binaries for the `fastq_utils` tools are (e.g, in the EC2 instance the command would be `export PATH=$PATH:/home/ubuntu/fastq_utils/bin`
1. For each set of R1/R2(/I1/I2) file, run the following command: `fastq2bam -s <schema> -b <path/to/out_bam> -1 <R1.fastq.gz> [ -2 <R2.fastq.gz> -3 <I1.fastq.gz> -4 <I2.fastq.gz>]`
     - Currently it only supports the following schemas: `drop-seq`, `10xV1`, `10xV1i`, `10xV1a`, `10xV2`

If the reads are in the same order across the files, it should exit successfully and create the bam file at the desired directory. If not, you should use the util `fastq_filterpair` from the same repository.

# Uploading data to a DSP submission <a name="3"></a>

Once you have all the bam files:

**Locate the submission ID** <a name="3a"></a>
1. Generate a token (Expires every hour): `curl -u <your_aap_username>:<your_aap_password> https://api.aai.ebi.ac.uk/auth`

1. Run `curl 'https://submission.ebi.ac.uk/api/user/submissions' -i -H 'Accept: application/hal+json' -H 'Authorization: Bearer '"$TOKEN"''`, replacing `$TOKEN` with the token generated in step 1.
    - This will return a list of all available submissions to the user. Inside the `['_links']['self']['href']` field you will find something like `"https://submission.ebi.ac.uk/api/submissions/96a514df-e72b-4e04-8d66-86881cad8ddd"`. The ID after the last slash is the submission ID.

**Upload the files** <a name="3b"></a>

Go to the directory the files are in and run the following command: `tus-upload --chunk-size 1024000 --metadata name <destination_file_name.cram> --metadata submissionID '<your_submission_id>' --metadata jwtToken ‘<your_jwt_token>' '<source_test_filename>' https://submission.ebi.ac.uk/files/`
  - Replace the chunk size with the size (in Bytes) you're most confortable with. Usually, bigger chunks mean higher upload speeds but worse for unstable connections and vice versa.
  - Replace `<destination_file_name.cram` for the filename of the bam file. This is the name by which it will be uploaded to ENA.
  - Replace `<your_submission_id>` by the submission ID retrieved in point 2.
  - Replace `<your_jwt_token>` with the token obtained in point 1.
  - Replace `<source_test_filename>` with the local filename.
        

**Check on the status of the files** <a name="3c"></a>

Run `curl 'https://submission.ebi.ac.uk/api/files/search/by-submission?submissionId=<your_submission_id>' -i -H 'Accept: application/hal+json' -H 'Authorization: Bearer '"$TOKEN"''`
  - Replace `<your_submission_id>` with the ID of the submission you're interested in.
  - Replace `$TOKEN` with the token generated in point 1.

It should return something like this (But with more files):
```
{'_embedded': {'files': [{'_embedded': {'validationResult': {'_links': {'self': {'href': 'https://submission.ebi.ac.uk/api/validationResults/<submission_uuid>{?projection}',
                                                                                 'templated': True}},
                                                             'overallValidationOutcomeByAuthor': {'FileContent': 'Pass',
                                                                                                  'FileReference': 'Pass'},
                                                             'validationStatus': 'Complete'}},
                          '_links': {'file': {'href': 'https://submission.ebi.ac.uk/api/files/<file_uuid>'},
                                     'self': {'href': 'https://submission.ebi.ac.uk/api/files/<file_uuid>'},
                                     'validationResult': {'href': 'https://submission.ebi.ac.uk/api/files/<file_uuid>/validationResult'}},
                          'checksum': 'a73b8b6816ff34552d0fb9ddc1758784',
                          'createdBy': 'Enrique Sapena Ventura',
                          'filename': '5386STDY7537944.bam',
                          'generatedTusId': '57dbdfa7f3eebd4510028a4b798c3d3b',
                          'status': 'READY_FOR_ARCHIVE',
                          'submissionId': '796306f2-e411-47bc-87fd-22999e55a7ef',
                          'targetPath': '/fire/staging/subs/upload/prod/ready_to_agent/7/9/<file_uuid>/5386STDY7537944.bam',
                          'totalSize': 48574997153,
                          'uploadFinishDate': '2020-02-14T01:49:24.194',
                          'uploadPath': '/fire/staging/subs/upload/prod/ready_to_agent/7/9/<file_uuid>/5386STDY7537944.bam',
                          'uploadStartDate': '2020-02-13T17:54:56.505',
                          'uploadedSize': 48574997153}]},
 '_links': {'self': {'href': 'https://submission.ebi.ac.uk/api/files/search/by-submission?submissionId=796306f2-e411-47bc-87fd-22999e55a7ef&page=0&size=20'}},
 'page': {'number': 0, 'size': 20, 'totalElements': 1, 'totalPages': 1}}
```

You will get a **paginated** json response indicating the status of the files. If you want to check them all, you will have to follow the `['_links']['next']['href']` endpoint. There should be an indication on the response about the total hits if you just want to know how many files have been registered in the DSP.

**Resume file upload** <a name="3d"></a>

Find the file you want by following the steps described in the previous subsection. In the file you want to resume uploading (Should have an `UPLOADING` status) locate the `generatedTusId`.

Run `tus-resume --chunk-size <chunk_size> '<source_file>' https://submission.ebi.ac.uk/files/<generatedTusID> --header Authorization 'Bearer $TOKEN'`
  - Replace `<chunk_size>` with the size of the chunks (Explained in `Upload the files` section)
  - Replace `<source_file` with the filename of the file you want to continue uploading
  - Replace `<generatedTusID>` with the Tus ID for your file
  - Replace `$TOKEN` with the jwt Token generated previously
