import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

external_stylesheets = [
    dbc.themes.FLATLY,
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css",
    #"/assets/style.css"  # Ścieżka do pliku CSS w folderze assets
]

# Inicjalizacja aplikacji
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True)

# Dodane dla wdrożeń, np. na Heroku
server = app.server

