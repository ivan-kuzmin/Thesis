from math import *
import PROGRAMS as prgs
import XSPGN1
import CXGD2
import PDGD1
import PGE

def CXNZ2(ANS):
    FM = float(ANS['FM'])
    FG = float(ANS['FG'])
    BG = float(ANS['BG'])
    AG = float(ANS['AG'])
    CM = float(ANS['CM'])
    CG = float(ANS['CG'])
    DG = float(ANS['DG'])
    FNG = float(ANS['FNG'])
    FN = float(ANS['FN'])
    BN = float(ANS['BN'])
    AN = float(ANS['AN'])
    B0G = float(ANS['B0G'])
    B0N = float(ANS['B0N'])
    WH = float(ANS['WH'])

    G = 1.4
    FM1 = 0.5*FM
    FG1 = 0.5*FG
    FN1 = 0.5*FN
    A0N = atan(0.5*(B0G - B0N)/BN)
    CNB = 0.8*sqrt(FNG)/B0G
    FNS = FN + 0.25*(FNG - FN)*CNB
    SNS = 2*(2.51*sqrt(FN)*(1 - 0.25*CNB) + B0N*(1 - 0.7*CNB))
    ANS1 = 2*(2.51*sqrt(FN)*(1 - 0.25*CNB)*(AN + 0.25*A0N) + B0N*(1 - 0.7*CNB)*AG)/SNS
    FN2 = 0.5*FNS
    BB = 0.5642*(sqrt(FG1) - sqrt(FN2))/tan(AG)
    CS = 12.57*FNS/SNS**2

    # Словарь для XSPGN1
    Input = {'FM': FM1, 'FG': FG1, 'BG': BG, 'AG': AG, 'FN': FN2, 'BN': BN, 'AN': ANS1, 'DG': DG, 'WH': WH}
    XSPGN1.XSPGN1(Input)
    XSP = XSPGN1.XSPGN1(Input).get('XSP')
    FS = XSPGN1.XSPGN1(Input).get('FSP')
    ASP = XSPGN1.XSPGN1(Input).get('ASP')

    FSP = 2*FS

    # Словарь для PDGD1
    Input = {'FM': FM, 'FG': FNS, 'AG': ANS1, 'CG': CS, 'DG': DG, 'WH': WH, 'Q2H': 0}
    PDGD1.PDGD1(Input)
    P1 = PDGD1.PDGD1(Input).get('PDO')
    P2 = PDGD1.PDGD1(Input).get('PDP')
    F = PDGD1.PDGD1(Input).get('DPF')
    D = PDGD1.PDGD1(Input).get('DPD')
    Q = PDGD1.PDGD1(Input).get('DPQ')
    P = PDGD1.PDGD1(Input).get('DPP')
    PD0 = PDGD1.PDGD1(Input).get('PD0')

    # Словарь для PDGD1
    Input = {'FM': FM, 'FG': FNS, 'AG': AG, 'CG': CS, 'DG': DG, 'WH': WH, 'Q2H': 0}
    PDGD1.PDGD1(Input)
    P1 = PDGD1.PDGD1(Input).get('PDO')
    P2 = PDGD1.PDGD1(Input).get('PDP')
    F = PDGD1.PDGD1(Input).get('DPF')
    D = PDGD1.PDGD1(Input).get('DPD')
    Q = PDGD1.PDGD1(Input).get('DPQ')
    P = PDGD1.PDGD1(Input).get('DPP')
    PDB = PDGD1.PDGD1(Input).get('PD0')

    # Словарь для CXGD2
    Input = {'FM': FM, 'FG': FG, 'BG': BG, 'AG': AG, 'CM': CM, 'CG': CG, 'DG': DG, 'WH': WH}
    CXG = CXGD2.CXGD2(Input).get('CXGD2')

    # Словарь для CXGD2
    Input = {'FM': FM, 'FG': FNS, 'BG': BG + BB, 'AG': AG, 'CM': CM, 'CG': CS, 'DG': DG, 'WH': WH}
    CXGN = CXGD2.CXGD2(Input).get('CXGD2')

    # Словарь для CXGD2
    Input = {'FM': FM1, 'FG': FG1, 'BG': BG, 'AG': AG, 'WH': WH}
    PG = PGE.PGE(Input).get('PGE')
    WG = prgs.WV(G, prgs.VPP(G, prgs.VW(G, WH), PG))
    DPA = 0.7*PG*WG**2*prgs.CPS(WG, AG - ANS1)*FG/FM
    DPD = PD0 - PDB
    Z1 = 1.43/(FM*WH**2)
    Z2 = 1 - 0.85*DG/FG1**0.5
    Z2 = Z2/(1 + (XSP - BG)*(1 + WH**6)/(BN*(1 + 3*WH**7)))
    if XSP > BG: DCX = ((FG - FSP)*Z2*DPA + 0.75*(FSP - FN)*DPD)*Z1
    if XSP <= BG: DCX = (FG - FN)*DPD*Z1
    CXN = CXGN - CXG - DCX

    answer = {'PD0': PD0, 'XSP': XSP, 'FSP': FSP, 'ASP': ASP, 'CXG': CXG, 'CXN': CXN}
    return answer
