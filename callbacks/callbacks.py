from dash.dependencies import Input, Output, State
from dash import html
import dash_bootstrap_components as dbc
from app import app
from layouts.home import get_layout as home_layout
from layouts.first_page import get_first_page as first_page

@app.callback(
    Output("offcanvas", "is_open"),
    Output("open-close-button", "style"),
    Input("open-close-button", "n_clicks"),
    State("offcanvas", "is_open"),
)
def toggle_offcanvas(n, is_open):
    if n:
        # Odwróć strzałkę w zależności od stanu
        button_style = {"transform": "rotate(0deg)"} if not is_open else {"transform": "rotate(180deg)"}
        return not is_open, button_style
    # Jeśli przycisk nie został kliknięty, zwróć obecny stan i odpowiedni styl
    return is_open, {"transform": "rotate(180deg)"} if is_open else {"transform": "rotate(0deg)"}

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