from math import *

# #### Подпрограмма FT:
def FT(A):
    FT = 15*abs(A)**2.4/(1+7.7*abs(A)**1.8)
    return FT


# #### Подпрограмма QV:
def QV(G, V):
    TV = 1 - (G - 1)/(G + 1)*V*V
    QV = (0.5*(G + 1))**(1/(G - 1))*V*TV**(1/(G - 1))
    return QV


# #### Подпрограмма VP:
def VP(G, PO):
    VP = sqrt((G + 1)/(G - 1)*(1 - PO**((1 - G)/G)))
    return VP


# #### Подпрограмма PV:
def PV(G, V):
    PV = (1 - (G - 1)/(G + 1)*V**2)**(G/(G - 1))
    return PV


# #### Подпрограмма TV:
def TV(G, V):
    TV = 1 - (G - 1)/(G + 1)*V**2
    return TV


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


# #### Подпрограмма WV:
def WV(G, V):
    WV = sqrt(2/(G + 1)*V**2/(1 - (G - 1)/(G + 1)*V**2))
    return WV


# #### Подпрограмма VPC:
def VPC(G, P):
    VPC = sqrt((G + 1)/(G - 1)*(1 - P**((G - 1)/G)))
    return VPC


# #### Подпрограмма CPS:
def CPS(W, A):
    if W <= 1: DPP = 1/(1 - 2*W**2/(1 + 0.2*W**2))**3.5 - 1
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


# #### Подпрограмма ZV:
def ZV(V):
    ZV = V + 1/V
    return ZV


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
    if P0 <= P0K: RID = ZR*P0*VP(G, P0)*QV(G, VP(G, P0))
    return RID


# #### Подпрограмма PSP:
def PSP(W, RE):
    PSP = 1 + 32*(W + 0.5*W**4/(1 + 5*RE*0.00001))   #CHANGED
    return PSP


# #### Подпрограмма PSZ:
def PSZ(X, A):
    PSZ = 1 + 0.5*X/((1 + (5*A)**3)*(1 + 0.85*X))
    return PSZ
