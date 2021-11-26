import numpy as np

#Verificação Básica Flexocompressão
NSd = 20
NcRd = 1044.5689189569382
MSd = 10000
MRd = 20069.89916864567

if(NSd/NcRd < 0.2):
	flexcom = NSd/(2*NcRd) + (MSd/MRd)
else:
	flexcom = NSd/NcRd + (8/9)*(MSd/MRd)

print(flexcom)