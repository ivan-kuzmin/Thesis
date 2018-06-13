from math import *
import PROGRAMS as prgs

def PDGDN1(ANS):
    FM = float(ANS['FM'])
    FG = float(ANS['FG'])
    AG = float(ANS['AG'])
    FN = float(ANS['FN'])
    BN = float(ANS['BN'])
    AN = float(ANS['AN'])
    DG = float(ANS['DG'])
    WH = float(ANS['WH'])
    Q2 = float(ANS['Q2H'])

    FGM = FG/FM
    FNM = FN/FM
    RG = 0.5642*sqrt(FG)
    RN = 0.5642*sqrt(FN)
    D = DG/RG
    AS = AN
    if BN > 0.001*RN: AS = atan((RG - RN)/BN)
    DA = AG - 2*AS + AN
    Z = 1 + 1.5*(1 - FNM)**2/(1 + WH**8)
    A = (AG*(FM - FG) + 2*AN*(FG - FN))/(FM + FG - 1.99*FN)
    DK = 0.4*abs(DA)**0.25/(1 + 10*abs(DA))*FGM
    Z3 = exp(-5*(WH - 1)**2)
    WK = 1.05 - 1.7*sqrt((1 - FNM)*FNM)*A/(1 + 1.5*A) + DK*Z3
    ZW = WH**1.5*exp(-2*WH**2)
    PD1 = (1 - 0.25*WH + 0.00173*WH**3)/(1 + 0.0003*WH**4) + 0.5*ZW
    PD2 = (1 - 0.52*WH + 0.085*WH**2)/(1 + 0.0024*WH**5) + 0.35*ZW
    DPD = 0.052*sqrt(D)*WH**2.5/(1 + 0.3*WH**2.5)
    VD = Q2/(PD1*prgs.TV(1.4, prgs.VW(1.4, WH)))
    DPQ = (1 - PD2)*(4*VD - 10*VD**2 + 12*VD**3)
    if WH > WK:
        Z2 = Z*(1 + (4*A**1.3*WK)**6)*(1 + 2*sqrt(WH/WK - 1))
        DPF = 2.15*WK**2*WH*AN**0.75*(1 - FNM)/Z2
    else:
        Z1 = Z*(1 + (4*A**1.3*WH)**6)
        DPF = 2.15*WH**3*A**0.75*(1 - FNM)/Z1
    PD = PD1 + DPF + DPQ + DPD
    print(PD)
    answer = {'PD0': PD}
    return answer
