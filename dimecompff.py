import numpy as np
import math as mt
import pandas as pd
from matplotlib import pyplot as plt
import sys

## Dimensionamento de Barras Comprimidas de PFF ##
## Nc,Sd <= Nc,Rd com Nc,Rd sendo o menor valor calculado em 9.7.2 e 9.7.3 da NBR 14762:2010 ##

### Atualmente este código está considerando apenas tenões uniformes em toda a seção transversal ###

#Ajustes iniciais
nperfis = 8 #número de perfis na planilha
#criar a linha de corte dos perfis
Line = np.ones((nperfis))

#Dados de projeto
perfil = 6
E = 20000 #kN/cm²
G = 7700 #kN/cm²
fy = 24 #kN/cm²
Kx = 1
Ky = 1
Kz = 1
Lx = 150 #cm
Ly = 150 #cm
Lz = 150 #cm
ka = 4.0
km = 0.43
rmin = 'y'
Ncsd = 15
PS = pd.read_excel(r'C:\Users\I5-Coffee Lake\Documents\AW\PYTHON\PythonProjects\Perfis\Perfis PFF.xlsx')
Bitola = np.array(PS[0:nperfis] ['Bitola'])
Ix = np.array(PS[0:nperfis] ['Ix'])
Iy = np.array(PS[0:nperfis] ['Iy'])
It = np.array(PS[0:nperfis] ['It'])
Cw = np.array(PS[0:nperfis] ['Cw'])
rx = np.array(PS[0:nperfis] ['rx'])
ry = np.array(PS[0:nperfis] ['ry'])
x0 = np.array(PS[0:nperfis] ['x0'])
r0 = np.array(PS[0:nperfis] ['r0'])
A = np.array(PS[0:nperfis] ['Area'])
bf = np.array(PS[0:nperfis] ['bf'])
bw = np.array(PS[0:nperfis] ['bw'])
t = np.array(PS[0:nperfis] ['t'])
bftf = bf/t
bwtw = bw/t

### O aumento da resistência ao escoamento
# pode ser utilizado no dimensionamento de
# barras submetidas à compressão ou à flexão,
# que não estejam sujeitas à redução de capacidade
# devido à ---instabilidade local---

# 9.7.2 Flambagem Global por Flexão, por Torção ou por Flexo-Torção #

gamma = 1.20
#Cálculo do qui
Nex = ((mt.pi**2)*E*Ix)/(Kx*Lx)**2
Ney = ((mt.pi**2)*E*Iy)/(Ky*Ly)**2
Nez = (1/r0**2)*(((mt.pi**2)*E*Cw)/(Kz*Lz)**2+G*It)
Nexz = ((Nex + Nez)/(2*(1-(x0/r0)**2)))*(1-(1-(4*Nex*Nez*(1-x0/r0)**2)/(Nex+Nez)**2)**0.5)
Ne = np.where(Ney < Nexz, Ney, Nexz)
lo = ((A*fy)/Ne)**0.5
X = np.where(lo > 1.5, 0.877/((lo)**2), 0.658**(lo**2))
           
# Instabilidade Local e o método das larguras efetivas (MLE)

sigma = X*fy
lpm = bftf/(0.95*(((km*E)/sigma)**0.5)) 
lpa = bwtw/(0.95*(((ka*E)/sigma)**0.5))
bfef = np.where(lpm > 0.673, (bf*(1-0.22/lpm))/lpm, bf)
bwef = np.where(lpa > 0.673, (bw*(1-0.22/lpa))/lpa, bw)
Aef = 2*bfef*t+bwef*t

#Cálculo da resistência
NcRd = (X*Aef*fy)/gamma

#Dimensionamento
Rank = np.array(range(nperfis))
dim = np.array(NcRd/Ncsd)

print('Analisando o perfil: ', perfil)
print('Bitola: ', Bitola[perfil])
print('ry: ', ry[perfil])
print('lpm: ', lpm[perfil])
print('lpa: ', lpa[perfil])
print('bfef: ', bfef[perfil])
print('bwef: ', bwef[perfil])
print('X: ', X[perfil])
print('Área: ', A[perfil])
print('Aef: ', Aef[perfil])
print('NcRd: ', NcRd[perfil])
plt.scatter(Rank, dim)
plt.plot(Rank, Line)
plt.show()