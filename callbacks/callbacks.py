import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, callback_context
import pandas as pd
import base64
import io
import requests
import plotly.express as px
from dash import dash_table
from io import StringIO
from .maps import register_map_callbacks
from layouts.home import get_home_page as home_page
from layouts.create_page import get_create_page as create_page
from layouts.documentation_page import get_documentation_page as documentation_page
from layouts.check_describe_page import get_check_and_describe_page as check_and_describe_page
from layouts.publish_page import get_publish_page as publish_page
from layouts.vizualize_page import get_vizualize_page as vizualize_page
from layouts.create_page import get_copy_paste_data, get_upload_data, get_import_data

def register_callbacks(app):
    from .maps import register_map_callbacks
    register_map_callbacks(app)

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

    @app.callback(Output('tabs-content-example', 'children'),
                  Input('tabs-example', 'value'))
    def render_content(tab):
        if tab == 'tab-1':
            return get_copy_paste_data()
        elif tab == 'tab-2':
            return get_upload_data()
        elif tab == 'tab-3':
            return get_import_data()

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
                html.H5("Wystąpił błąd przy przetwarzaniu danych:"),
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
                html.H5("Wystąpił błąd przy przetwarzaniu danych:"),
                html.P(str(e))
            ])
    @app.callback(
        Output('graph-output-bar', 'figure'),
        Input('bar-chart', 'n_clicks'),
        State('data-input', 'value'),
        State('template-dropdown', 'value')
    )
    def render_bar_chart(bar_clicks, data_value, template):
        if not bar_clicks:
            return {}

        df = pd.read_csv(StringIO(data_value))
        fig = px.bar(df, x='sepal_width', y='sepal_length', title='Bar Chart', template=template)
        return fig

    @app.callback(
        Output('graph-output-pie', 'figure'),
        Input('pie-chart', 'n_clicks'),
        State('data-input', 'value'),
        State('template-dropdown', 'value')
    )
    def render_pie_chart(pie_clicks, data_value, template):
        if not pie_clicks:
            return {}

        df = pd.read_csv(StringIO(data_value))
        fig = px.pie(df, names='species', values='sepal_length', title='Pie Chart', template=template)
        return fig

    @app.callback(
        Output('graph-output-line', 'figure'),
        Input('line-chart', 'n_clicks'),
        State('data-input', 'value'),
        State('template-dropdown', 'value')
    )
    def render_line_chart(line_clicks, data_value, template):
        if not line_clicks:
            return {}

        df = pd.read_csv(StringIO(data_value))
        fig = px.line(df, x='sepal_width', y='sepal_length', title='Line Chart', template=template)
        return fig

    @app.callback(
        Output('graph-output-scatter', 'figure'),
        Input('scatter-plot', 'n_clicks'),
        State('data-input', 'value'),
        State('template-dropdown', 'value')
    )
    def render_scatter_plot(scatter_clicks, data_value, template):
        if not scatter_clicks:
            return {}

        df = pd.read_csv(StringIO(data_value))
        fig = px.scatter(df, x='sepal_width', y='sepal_length', title='Scatter Plot', template=template)
        return fig

    @app.callback(
        Output('graph-output-area', 'figure'),
        Input('area-chart', 'n_clicks'),
        State('data-input', 'value'),
        State('template-dropdown', 'value')
    )
    def render_area_chart(area_clicks, data_value, template):
        if not area_clicks:
            return {}

        df = pd.read_csv(StringIO(data_value))
        fig = px.area(df, x='sepal_width', y='sepal_length', title='Area Chart', template=template)
        return fig

    @app.callback(
        [Output('table-output', 'data'), Output('table-output', 'columns'), Output('table-output', 'style_table')],
        Input('table', 'n_clicks'),
        State('data-input', 'value')
    )
    def render_table(table_clicks, data_value):
        if table_clicks is None:
            return [], [], {'display': 'none'}

        df = pd.read_csv(StringIO(data_value))
        columns = [{"name": col, "id": col} for col in df.columns]
        data = df.to_dict('records')
        return data, columns, {'display': 'block'}

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
        elif pathname == '/check-and-describe-page':
            return check_and_describe_page()
        elif pathname == '/vizualize-page':
            return vizualize_page()
        elif pathname == '/publish-page':
            return publish_page()
        else:
            return html.H1('404 - Page not found')