---
layout: default
title: HCA to SCEA Guide
parent: SOPs
---

# HCA to SCEA Guide

_Please note: this is not a tool to generate a perfect set of SCEA idf and sdrf files automatically. It speeds up the process by part automation but manual curation is an important part of the process._

A range of idf and sdrf files can be found in the relevant SCEA Gitlab repository here: [https://gitlab.ebi.ac.uk/ebi-gene-expression/scxa-metadata/tree/master/HCAD](https://gitlab.ebi.ac.uk/ebi-gene-expression/scxa-metadata/tree/master/HCAD)

If you do not have access, you can request access from Silvie. It will be extremely helpful to use these as example templates during this process.

Other documents that Silvie shared with us can be found here: [https://drive.google.com/drive/folders/1GHaqpQsz4CY6_KkBTTXHJo69J4FXMNcw](https://drive.google.com/drive/folders/1GHaqpQsz4CY6_KkBTTXHJo69J4FXMNcw). They are not all entirely clear so I have culminated what I know of the process so far into this document. However, if you are unsure of anything, please refer back to these documents before asking me/Silvie/SCEA team in case your question is answered by those.


## Useful documents 

<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2020-10-06T13:45:39.313Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36\&quot; etag=\&quot;kT6bK9NXz6dONPBydThC\&quot; version=\&quot;13.7.5\&quot; type=\&quot;google\&quot;&gt;&lt;diagram id=\&quot;FsEeLdDOj7soeLvYh2q5\&quot; name=\&quot;Page-1\&quot;&gt;3VnbcqM4EP0aP+LiZmw/JraZzF4qW5vamap9SQkhgzYYMUIMzn79tkBgsCHGM8SeneTB0Lr3OTrdEhNrtdt/4CgJf2c+iSam7u8n1npimoZtOvAjLa+lxVnOS0PAqa8qHQxP9F+ijLqyZtQnaauiYCwSNGkbMYtjgkXLhjhnebvalkXtURMUkBPDE0bRqfUz9UVYWhfm/GB/IDQIq5ENZ1mW7FBVWa0kDZHP8obJ2kysFWdMlE+7/YpE0nmVX8p2bk9pPTFOYjGkwV3+64P+6cNT/tHO/ka294v4I9YqN39FUaZWrGYrXisXcJbFPpG9GBPrPg+pIE8JwrI0B9DBFopdpIpTwdkLWbGI8aK15eAF8bZQsqVR1LBv1o6r62APOPIprGFNOQBIWSz7JaloFDWaue79bC6bqXkTLsi+1yNG7WcgKGE7IvgrVFENbFutvuKmes0PQNu6soUNkGcVpEiRK6i7PvgfHhQEF8CxvBUad8uVvbnvQYOgPjTW9sZwZyOhcT0w/koJf/T+kXph6hHySFQ2XSOBpLczKpBHIyrk9DAHF3OKylEiGr+UlUMhpAbdyUFM14em0zDboRjDMEhEKJ0yHkAJKJPg1MsEab7QONBkG601mHVqMs9xZtHwquLY99Gl0jnzEgL5iCy2eBwmGHqbCqZ1ygXD6OCCczkV4LXBhkuU0+jYq04kN8oWQG6h4HzJWFWgpUWMA9rolpPsD4XwFKjfohevMsD8tlkRVRnOduDDtKoCk/eOm4GtHL8y9+qH/i36Ufx1UuWIENuZ/FeLbtjLv2tJxqJLMubjKcYx5FX+UoFqDcD3YXV3MaB9MpTnebcKDRASw3pTSSB/SeRjwhkmaXqePB7CL0FBt8dMwIRJp8oYA4JRV8TppKbrvguxjA4B6gxG9igC1Ee2zxzFQUQ4WD/RNEMSoI+wmfdvc4J4VENUTAMqwsybUga2ECNN2nPVpYbBM1z2OIgp9k8Xc2pRuE3MeU99eVptxhUYIM4U4Wn2Au/BHhIjN8WSU7DwIeSZ3Upm+iXj3NnkSgeQH0Rn7mTckDDGOMpSeQYYmgUricFsp3QnIDHRyD7hACV0pEmgEll2MBVRSsMZR6KoIQ/8kqYR8+QS4OwhFc+VJ22YlFtP6rma0nTnD6Gdc1XN8udLr6DQcVq0JQ4eSbNmt82T++ijnCteYR8DcRSw8MizSEJ4cwJtCefEf5Yp0rOc5UACzX86Ajk/dtBLExRXUanSpC3A+UUukrOvgLPMhThJWEoFk8PXEa3ZdiTKlTwrJqAdhj/Pm+WgeIczjwwIdiXLfvPORT8f8ZdH6EbeIcBRb6rP2kazsHZGxZp5ZxP1UcVsMWtx0e44zXVy8RtOcxdwEQ5nmmBamUPpmElpaTHuImpBGq6Sb+gzxUT+sigdwKLGlfH/g0V10n6WRaOm8Uch8cosGnZ1ZFqTvqujOjlfv33X8/2Xwv2Jccwk/vf19wopBawmwWyk3NdaHOW+iw6kzA6krMuRGgiLfR6WP6udT4tcYlXowY0Aen9MbOPmmMwHbBUkUEqkbgsOOkbjQPo+JNI0AJpKOmMmhkjnJUrZvmttbahTvVwtNvduZ27YeQpdbZbu5M3vNUcyO+63mjZRLP2UKIsOntQ3+5fJ7OEjaVHW+NRsbf4D&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>


## Section A: Running the hca-to-scea-tools converter**

1. Submit completed HCA metadata spreadsheet to the hca-to-scea-tool which can be found in the following Github repository: [https://github.com/ebi-ait/hca-to-scea-tools](https://github.com/ebi-ait/hca-to-scea-tools). To do this, clone the repository to your local directory. Instructions on how to install and use the tool are documented in the README file. Once you have navigated to [http://127.0.0.1:5000](https://github.com/ebi-ait/hca-to-scea-tools/blob/master) in a browser as specified in the README, follow the next steps described here.

2. You should see a webpage which looks like the following:
![Base webpage](/assets/images/scea_screenshots/base_web.png)

   2. Upload the spreadsheet file as indicated. Note that if your spreadsheet has multiple technologies that you will need to upload a separate spreadsheet per technology.

   2. Enter an accession id number in the ‘E-HCAD-” box. The E-HCAD accession series is specifically for HCA metadata which has been converted to SCEA standard. The next number in the series should be identified using the data backlog tracking sheet located here: [https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0](https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0). This is obviously going to get difficult; any ideas to improve this process are welcome. 

   2. Enter the curator’s initials. There is an option to click the “-” button to remove the 2nd box. Default values are AD and JFG.

   2. Once you are happy with this, click on ‘process!’.

   2. A new step will appear: “Force a Project UUID”. You can either enter a uuid or click “Fill in project details manually”. **For now, always click “Fill in project details manually”**. This will ensure the correct information is added to the idf and sdrf files.


3. You should now see a webpage like the following:
    ![Protocol matching](/assets/images/scea_screenshots/protocol_matching.png)
   
   You can edit the text inside the protocol descriptions and merge the protocols into 1 by dropping and dragging. The idea is to keep duplication across protocols as minimal as possible.

4. You should also see the following on the same webpage:
    ![Prefilled values](/assets/images/scea_screenshots/pre_filled_values.png)
    
    These are pre-filled values for the sequencing protocol that is specified in the HCA metadata spreadsheet. Currently, if ‘10X v2 sequencing’ is specified, these fields are pre-filled. You can then manually edit them. If another technology is specified, these fields are not pre-filled and you need to enter the information here manually. SCEA requires that datasets are split by technology, so you should only have 1 technology type in your HCA metadata file.

5. Click ‘this looks alright’. An idf and sdrf file will be generated in a newly created folder inside the ‘spreadsheets’ folder in your local repository directory.
6. The idf and sdrf files that are generated will need to be edited and some fields/values manually added to accurately reflect the experimental design and meet SCEA metadata requirements.

## Section B: Refining the idf and sdrf files 

### idf file

1. Any fields which need to be filled manually will be indicated in the file by <fill this>:

     Some are straight-forward:

    *   `Public Release Date`: when was the data publicly released? It needs to be in this format to pass validation: YYYY-MM-DD
    *   `Comment[EAExpectedClusters]`: this can be left blank
    *   `Comment[HCALastUpdateDate]`: when was the HCA spreadsheet last updated?
    *   `Comment[SecondaryAccession]`: tab-separated list of secondary accesions: HCA uuid; other secondary accessions (e.g. GEO,AE) 

    Others need a bit more work:

    *   `Comment[EAAdditionalAttributes]`: which attributes in the sdrf file do you think would be useful attributes to display visually when a user hovers over the cell clusters? Please give a tab-separated list. Factor values are automatically displayed so do not include  these.
    *   `Comment[EAExperimentType]`: how would you describe the experiment: baseline or differential? An example of baseline would be sequencing kidney cells to map the normal kidney. An example of differential would be sequencing kidney cells to map the normal versus disease kidney.
    *   We will come back to ‘Experimental Factor Name’ and ‘Experimental Factor Type’ later in this document.

An example screenshot to illustrate the above points:

![Refining fields](hca-ebi-wrangler-central/assets/images/scea_screenshots/refining_fields.png)




2. You can further edit the list of Protocol Name, Protocol Type and Protocol Description in the idf file if you need to:
*   Each Name, Type and Description must be tab-separated.
*   The Name should be ordered by number.
*   The Type and Description order must reflect the Name orderhttps://github.com/ebi-gene-expression-group/atlas-fastq-provider.
*   Protocol Types have to be 1 of: ‘sample collection protocol’,’treatment protocol’,’enrichment protocol’,’nucleic acid library construction protocol’,’nucleic acid sequencing protocol’.
*   SCEA dissociation protocols are labelled as “enrichment protocol”.
*   The Protocol Name is used in the sdrf file to detail which protocols are applied in which experiments. It is worth checking these are all correct in the sdrf.
*   If the experimental design consists of a treatment, a stimulus, or some other protocol which you believe is not reflected by HCA protocol names, you can add a new protocol Name, Type and Description in the idf file. You would need to then modify the number order of all protocol Names and the associated Type and Descriptions. The sdrf protocol REF fields would need to reflect these changes.

Example screenshot taken from an idf file:

_sdrf file_



*   You will need to check that the number and name of the protocol REF ids in the idf file (e.g. P-HCADX-1,P-HCADX-2) matches correctly with the experiment rows in the sdrf files, based on the experimental design. The automatic conversion should be correct but this is a good check to do.
*   You will need to fill cells consisting of &lt;FILL THIS> or if no relevant information is available, you can leave these blank.
*   Material Type is currently set to “whole organism” by default (hca-to-scea-tools script needs updating). Please change to “organism part” if the sample is an organ/tissue specimen or “cell” if the sample was an organoid or cell line culture.
*   The last columns in the sdrf file should be Factor Value fields. They are not automatically generated. It is good to add these where you can identify a factor which may be useful to the user to reflect potential differential groups. These should be selected from the ‘Characteristic’ fields. For example, you might choose to add Factor Value[organism part] or Factor Value[disease] if they are variable. You can also add additional Characteristic fields such as Characteristic[immunophenotype] or Characteristics[stimulus]. These can then be used as a Factor Value field such as Factor Value[stimulus].
*   Controlled vocabulary is applicable in certain sdrf fields: please see the shared documents from Silvie found here: [https://drive.google.com/drive/folders/1GHaqpQsz4CY6_KkBTTXHJo69J4FXMNcw](https://drive.google.com/drive/folders/1GHaqpQsz4CY6_KkBTTXHJo69J4FXMNcw)
*   Make sure you save the sdrf file as a tab-delimited .txt file: beware of excel changing your time unit ranges to a date format and of empty rows/lines at the bottom of the file. Empty rows/lines will cause errors in validation.
*   Once this is all complete, go back to the idf file and fill these fields: ‘Experimental Factor Name’ and ‘Experimental Factor Type’ with a tab-separated list of the Factor values you had chosen to add in the sdrf file. See below screenshot as an example:

    

<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![Refining SDRF](hca-ebi-wrangler-central/assets/images/scea_screenshots/sdrf_refining.png)



**Section C: Validation of idf and sdrf files**

_There are 2 validation steps for SCEA: a python validator and perl validator. In Silvie’s words: “the perl script checks the mage-tab format in general (plus some curation checks etc) and the the python script mainly checks for single-cell expression atlas specific fields and requirements”._

_Python Validator:_

A MAGE-TAB pre-validation module for running checks that guarantee the experiment can be processed for SCEA. You can clone the repository and run the script locally:

[https://github.com/ebi-gene-expression-group/atlas-metadata-validator](https://github.com/ebi-gene-expression-group/atlas-metadata-validator)

<span style="text-decoration:underline;">General Command:</span>

python atlas_validation.py path/to/test.idf.txt

<span style="text-decoration:underline;">Useful HCA-specific and single-cell specific command:</span>

python atlas_validation.py path/to/test.idf.txt -sc -hca -v



*   The SDRF file is expected in the same directory as the IDF file. If this is not the case, the location of the SDRF and other data files can be specified with -d PATH_TO_DATA option.
*   The script guesses the experiment type (sequencing, microarray or single-cell) from the MAGE-TAB. If this was unsuccessful the experiment type can be set by specifying the respective argument -seq, -ma or -sc.
*   The data file and URI checks may take a long time. Hence there is an option to skip these checks with -x.
*   Verbose logging can be activated with -v.
*   Special validation rules for HCA-imported experiments can be invoked with -hca option. The validator will otherwise guess if the experiment is an HCA import based on the HCAD accession code in the ExpressionAtlasAccession field.

An example of a successful validation looks like this:



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![Validation](hca-ebi-wrangler-central/assets/images/scea_screenshots/validation.png)


_Perl validator_



*   Install Anaconda if you don’t have it already and the Anaconda directory to your path
*   Configure conda by typing the following at the terminal:

    conda config --add channels defaults


    conda config --add channels bioconda


    conda config --add channels conda-forge

*   Install the perl atlas module in a new environment: 

    conda create -n perl-atlas-test -c ebi-gene-expression-group perl-atlas-modules



*   Activate the environment:

conda activate perl-atlas-test



*   Download the validate_magetab.pl_ _perl script from here: [https://drive.google.com/drive/folders/1Ja2NKtHkDh2YIvUhNa1mpivL-UjCsmbR](https://drive.google.com/drive/folders/1Ja2NKtHkDh2YIvUhNa1mpivL-UjCsmbR))
*   Execute the script (with idf and sdrf files in the same directory):

perl path-to/validate_magetab.pl -i &lt;idf-file>



*   You can ignore ArrayExpress errors

**Section D: SCEA file upload**



*   Create a new branch in the Gitlab gene-expression-atlas HCAD repository directory: [https://gitlab.ebi.ac.uk/ebi-gene-expression/scxa-metadata/tree/master/HCAD](https://gitlab.ebi.ac.uk/ebi-gene-expression/scxa-metadata/tree/master/HCAD)
*   Upload your validated SCEA files to this branch.
*   Submit a merge request and select ‘requires approval’.
*   Your SCEA files will then be reviewed for merging to the Master directory.