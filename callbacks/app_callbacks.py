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
    """
       Register all callbacks related to user interactions.
       Rejestruje wszystkie callbacki związane z interakcjami użytkownika.
       """
    @app.callback(
        [Output('theme-link', 'href'), Output('theme-dropdown', 'label'), Output('page-content', 'className')],
        [Input('light-mode', 'n_clicks'), Input('dark-mode', 'n_clicks')],
        State('theme-store', 'data')
    )
    def update_theme(light_clicks, dark_clicks, data):
        """
                Callback to update the application's theme to light or dark mode.
                Callback do aktualizacji motywu aplikacji na jasny lub ciemny.

                Args:
                    light_clicks (int): Number of clicks on the button to enable light mode.
                                        Liczba kliknięć przycisku do włączenia jasnego motywu.
                    dark_clicks (int): Number of clicks on the button to enable dark mode.
                                       Liczba kliknięć przycisku do włączenia ciemnego motywu.
                    data (dict): Data stored in the application state regarding the current theme.
                                 Dane przechowywane w stanie aplikacji dotyczące aktualnego motywu.

                Returns:
                    tuple: Contains the new theme, icon, and CSS class for the page.
                           Zawiera nowy motyw, ikonę i klasę CSS dla strony.
                """
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
        """
                Callback to display the appropriate page based on the current URL path.
                Callback do wyświetlania odpowiedniej strony w zależności od aktualnej ścieżki URL.

                Args:
                    pathname (str): Current URL path.
                                    Aktualna ścieżka URL.

                Returns:
                    html.Div: Content of the page corresponding to the current URL path.
                              Zawartość strony odpowiadająca aktualnej ścieżce URL.
                """
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
        """
                Callback to render content within the tabs on the data creation page.
                Callback do renderowania zawartości w zakładkach na stronie tworzenia danych.

                Args:
                    tab (str): Selected tab.
                               Wybrana zakładka.

                Returns:
                    list: List of Dash components to display in the selected tab.
                          Lista komponentów Dash do wyświetlenia w wybranej zakładce.
                """
        if tab == 'tab-1':
            return [dcc.Textarea(id='data-input', placeholder="Paste your copied data here...", style={'width': '100%', 'height': 200})]
        elif tab == 'tab-2':
            return [dcc.Upload(id='upload-data', children=html.Div(['Drag and Drop or ', html.A('Select Files')]), style={'width': '100%', 'height': '60px', 'lineHeight': '60px', 'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px 0'})]
        elif tab == 'tab-3':
            return [dcc.Input(id='google-sheet-url', type='url', placeholder='Enter Google Sheet URL', style={'width': '100%', 'margin-top': '10px'})]
        return []