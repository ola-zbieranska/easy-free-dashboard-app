import dash
from dash.dependencies import Input, Output, State
from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app
from layouts.home import get_home_page as home_page
from layouts.first_page import get_first_page as first_page
from layouts.documentation_page import get_documentation_page as documentation_page
from layouts.copy_paste_data_page import get_copy_paste_data_page as copy_paste_data_page
from layouts.upload_data_page import get_upload_data_page as upload_data_page
from layouts.import_data_page import get_import_data_page as import_data_page


#DropDownMenu do zmiany motywu
@app.callback(
    [Output('theme-link', 'href'), Output('theme-dropdown', 'label')],
    [Input('light-mode', 'n_clicks'), Input('dark-mode', 'n_clicks')],
    State('theme-store', 'data')
)
def update_theme(light_clicks, dark_clicks, data):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = 'light-mode'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'dark-mode':
        new_theme = dbc.themes.DARKLY
        icon = html.I(className="bi bi-moon")
    else:
        new_theme = dbc.themes.FLATLY
        icon = html.I(className="bi bi-brightness-high")

    data['theme'] = new_theme
    return new_theme, icon

#prawidłowe renderowanie stron
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_pages(pathname):
    if pathname == '/' or pathname == '/home':
        return home_page()
    elif pathname == '/first-page':
        return first_page()
    #elif pathname == '/blog':
        #return get_blog_page()
    elif pathname == '/documentation':
        return documentation_page()
    elif pathname == '/copy-paste-data-page':
        return copy_paste_data_page()
    elif pathname == '/upload-data-page':
        return upload_data_page()
    elif pathname == '/import-data-page':
        return import_data_page()
    else:
        return '404'

# sidebar = offcanvas
@app.callback(
    Output("offcanvas", "is_open"),
    [Input("open-sidebar", "n_clicks")],
    [State("offcanvas", "is_open")]
)
def toggle_offcanvas(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server(debug=True)