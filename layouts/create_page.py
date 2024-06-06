import dash_bootstrap_components as dbc
from dash import html, dcc
from dash import dash_table

def get_create_page():
    create_page = dbc.Container([
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
                            dcc.Tab(label='Copy & paste data table', value='tab-1', children=[
                                html.Div([
                                    html.P("Select your data (including header row/column) in Excel or LibreOffice and paste it in the text field."),
                                    html.P("You can also upload a CSV or Excel file from your computer."),
                                    html.P("If you just want to try Easy Dashboard, here‘s a list of some example datasets you can use:"),
                                    dcc.Textarea(id='data-input', style={'width': '100%', 'height': 200}),
                                    html.Div(id='output-data')
                                ])
                            ], className='tab'),
                            dcc.Tab(label='XLS/CSV upload', value='tab-2', children=[
                                html.Div([
                                    html.P("In the pop-up window, select the Excel/CSV file from your computer or drag and drop the file in the window below."),
                                    html.P("If you just want to try Easy Dashboard, here‘s a list of some example datasets you can use:"),
                                    dcc.Upload(id='upload-data', children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
                                                style={
                                                    'width': '100%',
                                                    'height': '60px',
                                                    'lineHeight': '60px',
                                                    'borderWidth': '1px',
                                                    'borderStyle': 'dashed',
                                                    'borderRadius': '5px',
                                                    'textAlign': 'center',
                                                    'margin': '10px 0'
                                                }, multiple=False),
                                    html.Div(id='output-data-upload')
                                ])
                            ], className='tab'),
                            dcc.Tab(label='Connect Google Sheet', value='tab-3', children=[
                                html.Div([
                                    html.P(["Make sure to enable ",
                                           html.A("Link Sharing", href="https://support.google.com/drive/answer/2494822?visit_id=1-636596603923192043-2988837136&p=link_sharing_on&hl=en&rd=1#link_sharing&zippy=%2Callow-general-access-to-the-file",
                                                  target="_blank"),
                                           " in the Google Sheet and copy the spreadsheet URL into the text field below."]),
                                    dcc.Input(id='google-sheet-url', type='url', placeholder='Enter Google Sheet URL', style={'width': '100%'}),
                                    html.Div(id='output-url')
                                ])
                            ], className='tab'),
                        ]
                    )
                ]
            ),
            dbc.Col(
                width=7,
                children=[
                    html.Div(id='tabs-content-example'),
                    dash_table.DataTable(id='table-output', style_table={'display': 'none'}),
                ]
            )
        ]),
        dcc.Store(id='stored-data', storage_type='session'),  # Przechowywanie danych w sesji
        dbc.Button("Next", id="next-page", color="primary", className="mt-2", href="/check-data-page")
    ], className="mt-4")
    return create_page