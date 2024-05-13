import dash_bootstrap_components as dbc
from dash import html, dcc

def get_first_page():
    first_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Create custom charts and dashboard in an easy & free way."),
                dbc.Button("Create", color="primary", className="me-1")
            ]))
        )
    ])
    return first_page
