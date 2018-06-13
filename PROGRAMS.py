from math import *

# #### Подпрограмма UA:
def UA(G, B, T):
    UA = sqrt(G*B*T)
    return UA

# #### Подпрограмма UK:
def UK(G, B, TO):
    UK = sqrt(2*G/(G + 1)*B*TO)
    return UK

# #### Подпрограмма PV:
def PV(G, V):
    PV = (1 - (G - 1)/(G + 1)*V**2)**(G/(G - 1))
    return PV

# #### Подпрограмма TV:
def TV(G, V):
    TV = 1 - (G - 1)/(G + 1)*V**2
    return TV

# #### Подпрограмма EV:
def EV(G, V):
    EV = (1 - (G - 1)/(G + 1)*V*V)**(1/(G - 1))
    return EV

# #### Подпрограмма WV:
def WV(G, V):
    WV = sqrt(2/(G + 1)*V**2/(1 - (G - 1)/(G + 1)*V**2))
    return WV

# #### Подпрограмма QV:
def QV(G, V):
    TV = 1 - (G - 1)/(G + 1)*V*V
    QV = (0.5*(G + 1))**(1/(G - 1))*V*TV**(1/(G - 1))
    return QV

# #### Подпрограмма YV:
def YV(G, V):
    TV = 1 - (G - 1)/(G + 1)*V*V
    YV = (0.5*(G + 1))**(1/(G - 1))*V/TV
    return YV

# #### Подпрограмма ZV:
def ZV(V):
    ZV = V + 1/V
    return ZV

# #### Подпрограмма VW:
def VW(G, W):
    VW = sqrt((G + 1)/2*W**2/(1 + (G - 1)/2*W**2))
    return VW

# #### Подпрограмма VP:
def VP(G, PO):
    VP = sqrt((G + 1)/(G - 1)*(1 - PO**((1 - G)/G)))
    return VP

# #### Подпрограмма VPC:
def VPC(G, P):
    VPC = sqrt((G + 1)/(G - 1)*(1 - P**((G - 1)/G)))
    return VPC

# #### Подпрограмма VPP:
def VPP(G, V, P):
    Z = 1 - P**((G - 1)/G)*(1 - (G - 1)/(G + 1)*V*V)
    if Z >= 0: VPP = sqrt(Z*(G + 1)/(G - 1))
    if Z < 0: VPP = sqrt(-Z*(G + 1)/(G - 1))
    return VPP

# #### Подпрограмма VQ:
def VQ(I, G, F):
    V = [0]*20
    Z1 = 0.5*(G + 1)
    Z2 = 0.5*(G - 1)
    Z3 = 0.5/Z2
    Z4 = G - 1
    if F <= 1:
        VQ = 1
        return VQ
    DF = F - 1
    if DF >= 0.01:
        if I == 1:
            V[0] = 1.1
            for j in range(1, 20):
                V[j] = sqrt((Z1 - (1/(V[j-1]*F))**Z4)/Z2)
            VQ = V[19]
            return VQ
        V[0] = 0.99
        for j in range(1,20):
            V[j] = 1/(F*(Z1 - Z2*V[j-1]**2)**Z3)
        VQ = V[19]
        return VQ
    if DF < 0.01 and I == 1:
        VQ = 1 + 0.93*sqrt(DF)
    if DF < 0.01 and I != 1:
        VQ = 1 - 0.93*sqrt(DF)
    return VQ

# #### Подпрограмма VY:
def VY(G, Y):
    Z1 = (G - 1)/(G + 1)
    Z2 = (0.5*(G + 1))**(1/(G - 1))
    B = abs(Y)
    if B < 0.2: VY = Y/Z2
    if B >= 0.2: VY = (sqrt(Z2**2 + 4*Z1*Y**2) - Z2)/(2*Z1*Y)
    return VY

# #### Подпрограмма DFI:
def DFI(DF, G, P0, PI):
    VF = VP(G, P0)
    V = VP(G, PI)
    DFI = DF*YV(G, VF)/YV(G, V)
    return DFI

# #### Подпрограмма AV:
def AV(G, V):
    Z = sqrt((G - 1)/(G + 1))
    ZW = sqrt(abs(WV(G, V)**2 - 1))
    AV = atan(Z*ZW)/Z - atan(ZW)
    return AV

