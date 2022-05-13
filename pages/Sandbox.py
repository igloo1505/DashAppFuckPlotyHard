from dash import Dash, dcc, html, Input, Output, dash_table, callback
import dash
import math
from astropy.constants import codata2018 as const
dash.register_page(__name__, "/sandbox", top_nav=True, name="Sandbox")
import numpy as np
import pandas as pd
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
from classes.TheoryGenerator import TheoryGenerator as Gen
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
pio.templates.default = "plotly_dark"
# c = const.c
from utils.relativityHandler import getRelativeValues


vals = []
L = 1000
for n in np.linspace(1, 299792458, L):
    rv = getRelativeValues(n)
    if rv:
        vals.append(rv)
rdf = pd.DataFrame(vals)
# print(rdf.head())
# print(rdf.tail())
# print(rdf.columns)
# (['beta', 'velocity', 'matrixV', 'gamma', 'tNaught', 'tPrimeAltered',
    #    'tNaughtAltered', 'theoreritcalEpsilonDerivative'],
fig = go.Figure()
fig.add_trace(go.Scatter(x=rdf["velocity"], y=rdf["tNaughtAltered"],
                        # visible=False,
                        mode='markers',
                        name="tNaughtAltered"
                        ))
fig.add_trace(go.Scatter(x=rdf["velocity"], y=rdf["theoreritcalEpsilonDerivative"],
                        mode='markers',
                        name="theory"
                        ))

fig.add_trace(go.Scatter(x=rdf["velocity"], y=rdf["gamma"],
                        mode='markers',
                        name="gamma"
                        ))
fig.add_trace(go.Scatter(x=rdf["velocity"], y=rdf["beta"],
                        mode='markers',
                        name="beta"
                        ))

# fig.update_yaxes(
#     range=[0, 100],
#     # domain=[0, 100],
#     scaleanchor= "x",
#     dtick=10,
#     constrain="range",
#     constraintoward="bottom"
# )

# fig.update_xaxes(
#     range=[0, 1],
#     domain=[0, 1 / 1.3],
#     dtick=0.1,
#     scaleanchor= "y",
#     constrain="domain",
#     constraintoward="left"
# )


layout = html.Div([
    html.H3("Sandbox"),
    dcc.Graph(id='sandbox-plot-one', figure=fig)
])