from math import *
import PROGRAMS as prgs
import XSPGN1
import PDGDN1

def PDJT1(ANS):
    FM = float(ANS['FM'])
    FG = float(ANS['FG'])
    BG = float(ANS['BG'])
    AG = float(ANS['AG'])
    FN = float(ANS['FN'])
    BN = float(ANS['BN'])
    AN = float(ANS['AN'])
    FC = float(ANS['FC'])
    FK = float(ANS['FK'])
    BC = float(ANS['BCN'])
    AC = float(ANS['AC'])
    DG = float(ANS['DG'])
    WH = float(ANS['WH'])
    P0C = float(ANS['P0C'])
    GC = float(ANS['GC'])
    Q2 = float(ANS['Q2'])

    # Словарь для XSPGN1
    Input = {'FM': FM, 'FG': FG, 'BG': BG, 'AG': AG, 'FN': FN, 'BN': BN, 'AN': AN, 'DG': DG, 'WH': WH}
    XSPGN1.XSPGN1(Input)
    XSP = XSPGN1.XSPGN1(Input).get('XSP')
    FSP = XSPGN1.XSPGN1(Input).get('FSP')
    ASP = XSPGN1.XSPGN1(Input).get('ASP')

    # Словарь для PDGDN1
    Input = {'FM': FM, 'FG': FG, 'AG': AG, 'FN': FN, 'BN': BN, 'AN': AN, 'DG': DG, 'WH': WH, 'Q2H': 0}
    PDGDN1.PDGDN1(Input)
    PD0 = PDGDN1.PDGDN1(Input).get('PD0')

    RM = 0.5642*sqrt(FM)
    RG = 0.5642*sqrt(FG)
    RN = 0.5642*sqrt(FN)
    RC = 0.5642*sqrt(FC)
    RK = 0.5642*sqrt(FK)
    VC = prgs.VQ(1, GC, FC/FK)
    WC = prgs.WV(GC, VC)
    PC = P0C*prgs.PV(GC, VC)
    VS = prgs.VP(GC, P0C)
    WS = prgs.WV(GC, VS)
    PN = P0C*prgs.PV(GC, VC)
    FS = FK/FSP*sqrt(PN)/prgs.QV(GC, VS)
    FSK = 0.7 - 0.25*WH**2/(1 + 0.7*WH**2)
    DF = FS - FSK
    if WH <= 1.1: Z1 = 0.48*WH**3
    if WH > 1.1: Z1 = 0.64/(0.285 + 0.65*WH)
    if WH <= 1: Z2 = 0.45*WH**3.2
    if WH > 1: Z2 = (0.45 - 0.18*(WH**2 - 1))/WH**2
    if WH <= 1: Z3 = 0.35*WH**3.2
    if WH > 1: Z3 = (0.35 + 0.061*(WH**2 - 1))/WH**2
    if FS <= FSK: DPS = Z1*FS**1.2
    if FS > FSK: DPS = Z1*FSK**1.2 - Z2*DF/(1 + Z3*DF)
    DPK = 0.1*Z1*exp(-2.5*sqrt(abs(DF)))
    A1 = AN
    while True:
        A2 = AN + AC - A1
        P1 = 1 + 0.7*WH**2*prgs.CPS(WH, A1)
        P2 = PC*(1 + 0.5*GC*WC**2*prgs.CPS(WC, A2))
        if abs(P2 - P1) <= 0.01:
            PDS = 0.5*(P1 + P2)
            PDS = PDS + (1 - PDS)*(DG/(DG + 0.318*FSP/RM))**0.5
            PS = 1 + 0.4*WC**2*(1 + 0.54*WC**2 - 0.003*WC**5)/(1 + WC**2)
            PDP = (1 - 0.52*WH + 0.085*WH**2)/(1 + 0.0024*WH**5) + 0.35*WH**1.5*exp(-2*WH**2)
            DPN = prgs.PV(GC, 1) - prgs.PV(GC, VC)
            Z5 = exp(-0.8*P0C**2*(1 - 1/(PS*PC))**2)
            DPC = 0.65*WH**2*FC*DPN*Z5/(FSP*(1 + WH**2))
            ZS = (1 + 5.5*FS**2*WH**3)/(1 + 1.5*FS**2/WH**3)
            ZFA = 0.45*prgs.CPS(WH, ASP)*WH**2*ZS/(1 + WH**8)
            if WH <= 0.99: DPA = ZFA
            if WH > 0.99: DPA = ZFA*(1 + 3*(WH - 0.99)**7)
            Y = Q2*P0C*FK/((FSP - 0.99*FC)*PD0)
            V = prgs.VY(1.4, Y)/prgs.VW(1.4, WH)
            DPQ = 1.67*(1 - PDP)*V**0.75
            if BC > 0.01*RN:
                PDH = 0
                B = 0
                ZA = 2.76*(RN - RC)/(BC*(FN/FK - 1)**4)
                VJ = prgs.VP(GC, P0C/PD0)
                FJ = FK*PN**0.25/prgs.QV(GC, VJ)
                RJ = 0.5642*sqrt(FJ)
                ZJ = (RN - RJ)/(RN - RC)
                if ZA + ZJ >= 1.1:
                    ZF = (RC + RJ)*BC/(FN - 0.5*(FJ + FC))
                    DPB = 0.045*PD0*(1 - V)**2*ZF*WS**2/(1 + 0.3*WS)
                else:
                    PDJ = P0C*prgs.PV(GC, prgs.VA(GC, VC, atan((RN - RC)/BC) - AC))
                    print("PDJT1, запуск второго контура")
                    answer = {'PDO': 0}
                    return answer
            else:
                DPB = 0
                B = -BC
                PDH = PDP + (1 - PDP)*(DG/(DG + RN - RC))**0.5
                PDS = PDS + (PDH - PDS)*B/(B + RN - RC)
            break
        else:
            A1 = 0.1*(P2 - P1) + A1

    PDJ = PD0 - DPC - DPB - DPS + DPA + DPQ
    Z6 = DG + 0.1*RC + (BG + BN + B - XSP)*1.5
    PDJ = PDJ + (1 - PDJ)*Z6/(Z6 + 0.5642*(sqrt(FSP) - sqrt(FC)))
    PDJ = PDS + (PDJ - PDS)*((FSP/FC)**4 - 1)/(FSP/FC)**4

    answer = {'XSP': XSP, 'FSP': FSP, 'ASP': ASP, 'PD0': PD0, 'PDJ': PDJ}
    return answer
