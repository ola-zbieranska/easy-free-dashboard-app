import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

def get_navbar():
    theme_toggle = dbc.DropdownMenu(
        label=html.I(className="bi bi-brightness-high-fill"),
        children=[
            dbc.DropdownMenuItem([html.I(className="bi bi-brightness-high-fill me-2"), "Light"], id="light-mode", n_clicks=0,
                                 className="dropdown-item"),
            dbc.DropdownMenuItem([html.I(className="bi bi-moon-fill me-2"), "Dark"], id="dark-mode", n_clicks=0,
                                 className="dropdown-item"),
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
            dbc.DropdownMenuItem("Visualize data", href="/visualize-page"),
            dbc.DropdownMenuItem("Check data", href="/check-and-describe-page"),
            dbc.DropdownMenuItem("Publish chart", href="/publish-page")
        ],
        nav=True,
        in_navbar=True,
        label="More",
    )

    github_button = dbc.Button(
        html.I(className="bi bi-github"),
        color="link",
        href="https://github.com/ola-zbieranska/easy-free-dashboard-app",
        external_link=True,
        className="me-2",
        target="_blank"
    )

    navbar = dbc.NavbarSimple(
        children=[
            github_button,
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