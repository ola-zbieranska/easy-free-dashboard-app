import dash_bootstrap_components as dbc
from dash import html, dcc
from dash import dash_table

def get_create_page():
    """
       Tworzy i zwraca stronę do przesyłania danych.
       Creates and returns the page for data upload.

       Returns:
           dbc.Container: Strona do przesyłania danych.
                          Data upload page.
       """
    return dbc.Container([
        # Nagłówek i przycisk do dokumentacji
        # Header and button to documentation
        dbc.Row(
            dbc.Col(html.Div([
                html.P("Check documentation to learn how to create your first chart step by step.", className="lead"),
                dbc.Button("Learn more", color="primary", href="/documentation", className="me-1"),
                html.Hr(className="my-4"),
                html.H3("Choose how do you want to upload your data.", className="lead")
            ]), width={"size": 12})
        ),
        dbc.Row([
            # Zakładki do różnych metod przesyłania danych
            # Tabs for different data upload methods
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
                            dcc.Tab(label='Connect Google Sheet', value='tab-3', className='tab')
                        ]
                    )
                ]
            ),
            # Obszar wyświetlania zawartości wybranej zakładki oraz elementy do przechowywania i wyświetlania danych
            # Area to display the content of the selected tab and elements for storing and displaying data
            dbc.Col(
                width=7,
                children=[
                    html.Div(id='tabs-content-example'),
                    dcc.Store(id='stored-data'),
                    html.Div(id='output-url'),
                    html.Div(id='output-data'),
                    html.Div(id='output-data-upload'),
                ]
            )
        ]),
        dbc.Button("Next", id="next-page", color="primary", className="mt-2", href="/check-data-page")
    ], className="mt-4")