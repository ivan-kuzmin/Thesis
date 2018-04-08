from math import *
import PROGRAMS as prgs

def RQLN1(ANS):

    K = float(ANS['K'])
    RD = [0]*11
    XD = [0]*11
    for i in range(11):
        RD[i] = (float(ANS['RD' + str(i)]))
        XD[i] = (float(ANS['XD' + str(i)]))
    GC = float(ANS['GC'])
    DXF = float(ANS['DXF'])
    RE = float(ANS['RE'])
    TW = float(ANS['TW'])
    PD = float(ANS['PD'])
    P0C = float(ANS['P0C'])

    RK = RD[10]
    FK = 3.142*RK**2
    SP = 0
    SD = 0
    A[0] = 0
    F[0] = (R[0]/RK)**2
    RED = 8*RE*DXF
    for i in range(1, 21):
        F[i] = (R[i]/RK)**2
        A[i] = atan((RD[i]-RD[i-1])/(XD[i]-XD[i-1]))
    ZA = 3.75*(1 + 2.7*(A[14] + A[15] + A[16] - A[11] - A[12] - A[13]))/(A[11] + A[12] + A[13] - A[8] - A[9] - A[10])
    AC = 0.25*(A[17] + A[18] + A[19] + A[20])
    P0D = P0C/(PD*(1 - 0.007/(0.07 + AC)))
    FC = F[20]
    for i in range(10):
        RD[i] = R[i]
        XD[i] = X[i]

    # Словарь для CQNZ1
    Input = {'K': K, 'DXF': DXF, 'G': G, 'FC': FC, 'AC': AC, 'P0C': P0D}
    for i in range(11): Input.update({'RD' + str(i): RD[i], 'XD' + str(i): XD[i]})
    CQNZ1.CQNZ1(Input)
    DK = CQNZ1.CQNZ1(Input).get('DK')
    DD = CQNZ1.CQNZ1(Input).get('DD')
    CQ = CQNZ1.CQNZ1(Input).get('CQ')
    CQK = CQNZ1.CQNZ1(Input).get('CQK')
    P0K = CQNZ1.CQNZ1(Input).get('P0K')

    FCQ = FC/CQ
    YI = CQ*prgs.YID(1, G, P0C, FCQ)
    RI = CQ*prgs.RID(G, P0C)
    DA = 0.8*(A[0] - A[1])*(1 - 5*DXF/R[0])
    PS = prgs.PV(G, prgs.VQ(2, G, F[0]))
    WS = prgs.WV(G, VPC(G, PS))
    DP[0] = 0.5*G*PS*WS**2*prgs.CPS(WS, DA)
    P[0] = PS + DP[0]
    if P[0] >= 1: W[0] = -prgs.WV(G, prgs.VPC(G, 1/P[0]))\
    if P[0] < 1: W[0] = prgs.WV(G, prgs.VPC(G, P[0]))
    for i in range(1, 20):
        FS = F[i]*2/(1 + cos(A[i]))
        if # ???
            VS = prgs.VQ(2, G, FS)
            WS = prgs.WV(G, VS)
            PS = prgs.PV(G, VS)
            DA = 0.8*(A[i] - A[i+1])*(1 - 5*DXF/R[i])
            Z1 = 0.5*G*PS*WS**2*CPS(WS, DA)
            Z2 = DP[i-1]*exp(-2*(X[i] - X[i-1])R[i-1])*(1 - WS**2)
            DP[i] = Z1 + Z2
            P[i] = PS + DP[i]
            if P[i] >= 1: W[i] = -prgs.WV(G, prgs.VPC(G, 1/P[0]))
            if P[i] > 1: W[i] = prgs.WV(G, prgs.VPC(G, P[i]))
        else # ???
            VS = prgs.VQ(1, G, FS)
            WS = prgs.WV(G, VS)
            PS = prgs.PV(G, VS)
            DA = 0.95*(A[i] - A[i+1])*(1 - 5*DXF/R[i])
            Z1 = 0.5*G*PS*WS**2*prgs.CPS(WS, DA)
            DXK = (X[i] - X[10])/RK
            Z2 = DP[10]*cos(ZA*DXK)/(1 + 4.3*DXK**0.7 + 16*DXK**3)
            P[i] = PS + Z1 + Z2
            W[i] = prgs.WV(G, VPC(G, P[i]))
        else # ???
            VS = prgs.VQ(1, G, FS)
            WS = prgs.WV(G, VS)
            PS = prgs.PV(G, VS)
            DA = 0.95*(A[i] - A[i+1])*(1 - 5*DXF/R[i])
            Z1 = 0.5*G*PS*WS**2*prgs.CPS(WS, DA)
            DXK = (X[i] - X[10])/RK
            Z2 = DP[10]*cos(ZA*DXK)/(1 + 4.3*DXK**0.7 + 16*DxK**3)
            P[i] = PS + Z1 + Z2
            W[i] = prgs.WV(G, prgs.VPC(G, P[i]))
    FS = F[20]*2/(1 + cos(A[20]))
    DXK = (X[20] - X[10])/RK
    Z2 = DP[10]*cos(ZA*DXK)/(1 + 4.3*DXK**0.7 + 16*DXK**3)
    P[20] = prgs.PV(G, prgs.VQ(1, G, FS)) + Z2
    W[20] = prgs.WV(G, prgs.VPC(G, P[20]))
    XSP = X[20]
    RSP = R[20]
    PS = P[20]
    N = 1
    if W[20] < 1.35: CSP = P[20]*P0D*prgs.PNSH(G, prgs.VW(G, W[20]))
    if W[20] >= 1.35: CSP = P[20]*P0D*prgs.PSP(W[20], RED)
    if CSP > 1:
        for i in range(10, 20):
            if XSP >= X[i] and XSP <= X[i+1]: SP = SP + (P[i]*R[i] + PS*RSP)*(RSP - R[i]) + (PS1*RSP + P[i+1]*R[i+1])*(R[i+1] - RSP)
            if XSP < X[i] or XSP > X[i+1]: SP = SP + (P[i]*R[i] + P[i+1]*R[i+1])*(R[i+1] - R[i])
            if XSP >= X[i+1]: SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2**(R[i] + R[i+1])*(X[i+1] - X[i])
            if XSP > X[i] and XSP <= X[i+1]: SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2**(R[i] + RSP)*(XSP - X[i])
            DYD = 3.142*SD*P0C/(FK*YI)
            DDK = DD*P0C/YI
            CYK = 1 - 0.15*DK
            DYK = 1 - (CYK*CQ*prgs.YID(1, G, 1, 1/CQ) + 3.142*SP/FK)*P0C/YI
            CY = 1 - DYK - DYD - DDK
            CR = (CY*YI - FC)/RI
            DRH = 1 - (prgs.YID(1, G, P0C, FC) - FC)/prgs.RID(G, P0C)

            answer = {'N': N, 'P': P, 'CQ': CQ, 'XSP': XSP, 'RSP': RSP, 'DYK': DYK, 'DYF': DYF, 'CY': CY, 'DRH': DRH, 'CR': CR}
            return answer
    N = 2
    ZS[20] = CSP
    for i in range(10):
        M = 20 - i         # CHANGED
        M1 = M + 1
        if W[M] < 1.35: CS[M] = prgs.PNSH(G, prgs.VW(G, W[M]))
        if W[M] >= 1.35: CS[M] = prgs.PSP(W[M], RED)
        DX = (X[20] - X[M])/R[M]
        DAS = A[M]
        ZS[M] = P[M]*P0D*CS[M]*prgs.PSZ(DX, DAS)
        if ZS[M] >= 1:
            Z = (1 - ZS[M1])/(ZS[M] - ZS[M1])
            XSP = X[M1] + (X[M] - X[M1])*Z
            RSP = R[M1] + (R[M] - R[M1])*Z
            PS = P[M1] + (P[M] - P[M1])*Z
            WS = W[M1] + (W[M] - W[M1])*Z
            PS1 = PS*(CS[M1] + (CS[M] - CS[M1])*Z)
            for i in range(M1, 21):
                DX = (X[i] - XSP)/RSP
                P[i] = PS1*prgs.PSZ(DX, DAS)
            for i in range(10, 20):
                if XSP >= X[i] and XSP <= X[i+1]: SP = SP + (P[i]*R[i] + PS*RSP)*(RSP - R[i]) + (PS1*RSP + P[i+1]*R[i+1])*(R[i+1] - RSP)
                if XSP < X[i] or XSP > X[i+1]: SP = SP + (P[i]*R[i] + P[i+1]*R[i+1])*(R[i+1] - R[i])
                if XSP >= X[i+1]: SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2**(R[i] + R[i+1])*(X[i+1] - X[i])
                if XSP > X[i] and XSP <= X[i+1]: SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2**(R[i] + RSP)*(XSP - X[i])
                DYD = 3.142*SD*P0C/(FK*YI)
                DDK = DD*P0C/YI
                CYK = 1 - 0.15*DK
                DYK = 1 - (CYK*CQ*prgs.YID(1, G, 1, 1/CQ) + 3.142*SP/FK)*P0C/YI
                CY = 1 - DYK - DYD - DDK
                CR = (CY*YI - FC)/RI
                DRH = 1 - (prgs.YID(1, G, P0C, FC) - FC)/prgs.RID(G, P0C)

                answer = {'N': N, 'P': P, 'CQ': CQ, 'XSP': XSP, 'RSP': RSP, 'DYK': DYK, 'DYF': DYF, 'CY': CY, 'DRH': DRH, 'CR': CR}
                return answer
    N = 3
    XSP = X[10]
    RSP = R[10]
    DX = (X[20] - X[10])/RK
    DAS = A[11] - prgs.AV(G, prgs.VP(G, P0C))
    PS1 = 1/(P0D*prgs.PSZ(DX, DAS))
    for i in range(M1, 21):
        DX = (X[i] - XSP)/RSP
        P[i] = PS1*prgs.PSZ(DX, DAS)
    for i in range(10, 20):
        if XSP >= X[i] and XSP <= X[i+1]: SP = SP + (P[i]*R[i] + PS*RSP)*(RSP - R[i]) + (PS1*RSP + P[i+1]*R[i+1])*(R[i+1] - RSP)
        if XSP < X[i] or XSP > X[i+1]: SP = SP + (P[i]*R[i] + P[i+1]*R[i+1])*(R[i+1] - R[i])
        if XSP >= X[i+1]: SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2**(R[i] + R[i+1])*(X[i+1] - X[i])
        if XSP > X[i] and XSP <= X[i+1]: SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2**(R[i] + RSP)*(XSP - X[i])
        DYD = 3.142*SD*P0C/(FK*YI)
        DDK = DD*P0C/YI
        CYK = 1 - 0.15*DK
        DYK = 1 - (CYK*CQ*prgs.YID(1, G, 1, 1/CQ) + 3.142*SP/FK)*P0C/YI
        CY = 1 - DYK - DYD - DDK
        CR = (CY*YI - FC)/RI
        DRH = 1 - (prgs.YID(1, G, P0C, FC) - FC)/prgs.RID(G, P0C)

    answer = {'N': N, 'P': P, 'CQ': CQ, 'XSP': XSP, 'RSP': RSP, 'DYK': DYK, 'DYF': DYF, 'CY': CY, 'DRH': DRH, 'CR': CR}
    return answer
