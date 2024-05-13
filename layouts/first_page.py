import dash_bootstrap_components as dbc
from dash import html, dcc

def get_first_page():
    first_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Create custom charts and dashboard in an easy & free way."),
                html.P("Easy Dashboard takes your data from spreadsheets to shareable graphics — no coding necessary. It’s free & no sign-up is required.")
            ], style={"marginLeft": "16rem"})))])
    return first_page