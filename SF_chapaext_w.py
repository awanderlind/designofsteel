import numpy as np
from matplotlib import pyplot as plt

#Ajuste inivial (line)
ndw = 20
line = [21.5]*ndw

#Cálculo da solda de filete em todo o entorno de um perfil W

Md = 13650 #kN.cm
Vd = 129.5 #kN
bf = 12.7
dw = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]) #cm
d = 34.9
tw = 0.58
h = 33.2
Ix = 2*(bf*0.707*dw*(d/2)**2 + (bf-tw)*0.707*dw*(h/2)**2) + 2*((0.707*dw*h**3)/12)
y = d/2
Ta = (Md/Ix)*y
Aw = 2*(0.707*dw*h)
T = Vd/Aw
Tb = (Ta**2 + T**2)**0.5

print('Ix: ', Ix)
print('Ta: ', Ta)
print('Tb: ', Tb)
plt.scatter(dw, Ta)
plt.scatter(dw, Tb)
plt.plot(dw, line)
plt.show()