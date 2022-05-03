import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix 
import statsmodels.formula.api as smf 
import numpy as np
import scipy.stats as stats
pd.options.mode.chained_assignment = None  # default='warn'

#Se Llaman los Archivos de los Indicadores que se van a Utilizar para la Predicción del S&P500
Aord = pd.read_csv('../Python/All Ordinaries (AORD).csv')
Dji = pd.read_csv('../Python/Dow Jones.csv')
Sp = pd.read_csv('../Python/S&P500.csv')
Nasdaq = pd.read_csv('../Python/Nasdaq Index.csv')
Dax = pd.read_csv('../Python/Dax Index.csv')
Nikkei = pd.read_csv('../Python/Nikkei Index.csv')
Spy = pd.read_csv('../Python/SPY Index.csv') 
Cac = pd.read_csv('../Python/Cac40 Index.csv')
Hsi = pd.read_csv('../Python/Hsi Index.csv')

#Se Crea la Columna de Precio Diff para Todos los Archivos 
Inpanel = pd.DataFrame(index = Spy.index)
Inpanel['Aord'] = Aord['Close'] - Aord['Open']
Inpanel['Dji'] = Dji['Open'] - Dji['Open'].shift(1)
Inpanel['Sp'] = Sp['Open'] - Sp['Open'].shift(1)
Inpanel['Nasdaq'] = Nasdaq['Open'] - Nasdaq['Open'].shift(1)
Inpanel['Dax'] = Dax['Open'] - Dax['Open'].shift(1)
Inpanel['Nikkei'] = Nikkei['Close'] - Nikkei['Open']
Inpanel['Spy'] = Spy['Open'].shift(-1) - Spy['Open']
Inpanel['Spy_lag1'] = Inpanel['Spy'].shift(1) 
Inpanel['Cac'] = Cac['Open']  - Cac['Open'].shift(1)
Inpanel['Hsi'] = Hsi['Close'] - Hsi['Open']

Inpanel['Price'] = Spy['Open'] #Se Deja un Registro de Apertura del SPY

#Se Llenan los Valores de NaN 
Inpanel = Inpanel.fillna(method='ffill')
Inpanel = Inpanel.dropna()

#Se Guardan estos Datos en otro Archivo
Inpanel.to_csv('../Python/Indice Panel.csv')

#División de Datos
Train = Inpanel.iloc[-252 : -126, :]
Test = Inpanel.iloc[-126: , :]
print(Train.shape, Test.shape)

#Gráfica de Dispersión por Pares 
Sm = scatter_matrix(Train, figsize=(10,10))
plt.show()

#Calcular la Correlación de Datos
Corr = Train.iloc[:,:-1].corr()['Spy']
print(Corr)

#Construir Modelos de Ecuaciones Lineales
Formula = 'Spy~Spy_lag1 + Sp + Nasdaq + Cac + Dax + Aord + Nikkei + Hsi'
Lm = smf.ols(formula = Formula, data = Train).fit()
Resumen = Lm.summary()
print(Resumen) 
    #Se toma en cuenta Prob(F-statistics) en donde si el valor es < 0.05 se sabe que tiene predicciones útiles
    #P>|t| el valor de p para el nivel de significancia de los predictores individuales 
    
#Predecir en el S&P500
Train['PredictedY'] = Lm.predict(Train)
Test['PredictedY'] = Lm.predict(Test)
plt.scatter(Train['Spy'], Train ['PredictedY'])
plt.show()

#Sobre Ajuste
def adjustedMetric(data, model, model_k, yname):
    data['yhat'] = model.predict(data)
    SST = ((data[yname] - data[yname].mean())**2).sum()
    SSR = ((data['yhat'] - data[yname].mean())**2).sum()
    SSE = ((data[yname] - data['yhat'])**2).sum()
    r2 = SSR/SST
    adjustR2 = 1 - (1-r2)*(data.shape[0] - 1)/(data.shape[0] -model_k -1)
    RMSE = (SSE/(data.shape[0] -model_k -1))**0.5
    return adjustR2, RMSE
