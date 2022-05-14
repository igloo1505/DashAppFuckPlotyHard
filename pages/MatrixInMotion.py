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
from utils.tableHandler import generateDashTable, generate_table
scatterFig = genScatterMatrixPlot(trajectoryXAndY, df)
from textContent.MatrixInMotionText import matrixInMotionText
from textContent.Formulas import alphaDerivation, matrixSurfaceColor
import describetable as dTable



markdowns = []
for p in matrixInMotionText:
    P = dcc.Markdown(p, mathjax=True, className="matrixInMotionTextSingle")
    markdowns.append(P)

halfAssedKwargs = {}

if settings["axisLength"] > 30:
    halfAssedKwargs["tooltip"] = {"placement": "bottom", "always_visible": True}
    halfAssedKwargs["marks"] = None
    halfAssedKwargs["step"] = None
    halfAssedKwargs["included"] = True
elif settings["axisLength"] <= 30:
    halfAssedKwargs["marks"] = {i: '{}'.format(round(i, 2)) for i in np.linspace(0, 1, len(df.columns))}
    halfAssedKwargs["step"] = None
    halfAssedKwargs["dots"] = True

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
    html.Div("Slider:", id="slider-label-text"),
    html.Div(dcc.Slider(
        0,
        1,
        id='matrix-scatter-slider',
        value=df.columns.min(),
        updatemode="drag",
        **halfAssedKwargs
    ), style={'width': '90%', 'padding': '0px 0px 20px 0px'})
    ], id="matrix-slider-container"),
    html.Div([
    html.Div([  
              
    dcc.Markdown(alphaDerivation, mathjax=True),
    dcc.Markdown(matrixSurfaceColor, mathjax=True),
    
    ], id="matrixInMotionDerivationContainer"),
    
    *markdowns
    
    ], id="matrixInMotion-markdown-container"),
    ], id="matrix-slider-container-outer"),
    dTable.Describetable(id="matrix-surface-dTable", data=df.describe().to_html(), buttonText="Describe Plotted Data", buttonFloat="right")
])




@callback(
    Output("matrix-surface-scatter-fig", "figure"), 
    Input("matrix-scatter-slider", "value"))
def updateScatterMatrixPlot(sliderVal):
    for i in range(len(scatterFig.data)):
        scatterFig.data[i].visible = False
    lsp = np.linspace(0, 1, len(scatterFig.data))
    index = (np.abs(lsp - sliderVal)).argmin()
    scatterFig.data[index].visible = True
    return scatterFig
