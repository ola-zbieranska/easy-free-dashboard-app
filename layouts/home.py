import dash_bootstrap_components as dbc
from dash import html, dcc
def get_home_page():
    layout = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Welcome to Easy Dashboard!"),
                html.H1("Create custom charts and dashboard in an easy & free way."),
                html.P("Easy Dashboard takes your data from spreadsheets to shareable graphics — no coding necessary. It’s free & no sign-up is required!"),
                html.P("Create stunning charts & maps"),
                html.P("Upload data from three different ways"),
                html.P("No software to install"),
                dbc.Button("Create", color="primary", href="/first-page", className="me-1"),
                html.P("Check out tutorials and tips on how to create custom charts and dashboard."),
                dbc.Button("Tutorials", color="primary", href="/documentation", className="me-2"),
            ]))
        )
    ])
    return layout