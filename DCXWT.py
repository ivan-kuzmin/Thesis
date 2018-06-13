from math import *
import PROGRAMS as prgs

def DCXWT(ANS):
    N = int(ANS['N'])
    FM = float(ANS['FM'])
    FN = float(ANS['FN'])
    BWT = [0]*N
    BWE = [0]*N
    BWN = [0]*N
    for i in range(N):
        BWT[i] = float(ANS['BWT'].split(',')[i])
        BWE[i] = float(ANS['BWE'].split(',')[i])
        BWN[i] = float(ANS['BWN'].split(',')[i])
    DXSP = float(ANS['DXSP'])
    FSP = float(ANS['FSP'])
    ASP = float(ANS['ASP'])
    WH = float(ANS['WH'])
    PD0 = float(ANS['PD0'])
    PDJ = float(ANS['PDJ'])

    DX = [0]*5
    DW = [0]*5
    BD = [0]*5
    ZX = [0]*5
    FSW = [0]*5

    FS = 0
    BS = 0
    ZS = 0
    ZW = 0.7*WH**2*FM
    for i in range(0, N):
        DX[i] = BWN[i] - DXSP
        if DX[i] <= 0: DX[i] = 0
        DW[i] = 0.15*BWT[i]
        BD[i] = BWE[i] + 2*DW[i]
        ZX[i] = 1 + 0.2 *(DX[i]/BD[i])**2
        FSW[i] = ((DX[i]*BD[i] + 2*DW[i]**2/(1 + 0.5*WH**6))*sin(ASP) + 3*BWE[i]**2 + 0.1*DW[i]**2)/ZX[i]
        FS = FS + FSW[i]
        BS = BS + BD[i]
        ZS = ZS + ZX[i]
    ZS = ZS/N
    DPW = 0.02*BS*(0.3*WH + exp(-10*abs(WH - 1)))/(FSP**0.5*ZS)
    DCXW = ((FSP - FN)*DPW + FS*(PD0 - PDJ + DPW))/ZW
    PDW = PDJ - DPW

    answer = {'PDW': PDW, 'DCXW': DCXW}
    return answer
