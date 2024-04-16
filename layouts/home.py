import dash_bootstrap_components as dbc
from dash import html

# Definicja głównego układu dla strony głównej
def get_layout():
    layout = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div("Easy Dashboard"), width=12)
        )
    ], fluid=True)
    return layout