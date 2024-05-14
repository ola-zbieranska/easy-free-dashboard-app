import dash_bootstrap_components as dbc
from dash import html, dcc

def get_upload_data_page():
    upload_data_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Upload CSV or Excel spreadsheets."),
                html.P("In the pop-up window, select the Excel/CSV file from your computer or drag and drop the file in the window below."),
                html.P("If you just want to try Easy Dashboard, here‘s a list of some example datasets you can use:")
            ]))
        )
    ])
    return upload_data_page