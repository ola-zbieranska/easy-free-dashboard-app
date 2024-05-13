import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from components.navbar import get_navbar
from callbacks.callbacks import *

# Ustawienie głównego układu aplikacji
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='theme-store', data={'theme': dbc.themes.FLATLY}),  # Przechowywanie obecnego tematu
    html.Link(id='theme-link', rel='stylesheet', href=dbc.themes.FLATLY),  # Link do arkusza stylów motywu
    dbc.Container([
        get_navbar(),
        html.Div(id='page-content'),
    ], fluid=True)
])

# Uruchomienie
if __name__ == '__main__':
    app.run_server(debug=True)