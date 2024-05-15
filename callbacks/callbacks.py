import dash
import pandas as pd
import base64
import io
# import gspread
from dash import html, dcc, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
from app import app
#from callbacks.validation import validate_data, get_google_sheet_data, parse_upload
from layouts.home import get_home_page as home_page
from layouts.first_page import get_first_page as first_page
from layouts.documentation_page import get_documentation_page as documentation_page
from layouts.copy_paste_data_page import get_copy_paste_data_page as copy_paste_data_page
from layouts.upload_data_page import get_upload_data_page as upload_data_page
from layouts.import_data_page import get_import_data_page as import_data_page
from layouts.check_describe_page import get_check_and_describe_page as check_and_describe_page


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
    elif pathname == '/check-and-describe-page':
        return check_and_describe_page()
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

# # Callback do nawigacji między stronami
# @app.callback(
#     Output('page-content', 'children'),
#     [Input('url', 'pathname')]
# )
# def display_page(pathname):
#     if pathname == '/check-data':
#         return check_and_describe_page()
#     elif pathname == '/import-data':
#         return import_data_page()
#     elif pathname == '/upload-data':
#         return upload_data_page()
#     elif pathname == '/copy-paste-data':
#         return copy_paste_data_page()
#     else:
#         return copy_paste_data_page()

# # Callback do przetwarzania danych z wklejania
# @app.callback(
#     Output('url', 'pathname'),
#     Input('proceed-to-check', 'n_clicks'),
#     State('data-input', 'value')
# )
# def process_copy_paste_data(n_clicks, data):
#     if n_clicks is not None and data:
#         df = pd.read_csv(pd.compat.StringIO(data), sep='\t', header=0)
#         errors = validate_data(df)
#         if not errors:
#             return '/check-data'
#     return dash.no_update
#
# # Callback do przetwarzania danych z uploadu
# @app.callback(
#     Output('output-data-upload', 'children'),
#     Input('upload-data', 'contents'),
#     State('upload-data', 'filename')
# )
# def process_upload_data(contents, filename):
#     if contents is not None:
#         content_type, content_string = contents.split(',')
#         decoded = base64.b64decode(content_string)
#         try:
#             if 'csv' in filename:
#                 df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
#             elif 'xls' in filename:
#                 df = pd.read_excel(io.BytesIO(decoded))
#             errors = validate_data(df)
#             if not errors:
#                 return html.Div([
#                     html.H5("Upload successful!"),
#                     dash_table.DataTable(
#                         id='data-table',
#                         data=df.to_dict('records'),
#                         columns=[{'name': i, 'id': i} for i in df.columns],
#                         editable=True,
#                         row_deletable=True,
#                         page_size=10
#                     )
#                 ])
#         except Exception as e:
#             print(e)
#     return html.Div()

# # Callback do przetwarzania danych z Google Sheets
# @app.callback(
#     Output('output-url', 'children'),
#     Input('import-button', 'n_clicks'),
#     State('google-sheet-url', 'value')
# )
# def import_google_sheet(n_clicks, url):
#     if n_clicks is not None and url:
#         df = get_google_sheet_data(url)
#         errors = validate_data(df)
#         if not errors:
#             return html.Div([
#                 html.H5("Google Sheet Data:"),
#                 dash_table.DataTable(
#                     id='data-table',
#                     data=df.to_dict('records'),
#                     columns=[{'name': i, 'id': i} for i in df.columns],
#                     editable=True,
#                     row_deletable=True,
#                     page_size=10
#                 )
#             ])
#     return html.Div()