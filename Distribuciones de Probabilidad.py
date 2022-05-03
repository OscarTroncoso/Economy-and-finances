from os import write
from matplotlib.pyplot import bar
from numpy.core.arrayprint import printoptions
from typing import Collection, MutableSequence
from scipy import stats 
from pandas.core.frame import DataFrame
from scipy.stats import norm 
from numpy import random 
from scipy import stats 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as stat

#~Distribución Uniforme~
#Variables
Lambda = 0.95      #Parámetro menor
Theta = 1.05      #Parámetro mayor
Prob1 = 1.02       #Parámetro probabilidad menor
Prob2 = 1.03       #Parámetro probabilidad mayor
Probx = 0.1     #Porcentaje del quantil

#Operaciones
Pleft1 = stats.uniform.cdf(Prob1, Lambda, (Theta - Lambda)) 
Pright1 = 1 - Pleft1
Pleft2 = stats.uniform.cdf(Prob2, Lambda, (Theta - Lambda)) 
Pright2 = 1 - Pleft2
Pleftx = stats.uniform.ppf(Probx, Lambda, (Theta - Lambda))
Ex = (Lambda + Theta)/2
Var = ((Theta - Lambda)**2)/12
Std = np.sqrt(Var)
Pdif = Pleft2 - Pleft1

#Salida
print("~Distribución Uniforme~")
print("La P(x<={}) es {}% y la P(x>={}) es {}%" .format(Prob1, round(Pleft1*100, 4), Prob1, round(Pright1*100, 4)))
print("La P(x<={}) es {}% y la P(x>={}) es {}%" .format(Prob2, round(Pleft2*100, 4), Prob2, round(Pright2*100, 4)))
print('La P({}<=x<={}) es {}%'.format(Prob1,Prob2,Pdif*100))
print('La P(x={}%) es {}'.format(Probx*100, Pleftx))
print('E(x) = {}' .format(round(Ex, 4)))
print('Var(x) = {}' .format(round(Var, 4)))
print('Std(x) = {}' .format(round(Std, 4)))
print()

#~Distribución Bernoulli~
#Variables
P = 1/6        #Probabilidad de éxito
Pob = 1            #Datos éxito

#Operaciones
Pleft = (P**Pob)*((1-P)**(1-Pob))
Pright = 1 - Pleft
Ex = P
Var = P*(1-P)
Std = np.sqrt(Var)

#Salida
print("~Distribución Bernoulli~")
print("La P(x=1) es {}% y la P(x=0) es {}%" .format(round(Pleft*100, 4), round(Pright*100,4)))
print('E(x) = {}' .format(round(Ex, 4)))
print('Var(x) = {}' .format(round(Var, 4)))
print('Std(x) = {}' .format(round(Std, 4)))
print()

#~Distribución Binomial~
#Variables
N = 4       #Total experimentos 
X1 = 1      #Total éxitos menor
X2 = 3       #Total éxitos mayor
P = 0.8     #Probabilidad de éxito

#Operaciones    
Px1 =  stats.binom.cdf(X1, N, P) - stats.binom.cdf(X1-1, N, P)
Pleft1 = stats.binom.cdf(X1, N, P)                 #Cálculo de la probabilidad con <= o >=
Pright1 = 1 - stats.binom.cdf(X1-1, N, P)          #Cálculo de la probabilidad con <= o >=
Pleft11 = stats.binom.cdf(X1-1, N, P)              #Cálculo de la probabilidad con < o >
Pright11 = 1 - stats.binom.cdf(X1, N, P)           #Cálculo de la probabilidad con < o >

Px2 =  stats.binom.cdf(X2, N, P) - stats.binom.cdf(X2-1, N, P) 
Pleft2 = stats.binom.cdf(X2, N, P)                  #Cálculo de la probabilidad con <= o >=
Pright2 = 1 - stats.binom.cdf(X2-1, N, P)          #Cálculo de la probabilidad con <= o >=
Pleft22 = stats.binom.cdf(X2-1, N, P)               #Cálculo de la probabilidad con < o >
Pright22 = 1 - stats.binom.cdf(X2, N, P)           #Cálculo de la probabilidad con < o >

