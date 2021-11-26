import numpy as np
import math as mt
import pandas as pd
from matplotlib import pyplot as plt

#Dimensionamento de elementos sofrendo apenas flexão


#Ajustes iniciais

#Ajustes iniciais
nperfis = 130 #número de perfis na planilha
#criar a linha de corte dos perfis
Line = np.ones((nperfis))

#Dados de projeto
E = 20000 #[kN/cm²]
fy = 25 #[kN/cm²]
ga1 = 1.1
Msd = 1000 #[kN.cm]
lb = 1200 #[cm]
Ma = Msd
Mb = Msd
Mc = Msd
perfil = 38
#Msd = (float(input('Momento máximo: ')))*np.ones((130))
#ga1 = float(input('coef. escoamento: '))
#fy = float(input('tensão de escoamento: '))
#lb = float(input('Comprimento destravado: '))
PS = pd.read_excel(r'\\SILIX\Documents\AW\PYTHON\PythonProjects\Perfis\Perfis VS.xlsx')
Bitola = np.array(PS[0:nperfis] ['Bitola'])
ix = np.array(PS[0:nperfis] ['rx'])
iy = np.array(PS[0:nperfis] ['ry'])
Ag = np.array(PS[0:nperfis] ['Ag'])
h0t0 = np.array(PS[0:nperfis] ['FLA'])
bf2tf = np.array(PS[0:nperfis] ['FLM'])
h0 = np.array(PS[0:nperfis] ['h'])
t0 = np.array(PS[0:nperfis] ['tw'])
bf = np.array(PS[0:nperfis] ['bf'])
tf = np.array(PS[0:nperfis] ['tf'])
Zx = np.array(PS[0:nperfis] ['Zx'])
Wx = np.array(PS[0:nperfis] ['Wx'])
d = np.array(PS[0:nperfis] ['d'])
Ix = np.array(PS[0:nperfis] ['Ix'])
Iy = np.array(PS[0:nperfis] ['Iy'])
J = np.array(PS[0:nperfis] ['J'])
kc = 4/(h0t0)**0.5
ar = np.where((h0*t0)/(bf*tf) <= 10, (h0*t0)/(bf*tf), 10) 
k = 1-((ar)/(1200+300*ar))*(h0t0-5.7*(E/fy)**0.5)
Cw = ((d-tf)**2)*(Iy/4)

#Verificação de Flambagem Lateral com torção
B1 = (0.7*fy*Wx)/(E*J)
lbp = 1.76*iy*(E/fy)**0.5
lbr = ((1.38*(Iy*J)**0.5)/(J*B1))*(1+((1+(27*Cw*B1**2)/Iy)**0.5))**0.5
#Verificação das flambagens locais (tipo do perfil)
lpm = 0.38*(E/fy)**0.5
lrm = 0.95*(E/(0.7*(fy/kc)))**0.5
lpa = 3.76*(E/fy)**0.5
lra = 5.7*(E/fy)**0.5
#Cálculo dos diversos momentos nominais
Mp = Zx*fy
Mrm = Wx*(0.7*fy)
Mra = Wx*fy
Mcrm = (0.9*E*kc*Wx)/(bf2tf)**2
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
Rank = np.array(range(130))
dim = np.array(Mrd/Msd)

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
plt.scatter(Rank, dim)
plt.plot(Rank, Line)
plt.show()