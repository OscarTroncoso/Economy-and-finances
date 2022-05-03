from typing import Collection, MutableSequence
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

#Crea un DataFrame de Población con 10 Datos
Data = pd.DataFrame()
Data['Population'] = [15,30,100,1,2,53,28,34,46,92]

#Muestra con Repetición 
With = Data['Population'].sample(5, replace= True).sort_index()

#Muestra sin Repetición
Without = Data['Population'].sample(5, replace = False).sort_index()

print(With, Without)

#Estimadora Imparcial
Lenght = 200
Variance_Collection = [[Data['Population'].sample(5, replace=True).var(ddof=1) for i in range(Lenght)]]
 
#Funciones
Mean = Data['Population'].mean()
Var = Data['Population'].var(ddof = 0)
Std = Data['Population'].std(ddof = 0)
Shape = Data['Population'].shape[0]

#Muestra y Distribución Normal
Sample = pd.DataFrame(np.random.normal(10, 5, size= 30))
print('Sample Mean is', Sample[0].mean())
print('Sample STD is', Sample[0].std(ddof= 1))

#Distribución Empírica del Promedio
Meanlist = []
for t in range (10000):
        sample = pd.DataFrame(np.random.normal(10, 5, size=10000))
        Meanlist.append(sample[0].mean())
Colection = pd.DataFrame()
Colection['MeanList'] = Meanlist
Colection['MeanList'].hist(bins= 100,figsize=(10,8))
plt.show()

#Muestra para la Distribución Arbitraria 
Size = 100
Slist = []
apop = pd.DataFrame([1,0,1,0,1,0])
for j in range (10000):
        Sample = apop[0].sample(Size, replace= True)
        Slist.append(Sample.mean())
Acollec = pd.DataFrame()
Acollec['Slist'] = Slist
Acollec['Slist'].hist(bins= 100,figsize=(10,8))
plt.show()

#Llamar a un Archivo .CSV
sp = pd.read_csv('../Python/S&P500.csv')

#Confidence Interval (Estimar el Retorno Promedio)
sp['PrecioF'] = sp['Close'].shift(-1)
sp['LogReturn'] = np.log(sp['PrecioF']) - np.log(sp['Close'])
sp['LogReturn'].hist(bins= 50,figsize=(10,8))
plt.show()

#Hallar el Valor de Alpha/2 para el 80%
Nivel_Conf = 80
Alpha_Left = (100 - Nivel_Conf) / 200
Alpha_Right = 1 - Alpha_Left

#Calcular Z de Alpha / 2
Alpha = (1 - (Nivel_Conf / 100))/2
Z_nAlphaM = 1 - Alpha

#Valores para Calcular el 80% de la Confianza del Intérvalo
z_left = norm.ppf(Alpha_Left)                   #Cuantiles de Distribución
z_right = norm.ppf(Alpha_Right)                 #Cuentiles de Distribución
Sample_Mean = sp['LogReturn'].mean()
Sample_Std = sp['LogReturn'].std(ddof=1)/(sp.shape[0]) ** 0.5 

#Se Calcula el 80% de Rendimiento Promedio de las Acciones
Interval_Left = Sample_Mean + z_left * Sample_Std
Interval_Right = Sample_Mean + z_right * Sample_Std
print('El Promedio de Muestra es', Sample_Mean)
print('El 80% del Intervalo de Confianza es', Interval_Left, Interval_Right)

#Prueba de Hipótesis
        #Hipótesis Nula y Alternativa: La Nula es la posición de la cual estamos en contra y la alternativa es lo que se cree opuesto al Nulo.
        #Se asume al comienzo que la Nula es correcta.
Media_Muestra = sp['LogReturn'].mean()
Std_Muestra = sp['LogReturn'].std(ddof= 1)
Tamaño_Muestra = sp['LogReturn'].shape[0]
Media_Poblacion = 0 

#Standarización
Z_Hat = (Media_Muestra - Media_Poblacion) / (Std_Muestra / (Tamaño_Muestra ** 0.5))
print(Z_Hat) #Si el valor de Z_Hat es diferente de cero significativamente se rechaza la hipótesis Nula porque no está muestreada para la Media de Población = 0 

#Criterio de Desición ó Nivel de Significación
#Si cae sobre las colas o el margen de rechazo se puede decir que las estadísticas están lejos de 0 y se puede rechazar la hipótesis Nula.
#Error tipo 1 = La porbabilidad del error es igual al nivel de significancia o alpha.
Porcentaje = 5
Alpha = Porcentaje / 100
zleft = norm.ppf(Alpha/2,0,1)
zright = -zleft
print(z_left,z_right)
print('En el nivel de significancia es del %', Porcentaje)
print('¿Debería Rechazarce?', Z_Hat>zright or Z_Hat<zleft)      #True = Rechazo a la Nula, False = No se Rechaza la Nula

#Prueba de la Cola
Porcentaje = 5
Alpha = Porcentaje / 100
zright = norm.ppf(1 - Alpha,0,1)
print(z_right)
print('En el nivel de significancia es del %', Porcentaje)
print('¿Debería Rechazarce?', Z_Hat>zright)

#Nivel de Significación
Porcentaje = 5
Alpha = Porcentaje / 100
Población = 1- (norm.cdf(abs(Z_Hat), 0 , 1))
print('En el nivel de significancia es del %', Porcentaje)
print('¿Debería Rechazarce?', Población < Alpha )


