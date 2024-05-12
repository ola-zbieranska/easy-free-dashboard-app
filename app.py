import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Inicjalizacja aplikacji
app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.FLATLY,
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css'
])

# Dodane dla wdrożeń, np. na Heroku
server = app.server

