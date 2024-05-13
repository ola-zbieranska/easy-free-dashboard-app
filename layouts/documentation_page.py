import dash_bootstrap_components as dbc
from dash import html

def get_documentation_page():
    sidebar = dbc.Offcanvas(
        [
            #html.H2("Documentation", className="display-4"),
            #html.Hr(),
            html.P("Useful links for documentation:", className="lead"),
            dbc.Nav(
                [
                    dbc.NavLink("Introduction", href="/documentation#introduction", active="exact"),
                    dbc.NavLink("Setup", href="/documentation#setup", active="exact"),
                    dbc.NavLink("Advanced Topics", href="/documentation#advanced", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        id="offcanvas",
        is_open=False,  # Keep the sidebar open
        backdrop=False,  # Disable the backdrop
        scrollable=True,
        placement="start",
        style={"width": "250px"}
    )

    # Główna treść strony "Documentation"
    content = html.Div([
            html.H1("Learn more about creating custom charts and dashboard in an easy & free way."),
            html.P("Here you can find extensive documentation on how to use the Easy Dashboard and create your charts."),
            dbc.Button("Learn more", id="open-sidebar", n_clicks=0)
        ], style={"margin-left": "270px"})  # Przesunięcie treści, aby uwzględnić sidebar

    # Całkowity layout strony zawierający sidebar i treść
    documentation_page = html.Div([sidebar, content])

    return documentation_page