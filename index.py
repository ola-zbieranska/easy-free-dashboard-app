import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from components.navbar import get_navbar
from callbacks.callbacks import *

# Ustawienie głównego układu aplikacji
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    get_navbar(),
    dcc.Store(id='theme-store', data={"theme": dbc.themes.FLATLY}),
    html.Link(id='theme-link', rel='stylesheet', href=dbc.themes.FLATLY),
    html.Div(id='page-content', className="light-mode"),  # Dodajemy klasę 'light-mode' na początku
])

# Uruchomienie
if __name__ == '__main__':
    app.run_server(debug=True)