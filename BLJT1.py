from math import *
import PROGRAMS as prgs
import TBLS, VBLS

def BLJT1(ANS):
    RC = float(ANS['RA'])
    VC = float(ANS['VA'])
    DC = float(ANS['DA'])
    GC = float(ANS['GC'])
    CPC = float(ANS['CPC'])
    CT = float(ANS['CT'])
    T0 = float(ANS['T0'])
    U2 = float(ANS['U2'])
    G2 = float(ANS['G2'])
    CP2 = float(ANS['CP2'])
    VS = float(ANS['VJ'])
    RS = float(ANS['RJ'])
    CB = float(ANS['CB'])
    XS = float(ANS['XJ'])

    R = [0]*50
    Y = [0]*50
    F = [0]*7
    FW = [0]*7
    Q = [0]*50

    # Словарь для TBLS
    def GI(Y):
        Input = {'T0': GC/G2, 'XD': XS, 'Y': Y}
        GI = G2*TBLS.TBLS(Input).get('TBLS')
        return GI

    def CPI(Y):
        # Словарь для TBLS
        Input = {'T0': CPC/CP2, 'XD': XS, 'Y': Y}
        CPI = CP2*TBLS.TBLS(Input).get('TBLS')
        return CPI

    def VI(Y):
        # Словарь для VBLS
        Input = {'CU': CB, 'YS': Y0, 'Y': Y}
        VI = VS*(U2 - (U2 - 1)*VBLS.VBLS(Input).get('VBLS'))
        return VI

    def QI(Y):
        # Словарь для TBLS
        Input = {'T0': T0, 'XD': XS, 'Y': Y}
        QI = prgs.QID(GI(Y), RG, TBLS.TBLS(Input).get('TBLS'))*prgs.YV(GI(Y), VI(Y))
        return QI

    RG = 287.3
    F2 = 0
    CH = RS/RC
    XD = XS/DC
    Z1 = 0.25*XD
    Z2 = 0.11*(1 + 0.64*Z1**2)/(1 + Z1**2)
    Z3 = Z1**2/(1 + Z1**2)
    Z4 = (1 + 0.01*Z1**2)/(1 + 0.005*Z1**2)
    Z5 = (1 - U2)/(1 + (U2 + 2*abs(U2))/3)
    Z6 = (0.8 + 0.2*CH)/(0.3*prgs.TV(GC, VS) + 0.4*Z1*sqrt(CH))
    Z7 = 0.048 + 0.3*CT
    Z8 = 0.065 + 0.42*CT
    Z9 = 0.115*(DC*(2*RC - DC))/prgs.TV(GC, VC)
    R1 = RS - DC - prgs.TV(GC, VS)*Z3*Z4*Z5*Z7*XS
    R3 = RS + (1 + 0.4*prgs.TV(GC, VS)*sqrt(CH)*Z1)*Z4*Z5*Z6*Z8*XS
    DS = R3 - R1
    Y0 = (R3 - RS)/DS
    R[0] = R1
    Q[0] = QI(0)
    FS = RS**2 - R1**2
    CQ = prgs.QID(GC, RG, T0)*(FS*prgs.YV(GC, VS) - Z9*prgs.YV(GC, VS*(1 - U2)))
    for i in range(1, 50):
        R[i] = R1 + 0.02*DS*i                                                       # CHANGED
        R2 = 0.5*(R[i-1] + R[i])
        Y[i] = abs((R3 - R[i])/DS)
        Q[i] = QI(Y[i])
        F2 = F2 + 0.5*(Q[i-1] + Q[i])*(R[i]**2 - R[i-1]**2)
        if F2 >= CQ:
            for i in range(7):
                R[i] = sqrt(R3**2 - 0.1667*(R3**2 - R2**2)*(i))                     # CHANGED
                Y[i] = abs((R3 - R[i])/DS)
                F[i] = QI(Y[i])

                # Словарь для TBLS
                Input = {'T0': T0, 'XD': XD, 'Y': Y[i]}
                FW[i] = F[i]*(CPI(Y[i])*TBLS.TBLS(Input).get('TBLS') - CP2)
            S = F[0] + F[6] + 2*(F[2] + F[4]) + 4*(F[1] + F[3] + F[5])
            SW = FW[0] + FW[6] + 2*(FW[2] + FW[4]) + 4*(FW[1] + FW[3] + FW[5])
            ZQ = prgs.QID(GC, RG, T0)*prgs.YV(GC, VS)*(R3**2 - R1**2)
            CQS = (0.0555*S - QI(0))*(R3**2 - R2**2)/ZQ
            CWS = 0.0555*SW*(R3**2 - R2**2)/(CPC*ZQ*T0)
            Y2 = (R3 - R2)/DS
            Y21 = Y2 + 0.02
            Y22 = Y2 - 0.02
            DV = 25*(VBLS.VBLS({'CU': CB, 'YS': Y0, 'Y': Y21}).get('VBLS') - VBLS.VBLS({'CU': CB, 'YS': Y0, 'Y': Y22}).get('VBLS'))
            CF2 = 2*(Z2*(1 - U2)*DV)**2
            CF2 = 0.0025 + (CF2 - 0.0025)*XD**2/(1 + XD**2)

            answer = {'R1': R1, 'R2': R2, 'R3': R3, 'CQJ': CQS, 'CWJ': CWS, 'CF2': CF2}
            return answer


    for i in range(7):
        R[i] = sqrt(R3**2 - 0.1667*(R3**2 - R2**2)*(i))                     # CHANGED
        Y[i] = abs((R3 - R[i])/DS)
        F[i] = QI[Y[i]]

        # Словарь для TBLS
        Input = {'T0': T0, 'XD': XD, 'Y': Y[i]}
        FW[i] = F[i]*(CPI[Y[i]]*TBLS.TBLS(Input).get('TBLS') - CP2)
    S = F[0] + F[6] + 2*(F[2] + F[4]) + 4*(F[1] + F[3] + F[5])
    SW = FW[0] + FW[6] + 2*(FW[2] + FW[4]) + 4*(FW[1] + FW[3] + FW[5])
    ZQ = prgs.QID(GC, RG, T0)*prgs.YV(GC, VS)*(R3**2 - R1**2)
    CQS = (0.0555*S - QI[0])*(R3**2 - R2**2)/ZQ
    CWS = 0.0555*SW*(R3**2 - R2**2)/(CPC*ZQ*T0)
    Y2 = (R3 - R2)/DS
    Y21 = Y2 + 0.02
    Y22 = Y2 - 0.02
    DV = 25*(VBLS.VBLS({'CU': CB, 'YS': Y0, 'Y': Y21}).get('VBLS') - VBLS.VBLS({'CU': CB, 'YS': Y0, 'Y': Y22}).get('VBLS'))
    CF2 = 2*(Z2*(1 - U2)*DV)**2
    CF2 = 0.0025 + (CF2 - 0.0025)*XD**2/(1 + XD**2)

    answer = {'R1': R1, 'R2': R2, 'R3': R3, 'CQJ': CQS, 'CWJ': CWS, 'CF2': CF2}
    return answer
