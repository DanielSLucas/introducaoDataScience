# Curva de Velocidade Zero (Tiago Pinheiro) 
# Linguagem = Python 3.9.5
#
# O Program calcula a CJ do P3C com base 
# no livro do Murray. Os seguintes dados 
# de entrada devem ser fornecidos pelo 
# usuario:
#
# n => movimento medio 
# mu2 (eq.3.2)
# N => numero de pontos 
# CJ => Constante de Jacobi 

#Bibliotecas
import numpy as np
import pylab as P
import math

# Dados de Entrada
k = 1.
mu1=0.1
mu2=0.
mu3=0.45
Lx= 0.5
N=800
size=3.0
CJ=[0,4]

# Calculando L3 e passo de integracao
delta=size/float(N)
L3=1.*((1-mu1-mu3)*(1-mu2)+mu2/2) + Lx*mu1*(1-mu2)

# Criando os vetores x e y
x = np.arange(-size/2.0, size/2.0, delta)
y = np.arange(-size/2.0, size/2.0, delta)
x, y = np.meshgrid(x, y)

# Calculando o CJ
r1=np.sqrt((1-L3+x)**2+y**2)
r2=np.sqrt((Lx-L3+x)**2+y**2)
r3=np.sqrt((x-L3)**2+y**2)
m1=(1-mu2)*(1-mu1-mu3)
m2=mu1*(1-mu2)
m3=mu3*(1-mu2)
z=(x**2+y**2) + 2*k*(m1/r1 + m2/r2 + m3/r3) #+ mu2*np.log((r1+r3+1)/(r1+r3-1)))

# Plotando as curvas
P.figure()
P.title('Curva de Velocidade Zero')
P.xlabel('X')
P.ylabel('Y')
P.xlim(-size/2.0,size/2.0)
P.ylim(-size/2.0,size/2.0)
cb=P.contourf(x,y,z,levels=CJ,extend='max')
P.scatter([-1+L3,L3-Lx,L3],[0,0,0])
label=["M1","M2","M3"]
for i,x in enumerate([-1+L3,L3-Lx,L3]):
   P.text(x+10*delta,-10*delta,label[i])
P.colorbar(cb)
P.show()
