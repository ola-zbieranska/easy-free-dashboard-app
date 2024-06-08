import dash
import dash_bootstrap_components as dbc

# External stylesheets
external_stylesheets = [
    dbc.themes.FLATLY,
    "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.8.1/font/bootstrap-icons.min.css",
    "/assets/style.css"
]

# Initialize Dash application
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True)

# Added for deployments, e.g., on Heroku
server = app.server