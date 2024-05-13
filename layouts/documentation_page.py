import dash_bootstrap_components as dbc
from dash import html, dcc

def get_documentation_page():
    documentation_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Learn more about creating custom charts and dashboard in an easy & free way."),
                dbc.Button("Learn more", color="primary", className="me-1")
            ]))
        )
    ])
    return documentation_page