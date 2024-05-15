import dash_bootstrap_components as dbc
from dash import html

def get_documentation_page():
    sidebar = html.Div(
        [
            html.P("Useful links for documentation:", className="lead"),
            dbc.Nav(
                [
                    dbc.NavLink("Introduction", href="/documentation#introduction", active="exact"),
                    dbc.NavLink("Setup", href="/documentation#setup", active="exact"),
                    dbc.NavLink("Advanced Topics", href="/documentation#advanced", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        className="sidebar"
    )

    content = html.Div(
        [
            html.H1("Learn more about creating custom charts and dashboard in an easy & free way."),
            html.P("Here you can find extensive documentation on how to use the Easy Dashboard and create your charts.")
        ],
        style={"margin-left": "270px", "padding": "20px"}
    )

    documentation_page = html.Div([sidebar, content])

    return documentation_page