import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix 
import statsmodels.formula.api as smf 
import numpy as np
import scipy.stats as stats

#Se Llama el Archivo .CSV que se Va a Manejar
bs = pd.read_csv('../Python/Housing Price Boston.csv')

#Se Utiliza la Covariancia para Hallar la Asociación
Cov = bs.cov()

#Se Utiliza la Correlación para Halla la Asociación que es Más Adecuada en esta Situación
Corr = bs.corr()

#Grafica la Relación de los Datos Medidas en Dos Variables
Sm = scatter_matrix(bs, figsize = (10,10))

#La Asociación entre MEDV y LSTAT
#Por la Falta de Datos se ven así las Gráficas
bs.plot(kind = 'scatter' , x = 'LSTAT', y = 'MEDV',figsize = (10,10))
plt.show()

#Para los Modelos de Regresión Lineal Simple se Asume 
    #Lienalidad 
    #Independencia: Con Diferentes X las Respuestas son Diferentes
    #Normalidad: El Ruido Aleatorio y el eje Y siguend Distribuciones Normales
    #Equal Variance: La Varianza es Igual Incluso si los Predictores son Diferentes
        #b_1 = Valor Estimado de la Pendiente
  
#Estimar los Parámetros del Modelo para Generar la Salida Esperada
b0 = 1
b1 = 2
bs['GuessResponse'] = b0 + b1 * bs['RM']

#Conocer el Error de la Salida Esperada
bs['ObservedError'] = bs['MEDV'] - bs['GuessResponse']

#Graficar la Salida Esperada y Saber el Valor del Error de la Suma de los Cuadrados
plt.figure(figsize=(10, 10))
plt.title('El Error de la Suma de los Cuadrados es {}'.format((((bs['ObservedError'])**2)).sum()))
plt.scatter(bs['RM'], bs['MEDV'], color='g', label='Observed')
plt.plot(bs['RM'], bs['GuessResponse'], color='red', label='GuessResponse')
plt.legend()
plt.xlim(bs['RM'].min()-2, bs['RM'].max()+2)
plt.ylim(bs['MEDV'].min()-2, bs['MEDV'].max()+2)
plt.show()

#Estimar los Parámetros del Modelo para Generar la Mejor Salida
model = smf.ols(formula='MEDV~RM', data=bs).fit()    #OLS = Estimación Mínima Cuadrada Ordinaria
b0_ols = model.params[0]     #Params = Indica Cuál Columna es la Respuesta o Predictores
b1_ols = model.params[1]
bs['BestResponse'] = b0_ols + b1_ols * bs['RM']

#Conocer el Error de la Mejor Salida
bs['BestError'] = bs['MEDV'] - bs['BestResponse']

#Graficar la Mejor Saber el Valor del Error de la Suma de los Cuadrados 
plt.figure(figsize=(10, 10))
plt.title('El Error de la Suma de los Cuadrados es {}'.format((((bs['BestError'])**2)).sum()))
plt.scatter(bs['RM'], bs['MEDV'], color='g', label='Observed')
plt.plot(bs['RM'], bs['GuessResponse'], color='red', label='GuessResponse')
plt.plot(bs['RM'], bs['BestResponse'], color='blue', label='BestResponse')
plt.legend()
plt.xlim(bs['RM'].min()-2, bs['RM'].max()+2)
plt.ylim(bs['MEDV'].min()-2, bs['MEDV'].max()+2)
plt.show()

#Resumen de la Tabla 
    #R-Squared: Es una Medida Importante del Rendimiento del Modelo
    #R- Squared Quiere Decir: El 47.9% de las Variaciones del MEDV pueden ser explicadas por el Modelo  
        #Si R-Squared está por debajo del 50% implica que el precio medio no está determinado exclusivamente por el número de filas
        #R-Squared ya es suficientemente alto (48%) para generar ganancias en el comercio
        #P es el valor de la pendiente
        #Los 2 datos al lado de P son el impacto estimado de RM en MEDV 
Resumen = model.summary()
print(Resumen)

#Para Realizar un Diagnóstico se Debe Demostrar:
    #1. Linealidad: El gráfico de dispersión se asemeje a un función lineal mx+b
    #2. Independencia: Se debe demostrar que el error observado es idependiente mutuamente graficando: y luego realizando una prueba de Durbin - Watson que se ve en el summary
bs['Error'] = bs['MEDV'] - bs['BestResponse']
plt.figure(figsize= (15,8))
plt.title('Residual vs Order')
plt.plot(bs.index, bs['Error'], color = 'purple')
plt.axhline(y=0, color = 'red')
plt.show() 
    #Durbin Watson: Se considera normal el error entre 1.5 y 2.5 (bien), si es menor a 1.5 se correlacionan positivamente (mal) y si es mayor a 2.5 se correlacionan negativamente (mal)
    #3. Normalidad: Comparar la distribución del error estandarizado con la distribución normal buscando que estén casi una encima de la otra sin mucha desviación
Normal = (bs['Error'] - bs['Error'].mean()) / bs['Error'].std(ddof= 1)
stats.probplot( Normal, dist='norm', plot = plt)
plt.title('Normal Q-Q plot')
plt.show()
    #4. Varianza Igual: Si la varianza de ruido es igual al predictor de varianza no debería tener un patrón
bs.plot(kind = 'scatter', x = 'RM', y = 'Error', figsize=(10,8), color='green')
plt.title('Residual vs Predictor')
plt.axhline(y=0, color='red')
plt.show()
#Si se Viola Alguna de las Suposiciones:
    #No se puede hacer una inferencia estadística como probar le intervalo de confianza 
    #Se puede utilizar para hacer predicciones 
    #La presición y consistencia no están reacionados a los supuestos