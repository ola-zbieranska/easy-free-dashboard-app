import dash
import dash_bootstrap_components as dbc
from dash import html
from components.navbar import get_navbar
from components.sidebar import get_sidebar
from layouts.home import get_layout as home_layout
from layouts.first_page import get_first_page as first_page
from callbacks.callbacks import *

# Ustawienie głównego układu aplikacji
app.layout = html.Div([
    dcc.Store(id='theme-store', data={'theme': dbc.themes.FLATLY}),  # Przechowywanie obecnego tematu
    html.Link(id='theme-link', rel='stylesheet', href=dbc.themes.FLATLY),  # Link do arkusza stylów motywu
    dbc.Container([
        get_navbar(),  # Navbar już zawiera przycisk zmiany motywu
        get_sidebar(),
        html.Div(id='page-content')
    ], fluid=True)
])

# Uruchomienie
if __name__ == '__main__':
    app.run_server(debug=True)