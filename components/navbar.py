import dash_bootstrap_components as dbc
from callbacks.callbacks import *
def get_navbar():
    theme_toggle = dbc.Button(
        "change theme", id="theme-toggle", n_clicks=0, className='ms-2', color='secondary'
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