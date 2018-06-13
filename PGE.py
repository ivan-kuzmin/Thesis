from math import *
import PROGRAMS as prgs

def PGE(ANS):
    FM = float(ANS['FM'])
    FG = float(ANS['FG'])
    BG = float(ANS['BG'])
    AG = float(ANS['AG'])
    WH = float(ANS['WH'])

    F = FG/FM
    RM = 0.5642*sqrt(FM)
    RG = 0.5642*sqrt(FG)
    DR = 1 - RG/RM
    WK = 1 - 1.4*sqrt((1 - F)*F)*AG/(1 + AG)
    if DR <= 0.01 or AG <= 0.001:
        PGE = 1
    else:
        ZB = BG*tan(AG)/(RM - RG)
        A = AG/(1 + (ZB - 1)**2)
        if WH > WK:
            W = WK/WH
            ZW = 1 + sqrt((1 - W)*W*F)
            PGE = 1 - 0.7*WH**2*prgs.CPA(WH, A)*(1 - 1.8*(AG*(1 - F))**0.25/ZW)
        else:
            PGE = 1 - 0.7*WH**2*prgs.CPA(WH, A)*(1 - 1.8*(AG*(1 - F))**0.25)

    answer = {'PGE': PGE}
    return answer
