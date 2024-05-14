import dash_bootstrap_components as dbc
from dash import html, dcc

def get_import_data_page():
    import_data_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Import data from Google Sheet."),
                html.P([
                    "Make sure to enable ",
                    html.A("Link Sharing", href="https://support.google.com/drive/answer/2494822?visit_id=1-636596603923192043-2988837136&p=link_sharing_on&hl=en&rd=1#link_sharing&zippy=%2Callow-general-access-to-the-file", target="_blank"),
                    " in the Google Sheet and copy the spreadsheet URL into the text field below."
                ]),
                dcc.Input(
                    id='google-sheet-url',
                    type='url',
                    placeholder='Enter Google Sheet URL',
                    style={'width': '100%', 'margin-top': '10px'}
                ),
                dbc.Button("Import", id="import-button", color="primary", className="mt-2"),
                html.Div(id='output-url')
            ]))
        )
    ])
    return import_data_page