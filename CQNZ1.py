from math import *
import PROGRAMS as prgs

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

    def FT(A):
        FT = 15*abs(A)**2.4/(1+7.7*abs(A)**1.8)
        return FT

    ZPK = (0.5*(G + 1))**(G/(G - 1))
    BD = XD[10] - XD[0]
    T[0] = 0
    F = 0
    XL[0] = BD/RD[0]
    for i in range(1, 11):
        T[i] = atan((RD[i-1] - RD[i])/(XD[i] - XD[i-1]))
    DP = 0.01*(1 - exp(-5*T[1]**2))*(RD[10]/RD[0])**2
    for i in range(9):
        Z = (XD[i+1] - XD[i])/(XD[i+2]-XD[i])
        T0[i] = T[i+1]*(1 + Z) - T[i+2]*Z
        T1[i] = T[i+1]*(1 - Z) + T[i+2]*Z
        T2[i] = -T[i+1]*(1 - Z) + T[i+2]*(2 - Z)
    TA[0] = T0[0]
    TA[1] = 0.5*(T0[1] + T1[0])
    TA[9] = 0.5*(T1[8] + T2[7])*(1 - 1*DXF*RD[10]/RD[0]**2)
    TA[10] = T2[8]*(1 - 5*DXF*RD[10]/RD[0]**2)
    for i in range(2,9):
        TA[i] = (T0[i] + T1[i-1] + T2[i-2])/3
    for i in range(1,11):
        XL[i] = (XD[10] - XD[i])/RD[0]
        Z1 = FT(TA[i-1])*exp(-15*XL[i-1])
        Z2 = FT(TA[i])*exp(-15*XL[i])
        F = F + 0.5*(Z1+Z2)*(XL[i-1] - XL[i])
    DK = F*(1 - (RD[10]/RD[0])**4) + DP
    ZDX = (RD[0]/DXF)**0.2
    DD = 3e-4*BD/RD[10]*ZDX + 3e-2*(RD[10]/RD[0])**6
    if K == 1:
        DD = 0
    CQK = 1 - DK - DD
    P0K = ZPK + 29*DK
    if FC > 1.01 or AC > 0.01:
        P0K = 1 + (P0K - 1)/(1 + 0.088*sqrt(FC - 1)/(0.005 + AC**1.5))
        CQK = CQK + 0.1*DK*exp(-1.2*AC/DK)
    if P0C >= P0K:
        CQ = CQK
    else:
        B = (1 + 2e5*DK**2)/(1 + 4e5*DK**2)
        P0C1 = 1 + (ZPK - 1)*((P0C - 1)/(P0K - 1))**B
        CQ = CQK*prgs.QV(G, prgs.VP(G, P0C1))

    answer = {'DK': round(DK, 4), 'DD': round(DD, 4), 'CQ': round(CQ, 4), 'CQK': round(CQK, 4), 'P0K': round(P0K, 3)}
    return answer
