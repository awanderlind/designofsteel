import numpy as np

NtSd = 433
bf = 10.160
t = 1.111
ec = 2.95
fy = 35
fu = 45
b = 2*bf-t
bi = bf-t
g = (bi-3-3.5)/2
s = 7
An1 = (b-2*(1.6+0.35))*t
An2 = (b-3*(1.6+0.35)+((s**2)/(4*g)))*t
A = b*t
def menor(An1,An2,A):
    min = An1

    if An2 < min:
        min = An2
    if A < min:
        min = A

    return min
lc = 14
Ct = 1-(ec/lc)
fyAg = (fy*A)/1.1
fuAe = (fu*menor(An1,An2,A)*Ct)/1.35

print('Ag: ', round(A,2),'cm²')
print('An1: ', round(An1,2),'cm²')
print('An2: ', round(An2,2),'cm²')
print('fyAg: ', round(fyAg,2),'kN')
print('fuAe: ', round(fuAe,2),'kN')
print('NtSd: ', NtSd, 'kN')