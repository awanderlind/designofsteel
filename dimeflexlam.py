import numpy as np
import math as mt
import pandas as pd
from matplotlib import pyplot as plt

#Dimensionamento de elementos sofrendo apenas flexão


#Ajustes iniciais
nperfis = 87 #número de perfis na planilha
#criar a linha de corte dos perfis
Line = np.ones((nperfis))

#Dados de projeto
E = 20000
ga1 = 1.1
fy = 35
Msd = 550.1*100
Ma = Msd
Mb = Msd
Mc = Msd
lb = 0
VSd = 135.5
perfil = 31
#Msd = (float(input('Momento máximo: ')))*np.ones((88))
#ga1 = float(input('coef. escoamento: '))
#fy = float(input('tensão de escoamento: '))
#lb = float(input('Comprimento destravado: '))
PS = pd.read_excel(r'\\SILIX\Documents\AW\PYTHON\PythonProjects\Perfis\Perfis W.xlsx')
Bitola = np.array(PS[0:nperfis] ['Bitola'])
iy = np.array(PS[0:nperfis] ['iy'])
Ag = np.array(PS[0:nperfis] ['Ag'])
h0t0 = np.array(PS[0:nperfis] ['FLA'])
bf2tf = np.array(PS[0:nperfis] ['FLM'])
h0 = np.array(PS[0:nperfis] ['hw'])
t0 = np.array(PS[0:nperfis] ['tw'])
bf = np.array(PS[0:nperfis] ['bf'])
tf = np.array(PS[0:nperfis] ['tf'])
Zx = np.array(PS[0:nperfis] ['Zx'])
Wx = np.array(PS[0:nperfis] ['Wx'])
Ix = np.array(PS[0:nperfis] ['Ix'])
d = np.array(PS[0:nperfis] ['d'])
Iy = np.array(PS[0:nperfis] ['Iy'])
J = np.array(PS[0:nperfis] ['J'])
ar = np.where((h0*t0)/(bf*tf) <= 10, (h0*t0)/(bf*tf), 10) 
k = 1-((ar)/(1200+300*ar))*(h0t0-5.7*(E/fy)**0.5)
Cw = ((d-tf)**2)*(Iy/4)

#Verificação de Flambagem Lateral com torção
B1 = (0.7*fy*Wx)/(E*J)
lbp = 1.76*iy*(E/fy)**0.5
lbr = ((1.38*(Iy*J)**0.5)/(J*B1))*(1+((1+(27*Cw*B1**2)/Iy)**0.5))**0.5
#Verificação das flambagens locais (tipo do perfil)
lpm = 0.38*(E/fy)**0.5
lrm = 0.83*(E/(0.7*fy))**0.5
lpa = 3.76*(E/fy)**0.5
lra = 5.7*(E/fy)**0.5
#Cálculo dos diversos momentos nominais
Mp = (Zx*fy)
Mrm = Wx*(0.7*fy)
Mra = Wx*fy
Mcrm = (0.69*E*Wx)/(bf2tf)**2
Mcra = Wx*k*fy
Mintm = Mp - (bf2tf - lpm)/(lrm - lpm)*(Mp - Mrm)
Minta = Mp - (h0t0 - lpa)/(lra - lpa)*(Mp - Mra)
#Cálculo da resistência
if(lb == 0):
	Mnm1 = np.where(bf2tf > lrm, Mcrm, Mintm)
	Mnm = np.where(bf2tf <= lpm, Mp, Mnm1)
	Mna1 = np.where(h0t0 > lra, Mcra, Minta)
	Mna = np.where(h0t0 <= lpa, Mp, Mna1)
	Mn = np.where(Mnm <= Mna, Mnm, Mna)
else:
	#Ma = float(input('Qual o valor de Ma: '))
	#Mb = float(input('Qual o valor de Mb: '))
	#Mc = float(input('Qual o valor de Mc: '))
	Cb = np.where((12.5*Msd)/(2.5*Msd+3*Ma+4*Mb+3*Mc) <= 3, (12.5*Msd)/(2.5*Msd+3*Ma+4*Mb+3*Mc), 3)
	Mcr = Cb*((np.pi**2*E*Iy)/lb**2)*((Cw/Iy)*(1+0.039*((J*lb**2)/Cw)))**0.5
	MintCb = Cb*(Mp-(Mp-Mrm)*((lb-lbp)/(lbr-lbp)))
	Mn1 = np.where(lb > lbr, Mcr, MintCb)
	Mn = np.where(lb <= lbp, Mp, Mn1)

#Dimensionamento
Mrd = Mn/ga1
Rank = np.array(range(nperfis))
dim = np.array(Mrd/Msd)

#Verificação Cortante
kv = 5
lp_v = 1.1*((kv*E)/fy)**0.5
lr_v = 1.37*((kv*E)/fy)**0.5
Vpl = 0.6*d*t0*fy
VRd1 = np.where(h0t0 > lr_v, (1.24*((lp_v/h0t0)**2)*Vpl)/ga1, ((lp_v/h0t0)*Vpl)/ga1)
VRd = np.where(h0t0 <= lp_v, Vpl/ga1, VRd1)

#Verificação da flecha limite

#Viga tipo 6

print('Analisando o perfil: ', perfil)
print('Bitola: ', Bitola[perfil])
if(lb != 0):
	print('Cb: ', Cb)
	print('lbp: ', lbp[perfil])
	print('lbr: ', lbr[perfil])
else:
	print('Cb: ', 1.0)

print('Mn: ', Mn[perfil])
print('Mrd: ', Mrd[perfil])
print('Msd: ', Msd)
print('Ix: ', Ix[perfil])
print('VSd: ', VSd, 'kN')
print('VRd: ', VRd[perfil], 'kN')
print('lp_v: ', lp_v)
print('lr_v: ', lr_v)
print('h0t0: ', h0t0[perfil])
plt.scatter(Rank, dim, color = 'k')
plt.plot(Rank, Line, 'b--')
plt.show()