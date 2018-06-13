from math import *
import PROGRAMS as prgs
import XSPGN1
import CXGD1
import PDGDN1
import PGE

def CXNZ1(ANS):
    FM = float(ANS['FM'])
    FG = float(ANS['FG'])
    BG = float(ANS['BG'])
    AG = float(ANS['AG'])
    DG = float(ANS['DG'])
    FN = float(ANS['FN'])
    BN = float(ANS['BN'])
    AN = float(ANS['AN'])
    WH = float(ANS['WH'])

    C = 0.005642*sqrt(FG)
    if BN <= C: AS = AG
    if BN > C: AS = atan(0.5642*(sqrt(FG) - sqrt(FN))/BN)
    DA = AG - 2*AS + AN

    # Словарь для XSPGN1
    Input = {'FM': FM, 'FG': FG, 'BG': BG, 'AG': AG, 'WH': WH}
    PG = PGE.PGE(Input).get('PGE')

    WG = prgs.WV(1.4, prgs.VPP(1.4, prgs.VW(1.4, WH), PG))
    DPA = 0.7*PG*WG**2*prgs.CPS(WG, DA)*FG/FM

    # Словарь для XSPGN1
    Input = {'FM': FM, 'FG': FG, 'BG': BG, 'AG': AG, 'FN': FN, 'BN': BN, 'AN': AN, 'DG': DG, 'WH': WH}
    XSPGN1.XSPGN1(Input)
    XSP = XSPGN1.XSPGN1(Input).get('XSP')
    FSP = XSPGN1.XSPGN1(Input).get('FSP')
    ASP = XSPGN1.XSPGN1(Input).get('ASP')

    BB = 0.5642*(sqrt(FG) - sqrt(FN))/tan(AG)

    # Словарь для CXGD1
    Input = {'FM': FM, 'FG': FG, 'BG': BG, 'AG': AG, 'DG': DG, 'WH': WH}
    CXGD1.CXGD1(Input)
    XS = CXGD1.CXGD1(Input).get('XSP')
    FS = CXGD1.CXGD1(Input).get('FSP')
    AS = CXGD1.CXGD1(Input).get('ASP')
    PD = CXGD1.CXGD1(Input).get('PD0')
    CXG = CXGD1.CXGD1(Input).get('CXG')

    # Словарь для CXGD1
    Input = {'FM': FM, 'FG': FG, 'BG': BG + BB, 'AG': AG, 'DG': DG, 'WH': WH}
    CXGD1.CXGD1(Input)
    XS = CXGD1.CXGD1(Input).get('XSP')
    FS = CXGD1.CXGD1(Input).get('FSP')
    AS = CXGD1.CXGD1(Input).get('ASP')
    PD = CXGD1.CXGD1(Input).get('PD0')
    CXGN = CXGD1.CXGD1(Input).get('CXG')

    # Словарь для PDGDN1
    Input = {'FM': FM, 'FG': FG, 'AG': AG, 'FN': FN, 'BN': BN, 'AN': AN, 'DG': DG, 'WH': WH, 'Q2H': 0}
    PDGDN1.PDGDN1(Input)
    PD0 = PDGDN1.PDGDN1(Input).get('PD0')

    # Словарь для PDGDN1
    Input = {'FM': FM, 'FG': FG, 'AG': AG, 'FN': FN, 'BN': BB, 'AN': AG, 'DG': DG, 'WH': WH, 'Q2H': 0}
    PDGDN1.PDGDN1(Input)
    PDB = PDGDN1.PDGDN1(Input).get('PD0')

    DPD = PD0 - PDB
    Z1 = 1.43/(FM*WH**2)
    Z2 = 1 - 1.25*(XSP - BG)/(BN*(1 + WH**8))
    if XSP > BG: DCX = ((FG - FSP)*DPA*Z2 + 0.75*(FSP - FN)*DPD)*Z1
    if XSP < BG: DCX = (1 - 0.25*FG/FSP)*(FG - FN)*DPD*Z1
    CXN = CXGN - CXG - DCX

    answer = {'XSP': XSP, 'FSP': FSP, 'ASP': ASP, 'PD0': PD0, 'CXG': CXG, 'CXN': CXN}
    return answer
