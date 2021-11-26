import numpy as np 
import sys

ga1 = 1.1
ga2 = 1.35
fy = 34.5						#(float(input('tensão de escoamento: ')))
fu = 45						#(float(input('tensão de ultima: ')))
Ag = 37.81						#(float(input('Area de seção bruta: ')))
ec = 2.62						#(float(input('excentricidade da ligação: ')))
lc = 14						#(float(input('comprimento conectado: ')))
np = 2						#(float(input('número de parafusos na linha de ruptura: ')))
db = 2.22						#(float(input('diâmetro dos parafusos: ')))
t = 1.59						#(float(input('espessura da chapa: ')))
diagonais = 'não'				#(input('possui diagonais?: '))
Ct = 1 - ec/lc
if(diagonais == 'sim'):
	s = 7						#(float(input('s: ')))
	g = 7.11						#(float(input('g: ')))
	nd = 2						#(float(input('número de diagonais(sim/não): ')))
	An = Ag - (np*(db+0.35)*t) + nd*((s**2)/(4*g))*t
elif(diagonais == 'não'):
	An = Ag - (np*(db+0.35)*t)
else:
	print('Escolha uma resposta correta para diagonais')
    
Ae = Ct*An

#Resstência ao escoamento da seção bruta
Ntag = (fy*Ag)/ga1

#Resistência à rup. da seção liq.
Ntae = (fu*Ae)/ga2

print('Area nominal: ', An)
print('Ct: ', Ct)
print('Escoamento: ', Ntag)
print('Ruptura: ', Ntae)