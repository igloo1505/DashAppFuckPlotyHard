c = 299792458
import math
import numpy as np
import pandas as pd
def getRelativeValues(v, matrixV=c, tPrime=1):
    if not v == 0 and not v == matrixV:
        beta = v**2 / matrixV**2
        gamma = math.sqrt(1 - beta)
        tNaught = tPrime / gamma
        tPrimeAltered = tNaught * gamma
        tNaughtAltered = tPrimeAltered / gamma
        theoreritcalEpsilonDerivative = (((tNaughtAltered * matrixV) - (v * tNaughtAltered)) / 2) + (v * tNaughtAltered)
        return {
            "beta": beta,
            "velocity": v,
            "matrixV": matrixV,
            "gamma": gamma,
            "tNaught": tNaught,
            "tPrimeAltered": tPrimeAltered,
            "tNaughtAltered": tNaughtAltered,
            "theoreritcalEpsilonDerivative": theoreritcalEpsilonDerivative
        }
