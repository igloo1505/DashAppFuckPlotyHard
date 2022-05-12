from dash import Dash, dcc, html, Input, Output, dash_table, callback
import dash
dash.register_page(__name__, "/sphericalRebound", top_nav=True, name="Spherical Rebound Pressure")

layout = html.Div([
    html.H3("Spherical Rebound Here")
])