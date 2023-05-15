---
layout: default
title: Uploading files to an s3 bucket from the archives
parent: Download from archives
grand_parent: Tools
nav_order: 3
---
# Uploading files to an s3 bucket from the archives

## Pre-requisites and installation
- `virtualenv`
- [`aws`](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- `wget`
- Connect to the EC2, create a virtual environment and install the python dependencies:
  ```
  virtualenv -p python3.7 <name_of_env>
  source <name_of_env>/bin/activate
  wget https://raw.githubusercontent.com/ebi-ait/hca-ebi-wrangler-central/master/src/requirements.txt
  pip3 install -r requirements.txt
  ```
- Set up your default aws credentials:
   - Go to `~/.aws/`
   - `vim credentials`
   - Copy this at the top of the file:
   ```
   [default]
   aws_secret_access_key = <AWS_secret_key>
   aws_access_key_id = <AWS_access_key>
   ```
   Replacing the keys with your wrangler access and secret keys
   
## Usage

1. Connect to the EC2
1. Create an upload area using the [`hca-util`](https://github.com/ebi-ait/hca-documentation/wiki/How-to-administrate-upload-areas-and-transfer-data-using-hca-util) tool. 
1. `wget` the `move_data_from_indsc.py` script to your root directory in EC2
   ```
   wget https://raw.githubusercontent.com/ebi-ait/hca-ebi-wrangler-central/master/src/move_data_from_insdc.py
   ```
1. Activate your python>=3.6 virtual environment if not already active
    ```
    source <name_of_env>/bin/activate
    ```
1. Run the script:
   ```
   python3 move_data_from_insdc.py -s <study/project accession> -o s3://hca-util-upload-area/<upload_area_id> -t <number_of_threads>
   ```
1. Enjoy while your data gets loaded into the s3 area! If you are running into some errors, the default database accession is the SRA, so try the corresponding SRA accession as an input to the script.

## Notes

- Right now, even with a good amount of threads (>= 5) it takes about 5 hours to move 1 TB of data. It is best practice to [set up a virtual screen](#use-terminal-sessions-in-ec2-tmux-screen) and leave it running.
- The `output_path` (-o) argument can be pointed out to a local directory
- Some GEO datasets do not have all their data available in a fastq format. For those datasets, a warning pointing to which runs the script failed to retrieve information from will be issued.
