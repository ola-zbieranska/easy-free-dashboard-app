import dash_bootstrap_components as dbc
from dash import html
def get_sidebar():
    sidebar = html.Div([
        html.H2("Easy Dashboard", className="display-4"),  # Tytuł sidebar
        html.Hr(),  # Linia separatora
        html.P("Navigation:", className="lead"),  # Nagłówek sekcji nawigacyjnej
        dbc.Nav([
            dbc.NavLink("Home", href="/home", active="exact"),
            dbc.NavLink("About", href="/about", active="exact"),
            dbc.NavLink("Settings", href="/settings", active="exact"),
        ], vertical=True, pills=True, className="flex-column"),  # Linki nawigacyjne
    ], style={'position': 'fixed', 'top': 0, 'left': 0, 'bottom': 0, 'width': '16rem', 'padding': '2rem', 'background-color': '#f8f9fa', 'z-index': 1000})
    return sidebar