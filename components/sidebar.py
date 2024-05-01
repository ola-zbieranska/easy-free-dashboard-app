import dash_bootstrap_components as dbc
from dash import html

def get_sidebar():
    sidebar = html.Div([
    dbc.Offcanvas(
        html.P("Treść Sidebar"),
        id="offcanvas",
        is_open=False,
        title="Sidebar",
        style={"width": "250px"},
        placement="start",
        backdrop=False  # Opcjonalnie, aby zapobiec zamknięciu przy kliknięciu poza sidebar
    ),
    html.Div(
        dbc.Button(
            "→", id="open-close-button", className="me-2",
            style={"transform": "rotate(180deg)"},
        ),
        id="button-container",
        style={"position": "absolute", "top": "50%", "left": "250px", "transform": "translateY(-50%)"}
    )]
    )
    return sidebar