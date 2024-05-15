
import dash
from dash import callback_context
from dash import html, Input, Output, State
import dash_bootstrap_components as dbc
from app import app
from layouts.home import get_home_page as home_page
from layouts.first_page import get_first_page as first_page
from layouts.first_page import get_copy_paste_data, get_upload_data, get_import_data
from layouts.documentation_page import get_documentation_page as documentation_page
from layouts.check_describe_page import get_check_and_describe_page as check_and_describe_page


#DropDownMenu do zmiany motywu
@app.callback(
    [Output('theme-link', 'href'), Output('theme-dropdown', 'label'), Output('page-content', 'className')],
    [Input('light-mode', 'n_clicks'), Input('dark-mode', 'n_clicks')],
    State('theme-store', 'data')
)
def update_theme(light_clicks, dark_clicks, data):
    ctx = callback_context

    if not ctx.triggered:
        button_id = 'light-mode'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'dark-mode':
        new_theme = dbc.themes.DARKLY
        icon = html.I(className="bi bi-moon-fill")
        class_name = "dark-mode"
    else:
        new_theme = dbc.themes.FLATLY
        icon = html.I(className="bi bi-brightness-high-fill")
        class_name = "light-mode"

    data['theme'] = new_theme
    return new_theme, icon, class_name

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
    elif pathname == '/check-and-describe-page':
        return check_and_describe_page()
    else:
        return '404'


# callback do obsługi dcc.Tabs na first page
@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return get_copy_paste_data()
    elif tab == 'tab-2':
        return get_upload_data()
    elif tab == 'tab-3':
        return get_import_data()
