import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from components.navbar import get_navbar as navbar
from callbacks.callbacks import *
from app import app

# Ustawienie głównego układu aplikacji
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar(),
    dcc.Store(id='theme-store', data={"theme": dbc.themes.FLATLY}),
    html.Link(id='theme-link', rel='stylesheet', href=dbc.themes.FLATLY),
    html.Div(id='page-content', className="light-mode")
])
if __name__ == '__main__':
    app.run_server(debug=True)