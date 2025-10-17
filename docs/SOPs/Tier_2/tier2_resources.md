# Tier 2 - Resources
[#1286](https://github.com/ebi-ait/hca-ebi-wrangler-central/issues/1286)
Here we have links for most of the tier 2 organising processes, and a table to record the progress of each bionetwork.
## Finalised Tier 2 google folder
[HCA Tier 2 metadata definitions [PUBLIC ACCESS]](https://drive.google.com/drive/folders/1ngcIgKBV9OUM1pPO-CDRH6ZIpyiSpamu)
This is a google drive folder managed by HCA exec team, that is publicly accessible and Clever Canary team is pulling info from there to build the Tier 2 Data Dictionary https://data.humancellatlas.org/metadata/tier-2 . The google drive folder should only contain the finalised and ready to published versions of Tier 2 definitions.
## WIP Tier 2 google folder
[EBI Tier 2](https://drive.google.com/drive/folders/1zKyhGugIw0BCGTaITF2wMGajqpI4VxeR)
This is google drive managed by the EBI team, that is private to the FG team, and individual sheets are shared with specific coordinators. Communication logs for some of the discussions are also recorded there.

## Cross-Bionetwork Summary sheet
[Tier 2: cross-bionetwork summary](https://docs.google.com/spreadsheets/d/12mHUijrbvhFRu85BqcMPVEslvAURpvhzHPZshZ17-ps/)
A sheet that pulls all metadata fields from finalised Tier 2 lists, compares between bionetworks and shows which fields are used by which bionetwork.
### Tabs description:
* **all_tier2**: summary tab with all info regarding the common fields per bionetwork
* **conf_sheet_link**: this is where we add the link for Tier 2 definitions google sheets and specify in which cell the programmatic names are found
* **conf_pull_data**: Bionetwork names are listed in column A. For each bionetwork a formula imports all the fields’ programmatic names into column B.
Make sure to fill the bionetwork name in column A next to all the corresponding  field names in column B. In unified_field (column C) a formula pulls from conf_similar_fields tab a unified field name for fields that are named slightly differently across bionetworks
* **conf_map_dcp**: this maps t2 fields to existing fields in the DCP metadata schema. 
Please add field name in column A and dcp programmatic name in column C.
* **conf_similar_fields**: every new field that has not been used before, needs to be added here in a new row.
Some bionetworks use different names to describe the same fields so if that’s the case, a synonym field should be added next to the appropriate field value (in columns C:F).
You can specify modules to describe what metadata module this field could be added to in the dcp schema. Using more descriptive groupings of the metadata helps to make the long list more readable, but serves no other functionality.
### How to update
To link a new finalised t2 sheet:
1. Update the **conf_sheet_link** tab with the correct link - it cannot be `.xlsx` format, in order to be accessible with importrange functions, it has to be a google sheet. Specify the cell where programmatic field names are found in the finalised sheet. 
1. In **conf_pull_data** write the bionetwork name in column A, copy the function to pull data from cell B2 and paste it at the end of the current fields.
If there is not enough space for all metadata fields, an error will appear so make sure you have enough space to pull everything. Drop down the functions for all other columns C:F and see what fields need to be added in the **conf_map_dcp** and **conf_similar_fields**. Follow the instructions below to add new t2 fields.
1. In the conf_map_dcp tab, sort by column A to keep consistency

To add a new t2 field:
1. New field will be automatically be pulled from the definitions spreadsheet defined in **conf_sheet_link**
1. If `#REF` is shown in **conf_sheet_link** make sure there is enough space after query-importrange function for the bionetwork, if no, add rows and extend functions
1. Check if the field should be matched to a similar field in **conf_similar_fields**
    1. If yes, add field in the next empty column of the appropriate row of **conf_similar_fields**!C:F
    1. If not, add field in a new row in **conf_similar_fields**!B
    1. Ideally, find a relevant group to fit in (**conf_similar_fields**!G) and add in the same cluster of rows so it appears grouped in all_tier2 tab
    1. find a relevant dcp schema module **conf_similar_fields**!A
1. Add new fields in conf_map_dcp
    1. Add new field to column A
    1. if the field can be mapped to an existing dcp field, add the dcp field in column B and C, if not leave them empty 

## Tier 2 sheet validator
[Tier 2 sheet - validator](https://docs.google.com/spreadsheets/d/1JUm5PMcbg8iy4Q7knXHhfjNjyMfeMEhUOfkYwejbGbg/)
This is a sheet to make sure that values in definitions and template sheets match.
We have one summary tab called validate and each bionetwork with finalised tier 2 has a separate tab as well.
### How to read
1. In the validate tab check any FALSE values that indicate mismatch between definitions and template sheets, or between bionetwork definitions and Genetic Diversity definitions
1. If FALSE values are existent, investigate in the relevant bionetwork tab.
    * We have two tables to compare in each tab: **Templates** and **Definitions**.
    * Template fields (columns A:E) and Definitions fields (column K:P) are imported directly from the corresponding spreadsheets, specified in validate!B:C.
    * In order to compare we need to align the two table fields, and this is done by matching the programmatic name of in col F. Then in the next columns friendly, description, examples are tested. Comparison results are found in columns F:I and correspond to metadata field from template (column E)
    * If any FALSE values are found in F:I columns address the mismatch
### How it works
For each bionetwork:
1. pull template and definition sheets with importrange() - neither can be `.xlsx` format, in order to be accessible with importrange functions, it has to be a google sheet and have permissions to read (and edit?)
1. check if the `programmatic` and `friendly field_name`, `description` and `examples` are matching between the two sheets
Each bionetwork has a separate tab where definitions and templates are pulled based on the links in the validate tab. In each bionetwork tab then
1. match the fields based on the `programmatic field name`
1. compare friendly, description and examples (after removing prefix sentence from template’s examples)
1. if mismatch get a FALSE in G,H and I columns for friendly, description, example
A comparison between each bionetwork and Genetic Diversity (GD) fields is done on the right extension of each tab. GD tab has a right extension to compare between definitions among all bionetworks.
We get a summary glimpse of errors in the validate tab where we can see if all is good within each bionetwork and between bionetwork and GD fields.
## Tier 2 collection tracker
[Tier 2 collection tracker](https://docs.google.com/spreadsheets/d/1nTNNxjfUffOU19jVabneyGwfz_RX-M8qjogBayosjFU)
This is a sheet to keep track of communication between wranglers and contributors regarding the Tier 2 collection.
Main tracking focus shifted to HCA DCA tracker since signing the DCA is the next part of the collection process, but the collection tracking sheet is used to keep mapping between emails and datasets/study names (when we can).
## HCA DCA tracker
[HCA DCA tracker](https://docs.google.com/spreadsheets/d/1iovc638KQsP9-OVUM3OQOZ77PWeeqwwo6j6WOf89ut4)
This is a sheet to keep track of communication between wranglers and contributors regarding the singing of DCA. 

