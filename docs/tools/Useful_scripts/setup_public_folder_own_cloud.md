---
layout: default
title: Setup public ownCloud folder
parent: Tools
grand_parent: Useful scripts
last_modified: 07/06/2021
---

# Setup public ownCloud folder

Sometimes to get smallish files from contributors the `hca-util` process is a bit heavy. Here is an alternate way to get a small number of smallish files from a contributor without them having to download and configure `hca-util`. The process below will create a public folder with a simple drag and drop interface. 

The standard storage amount for EBI's ownCloud service is 50gb, so if the files are bigger than that or you don't have enough storage this method is not suitable.

## Step-by-step

1. Login to your ebi ownCloud account with your ebi username and password -> [https://oc.ebi.ac.uk/login](https://oc.ebi.ac.uk/login)
1. Create a directory in your ownCloud 
1. Follow the instructions in the [ownCloud link share docs](https://doc.owncloud.com/server/user_manual/files/public_link_shares.html#creating-public-link-shares)
    - If you enter an email address, an automatic notification will be sent to that address with a link to the folder.
    - If you set a password to the folder, you will need to email the password to the contributor. 
    - If you don't set a password, anyone with the link can access the folder

## Resource links

- [EBI Intranet page](https://intranet.ebi.ac.uk/article/what-do-i-need-know-about-owncloud)
- [ownCloud login page](https://oc.ebi.ac.uk/login)
- [ownCloud link share docs](https://doc.owncloud.com/server/user_manual/files/public_link_shares.html#creating-public-link-shares)
