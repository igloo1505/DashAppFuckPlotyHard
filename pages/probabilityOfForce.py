from dash import Dash, dcc, html, Input, Output, dash_table, callback
import dash
dash.register_page(__name__, "/probabilityOfForce", top_nav=True, name="Probability of Force")

layout = html.Div([
    html.H3("Probability Of Force Here")
])