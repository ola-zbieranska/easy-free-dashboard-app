import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Inicjalizacja aplikacji
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# Dodane dla wdrożeń, np. na Heroku
server = app.server

