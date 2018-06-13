from math import *

def RXSP1(ANS):
    W = float(ANS['WS'])
    R = float(ANS['RS0'])
    A = float(ANS['AS0'])
    XS = float(ANS['XS'])

    TA = tan(A)
    X = XS/R
    RS = R*(1 + TA*X*(1 + 2*X/(1 + W)))
    AS = atan(TA*(1 + 4*X/(1 + W)))

    answer = {'RS': round(RS, 4), 'AS': round(AS, 4)}
    return answer
