import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

import base64
import io
import datetime

#-------------------------------------------------------------------------
# Load chart templates for all available Bootstrap themes
load_figure_template('LUX')

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

#-------------------------------------------------------------------------
# Components

# Górny pasek nawigacyjny
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
        # Możesz dodać więcej elementów nawigacyjnych tutaj
    ],
    brand="Easy Dashboard App",
    brand_href="#",
    color="primary",
    dark=True,
)

# Style sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "24rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "overflow-y": "auto",
}

# Style content
CONTENT_STYLE = {
    "margin-left": "26rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Style drop down box
UPLOAD_STYLE = {
    'width': '100%',
    'height': '60px',
    'lineHeight': '60px',
    'borderWidth': '1px',
    'borderStyle': 'dashed',
    'borderRadius': '5px',
    'textAlign': 'center',
    'margin-bottom': '2rem',
}

#-------------------------------------------------------------------------
# Layout

app.layout = html.Div([
    navbar,
    html.Div(style=SIDEBAR_STYLE, children=[
        html.H2("Filters", style={"padding-top": "2rem"}),
        html.Hr(),
        html.P("A simple sidebar layout with filters", className="lead"),
        dbc.Nav(
            [
                dcc.Dropdown(id='dropdown-one', options=[{"label": "test", "value": "test"}], placeholder="Select an option"),
                html.Br(),
                dcc.Dropdown(id='dropdown-two', options=[{"label": "test", "value": "test"}], placeholder="Select an option"),
                html.Br(),
                dcc.Dropdown(id='dropdown-three', options=[{"label": "test", "value": "test"}], placeholder="Select an option")
            ],
            vertical=True,
            pills=True,
        ),
    ]),
    html.Div(id='page-content', style=CONTENT_STYLE, children=[
        dcc.Upload(
            id='upload-data',
            children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
            style=UPLOAD_STYLE,
            multiple=False
        ),
        html.Div(id='output-data-upload'),
    ])
])

#-------------------------------------------------------------------------
# Callback

@app.callback(
    Output('output-data-upload', 'children'),
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename'),
     State('upload-data', 'last_modified')]
)
def update_output(contents, filename, last_modified):
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Assuming the user uploads a CSV file
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
                return html.Div([
                    html.H5(filename),
                    html.H6(datetime.datetime.fromtimestamp(last_modified)),

                    dcc.Graph(
                        figure=px.bar(df, x=df.columns[0], y=df.columns[1])
                    ),

                    html.Hr(),  # Horizontal line

                    html.Div('Raw CSV file contents:'),
                    html.Pre(contents[:200] + '...', style={
                        'whiteSpace': 'pre-wrap',
                        'wordBreak': 'break-all'
                    })
                ])
            else:
                return html.Div([
                    'This file type is not supported.'
                ])
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])
    return html.Div([
        'Upload a file to see its content.'
    ])

#-------------------------------------------------------------------------
# Run the app

if __name__ == '__main__':
    app.run_server(debug=True)
