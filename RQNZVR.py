from math import *
import PROGRAMS as prgs

def RQNZVR(ANS):
    N = int(ANS['N'])
    DF = float(ANS['DF'])
    P0 = float(ANS['P0'])
    T0 = float(ANS['T0'])
    G = float(ANS['G'])
    B = float(ANS['B'])
    CP = float(ANS['CP'])
    DF = [0]*N
    P0 = [0]*N
    T0 = [0]*N
    G = [0]*N
    B = [0]*N
    CP = [0]*N
    for i in range(N):
        DF[i] = float(ANS['DF'].split(',')[i])
        P0[i] = float(ANS['P0'].split(',')[i])
        T0[i] = float(ANS['T0'].split(',')[i])
        G[i] = float(ANS['G'].split(',')[i])
        B[i] = float(ANS['B'].split(',')[i])
        CP[i] = float(ANS['CP'].split(',')[i])
    PF = float(ANS['PF'])
    PH = float(ANS['PH'])

    F = [0]*25
    P = [0]*25
    P0F = [0]*25

    def FG(G):
        FG = G*(2/(G + 1))**(G/(G - 1))                            # CHANGED
        return FG

    QC = 0
    EC = 0
    RI = 0
    FCI = 0
    FF = 0
    CS = 0
    BS = 0
    CPS = 0
    for i in range(N):
        FF = FF + DF[i]
        P0F[i] = P0[i]/PF
        P0C = P0[i]/PH
        GC = G[i]
        U = prgs.UK(GC, B[i], T0[i])
        VF = prgs.VP(GC, P0F[i])
        YVF = prgs.YV(GC, VF)
        VC = prgs.VP(GC, P0C)
        YVC = prgs.YV(GC, VC)
        DQ = FG(GC)*PF*DF[i]*YVF/U
        DFC = prgs.DFI(DF[i], GC, P0F[i], P0C)*PF/PH
        QC = QC + DQ
        EC = EC + CP[i]*T0[i]*DQ
        GS = GS + GC*DQ
        BS = BS + B[i]*DQ
        CPS = CPS + CP[i]*DQ
        FCI = FCI + DFC
        RI = RI + GC*PH*prgs.WV(GC, VC)**2*DFC
    GS = GS/QC
    BS = BS/QC
    CPS = CPS/QC
    T0S = EC/(CPS*QC)
    YC = RI + FCI*PH
    Z1 = FG[GS]
    Z2 = (0.5*(GS + 1))**(1/(GS - 1))
    Z3 = (GS - 1)/(GS + 1)
    YS = QC*prgs.UK(GS, BS, T0S)/(Z1*FF*PF)
    VS = prgs.VY(GS, YS)
    P0S = PF/prgs.PV(GC, VS)
    FKS = FF*prgs.QV(GS, VS)
    P0CS = P0S/PH
    RIS = PH*FKS*prgs.RID(GS, P0CS)
    CY = (RIS + FCI*PH)/YC
    CR = RIS/RI
    CRC = 1
    F[0] = FF
    P[0] = PF
    C = 1
    for j in range(1, 25):
        M = j
        P[j] = PF - 0.04*C*(PF - PH)*j                                        # CHANGED
        FI = 0
        for i in range(N):
            P0I = P0[i]/P[j]
            FI = FI + prgs.DFI(DF[i], G[i], P0F[i], P0I)*PF/P[j]
        F[j] = FI
        if F[1] > FF and C == 1: C = -1
        A = C*(F[j] - F[j-1])
        if A >= 0:
            F[0] = F[M - 1]                                                   # CHANGED
            P[0] = P[M - 1]                                                   # CHANGED
            for j in range(1, 25):
                P[j] = P[0] - 0.04*C*(P[0] - P[M])*J                          # CHANGED
                FI = 0
                for i in range(N):
                    P0I = P0[i]/P[j]
                    FI = FI + prgs.DFI(DF[i], G[i], P0F[i], P0I)*PF/P[j]
                F[j] = FI
                FK = F[j-1]
                PK = P[j-1]
                A = C*(F[j] - F[j-1])
                if A >= 0:
                    break
                break
        FK = FCI
        PK = PH
    CQ = FKS/FK
    if FC == 0: FC = FCI
    if FC < FK: print("FC задано меньше FK")
    FCK = FC/FK
    VCC = prgs.VQ(1, GS, FCK)
    PCS = prgs.PV(GS, VCC)
    D = 1
    for l in range(2):
        for j in range(20):
            P[j] = PCS*(1.2 - 0.2*D*j)                                         # CHANGED
            FI = 0
            for i in range(N):
                P0I = P0[i]/P[j]
                FI = FI + prgs.DFI(DF[i], G[i], P0F[i], P0I)*PF/P[j]
            F[j] = FI
            PC = P[j]
            if F[j] - FC > 0:
                continue
            if F[j] - FC == 0:
                for i in range(N):
                    P0I = P0[i]/PC
                    VC = prgs.VP(G[i], P0I)
                    DR = PC*(G[i]*prgs.WV(G[i], VC)**2 + 1) - PH
                    FI = FI + DR*prgs.DFI(DF[i], G[i], P0F[i], P0I)*PF/PC
                    CRC = FI/RI
                    answer = {'FF': FF, 'FK': FK, 'FC': FC, 'PK': PK, 'PC': PC, 'QC': QC, 'EC': EC, 'YC': YC, 'RI': RI, 'P0S': P0S, 'T0S': T0S, 'GS': GS, 'BC': BC, 'CPS': CPS, 'CQ': CQ, 'CY': CY, 'CR': CR, 'CRC': CRC}
                    return
            if F[j] - FC > 0:
                PCS = PC
                D = 1
                break
        PCS = PC
        D = 1
    FI = 0
    for i in range(N):
        P0I = P0[i]/PC
        VC = prgs.VP(G[i], P0I)
        DR = PC*(G[i]*prgs.WV(G[i], VC)**2 + 1) - PH
        FI = FI + DR*prgs.DFI(DF[i], G[i], P0F[i], P0I)*PF/PC
    CRC = FI/RI
    answer = {'FF': FF, 'FK': FK, 'FC': FC, 'PK': PK, 'PC': PC, 'QC': QC, 'EC': EC, 'YC': YC, 'RI': RI, 'P0S': P0S, 'T0S': T0S, 'GS': GS, 'BC': BC, 'CPS': CPS, 'CQ': CQ, 'CY': CY, 'CR': CR, 'CRC': CRC}
    return
