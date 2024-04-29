import dash
import dash_bootstrap_components as dbc

# Inicjalizacja aplikacji

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA])

server = app.server
