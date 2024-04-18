import dash_bootstrap_components as dbc
from dash import html

# Style for the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "margin-top": "56px",  # Dodaj odstęp na górze, zgodnie z wysokością navbar
}

def get_sidebar():
    sidebar = html.Div(
        [
            html.H2("Sidebar", className="display-4"),
            html.Hr(),
            html.P("A simple sidebar layout with navigation links" , className="lead"),
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
            ),
        ],
        style=SIDEBAR_STYLE,
    )
    return sidebar