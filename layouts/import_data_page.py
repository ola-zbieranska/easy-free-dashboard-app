import dash_bootstrap_components as dbc
from dash import html, dcc

def get_import_data_page():
    import_data_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.P("Import Google Sheet page in progres.")
            ]))
        )
    ])
    return import_data_page