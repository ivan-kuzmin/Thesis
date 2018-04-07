from math import *
import PROGRAMS as prgs
# import pandas as pd

# K = 2
# RD = [2.305, 2.238, 1.926, 1.610, 1.453, 1.376, 1.297, 1.225, 1.151, 1.074, 1.000]
# XD = [0, 0.640, 1.260, 1.880, 2.190, 2.340, 2.490, 2.640, 2.790, 2.940, 3.090]

#RD = [0.745955, 0.72, 0.62, 0.51383, 0.464429, 0.441026, 0.416707, 0.394413, 0.37129, 0.347041, 0.323625]
#XD = [0.0, 0.2, 0.4, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]

# DXF = 0.0288
# G = 1.4
# FC = 1
# AC = 0
# P0C = 2.0

# def CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C):
def CQNZ1(ANS):
    K = float(ANS['K'])
    RD = [0]*11
    XD = [0]*11
    for i in range(11):
        RD[i] = (float(ANS['RD' + str(i)]))
        XD[i] = (float(ANS['XD' + str(i)]))
    DXF = float(ANS['DXF'])
    G = float(ANS['G'])
    FC = float(ANS['FC'])
    AC = float(ANS['AC'])
    P0C = float(ANS['P0C'])

    T = [0]*11
    T0 = [0]*11
    T1 = [0]*11
    T2 = [0]*11
    TA = [0]*11
    XL = [0]*11

    ZPK = (0.5*(G + 1))**(G/(G - 1))
    BD = XD[10] - XD[0]
    T[0] = 0
    F = 0
    XL[0] = BD/RD[0]
    for i in range(1,11):                                                 #DO 1 I=2,11
        T[i] = atan((RD[i-1]-RD[i])/(XD[i]-XD[i-1]))                      #END DO 1
    DP = 0.01*(1 - exp(-5*T[1]**2))*(RD[10]/RD[0])**2
    for i in range(0,9):                                                  #DO 2 I=1,9
        Z = (XD[i+1] - XD[i])/(XD[i+2] - XD[i])
        T0[i] = T[i+1]*(1 + Z) - T[i+2]*Z
        T1[i] = T[i+1]*(1 - Z) + T[i+2]*Z
        T2[i] = -T[i+1]*(1 - Z) + T[i+2]*(2 - Z)                          #END DO 2
    TA[0] = T0[0]
    TA[1] = 0.5*(T0[1] + T1[0])
    TA[9] = 0.5*(T1[8] + T2[7])*(1 - 1*DXF*RD[10]/RD[0]**2)
    TA[10] = T2[8]*(1 - 5*DXF*RD[10]/RD[0]**2)
    for i in range(2,9):                                                  #DO 3 I=3,9
        TA[i] = (T0[i] + T1[i-1] + T2[i-2])/3                             #END DO 3
    for i in range(1,11):                                                 #DO 4 I=2,11
        XL[i] = (XD[10] - XD[i])/RD[0]
        Z1 = prgs.FT(TA[i-1])*exp(-15*XL[i-1])
        Z2 = prgs.FT(TA[i])*exp(-15*XL[i])
        F += 0.5*(Z1+Z2)*(XL[i-1] - XL[i])                                #END DO 4
    DK = F*(1 - (RD[10]/RD[0])**4) + DP
    ZDX = (RD[0]/DXF)**0.2
    DD = 3e-4*BD/RD[10]*ZDX + 3e-2*(RD[10]/RD[0])**6
    if K == 1:
        DD = 0
    CQK = 1 - DK - DD
    P0K = ZPK + 29*DK
    if FC <= 1.01 or AC <= 0.01:
        if (P0C >= P0K):
            CQ = CQK
        else:
            B = (1 + 2e5*DK**2)/(1 + 4e5*DK**2)
            P0C1 = 1 + (ZPK - 1)*((P0C - 1)/(P0K - 1))**B
            CQ = CQK*prgs.QV(G, prgs.VP(G, P0C1))
    else:
        P0K = 1 + (P0K - 1)/(1 + 0.088*sqrt(FC - 1)/(0.005 + AC**1.5))
        CQK = CQK + 0.1*DK*exp(-1.2*AC/DK)

    # answer = [["DK", "DD", "CQ", "CQK", "P0K"], [DK, DD, CQ, CQK, P0K]]
    answer = {'DK': round(DK, 4), 'DD': round(DD, 4), 'CQ': round(CQ, 4), 'CQK': round(CQK, 4), 'P0K': round(P0K, 3)}
    # return(DK, DD, CQ, CQK, P0K)
    return answer

# CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)
# DK = CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)[0]
# DD = CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)[1]
# CQ = CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)[2]
# CQK = CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)[3]
# P0K = CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)[4]
#
# answer = [["DK", "DD", "CQ", "CQK", "P0K"], [0, 0, 0, 0, 0]]
# for i in range(len(answer[0])):
#     answer[1][i] = CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)[i]
# answer = {"DK":CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)[0], "DD":CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)[1], "CQ":CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)[2], "CQK":CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)[3], "P0K":CQNZ1(K, RD, XD, DXF, G, FC, AC, P0C)[4]}

# print("Подпрограмма CQNZ1.")
# print("=======================")
# print("Иходные идентификаторы:", end = "\n\n")
# print("K =", K)
# print("DXF =", DXF)
# print("G =", G)
# print("FC =", FC)
# print("AC =", AC)
# print("P0C =", P0C, end="\n\n")
# frame = pd.DataFrame({'RD': [RD[i] for i in range(11)], 'XD': [XD[i] for i in range(11)]})
# print(frame, end = "\n\n")
# print("-----------------------")
# print("DK =", round(DK, 4), end=" ")
# print("(0.055) +") if round(DK, 4) == 0.055 else print("(0.055) -")
# print("DD =", round(DD, 4), end=" ")
# print("(0.0025) +") if round(DD, 4) == 0.0025 else print("(0.0025) -")
# print("CQ =", round(CQ, 4), end=" ")
# print("(0.9169) +") if round(CQ, 4) == 0.9169 else print("(0.9169) -")
# print("CQK =", round(CQK, 4), end=" ")
# print("(0.9426) +") if round(CQK, 4) == 0.9426 else print("(0.9426) -")
# print("P0K =", round(P0K, 3), end=" ")
# print("(3.487) +") if round(P0K, 3) == 3.487 else print("(3.487) -")
# print("-----------------------")
