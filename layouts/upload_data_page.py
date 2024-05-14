import dash_bootstrap_components as dbc
from dash import html, dcc

def get_upload_data_page():
    upload_data_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.P("Import Google Sheet page in progres.")
            ]))
        )
    ])
    return upload_data_page