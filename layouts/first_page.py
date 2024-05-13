import dash_bootstrap_components as dbc
from dash import html, dcc

def get_first_page():
    first_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Create custom charts and dashboard in an easy & free way."),
                html.P("If you need help learn how to create your first chart step by step click below to check out tutorials and documentation."),
                dbc.Button("Learn more", color="primary", href="/documentation", className="me-1")
            ]))
        )
    ])
    return first_page
