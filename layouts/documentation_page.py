import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import dash

def get_documentation_page():
    sidebar = html.Div(
        [
            html.P("Useful links for documentation:", className="lead"),
            dbc.Nav(
                [
                    dbc.NavLink("Introduction", href="/documentation#introduction", active="exact", className="sidebar-link"),
                    dbc.NavLink("Setup", href="/documentation#setup", active="exact", className="sidebar-link"),
                    dbc.NavLink("Advanced Topics", href="/documentation#advanced", active="exact", className="sidebar-link"),
                ],
                vertical=True,
                pills=True,
                className='sidebar-nav'
            ),
        ],
        className="sidebar sidebar-background"
    )

    content = html.Div(
        [
            html.P("Here you can find extensive documentation on how to use the Easy Dashboard and create your charts.", className="lead"),
            html.Hr(className="my-4"),
            html.Div(id="content-section")
        ],
        className="content"
    )

    documentation_page = html.Div([sidebar, content])

    return documentation_page