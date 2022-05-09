from dash import Dash, dcc, html
import numpy as np
import pandas as pd
import sys
sys.path.insert(0, "../classes")
import plotly.graph_objects as go
import plotly.express as px
# from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.offline as pyo
# pyo.init_notebook_mode()
pio.templates.default = "plotly_dark"
import os
module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)
from utils.isSafeNumber import isSafeNumber
from utils.settings import settings
directory = os.fsencode(settings["csvRootPath"]["matrix"])
from classes.windEpsilon import getEpsilon
from utils.tableHandler import  generate_table

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


trajectoryXAndY = np.linspace(sys.float_info.min * 10, 1, settings["axisLength"])
vals, colors = getEpsilon(trajectoryXAndY, trajectoryXAndY)
df = pd.DataFrame(vals)
# Add this to table method
# df.describe()
# layout = 

def MatrixInMotion():
        return html.Div(style={'backgroundColor': colors['background']}, children=[
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

