
import dash
from dash import callback_context
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from app import app
import base64
import io
from io import StringIO
from layouts.home import get_home_page as home_page
from layouts.first_page import get_first_page as first_page
from layouts.first_page import get_copy_paste_data, get_upload_data, get_import_data
from layouts.documentation_page import get_documentation_page as documentation_page
from layouts.check_describe_page import get_check_and_describe_page as check_and_describe_page
from layouts.vizualize_page import get_vizualize_page as vizualize_page


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
    elif pathname == '/vizualize-page':
        return vizualize_page()
    else:
        return '404'


# callback do obsługi dcc.Tabs na first page - do wywalenia po zmianach
app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    #if tab == 'tab-1':
        #return get_copy_paste_data()
    #elif tab == 'tab-2':
        #return get_upload_data()
    if tab == 'tab-3':
        return get_import_data()

# callback do obsługi get_copy_paste_data

@app.callback(
    Output('output-data', 'children'),
    Input('proceed-to-check', 'n_clicks'),
    State('data-input', 'value')
)
def update_output(n_clicks, value):
    if n_clicks is None or not value:
        return ""

    # Przetwarzanie danych
    try:
        df = pd.read_csv(StringIO(value))
        return html.Div([
            html.H5("Twoje dane:"),
            dcc.Graph(
                figure={
                    'data': [{'x': df.columns, 'y': df.iloc[0], 'type': 'bar'}],
                    'layout': {'title': 'Podgląd danych'}
                }
            )
        ])
    except Exception as e:
        return html.Div([
            html.H5("Wystąpił błąd przy przetwarzaniu danych:"),
            html.P(str(e))
        ])

# callback do obsługi get_upload_data

@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified')
)
def update_output(contents, filename, date):
    if contents is None:
        return html.Div([
            'No file uploaded yet.'
        ])

    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Zakładamy, że dane są w formacie CSV
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Zakładamy, że dane są w formacie Excel
            df = pd.read_excel(io.BytesIO(decoded))
        else:
            return html.Div([
                'Unsupported file format.'
            ])

        return html.Div([
            html.H5(filename),
            dcc.Graph(
                figure={
                    'data': [{'x': df.columns, 'y': df.iloc[0], 'type': 'bar'}],
                    'layout': {'title': 'Podgląd danych'}
                }
            )
        ])
    except Exception as e:
        return html.Div([
            'There was an error processing this file.'
        ])
