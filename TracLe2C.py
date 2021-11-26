import numpy as np
import math as mt
##Questão 1##
fy = 35
A = 37.8
bf = 12.7
xg = 3.76
fw = 48.5
ga1 = 1.1
ga2 = 1.35
gw2 = 1.35
NtSd = 0.9*((fy*A)/ga1)
b = 1
tw = 0.707*b
lw = (NtSd*gw2)/(0.6*tw*fw)
F2 = 0.6*fw*tw*bf
F1 = NtSd*(xg/bf)-(F2/2)
F3 = NtSd-F1-F2
lw1 = (F1*gw2)/(0.6*tw*fw)
lw2 = bf
lw3 = (F3*gw2)/(0.6*tw*fw)
FRd = (0.6*25*(lw*1.9))/1.1

print('Questão 1')
print('NtSd: ', NtSd)
print('lw: ', lw)
print('lw1: ', lw1)
print('lw2: ', lw2)
print('lw3: ', lw3)
print('FRd: ', FRd)

##Questão 2##
Vd = 1250
nv = 2 #planos de corte do parafuso
fub = 82.5
db = (3/4)*2.54
Ab = 0.25*np.pi*db**2
FvRd = nv*(0.4*Ab*fub)/1.35
np = mt.ceil(Vd/FvRd)


print('Questão 2')
print('np: ', np)