Ex = N*P
Var = N*P*(1-P)
Std = np.sqrt(Var)
Pdif =  stats.binom.cdf(X2, N, P) - stats.binom.cdf(X1-1, N, P) 

#Salida
print("~Distribución Binomial~")
print("La P(x={}) es {}% " .format(X1, round(Px1*100, 4)))
print("La P(x<={}) es {}% y la P(x>={}) es {}%" .format(X1, round(Pleft1*100, 4), X1, round(Pright1*100, 4)))
print("La P(x<{}) es {}% y la P(x>{}) es {}%" .format(X1, round(Pleft11*100, 4), X1, round(Pright11*100, 4)))
print("La P(x={}) es {}% " .format(X2, round(Px2*100, 4)))
print("La P(x<={}) es {}% y la P(x>={}) es {}%" .format(X2, round(Pleft2*100, 4), X2, round(Pright2*100, 4)))
print("La P(x<{}) es {}% y la P(x>{}) es {}%" .format(X2, round(Pleft22*100, 4), X2, round(Pright22*100, 4)))
print('La P({}<=x<={}) es {}%'.format(X1,X2,round(Pdif*100, 4)))
print('E(x) = {}' .format(round(Ex, 4)))
print('Var(x) = {}' .format(round(Var, 4)))
print('Std(x) = {}' .format(round(Std, 4)))
print()

#~Distribución Binomial Negativa~
#Variables

#Operaciones

#Salida
print("~Distribución Binomial Negativa~")

print()

#~Distribución Geométrica~
#Variables

#Operaciones

#Salida
print("~Distribución Geométrica~")

print()

#~Distribución Hipergeométrica~
#Variables

#Operaciones

#Salida
print("~Distribución Hipergeométrica~")

print()

#~Distribución de Poisson~
#Variables
Lambda = 3
X1 = 2
X2 = 2
#Operaciones
Px1 =  stats.binom.cdf(X1, N, P) - stats.binom.cdf(X1-1, N, P)
Pleft1 = stats.binom.cdf(X1, N, P)                 #Cálculo de la probabilidad con <= o >=
Pright1 = 1 - stats.binom.cdf(X1-1, N, P)          #Cálculo de la probabilidad con <= o >=
Pleft11 = stats.binom.cdf(X1-1, N, P)              #Cálculo de la probabilidad con < o >
Pright11 = 1 - stats.binom.cdf(X1, N, P)           #Cálculo de la probabilidad con < o >

Px2 =  stats.binom.cdf(X2, N, P) - stats.binom.cdf(X2-1, N, P) 
Pleft2 = stats.binom.cdf(X2, N, P)                  #Cálculo de la probabilidad con <= o >=
Pright2 = 1 - stats.binom.cdf(X2-1, N, P)          #Cálculo de la probabilidad con <= o >=
Pleft22 = stats.binom.cdf(X2-1, N, P)               #Cálculo de la probabilidad con < o >
Pright22 = 1 - stats.binom.cdf(X2, N, P)           #Cálculo de la probabilidad con < o >

Ex = Lambda
Var = Lambda
Std = np.sqrt(Var)
Pdif =  stats.binom.cdf(X2, N, P) - stats.binom.cdf(X1-1, N, P) 

#Salida
print("~Distribución de Poisson~")
print("La P(x={}) es {}% " .format(X1, round(Px1*100, 4)))
print("La P(x<={}) es {}% y la P(x>={}) es {}%" .format(X1, round(Pleft1*100, 4), X1, round(Pright1*100, 4)))
print("La P(x<{}) es {}% y la P(x>{}) es {}%" .format(X1, round(Pleft11*100, 4), X1, round(Pright11*100, 4)))
print("La P(x={}) es {}% " .format(X2, round(Px2*100, 4)))
print("La P(x<={}) es {}% y la P(x>={}) es {}%" .format(X2, round(Pleft2*100, 4), X2, round(Pright2*100, 4)))
print("La P(x<{}) es {}% y la P(x>{}) es {}%" .format(X2, round(Pleft22*100, 4), X2, round(Pright22*100, 4)))
print('La P({}<=x<={}) es {}%'.format(X1,X2,round(Pdif*100, 4)))
print('E(x) = {}' .format(round(Ex, 4)))
print('Var(x) = {}' .format(round(Var, 4)))
print('Std(x) = {}' .format(round(Std, 4)))
print()

