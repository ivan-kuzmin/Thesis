from math import *
import PROGRAMS as prgs
import RXJT1
import BLJT1

def DCXCS(ANS):
    CC = [0]*3
    XC= [0]*2
    RC = [0]*3
    for i in range(3):
        CC[i] = float(ANS['CC'].split(',')[i])
        RC[i] = float(ANS['RC'].split(',')[i])
    for i in range(2):
        XC[i] = float(ANS['XC'].split(',')[i])
    FM = float(ANS['FM'])
    FK = float(ANS['FK'])
    FN = float(ANS['FN'])
    AN = float(ANS['AN'])
    GJ = float(ANS['GC'])
    WH = float(ANS['WH'])
    P0C = float(ANS['P0C'])
    PD0 = float(ANS['PD0'])
    PDJ = float(ANS['PDJ'])

    G = 1.4
    CV = 0.14
    CT = 0.035
    CP = 1000
    RN = 0.5642*sqrt(FN)
    RK = 0.5642*sqrt(FK)
    VN = prgs.VQ(1, GJ, FN/FK)
    PDS = PDJ
    DN = 0.1*RN
    RJ = [0]*2
    R3 = [0]*2
    CF = [0]*2
    for j in range(0, 2):
        P0D = P0C/PDS
        VJ = prgs.VP(GJ, P0D)
        WJ = prgs.WV(GJ, VJ)
        for i in range(0, 2):

            # Словарь для RXJT1
            Input = {'RA': RN, 'AA': AN, 'GC': GJ, 'VA': VN, 'P0C': P0D, 'XJ': XC[i]}
            RXJT1.RXJT1(Input)
            RJ[i] = RXJT1.RXJT1(Input).get('RJ')
            AJ = RXJT1.RXJT1(Input).get('AJ')

            # Словарь для BLJT1
            Input = {'RA': RN, 'VA': VN, 'DA': DN, 'GC': GJ, 'CPC': CP, 'CB': CV, 'CT': CT, 'T0': 1, 'U2': 0, 'G2': G, 'CP2': CP, 'VJ': VJ, 'XJ': XC[i], 'RJ': RJ[i]}
            BLJT1.BLJT1(Input)
            R1 = BLJT1.BLJT1(Input).get('R1')
            R2 = BLJT1.BLJT1(Input).get('R2')
            R3[i] = BLJT1.BLJT1(Input).get('R3')
            CQ = BLJT1.BLJT1(Input).get('CQJ')
            CW = BLJT1.BLJT1(Input).get('CWJ')
            CF[i] = BLJT1.BLJT1(Input).get('CF2')

        if R3[0] >= RC[1] or R3[1] >= RC[2]:
            FC3 = (RC[2]/RK)**2
            PC3 = P0C*prgs.PV(GJ, prgs.VQ(1, GJ, FC3))
            FC2 = (RC[1]/RK)**2
            PC2 = P0C*prgs.PV(GJ, prgs.VQ(1, GJ, FC2))
            A1 = atan((RC[1] - RN)/XC[0]) - AN
            PC1 = P0C*prgs.PV(GJ, prgs.VA(GJ, VN, A1))
        else:
            PC3 = PDJ
            S2 = pi*(CC[1]*RJ[0] + CC[2]*RJ[1])*(XC[1] - XC[0])
            F2 = (RC[1] - RJ[0] + RC[2] - RJ[1])*(XC[1] - XC[0]) + pi*CC[2]*(RC[2]**2 - RJ[1]**2)
            PC2 = PC3*(1 - 0.5*GJ*WJ**2*CF[1]*S2/F2)
            S1 = pi*(CC[0]*RN + CC[1]*RJ[0])*XC[0]
            F1 = (RC[0] - RN + RC[1] - RJ[0])*XC[0] + pi*CC[1]*(RC[1]**2 - RJ[0]**2)
            PC1 = PC2*(1 - 0.5*GJ*WJ**2*CF[0]*S1/F1)
            PDS = 0.333*(PC1 + PC2 + PC3)

        PF1 = pi*CC[0]*(RC[0]**2 - RN**2)*(PD0 - PC1)
        PF2 = pi*(CC[0]*RC[0] + CC[1]*RC[1])*(RC[1] - RC[0])*(PD0 - 0.5*(PC1 + PC2))
        PF3 = pi*(CC[1]*RC[1] + CC[2]*RC[2])*(RC[2] - RC[1])*(PD0 - 0.5*(PC2 + PC3))
        DCXCS = 1.43*(PF1 + PF2 + PF3)/(FM*WH**2)

        answer = {'DCXCS': DCXCS}
        return answer
