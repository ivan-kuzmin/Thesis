from math import *
import PROGRAMS as prgs
# import pandas as pd

# RF = 5
# RK = 4.27
# RC = 5.93
# BD = 2.92
# BC = 7.01
# G = 1.4
# TW = 1
# PD = 1
# P0C = 3.0

def RQCN1(ANS):

    RF = float(ANS['RF'])
    RK = float(ANS['RK'])
    RC = float(ANS['RC'])
    BD = float(ANS['BD'])
    BC = float(ANS['BC'])
    G = float(ANS['G'])
    TW = float(ANS['TW'])
    PD = float(ANS['PD'])
    P0C = float(ANS['P0C'])

    X = [0]*11
    PS = [0]*11
    ZSP = [0]*11
    FK = pi*RK**2
    FF = (RF/RK)**2
    FC = (RC/RK)**2
    AD = atan((RF - RK)/BD)
    AC = atan((RC - RK)/BC)
    ZQ1 = 0.0585*(1 + 2.63*AD)*AD*(1 - 1/FF**2)/(1 + AD**2)
    ZQ2 = 0.001*(1 - exp(-5*AD**2))/FF
    CQ = 1 - ZQ1 - ZQ2
    AS = 0.7*AD + 0.9*AC
    VK = prgs.VA(G, 1, AS)
    WK = prgs.WV(G, VK)
    PH = PD*(1 - 0.007/(0.07 + AC))
    YIC = CQ*FK*prgs.YID(1, G, P0C, FC/CQ)
    RI = CQ*FK*prgs.RID(G, P0C)
    for i in range(0, 11):
        K = i
        X[i] = BC*(1.1 - 0.1*i)
        R = RC - (BC - X[i])*tan(AC)
        F = (R/RK)**2
        V = prgs.VQ(1, G, F)
        W = prgs.WV(G, V)
        if W <= 1.36:
            N = 3
            BS = 0
            RS = RK
            FS = FK
            DK = BC/RK
            PS1 = PH/prgs.PSZ(DK, AC)
        else:
            DX = (BC - X[i])/R
            CS = prgs.PSP(W, 10000)
            PS[i] = P0C*prgs.PV(G, V)*CS
            ZSP[i] = PS[i]*prgs.PSZ(DX, AC)/PH
            if ZSP[i] >= 1 and i == 1:
                N = 1
                BS = BC
                RS = RC
                FS = FC*FK
                PS1 = PS[1]
            elif ZSP[i] >= 1 and i != 1:
                N = 2
                Z = (1 - ZSP[K-1])/(ZSP[K] - ZSP[K-1])
                BS = X[K-1] + (X[K] - X[K-1])*Z
                RS = RC - (BC - BS)*tan(AC)
                FS = pi*RS**2
                PS1 = PS[K-1] + (PS[K] - PS[K-1])*Z
        FSK = FS/FK
        VS = prgs.VQ(1, G, FSK)
        WS = prgs.WV(G, VS)
        YIS = CQ*FK*prgs.YID(1, G, P0C, FSK/CQ)
        DYA = 0.5*G/(1 + G)*VS**2/(1 + VS**2)*AC**2
        B1 = BS/RK
        DYK = DYA*(1 + 3.1*sin(0.282*B1/AS)*exp(-0.423*B1/AS))
        CF = 0.0025/TW**0.5
        Z1 = RK*prgs.PV(G, VK)*prgs.TV(G, VK)**0.5*WK**4
        Z2 = RS*prgs.PV(G, VS)*prgs.TV(G, VS)**0.5*WS**2*(1 + 2*AC**2)
        DYD = 0.5*pi*G*CF*(Z1 + Z2)*BS*P0C
        F1 = RS
        DX = 0.5*(BC - BS)/RS
        F2 = 0.5*(RS + RC)*prgs.PSZ(DX, AC)
        DX = (BC-BS)/RS
        F3 = RC*prgs.PSZ(DX, AC)
        DYS = 0.333*pi*PS1*(F1 + 4*F2 + F3)*(RC - RS)
        CY = ((1 - DYK)*YIS + DYS - DYD)/YIC
        CR = (CY*YIC - FC*FK)/RI

        answer = {'N': round(N, 4), 'CQ': round(CQ, 4), 'BS': round(BS, 3), 'RS': round(RS, 3), 'CY': round(CY, 3), 'CR': round(CR, 4)}
    return(answer) #(N, CQ, BS, RS, DRH, CY, CR)

# RQCN1(RF, RK, RC, BD, BC, GC, TW, PD, P0C)
# N = RQCN1(RF, RK, RC, BD, BC, GC, TW, PD, P0C)[0]
# CQ = RQCN1(RF, RK, RC, BD, BC, GC, TW, PD, P0C)[1]
# BS = RQCN1(RF, RK, RC, BD, BC, GC, TW, PD, P0C)[2]
# RS = RQCN1(RF, RK, RC, BD, BC, GC, TW, PD, P0C)[3]
# DRH = RQCN1(RF, RK, RC, BD, BC, GC, TW, PD, P0C)[4]
# CY = RQCN1(RF, RK, RC, BD, BC, GC, TW, PD, P0C)[5]
# CR = RQCN1(RF, RK, RC, BD, BC, GC, TW, PD, P0C)[6]

# print("-----------------------")
# print("N =", N, end=" ")
# print("+") if N == 2 else print("(2) -")
# print("CQ =", round(CQ, 4), end=" ")
# print("+") if round(CQ, 4) == 0.9877 else print("(0.9877) -")
# print("BS =", round(BS, 3), end=" ")
# print("+") if round(BS, 3) == 3.429 else print("(3.429) -")
# print("RS =", round(RS, 3), end=" ")
# print("+") if round(RS, 3) == 5.082 else print("(5.082) -")
# print("DRH =", round(DRH, 3), end=" ")
# print("+") if round(DRH, 3) == 0.145 else print("(0.145) -")
# print("CY =", round(CY, 3), end=" ")
# print("+") if round(CY, 3) == 1.046 else print("(1.046) -")
# print("CR =", round(CR, 4), end=" ")
# print("+") if round(CR, 4) == 0.9842 else print("(0.9842) -")
# print("-----------------------")