#~Distribución Normal~
#Variables
px1 = 3.2               #Evento menor
px2 = 3.4               #Evento mayor 
mu = 3.2                 #Parámetros del ejercicio
sigma = 1.6               #Parámetros del ejercicio
#Variables Intervalos de Confianza
mu1 = 3.2
std1 = 1.6
n = 64
Prob1 = 0.99      #Int. Confianza

#Operaciones
z1 = (px1-mu)/sigma                                       #P(X<=>x) = P(z <=> (px-mu)/sigma)
z2 = (px2-mu)/sigma
Pleft1 = norm.cdf(z1)                                     #CDF es la función cuyos valores y representan la probabilidad de que una variable aleatoria tome los valores menores o iguales al valor x. (F. Distribución Acumulativa)
Pright1 = 1 - Pleft1                                      #x función inversa a cdf(x). Nos permite obtener el valor correspondiente a una probabilidad.
Pleft2 = norm.cdf(z2) 
Pright2 = 1 - Pleft2
Pdif = Pleft2 - Pleft1

    #Calcular el valor de x con el valor de la probabilidad (Int. COnfianza)
Prob = (Prob1/2)+0.5
ProbW = norm.ppf(Prob)
Probx = norm.ppf(Prob1, mu, sigma)                       #A menos de que se le indique un valor de mu y sigma este toma valores de 0 y 1
Xleft = mu1 - ((ProbW * std1)/(np.sqrt(n)))
Xright = mu1 + ((ProbW * std1)/(np.sqrt(n)))
Prob2 = 1-Prob1
Probx2 = 100-Probx

#Salida
print("~Distribución Normal~")
print(ProbW) 
print('La P(x<={}) es {}% y la P(x>={}) es {}%'.format(px1,round(Pleft1*100, 4),px1,round(Pright1*100,4)))
print('La P(x<={}) es {}% y la P(x>={}) es {}%'.format(px2,round(Pleft2*100, 4),px2,round(Pright2*100, 4)))
print('La P({}<=x<={}) es {}%'.format(px1,px2,round(Pdif*100, 4)))
print('La P(x<={}%) es {}'.format(Prob1*100, round(Probx, 4)))
print('La P(x>={}%) es {}'.format(round(Prob2*100,4) ,round(Probx2, 4)))
print('El intérvalo de confianza está entre [{},{}]' .format(round(Xleft, 4), round(Xright, 4)))
print('La probabilidad de que la media muestral esté entre 3.2 y 3.4 es = 34.1346%')
print()

#~Chi Cuadrado~
#Variables
Y1 = 18.3    #Evento 1 (menor)
Y2 = 20      #Evento 2 (mayor)
#Variables del Int. Confianza
Mu = 0
n = 100
Std = 50
Df = n-1         #Grados de libertad
Prob = 0.90      #Valor de la probabilidad

#Operaciones
chi2 = stats.chi2(Df)
x = np.linspace(chi2.ppf(0.01),
                chi2.ppf(0.99), 100)
Fp = chi2.pdf(x)    #Función de Probabilidad
plt.plot(x, Fp)
plt.title('Distribución Chi cuadrado')
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
plt.show()

    #Hallar el valor de la probabilidad % con un valor Y
Pleft1 = stats.chi2.cdf(Y1,Df)
Pright1 = 1 - Pleft1
Pleft2 = stats.chi2.cdf(Y2,Df)
Pright2 = 1 - Pleft2
Pdif = Pleft2 - Pleft1

    #Hallar el valor Y con el valor de la probabilidad xº% (Int. Confianza)
Proba = (Prob/2) + 0.5
ProbY = chi2.ppf(Proba)
Proba1 = 1 - Proba
ProbY1 = chi2.ppf(Proba1)
Xleft = ((Std**2)*(Df))/ProbY
Xright = ((Std**2)*(Df))/ProbY1

