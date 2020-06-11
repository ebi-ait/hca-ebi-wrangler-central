---
layout: default
title: Handy snippets
parent: Tools
---

# Handy code snippets
{: .no_toc }

Handy snippets that are useful to wranglers that don't quite fit elsewhere

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Downloading 10x files from archives

These instructions are for getting BAM files of primary sequence data from the ENA that represent 10X sequencing data and converting them to the original I1, R1, and R2 files using the 10X `bamtofastq` tool. Please note that this tool only works for 10X data, and even then only for data processed with CellRanger and LongRagner. See the https://support.10xgenomics.com/docs/bamtofastq[10X website] for more information about what data can be converted with this tool.

### Pre-requisites and installation

- wget
- bamtofastq

If you don't have `wget` installed on the machine where you want to download the files (it is on the EC2 already), you can find instructions how to install it with Homebrew for Mac https://www.cyberciti.biz/faq/howto-install-wget-om-mac-os-x-mountain-lion-mavericks-snow-leopard/[here].

To "install" `bamtofastq`, go to https://support.10xgenomics.com/docs/bamtofastq[10X’s website] and click "Download bamtofastq 1.1.2" to download the executable file to your local machine. There is no need to compile the tool. Simply move or copy the file to the machine where you want to use it (e.g. your home directory on the EC2), making sure to put it somewhere on your `$PATH` if you want to be able to call it from any folder.

### Usage

1. Find the project of interest in the ENA (can search by PRJN or SRP accession from GEO).
1. From the "Study" view showing all the experiments, copy the ftp URL to the "BAM File 1" for the run you want from the "Submitted files (FTP)" column. **Pro-tip: right-click "BAM File 1" and select "Copy link address" to get the URL**.
1. From wherever you want to temporarily store the files (e.g. EC2, another server), use `wget` to download the BAM file.

	wget <paste ftp URL>

1. After the BAM file has been downloaded, convert to fastq files using the `bamtofastq` tool.

	bamtofastq <downloaded_bam>.bam <name of a folder to put fastqs in>

