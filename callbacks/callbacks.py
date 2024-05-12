from dash.dependencies import Input, Output, State
from dash import html
import dash_bootstrap_components as dbc
from app import app
from layouts.home import get_layout as home_layout
from layouts.first_page import get_first_page as first_page
@app.callback(
    Output('theme-link', 'href'),
    Input('theme-toggle', 'n_clicks'),
    State('theme-store', 'data')
)
def update_theme(n_clicks, data):
    if n_clicks is not None:
        # Zmiana tematu między jasnym a ciemnym w zależności od liczby kliknięć
        data['theme'] = dbc.themes.DARKLY if n_clicks % 2 != 0 else dbc.themes.FLATLY
    return data['theme']

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/home' or pathname == '/':
        return home_layout()
    elif pathname == '/first-page':
        return first_page()
    else:
        return html.Div('404 Not Found', style={'margin-top': '20px', 'text-align': 'center'})