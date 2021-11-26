import numpy as np
import pandas as pd

perfil = 44
E = 20000
fy = 34.5
PL = pd.read_excel(r'C:\Users\I5-Coffee Lake\Documents\AW\Momento\PythonProjects\Perfis\Bitolas_Perfis_Laminados.xlsx')
h0t0 = np.array(PL[0:88] ['FLA'])
h0 = np.array(PL[0:88] ['h'])
t0 = np.array(PL[0:88] ['tw'])

lp = 1.10*((5*E)/fy)**0.5
lr = 1.37*((5*E)/fy)**0.5
Vp = 0.6*h0*t0*fy
Vine = (lp/h0t0)*Vp
Vela = 1.24*((lp/h0t0)**2)*Vp
Vn1 = np.where(h0t0 > lr, Vela, Vine)
Vn = np.where(h0t0 <= lp, Vp, Vn1)
Vrd = Vn/1.1

print('Analisando o perfil: ', perfil)
print('lambda: ', h0t0[perfil])
print('lbp: ', lp)
print('lr: ', lr)
print('Vn: ', Vn[perfil])
print('Vrd: ', Vrd[perfil])