# Import packages

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import base64
import io
import datetime

#-------------------------------------------------------------------------
# Initialize the app
app = dash.Dash(__name__)

#-------------------------------------------------------------------------
# User interface for uploading files with specific style settings. Users can transfer single files
app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Przeciągnij i upuść lub ',
            html.A('wybierz plik')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Do not allow multiple files to be uploaded
        multiple=False
    ),
    html.Div(id='output-data-upload'),
])


#-------------------------------------------------------------------------
# Callback for processing the uploaded file
@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified')
)
def update_output(contents, filename, last_modified):
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Przyjmujemy, że użytkownik przesyła plik CSV
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
                return html.Div([
                    html.H5(filename),
                    html.H6(datetime.datetime.fromtimestamp(last_modified)),

                    dcc.Graph(
                        figure={
                            'data': [{'x': df[df.columns[0]], 'y': df[df.columns[1]], 'type': 'bar'}]
                        }
                    ),

                    html.Hr(),  # Linia pozioma

                    html.Div('Surowe zawartości pliku CSV:'),
                    html.Pre(contents[:200] + '...', style={
                        'whiteSpace': 'pre-wrap',
                        'wordBreak': 'break-all'
                    })
                ])
            else:
                return html.Div([
                    'Ten typ pliku nie jest obsługiwany.'
                ])
        except Exception as e:
            print(e)
            return html.Div([
                'Wystąpił błąd podczas przetwarzania pliku.'
            ])
    return html.Div([
        'Prześlij plik, aby zobaczyć jego zawartość.'
    ])



#-------------------------------------------------------------------------
# Run the app

if __name__ == '__main__':
    app.run_server(debug=True)# Import packages

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input

# Initialize the app

app = dash.Dash(__name__)

#-------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)

#df = pd.read_csv("")


#-------------------------------------------------------------------------
# App layout

app.layout = html.Div([
    html.Div(children='Hello World')
])

# Run the app

if __name__ == '__main__':
    app.run(debug=True)
