import dash_bootstrap_components as dbc
from dash import html, dcc

def get_copy_paste_data_page():
    copy_paste_data_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Copy & paste your data"),
                html.P("Select your data (including header row/column) in Excel or LibreOffice and paste it in the text field. You can also upload a CSV or Excel file from your computer."),
                html.P("If you just want to try Easy Dashboard, here‘s a list of some example datasets you can use:")
            ]))
        )
    ])
    return copy_paste_data_page