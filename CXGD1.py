from math import *
import PROGRAMS as prgs
import PDGD1
import CXCT
import XSPGN1

def CXGD1(ANS):
    FM = float(ANS['FM'])
    FG = float(ANS['FG'])
    BG = float(ANS['BG'])
    AG = float(ANS['AG'])
    DG = float(ANS['DG'])
    WH = float(ANS['WH'])

    G = 1.4
    RM = 0.5642*sqrt(FM)
    RG = 0.5642*sqrt(FG)
    FGM = FG/FM
    DF = 1 - FGM
    VH = prgs.VW(1.4, WH)
    DC = 0.5 + 0.75*WH
    FB = 78.54
    F1 = FG*FB/FM

    # Словарь для PDGD1
    Input = {'FM': FB, 'FG': F1, 'AG': AG, 'CG': 1, 'DG': DC, 'WH': WH, 'Q2H': 0}
    PDGD1.PDGD1(Input)
    P0 = PDGD1.PDGD1(Input).get('PD0')
    PP = PDGD1.PDGD1(Input).get('PDP')
    D1 = PDGD1.PDGD1(Input).get('DPF')
    D2 = PDGD1.PDGD1(Input).get('DPD')
    D3 = PDGD1.PDGD1(Input).get('DPQ')
    D4 = PDGD1.PDGD1(Input).get('DPP')
    PDB = PDGD1.PDGD1(Input).get('PD0')

    # Словарь для PDGD1
    Input = {'FM': FM, 'FG': FG, 'AG': AG, 'CG': 1, 'DG': DG, 'WH': WH, 'Q2H': 0}
    PDGD1.PDGD1(Input)
    P0 = PDGD1.PDGD1(Input).get('PD0')
    PP = PDGD1.PDGD1(Input).get('PDP')
    D1 = PDGD1.PDGD1(Input).get('DPF')
    D2 = PDGD1.PDGD1(Input).get('DPD')
    D3 = PDGD1.PDGD1(Input).get('DPQ')
    D4 = PDGD1.PDGD1(Input).get('DPP')
    PD0 = PDGD1.PDGD1(Input).get('PD0')

    # Словарь для XSPGN1
    Input = {'FM': FM, 'FG': FG, 'BG': BG, 'AG': AG, 'FN': FG, 'BN': 0, 'AN': AG, 'DG': DG, 'WH': WH}
    XSPGN1.XSPGN1(Input)
    XSP = XSPGN1.XSPGN1(Input).get('XSP')
    FSP = XSPGN1.XSPGN1(Input).get('FSP')
    ASP = XSPGN1.XSPGN1(Input).get('ASP')

    RS = 0.5642*sqrt(FSP)
    if DF >= 0.01 or AG >= 0.001:
        RCM = (BG*tan(AG) + RG - RM)/(tan(AG)*tan(0.5*AG))
        if RCM <= 0: RCM = 0
        RK = RCM/RM
        ZR = 1 + 2.5 *(2 - RK)*WH**2*AG**0.75/((2 + RK)*(1 + WH**8))
        ZD1 = 0.004*(RM + RS)*XSP*((0.2*DC*RM/DG)**0.2 - 1)/RM**2
        ZD2 = 1.43*(FSP - FG)*(PDB - PD0)/(FM*WH**2)

        # Словарь для CXCT
        Input = {'WH': WH, 'F': FGM, 'AG': AG}
        CX = CXCT.CXCT(Input).get('CXCT')*ZR + ZD1 + ZD2
    else:
        CX = 0.008*BG*((DC/DG)**0.2 - 1)/RM

    answer = {'XSP': XSP, 'FSP': FSP, 'ASP': ASP, 'CXG': CX, 'PD0': PD0}
    return answer
