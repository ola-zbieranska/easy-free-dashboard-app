import dash
from dash import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from io import StringIO
import base64
import io
import requests
import plotly.express as px
from dash import html, dcc
import plotly.graph_objects as go
from dash import dash_table
from layouts.home import get_home_page as home_page
from layouts.create_page import get_create_page as create_page
from layouts.documentation_page import get_documentation_page as documentation_page
from layouts.check_data_page import get_check_data_page as check_data_page
from layouts.publish_page import get_publish_page as publish_page
from layouts.vizualize_page import get_vizualize_page as vizualize_page
from callbacks.map_helpers import map_country_names_to_iso_alpha3, add_lat_lon, generate_scatter_map, generate_heatmap, generate_bubble_map
#from layouts.create_page import get_import_data, get_upload_data, get_copy_paste_data

def register_callbacks(app):

    @app.callback(
        Output('theme-link', 'href'),
        Output('page-content', 'className'),
        [Input('light-mode', 'n_clicks'), Input('dark-mode', 'n_clicks')],
        State('theme-store', 'data')
    )
    def update_theme(light_clicks, dark_clicks, data):
        ctx = dash.callback_context
        if not ctx.triggered:
            return data['theme'], 'light-mode'

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'dark-mode':
            new_theme = dbc.themes.DARKLY
            class_name = 'dark-mode'
        else:
            new_theme = dbc.themes.FLATLY
            class_name = 'light-mode'

        data['theme'] = new_theme
        return new_theme, class_name

    @app.callback(
        Output('tabs-content-example', 'children'),
        Input('tabs-example', 'value')
    )
    def render_content(tab):
        if tab == 'tab-1':
            return dcc.Textarea(id='data-input', style={'width': '100%', 'height': 200})
        elif tab == 'tab-2':
            return dcc.Upload(id='upload-data', children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
                              style={
                                  'width': '100%',
                                  'height': '60px',
                                  'lineHeight': '60px',
                                  'borderWidth': '1px',
                                  'borderStyle': 'dashed',
                                  'borderRadius': '5px',
                                  'textAlign': 'center',
                                  'margin': '10px 0'
                              }, multiple=False)
        elif tab == 'tab-3':
            return dcc.Input(id='google-sheet-url', type='url', placeholder='Enter Google Sheet URL', style={'width': '100%'})

    @app.callback(
        Output('output-data', 'children'),
        Input('data-input', 'value')
    )
    def update_output_copy_paste(value):
        if not value:
            return ""

        try:
            df = pd.read_csv(StringIO(value))
            return dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns],
                style_table={'display': 'block'}
            )
        except Exception as e:
            return html.Div([
                html.H5("Error processing data:"),
                html.P(str(e))
            ])

    @app.callback(
        Output('output-data-upload', 'children'),
        Input('upload-data', 'contents'),
        State('upload-data', 'filename')
    )
    def update_output_upload(contents, filename):
        if contents is None:
            return html.Div(['No file uploaded yet.'])

        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                df = pd.read_excel(io.BytesIO(decoded))
            else:
                return html.Div(['Unsupported file format.'])

            return dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns],
                style_table={'display': 'block'}
            )
        except Exception as e:
            return html.Div(['There was an error processing this file.'])

    @app.callback(
        Output('output-url', 'children'),
        Input('google-sheet-url', 'value')
    )
    def update_output_google_sheet(url):
        if not url:
            return ""

        try:
            if 'docs.google.com/spreadsheets/d/' in url:
                csv_url = url.replace('/edit#gid=', '/export?format=csv&gid=')
            else:
                return html.Div([html.P("Invalid Google Sheet URL. Please provide a valid URL.")])

            response = requests.get(csv_url)
            df = pd.read_csv(io.StringIO(response.text))

            return dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns],
                style_table={'display': 'block'}
            )
        except Exception as e:
            return html.Div([
                html.H5("Error processing data:"),
                html.P(str(e))
            ])

    @app.callback(
        Output('stored-data', 'data'),
        [Input('data-input', 'value'),
         Input('upload-data', 'contents'),
         Input('google-sheet-url', 'value')],
        [State('upload-data', 'filename')]
    )
    def store_data(copy_paste_data, upload_contents, google_sheet_url, upload_filename):
        if copy_paste_data:
            try:
                df = pd.read_csv(StringIO(copy_paste_data))
                return df.to_dict('records')
            except Exception as e:
                return []

        if upload_contents and upload_filename:
            content_type, content_string = upload_contents.split(',')
            decoded = base64.b64decode(content_string)
            try:
                if 'csv' in upload_filename:
                    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
                elif 'xls' in upload_filename:
                    df = pd.read_excel(io.BytesIO(decoded))
                return df.to_dict('records')
            except Exception as e:
                return []

        if google_sheet_url:
            try:
                if 'docs.google.com/spreadsheets/d/' in google_sheet_url:
                    csv_url = google_sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
                    response = requests.get(csv_url)
                    df = pd.read_csv(io.StringIO(response.text))
                    return df.to_dict('records')
            except Exception as e:
                return []

        return []

    @app.callback(
        [Output('data-table', 'data'), Output('data-table', 'columns')],
        Input('url', 'pathname'),
        State('stored-data', 'data')
    )
    def display_data_table(pathname, data):
        if pathname == '/check-data-page' and data:
            df = pd.DataFrame(data)
            columns = [{'name': col, 'id': col} for col in df.columns]
            return df.to_dict('records'), columns
        return [], []

    @app.callback(
        Output('graph-output', 'figure'),
        [Input('bar-chart', 'n_clicks'),
         Input('pie-chart', 'n_clicks'),
         Input('line-chart', 'n_clicks'),
         Input('scatter-plot', 'n_clicks'),
         Input('area-chart', 'n_clicks'),
         Input('scatter-map', 'n_clicks'),
         Input('heatmap', 'n_clicks'),
         Input('bubble-map', 'n_clicks')],
        [State('template-dropdown', 'value'),
         State('stored-data', 'data')]
    )
    def render_charts_and_maps(bar_clicks, pie_clicks, line_clicks, scatter_clicks, area_clicks, scatter_map_clicks, heatmap_clicks, bubble_map_clicks, template, data):
        ctx = dash.callback_context
        if not ctx.triggered or not data:
            return {}

        df = pd.DataFrame(data)
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'bar-chart':
            fig = px.bar(df, x=df.columns[0], y=df.columns[1], title='Bar Chart', template=template)
        elif button_id == 'pie-chart':
            fig = px.pie(df, names=df.columns[0], values=df.columns[1], title='Pie Chart', template=template)
        elif button_id == 'line-chart':
            fig = px.line(df, x=df.columns[0], y=df.columns[1], title='Line Chart', template=template)
        elif button_id == 'scatter-plot':
            fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title='Scatter Plot', template=template)
        elif button_id == 'area-chart':
            fig = px.area(df, x=df.columns[0], y=df.columns[1], title='Area Chart', template=template)
        elif button_id == 'scatter-map':
            fig = generate_scatter_map(df, template)
        elif button_id == 'heatmap':
            fig = generate_heatmap(df, template)
        elif button_id == 'bubble-map':
            size_col = df.columns[2]
            if size_col not in ['Latitude', 'Longitude']:
                fig = generate_bubble_map(df, size_col, template)
            else:
                fig = {}
        else:
            fig = {}

        return fig

    @app.callback(
        [Output('table-output', 'data'), Output('table-output', 'columns'), Output('table-output', 'style_table')],
        Input('table', 'n_clicks'),
        State('stored-data', 'data')
    )
    def render_table(table_clicks, data):
        if table_clicks and data:
            df = pd.DataFrame(data)
            columns = [{'name': col, 'id': col} for col in df.columns]
            return df.to_dict('records'), columns, {'display': 'block'}
        return [], [], {'display': 'none'}

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