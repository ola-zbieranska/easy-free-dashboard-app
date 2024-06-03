import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, callback_context
import pandas as pd
import base64
import io
import requests
import plotly.express as px
from io import StringIO
from .maps import register_map_callbacks
from layouts.home import get_home_page as home_page
from layouts.first_page import get_first_page as first_page
from layouts.documentation_page import get_documentation_page as documentation_page
from layouts.check_describe_page import get_check_and_describe_page as check_and_describe_page
from layouts.publish_page import get_publish_page as publish_page
from layouts.vizualize_page import get_vizualize_page as vizualize_page

def register_callbacks(app):
    register_map_callbacks(app)

    # Callback do zmiany motywu
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

    # Callback do obsługi get_copy_paste_data
    @app.callback(
        Output('output-data', 'children'),
        Input('check-data', 'n_clicks'),
        State('data-input', 'value')
    )
    def update_output_copy_paste(n_clicks, value):
        if n_clicks is None or not value:
            return ""

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

    # Callback do obsługi get_upload_data
    @app.callback(
        Output('output-data-upload', 'children'),
        Input('proceed-to-check', 'n_clicks'),
        State('upload-data', 'contents'),
        State('upload-data', 'filename'),
        State('upload-data', 'last_modified')
    )
    def update_output_upload(n_clicks, contents, filename, date):
        if n_clicks is None or contents is None:
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
            return html.Div(['There was an error processing this file.'])

    # Callback do obsługi importowania z Google Sheets
    @app.callback(
        Output('output-url', 'children'),
        Input('check-google-sheet', 'n_clicks'),
        State('google-sheet-url', 'value')
    )
    def update_output_google_sheet(n_clicks, url):
        if n_clicks is None or not url:
            return ""

        try:
            if 'docs.google.com/spreadsheets/d/' in url:
                csv_url = url.replace('/edit#gid=', '/export?format=csv&gid=')
            else:
                return html.Div([html.P("Invalid Google Sheet URL. Please provide a valid URL.")])

            response = requests.get(csv_url)
            df = pd.read_csv(io.StringIO(response.text))

            return html.Div([
                html.H5("Data from Google Sheet:"),
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

    # Callback do renderowania wykresu na podstawie wybranego przycisku
    @app.callback(
        [Output('graph-output-bar', 'figure'),
         Output('graph-output-bar', 'style')],
        [Input('bar-chart', 'n_clicks')],
        State('data-input', 'value')
    )
    def render_bar_chart(bar_clicks, data_value):
        if not bar_clicks or not data_value:
            return {}, {'display': 'none'}

        df = pd.read_csv(StringIO(data_value))
        fig = px.bar(df, x='sepal_width', y='sepal_length', title='Bar Chart')
        return fig, {'display': 'block'}

    @app.callback(
        [Output('graph-output-pie', 'figure'),
         Output('graph-output-pie', 'style')],
        [Input('pie-chart', 'n_clicks')],
        State('data-input', 'value')
    )
    def render_pie_chart(pie_clicks, data_value):
        if not pie_clicks or not data_value:
            return {}, {'display': 'none'}

        df = pd.read_csv(StringIO(data_value))
        fig = px.pie(df, names='species', values='sepal_length', title='Pie Chart')
        return fig, {'display': 'block'}

    @app.callback(
        [Output('graph-output-line', 'figure'),
         Output('graph-output-line', 'style')],
        [Input('line-chart', 'n_clicks')],
        State('data-input', 'value')
    )
    def render_line_chart(line_clicks, data_value):
        if not line_clicks or not data_value:
            return {}, {'display': 'none'}

        df = pd.read_csv(StringIO(data_value))
        fig = px.line(df, x='sepal_width', y='sepal_length', title='Line Chart')
        return fig, {'display': 'block'}

    @app.callback(
        [Output('graph-output-scatter', 'figure'),
         Output('graph-output-scatter', 'style')],
        [Input('scatter-plot', 'n_clicks')],
        State('data-input', 'value')
    )
    def render_scatter_plot(scatter_clicks, data_value):
        if not scatter_clicks or not data_value:
            return {}, {'display': 'none'}

        df = pd.read_csv(StringIO(data_value))
        fig = px.scatter(df, x='sepal_width', y='sepal_length', title='Scatter Plot')
        return fig, {'display': 'block'}

    @app.callback(
        [Output('graph-output-area', 'figure'),
         Output('graph-output-area', 'style')],
        [Input('area-chart', 'n_clicks')],
        State('data-input', 'value')
    )
    def render_area_chart(area_clicks, data_value):
        if not area_clicks or not data_value:
            return {}, {'display': 'none'}

        df = pd.read_csv(StringIO(data_value))
        fig = px.area(df, x='sepal_width', y='sepal_length', title='Area Chart')
        return fig, {'display': 'block'}

    # Callback do renderowania tabeli
    @app.callback(
        [Output('table-output', 'data'), Output('table-output', 'columns'), Output('table-output', 'style_table')],
        Input('table', 'n_clicks'),
        State('data-input', 'value')
    )
    def render_table(table_clicks, data_value):
        if table_clicks is None or not data_value:
            return [], [], {'display': 'none'}

        df = pd.read_csv(StringIO(data_value))
        columns = [{"name": col, "id": col} for col in df.columns]
        data = df.to_dict('records')
        return data, columns, {'display': 'block'}

    # Callback do wyświetlania stron na podstawie ścieżki URL
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/' or pathname == '/home':
            return home_page()
        elif pathname == '/first-page':
            return first_page()
        elif pathname == '/documentation':
            return documentation_page()
        elif pathname == '/check-and-describe-page':
            return check_and_describe_page()
        elif pathname == '/vizualize-page':
            return vizualize_page()
        elif pathname == '/publish-page':
            return publish_page()
        else:
            return html.H1('404 - Page not found')