# #### Подпрограмма VA:
def VA(G, V, A):
    VI = [0]*100
    DA = [0]*100
    A1 = A + AV(G, V)
    if A1 >= 0:
        if A1 > 0.0001:
            VI[0] = 1
            DA[0] = 0
            for i in range(1, 100):
                K = i
                VI[i] = 1 + 0.025*(i - 1)
                DA[i] = A1 - AV(G, VI[i])
                if DA[i] != 0:
                    Z = 0.5*(1 + (DA[K-1] + DA[K])/(DA[K-1] - DA[K]))
                    VA = VI[K-1] + (VI[K] - VI[K-1])*Z
                elif DA[i] == 0:
                    VA = VI[K]
                return VA
        else:
            VA = V
            return VA
    else:
        print("Отрицательный угол А больше предельного!")
        return 0

# #### Подпрограмма P0NSH:
def P0NSH(G, V):
    P0NSH = V*V*(TV(G, V)/TV(G, 1/V))**(1/(G - 1))
    return P0NSH

# #### Подпрограмма PNSH:
def PNSH(G, V):
    TV = 1 - (G - 1)/(G + 1)*V*V
    PNSH = (V*V - (G - 1)/(G + 1))/TV
    return PNSH

# #### Подпрограмма P0NSH:
def P0NSH(G, V):
    P0NSH = V*V*(TV(G, V)/TV(G, 1/V))**(1/(G - 1))
    return P0NSH

# #### Подпрограмма ASH:
def ASH(G, V, A):
    D = [0]*25
    A1 = [0]*25
    Z = (G - 1)/(G + 1)
    V2 = V*V
    A0 = asin(sqrt(1 - 0.5*(G + 1)*(1 - 1/V2)))
    A1[0] = A0
    Z1 = (1 - Z*V2*cos(A0)**2)/(V2*sin(A0)**2)
    D[0] = tan(A0)*Z1 - tan(A0 - A)
    for i in range(1, 25):
        K = i
        A1[i] = A0 + 0.02*i                          # CHANGED
        ZI = (1 - Z*V2*cos(A1[i])**2)/(V2*sin(A1[i])**2)
        D[i] = tan(A1[i])*ZI - tan(A1[i] - A)
        if D[i] <= 0:
            break
    ASH = A1[K-1] - (A1[K-1] - A1[K])*D[K-1]/(D[K-1] - D[K])
    return ASH

# #### Подпрограмма VASH:
def VASH(G, V, A):
    Z = (G - 1)/(G + 1)
    A2 = ASH(G, V, A)
    V2 = V*V
    Z1 = (1 - Z*V2*cos(A2)**2)**2/(V2*sin(A2)**2)
    VASH = sqrt(V2*cos(A2)**2 + Z1)
    return VASH

# #### Подпрограмма PASH:
def PASH(G, V, A):
    Z = (G - 1)/(G + 1)
    A2 = ASH(G, V, A)
    V2 = V*V
    PASH = (V2*(1 - G*(2*cos(A2)/(G + 1))**2) - Z)/TV(G, V)
    return PASH

# #### Подпрограмма P0ASH:
def P0ASH(G, V, A):
    V1 = VASH(G, V, A)
    P0ASH = PV(G, V)*PASH(G, V, A)/PV(G, V1)
    return P0ASH

# #### Подпрограмма QID:
def QID(G, B, TO):
    QID = G*(2/(G + 1))**(G/(G - 1))/UK(G, B, TO)
    return QID

# #### Подпрограмма YID:
def YID(I, G, P0, F):
    ZY = (2/(G + 1))**(1/(G - 1))
    if I == 1: YID = ZY*P0*ZV(VQ(I, G, F))
    if I != 1: YID = ZY*P0*ZV(VQ(I, G, F))*QV(G, VQ(I, G, F))
    return YID

# #### Подпрограмма RID:
def RID(G, P0):
    P0K = ((G + 1)/2)**(G/(G - 1))
    ZR = G/P0K
    if P0 >= P0K: RID = ZR*P0*VP(G, P0)
    if P0 < P0K: RID = ZR*P0*VP(G, P0)*QV(G, VP(G, P0))
    return RID

# #### Подпрограмма AAD:
def AAD(W, U, D, A, F):
    ZQ = 1 - U
    if ZQ < 0: ZQ = 0
    ZD = 0.12*D**0.5
    ZF = 1 + 0.5*F**1.5
    ZW = 0.11 + 0.325*(W - 1)/W**0.5
    AAD = (ZW - ZD - 0.5*A)*ZQ/ZF
    return AAD

