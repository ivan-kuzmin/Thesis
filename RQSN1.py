from math import *
import PROGRAMS as prgs
import CQNZ1
# import pandas as pd

# K = 1
# GC = 1.4
# DXF = 0.0288
# P0C = 2
# PD = 0.95
# RD = [2.305, 2.238, 1.926, 1.610, 1.453, 1.376, 1.297, 1.225, 1.151, 1.074, 1.000]
# XD = [0, 0.640, 1.260, 1.880, 2.190, 2.340, 2.490, 2.640, 2.790, 2.940, 3.090]
# P = [0]*11
# ZY = (2/(G + 1))**(1/(G - 1))
# ZR = G*(2/(G + 1))**(G/(G - 1))
# RK = RD[10]
# A1 = 0
# DP = 0

def RQSN1(ANS):

    K = float(ANS['K'])
    G = float(ANS['GC'])
    DXF = float(ANS['DXF'])
    P0C = float(ANS['P0C'])
    PD = float(ANS['PD'])
    RD = [0]*11
    XD = [0]*11
    for i in range(11):
        RD[i] = (float(ANS['RD' + str(i)]))
        XD[i] = (float(ANS['XD' + str(i)]))
    P = [0]*11
    ZY = (2/(G + 1))**(1/(G - 1))
    ZR = G*(2/(G + 1))**(G/(G - 1))
    RK = RD[10]
    A1 = 0
    DP = 0

    for i in range(0, 10):
        A2 = atan((RD[i+1] - RD[i])/(XD[i+1] - XD[i]))
        AS = 0.5*(A1 + A2)
        DA = 0.8*(A1 - A2)*(1 - 5*DXF/RD[i])
        FS = (RD[i]/RK)**2*2/(1 + cos(AS))
        PS = prgs.PV(G, prgs.VQ(2, G, FS))
        WS = prgs.WV(G, prgs.VPC(G, PS))
        Z1 = 0.5*G*PS*WS**2*prgs.CPS(WS, DA)
        Z2 = DP*exp(-2*(XD[i+1]-XD[i])/RD[i])*(1 - WS**2)
        DP = Z1 + Z2
        A1 = A2
        P[i] = PS + DP
    P[10] = (2/(G + 1))**(G/(G - 1)) + 0.5*DP
    A2 = atan((RD[5] - RD[10])/(XD[10] - XD[6]))**2*0.1

    # Словарь для CQNZ1
    Input = {'K': K, 'DXF': DXF, 'G': G, 'FC': 1, 'AC': 0, 'P0C': P0C}
    for i in range(11): Input.update({'RD' + str(i): RD[i], 'XD' + str(i): XD[i]})
    CQNZ1.CQNZ1(Input)
    DK = CQNZ1.CQNZ1(Input).get('DK')
    DD = CQNZ1.CQNZ1(Input).get('DD')
    CQ = CQNZ1.CQNZ1(Input).get('CQ')
    CQK = CQNZ1.CQNZ1(Input).get('CQK')
    P0K = CQNZ1.CQNZ1(Input).get('P0K')

    DQK = 1 - CQK
    CP0 = 1 - DD
    RI = ZR*CQ*P0C*prgs.VP(G, P0C)
    Q = CQ
    VK = prgs.VQ(2, G, CQK/Q)
    YK = ZY*Q*prgs.ZV(VK)
    CY = (ZR*VK*(Q - A2 - (1 - prgs.QV(G, VK)*VK)*DQK) + prgs.PV(G, VK))/YK
    CR = (CY*CP0*P0C*YK - 1)/RI
    P0D = P0C/PD

    # Словарь для CQNZ1
    Input = {'K': K, 'DXF': DXF, 'G': G, 'FC': 1, 'AC': 0, 'P0C': P0D}
    for i in range(11): Input.update({'RD' + str(i): RD[i], 'XD' + str(i): XD[i]})
    CQNZ1.CQNZ1(Input)
    DK = CQNZ1.CQNZ1(Input).get('DK')
    DD = CQNZ1.CQNZ1(Input).get('DD')
    CQ1 = CQNZ1.CQNZ1(Input).get('CQ')
    CQK = CQNZ1.CQNZ1(Input).get('CQK')
    P0K = CQNZ1.CQNZ1(Input).get('P0K')

    Q = CQ1
    VK = prgs.VQ(2, G, CQK/Q)
    YK = ZY*Q*prgs.ZV(VK)
    CY = (ZR*VK*(Q - A2 - (1 - prgs.QV(G, VK)*VK)*DQK) + prgs.PV(G, VK))/YK
    CR1 = (CY*CP0*P0C*YK - 1)/RI
    P02 = P0D

    # Словарь для CQNZ1
    Input = {'K': K, 'DXF': DXF, 'G': G, 'FC': 1, 'AC': 0, 'P0C': P02}
    for i in range(11): Input.update({'RD' + str(i): RD[i], 'XD' + str(i): XD[i]})
    DK = CQNZ1.CQNZ1(Input).get('DK')
    DD = CQNZ1.CQNZ1(Input).get('DD')
    CQ2 = CQNZ1.CQNZ1(Input).get('CQ')
    CQK = CQNZ1.CQNZ1(Input).get('CQK')
    P0K = CQNZ1.CQNZ1(Input).get('P0K')

    P0Q = CQ*P0C/CQ2
    P03 = P0Q/PD
    DP = abs(P02 - P03)
    P02 = P03
    if (DP > 0.002):
        # Словарь для CQNZ1
        Input = {'K': K, 'DXF': DXF, 'G': G, 'FC': 1, 'AC': 0, 'P0C': P02}
        for i in range(11): Input.update({'RD' + str(i): RD[i], 'XD' + str(i): XD[i]})
        DK = CQNZ1.CQNZ1(Input).get('DK')
        DD = CQNZ1.CQNZ1(Input).get('DD')
        CQ2 = CQNZ1.CQNZ1(Input).get('CQ')
        CQK = CQNZ1.CQNZ1(Input).get('CQK')
        P0K = CQNZ1.CQNZ1(Input).get('P0K')
        
    CP2 = P0Q/P0C
    Q = CQ2
    VK = ZY*Q*prgs.ZV(VK)
    CY = (ZR*VK*(Q - A2 - (1 - prgs.QV(G, VK)*VK)*DQK) + prgs.PV(G, VK))/YK
    CR2 = (CY*CP0*CP2*P0C*YK - 1)/RI

    answer = {'CQ': round(CQ, 4), 'CQ1': round(CQ1, 4), 'CP2': round(CP2, 4), 'CJ': round(CY, 4), 'CR': round(CR, 4), 'CR1': round(CR1, 4), 'CR2': round(CR2, 4)}
    return answer

