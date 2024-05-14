import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

external_stylesheets = [
    dbc.themes.FLATLY,
    "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.8.1/font/bootstrap-icons.min.css",
    "/assets/style.css"
]

# Inicjalizacja aplikacji
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True)

# Dodane dla wdrożeń, np. na Heroku
server = app.server

