import dash
import dash_bootstrap_components as dbc

# Inicjalizacja aplikacji

app = dash.Dash(__name__)

# Dodanie stylów Bootstrap

app.external_stylesheets = [dbc.themes.FLATLY]

# Layout aplikacji

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([]),
        dbc.Col([])
    ])
], fluid=True)

# Run the app

if __name__ == '__main__':
    app.run_server(debug=True)
