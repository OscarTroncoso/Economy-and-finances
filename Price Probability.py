from os import write
from matplotlib.pyplot import bar
from numpy.core.arrayprint import printoptions
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

#Llamar a un Archivo .CSV
sp = pd.read_csv('../Python/S&P500.csv')

#Imprimir 5 Datos en Orden
print(sp.head())    #Primeros 5 
print(sp.tail())    #Últimos 5

#Conocer Cantidad de Rows and Columns
print(sp.shape)

#Resumen de los Datos
print(sp.describe())

#Crea Columna con Valor de Precio Futuro
sp['Precio F'] = sp['Close'].shift(-1)

#Crea Columna con la Diferencia de Precios
sp['Price Diff'] = sp['Precio F'] - sp['Close']

#Número Aleatorio (Tomar el Resultado de Lanzar 'x' Cantidad de Dados Una Vez)
Dice = pd.DataFrame([1,2,3,4,5,6])                  #Cantidad de Caras del Dado
Number_Dices = 2
Sum_Dice = Dice.sample(Number_Dices, replace = True).sum().loc[0]
print('Sum of {} Dices is {}'.format(Number_Dices, Sum_Dice))

#Número Aleatiorio (Lanzar 'x' Cantidad de Dados 'y' Veces)
Dice = pd.DataFrame([1,2,3,4,5,6])                  #Cantidad de Caras del Dado
Number_Dices = 2
Number_Trial = 50
Sum_Dice = [Dice.sample(Number_Dices, replace = True).sum().loc[0] for i in range(Number_Trial)]
print(Sum_Dice)

#Frecuencia (Cantidad de Items que Hay por Index)
Freq =  pd.DataFrame(Sum_Dice)[0].value_counts() 
Sort_Freq = Freq.sort_index()
print(Sort_Freq)  
Sort_Freq.plot(kind='bar', color='red', figsize=(10, 8))
plt.show()

#Frecuencia Relativa (Porcentaje por Item en Relación del Total)
Relative_Freq = (Sort_Freq / Number_Trial) * 100 
print(Relative_Freq)  
Relative_Freq.plot(kind='bar', color='red', figsize=(10, 8))
plt.show()

#Tabla de Distribución
X_distri = pd.DataFrame(index=[2,3,4,5,6,7,8,9,10,11,12])
X_distri['#Prob'] = [1,2,3,4,5,6,5,4,3,2,1]
X_distri['Prob'] = X_distri['#Prob'] / 36
print(X_distri)

#Media de la Tabla de Distribución
Media = (X_distri.index * X_distri['Prob']).sum()
print('La Media es', Media)

#Variación de la Tabla de Distribución
Var = (((X_distri.index - Media )** 2)* X_distri['Prob']).sum()
print('La Variación es', Var)

#Se trae libreria para poder operar con PDF y CDF
from scipy.stats import norm 
import numpy as np

#Se Toma el Promedio y la Desviación Standar de Price Diff
#Se toma la resta de sp['Price Diff'] = sp['Precio F'] - sp['Close'] que se hizo anteriormente
MediaP = (sp['Price Diff'].mean())
VarP = (sp['Price Diff'].std(ddof= 1)) 

#Crea un DataFrame para la Densidad 
Density = DataFrame()
Density['x'] = np.arange(sp['Price Diff'].min()-0.1, sp['Price Diff'].max()+0.1, 0.1)
Density['PDF'] = norm.pdf(Density['x'], MediaP, VarP)       #PDF = Funcion de Probabilidad de Densidad

#Retorno Diario de las Acciones
sp['Price Diff'].hist(bins=50, figsize= (10,8)).plot()
plt.plot(Density['x'], Density['PDF'], color= 'red')
plt.show()
#print(Density)

#Calcular la Probabilidad de que las Acciones Caigan un % en un Día 
Drop_Percentaje = -0.05
Prob_Return = norm.cdf(Drop_Percentaje, MediaP, VarP)       #CDF = Función de Distribución Cumulativa 
print('La Probabilidad de que las Acciones Caigan un {} es {}% en un día'.format(Drop_Percentaje, Prob_Return*100))

#Calcular la Probabilidad de que las Acciones Caigan un % en un Año
LaboralD = 220
Porcentaje = 40
Drop_Percentaje = Porcentaje / -100
MediaP220 = LaboralD * MediaP
VarP220 = LaboralD**0.5 * VarP
FDrop =  norm.cdf(Drop_Percentaje, MediaP220, VarP220)
print('La Probabilidad de que las Accciones Caigan un {}% en {} Días es {}%'.format(Porcentaje, LaboralD, FDrop*100))

#Calcular el Riesgo o VAR en un Día
Quantile1 = 0.05
VAR = norm.ppf(Quantile1, MediaP, VarP)
print('El Valor del Riesgo en un Día es %{}'.format(VAR))

#Calcular el Riesgo por Quantiles 
Q1 = 0.25
Q2 = 0.75
VAR1 = norm.ppf(Q1, MediaP, VarP)       
VAR2 = norm.ppf(Q2, MediaP, VarP)
print('El Riesgo en el %{} del Quantil 1 es de %{} y el Riesgo en el %{} del Quantil 2 es de %{}'.format(Q1*100, VAR1*100, Q2*100, VAR2*100))
#Los Valores de los Riesgos en Q1 y Q2 son tan Altos Debido a que por Defectos del Ejercicio la MediaP y VarP son Demasiado Grandes
#Se Recomienda para Enterder Mejor ese Numeral Utilizar:
#VarP = 0.0141918973887
#MediaP = 0.000820231486123
