from dash.dependencies import Input, Output, State
from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app
from layouts.home import get_home_page as home_page
from layouts.first_page import get_first_page as first_page
from layouts.documentation_page import get_documentation_page as documentation_page
@app.callback(
    Output('theme-link', 'href'),
    Input('theme-toggle', 'n_clicks'),
    State('theme-store', 'data')
)
def update_theme(n_clicks, data):
    if n_clicks is not None:
        # Zmiana motywu między jasnym a ciemnym w zależności od liczby kliknięć
        data['theme'] = dbc.themes.DARKLY if n_clicks % 2 != 0 else dbc.themes.FLATLY
    return data['theme']

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_pages(pathname):
    if pathname == '/home':
        return home_page()  # Funkcja zwracająca layout strony głównej
    elif pathname == '/first-page':
        return first_page()  # Funkcja zwracająca layout pierwszej strony
    #elif pathname == '/blog':
        #return get_blog_page()  # Funkcja zwracająca layout bloga
    elif pathname == '/documentation':
        return documentation_page()  # Funkcja zwracająca layout dokumentacji
    else:
        return '404'  # Strona nie znaleziona