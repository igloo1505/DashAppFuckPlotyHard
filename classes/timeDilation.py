import math


def Lorrentz(observerVelocity, matrixVelocity=299792458):
    if not matrixVelocity == 0:
        beta = observerVelocity**2 / matrixVelocity**2
    if matrixVelocity == 0:
        beta = observerVelocity**2
    if not beta == 1:
        return math.sqrt(1 - beta)
    # if beta == 1:
    # return 1
