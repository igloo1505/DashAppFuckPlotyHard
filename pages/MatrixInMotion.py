from dash import Dash, dcc, html, Input, Output, dash_table, callback
import dash
dash.register_page(__name__, "/matrixInMotion", top_nav=True, name="Matrix in Motion")
import pandas as pd
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
from plotGenerators.MatrixEpsilonSurface import genMatrixSurfacePlot
from plotGenerators.MatrixEpsilonScatter import genScatterMatrixPlot
from state.settings import style, settings
from classes.windEpsilon import getEpsilon
import numpy as np
colorrr = style["colors"]
trajectoryXAndY = np.linspace(sys.float_info.min * 10, 1, settings["axisLength"])
vals, colors = getEpsilon(trajectoryXAndY, trajectoryXAndY)
surface = genMatrixSurfacePlot(trajectoryXAndY, colors, vals)
df = pd.DataFrame(vals)
from utils.tableHandler import generateDashTable
scatterFig = genScatterMatrixPlot(trajectoryXAndY, df)
from textContent.MatrixInMotionText import matrixSliderText

tbl = generateDashTable(df)

cols = []
vals = []
edf = df.describe().to_dict()
for j in edf:
    cols.append({j})
    vals.append(edf[j])
print(vals)
# print(tbl)
layout = html.Div(style={'backgroundColor': colorrr['background']}, id="matrix-in-motion-layout", children=[
    # html.Div(children='Dash: A web application framework for your data.', style={
    #     'textAlign': 'center',
    #     'color': colorrr["plotText"]
    # }),
    dcc.Graph(
        id='matrix-surface-fig',
        figure=surface
    ),
    html.Div([  
    html.Div([
    dcc.Graph(
        id='matrix-surface-scatter-fig',
        figure=scatterFig
    ), 
    html.Div(dcc.Slider(
        df.columns.min(),
        df.columns.max(),
        step=None,
        id='matrix-scatter-slider',
        value=df.columns.min(),
        marks={str(n): str(f"{round(n / df.columns.max(), 2)}") for n in df.columns},
        dots=True
        # marks=None,
        # tooltip={"placement": "bottom", "always_visible": True}
    ), style={'width': '90%', 'padding': '0px 0px 20px 0px'})
    ], id="matrix-slider-container"),
    dcc.Markdown(matrixSliderText, mathjax=True)
    ], id="matrix-slider-container-outer"),
    # tbl
])



@callback(
    Output("matrix-surface-scatter-fig", "figure"), 
    Input("matrix-scatter-slider", "value"))
def updateScatterMatrixPlot(sliderVal):
    for i in range(len(scatterFig.data)):
        if sliderVal == i:
            scatterFig.data[i].visible = True
        if not sliderVal == i:
            scatterFig.data[i].visible = False
    return scatterFig
