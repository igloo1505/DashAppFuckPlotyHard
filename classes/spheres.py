import math
import numpy as np

class Sphere:
    def __init__(self, centerPoints=[0, 0, 0], radius=1, nLimit=10, accuracy=1):
        self.center = centerPoints
        self.radius = radius
        self.nLimit = nLimit
        self.intervalAccuracy = accuracy
    
    def genPoints(self):
        points = []
        xs = []
        ys = []
        zs = []
        nLimit = self.nLimit
        for xFactor in np.arange(0, nLimit, self.intervalAccuracy):
            thetaPrime = xFactor / nLimit
            rNaught = thetaPrime * self.radius
            _y = math.sqrt(self.radius**2 - rNaught**2)
#             Resume here by adjusting this to not use nLimit but rather loop through for some accuracy int, not tied to number of points currently...
            for _z in np.arange(0, nLimit, self.intervalAccuracy):
                # zF = ((_z / nLimit) * rNaught)
                zF = ((_z / nLimit) * self.radius)
                xF = ((nLimit - _z) / nLimit) * rNaught
                yF = math.sqrt(self.radius**2 - xF**2 - zF**2)
                yFF = math.sqrt(self.radius**2 - rNaught**2)
                points.append([self.center[0] + xF, self.center[1] + yF, self.center[2] + zF])
                points.append([self.center[0] + xF, self.center[1] + yF, self.center[2] - zF])
                points.append([self.center[0] + xF, self.center[1] - yF, self.center[2] + zF])
                points.append([self.center[0] + xF, self.center[1] - yF, self.center[2] - zF])
                points.append([self.center[0] - xF, self.center[1] + yF, self.center[2] + zF])
                points.append([self.center[0] - xF, self.center[1] + yF, self.center[2] - zF])
                points.append([self.center[0] - xF, self.center[1] - yF, self.center[2] + zF])
                points.append([self.center[0] - xF, self.center[1] - yF, self.center[2] - zF])
        return np.array(points)

