# %%
import math
import numpy as np
import pandas as pd

# np.seterr(divide="ignore", invalid="ignore")


# def getEpsilon(xArray, yArray, squared=False):
#     vals = []
#     colors = []
#     with np.errstate(divide='ignore'):
#         for _x in xArray:
#             linpath = []
#             _colors = []
#             for _y in yArray:
#                 ySquared = _y**2
#                 xSquared = _x**2
#                 numer = xSquared + ySquared
#                 denom = ySquared + (ySquared * (np.divide(ySquared, xSquared, out=np.zeros_like(ySquared), where=xSquared!=0)))
#                 if not denom == 0:
#                     v = numer / denom
#                 if denom == 0 or math.isfinite(denom):
#                     v = 1
#                 if not math.isnan(v) or math.isfinite(v):
#                     if not _x == 0:
#                         if squared:
#                             _colors.append(_y**2 / _x**2)
#                         if not squared:
#                             _colors.append(_y / _x)
#                     if _x == 0:
#                         _colors.append(0)
#                 if math.isnan(v) or not math.isfinite(v):
#                     if not len(linpath) == 0:
#                         linpath.append(linpath[len(linpath) - 1])
#                     if len(linpath) == 0:
#                         linpath.append(1)
#                     if not len(_colors) == 0:
#                         _colors.append(_colors[len(_colors) - 1])
#                     if len(_colors) == 0:
#                         _colors.append(1)
                    
#                     # This might be issue causing graph to have that wall.
#             linpath[linpath == np.inf] = 0
#             _colors[_colors == np.inf] = 0
#             vals.append(np.array(linpath))
#             colors.append(np.array(_colors))
#             linpath = []
#             _colors = []
#     return vals, np.array(colors)

# BUG delete above here once this new function takes over the job.





# def getEpsilon(xArray, yArray, squared=False):
#     length = len(np.trim_zeros(xArray))
#     lengthCheck = len(np.trim_zeros(yArray))
#     if not length == lengthCheck:
#         return print("Oh lord... somethings wrong in getEpsilon function")
#     returnColors = [] 
#     returnAmplitude = []
#     for x in xArray:
#         linearColors = []
#         linearAmplitude =[]
#         for y in yArray:
#             if not x == 0 and not y == 0:
#                 xSquared = x**2
#                 ySquared = y**2
#                 numerator = xSquared + ySquared
#                 cosSquared = (y**2 / x**2)
#                 # cosSquared = (y / x)
#                 denomerator = xSquared + (ySquared * cosSquared)
#                 val = numerator / denomerator
#                 # np.append(linearColors, x / y)
#                 # np.append(linearAmplitude, val)
#                 linearColors.append(y / x)
#                 linearAmplitude.append(val)
#         # np.append(returnColors, linearColors)
#         # np.append(returnAmplitude, linearAmplitude)
#         returnColors.append(linearColors)
#         returnAmplitude.append(linearAmplitude)
            # linearColors = []
            # linearAmplitude = []
#     return np.array(returnAmplitude), np.array(returnColors)
                
                
  
                
def getEpsilon(xArray, yArray):
    vals = []
    colors = []
    for _x in xArray:
        linpath = []
        _colors = []
        for _y in yArray:
            nm = _x ** 2 + _y ** 2
            dm = _x ** 2 + (_y ** 2 * (_y ** 2 / _x ** 2))
            v = nm / dm
            if not math.isnan(v):
                linpath.append(nm / dm)
                # Diverted ratio:
                _colors.append(_y / _x)
            if math.isnan(v):
                if not len(linpath) == 0:
                    linpath.append(linpath[len(linpath) - 1])
                if not len(_colors) == 0:
                    _colors.append(_colors[len(_colors) - 1])
        vals.append(linpath)
        colors.append(_colors)
        linpath = []
        _colors = []
    return np.array(vals, dtype=object), np.array(colors, dtype=object)          
        








xxx = np.linspace(1, 2, 100)
yyy = np.linspace(1, 2, 100)


dfd, colors = getEpsilon(xxx, yyy)

df = pd.DataFrame(colors)
dff = pd.DataFrame(dfd)


df.describe()
# dff.plot()




