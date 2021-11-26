import numpy as np
import math as mt
import pandas as pd
from matplotlib import pyplot as plt
import time
import sys

#Dimensionamento de elementos sofrendo apenas compressão

#Ajustes iniciais
nperfis = 87 #número de perfis na planilha
#criar a linha de corte dos perfis
Line = np.ones((nperfis))

#Dados de projeto
E = 20000
ga1 = 1.1
fy = 35
K = 1
L = 200
imin = 'y'
Ncsd = 20
perfil = 24
#Ncsd = (float(input('Carga de solicitação: ')))*np.ones((88))
#ga1 = float(input('coef. escoamento: '))
#fy = float(input('tensão de escoamento: '))
#K = float(input('coef. do apoio: '))
#L = float(input('comprimento do elemento: '))
#imin = input('eixo de flambagem: ')
inicio = time.time()
PS = pd.read_excel(r'\\SILIX\Documents\AW\PYTHON\PythonProjects\Perfis\Perfis W.xlsx')
Bitola = np.array(PS[0:nperfis] ['Bitola'])
ix = np.array(PS[0:nperfis] ['ix'])
iy = np.array(PS[0:nperfis] ['iy'])
Ag = np.array(PS[0:nperfis] ['Ag'])
h0t0 = np.array(PS[0:nperfis] ['FLA'])
bf2tf = np.array(PS[0:nperfis] ['FLM'])
h0 = np.array(PS[0:nperfis] ['hw'])
t0 = np.array(PS[0:nperfis] ['tw'])

#Cálculo da resistência
#Cálculo do qui
if(imin == 'y'):
    lo = ((K*L)/iy)*((fy/(mt.pi**2*E))**0.5)
    X_i = np.where(lo > 1.5, 0.877/((lo)**2), 0.658**(lo**2))
    
elif(imin == 'x'): 
    lo = ((K*L)/ix)*((fy/(mt.pi**2*E))**0.5)
    X_i = np.where(lo > 1.5, 0.877/((lo)**2), 0.658**(lo**2))
else:
    print('Escolha um eixo de flambagem válido')
    sys.exit()
              
sigma = X_i*fy
    
#Verificação das flambagens locais (Q)
#Flambagem local na Alma (Qa)
hef = np.where(h0 < 1.92*t0*((E/sigma)**0.5)*(1-((0.34/h0t0)*((E/sigma)**0.5))), h0, 1.92*t0*((E/sigma)**0.5)*(1-((0.34/h0t0)*((E/sigma)**0.5))))
Qa = np.where(h0t0 > 1.49*((E/fy)**0.5), (Ag - (h0 - hef)*t0)/Ag, 1.0) 
#Flambagem local na mesa (Qs)
Qsi = 1.415 - 0.74*bf2tf*((fy/E)**0.5)                  #Flambagem local na mesa inelástica
Qss = (0.69*E)/(fy*bf2tf**2)                               #Flambagem local na mesa elástica
Qs1 = np.where(bf2tf > 1.03*(E/fy)**0.5, Qss, Qsi)      #Cálculo considerando que todos os perfis possuam FLM
Qs = np.where(bf2tf <= 0.56*(E/fy)**0.5, 1.0, Qs1)
Q = Qa*Qs

#Recalcular X considerando mt.sqrt(Q)
lo_f = lo*(Q)**0.5
X_f = np.where(lo_f > 1.5, 0.877/((lo_f)**2), 0.658**(lo_f**2))
X = np.where(Q < 1.0, X_f, X_i)

Ncrd = (X*fy*Ag*Q)/ga1

#Dimensionamento
Rank = np.array(range(nperfis))
dim = np.array(Ncrd/Ncsd)

fim = time.time()
exectime = fim - inicio
print('Tempo de execução do cálculo: ', exectime)
print('Analisando o perfil: ', perfil)
print('Bitola: ', Bitola[perfil])
print('iy: ', iy[perfil])
print('Qa: ', Qa[perfil])
print('Qs: ', Qs[perfil])
print('X: ', X[perfil])
print('Ncrd: ', Ncrd[perfil])
print('dim: ', dim[perfil])
plt.scatter(Rank, dim)
plt.plot(Rank, Line)
plt.show()