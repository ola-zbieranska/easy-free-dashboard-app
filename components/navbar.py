import dash
import dash_bootstrap_components as dbc
from callbacks.callbacks import *
def get_navbar():
    theme_toggle = dbc.DropdownMenu(
        label=html.I(className="fas fa-adjust"),  # Ikona do wyboru trybu
        children=[
            dbc.DropdownMenuItem("Light", id="light-mode", n_clicks=0, className="dropdown-item"),
            dbc.DropdownMenuItem("Dark", id="dark-mode", n_clicks=0, className="dropdown-item"),
        ],
        className="theme-switch-container",
        id="theme-dropdown"
    )
    dropdown = dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("More pages", header=True),
            dbc.DropdownMenuItem("Main", href="/home"),
            dbc.DropdownMenuItem("Create", href="/first-page"),
            dbc.DropdownMenuItem("Blog", href="/blog"),
            dbc.DropdownMenuItem("Documentation", href="/documentation"),
        ],
        nav=True,
        in_navbar=True,
        label="More",
    )
    navbar = dbc.NavbarSimple(
        children=[
            theme_toggle,
            dbc.NavItem(dbc.NavLink("Main", href="/home")),
            dbc.NavItem(dbc.NavLink("Create", href="/first-page")),
            dropdown
        ],
        brand="Easy Dashboard",
        brand_href="/home",
        sticky="top",
        color="primary",
        dark=True,
    )
    return navbar