1. By default, fastq files are generated with a max of 50M reads per file. If there are more reads, the files will be split across multiple sets of fastqs. It is recommended to avoid this (it means you'll have to concatenate them later) by using the `--reads-per-fastq` parameter. Below, the max reads per file is set to 500M: 

	bamtofastq --reads-per-fastq=500000000 <downloaded_bam>.bam <name of a folder to put fastqs in>

1. Bask in the joy of being able to get R1, R2, AND I1 files from BAMs


## Validating files on the ec2: fastq_info

TODO: Check whether we can do the syncing to ec2 currently

This is only needed if you need to validate the files manually for some reason, generally this should occur automatically once files are uploaded to the ingest upload bucket.

#### Pre-requisites and installation

- fastq_info

Run the following command after ssh-ing into the EC2 instance:

```
export PATH=$PATH:/home/ubuntu/fastq_utils/bin
```

#### Usage

Sync the files stuck in VALIDATING status from their S3 bucket to their corresponding folder on the EC2. 

```
aws s3 sync <s3 bucket URI> /data/<data-folder>/
```

Include only certain files using `--exclude` and `--include`:

```
aws s3 sync <s3 bucket URI> /data/<data-folder>/ --exclude "*" --includ "SRR43*.fastq.gz"
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

## Generating submission summary report: generate_summary.py

TODO: see if this is still useful to wranglers

This tool generates two summary metadata reports for a submission/project. The first report counts the number specific entities in the submission/project. Currently, the entities counted is hard-coded and not complete. The second report contains a summary of other useful metadata pieces that can be used to populate projects pages. It is also not complete.

### Pre-requisites and installation

- python3
- git
- requirements of the repo

To install the tool, clone the [ingest-broker repository](https://github.com/ebi-ait/ingest-broker).

#### Usage

Move to the ingest broker directory.

```
cd ingest-broker
```

Install the requirements of the package or run in docker (instructions for how to do this in the main README)

```
pip install -r requirements.txt

```

Check out the usage of `generate_summary.py` by using `--help`:

```
mfreeberg$ python generate_summary.py --help
usage: generate_summary.py [-h] H T U O

Process some integers.

positional arguments:
  H           the url of the ingest API (e.g
              http://api.ingest.dev.data.humancellatlas.org)
  T           the type of summary (project or submission)
  U           the uuid of the project/submission
  O           summary output format

optional arguments:
  -h, --help  show this help message and exit
```

Run the `generate_summary.py` script supplying the ingest API url, the type of summary (project or submission), the (project or submission envelope, respectively) UUID, and the desired output format (json or tsv). If you choose json, the report will be printed to the screen. If you choose tsv, the report be written to `report.tsv`.

```
mfreeberg$ python3 generate_summary.py http://api.ingest.dev.data.humancellatlas.org project 763e071c-34ed-4db5-9006-8929ccdf5b26 tsv
mfreeberg$ cat report.tsv
entity	count
dissociation_protocol	1
enrichment_protocol	1
library_preparation_protocol	1
sequencing_protocol	1
process	5096
donor_organism	8
specimen_from_organism	8
cell_suspension	2544
sequence_file	5088

```

Also generated is a file `scrape.tsv` which contains a bit more key pieces of metadata that can be useful to fill out project pages.

```
mfreeberg$ cat scrape.tsv
cell_type	['pancreatic A cell', 'acinar cell', 'type B pancreatic cell', 'pancreatic D cell', 'pancreatic ductal cell', 'mesenchymal cell']
num_total_estimated_cells	2544
organ	['pancreas', 'islet of Langerhans']
organoid_organ_model	[]
genus_species	['Homo sapiens']
num_donors	8
num_specimens	8
num_cell lines	0
num_organoids	0
num_cell suspension	2544
library_construction_approach	['Smart-seq2']
num_fastqs	5088
project_title	['Single cell transcriptome analysis of human pancreas reveals transcriptional signatures of aging and somatic mutation patterns.']
contact_names/emails	['Martin, Enge', 'Laura,,Huerta', 'Matthew,,Green', 'martin.enge@gmail.com', 'lauhuema@ebi.ac.uk', 'hewgreen@ebi.ac.uk']
```

If you would like additional metadata reported by this tool, please make a request via a GitHub issue in the ingest-central repository.

## Use terminal sessions in EC2: tmux, screen

### Pre-requisites and installation

No pre-requisites or installation required. Both programs are already installed in the EC2.

### Usage

Using `tmux` or `screen` in the EC2 (or in life) is useful because you can run a job in a session without it being cancelled due to a dropped connection. For example, you can run an `hca upload files *` job that takes hours to complete, and you don't have to worry about it being interrupted. Below are some hints for using `tmux`, but `screen` acts in a similar manner. Try `man tmux` or `man screen` in the EC2 to view the manual for the two commands.

1. Make and enter a session using `tmux`:

```
tmux new -s <session_name>
```

1. Run any command(s) like you normally would in the EC2:

```
hca upload files *.fastq.gz
```

1. To detach from your session: press CTRL+b, release both keys, and then press d. You'll be back in EC2, and the command will still be running.
1. To view all the session you have running:
```
tmux ls
```

1. To get back to a session to see how the job is going:
```
tmux a -t <session_name>
```

See the cheat sheet for more details like how to delete sessions and some other cool stuff: https://gist.github.com/henrik/1967800.


## Transfer files between local machine and EC2: scp, rsync

### Pre-requisites and installation

No pre-requisites or installation required. Both programs are already installed in the EC2 (and in most unix environments).

### Usage

Using `scp` or `rsync` lets you transfer files from one location to another. `rsync` is better when you are transferring lots of files or large files (can pick up from where you left off if sync gets disconnected). `scp` is fine for small or just a few files. Below are some hints for using `rsync`, but `scp` acts in a similar manner. The argument `-r` is useful for recursively grabbing all files in a directory. Try `man rsync` or `man scp` in the EC2 to view the manual for the two commands.

1. Transfer set of fastq files from EC2 to the current directory of your local machine (from your local machine):
```
cd target_directory
rsync -r <username>@@tool.archive.data.humancellatlas.org:/path/to/file/*.fastq.gz ./
```

## Extract all text to ontology mappings from one or more submissions in ingest

TODO: Check if this will work for current ingest or how to modify to make it work

### Pre-requisites and installation

- python 3
- pip
- python requests module (install via `pip install requests` - only needed once!)

### Usage

Edit the script by putting the submission envelope IDs for the submissions you want to extract mappings from into the empty array at the very bottom of the script:

```
# -----> PUT YOUR ENVELOPE IDs IN HERE <---------
    envelope_ids = []
```

If you don't want the output file to have the default file name, you can also edit this.

Run the script in the command line using

```
python3 ontology_mappings_extractor.py
```

Once the output file has been generated, remove duplicate entries from the file by running

```
sort all_mappings.txt | uniq > all_mappings_unique.txt
```

## Converting JSON schema properties to csv: json_fields_to_csv.py

TODO: Check if this is still useful and what it does

### Pre-requisites and installation

- python3
- python packages: json, argparse, os, logging

### Usage

This script converts all properties in the JSON schema files into csv format. A file path to the metadata repo needs to be provided. For guidance on how to use the tool, run the script with `--help`:

```
dwelter$ python3 json_fields_to_csv.py --path_to_schemas ../../metadata-schema/json_schema

```

## git commands

The following wrangler tools are related to using git. When working in the terminal, there are a few useful git commands to remember. To use them, you must have run `git clone <repo>` locally to get a copy of the repository and you must be currently located somewhere in the cloned git folder.

1. `git status` - check what changes have been made locally to the git repo.
1. `git add .` - prepare (stage) all the files in the current directory (recursively) you have changed for committing back to the repo. Replace `.` with a specific file or regex to target ony specific file(s).
1. `git commit -m "Message"` - commit your staged changes. Include a helpful commit message.
1. `git push` - Push your committed changes to the repo.
1. `git pull` - Pull any remote changes into your local repo.
1. `git pull origin <branch>` - Pull any remote changes from an upstream branch and merge with your current branch. Used during release process.
1. `git reset --hard origin/master` - Get rid of any local changes and revert to the current state of master branch
1. `git checkout <branch>` - Switch to a specific branch locally.
1. `git checkout -b <new_branch>` - Create a new branch from the current branch and switch to it.

Please request additional commands!

### Converting markdown to pdf: grip

#### Pre-requisites and installation

- https://github.com/joeyespo/grip[grip]

See the https://github.com/joeyespo/grip#installation[grip GitHub repo] for instructions on how to install `grip`.

Briefly:

To install grip, simply:

```
$ pip install grip
```

On OS X, you can also install with Homebrew:

```
$ brew install grip
```

#### Usage

See the https://github.com/joeyespo/grip#usage[grip GitHub repo] for instructions on how to use `grip`.

Briefly:

1. Install grip locally
1. Navigate to a directory with a markdown file
1. Run `grip <file>.md`
1. Navigate to local host name (e.g. `http://localhost:6419/`)
1. Print screen and save as PDF

### Converting yaml to csv: generic_yaml2csv.py

#### Pre-requisites and installation

- python3
- python packages: yaml, argparse, csv, sys, pandas

#### Usage

This script converts any yaml file into csv format. The default file to convert is the potential_datasets.yaml file, but any file path can be provided. For guidance on how to use the tool, run the script with `--help`:

```
mfreeberg$ python3 generic_yaml2csv.py --help
usage: generic_yaml2csv.py [-h] [--yaml_file YAML_FILE] [--csv_file CSV_FILE]

Throw away script potential_datasets.yaml to csv

optional arguments:
  -h, --help            show this help message and exit
  --yaml_file YAML_FILE, -i YAML_FILE
                        yaml file name
  --csv_file CSV_FILE, -o CSV_FILE
                        csv output file name
```

## hca cli commands

The following wrangler tools are related to using the hca cli.

## Upload: hca upload

### Pre-requisites and installation

- pip

Install the hca cli tool locally or in a virtual environment (e.g. venv, conda) using pip:

```
pip install hca
```

If you haven't updated the hca cli in a while, update to the newest version using pip:

```
pip install --upgrade hca
```

### Usage

The two main `hca upload` commands wranglers use is the one to select the upload area of interest (`hca upload select`) and to transfer files to that upload area (`hca upload files`). Wranglers might also want to view a list of files in the selected upload area (`hca upload list`) or view a list of all upload areas they have accessed (`hca upload areas`).

To select an upload area:

```
mfreeberg$ hca upload select s3://org-humancellatlas-upload-staging/d2313de3-11bf-4a19-b1eb-a7b82a9467af/
Upload area d2313de3-11bf-4a19-b1eb-a7b82a9467af selected.
In future you may refer to this upload area using the alias "d"
```

To transfer all local files that end with `.fastq.gz` to the selected upload area:

```
mfreeberg$ hca upload files *.fastq.gz

Starting upload of 2 files to upload area d2313de3-11bf-4a19-b1eb-a7b82a9467af

Completed 122 KiB/249 KiB with 2 of 2 files remaining
Download complete of R1.fastq.gz to upload area d2313de3-11bf-4a19-b1eb-a7b82a9467af/R1.fastq.gz

Completed 249 KiB/249 KiB with 1 of 2 files remaining
Download complete of R2.fastq.gz to upload area d2313de3-11bf-4a19-b1eb-a7b82a9467af/R2.fastq.gz

Completed upload of 2 files to upload area d2313de3-11bf-4a19-b1eb-a7b82a9467af
```

To transfer all files from a source s3 bucket (`s3://org-humancellatlas-upload-staging/aaaaaaaa-bbbb-cccc-dddd-acf331bf0e8f/`) to the selected upload area:

```
hca upload files s3://org-humancellatlas-upload-staging/aaaaaaaa-bbbb-cccc-dddd-acf331bf0e8f/
```

To transfer all files that start with "SRR" from a source s3 bucket (`s3://org-humancellatlas-upload-staging/aaaaaaaa-bbbb-cccc-dddd-acf331bf0e8f/`) to the selected upload area:

```
hca upload files s3://org-humancellatlas-upload-staging/00104402-ccf2-45bd-9ef9-c172a5f7503b/SRR
```


To view the files in the selected upload area:

```
mfreeberg$ hca upload list
R1.fastq.gz
R2.fastq.gz
```
