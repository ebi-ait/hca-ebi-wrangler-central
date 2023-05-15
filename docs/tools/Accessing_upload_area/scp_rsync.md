---
layout: default
title: Transfer files between local and EC2 - scp, rsync
parent: Accessing upload area
grand_parent: Tools
---
# Transfer files between local machine and EC2: scp, rsync

## Pre-requisites and installation

No pre-requisites or installation required. Both programs are already installed in the EC2 (and in most unix environments).

## Usage

Using `scp` or `rsync` lets you transfer files from one location to another. `rsync` is better when you are transferring lots of files or large files (can pick up from where you left off if sync gets disconnected). `scp` is fine for small or just a few files. Below are some hints for using `rsync`, but `scp` acts in a similar manner. The argument `-r` is useful for recursively grabbing all files in a directory. Try `man rsync` or `man scp` in the EC2 to view the manual for the two commands.

1. Transfer set of fastq files from EC2 to the current directory of your local machine (from your local machine):
	```
	cd target_directory
	rsync -r <username>@tool.archive.data.humancellatlas.org:/path/to/file/*.fastq.gz /localmachine/path/to/file
	```

2. To transfer files from your local machine to EC2, simply flip the order of the arguments:
	```
	rsync /localmachine/path/to/file <username>@tool.archive.data.humancellatlas.org:/EC2/path/to/file
	```