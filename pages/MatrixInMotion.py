from dash import Dash, dcc, html
import dash
dash.register_page(__name__, "/matrixInMotion", top_nav=True)
import pandas as pd
import plotly.express as px
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print("path")
print(sys.path)
print("path")
from plotGenerators.MatrixEpsilonSurface import genMatrixSurfacePlot

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


fig, df = genMatrixSurfacePlot()



layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])