# #### Подпрограмма ADP:
def ADP(W, P):
    DP = [0]*20
    A = [0]*20
    C = 1
    if P - 1 < 0: C = -1
    if P - 1 == 0:
        ADP = 0
        return ADP
    if P - 1 > 0:
        for l in range(20):
            K = l
            A[l] = 0.050*C*l                                     # CHANGED
            DP[l] = (P - 1 - 0.7*W**2*CPS(W, A[l]))*C
            if DP[l] <= 0:
                ADP = A[K-1] - (A[K-1] - A[K])*DP[K-1]/(DP[K-1] - DP[K])
                return ADP
            print("Значение P вне области функции ADP")
    return ADP

# #### Подпрограмма CF:
def CF(TW, G, RE, W, DX):
    Z1 = (1 + (G - 1)/2*W**2)**((G + 1)/(8*(G - 1)) - 0.51)
    Z2 = (1 + 0.448*(G - 1)*W**2)**0.353*(0.777*RE*W*DX)**0.25
    CF = 0.0258*(2/(G - 1))**0.125/TW**0.51*Z1/Z2
    return CF

# #### Подпрограмма CPA:
def CPA(W, A):
    Z = 2.4*A
    Z2 = 1 + Z**5/(1 + Z**6)
    if W >= 0.7:
        if W >= 1.5:
            Z3 = 1 + (0.6*W**4/(W*W - 1) - 1)*A/sqrt(W*W - 1)
            CPA = 2*Z3*A/sqrt(W*W - 1)
        else:
            Z1 = 30*((0.9/(1 + 0.2*Z*Z) - W)**2*W + 2.5*Z**6)
            Z4 = 2.236*(W - 0.7)*(1 + 1.279*A)
            Z5 = 3.5*(1.5 - W)*Z2
            Z6 = 20*(W - 7)*(1.5 - W)*exp(-Z1)
            CPA = (Z4 + Z5 + Z6)*A
    else:
        CPA = 2*Z2*A/sqrt(1 - W**2)
    return CPA

# #### Подпрограмма CPS:
def CPS(W, A):
    if W <= 1: DPP = 1/(1 - 0.2*W**2/(1 + 0.2*W**2))**3.5 - 1
    if W > 1 and W <= 1.35: DPP = 0.89
    if W > 1.35: DPP = 0.45 + 0.32*(W + 0.01*W**4)
    DPD = (1 - 0.52*W + 0.085*W*W)/(1 + 0.0024*W**5) + 0.35*W**1.5*exp(-2*W**2) - 1
    ZP = 1.43*DPP/W**2
    ZD = 1.43*DPD/W**2
    if W <= 0.7: CP = 2/sqrt(1 - W*W)
    if W > 0.7 and W <= 1.3: CP = 3.67*(W - 0.7) + 4.67*(1.3 - W) + 40*(W - 0.7)*(1.3 - W)*exp(-30*(W - 0.9)**2*W)
    if W > 1.3: CP = 2/sqrt(W*W - 1)
    if A < 0: AK = ZD/CP
    if A >= 0: AK = ZP/CP
    ZA = 0.1*exp(-10*abs(A - AK))*2.5*A
    if A <= 0:
        if A > AK: CPS = CP*A - ZA
        if A <= AK: CPS = ZD - ZA
    else:
        if A <= AK: CPS = CP*A - ZA
        if A > AK: CPS = ZP - ZA
    return CPS

# #### Подпрограмма PSP:
def PSP(W, RE):
    PSP = 1 + 0.32*(W + 0.05*W**4/(1 + 5*RE*0.00001))   #CHANGED
    return PSP

# #### Подпрограмма SIMP:
def SIMP(F, K, X):
    F = [0]*51
    S2 = 0
    S4 = 0
    N = K - 1
    L = 1
    for i in range(1, N):
        if L == 2:
            S2 = S2 + F[i]
            L = 1
        else:
            S4 = S4 + F[i]
            L = 2
    SIMP = X*(F[0] + F[K] + 4*S4 + 2*S2)/(3*N)
    return SIMP

# #### Подпрограмма YI2:
def YI2(Y1, Y2, Y3, X1, X2, X3, X):
    A = ((Y3 - Y1)*(X2 - X1)**2 - (Y2 - Y1)*(X3 - X1)**2)/((X2 - X1)*(X3 - X1)*(X2 - X3))
    B = ((Y2 - Y1)*(X3 - X1) - (Y3 - Y1)*(X2 - X1))/((X2 - X1)*(X3 - X1)*(X2 - X3))
    YI2 = Y1 + A*(X - X1) + B*(X - X1)**2
    return YI2

# #### Подпрограмма PSZ:
def PSZ(X, A):
    PSZ = 1 + 0.5*X/((1 + (5*A)**3)*(1 + 0.85*X))
    return PSZ
