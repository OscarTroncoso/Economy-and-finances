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

#Asignar Valores Dependiendo de su Comportamiento
sp['Direction'] = [1 if sp.loc[i, 'Price Diff'] > 0 else 0 for i in sp.index]

#Crea un Promedio
sp['Average'] = (sp['Close'] + sp['Close'].shift(-1) + sp['Close'].shift(-2))/3

#Crear Dos Promedios Dinámicos de Rango 10 y 20 
sp['MA10'] = sp['Close'].rolling(10).mean()
sp['MA50'] = sp['Close'].rolling(50).mean()

#Crear Lista de Impresión con Variables para 'Date', 'Close', 'Direction', 'Average' y la Gráfica Total
Fila = 21
print('Para la fecha {} las acciones cerraron a un precio de ${} con un valor {} y un promedio dinámico de 10 días ${} y otro de 50 días ${}'.format( sp.iloc[Fila, 0], sp.iloc[Fila, 1], sp.iloc[Fila, 7], sp.iloc[Fila, 9], sp.iloc[Fila, 10]))

#Crear un Archivo Destino Donde se Guarde la Última Tabla Obtenida
plt.figure(figsize=(10,8))
sp['Close'].loc['1/1/2015':'5/22/2015'].plot(label='Close')
sp['MA10'].loc['1/1/2015':'5/22/2015'].plot(label='MA10')
sp['MA50'].loc['1/1/2015':'5/22/2015'].plot(label='MA50')
plt.legend()
plt.show()

#Crea Columna "Shares = Acciones para tomar desiciones basadas en strategia"
sp['Shares'] = [1 if sp.loc[ei, 'MA10'] > sp.loc[ei, 'MA50'] else 0 for ei in sp.index]

#Crea Columna "Profit" Junto con su Impresión
sp['Profit'] = [sp.loc[ei, 'Precio F'] - sp.loc[ei, 'Close'] if sp.loc[ei, 'Shares'] ==1 else 0 for ei in sp.index]
sp['Profit'].plot()
plt.axhline(y=0, color= 'Red')
plt.show()

#Crea Columna para tener la Suma Acumulada 
sp['Wealth'] = sp['Profit'].cumsum()
sp['Wealth'].plot()
plt.title('Total money you win is ${}'.format(sp.loc[sp.index[-2], 'Wealth']))
plt.show()
print(sp.columns)
print(sp.head(60))
print('Total money you win is ${} and the total money that you invested was ${}'.format(sp.loc[sp.index[-2], 'Wealth'], sp.loc[sp.index[0], 'Close']))

#Crea un Archivo para Guardar Datos en específico
file=open('Result Summary Pandas.dat', 'w')
Dos=('Total money you win is ${} and the total money that you invested was {}'.format(sp.loc[sp.index[-2], 'Wealth'], sp.loc[sp.index[0], 'Close']))
Uno=('Para la fecha {} las acciones cerraron a un precio de ${} con un valor {} y un promedio dinámico de 10 días ${} y otro de 50 días ${}'.format( sp.iloc[Fila, 0], sp.iloc[Fila, 1], sp.iloc[Fila, 7], sp.iloc[Fila, 9], sp.iloc[Fila, 10]))
file.write(Uno)
file.write(",")
file.write(Dos)
file.close

