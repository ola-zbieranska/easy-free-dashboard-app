
import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc
from layouts.home import get_home_page as home_page
from layouts.create_page import get_create_page as create_page
from layouts.documentation_page import get_documentation_page as documentation_page
from layouts.check_data_page import get_check_data_page as check_data_page
from layouts.publish_page import get_publish_page as publish_page
from layouts.vizualize_page import get_vizualize_page as vizualize_page

def register_app_callbacks(app):
    @app.callback(
        [Output('data-input', 'style'),
         Output('upload-data', 'style'),
         Output('google-sheet-url', 'style')],
        Input('tabs-example', 'value')
    )
    def render_content(tab):
        style_hide = {'display': 'none'}
        style_show = {'display': 'block', 'width': '100%', 'height': '200px'}

        if tab == 'tab-1':
            return style_show, style_hide, style_hide
        elif tab == 'tab-2':
            return style_hide, {'display': 'block', 'width': '100%', 'height': '60px', 'lineHeight': '60px',
                                'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                                'textAlign': 'center', 'margin': '10px 0'}, style_hide
        elif tab == 'tab-3':
            return style_hide, style_hide, {'display': 'block', 'width': '100%', 'height': '40px', 'margin-top': '10px'}
        return style_hide, style_hide, style_hide

    @app.callback(
        Output('theme-link', 'href'),
        Output('theme-dropdown', 'label'),
        Output('page-content', 'className'),
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
            icon = html.I(className="bi bi-moon-fill")
            class_name = "dark-mode"
        else:
            new_theme = dbc.themes.FLATLY
            icon = html.I(className="bi bi-brightness-high-fill")
            class_name = "light-mode"

        data['theme'] = new_theme
        return new_theme, icon, class_name

    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_pages(pathname):
        if pathname == '/' or pathname == '/home':
            return home_page()
        elif pathname == '/create-page':
            return create_page()
        elif pathname == '/documentation':
            return documentation_page()
        elif pathname == '/check-data-page':
            return check_data_page()
        elif pathname == '/vizualize-page':
            return vizualize_page()
        elif pathname == '/publish-page':
            return publish_page()
        else:
            return html.H1('404 - Page not found')