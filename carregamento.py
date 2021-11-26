import numpy as np 

Pp = 44
SC = 75
Vib = 76
Eq = 66
gPp = 1.3
gSC = 1.4
gVib = 1.3
gEq = 1.5
psiSC = 0.7
psiVib = 0.8
psiEq = 0.8
Fd1 = gPp*Pp+gSC*SC+gEq*psiEq*Eq+gVib*psiVib*Vib
Fd2 = gPp*Pp+gSC*psiSC*SC+gEq*Eq+gVib*psiVib*Vib
Fd3 = gPp*Pp+gSC*psiSC*SC+gEq*psiEq*Eq+gVib*Vib
print('Fd1: ',Fd1)
print('Fd2: ',Fd2)
print('Fd3: ',Fd3)