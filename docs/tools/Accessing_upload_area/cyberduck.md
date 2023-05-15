---
layout: default
title: Transfer files between local and EC2 - cyberduck
parent: Accessing upload area
grand_parent: Tools
---
# Transfer files between local and EC2: Cyberduck

## Install Cyberduck

EBI mac users can download from the Managed Software Centre, or else see: [Cyberduck](https://cyberduck.io/download/).

Currently only for Windows and Mac users.

## Configure connection to the EC2

1. Open the Cyberduck application and go to top menu option `File > Open connection`
1. Choose `SFTP (SSH File Transfer Protocol)` and fill in the server, username and password information as follows:
    1. Server: tool.archive.data.humancellatlas.org
    1. Username: your EC2 username
    1. Password: your EC2 password
    1. SSH Private Key: path to your private key, the default will probably work unless you configured this differently  
1. Click `Connect`

## Browse, download, upload

You should then be able to browse files on the EC2. 

To **download** a file from the EC2, simply double click it and it should get downloaded to your default download location (usually Downloads folder).

To **upload** a file to the EC2, navigate to the folder where you want the file uploaded, go to the top menu `File > Upload...` and choose the file. you may be prompted for your Username, Password and private key location, enter these and confirm and you file should get uploaded to that location.

To store the information you configured, go to the top menu option `Bookmark > New bookmark`. The next time you open the program you should be able to double click the bookmark in order to connect without having to enter the above information again.

This program can also be used for syncing files to ftp sites, such as for ArrayExpress submissions.

[reference](http://www.brianhoshi.com/blog/how-to-ftp-into-your-ec2-instance-with-cyberduck/)