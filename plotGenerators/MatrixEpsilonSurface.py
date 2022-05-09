import sys
sys.path.insert(0, "../classes")
import plotly.graph_objects as go
# from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.offline as pyo
# pyo.init_notebook_mode()
import pandas as pd
import numpy as np
pio.templates.default = "plotly_dark"
import os
module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)
from utils.isSafeNumber import isSafeNumber
from state.settings import settings
directory = os.fsencode(settings["csvRootPath"]["matrix"])
from classes.windEpsilon import getEpsilon
from utils.tableHandler import  generate_table


def getEpsilon(xArray, yArray):
    vals = []
    colors = []
    for _x in xArray:
        linpath = []
        _colors = []
        if not _x**2 == 0:
            for _y in yArray:
                ySquared = _y**2 
                xSquared = _x**2
                numer = xSquared + ySquared
                denom = xSquared + (ySquared * (ySquared / xSquared))
                v = numer / denom
                iy = 1 / _y
                ix = 1 / _x
                colorValue = 1 - (abs(_x - _y))
                # colorValue = _y / _x
                if isSafeNumber(denom, withZero=True) and isSafeNumber(v) and isSafeNumber(colorValue):
                    _colors.append(colorValue)
                    linpath.append(v)
        if not np.isnan(_colors).any() and not np.isnan(linpath).any() and not len(_colors) == 0 and not len(linpath) == 0 and len(linpath) == len(_colors):
            colors.append(np.array(_colors))
            vals.append(np.array(linpath))
            linpath = []
            _colors = []
    return vals, np.array(colors)


def genMatrixSurfacePlot():
    trajectoryXAndY = np.linspace(sys.float_info.min * 10, 1, settings["axisLength"])
    vals, colors = getEpsilon(trajectoryXAndY, trajectoryXAndY)
    df = pd.DataFrame(vals)
    # df.describe()
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
    return surfaceFig, df


