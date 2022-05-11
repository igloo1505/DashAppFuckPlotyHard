import sys
sys.path.insert(0, "../classes")
import plotly.graph_objects as go
# from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.express as px
pio.templates.default = "plotly_dark"
import os
module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)
from state.settings import settings
directory = os.fsencode(settings["csvRootPath"]["matrix"])
# from classes.windEpsilon import getEpsilon
# from utils.tableHandler import  generate_table

 
def genScatterMatrixPlot(trajectoryXAndY, df):
        linearScatterFig = go.Figure()
        for __y in range(settings["axisLength"]):
            linearScatterFig.add_trace(
                go.Scatter(x=trajectoryXAndY, y=df[__y],
                        visible=False,
                        mode='markers',
                        name='{}'.format(__y),
                        marker=dict(
                            size=df[__y]  * (settings["axisLength"] / 3),
                            color=trajectoryXAndY,
                            colorscale='Plasma',
                            opacity=0.8
                        )
                        )
            )
        linearScatterFig.data[0].visible = True
        linearScatterSteps = []

        for i, vd in enumerate(linearScatterFig.data):
            step = dict(
                method="update",
                args=[{"visible": [False] * len(linearScatterFig.data)}],
                label="{}/{}".format(i, settings["axisLength"])
            )
            step["args"][0]["visible"][i] = True
            linearScatterSteps.append(step)

        linearScatterFig.update_layout(title='Lateral-Symmetrical Movement through a Matrix in Motion', autosize=True,
                                height=700,
                                margin=dict(l=65, r=50, b=65, t=90),
                                yaxis_title="α",
                                xaxis_title='Δε'
                                )

        linearScatterFig.update_yaxes(
            range=[0, 1.3],
            domain=[0, 1],
            scaleanchor= "x",
            dtick=0.1,
            constrain="domain",
            constraintoward="bottom"
        )

        linearScatterFig.update_xaxes(
            range=[0, 1],
            domain=[0, 1 / 1.3],
            dtick=0.1,
            scaleanchor= "y",
            constrain="domain",
            constraintoward="left"
        )
        return linearScatterFig
        
    