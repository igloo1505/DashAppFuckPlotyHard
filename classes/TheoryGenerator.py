import numpy as np
import pandas as pd
import math
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
from utils.relativityHandler import getRelativeValues

def alphaAsFunctionOfTimeNaught(length=1000):
    c = 299792458
    timePrime = 60 * 60 # One hour simulated
    velocities = []
    gammas = []
    tNaughts = []
    tPrimes = []
    theoryValues = []
    ns = []
    inverseN = []
    for n in range(length):
        if not n == 0:
            v = c / (length - n)
            gamma = math.sqrt(1 - (v**2 / c**2))
            if not gamma == 0:
                velocities.append(v)
                ns.append(n)
                inverseN.append(length - n)
                gammas.append(gamma)
                tNaught = timePrime * gamma
                tNaughts.append(tNaught)
                theory = (((tNaught * c) - (v*tNaught)) / 2) * (v * tNaught)
                theoryValues.append(theory)
    df = pd.DataFrame((velocities, gammas, tNaughts, theoryValues, ns, inverseN))
    _df = df.transpose()
    _df.columns = ["velocity", "gamma", "tNaught", "theory", "n", "inverseN"]
    return _df

class TheoryGenerator:
    def __init__(self):
        self.data = []
        
    def alphaOfTNaught(self, length=1000): 
        return alphaAsFunctionOfTimeNaught(length)
    
