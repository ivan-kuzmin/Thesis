from math import *
import PROGRAMS as prgs

def PDGD1(ANS):
    FM = float(ANS['FM'])
    FG = float(ANS['FG'])
    AG = float(ANS['AG'])
    CG = float(ANS['CG'])
    DG = float(ANS['DG'])
    WH = float(ANS['WH'])
    Q2H = float(ANS['Q2H'])

    DFG = 1 - FG/FM
    DN = 1.772*DG/sqrt(FG)
    WK = 1.05 - 1.7*sqrt((1 - DFG)*DFG)*AG*CG/(1 + 1.5*AG)
    ZW = WH**1.5*exp(-2*WH**2)
    Z = 1 + 1.5*DFG**2/(1 + WH**8)
    PDO = (1 - 0.25*WH + 0.00173*WH**3)/(1 + 0.0003*WH**4) + 0.5*ZW
    PDP = (1 - 0.52*WH + 0.085*WH**2)/(1 + 0.0024*WH**5) + 0.35*ZW
    DPP = (PDP - PDO)*(1 - CG)
    DPD = 0.052*sqrt(DN)*WH**2.5/(1 + 0.3*WH**2.5)
    VD = Q2H/((PDO - PDP)*prgs.TV(1.4, prgs.VW(1.4, WH)))
    DPQ = (1 - PDP)*(4*VD - 10*VD**2 + 12*VD**3)
    if WH > WK:
        Z2 = Z*(1 + (4*AG**1.3*WK)**6)*(1 + 2*sqrt(WH/WK - 1))
        DPF = 2.15*WH*WK**2*AG**0.75*DFG/Z2
    else:
        Z1 = Z*(1 + (4*AG**1.3*WH)**6)
        DPF = 2.15*WH**3*AG**0.75*DFG/Z1
    PD = PDO + DPF + DPQ + DPD + DPP

    answer = {'PDO': PDO, 'PDP': PDP, 'DPF': DPF, 'DPD': DPD, 'DPQ': DPQ, 'DPP': DPP, 'PD0': PD}
    return answer
