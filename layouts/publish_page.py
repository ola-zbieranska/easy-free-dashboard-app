import dash_bootstrap_components as dbc
from dash import html, dcc
def get_publish_page():
    """
        Tworzy i zwraca stronę publikacji wizualizacji.
        W trakcie prac.
        Creates and returns the publish visualization page.
        Work i n progres.
        """
    publish_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Publish visualization", className="lead"),
                html.H1("Embed your chart or download it as PNG.", className="lead"),
                dbc.Button("Back", color="secondary", href="/vizualize-page", className="mt-2 me-2"),
                dbc.Button("Publish", color="primary", href="/", className="mt-2")
            ]))
        )
    ])
    return publish_page