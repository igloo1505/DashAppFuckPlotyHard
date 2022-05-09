from dash import Dash, dcc, html, Input, Output, callback
import dash
dash.register_page(__name__, "/matrixInMotion", top_nav=True, name="Matrix in Motion")
import pandas as pd
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
from plotGenerators.MatrixEpsilonSurface import genMatrixSurfacePlot
from plotGenerators.MatrixEpsilonScatter import genScatterAsPx, genScatterMatrixPlot
from state.settings import style, settings
from classes.windEpsilon import getEpsilon
import numpy as np
colorrr = style["colors"]


trajectoryXAndY = np.linspace(sys.float_info.min * 10, 1, settings["axisLength"])
vals, colors = getEpsilon(trajectoryXAndY, trajectoryXAndY)
surface = genMatrixSurfacePlot(trajectoryXAndY, colors, vals)
df = pd.DataFrame(vals)
# linear = genScatterAsPx(df)
scatterFig = genScatterMatrixPlot(trajectoryXAndY, df)



layout = html.Div(style={'backgroundColor': colorrr['background']}, id="matrix-in-motion-layout", children=[
    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colorrr["plotText"]
    }),
    dcc.Graph(
        id='matrix-surface-fig',
        figure=surface
    ),
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
        marks={str(n): str(n) for n in df.columns}
    ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
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


    # def update_bar_chart(slider_range):
    #     df = px.data.iris() # replace with your own data source
    # low, high = slider_range
    # mask = (df['petal_width'] > low) & (df['petal_width'] < high)
    # fig = px.scatter(
    #     df[mask], x="sepal_width", y="sepal_length", 
    #     color="species", size='petal_length', 
    #     hover_data=['petal_width'])
    # return fig