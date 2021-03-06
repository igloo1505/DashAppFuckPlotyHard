import dash_bootstrap_components as dbc
from dash import Input, Output, State, html,  callback
import dash
from dash_bootstrap_components._components.Container import Container
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
from state.settings import style
color = style["colors"]["highlightBackground"]
# from assets import logo
# from PIL import Image
# logoPath = "./assets/"
# logo = Image.open(os.path.join(logoPath, "logo.png"))

def Navbar():
    return html.Div(dbc.NavbarSimple(
    dbc.Nav(
        [
            dbc.NavLink(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page.get("top_nav")
        ],
    ),
    brand="Movement Through A Matrix In Motion",
    color=color,
    # dark=True,
    className="mb-2",
))