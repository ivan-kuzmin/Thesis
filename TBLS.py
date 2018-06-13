from math import *

def TBLS(ANS):
    T0 = float(ANS['T0'])
    XD = float(ANS['XD'])
    Y = float(ANS['Y'])

    if XD <= 0.5:
        TBLS = T0
    else:
        Z1 = XD**2
        Z = (Z1 - Y)/Z1
        if Y <= Z1: TBLS = 1 + (T0 - 1)*(1 - Z**1.25)**1.25
        if Y > Z1: TBLS = T0

    answer = {'TBLS': TBLS}
    return answer
