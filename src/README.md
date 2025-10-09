## Wrangler scripts for various handy purposes

### check_fastq.py

### compare_tracker_with_nxn_sheet.py

### fill_accessions.py

### fill_ontologies.py

Instructions of use and main algorithm

1. Algorithm
    1. Load the workbook at path specified with `-s` flag with openpyxl tools. Name will be the arg passed as args.wb_path
    1. Try to load pickled schemas, if not present at `pickled_schemas.pkl`, load a SchemaTemplate object and save schemas to picked_schemas.pkl (Takes a while, but necessary)
    1. Parse each cell of the workbook below row 5
    1. When an ontology property is found (Row 4.endswith("text"), load the schema from the full qualified key to apply DB restrictions
    1. Query the OLS/HCAO with database restrictions
    1. If array delimiter `||` is detected in the cell, each term is automatically searched and the returned curations are concatenated in the spreadsheet.
    1. If ZOOMA `--zooma`/`-z` option enabled, query the ZOOMA API for any available curation
    1. If `--keep`/`-k` option specified, no existing ontologies will be overwritten.
    1. Return ontologies that match the search and ask the user which one is correct.
    1. Save spreadsheet with the same name + `_ontologies`
    1. If interrupted with `ctrl+c` during running, in progress workbook is saved with spreadsheet name + `_partial_ontologies`

1. Instruction of use

```
cd src/
python3 -m pip install -r requirements.txt
python3 fill_ontologies.py -s <path_to_spreadsheet> [OPTIONS -z -k]
```
The script takes some time to get started (If it's loading a SchemaTemplate object). After approx 30 secs/1 min, it will begin the search, with the following possible outputs:
- `Found exact match for term 'x' (Ontology: 'y')`: The program has found an ontology that matches perfectly the spreadsheet value
- `Found high confidence, HCA match for term 'x' (Ontology: y)`
- `x matches found for your search term 'y' for field <spreadsheet text value>.`
   - Numbered list of matches in format (ZOOMA info show with option -z):
      - n. ontology_label - ontology_id. ZOOMA: confidence: (`HIGH`/`GOOD`/`MEDIUM`/`LOW`), source: `<SOURCE>`.
      - Enter the appropriate number or 'm' for manual input or 'none' to skip this term
   - Input n - The tool will fill the spreadsheet with that ontology.
   - Input 'm' - You'll be prompted to introduce the term that you want to look for
   - Input 'none': The ontology cells will be filled with empty strings for that field
- If array delimiter `||` is detected in the cell `Multiple terms detected for term: x||y||z in field <spreadsheet text value>` and search proceeds as above.
- `No ontology was found for this term. Please input it manually`: Type an alternate text description to search.
    
#### Ideas for future development
- ensure zooma matches are a child term before automatically matching (not sure if necessary)
- enable ability to specify confidence level
- review datasource
- enable searching by field, can search with tab between field type and text field to narrow search

### move_data_from_insdc.py

### MVP_timestamps_desciptor_fix.ipynb

### submit_project_from_doi.py

This is deprecated as it can now be done directly in the production ui.

### get uuid map per twin project.py

Get csv with `entity`, `id`, `ma_uuid`, `oa_uuid` for twin project described in #1430 . Provide MA and OA spreadsheets with uuids to produce mapping csv.