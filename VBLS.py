from math import *

def VBLS(ANS):
    CU = float(ANS['CU'])
    YS = float(ANS['YS'])
    Y = float(ANS['Y'])

    if Y < 0: Y = 0
    CV = CU + 0.09*YS**0.8
    for i in range(0, 500):
        YI = YS + 0.01*(i+1)                                              # CHANGED
        Z = (YI - YS)/(1 - YS)
        ZD = Z**CV
        Z3 = Z**3
        F = YI - 1.25*(YI - YS)*(3*ZD - CV*Z3)/(3*CV*(ZD - Z3))
        if F <= 0:
            break
    Z2 = (3*ZD - CV*Z3)/(YI**1.25*(3 - CV))
    if Y >= YI:
        Z = (Y - YS)/(1 - YS)
        VBLS = (3*Z**CV - CV*Z**3)/(3 - CV)
    else:
        VBLS = Z2*Y**1.25

    answer = {'VBLS': VBLS}
    return answer
