from math import *
import PROGRAMS as prgs
import CQNZ1

def RQLN1(ANS):
    # def RQLN11(PPP):
    K = float(ANS['K'])
    R = [0]*21
    X = [0]*21
    for i in range(21):
        R[i] = (float(ANS['RD' + str(i)]))
        X[i] = (float(ANS['XD' + str(i)]))
    G = float(ANS['GC'])
    DXF = float(ANS['DXF'])
    RE = float(ANS['RE'])
    TW = float(ANS['TW'])
    PD = float(ANS['PD'])
    P0C = float(ANS['P0C'])
    # P0C = PPP

    RD = [0]*11
    XD = [0]*11
    A = [0]*21
    F = [0]*21
    P = [0]*21
    DP = [0]*21
    W = [0]*21
    ZS = [0]*21
    GS = [0]*21

    RK = R[10]
    FK = 3.142*RK**2
    SP = 0
    SD = 0
    A[0] = 0
    F[0] = (R[0]/RK)**2
    RED = 8*RE*DXF
    for i in range(1, 21):
        F[i] = (R[i]/RK)**2
        A[i] = atan((R[i]-R[i-1])/(X[i]-X[i-1]))
        # print(str(R[i]-R[i-1])+" = R[i]-R[i-1]\n"+str(X[i]-X[i-1])+" = X[i]-X[i-1]\n"+str(A[i]) + " = A[" + str(i) + "]\n")
        # if i == 6 or i == 8 or i == 10: A[i] = -0.38050637711236673
        # if i == 7 or i == 9: A[i] = -0.3805063771123637
        # if i == 12 or i == 16 or i == 18 or i == 20: A[i] = 0.23824475817874446
        # if i == 11 or i == 17 or i == 19: A[i] = 0.23824475817874544
    # A[6] = -0.38050637711236673
    # A[7] = -0.3805063771123637
    # A[8] = -0.38050637711236673
    # A[9] = -0.3805063771123637
    # A[10] = -0.38050637711236673
    # A[11] = 0.23824475817874544
    # A[12] = 0.23824475817874446
    # A[16] = 0.23824475817874446
    # A[17] = 0.23824475817874544
    # A[18] = 0.23824475817874446
    # A[19] = 0.23824475817874544
    # A[20] = 0.23824475817874446
    ZA = 3.75*(1 + 2.7*(A[14] + A[15] + A[16] - A[11] - A[12] - A[13]))/(A[11] + A[12] + A[13] - A[8] - A[9] - A[10])
    AC = 0.25*(A[17] + A[18] + A[19] + A[20])
    P0D = P0C/(PD*(1 - 0.007/(0.07 + AC)))
    FC = F[20]
    for i in range(11):
        RD[i] = R[i]
        XD[i] = X[i]

    # print(str(FC)+" = FC\n"+str(AC)+" = AC\n"+str(P0C)+" = P0C\n")
    # Словарь для CQNZ1
    Input = {'K': K, 'DXF': DXF, 'G': G, 'FC': FC, 'AC': AC, 'P0C': P0D}
    for i in range(11): Input.update({'RD' + str(i): RD[i], 'XD' + str(i): XD[i]})
    CQNZ1.CQNZ1(Input)
    DK = CQNZ1.CQNZ1(Input).get('DK')
    DD = CQNZ1.CQNZ1(Input).get('DD')
    CQ = CQNZ1.CQNZ1(Input).get('CQ')
    CQK = CQNZ1.CQNZ1(Input).get('CQK')
    PQK = CQNZ1.CQNZ1(Input).get('P0K')

    # print(str(DK)+" = DK\n"+str(DD)+" = DD\n"+str(CQ)+" = CQ\n"+str(CQK)+" = CQK\n"+str(PQK)+" = PQK\n")
    FCQ = FC/CQ
    YI = CQ*prgs.YID(1, G, P0C, FCQ)
    RI = CQ*prgs.RID(G, P0C)
    DA = 0.8*(A[0] - A[1])*(1 - 5*DXF/R[0])
    PS = prgs.PV(G, prgs.VQ(2, G, F[0]))
    WS = prgs.WV(G, prgs.VPC(G, PS))
    DP[0] = 0.5*G*PS*WS**2*prgs.CPS(WS, DA)
    P[0] = PS + DP[0]
    if P[0] >= 1: W[0] = -prgs.WV(G, prgs.VPC(G, 1/P[0]))
    if P[0] < 1: W[0] = prgs.WV(G, prgs.VPC(G, P[0]))
    for i in range(1, 20):
        FS = F[i]*2/(1 + cos(A[i]))
        if i-10 < 0:
            VS = prgs.VQ(2, G, FS)
            WS = prgs.WV(G, VS)
            PS = prgs.PV(G, VS)
            DA = 0.8*(A[i] - A[i+1])*(1 - 5*DXF/R[i])
            # if i == 5 or i == 7 or i == 9: DA = 2.4326109166977814e-15
            # if i == 6 or i == 8: DA = -2.432383796295998e-15
            # if i == 6: DA = 1.2375010576993932e-15
            # if i == 9: DA = -1.2373594212736603e-15
            Z1 = 0.5*G*PS*WS**2*prgs.CPS(WS, DA)
            Z2 = DP[i-1]*exp(-2*(X[i] - X[i-1])/R[i-1])*(1 - WS**2)
            DP[i] = Z1 + Z2
            P[i] = PS + DP[i]
            if P[i] >= 1: W[i] = -prgs.WV(G, prgs.VPC(G, 1/P[0]))
            if P[i] < 1: W[i] = prgs.WV(G, prgs.VPC(G, P[i]))
        elif i-10 == 0:
            PS = (2/(G + 1))**(G/(G - 1))
            DA = (0.65*A[10] - 0.9*A[11])*(1 - 5*DXF/RK)
            Z1 = prgs.PV(G, prgs.VA(G, 1, -DA)) - PS
            Z2 = 0.1*DP[i-1]*exp(-2*(X[i] - X[i-1])/R[i-1])
            DP[i] = Z1 + Z2
            P[i] = PS + DP[i]
            W[i] = prgs.WV(G, prgs.VPC(G, P[i]))
        elif i-10 > 0:
            VS = prgs.VQ(1, G, FS)
            WS = prgs.WV(G, VS)
            PS = prgs.PV(G, VS)
            DA = 0.95*(A[i] - A[i+1])*(1 - 5*DXF/R[i])
            # if i == 14 or i == 15 or i == 19: DA = 8.401097755881618e-16
            # if i == 11 or i == 16: DA = -8.412796870795661e-16
            Z1 = 0.5*G*PS*WS**2*prgs.CPS(WS, DA)
            DXK = (X[i] - X[10])/RK
            Z2 = DP[10]*cos(ZA*DXK)/(1 + 4.3*DXK**0.7 + 16*DXK**3)
            P[i] = PS + Z1 + Z2
            W[i] = prgs.WV(G, prgs.VPC(G, P[i]))
        # print(str(i)+" = i\n"+str(PS)+" = PS\n"+str(Z1)+" = Z1\n"+str(Z2)+" = Z2\n"+str(P[i])+"=P["+str(i)+"]\n"+str(P0D)+" = P0D\n"+str(WS)+"=WS\n"+str(DA)+"=DA\n"+str(A[i])+"=A[i]\n"+str(A[i+1])+"=A[i+1]\n"+str((R[i]-R[i-1])/(X[i]-X[i-1]))+"=(R[i]-R[i-1])/(X[i]-X[i-1])\n")
        # print(str(R[i]-R[i-1])+" = R["+str(i)+"]-R["+str(i-1)+"]\n"+str(R[i])+" = R["+str(i)+"]\n"+str(A[i])+" = A["+str(i)+"]\n"+str(DA)+" = DA["+str(i)+"]\n")
        # print("DA[" + str(i) + "] = " + str(DA))
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
    # print(str(CSP)+"=CSP")
    # CSP = 0.9
    if CSP > 1:
        for i in range(10, 20):
            if XSP >= X[i] and XSP <= X[i+1]:
                SP = SP + (P[i]*R[i] + PS*RSP)*(RSP - R[i]) + (PS1*RSP + P[i+1]*R[i+1])*(R[i+1] - RSP)
                SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i])
            if XSP < X[i] or XSP > X[i+1]:
                SP = SP + (P[i]*R[i] + P[i+1]*R[i+1])*(R[i+1] - R[i])
                SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i])
            if XSP >= X[i+1]:
                # print(str(SD)+"=SD\n"+str(G)+"=G\n"+str(P[i])+"=P["+str(i)+"]\n"+str(W[i])+"=W["+str(i)+"]\n"+str(prgs.CF(TW, G, RE, W[i], DXF))+"=CF(TW, G, RE, W[i], DXF)\n"+str(W[i-1])+"=W["+str(i-1)+"]")
                SD1 = 0.5*G*P[i]
                SD2 = W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)
                SD3 = W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i])
                # print(str(R[i])+"=R[i]\n"+str(R[i+1])+"=R[i+1]\n"+str(X[i])+"=X[i]\n"+str(X[i+1])+"=X[i+1]")
                # print(str(W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i]))+"=W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i])")
                # print(str(W[i-1])+"=W[i-1]")
                SD = SD + SD1*SD2/SD3
                # SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i])
            if XSP > X[i] and XSP <= X[i+1]:
                SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + RSP)*(XSP - X[i])
            DYD = 3.142*SD*P0C/(FK*YI)
            DDK = DD*P0C/YI
            CYK = 1 - 0.15*DK
            DYK = 1 - (CYK*CQ*prgs.YID(1, G, 1, 1/CQ) + 3.142*SP/FK)*P0C/YI
            CY = 1 - DYK - DYD - DDK
            CR = (CY*YI - FC)/RI
            DRH = 1 - (prgs.YID(1, G, P0C, FC) - FC)/prgs.RID(G, P0C)

            answer = {'N': N, 'P': P, 'CQ': CQ, 'XSP': XSP, 'RSP': RSP, 'DYK': DYK, 'DYF': DYD, 'CY': CY, 'DRH': DRH, 'CR': CR}
            return answer
    N = 2
    ZS[20] = CSP
    CS = [0]*21
    for i in range(10):
        M = 19 - i         # CHANGED
        M1 = M + 1
        if W[M] < 1.35: CS[M] = prgs.PNSH(G, prgs.VW(G, W[M]))
        if W[M] >= 1.35: CS[M] = prgs.PSP(W[M], RED)
        DX = (X[20] - X[M])/R[M]
        DAS = A[M]
        ZS[M] = P[M]*P0D*CS[M]*prgs.PSZ(DX, DAS)
        if ZS[M] >= 1:
            # ZS[M1] = 28
            # print(str(ZS[M])+"=ZS[M]\n"+str(ZS[M1])+"=ZS[M1]")
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
                if XSP >= X[i] and XSP <= X[i+1]:
                    SP = SP + (P[i]*R[i] + PS*RSP)*(RSP - R[i]) + (PS1*RSP + P[i+1]*R[i+1])*(R[i+1] - RSP)
                    SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i])
                if XSP < X[i] or XSP > X[i+1]:
                    SP = SP + (P[i]*R[i] + P[i+1]*R[i+1])*(R[i+1] - R[i])
                    SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i])
                if XSP >= X[i+1]: SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i])
                if XSP > X[i] and XSP <= X[i+1]: SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + RSP)*(XSP - X[i])
                DYD = 3.142*SD*P0C/(FK*YI)
                DDK = DD*P0C/YI
                CYK = 1 - 0.15*DK
                DYK = 1 - (CYK*CQ*prgs.YID(1, G, 1, 1/CQ) + 3.142*SP/FK)*P0C/YI
                CY = 1 - DYK - DYD - DDK
                CR = (CY*YI - FC)/RI
                DRH = 1 - (prgs.YID(1, G, P0C, FC) - FC)/prgs.RID(G, P0C)

                answer = {'N': N, 'P': P, 'CQ': CQ, 'XSP': XSP, 'RSP': RSP, 'DYK': DYK, 'DYF': DYD, 'CY': CY, 'DRH': DRH, 'CR': CR}
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
        if XSP >= X[i] and XSP <= X[i+1]:
            SP = SP + (P[i]*R[i] + PS*RSP)*(RSP - R[i]) + (PS1*RSP + P[i+1]*R[i+1])*(R[i+1] - RSP)
            SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i])
        if XSP < X[i] or XSP > X[i+1]:
            SP = SP + (P[i]*R[i] + P[i+1]*R[i+1])*(R[i+1] - R[i])
            SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i])
        if XSP >= X[i+1]: SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + R[i+1])*(X[i+1] - X[i])
        if XSP > X[i] and XSP <= X[i+1]: SD = SD + 0.5*G*P[i]*W[i]**4*prgs.CF(TW, G, RE, W[i], DXF)/W[i-1]**2*2/(R[i] + RSP)*(XSP - X[i])
        DYD = 3.142*SD*P0C/(FK*YI)
        DDK = DD*P0C/YI
        CYK = 1 - 0.15*DK
        DYK = 1 - (CYK*CQ*prgs.YID(1, G, 1, 1/CQ) + 3.142*SP/FK)*P0C/YI
        CY = 1 - DYK - DYD - DDK
        CR = (CY*YI - FC)/RI
        DRH = 1 - (prgs.YID(1, G, P0C, FC) - FC)/prgs.RID(G, P0C)

    answer = {'N': N, 'P': P, 'CQ': CQ, 'XSP': XSP, 'RSP': RSP, 'DYK': DYK, 'DYF': DYD, 'CY': CY, 'DRH': DRH, 'CR': CR}
    return answer

    # P_mid = [0]*4
    # P_mid[0] = [1.8, 2.2, 2.3, 2.8, 3.2, 3.5, 5]
    # P_mid[1] = [1.8, 2.1, 2.6, 3.1, 4.3, 5.1, 8]
    # P_mid[2] = [2.0, 2.3, 2.6, 3.1, 4.3, 6.9, 10]
    # P_mid[3] = [2.0, 2.6, 3.3, 3.9, 4.8, 6.1, 7.8]
    # Number = 3
    # P_mid = P_mid[Number]
    # print("Example = "+str(Number+1))
    # print("P[0] = "+str(P_mid))
    # for i in range(7):
    #     answer1 = RQLN11(P_mid[i])
    #     print("P["+str(i+1)+"] = "+str(answer1.get('P'))+" # P_mid = "+str(P_mid[i]))
    #
    # return answer1
