import dash_bootstrap_components as dbc
from dash import html, dcc

def get_home_page():
    """
      Tworzy i zwraca stronę główną.
      Creates and returns the home page.
      """
    home_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Welcome to Easy Dashboard!", className="display-3"),
                html.H4("Create custom charts and dashboard in an easy & free way.", className="lead"),
                html.Hr(className="my-4"),
                html.H5("Easy Dashboard takes your data from spreadsheets to shareable graphics — no coding necessary."),
                html.H5("It’s free & no sign-up is required."),
                html.Ul([
                    html.Li("Create charts & maps quickly and easily"),
                    html.Li("Upload data from three different ways"),
                    html.Li("No software to install")
                ], className="lead"),
                dbc.Button("Create", color="primary", href="/create-page", className="me-2"),
                html.Br(),
                html.Br(),
                dbc.Button("Tutorials", color="secondary", href="/documentation", className="me-2"),
            ]), width=8)
        , justify="center")
    ], className="mt-4")
    return home_page