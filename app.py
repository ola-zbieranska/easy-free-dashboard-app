import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Inicjalizacja aplikacji

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Store(id='theme-store', data={'theme': dbc.themes.FLATLY}),  # Domyslny motyw ustawiony na FLATLY
    dbc.Button("Zmień motyw", id="theme-toggle", n_clicks=0),
    # Inne elementy UI...
])


server = app.server

