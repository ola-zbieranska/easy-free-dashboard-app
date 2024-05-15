import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import dash

def get_first_page():
    first_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Create custom charts and dashboard in an easy & free way."),
                html.P("If you need help learn how to create your first chart step by step click below to check out tutorials and documentation."),
                dbc.Button("Learn more", color="primary", href="/documentation", className="me-1"),
                html.H3("First Step: How do you want to upload your data?")
            ]))
        ),
        dbc.Row(
            dcc.Tabs(id="tabs-example", value='tab-1', children=[
                dcc.Tab(label='Copy & paste data table', value='tab-1', className='tab-background'),
                dcc.Tab(label='XLS/CSV upload', value='tab-2', className='tab-background'),
                dcc.Tab(label='Connect Google Sheet', value='tab-3', className='tab-background'),
            ]),
            className="mt-4"
        ),
        html.Div(id='tabs-content-example')
    ])
    return first_page

def get_copy_paste_data():
    return html.Div([
        html.H1("Copy & paste your data"),
        html.P("Select your data (including header row/column) in Excel or LibreOffice and paste it in the text field. You can also upload a CSV or Excel file from your computer."),
        html.P("If you just want to try Easy Dashboard, here‘s a list of some example datasets you can use:"),
        dcc.Textarea(
            id='data-input',
            placeholder="Paste your copied data here...",
            className='textarea-background',
            style={'width': '100%', 'height': 200},
        ),
        dbc.Button("Check data", id="proceed-to-check", color="primary", className="mt-2",
                   href="/check-and-describe-page")
    ])

def get_upload_data():
    return html.Div([
        html.H1("Upload CSV or Excel spreadsheets."),
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
        dbc.Button("Check data", id="proceed-to-check", color="primary", className="mt-2", href="/check-and-describe-page"),
        html.Div(id='output-data-upload')
    ])

def get_import_data():
    return html.Div([
        html.H1("Import data from Google Sheet."),
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
        dbc.Button("Check data", id="proceed-to-check", color="primary", className="mt-2",
                   href="/check-and-describe-page"),
        html.Div(id='output-url')
    ])