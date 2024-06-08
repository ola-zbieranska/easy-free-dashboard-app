import dash_bootstrap_components as dbc
from dash import html, dcc
from dash import dash_table

def get_create_page():
    """
       Zwraca stronę do przesyłania danych w aplikacji.
       Returns a data   page in the application.
       """
    return dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.P("Check documentation to learn how to create your first chart step by step.", className="lead"),
                dbc.Button("Learn more", color="primary", href="/documentation", className="me-1"),
                html.Hr(className="my-4"),
                html.H3("Choose how do you want to upload your data.", className="lead")
            ]), width={"size": 12})
        ),
        dbc.Row([
            dbc.Col(
                width=5,
                children=[
                    dcc.Tabs(
                        id="tabs-example",
                        value='tab-1',
                        className='custom-tab',
                        children=[
                            dcc.Tab(label='Copy & paste data table', value='tab-1', className='tab', children=[
                                html.P("Select your data (including header row/column) in Excel or LibreOffice and paste it in the text field.")
                            ]),
                            dcc.Tab(label='XLS/CSV upload', value='tab-2', className='tab', children=[
                                html.P("Upload your XLS or CSV file using the upload component.")
                            ]),
                            dcc.Tab(label='Connect Google Sheet', value='tab-3', className='tab', children=[
                                html.P([
                                    "Make sure to enable ",
                                    html.A("Link Sharing", href="https://support.google.com/drive/answer/2494822?visit_id=1-636596603923192043-2988837136&p=link_sharing_on&hl=en&rd=1#link_sharing&zippy=%2Callow-general-access-to-the-file",
                                           target="_blank"),
                                    " in the Google Sheet and copy the spreadsheet URL into the text field on the right."
                                ])
                            ])
                        ]
                    )
                ]
            ),
            dbc.Col(
                width=7,
                children=[
                    html.Div(id='tabs-content-example'),
                    dcc.Store(id='stored-data'),
                    dcc.Textarea(
                        id='data-input',
                        placeholder="Paste your copied data here...",
                        style={'display': 'none', 'width': '100%', 'height': '200px'}
                    ),
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
                        style={
                            'display': 'none',
                            'width': '100%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px 0'
                        }
                    ),
                    dcc.Input(
                        id='google-sheet-url',
                        type='url',
                        placeholder='Enter Google Sheet URL',
                        style={'display': 'none', 'width': '100%', 'height': '40px', 'margin-top': '10px'}
                    )
                ]
            )
        ]),
        dbc.Button("Next", id="next-page", color="primary", className="mt-2", href="/check-data-page")
    ], className="mt-4")