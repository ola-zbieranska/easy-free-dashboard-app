import pandas as pd
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

#-------------------------------------------------------------------------
# Layout

app.layout = html.Div([
    navbar,
    html.Div(style=SIDEBAR_STYLE, children=[
        html.H2("Filters", style={"padding-top": "2rem"}),
        html.Hr(),
        html.P("A simple sidebar layout with navigation and filters", className="lead"),
        dbc.Nav(
            [
                dcc.Dropdown(id='dropdown-one', options=[{"label": "Option 1", "value": "1"}], placeholder="Select an option"),
                html.Br(),
                dcc.Dropdown(id='dropdown-two', options=[{"label": "Option 2", "value": "2"}], placeholder="Select an option"),
                html.Br(),
                dcc.Dropdown(id='dropdown-three', options=[{"label": "Option 3", "value": "3"}], placeholder="Select an option"),
                html.Br(),
                dbc.Label("Dashboard Description"),
                dbc.Textarea(
                    id='textarea-dashboard-description',
                    placeholder="Enter a description for the dashboard...",
                    style={'width': '100%', 'height': '100px'},
                ),
                html.Br(),
            ],
            vertical=True,
            pills=True,
        ),
    ]),
    html.Div(id='page-content', style=CONTENT_STYLE, children=[
        # ... Tutaj możesz dodać pozostałą część layoutu strony ...
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
