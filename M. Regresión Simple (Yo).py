from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Abrir Archivo
Dat = pd.read_csv('../Microeconometría/DataMLRM.csv')
pfile = open('Regresión Lineal.txt', 'w')

#Variables
X = 10                                                                       #Cuando nos dan el valor de x hallar cuanto es Y
NX = 'Educación'                                                              #Nombre del eje x
NY = 'Salario'                                                               #Nombre del eje y

#Operaciones
n = len(Dat)
XY = Dat['x1'] * Dat['y']                                                    #Se multiplica las columnas del archivo .csv
X2 = Dat['x1'] ** 2                                  
Y2 = Dat['y'] ** 2
Xb = Dat['x1'].mean()
Yb = Dat['y'].mean()
  
#Ecuaciones
B2 = (sum(XY) - n * Xb * Yb)/(sum(X2) - n * Xb ** 2)                        #Pendiente
B1 = Yb - B2 * Xb                                                           #Punto de corte
S = np.sqrt((sum(Y2) - B1 * sum(np.sqrt(Y2)) - B2 * sum(XY)) / (n - 2))     #Error estandar de la estimación
r = (n * sum(XY) - sum(np.sqrt(X2)) * sum(np.sqrt(Y2))) / (np.sqrt((n * sum(X2) - (sum(np.sqrt(X2)) ** 2)) * (n * sum(Y2) - (sum(np.sqrt(Y2)) ** 2))))      #Correlación de Pearson
ra = r ** 2

#Salidas
print('Modelo de Regresión Lineal')
print('La ecuación de la recta es: {}x + {}' .format(B2,B1))
print("Tomando el valor dado de X, Y es:", (np.round(B2 * X + B1)))
print("El término de perturbación es:", (np.round(S , 4)))
print("El coeficiente de correlación es:", (np.round(r , 4)))
print("El ajuste del modelo a la variable que se intenta explicar ({}) es de {}%" .format(NY, np.round(ra * 100, 4)))

#Gráfica
plt.plot(X, B2)
plt.plot((0, X), (B1, (B1 + B2 * X)), color = 'm', linestyle= "--")
plt.scatter(Dat['x1'], Dat['y'], c = "blue")                                 #Diagrama de dispersión color ponerle ycomo desea que esten los puntos 
plt.xlabel('Label X ({})' .format(NX))                                      #Nombrar el eje x
plt.ylabel('Label Y ({})' .format(NY))                                      #Nombrar el eje Y
plt.title("Regresión Líneal")                                               #Título del Gráfico
plt.grid(True)
plt.show()