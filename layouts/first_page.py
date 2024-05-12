import dash_bootstrap_components as dbc
from dash import html, dcc
from components.navbar import get_navbar

def get_first_page():
    first_page = html.Div([
        html.H1("Create custom charts and dashboard in an easy & free way."),
        html.P("Easy Dashboard takes your data from spreadsheets to shareable graphics — no coding necessary. It’s free & no sign-up is required."),
    ])
    return first_page