import dash_bootstrap_components as dbc
from callbacks.callbacks import *
def get_navbar():
    theme_toggle = dbc.Button(
        "change theme", id="theme-toggle", n_clicks=0, className='ms-2', color='secondary'
    )
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Strona główna", href="/first-page", className="nav-link"), className="nav-item"),
            dbc.NavItem(dbc.NavLink("O Aplikacji", href="/about", className="nav-link"), className="nav-item"),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Profil", href="/profile", className="dropdown-item"),
                    dbc.DropdownMenuItem("Ustawienia", href="/settings", className="dropdown-item"),
                    dbc.DropdownMenuItem("Wyloguj", href="/logout", className="dropdown-item"),
                ],
                nav=True,
                in_navbar=True,
                label="Twoje Konto",
                className="dropdown-menu"
            ),
            theme_toggle  # Włączony do navbar
        ],
        brand="easy dashboard",
        brand_href="/home",
        sticky="top",
        color="primary",
        dark=True,
        className="mb-4 navbar",
        fluid=True
    )
    return navbar