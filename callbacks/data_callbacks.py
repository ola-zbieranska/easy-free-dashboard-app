import dash
from dash import Input, Output, State, html
from dash.dependencies import ALL
import pandas as pd
from io import StringIO
import base64
import io
import requests
from dash import dash_table

def register_data_callbacks(app):
    @app.callback(
        Output('stored-data', 'data'),
        [Input({'type': 'dynamic-input', 'index': ALL}, 'value'),
         Input('upload-data', 'contents'),
         Input('google-sheet-url', 'value')],
        [State('upload-data', 'filename')]
    )
    def store_data(copy_paste_data, upload_contents, google_sheet_url, upload_filename):
        data = []
        if copy_paste_data and copy_paste_data[0]:
            try:
                df = pd.read_csv(StringIO(copy_paste_data[0]))
                data = df.to_dict('records')
            except Exception as e:
                print(f"Błąd podczas przetwarzania danych skopiowanych: {e}")

        if upload_contents and upload_filename:
            content_type, content_string = upload_contents.split(',')
            decoded = base64.b64decode(content_string)
            try:
                if 'csv' in upload_filename:
                    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
                elif 'xls' in upload_filename:
                    df = pd.read_excel(io.BytesIO(decoded))
                data = df.to_dict('records')
            except Exception as e:
                print(f"Błąd podczas przetwarzania przesłanego pliku: {e}")

        if google_sheet_url:
            try:
                if 'docs.google.com/spreadsheets/d/' in google_sheet_url:
                    csv_url = google_sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
                    response = requests.get(csv_url)
                    df = pd.read_csv(io.StringIO(response.text))
                    data = df.to_dict('records')
            except Exception as e:
                print(f"Błąd podczas przetwarzania Google Sheet: {e}")

        print(f"Przechowywane dane: {data}")
        return data

    @app.callback(
        Output('data-table', 'data'),
        Output('data-table', 'columns'),
        Input('url', 'pathname'),
        State('stored-data', 'data')
    )
    def display_data_table(pathname, data):
        print(f"URL pathname: {pathname}")
        print(f"Otrzymane dane: {data}")
        if pathname == '/check-data-page' and data:
            try:
                df = pd.DataFrame(data)
                columns = [{'name': col, 'id': col} for col in df.columns]
                return df.to_dict('records'), columns
            except Exception as e:
                print(f"Błąd podczas przetwarzania danych: {e}")
                return [], []
        return [], []

    @app.callback(
        Output('output-data', 'children'),
        Input({'type': 'dynamic-input', 'index': ALL}, 'value')
    )
    def update_output_copy_paste(value):
        if not value or not value[0]:
            return ""

        try:
            df = pd.read_csv(StringIO(value[0]))
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