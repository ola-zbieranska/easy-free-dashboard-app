import dash_bootstrap_components as dbc
from dash import html, dcc

def get_copy_paste_data_page():
    copy_paste_data_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.P("Copy & Paste data page in progres.")
            ]))
        )
    ])
    return copy_paste_data_page