# print("Подпрограмма RQSN1.")
# print("=======================")
# print("Иходные идентификаторы:", end = "\n\n")
# print("K =", K)
# print("GC =", GC)
# print("DXF =", DXF)
# print("P0C =", P0C)
# print("PD =", PD, end="\n\n")
# frame = pd.DataFrame({'RD': [RD[i] for i in range(11)], 'XD': [XD[i] for i in range(11)]})
# print(frame, end = "\n\n")
# print("-----------------------")
# print("CQ =", round(CQ, 4), end=" ")
# print("+") if round(CQ, 4) == 0.9146 else print("(0.9146) -")
# print("CQ1 =", round(CQ1, 4), end=" ")
# print("+") if round(CQ1, 4) == 0.9200 else print("(0.9200) -")
# print("CP2 =", round(CP2, 4), end=" ")
# print("+") if round(CP2, 4) == 0.9948 else print("(0.9948) -")
# print("CJ =", round(CY, 4), end=" ")
# print("+") if round(CY, 4) == 1.0141 else print("(1.0141) -")
# print("CR =", round(CR, 4), end=" ")
# print("+") if round(CR, 4) == 0.9878 else print("(0.9878) -")
# print("CR1 =", round(CR1, 4), end=" ")
# print("+") if round(CR1, 4) == 0.9918 else print("(0.9918) -")
# print("CR2 =", round(CR2, 4), end=" ")
# print("+") if round(CR2, 4) == 0.9823 else print("(0.9823) -")
# print("-----------------------")
