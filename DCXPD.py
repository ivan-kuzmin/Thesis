from math import *

def DCXPD(ANS):
    FM = float(ANS['FM'])
    FN = float(ANS['FN'])
    FSP = float(ANS['FSP'])
    ASP = float(ANS['ASP'])
    DG = float(ANS['DG'])
    WH = float(ANS['WH'])
    PD0 = float(ANS['PD0'])
    PDJ = float(ANS['PDJ'])

    Z1 = 0.5*exp(-4*WH*(1 - 1.02*WH**2)**2)
    Z2 = 0.15*sqrt(DG/sqrt(FN))/(1 + WH**4)
    Z3 = 1.43/(FM*WH**2)
    DCXPD = ((Z1 + Z2)*FSP*sin(ASP) + FSP - FN)*(PD0 - PDJ)*Z3

    # Выходные данные
    # answer = {'EPS': round(EPS, 4), 'CQ': round(CQ, 4), 'CY': round(CY, 4)}
    answer = {'DCXPD' : DCXPD}
    return answer
