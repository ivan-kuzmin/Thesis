from math import *
import PROGRAMS as prgs

def RXJT1(ANS):
    RC = float(ANS['RA'])
    AC = float(ANS['AA'])
    GC = float(ANS['GC'])
    VC = float(ANS['VA'])
    P0C = float(ANS['P0C'])
    XS = float(ANS['XJ'])

    X = XS/RC
    VS = prgs.VP(GC, P0C)
    CN = prgs.PV(GC, VC)/prgs.PV(GC, VS)
    if VC <= 1: VC = 1.001
    if VS <= 1:
        if VC <= 1.001:
            Z2 = 0.05*(1 - 2.63*AC)*AC/(1 + AC**2)
            G1 = Z2*X*X/(0.5 + X*X)
            G2 = X*tan(AC)*exp(-2*X)
            G3 = 0
            Z7 = Z2*X/(0.5 + X*X)**2 + (1 - 2*X)*tan(AC)*exp(-2*X)
        else:
            Z2 = sqrt(prgs.QV(GC, VC)/(prgs.QV(GC, 1/VC)*prgs.P0NSH(GC, VC))) - 1
            Z7 = Z2*X/(0.5 + X*X)**2 + (1 - 2*X)*tan(AC)*exp(-2*X)
            G = Z2*X*X/(0.5 + X*X)
            G2 = X*tan(AC)*exp(-2*X)
            G3 = 0
    else:
        WC = sqrt(prgs.WV(GC, VC)**2 - 1)                                                          # CHANGED
        WS = sqrt(prgs.WV(GC, VS)**2 - 1)
        if AC <= 0 and -AC > 0.09: ASC = prgs.AV(GC, VS) + 0.6*(AC + 0.09)
        if AC <= 0 and -AC <= 0.09: ASC = prgs.AV(GC, VS)
        if AC > 0: ASC = prgs.AV(GC, VS) - prgs.AV(GC, VC) + AC
        Z2 = sqrt(prgs.QV(GC, VC)/prgs.QV(GC, VS)*CN**0.25) - 1
        Z3 = 0.6366*(WC + 1.4*(WS - 0.71*WC)*abs(1 - 1/CN)**0.125)
        AX = X/Z3
        G1 = Z2*X*X/(3.5 + X*X)
        G2 = X*tan(ASC)*exp(-X)
        G3 = 1.5*Z2*abs(sin(AX))*X/(2 + X*X)
        N = 0.3183*AX
        Z4 = (1 - X)*tan(ASC)*exp(-X)
        Z5 = (2 - X*X)/(2 + X*X)**2
        print(str(AX) + "AX\n" + str(X) + "X\n" + str(N) + "N\n" + str(Z3) + "Z3\n")
        Z6 = cos(AX)*X*-1**(2 + N)/((2 + X*X)*Z3)
        Z6 = 1.5*Z2*(Z6 + Z5*abs(sin(AX)))
        Z7 = 7*Z2*X/((3.5 + X*X)**2) + Z4 + Z6
    RS = (1 + G1 + G2 + G3)*RC
    AS = atan(Z7)

    answer = {'RJ': round(RS, 4), 'AJ': round(AS, 4)}
    return answer
