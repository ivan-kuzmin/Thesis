from math import *
import ASPG

def XSPGN1(ANS):
    FM = float(ANS['FM'])
    FG = float(ANS['FG'])
    BG = float(ANS['BG'])
    AG = float(ANS['AG'])
    FN = float(ANS['FN'])
    BN = float(ANS['BN'])
    AN = float(ANS['AN'])
    DG = float(ANS['DG'])
    WH = float(ANS['WH'])

    A = [0]*50
    RM = 0.5642*sqrt(FM)
    RG = 0.5642*sqrt(FG)
    RN = 0.5642*sqrt(FN)
    B = BN + BG
    FNM = FN/FM
    C = 0.01
    XSP = B
    FSP = FN
    ASP = AN
    if AN <= C:
        answer = {'XSP': round(XSP, 4), 'FSP': round(FSP, 4), 'ASP': round(ASP, 4)}
        return answer
    if AG <= C: R = 0
    if AG > C: R = (BG*tan(AG) - RM + RG)/tan(AG)/tan(0.5*AG)
    if R <= 0: R = 0
    XCG = R*sin(AG)
    D = DG/RM

    # Словарь для ASPG
    Input = {'F': FNM, 'D': D, 'WH': WH}
    ASC = ASPG.ASPG(Input).get('ASPG')

    if ASC >= AN:
        answer = {'XSP': round(XSP, 4), 'FSP': round(FSP, 4), 'ASP': round(ASP, 4)}
        return answer
    A[0] = AN
    XS = B
    FS1 = FN
    for i in range(1, 50):
        XSP = XS
        FSP = FS1
        ASP = A[i - 1]
        XS = B - 0.02*B*(i - 2)                     # ??????????????
        if XS <= BG:
            if XS <= XCG:
                FS1 = pi*(sqrt(R**2 - XS**2) - R + RM)**2
                A[i] = atan(XS/sqrt(R**2 - XS**2))
            else:
                FS1 = pi*(RG + tan(AG)*(BG - XS))**2
                A[i] = AG
            FSM = FS1/FM
            DAX = 4*(A[i-1] - A[i])
            Z = 1 + DAX/(1 + (3*WH*DAX)**2)

            # Словарь для ASPG
            Input = {'F': FSM, 'D': D, 'WH': WH}
            ASI = ASPG.ASPG(Input).get('ASPG')*Z

            if ASI >= A[i]:
                answer = {'XSP': round(XSP, 4), 'FSP': round(FSP, 4), 'ASP': round(ASP, 4)}
                return answer
            continue

        if BN <= C*RM:
            if XS <= XCG:
                FS1 = pi*(sqrt(R**2 - XS**2) - R + RM)**2
                A[i] = atan(XS/sqrt(R**2 - XS**2))
            else:
                FS1 = pi*(RG + tan(AG)*(BG - XS))**2
                A[i] = AG
            FSM = FS1/FM
            DAX = 4*(A[i-1] - A[i])
            Z = 1 + DAX/(1 + (3*WH*DAX)**2)

            # Словарь для ASPG
            Input = {'F': FSM, 'D': D, 'WH': WH}
            ASI = ASPG.ASPG(Input).get('ASPG')*Z

            if ASI >= A[i]:
                answer = {'XSP': round(XSP, 4), 'FSP': round(FSP, 4), 'ASP': round(ASP, 4)}
                return answer
            continue

        AS = atan((RG - RN)/BN)
        DX = BN + BG - XS
        FS1 = pi*(RN + tan(AN)*DX - (tan(AN) - tan(AS))*DX**2/BN)**2
        A[i] = atan(tan(AN) - 2*(tan(AN) - tan(AS))*DX/BN)
        FSM = FS1/FM
        DAX = 4*(A[i-1] - A[i])
        Z = 1 + DAX/(1 + (3*WH*DAX)**2)

        # Словарь для ASPG
        Input = {'F': FSM, 'D': D, 'WH': WH}
        ASI = ASPG.ASPG(Input).get('ASPG')*Z

        if ASI >= A[i]:
            answer = {'XSP': round(XSP, 4), 'FSP': round(FSP, 4), 'ASP': round(ASP, 4)}
            return answer
    answer = {'XSP': round(XSP, 4), 'FSP': round(FSP, 4), 'ASP': round(ASP, 4)}
    return answer