print('Adjusted R2 and RMSE on Train is', adjustedMetric(Train, Lm, 9, 'Spy'))
print('Adjusted R2 and RMSE on Test is',adjustedMetric(Test, Lm, 9, 'Spy'))

    #Ambos calculan lo mismo solo que es mejor el de abajo por la manera de ver los datos y compararlos 

#Sobre Ajuste
def assessTable(test, train, model, model_k, yname):
    r2test, RMSEtest = adjustedMetric(test, model, model_k, yname)
    r2train, RMSEtrain = adjustedMetric(train, model, model_k, yname)
    assessment = pd.DataFrame(index=['R2', 'RMSE'], columns=['Train', 'Test'])
    assessment['Train'] = [r2train, RMSEtrain]
    assessment['Test'] = [r2test, RMSEtest]
    return assessment
print(assessTable(Test, Train, Lm, 9, 'Spy'))
    #Si los datos presentados difieren demasiado significa que no se puede aplicar este modelo al mercado real del futuro
    
#Señal de Ganancia, basado en los Datos del Train
Train['Order'] = [1 if sig > 0 else -1 for sig in Train['PredictedY']]
Train['Profit'] = Train['Spy'] * Train['Order']
Train['Wealth'] = Train['Profit'].cumsum()
print('Total profit made in Train is', Train['Profit'].sum())

#Señal de Ganancia, basado en los Datos del Test
Test['Order'] = [1 if sig > 0 else -1 for sig in Test['PredictedY']]
Test['Profit'] = Test['Spy'] * Test['Order'] 
Test['Wealth'] = Test['Profit'].cumsum()
print('Total profit made in Test is', Test['Profit'].sum())

#Ratio de Sharpe: Mide el exceso del retorno por unidad de desviación en un activo invertido 
Train['Wealth1'] = Train['Wealth'] + Train.loc[Train.index[0], 'Price']
Test['Wealth1'] = Test['Wealth'] + Test.loc[Test.index[0], 'Price']
DiasN = 252 #Número de Días que se Negocia Anualmente en USA

    #Para los datos de Train
Train['Return'] = np.log(Train['Wealth'] - np.log(Train['Wealth'].shift(-1)))
DailyR = Train['Return'].dropna()
print('El Radio de Sharpe Diario en Train es', DailyR.mean()/DailyR.std(ddof=1))
print('El Radio de Sharpe Anual en Train es', (DiasN **0.5) * DailyR.mean()/ DailyR.std(ddof=1))
plt.figure(figsize=(10, 10))
plt.title('Performance of Strategy in Train')
plt.plot(Train['Wealth'].values, color='green', label='Signal based strategy')
plt.plot(Train['Spy'].cumsum().values, color='red', label='Buy and Hold strategy')
plt.legend()
plt.show()
    #Para los datos de Test
Test['Return'] = np.log(Test['Wealth'] - np.log(Test['Wealth'].shift(-1)))
DailyR = Test['Return'].dropna()
print('El Radio de Sharpe Diario en Test es', DailyR.mean()/DailyR.std(ddof=1))
print('El Radio de Sharpe Anual en Test es', (DiasN **0.5) * DailyR.mean()/ DailyR.std(ddof=1))
plt.figure(figsize=(10, 10))
plt.title('Performance of Strategy in Train')
plt.plot(Test['Wealth'].values, color='green', label='Signal based strategy')
plt.plot(Test['Spy'].cumsum().values, color='red', label='Buy and Hold strategy')
plt.legend()
plt.show()
#Máximo de Drawdown: El máximo % de reducción en la estrategía desde su pico de ganancia histórico en cada punto del tiempo
                    # El riesgo para casos extremos de perdida de una estrategia
Train['Peak'] = Train['Wealth'].cummax()
Train['Drawdown'] = (Train['Peak'] - Train['Wealth'])/Train['Peak']
print('Maximum Drawdown in Train is {}%'.format( Train['Drawdown'].max() * 100))

Test['Peak'] = Test['Wealth'].cummax()
Test['Drawdown'] = (Test['Peak'] - Test['Wealth'])/Test['Peak']
print('Maximum Drawdown in Test is {}%'.format(Test['Drawdown'].max() * 100))