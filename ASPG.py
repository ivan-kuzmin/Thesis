from math import *

def ASPG(ANS):
    F = float(ANS['F'])
    D = float(ANS['D'])
    W = float(ANS['WH'])

    ZD = 0.04/((1 + W)*D**0.5)
    if W >= 1:
        ZF = 0.085*(F + 1.3*F**4)
        ZW = ((W**2 - 1)/(W**2 + 1))**0.75
        ASPG = 0.04 + ZF + 0.36*ZW + ZD
    else:
        ZF = 0.17*(F + 2.6*F**4/(1 + W**4))/(1 + W**2)
        ZW = sqrt(1 - W**1.5)
        ASPG = 0.04 + ZF + 0.18*ZW + ZD
    answer = {'ASPG': ASPG}
    return answer
