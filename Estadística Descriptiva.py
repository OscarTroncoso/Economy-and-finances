import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statistics as stat
from scipy import stats 

#~Estadística Descriptiva~
#Llamar a un Archivo .CSV
EA = pd.read_csv('../F. Estadística Aplicada/Ejercicio 2.csv')

#Operaciones
Mean = EA['Porcentaje de desempleo'].mean()
Var = EA['Esperanza de vida al nacer, total (años)'].var(ddof= 1) #Hace que el denominador sea n-1
Std = np.sqrt(Var)
Range = EA.iloc[np.argmax(EA['Porcentaje de desempleo']),1] - EA.iloc[np.argmin(EA['Porcentaje de desempleo']),1]
Mo = stat.mode(EA['Porcentaje de desempleo'])
Md = np.median(EA['Porcentaje de desempleo'])

#Salida
print('El promedio es {}' .format(round(Mean, 4)))
print('La varianza es {} y la desviación estandar es {}' .format(round(Var, 4), round(Std, 4)))
print('El rango es {}' .format(round(Range, 4)))
print('La moda es {} y la mediana es {}' .format(round(Mo, 4), round(Md, 4)))   

#~Máxima Verosimilitud (D. Bernoulli)~
#Llamar a un Archivo .CSV
BN = pd.read_csv('../F. Estadística Aplicada/Ejercicio 1.csv')

#Operaciones
#Ex_i = EA['Cancelación suscripción'].sum()
#n = EA['Cancelación suscripción'].count()
#p1 = Ex_i
#p2 = n - Ex_i   #1-p      
#Mv = BN.loc[p1-1, 'P.Muestra']  #Saca error si p1 y p2 exceden el rango de la probabilidad = 1

#Salida
#print('El exponente de p es {} y de 1-p es {}' .format(p1/10 ,p2/10))
#print('El estimador de máxima verosimilitud es {}' .format(Mv))

#~Chi Cuadrado~
#Variables
Df = 149     #Grados de libertad
Y1 = 18.3    #Evento 1 (menor)
Y2 = 20      #Evento 2 (mayor)
Prob = 0.05      #Valor de la probabilidad

#Operaciones
chi2 = stats.chi2(Df)
x = np.linspace(chi2.ppf(0.01),
                chi2.ppf(0.99), 100)
Fp = chi2.pdf(x)    #Función de Probabilidad
plt.plot(x, Fp)
plt.title('Distribución Chi cuadrado')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()

    #Hallar el valor de la probabilidad % con un valor Y
Pleft1 = stats.chi2.cdf(Y1,Df)
Pright1 = 1 - Pleft1
Pleft2 = stats.chi2.cdf(Y2,Df)
Pright2 = 1 - Pleft2
Pdif = Pleft2 - Pleft1

    #Hallar el valor Y con el valor de la probabilidad %
ProbY = chi2.ppf(Prob)

#Salida
print("~Distribución Chi Cuadrado~")
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(Y1, round(Pleft1*100, 4), Y1, round(Pright1*100,4)))
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(Y2, round(Pleft2*100, 4), Y2, round(Pright2*100, 4)))
print('La P({}<=x<={}) es {}%'.format(Y2,Y1,round(Pdif*100, 4)))
print('La P(x<={}%) es {}'.format(Prob*100, round(ProbY, 4)))

#~Distribución T~
#Variables
Df = 149     #Grados de libertad
W1 = 2.11   #Evento 1 (menor)
W2 = 3      #Evento 1 (mayor)

#Variables Intervalo de Confianza
Proba = 0.8    #Valor de la probabilidad a la izquierda
Mu = 2540000
n = 15
Std = 860000

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
ProbW = t.ppf(Prob)
Xleft = Mu - ((ProbW * Std)/(np.sqrt(n)))
Xright = Mu + ((ProbW * Std)/(np.sqrt(n)))

#Salida
print("~Distribución T-Student~")
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(W1, round(Pleft1*100, 4), W1, round(Pright1*100,4)))
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(W2, round(Pleft2*100, 4), W2, round(Pright2*100, 4)))
print('La P({}<=x<={}) es {}%'.format(W2,W1,round(Pdif*100, 4)))
print('La P(x<={}%) es {}'.format(Prob*100, round(ProbW, 4)))
print('El intérvalo de confianza está entre [{},{}]' .format(Xleft, Xright))

#~Distribución F~
#Variables
M = 15     #Grados de libertad
N = 35      #Grados de libertad
V1 = 4.73   #Evento 1 (menor)
V2 = 5      #Evento 1 (mayor)
Prob = 0.99     #Valor de la probabilidad

#Operaciones
f = stats.f(M,N)
x = np.linspace(f.ppf(0.01),
                f.ppf(0.99), 100)
fp = f.pdf(x) # Función de Probabilidad
plt.plot(x, fp)
plt.title('Distribución f de Fisher')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
    #Hallar el valor de la probabilidad % con un valor Y
Pleft1 = stats.f.cdf(V1,M,N)
Pright1 = 1 - Pleft1
Pleft2 = stats.f.cdf(V2,M,N)
Pright2 = 1 - Pleft2
Pdif = Pleft2 - Pleft1
    #Hallar el valor Y con el valor de la probabilidad %
ProbV = f.ppf(Prob)

#Salida
print("~Distribución F-Fisher Snedecor~")
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(V1, round(Pleft1*100, 4), V1, round(Pright1*100,4)))
print('La P(x<={}) es {}% y la P(x>={}) es {}%' .format(V2, round(Pleft2*100, 4), V2, round(Pright2*100, 4)))
print('La P({}<=x<={}) es {}%'.format(V2,V1,round(Pdif*100, 4)))
print('La P(x<={}%) es {}'.format(Prob*100, round(ProbV, 4)))