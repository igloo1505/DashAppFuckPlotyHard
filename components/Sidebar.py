import dash_bootstrap_components as dbc
import dash
from dash import Input, Output, State, html, callback

# placement_selector = html.Div(
#     [
#         dbc.Label("Placement:"),
#         dbc.RadioItems(
#             id="offcanvas-placement-selector",
#             options=[
#                 {"label": "start (Default)", "value": "start"},
#                 {"label": "end", "value": "end"},
#                 {"label": "top", "value": "top"},
#                 {"label": "bottom", "value": "bottom"},
#             ],
#             value="start",
#             inline=True,
#         ),
#     ],
#     className="mb-2",
# )

# offcanvas = html.Div(
#     [
#         placement_selector,
#         dbc.Button(
#             "Open Offcanvas", id="open-offcanvas-placement", n_clicks=0
#         ),
#         dbc.Offcanvas(
#             html.P("Some offcanvas content..."),
#             id="offcanvas-placement",
#             title="Placement",
#             is_open=False,
#         ),
#     ]
# )


# @callback(
#     Output("offcanvas-placement", "is_open"),
#     Input("open-offcanvas-placement", "n_clicks"),
#     [State("offcanvas-placement", "is_open")],
# )
# def toggle_offcanvas(n1, is_open):
#     if n1:
#         return not is_open
#     return is_open


# @callback(
#     Output("offcanvas-placement", "placement"),
#     Input("offcanvas-placement-selector", "value"),
# )
# def toggle_placement(placement):
#     return placement


def sidebar():
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
                if page["path"].startswith("/topic")
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    )