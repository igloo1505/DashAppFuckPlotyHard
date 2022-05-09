import math

def isSafeNumber(n, withZero=False):
    if not withZero:
        if math.isfinite(n) and not math.isnan(n):
            return True
        if not math.isfinite(n) or math.isnan(n):
            return False
    if withZero:
        if math.isfinite(n) and not math.isnan(n) and not n == 0:
            return True
        if not math.isfinite(n) or math.isnan(n) or n == 0:
            return False