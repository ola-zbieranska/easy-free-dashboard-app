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
            # Tabs po lewej stronie
            dbc.Col(
                width=5,
                children=[
                    dcc.Tabs(
                        id="tabs-example",
                        value='tab-1',
                        className='custom-tab',
                        children=[
                            dcc.Tab(label='Copy & paste data table', value='tab-1', className='tab'),
                            dcc.Tab(label='XLS/CSV upload', value='tab-2', className='tab'),
                            dcc.Tab(label='Connect Google Sheet', value='tab-3', className='tab'),
                        ]
                    )
                ]
            ),
            # Okna do pobierania danych po prawej stronie
            dbc.Col(
                width=7,
                children=[
                    html.Div(id='tabs-content-example'),  # Tutaj będą wyświetlane wyniki
                    dcc.Textarea(id='data-input', placeholder='Paste your copied data here...', style={'display': 'none', 'width': '100%', 'height': 200}),
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div([
                            'Drag and Drop or ',
                            html.A('Select Files')
                        ]),
                        style={
                            'display': 'none',  # Początkowo ukryty
                            'width': '100%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px 0'
                        },
                        multiple=False
                    ),
                    dcc.Input(id='google-sheet-url', type='url', placeholder='Enter Google Sheet URL', style={'width': '100%', 'display': 'none'}),
                    dash_table.DataTable(id='table-output', style_table={'display': 'none'})
                ]
            )
        ]),
        dbc.Button("Next", id="next-page", color="primary", className="mt-2", href="/check-data-page")
    ], className="mt-4")
    return create_page