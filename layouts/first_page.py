import dash_bootstrap_components as dbc
from dash import html, dcc
from dash import dash_table
from dash.dependencies import Input, Output
import dash

def get_first_page():
    first_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Create custom charts and dashboard in an easy & free way.", className="display-4"),
                html.P("If you need help learn how to create your first chart step by step click below to check out tutorials and documentation.", className="lead"),
                dbc.Button("Learn more", color="primary", href="/documentation", className="me-1"),
                html.Hr(className="my-4"),
                html.H3("First Step: How do you want to upload your data?", className="mt-4")
            ]), width=8), justify="center"
        ),
        dbc.Row(
            dbc.Col(
                dcc.Tabs(id="tabs-example", value='tab-1', children=[
                    dcc.Tab(label='Copy & paste data table', value='tab-1', children=[get_copy_paste_data()], className='tab-background'),
                    dcc.Tab(label='XLS/CSV upload', value='tab-2', children=[get_upload_data()], className='tab-background'),
                    dcc.Tab(label='Connect Google Sheet', value='tab-3', children=[get_import_data()], className='tab-background')
                ]), width=12
            ), className="mt-4"
        ),
        html.Div(id='tabs-content-example'),
        dcc.Graph(id='graph-output-bar', style={'display': 'none'}),
        dcc.Graph(id='graph-output-pie', style={'display': 'none'}),
        dcc.Graph(id='graph-output-line', style={'display': 'none'}),
        dcc.Graph(id='graph-output-scatter', style={'display': 'none'}),
        dcc.Graph(id='graph-output-area', style={'display': 'none'}),
        dcc.Graph(id='graph-output', style={'display': 'none'}),
        dash_table.DataTable(id='table-output', style_table={'display': 'none'})
    ], className="mt-4")
    return first_page

def get_copy_paste_data():
    return html.Div([
        html.H2("Copy & paste your data", className="mt-4"),
        html.P("Select your data (including header row/column) in Excel or LibreOffice and paste it in the text field. You can also upload a CSV or Excel file from your computer."),
        html.P("If you just want to try Easy Dashboard, here‘s a list of some example datasets you can use:"),
        dcc.Textarea(
            id='data-input',
            placeholder="Paste your copied data here...",
            className='textarea-background',
            style={'width': '100%', 'height': 200},
        ),
        dbc.Button("Check data", id="check-data", color="primary", className="mt-2"),
        html.Div(id='output-data')
    ])

def get_upload_data():
    return html.Div([
        html.H2("Upload CSV or Excel spreadsheets.", className="mt-4"),
        html.P("In the pop-up window, select the Excel/CSV file from your computer or drag and drop the file in the window below."),
        html.P("If you just want to try Easy Dashboard, here‘s a list of some example datasets you can use:"),
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px 0'
            },
            multiple=False  # Umożliwia wgrywanie tylko jednego pliku na raz
        ),
        dbc.Button("Check data", id="proceed-to-check", color="primary", className="mt-2"),
        html.Div(id='output-data-upload')
    ])

def get_import_data():
    return html.Div([
        html.H2("Import data from Google Sheet.", className="mt-4"),
        html.P([
            "Make sure to enable ",
            html.A("Link Sharing", href="https://support.google.com/drive/answer/2494822?visit_id=1-636596603923192043-2988837136&p=link_sharing_on&hl=en&rd=1#link_sharing&zippy=%2Callow-general-access-to-the-file", target="_blank"),
            " in the Google Sheet and copy the spreadsheet URL into the text field below."
        ]),
        dcc.Input(
            id='google-sheet-url',
            type='url',
            placeholder='Enter Google Sheet URL',
            className='input-background',
            style={'width': '100%', 'margin-top': '10px'}
        ),
        dbc.Button("Check data", id="check-google-sheet", color="primary", className="mt-2"),
        html.Div(id='output-url')
    ])