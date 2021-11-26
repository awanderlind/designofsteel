import numpy as np
import math as mt
import pandas as pd
from matplotlib import pyplot as plt

#Ajustes iniciais
nperfis = 51 #número de perfis na planilha
#Dados de projeto
perfil = 0
E = 20000 #kN/cm²
Kx = 1.0
Lx = 153.6 #cm
PS = pd.read_excel(r'\\SILIX\Documents\AW\PYTHON\PythonProjects\Perfis\Perfis L.xlsx')
Ix = np.array(PS[0:nperfis] ['Ix'])
rx = np.array(PS[0:nperfis] ['rx'])
Lef = np.where(Lx/rx <= 75, 60*rx + 0.8*Lx, 45*rx + Lx)

Nex = (np.pi**2*E*Ix)/(Lef)**2

#Iy = np.array(PS[0:nperfis] ['Iy'])
#Ixy =
#Cw =
#J = np.array(PS[0:nperfis] ['It'])

#a = E**3*(Iy*Ix-Ixy**2)*Cw
#b = E**2*[(Iy*Ix-Ixy**2)*P*r0**2-G*J]

print('Analisando o perfil: ', perfil)
print('Nex: ', round(Nex[perfil],2), 'kN')
print('Lef: ', round(Lef[perfil],2), 'cm')
print(Ix[perfil])