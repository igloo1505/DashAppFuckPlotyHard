#  %%
import math
import numpy as np
import pandas as pd
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)
import utilitiesAndGenerators.utilFunctions as uf
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import plotly.offline as pyo
pyo.init_notebook_mode()
pio.templates.default = "plotly_dark"
from settings import settings
directory = os.fsencode(settings["csvRootPath"]["asymSphGen"])


class Circle:
    def __init__(self, center=[0, 0, 0], radius=1, nPoints=100):
        self.center = center
        self.radius = radius
        self.acc = nPoints
    
    def getPoints(self):
        radius = np.linspace(0, self.radius, self.acc)
        yDeviatedFromXCenter = []
        for _x in radius:
            v = math.sqrt(self.radius**2 - _x**2)
            yDeviatedFromXCenter.append(v)
        # xValues length = accuracy * 2
        xDiameterValues = np.concatenate((
            np.flip(np.subtract(self.center[0], radius)),
            np.add(self.center[0], radius),
        ))
        # yValues length = accuracy * 2
        yDeviatedPath = np.concatenate((
            np.flip(yDeviatedFromXCenter),
            yDeviatedFromXCenter
        ))
        xBoomerang = np.concatenate((
            xDiameterValues,
            np.flip(xDiameterValues)
        ))
        
        yPath = uf.pm(yDeviatedPath)
        yp = np.concatenate((yPath[0], yPath[1]))
        df = pd.DataFrame(yp, index=xBoomerang, columns=["y"])
        df.index.name = "x"
        return df

    def readStoredCsvs(self, sort="points"):
        data = []
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".csv"):
                tempDf = pd.read_csv("{}/{}".format(settings["csvRootPath"]["asymSphGen"], filename))
                _nPoints = filename[filename.index("nPoints") + 8 : filename.index("_")]
                radius = filename[filename.index("radius") + 7 : filename.index(".csv")]
                data.append({"data": np.array(tempDf), "nPoints": _nPoints, "radius": radius})
                continue
            else:
                continue
        return data
            
            
            
c = Circle(nPoints=10)
# d = c.readStoredCsvs()
d = c.getPoints()
# print(d)