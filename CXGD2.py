from math import *
import PROGRAMS as prgs
import CXCT

def CXGD2(ANS):
    FM = float(ANS['FM'])
    FG = float(ANS['FG'])
    BG = float(ANS['BG'])
    AG = float(ANS['AG'])
    CM = float(ANS['CM'])
    CG = float(ANS['CG'])
    DG = float(ANS['DG'])
    WH = float(ANS['WH'])

    G = 1.4
    FGM = FG/FM
    DF = 1 - FGM
    if DF >= 0.01 or AG >= 0.005:
        RM = 0.5642*sqrt(FM)
        RG = 0.5642*sqrt(FG)
        RC = ((BG*tan(AG) + RG)/RM - 1)/(tan(AG)*tan(0.5*AG))
        if RC <= 0: RC = 0
        ZR = 1 + 2.5*(2 - RC)*WH*AG**0.75/((1 + RC)*(1 + 1.4*WH**8))
        CS = (FM*CM + FG*CG)/(FM + FG)
        CS2 = sqrt(0.5*((CM - CS)**2 + (CG - CS)**2))
        DC = 0.1 + 0.15*WH
        AD = 0.125*(DG/RM - DC)*(RM - RG)/(BG*prgs.TV(G, prgs.VW(G, WH)))
        ZD1 = 0.75*prgs.CPA(WH, AD)*DF
        Z = RM**2*sqrt(CS)
        ZD2 = 0.004*(RM + RG)*BG*((DC*RM/DG)**0.25 - 1)/Z
        APL = atan((1 - (1 - sqrt(FGM))/DF)*(RM - RG)/BG)
        ZPL = 0.75*prgs.CPA(WH, APL)*(1 - CS + CS2)*DF

        # Словарь для CXCT
        Input = {'WH': WH, 'F': FGM, 'AG': AG}
        CXGD2 = CXCT.CXCT(Input).get('CXCT')*ZR + ZPL + ZD2 - ZD1
    else:
        CXGD2 = 0

    answer = {'CXGD2': CXGD2}
    return answer
