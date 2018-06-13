from math import *
import PROGRAMS as prgs

def RQLNSQ(ANS):
    N = int(ANS['N'])
    RFK = float(ANS['RFK'])
    # VF = float(ANS['VF'])
    VF = [0]*N
    AB = [0]*N
    for i in range(N):
        VF[i] = float(ANS['VF'].split(',')[i])
        AB[i] = float(ANS['AB'].split(',')[i])

    PSI = [0]*20
    AAM = [0]*20
    R = [0]*20
    UB = [0]*20
    F = [0]*20

    N1 = N - 1
    DR = 1/N1
    for i in range(N):
        R[i] = i*DR                                  # CHANGED
        AAM[i] = VF[i]*sin(AB[i])*R[i]*RFK
    PSI[0] = 0
    for M in range(1, N):
        PSI[M] = PSI[M-1] + 0.5*DR*(cos(AB[M])*R[M] + cos(AB[M-1])*R[M-1])
    for M1 in range(1, N):
        PSI[M1] = PSI[M1]/PSI[N-1]                     # CHANGED
    F[N] = 0
    for J in range(1, N):
        S = 0
        for K in range(J, N1):
            S = S + 0.5*(PSI[K+1] - PSI[K])*((AAM[K+1]/PSI[K+1])**2 + (AAM[K]/PSI[K])**2)
        F[J] = S
    F[0] = F[1] + AAM[1]**2/PSI[1]
    S = 0
    for J in range(N1):
        S = S + 0.5*(PSI[J+1] - PSI[J])*(F[J+1] + F[J])
    EPS = S
    QC = 0.5*EPS
    CQ = 1 - QC
    CY = 1 - 0.1*QC

    answer = {'EPS': round(EPS, 4), 'CQ': round(CQ, 4), 'CY': round(CY, 4)}
    return answer
