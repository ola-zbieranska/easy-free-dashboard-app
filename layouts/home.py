import dash_bootstrap_components as dbc
from dash import html, dcc
def get_home_page():
    layout = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Create custom charts and dashboard in an easy & free way."),
                html.P("Easy Dashboard takes your data from spreadsheets to shareable graphics — no coding necessary. It’s free & no sign-up is required!"),
                dbc.Button("Create", color="primary", className="me-1"),
                html.P("Check out tutorials and tips on how to create custom charts and dashboard."),
                dbc.Button("Tutorials", color="primary", className="me-2"),
            ]))
        )
    ])
    return layout