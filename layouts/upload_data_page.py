import dash_bootstrap_components as dbc
from dash import html, dcc

def get_upload_data_page():
    upload_data_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
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
                dbc.Button("Back", id="back-to-input", color="secondary", className="mt-2 me-2"),
                dbc.Button("Check data", id="proceed-to-check", color="primary", className="mt-2", href="/check-and-describe-page"),
                html.Div(id='output-data-upload')
            ]))
        )
    ])
    return upload_data_page