import argparse
import pandas as pd

"""
This is a script to map ID values of two spreadsheets and provide 
the UUID of each entity in each spreadsheet.

We might need to have two projects describing the same experiment
(one for OA and one for MA), thus we might need to keep track of the mapping
to make sure that future updates are done on both values.
"""

def define_parser():
    parser = argparse.ArgumentParser(description="Parser for the arguments")
    parser.add_argument("-ma", "--ma_path", action="store",
                        type=str, required=True,
                        help="MA spreadsheet path")
    parser.add_argument("-oa", "--oa_path", action="store",
                        type=str, required=True,
                        help="OA spreadsheet path")
    parser.add_argument("-out", "--output_path", action="store",
                        type=str, required=False, default='ma_oa_uuid_mapping.csv',
                        help="Output csv file path")
    return parser

def get_id_col_from_sheet(sheet_name):
    if 'Project -' in sheet_name or 'Schema' in sheet_name:
        return False
    if 'Project' == sheet_name:
        return True
    if 'protocol' in sheet_name.lower():
        return f"{sheet_name.lower().replace(' ', '_')}.protocol_core.protocol_id"
    if 'file' in sheet_name.lower():
        return f"{sheet_name.lower().replace(' ', '_')}.file_core.file_name"
    return f"{sheet_name.lower().replace(' ', '_')}.biomaterial_core.biomaterial_id"

def add_project(ma_df, oa_df):
    uuid_col = 'project.uuid'
    if 'Project' not in ma_df or 'Project' not in oa_df:
        return pd.DataFrame()
    if uuid_col not in ma_df['Project'] or uuid_col not in oa_df['Project']:
        return pd.DataFrame()
    return pd.DataFrame({'id': [None], 
                         'MA_uuid': ma_df['Project'][uuid_col].values, 
                         'OA_uuid': oa_df['Project'][uuid_col].values, 
                         'entity': ['project']})

def get_uuid_col_from_sheet(sheet_name):
    return f"{sheet_name.lower().replace(' ', '_')}.uuid"

def check_cols_in_both(id_col, uuid_col, ma_sheet, oa_sheet, sheet_name):
    check_dict = {name: col for col in [id_col, uuid_col] for name, sheet in {'MA': ma_sheet, 'OA': oa_sheet}.items() if col not in sheet}
    if check_dict:
        raise ValueError(f"{list(check_dict.values())} not found in MA spreadsheet in tab {sheet_name} of the {list(check_dict.keys())} sheet")

def check_same_id_values(id_col, ma_sheet, oa_sheet, sheet_name):
    if set(ma_sheet[id_col]) != set(oa_sheet[id_col]):
        raise ValueError(f"Not matching ID {id_col} values in {sheet_name}")

def all_uuid(sheet):
    return sheet.isna().any(axis=None)

def check_uuid_values(ma_sheet, oa_sheet, uuid_col):
    empty_sheet = next((name for name, sheet in {"MA": ma_sheet, "OA": oa_sheet}.items() if all_uuid(sheet[uuid_col])), None)
    if empty_sheet:
        raise ValueError(f"Empty {uuid_col} value in {empty_sheet}.")

def main(ma_path, oa_path, output_path):
    ma_df = pd.read_excel(ma_path, sheet_name=None, skiprows=[0,1,2,4])
    oa_df = pd.read_excel(oa_path, sheet_name=None, skiprows=[0,1,2,4])

    mapping_df = pd.DataFrame()

    for sheet_name, ma_sheet in ma_df.items():
        id_col = get_id_col_from_sheet(sheet_name)
        if sheet_name in oa_df and id_col:
            oa_sheet = oa_df[sheet_name]
            uuid_col = get_uuid_col_from_sheet(sheet_name)
            check_uuid_values(ma_sheet, oa_sheet, uuid_col)
            if sheet_name != 'Project':
                check_cols_in_both(id_col, uuid_col, ma_sheet, oa_sheet, sheet_name)
                check_same_id_values(id_col, ma_sheet, oa_sheet, sheet_name)
                cols_dict = {id_col: 'id', f"{uuid_col}_x": 'MA_uuid', f"{uuid_col}_y": 'OA_uuid'}
                merger_df = ma_sheet[[id_col, uuid_col]].drop_duplicates()\
                    .merge(oa_sheet[[id_col, uuid_col]].drop_duplicates(), on = id_col)\
                    .rename(columns=cols_dict)
            else: 
                merger_df = add_project(ma_df, oa_df)
            merger_df['entity'] = sheet_name
            mapping_df = pd.concat([mapping_df, merger_df], axis=0)
        elif sheet_name not in oa_df:
            print(f"Skipping {sheet_name} missing from OA spreadsheet")
    mapping_df[['entity', 'id', 'MA_uuid', 'OA_uuid']].to_csv(output_path, index=False)
    print(f'printed uuid mapping into {output_path}')


if __name__ == "__main__":
    args = define_parser().parse_args()
    main(ma_path=args.ma_path, oa_path=args.oa_path, output_path=args.output_path)