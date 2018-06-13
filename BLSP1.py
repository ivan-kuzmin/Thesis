from math import *
import PROGRAMS as prgs
import TBLS, VBLS

def BLSP1(ANS):
    RN = float(ANS['RSP'])
    VS = float(ANS['VS'])
    DN = float(ANS['DS'])
    CV = float(ANS['CB'])
    CT = float(ANS['CT'])
    U2 = float(ANS['U2'])
    T0 = float(ANS['T0'])
    XS = float(ANS['XS'])
    RS = float(ANS['RS'])

    R = [0]*50
    Y = [0]*50
    F = [0]*7
    FW = [0]*7
    Q = [0]*50

    def VI(Y):
        # Словарь для VBLS
        Input = {'CU': CV, 'YS': Y0, 'Y': Y}
        VI = VS*(U2 - (U2 - 1)*VBLS.VBLS(Input).get('VBLS'))
        return VI

    def QI(Y):
        # Словарь для TBLS
        Input = {'T0': T0, 'XD': XD, 'Y': Y}
        QI = prgs.QID(G, RG, TBLS.TBLS(Input).get('TBLS'))*prgs.YV(G, VI(Y))
        return QI

    G = 1.4
    RG = 287.3
    F2 = 0
    XD = XS/DN
    Z1 = 0.25*XD
    Z2 = 0.11*(1 + 0.64*Z1**2)/(1 + Z1**2)
    Z3 = Z1**2/(1 + Z1**2)
    Z4 = (1 + 0.01*Z1**2)/(1 + 0.005*Z1**2)
    Z5 = (1 - U2)/(1 + (U2 + 2*abs(U2))/3)
    Z6 = (0.8 + 0.2*RN/RS)/(0.3*prgs.TV(G, VS) + 0.4*Z1)
    Z7 = 0.048 + 0.3*CT
    Z8 = 0.065 + 0.42*CT
    Z9 = 0.115*(DN*(2*RN + DN))/prgs.TV(G, VS)
    R1 = RS + DN + prgs.TV(G, VS)*Z3*Z4*Z5*Z7*XS
    R3 = RS - (1 + 0.4*prgs.TV(G, VS)*Z1)*Z4*Z5*Z6*Z8*XS
    DS = R1 - R3
    Y0 = (RS - R3)/DS
    R[0] = R1
    Q[0] = QI(1)
    FS = R1**2 - RS**2
    CQ = prgs.QID(G, RG, T0)*(FS*prgs.YV(G, VS) - Z9*prgs.YV(G, VS*(1 - U2)))
    for i in range(1, 50):
        R[i] = R1 - 0.02*DS*i                                     # CHANGED
        R2 = 0.5*(R[i-1] + R[i])
        Y[i] = abs((R[i] - R3)/DS)
        Q[i] = QI(Y[i])
        F2 = F2 + 0.5*(Q[i-1] + Q[i])*(R[i-1]**2 - R[i]**2)
        if F2 >= CQ:
            break
    for j in range(7):
        R[j] = sqrt(0.1667*(R2**2 - R3**2)*i + R3**2)                 # CHANGED
        Y[j] = abs((R[j] - R3)/DS)
        F[j] = QI(Y[j])

        # Словарь для TBLS
        Input = {'T0': T0, 'XD': XD, 'Y': Y[j]}
        F[j] = F[j]*(TBLS.TBLS(Input).get('TBLS') - 1)
    S = F[0] + F[6] + 2*(F[2] + F[4]) + 4*(F[1] + F[3] + F[5])
    SW = FW[0] + FW[6] + 2*(FW[2] + FW[4]) + 4*(FW[1] + FW[3] + FW[5])
    ZQ = prgs.QID(G, RG, T0)*prgs.YV(G, VS)*(R1**2 - R3**2)
    CQS = (0.0555*S - QI(0))*(R2**2 - R3**2)/ZQ
    CWS = 0.0555*SW*(R2**2 - R3**2)/(ZQ*T0)
    Y2 = (R2 - R3)/DS
    Y21 = Y2 + 0.01
    Y22 = Y2 - 0.01

    # Словарь для VBLS
    DV = 50*(VBLS.VBLS({'CU': CV, 'YS': Y0, 'Y': Y21}).get('VBLS') - VBLS.VBLS({'CU': CV, 'YS': Y0, 'Y': Y22}).get('VBLS'))
    CF2 = 2*(Z2*(1 - U2)*DV)**2

    answer = {'R1': R1,'R2': R2,'R3': R3,'CQS': CQS,'CWS': CWS,'CF2': CF2}
    return answer
