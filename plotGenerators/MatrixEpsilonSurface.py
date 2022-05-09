import sys
sys.path.insert(0, "../classes")
import plotly.graph_objects as go
# from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.offline as pyo
import pandas as pd
import numpy as np
pio.templates.default = "plotly_dark"
import os
module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)
from utils.isSafeNumber import isSafeNumber
from state.settings import settings
directory = os.fsencode(settings["csvRootPath"]["matrix"])
# from classes.windEpsilon import getEpsilon
# from utils.tableHandler import  generate_table


def genMatrixSurfacePlot(trajectoryXAndY, colors, vals):
    surfaceFig = go.Figure()
    surfaceFig.add_trace(
        go.Surface(
            x=trajectoryXAndY,
            y=trajectoryXAndY,
            z=vals,
            surfacecolor=colors,
            colorscale="Plasma",
            cauto=False,
            cmin=np.min(colors),
            cmax=np.max(colors),
            name=""
        )
    )
    surfaceFig.update_layout(
        title='Lateral-Symmetrical Movement through a Matrix in Motion', autosize=True,
                            height=700,
                            margin=dict(l=65, r=50, b=65, t=90),
                            scene=dict(
                                xaxis_title='Δω',
                                yaxis_title="Δy",
                                zaxis_title="ε",
                                aspectmode='manual',
                                yaxis = dict(nticks=8, range=[0, 1]),
                                xaxis = dict(nticks=8, range=[0, 1]),
                                zaxis = dict(nticks=8, range=[0, 1.3]),
                                aspectratio=dict(x=1, y=1, z=1.3),
                            ),
                            hoverlabel=dict(
                                align="auto",
                                bgcolor="#651fff",
                            ),
                                xaxis_title='Δω',
                                yaxis_title='ε',
                        )
    return surfaceFig


