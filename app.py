import dash
import dash_bootstrap_components as dbc

# Inicjalizacja aplikacji

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server  # Umożliwia wdrożenie na serwerach
