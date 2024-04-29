from dash.dependencies import Input, Output, State
from dash import callback
from dash import dcc
from dash import html
from app import app

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
    Output('theme-link', 'href'),
    Input('theme-toggle', 'n_clicks'),
    State('theme-store', 'data')
)
def update_theme(n_clicks, data):
    if n_clicks % 2 == 0:
        data['theme'] = dbc.themes.FLATLY
    else:
        data['theme'] = dbc.themes.DARKLY
    return data['theme']