#Salida
print("~Distribución Chi Cuadrado~")
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(Y1, round(Pleft1*100, 4), Y1, round(Pright1*100,4)))
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(Y2, round(Pleft2*100, 4), Y2, round(Pright2*100, 4)))
print('La P({}<=x<={}) es {}%'.format(Y2,Y1,round(Pdif*100, 4)))
print('La P(x<={}%) es {}'.format(Prob*100, round(ProbY, 4)))
print('El intérvalo de confianza está entre [{},{}]' .format(round(Xleft, 4), round(Xright, 4)))
print(round(ProbY, 4), round(ProbY1, 4), round(Proba1, 4), round(Proba, 4))
print() 

#~Distribución T~
#Variables
W1 = 2.11   #Evento 1 (menor)
W2 = 3      #Evento 1 (mayor)

#Variables Intervalo de Confianza
Proba = 0.95    #Valor de la probabilidad a la izquierda
Mu = 4000
n = 100
Std = np.sqrt(1000000)
Df = n-1     #Grados de libertad

#Operaciones
t = stats.t(Df)
x = np.linspace(t.ppf(0.01),
                t.ppf(0.99), 100)
fp = t.pdf(x) # Función de Probabilidad
plt.plot(x, fp)
plt.title('Distribución t de Student')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
    #Hallar el valor de la probabilidad % con un valor Y
Pleft1 = stats.t.cdf(W1,Df)
Pright1 = 1 - Pleft1
Pleft2 = stats.t.cdf(W2,Df)
Pright2 = 1 - Pleft2
Pdif = Pleft2 - Pleft1
    #Hallar el valor Y con el valor de la probabilidad % (Int. Confianza)
Prob = (Proba/2)+0.5
ProbZ = t.ppf(Proba)
ProbW = t.ppf(Prob)
Xleft = Mu - ((ProbW * Std)/(np.sqrt(n)))
Xright = Mu + ((ProbW * Std)/(np.sqrt(n)))

#Salida
print("~Distribución T-Student~")
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(W1, round(Pleft1*100, 4), W1, round(Pright1*100,4)))
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(W2, round(Pleft2*100, 4), W2, round(Pright2*100, 4)))
print('La P({}<=x<={}) es {}%'.format(W2,W1,round(Pdif*100, 4)))
print('La P(x<={}%) es {}'.format(Proba*100, round(ProbZ, 4)))
print('La P(x<={}%) es {}'.format(Prob*100, round(ProbW, 4)))
print('El intérvalo de confianza está entre [{},{}]' .format(round(Xleft, 4), round(Xright, 4)))
print()

#~Distribución F~
#Variables
M = 21     #Grados de libertad
N = 21      #Grados de libertad
S1 = 1.96**2   #Evento 1 (menor)(Varianza)
S2 = 2.13**2   #Evento 1 (mayor)(Varianza)
Prob = 0.95     #Valor de la probabilidad

#Operaciones
f = stats.f(M,N)
x = np.linspace(f.ppf(0.01),
                f.ppf(0.99), 100)
fp = f.pdf(x) # Función de Probabilidad
plt.plot(x, fp)
plt.title('Distribución f de Fisher')
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
plt.show()
    #Hallar el valor de la probabilidad % con un valor Y
M1 = M - 1
N2 = N - 1 
Pleft1 = stats.f.cdf(S1,M1,N2)
Pright1 = 1 - Pleft1
Pleft2 = stats.f.cdf(S2,M1,N2)
Pright2 = 1 - Pleft2
Pdif = Pleft2 - Pleft1
    #Hallar el valor Y con el valor de la probabilidad % (Int. Confianza)
ProbV = f.ppf(Prob)


#Salida
print("~Distribución F-Fisher Snedecor~")
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(round(S1, 4), round(Pleft1*100, 4), round(S1, 4), round(Pright1*100,4)))
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(round(S2, 4), round(Pleft2*100, 4), round(S2, 4), round(Pright2*100, 4)))
print('La P({}<=x<={}) es {}%'.format(round(S1, 4),round(S2, 4),round(Pdif*100, 4)))
print('La P(x<={}%) es {}'.format(Prob*100, round(ProbV, 4)))
print()