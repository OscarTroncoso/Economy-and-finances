import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf 
import scipy.optimize as op
from pandas_datareader import data as pdr

##### ####################### #####
##### Portafolio de Markowitz #####
##### ####################### #####

#Variables
yf.pdr_override()
Activos = ['SPY', 'AAPL', 'MSFT', 'JPM', 'AMZN']           #Nemotécnico de los activos
Star_date = '2021-01-01'                            #Formato yy/mm/dd
End_date = '2022-01-01'                             #Formato yy/mm/dd
Rf = 0.4                                            #Ingresar el porcentaje sin el %
N_portafolios = 2
T_Mercado = input('El tipo de mercado que busca analizar es de: ')            #Acciones, Forex

#Lectura de los archivos
Df = pd.DataFrame()
for Activo in Activos:
        Df_Activo = pdr.get_data_yahoo(Activo, start = Star_date, end = End_date)['Adj Close']
        Df_Activo = Df_Activo.to_frame(name = Activo)
        Df = pd.concat([Df_Activo, Df], axis = 1, sort = False)
Df = Df.dropna()
Df = Df.pct_change().dropna()

#Cálculos de la frontera eficiente
Weights = []
N_Activos = len(Activos)
for i in range(N_Activos):
    Weights.append(1 / N_Activos)
    
W = np.array(Weights)       
R = np.array(np.mean(Df))   #Rentabilidad de los activos
C = np.cov(Df.transpose())  #Matriz de covarianza

if T_Mercado == 'Acciones': #Saber cuantos dias opera el mercado que desea analizar
    T_Mercado = 250
elif T_Mercado == 'Forex':
    T_Mercado = 360
    
def mu(W, R):               #Retorno esperado del portafolio anualizado
    return sum(W * R * T_Mercado)

def sigma(W, C):            #Std del portafolio anualizado
    return np.dot(W, np.dot(C, W.T)) ** (1/2) * T_Mercado ** (1/2)

Rf = Rf / 100
def sharpe(W):              #Sharpe ratio del portafolio (Rendimiento de la inversion considerando el riesgo)
    return((mu(W, R) - Rf) / sigma(W, C))

def neg_sharpe(W):          #Sharpe ratio negativo
    return -sharpe(W)

def random_ports(n):         #Combinación de portafolios entre retornos y riesgos
    means, stds = [],[]
    for i in range(n):
        rand_w = np.random.rand(len(Activos))
        rand_w = rand_w / sum(rand_w)
        means.append(mu(rand_w, C))
        stds.append(sigma(rand_w, C))
    return means, stds

def apply_sum_constraint(inputs):
    total = 1 - np.sum(inputs)
    return total

my_constraints = ({'type': 'eq', 'fun': apply_sum_constraint})

result = op.minimize(neg_sharpe, W,
                     method = 'SLSQP',          #Minimización por mínimos cuadrados secuenciales 
                     bounds = ((0, 1.0),(0, 1.0),(0, 1.0),(0, 1.0),(0, 1.0)),    #Si desea añadir más de 5 activos es recomendable añadir la cantidad de (0, 1.0)
                     options = {'disp': True},
                     constraints = my_constraints)
Op_W = result['x']

#Gráfica 1
means, stds = random_ports(N_portafolios)
Best_mu = mu(Op_W, R)
Best_sigma = sigma(Op_W, C)
Best_sharpe = sharpe(Op_W)
plt.figure(figsize = (16,8))
plt.plot(stds, means, 'o', markersize = 0.5)
plt.plot(Best_sigma, Best_mu, 'x', markersize = 15)
plt.xlabel('Standar Desviation')
plt.ylabel('Expected Return')
plt.title('Modelo de Markowitz')
# plt.colorbar(cmap = 'plasma', label = 'Sharpe Ratio')
plt.show() 

# #Gráfica 2 
# plt.figure(figsize = (16,8))
# plt.scatter(stds, means, c = np.array(means)/np.array(stds),marker = 'o') 
# plt.grid(True)
# plt.xlabel('Standar Desviation')
# plt.ylabel('Expected Return')
# plt.colorbar(cmap = 'plasma', label = 'Sharpe Ratio')
# plt.show()
# print((means))
# print((stds))
                                
# #Salidas
print('El sharpe ratio del portafolio es: {}' .format(round(sharpe(W), 2)))
print(result)