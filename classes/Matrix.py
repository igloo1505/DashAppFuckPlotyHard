import math
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


class SimulatedMatrix:
    def __init__(self, matrixVelocity, dimensions=[10, 10, 10], interaction=10):
        self.epsilon = matrixVelocity
        self.dims = dimensions
        self.interactionConstant = interaction
        
    def F_epsilonX(self, observerRateOfChange):
        oroc = observerRateOfChange
        # Forward force supplied from matrix relative to motion of observer.
        return self.epsilon * (np.divide(oroc[0] / oroc[1]))
    
    def F_epsilon_negX(self, oroc):
        v = (self.epsilon - oroc[0]) * self.interactionConstant
        return v
    



mtx = SimulatedMatrix(10)
sampleLength = 1000
sampleEnd = 1000
_n = np.linspace(0, sampleEnd, sampleEnd / sampleLength)
vals = []
for n in _n:
    mtx.F_epsilon_negX([])