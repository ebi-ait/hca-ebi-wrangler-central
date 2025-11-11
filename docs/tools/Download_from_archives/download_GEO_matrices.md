---
layout: default
title: Downloade GEO supplementary files
parent: Download from archives
grand_parent: Tools
has_children: false
nav_order: 3
---

For most publications with a GEO accession, gene matrices files are available for download. The matrices files can be directly downloaded either locally to your desktop by clicking the link, or via wget in the terminal and on EC2.

If the file is particularly large, the wget command will get stuck and the matrices file will not be downloaded. In that case, you can do the following:

Upon running the wget command, if the file is particularly large, you will see that an index.html file path is returned.

Example:

`index.html?acc=GSE171668.1 saved`

You can then run the following command to get an ftp link:

`cat index.html\?acc\=[your GEO accession] | grep "RAW.tar"`

Example:

`cat index.html\?acc\=GSE171668 | grep "RAW.tar"`

You can then wget the ftp link:

`wget ftp://ftp.ncbi.nlm.nih.gov/geo/series/[your GEO accession prefix]nnn/[your GEO accession]/suppl/[your GEO accession]_RAW.tar`

Example:

`wget ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE171nnn/GSE171668/suppl/GSE171668_RAW.tar`
