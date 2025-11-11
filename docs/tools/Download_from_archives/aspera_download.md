---
layout: default
title: Download files using aspera
parent: Download from archives
grand_parent: Tools
nav_order: 4
---
# Download ENA files using aspera 

ENA offers an option to download data files through Aspera, which is usually faster than accessing the files through each link.

## Install
To install:
1. Download aspera on your home directory on EC2 using the following command:
```shell
wget https://ak-delivery04-mul.dhe.ibm.com/sar/CMA/OSA/08q6g/0/ibm-aspera-cli-3.9.6.1467.159c5b1-linux-64-release.sh
```
1. Run the file to install aspera:
```shell
sh ibm-aspera-cli-3.9.6.1467.159c5b1-linux-64-release.sh
```
1. After installing, export the path to your .bashrc file by running `vim .bashrc` and copying this `export` statement to the end of the file: `export PATH=~/.aspera/cli/bin:$PATH`. The next time you log into the EC2, you will be able to run the commands without any additional step.

## Download files
Once installed, downloading the files locally is easy by following the instructions on [ENA's ReadTheDocs page](https://ena-docs.readthedocs.io/en/latest/retrieval/file-download.html#using-aspera). Alternatively, you can follow these steps if you need to download a full dataset:
1. Locate the project page (e.g. https://www.ebi.ac.uk/ena/browser/view/PRJEB40448)
1. Download the Json report at the bottom of the page and upload it to your own `/data/` folder in the EC2
1. Open a virtual session (The next step will take some time, so it's better to leave it running under a virtual session)
1. `cd` to your `/data/` folder and run the following command:
```shell
cat <name_of_report_file> | jq '.[].fastq_ftp' | grep -E -o "ftp\.[^;]*fastq\.gz" | sed 's/ftp.sra.ebi.ac.uk\///g' | \
    xargs -I{} sh -c "\
        ascp -QT -l 300m -P33001 \
             -i ~/.aspera/cli/etc/asperaweb_id_dsa.openssh \
             era-fasp@fasp.sra.ebi.ac.uk:{} \
             \$( echo {} |\
        awk -F/ '{print $6}' )"
```
This command will read the report, isolate the file names and start downloading them. 

## Useful tips
You can pass the argument -P to parallelize xargs. This will run several downloads in parallel.
Example:
```shell
cat <name_of_report_file> | jq '.[].fastq_ftp' | grep -E -o "ftp\.[^;]*fastq\.gz" | sed 's/ftp.sra.ebi.ac.uk\///g' | xargs -I{} -P [enter parallelisation number] sh -c "ascp -QT -l 300m -P33001 -i ~/.aspera/cli/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:{} \$( echo {} | awk -F/ '{print $6}' )"
```

The last `{}` is the filename that will be used for download. If you want to create a specific folder for the files, you can create the folder and append it to the argument, following the next example (where `\"my_cool_fastq/\"` would be the name of the folder)
Example:
```shell
cat <name_of_report_file> | jq '.[].fastq_ftp' | grep -E -o "ftp\.[^;]*fastq\.gz" | sed 's/ftp.sra.ebi.ac.uk\///g' | xargs -I{} sh -c "ascp -QT -l 300m -P33001 -i ~/.aspera/cli/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:{} \$( echo {} | awk -F/ '{print \"my_cool_fastq/\" $6}' )"
```