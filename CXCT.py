from math import *

def CXCT(ANS):
    W = float(ANS['WH'])
    F = float(ANS['F'])
    A = float(ANS['AG'])

    Z = A/((1 + A)*sqrt(0.25 + F))
    Z1 = 1.4*(1 - 0.13*exp(-12*abs(W - 1.075)))
    # Z1 = 1.46
    if W >= 1.075:
        Z2 = (1 - 1.904*A)*A
        Z3 = (1 - F)*(0.04 + 1.2*F*F + 2.161*Z)
        Z4 = 2.469/W**1.23
    else:
        Z2 = (1 - (1.2 + 0.75*exp(-20*(1 - W)**2))*A)*A
        Z3 = (1 - F)*(0.04 + 1.2*F*F + 1.2*Z*W**8)
        Z4 = 1 + 1.2*W**3*exp(-30*(1 - W)**2)
    CXCT = Z1*Z2*Z3*Z4

    answer = {'CXCT': round(CXCT, 4)}
    return answer
