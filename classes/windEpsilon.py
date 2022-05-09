# %%
import math
import numpy as np
import pandas as pd
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)
from utils.isSafeNumber import isSafeNumber

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