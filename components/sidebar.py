import dash_bootstrap_components as dbc
from dash import html

def get_sidebar():
    sidebar = html.Div(
        [
            html.Div(
                [dbc.Button("→", id="toggle-sidebar-btn", className="toggle-button")],
                className="toggle-container"
            ),
            html.H2("Sidebar", className="display-4"),
            html.Hr(),
            html.P("A simple sidebar layout with navigation links", className="lead"),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/home", active="exact"),
                    dbc.NavLink("About", href="/about", active="exact"),
                    dbc.NavLink("Profile", href="/profile", active="exact"),
                    dbc.NavLink("Settings", href="/settings", active="exact"),
                    dbc.NavLink("Logout", href="/logout", active="exact"),
                ],
                vertical=True,
                pills=True,
                className="flex-column",
            ),
        ],
        id="sidebar",
        className="sidebar"
    )
    return sidebar