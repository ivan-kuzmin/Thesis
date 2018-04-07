from math import *
import pandas as pd

FK = 3.14
FCK = 2
GC = 1.4
DK = 0.1
RE = 1000000
TW = 1
DY0 = 0.004
RD = [2.305, 2.238, 1.926, 1.610, 1.453, 1.376, 1.297, 1.225, 1.151, 1.074, 1.000]
XD = [0, 0.640, 1.260, 1.880, 2.190, 2.340, 2.490, 2.640, 2.790, 2.940, 3.090]

def RXLN1():
    A = [0]*15
    A1 = [0]*15
    D1 = [0]*15
    D2 = [0]*15
    D3 = [0]*15
    D = [0]*15
    B = [0]*15

    YI = YID(1, G, 1.0, FCK)
    VC = VQ(1, G, FCK)
    RK = 0.5642*sqrt(FK)
    RC = 0.5642*sqrt(FCK*FK)
    XD[0] = 0
    RD[0] = RK
    DXK = 0.09*DK
    DY = 0.1
    L = 1
    for i in range(0, 15):
        K = i
        A[i] = 0.04*((i+1) - 1)                                   #CHANGED
        ZS = 2/(1 + cos(A(i)))
        TC = tan(A(i))
        VS = VQ(1, G, FCK*ZS)
        AA = asin(1/WV(G, VS)) + A[i]
        D1[i] = 1 - ZV(VS)/(ZS*ZV(VC))
        X2 = 0
        if i == 1:
            X2 = RC/tan(AA)
            W0 = WV(G, VC)
        else:
            R0 = RC/sin(A[i])
            X0 = RC/tan(A[i])
            for j in range(0,20):
                R2 = RC*(1 - 0.05*(j+1))                          #CHANGED
                X1 = X2 + 0.05*RC/tan(AA)
                FSK = FCK*ZS*(R2**2 + (X0 - X1)**2)/R0**2
                VS = VQ(1, G, FSK)
                AA1 = asin(1/WV(G, VS)) + atan(R2/(X0 - X1))
                X2 = X2 + 0.025*(0.5/tan(AA) + 1.5/tan(AA1))*RC
                FSK = FCK*ZS*(R2**2 + (X0 - X2)**2)/R0**2
                VS = VQ(1, G, FSK)
                AA = asin(1/WV(G, VS)) + atan(R2/(X0 - X2))
            W0 = WV(G, VS)
        get_ipython().magic('pinfo2 ')
        B[i] = RK*XK + X2
        BC = B[i]
        C1 = tan(A1[i])
        C2 = (4*(RC - RK) - 2*BC*(C1 + TC))/BC**1.5
        C3 = (-3*(RC - RK) + BC*(C1 + 2*TC))/BC**2
        W1 = 1
        S = 0
        for j in range(1, 21):
            XD[j] = 0.05*((j+1) - 1)*BC                           #CHANGED
            RD[j] = RK + C1*XD[j] + C2*XD[j]**1.5 + C3*XD[j]**2
            F = (RD[j]/RK)**2
            W2 = WV(G, VQ(1, G, F))
            DS = 0.0786*BC*(RD(j-1) + RD[j])/FK
            S = S + DS*G*W2**4*PV(G, VW(G, W2))*CF(TW, G, RE, W2, DXK)/W1**2
            W1 = W2
        D2[i] = S/YI
        D3[i] = D1[i] + D2[i]
        if L == 1: D[i] = D3[i] - DY
        if L == 2: D[i] = D3[i] - DY1
        if D[i] >= 0 and L == 1:
            L = 2
            DY1 = DY + DY0
            get_ipython().magic('pinfo2 ')
        if D[i] >= 0 and L == 2:
            Z = 0.5*(1 + (D[K-1] + D[K])/(D[K-1] - D[K]))
            DYA = D1[K-1] + (D1[K] - D1[K-1])*Z
            DYD = D2[K-1] + (D2[K] - D2[K-1])*Z
            CY = 1 - D3[K-1] - (D3[K] - D3[K-1])*Z
            AC = A[K-1] + (A[K] - A[K-1])*Z
            AK = A1[K-1] + (A1[K] - A1[K-1])*Z
            BC = B[K-1] + (B[K] - B[K-1])*Z
            TC = tan(AC)
            C1 = tan(AK)
            C2 = (4*(RC - RK) - 2*BC*(C1 + TC))/BC**1.5
            C3 = (-3*(RC - RK) + BC*(C1 + 2*TC))/BC**2
            for j in range(1, 21):
                XD[j] = 0.5*((j+1) - 1)*BC
                RD[j] = RK + C1*XD[j] + C2*XD[j]**1.5 + C3*XD[j]**2
    return(BC, AC, DYA, DYF, CY)

RXLN1(FK, FCK, GC, DK, RE, TW, DY0, RC, XC)
BC = RXLN1(FK, FCK, GC, DK, RE, TW, DY0, RC, XC)[0]
AC = RXLN1(FK, FCK, GC, DK, RE, TW, DY0, RC, XC)[1]
DYA = RXLN1(FK, FCK, GC, DK, RE, TW, DY0, RC, XC)[2]
DYF = RXLN1(FK, FCK, GC, DK, RE, TW, DY0, RC, XC)[3]
CY = RXLN1(FK, FCK, GC, DK, RE, TW, DY0, RC, XC)[4]

print("Подпрограмма RXLN1.")
print("=======================")
print("Иходные идентификаторы:", end = "\n\n")
print("FK =", FK)
print("FCK =", FCK)
print("GC =", GC)
print("DK =", DK)
print("RE =", RE)
print("TW =", TW)
print("DY0 =", DY0, end="\n\n")
frame = pd.DataFrame({'RD': [RD[i] for i in range(11)], 'XD': [XD[i] for i in range(11)]})
print(frame, end = "\n\n")
print("-----------------------")
print("BC =", round(BC, 2), end=" ")
print("+") if round(BC, 2) == 2.60 else print("(2.60) -")
print("AC =", round(AC, 3), end=" ")
print("+") if round(AC, 3) == 0.175 else print("(0.175) -")
print("DYA =", round(DYA, 4), end=" ")
print("+") if round(DYA, 4) == 0.0067 else print("(0.0067) -")
print("DYF =", round(DYF, 4), end=" ")
print("+") if round(DYF, 4) == 0.0051 else print("(0.0051) -")
print("CY =", round(CY, 4), end=" ")
print("+") if round(CY, 4) == 0.9842 else print("(0.9842) -")
print("-----------------------")
#BC = 2.60
#AC = 0.175
#DYA = 0.0067
#DYF = 0.0051
#CY = 0.9842
