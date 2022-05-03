---
layout: default
title: How to get data from Globus
parent: SOPs
has_children: false
last_modified_date: 7/04/2022
---

# How to get data from Globus

[Globus](https://www.globus.org/) is a service that makes it easy to move, sync, and share large amounts of data. Globus can manage file transfers, monitor performance, retry failures, recover from faults automatically when possible, and report the status of data transfer. Globus uses GridFTP for more reliable and high-performance file transfer, and will queue file transfers to be performed asynchronously in the background.
Globus was developed and is maintained at the University of Chicago and is used extensively at supercomputer centres and major research facilities. 

Globus can support different types of storage and present them through a unified interface to simplify file transfer. 
A resource - server, cluster, storage system, laptop, or other system - is identified through an endpoint: an endpoint is defined, it will be available to authorised users who can transfer files to or from this endpoint.

## General flow
Using GlobusPersonalConnect you can establish a private endpoint in your machine, for example in the ec2 instance. 
You can then transfer files from the public endpoint shared by the scientists to your machine through your the private endpoint.
Once the data is in your filesystem you can upload it to a bucket with hca-util.

To avoid transfering the files twice we could potentially mount the hca-util bucket to the ec2 and transfer the files directly in the hca-util bucket. There are guides on how to mount s3 buckets but that would require a dev because wranglers don’t have sudo powers in the ec2.

#### Step 1: Sign up
Register on globus [here](https://auth.globus.org/p/login?client_id=89ba3e72-768f-4ddb-952d-e0bb7305e2c7&scope=urn%3Aglobus%3Aauth%3Ascope%3Aauth.globus.org%3Aview_identities+urn%3Aglobus%3Aauth%3Ascope%3Anexus.api.globus.org%3Agroups+urn%3Aglobus%3Aauth%3Ascope%3Atransfer.api.globus.org%3Aall&response_type=token&redirect_uri=%2Fv2%2Foauth2%2Fauthorize%3Fclient_id%3D89ba3e72-768f-4ddb-952d-e0bb7305e2c7%26scope%3Durn%253Aglobus%253Aauth%253Ascope%253Aauth.globus.org%253Aview_identities%2520urn%253Aglobus%253Aauth%253Ascope%253Anexus.api.globus.org%253Agroups%2520urn%253Aglobus%253Aauth%253Ascope%253Atransfer.api.globus.org%253Aall%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fapp.globus.org%252Flogin%26redirect_name%3DGlobus%2520Web%2520App%26state%3Dmq2sv0x1w8h%26viewlocale%3Den_US&redirect_name=Globus+Web+App&viewlocale=en_US)\
If you just want to browse the files available from a public endpoint this could be enough.
 <br/>
  <br/>

#### Step 2: Get Globus Connect Personal
It is more convinient to install Globus in the EC2 both because there is more storgae space available than in a personal computer and because it's possible to leave files to download overnight.
Download Globus Connect Personal from [here](https://docs.globus.org/how-to/globus-connect-personal-linux/) using the wget command and install it in the EC2.  \
Authenticate following the instructions there
 <br/>
 <br/>
 
#### Step 3: Create a private endpoint
Establish an endpoint in the ec2.
```bash
$ ./globusconnectpersonal -setup 
```
Note that by default the only path that globus personal connect will share is the home directory.\
To enable globus to see and move files to other locations, like the folders under /data you have to edit the file `~/.globusonline/lta/config-paths` [see instructions](https://docs.globus.org/how-to/globus-connect-personal-linux/#config-paths)
 <br/>
 <br/>

#### Step 4: Globus cli
At this point you can move files between your private endpoint in the ec2 and any public endpoint by using the graphic interface [here](https://auth.globus.org/p/login?client_id=89ba3e72-768f-4ddb-952d-e0bb7305e2c7&scope=urn%3Aglobus%3Aauth%3Ascope%3Aauth.globus.org%3Aview_identities+urn%3Aglobus%3Aauth%3Ascope%3Anexus.api.globus.org%3Agroups+urn%3Aglobus%3Aauth%3Ascope%3Atransfer.api.globus.org%3Aall&response_type=token&redirect_uri=%2Fv2%2Foauth2%2Fauthorize%3Fclient_id%3D89ba3e72-768f-4ddb-952d-e0bb7305e2c7%26scope%3Durn%253Aglobus%253Aauth%253Ascope%253Aauth.globus.org%253Aview_identities%2520urn%253Aglobus%253Aauth%253Ascope%253Anexus.api.globus.org%253Agroups%2520urn%253Aglobus%253Aauth%253Ascope%253Atransfer.api.globus.org%253Aall%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fapp.globus.org%252Flogin%26redirect_name%3DGlobus%2520Web%2520App%26state%3Dewa5ysmp6xj%26viewlocale%3Den_US&redirect_name=Globus+Web+App&viewlocale=en_US)
See [here](https://docs.globus.org/how-to/get-started/) for a short guide on how to use the graphical interface.

To move files from with a cli in the ec2 you need to install the python package globus from [here](https://docs.globus.org/cli/), the documentation is [here](https://docs.globus.org/cli/reference/list-commands/) \
With this you can do a couple of useful things like:

- `bookmark` \
You can bookmark an endpoint to avoid having to look for the endpoint’s id
```bash
$ globus bookmark create endpoint_uuid:path bookmark_name
```

Use the bookmark like this
```bash
$ globus ls $(globus bookmark show bookmark_name)
```

- `ls` \
You can navigate the folders in an endpoint the same way you would with a normal filesystem.\
You can list the contents of a directory recursively with the option `-r`
```bash
$ globus ls endpoint_uuid:path -r
```
By default it will traverse 3 directories, but the limit can be changed with the option `--recursive-depth-limit` 

To filter for certain words use the option `--filter`
```bash
$ globus ls endpoint_uuid:path –-filter ~*key_word*
```
For a more detailed description see the [documentation](https://docs.globus.org/cli/reference/ls/)
 <br/>
 <br/>

#### Step 5: Transfer files
Using globus transfer you can transfer files between 2 endpoints for which you have the id.
You can:
1. Transfer a single file
```bash
$ globus transfer source_endpoint_uuid:/path/file1.txt destination_endpoint_uuid:~/mynewfile.txt
```

2. Transfer all the contents of a folder with the option `--recursive`
```bash
$ globus transfer source_endpoint_uuid:/path/ destination_endpoint_uuid:~/mynewdir/ --recursive
```

3. Transfer a list of files from a file with the option `--batch`
```bash
$ globus transfer source_endpoint_uuid destination_endpoint_uuid --batch file_list.txt
```
Note the format of the file: you need to explicitly define the location and name of every file you want to transfer
```
/path/file1.txt ~/myfile1.txt
/path/file2.txt ~/myfile2.txt
/path/file3.txt ~/file3.txt
```

An example of how to find the files you want to transfer based on a key word and make a file to batch transfer them if they don’t need to be renamed.
```bash
$ globus ls $(globus bookmark show my_bookmark)/  --filter ~*key_word1* >> file_names.txt
$ globus ls $(globus bookmark show my_bookmark)/  --filter ~*key_word2* >> file_names.txt
$ for i in `cat file_names.txt`; do echo ep_path/$i /local_path/$i ; done > file_list.txt
$ globus transfer source_endpoint_uuid destination_endpoint_uuid --batch file_list.txt
```
