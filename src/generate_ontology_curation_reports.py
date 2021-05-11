
import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import os
import tempfile
import requests as rq
import glob

def get_label_from_iri(iri):
    request_url = "http://www.ebi.ac.uk/ols/api/terms?iri={}".format(iri)
    response = rq.get(request_url)
    if response:
        response_json = response.json()
        label = response_json['_embedded']['terms'][0]['label']
        return label


def summarise_by_curation(pd_df):
    grouped_df = pd_df.groupby(['BIOENTITY', 'PROPERTY_TYPE', 'SEMANTIC_TAG'], as_index=False)['PROPERTY_VALUE'].apply(lambda x: '\n'.join(list(set(x)))).reset_index()
    grouped_df['curation_count'] = grouped_df['PROPERTY_VALUE'].apply(lambda x: x.count("\n") + 1)
    grouped_df = grouped_df.sort_values(by=["curation_count"], ascending=False, ignore_index=True)
    # grouped_df['SEMANTIC_TAG'] = grouped_df['SEMANTIC_TAG'].apply(lambda x: get_label_from_iri(x) + "\n" + x)
    return grouped_df


def summarise_by_project_curation(pd_df):
    grouped_df = pd_df.groupby(['STUDY', 'BIOENTITY', 'PROPERTY_TYPE', 'SEMANTIC_TAG'], as_index=False)['PROPERTY_VALUE'].apply(
        lambda x: '\n'.join(list(set(x)))).reset_index()
    grouped_df['curation_count'] = grouped_df['PROPERTY_VALUE'].apply(lambda x: x.count("\n") + 1)
    grouped_df = grouped_df.sort_values(by=["curation_count"], ascending=False, ignore_index=True)
    return grouped_df


def make_dash_table(pd_df, id_string, dash_table):
    this_table = dash_table.DataTable(
        id='{}-datatable'.format(id_string),
        style_cell={
            'whiteSpace': 'pre-line',
            'height': 'auto',
            'textAlign': 'left'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": False} for i in pd_df.columns
        ],
        data=pd_df.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current=0,
        page_size=10,
    )
    return this_table


os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()

mapping_files = glob.glob('outputs/*_property_mappings.tsv')
recent_zooma_df = pd.read_csv(max(mapping_files, key=os.path.getctime), sep="\t")
summarised_recent = summarise_by_curation(recent_zooma_df)
summarised_recent_per_project = summarise_by_project_curation(recent_zooma_df)
full_zooma_df = pd.read_csv("outputs/current_zooma_import.txt", sep="\t", index_col=False)
summarised_full = summarise_by_curation(full_zooma_df)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3(children="Summarised table of curations from most recent harvest per project"),
    make_dash_table(summarised_recent_per_project, "summarised-recent-per-project", dash_table),
    html.H3(children="Summarised table of curations from most recent harvest"),
    make_dash_table(summarised_recent, "summarised-recent", dash_table),
    html.H3(children="Summarised table of curations from full ZOOMA file"),
    make_dash_table(summarised_full, "summarised-full", dash_table),
    html.H3(children="Full table of curations from most recent harvest"),
    make_dash_table(recent_zooma_df, "recent-curations", dash_table),
    html.Div(id='recent-curations-datatable-container'),
    html.H3(children="Full table of curations from full ZOOMA data source"),
    make_dash_table(full_zooma_df, "full-curations", dash_table),
    html.Div(id='full-curations-datatable-container')
])


def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]


if __name__ == '__main__':
    app.run_server(debug=True)
