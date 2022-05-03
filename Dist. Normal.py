from os import write
from matplotlib.pyplot import bar
from numpy.core.arrayprint import printoptions
from typing import Collection, MutableSequence
from scipy import stats 
from pandas.core.frame import DataFrame
from scipy.stats import norm 
from numpy import random 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Parámetros dados en el ejercicio.          #Distribution Quantiles 
px1 = 0.1               #Evento menor
px2 = 10               #Evento mayor 
mu = 0                 #Parámetros del ejercicio
sigma = 1               #Parámetros del ejercicio
Prob = 0.1           #En caso de tener la probabilidad de x a la izquierda de la normal
Aq = 0                  #Cantidad adicional al valor de x teniendo la probabilidad 


#Px1
#Cálculos para la distribución tomando valores aleatorios de un intérvalo con 1M de iteraciones
z1 = (px1-mu)/sigma                                       #P(X<=>x) = P(z <=> (px-mu)/sigma)
z2 = (px2-mu)/sigma
i = 0
s = 0
while(i<1000000):
    r = np.random.normal(0,1) 
    if(r<=z1):
        s = s+1
    i = i+1
s = float(s)
Pleft = (s/1000000)
Pright = 1-Pleft
print('Iteraciones: La P(x<={}) es {}% y la P(x>={}) es {}%'.format(px1,Pleft*100,px1,Pright*100))

#Cálculo exacto de la probabilidad de un evento sin iteración. 
Pleft1 = norm.cdf(z1)                                     #CDF es la función cuyos valores y representan la probabilidad de que una variable aleatoria tome los valores menores o iguales al valor x. (F. Distribución Acumulativa)
Pright1 = 1 - Pleft1                                        #x función inversa a cdf(x). Nos permite obtener el valor correspondiente a una probabilidad.
print('La P(x<={}) es {}% y la P(x>={}) es {}%'.format(px1,Pleft1*100,px1,Pright1*100))
Pleft2 = norm.cdf(z2) 
Pright2 = 1 - Pleft2
print('La P(x<={}) es {}% y la P(x>={}) es {}%'.format(px2,Pleft2*100,px2,Pright2*100))
Pdif = Pleft2 - Pleft1
print('La P({}<=x<={}) es {}%'.format(px1,px2,Pdif*100))

#Calcular el valor de x con el valor de la probabilidad
Probx = norm.ppf(Prob, mu, sigma)                       #A menos de que se le indique un valor de mu y sigma este toma valores de 0 y 1
print('La P(x<={}%) es {}%'.format(Prob*100, Probx))
Prob2 = 1-Prob
Probx2 = 100-Probx
print('La P(x>={}%) es {}%'.format(Prob2*100,Probx2))

#Cantidad de puntos adicionales al calculo del valor de x con el valor de la probabilidad
Probx3 = Probx + Aq
Probx3_1 = norm.cdf(Probx3,mu,sigma) 
Probx3_2 = 1 - Probx3_1
print('La P(x<={}% + {}) es {}%'. format(Prob*100, Aq, Probx3_2*100))
print('La P(x>={}% + {}) es {}%'. format(Prob2*100, Aq, Probx3_1*100))

#Parte gráfica con valores px. 
normal = stats.norm(mu, sigma)
x = np.linspace(normal.ppf(0.01),
                normal.ppf(0.99), 100)
fp = normal.pdf(x)                                        #Función de Probabilidad
plt.plot(x, fp)
plt.title('Distribución Normal Valores Px_#')
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
plt.show()

#Parte gráfica con valores z.
x = np.arange(z1,z2,0.0001)
x2 = np.arange(-5,5,0.0001)
y = norm.pdf(x,0,1)
y2 = norm.pdf(x2,0,1)
fig,ax = plt.subplots(figsize=(9,6))
plt.style.use("fivethirtyeight")
ax.plot(x2,y2)
ax.fill_between(x,y,0,color="g")
ax.fill_between(x2,y2,0,alpha=0.1)
ax.set_xlim([-4,4])
ax.set_xlabel("Valores")
ax.set_ylabel("Probabilidades")
ax.set_title("Distribución Normal Valores Z")
plt.show()


