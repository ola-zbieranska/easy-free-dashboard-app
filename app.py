import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Inicjalizacja aplikacji

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

app.layout = html.Div([
    dbc.Button("Zmień temat", id="theme-toggle", n_clicks=0),
    dcc.Store(id='theme-store', data={'theme': dbc.themes.FLATLY}),  # Przechowywanie obecnego tematu
    html.Link(id='theme-link', rel='stylesheet', href=dbc.themes.FLATLY)  # Link do arkusza stylów
])



server = app.server

