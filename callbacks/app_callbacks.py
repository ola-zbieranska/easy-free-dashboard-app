import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import ALL
from layouts.home import get_home_page as home_page
from layouts.create_page import get_create_page as create_page
from layouts.documentation_page import get_documentation_page as documentation_page
from layouts.check_data_page import get_check_data_page as check_data_page
from layouts.publish_page import get_publish_page as publish_page
from layouts.vizualize_page import get_vizualize_page as vizualize_page

def register_app_callbacks(app):
    @app.callback(
        [Output('theme-link', 'href'), Output('theme-dropdown', 'label'), Output('page-content', 'className')],
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

    @app.callback(
        Output('tabs-content-example', 'children'),
        Input('tabs-example', 'value')
    )
    def render_content(tab):
        if tab == 'tab-1':
            return [dcc.Textarea(id='data-input', placeholder="Paste your copied data here...", style={'width': '100%', 'height': 200})]
        elif tab == 'tab-2':
            return [dcc.Upload(id='upload-data', children=html.Div(['Drag and Drop or ', html.A('Select Files')]), style={'width': '100%', 'height': '60px', 'lineHeight': '60px', 'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px 0'})]
        elif tab == 'tab-3':
            return [dcc.Input(id='google-sheet-url', type='url', placeholder='Enter Google Sheet URL', style={'width': '100%', 'margin-top': '10px'})]
        return []