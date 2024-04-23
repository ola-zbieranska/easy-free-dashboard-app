from dash.dependencies import Input, Output, State
from dash import callback
from dash import dcc
from dash import html
from app import app

# Callback to toggle the sidebar

@app.callback(
    Output("sidebar", "className"),
    [Input("toggle-sidebar-btn", "n_clicks")],
    [State("sidebar", "className")]
)
def toggle_sidebar(n_clicks, classname):
    if n_clicks and classname == "sidebar":
        return "sidebar collapsed"
    elif n_clicks:
        return "sidebar"
    return classname


@app.callback(
    Output('body', 'className'),
    Input('theme-toggle', 'n_clicks')
)
def toggle_theme(n):
    if n % 2 == 0:  # Jeśli liczba kliknięć jest parzysta, ustaw jasny motyw
        return 'light'
    else:  # W przeciwnym razie ustaw ciemny motyw
        return 'dark'