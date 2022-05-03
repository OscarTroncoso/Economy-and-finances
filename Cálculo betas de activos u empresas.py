from operator import index
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf 
# import plotly.graph_objects as go
from pandas_datareader import data as pdr

##### ######################## #####
##### Estimación de Betas (^^) #####
##### ######################## #####

yf.pdr_override()

#Variables Iniciales
Stocks = ['ZM', 'TSLA', 'NVDA', 'MSFT', 'FB', 'GME', 'GD', 'HAL', 'HOG', 'HIG']                     #Nemotécnico de los activos
Stockm = ['SPY']                                    #Nemotécnico de los activos
Star_date1 = '2015-01-01'                            #Formato yy/mm/dd
End_date1 = '2019-11-01'                             #Formato yy/mm/dd
Star_date2 = '2019-11-02'                            #Formato yy/mm/dd
End_date2 = '2022-03-09'                             #Formato yy/mm/dd

#Variables Betas
T = 0.21                                          #Tasa de impuesto de USA para las empresas
DE = pd.read_csv('../Banca de Inversión/Bdata.csv')     #Los datos de las variables son llamados desde el .csv 

#Variación pre - pandemia
Activos = Stocks + Stockm
Df1 = pd.DataFrame()
for Activo in Activos:
        Df_Activo1 = pdr.get_data_yahoo(Activo, start = Star_date1, end = End_date1)['Adj Close']
        Df_Activo1 = Df_Activo1.to_frame(name = Activo)
        Df1 = pd.concat([Df_Activo1, Df1], axis = 1, sort = False)
Df1 = Df1.dropna()
Df1 = Df1.pct_change().dropna()
Me1 = Df1.mean()
Me1 = Me1.drop(Me1.index[[0]])

#Variación pandemia
Df2 = pd.DataFrame()
for Activo in Activos:
        Df_Activo2 = pdr.get_data_yahoo(Activo, start = Star_date2, end = End_date2)['Adj Close']
        Df_Activo2 = Df_Activo2.to_frame(name = Activo)
        Df2 = pd.concat([Df_Activo2, Df2], axis = 1, sort = False)
Df2 = Df2.dropna()
Df2 = Df2.pct_change().dropna()
Me2 = Df2.mean()
Me2 = Me2.drop(Me2.index[[0]])

#Varianzas y covarianzas pre - pandemia
Cov = Df1.cov() * len(Df1)
Varm = Cov.iloc[0, 0] 

#Betas Apalancado pre - pandemia
Betae = []
for i in range(1, len(Df1.columns)):
    Betas = Cov.iloc[0, i]/Varm
    Betae.append((Betas))
Beta1 = pd.DataFrame(Betae, index = Stocks[::-1], columns = ['Beta apalancado pre'])

# print('Los betas apalancados pre - pandemia son: {}' .format(Beta1))

#Varianzas y covarianzas pandemia
Cov2 = Df2.cov() * len(Df2)
Varm2 = Cov2.iloc[0, 0] 

#Betas Apalancado pandemia
Betai = []
for i in range(1, len(Df2.columns)):
    Betas = Cov2.iloc[0, i]/Varm2
    Betai.append((Betas))
Beta2 = pd.DataFrame(Betai, index = Stocks[::-1], columns = ['Beta apalancado pan'])

# print('Los betas apalancados en pandemia son: {}' .format(Beta2))

#Beta Hamada desapalancada pre pandemia
Btu1 = []
for i in range(0, len(Beta1)):
    Betau1 = Beta1.iloc[i, 0] / (1 + (1 - T) * (DE.iloc[i, 1]))
    Btu1.append((Betau1))
Bhu1 = pd.DataFrame(Btu1, index = Stocks[::-1], columns = ['Beta u Hamada pre'])

# print('Los betas desapalancados por Hamada son: {}' .format(Bhu1))

#Beta Hamada desapalancada pandemia
Btu2 = []
for i in range(0, len(Beta2)):
    Betau2 = Beta2.iloc[i, 0] / (1 + (1 - T) * (DE.iloc[i, 1]))
    Btu2.append((Betau2))
Bhu2 = pd.DataFrame(Btu2, index = Stocks[::-1], columns = ['Beta u Hamada pan'])

# print('Los betas desapalancados por Hamada son: {}' .format(Bhu2))

#Beta desapalancado Miles - Ezzel pre - pandemia
Btu3 = []
for i in range(0, len(Beta1)):
    Betau3 = ((Me1.iloc[i] * Beta1.iloc[i, 0]) + DE.iloc[i, 3] * DE.iloc[i, 4] * (1 - ((T * DE.iloc[i, 2]) / (1 + DE.iloc[i, 2])))) / (Me1.iloc[i] + DE.iloc[i, 3] * (1 - ((T * DE.iloc[i, 2]) / (1 + DE.iloc[i, 2]))))
    Btu3.append(Betau3)
Bmu1 = pd.DataFrame(Btu3, index = Stocks[::-1], columns = ['Beta u Miles pre'])

# print('Los betas desapalancados por Miles son: {}' .format(Bmu1))

#Beta desapalancado Miles - Ezzel pandemia
Btu4 = []
for i in range(0, len(Beta2)):
    Betau4 = ((Me2.iloc[i] * Beta2.iloc[i, 0]) + DE.iloc[i, 3] * DE.iloc[i, 4] * (1 - ((T * DE.iloc[i, 2]) / (1 + DE.iloc[i, 2])))) / (Me2.iloc[i] + DE.iloc[i, 3] * (1 - ((T * DE.iloc[i, 2]) / (1 + DE.iloc[i, 2]))))
    Btu4.append(Betau4)
Bmu2 = pd.DataFrame(Btu4, index = Stocks[::-1], columns = ['Beta u Miles pan'])

# print('Los betas desapalancados por Miles son: {}' .format(Bmu2))

#Beta desapalancado Harris Pringle pre - pandemia
Btu5 = []
for i in range(0, len(Beta1)):
    Betau5 = (Beta1.iloc[i , 0] + DE.iloc[i, 4] * DE.iloc[i, 1]) / (1 + DE.iloc[i, 1])
    Btu5.append(Betau5)
Bhpu1 = pd.DataFrame(Btu5, index = Stocks[::-1], columns = ['Beta u Harris pre'])

# print('Los betas desapalancados por Harris son: {}' .format(Bhpu1))

#Beta desapalancado Harris Pringle pre - pandemia
Btu6 = []
for i in range(0, len(Beta2)):
    Betau6 = (Beta2.iloc[i , 0] + DE.iloc[i, 4] * DE.iloc[i, 1]) / (1 + DE.iloc[i, 1])
    Btu6.append(Betau6)
Bhpu2 = pd.DataFrame(Btu6, index = Stocks[::-1], columns = ['Beta u Harris pan'])

# print('Los betas desapalancados por Harris son: {}' .format(Bhpu2))


#Beta desapalancado Practicioners Method pre - pandemia
Btu7 = []
for i in range(0, len(Beta1)):
    Betau7 = Beta1.iloc[i, 0] / (1 + (DE.iloc[i, 1]))
    Btu7.append((Betau7))
Bpu1 = pd.DataFrame(Btu7, index = Stocks[::-1], columns = ['Beta u Practicioners M. pre'])

# print('Los betas desapalancados por Practicioners M. son: {}' .format(Bpu1))

#Beta desalpalancado Practicioners Method pandemia
Btu8 = []
for i in range(0, len(Beta2)):
    Betau8 = Beta2.iloc[i, 0] / (1 + (DE.iloc[i, 1]))
    Btu8.append((Betau8))
Bpu2 = pd.DataFrame(Btu8, index = Stocks[::-1], columns = ['Beta u Practicioners M. pan'])

# print('Los betas desapalancados por Practicioners M. son: {}' .format(Bpu2))

#Beta apalancado Hamada pre - pandemia
Btu9 = []
for i in range(0, len(Beta1)):
    Betau9 = Bhu1.iloc[i, 0] * (1 + (1 - T) * DE.iloc[i, 5])
    Btu9.append((Betau9))
Bhl1 = pd.DataFrame(Btu9, index = Stocks[::-1], columns = ['Beta l Hamada pre'])

# print('Los betas apalancados por Hamada son: {}' .format(Bhl1))

#Beta apalancado Hamada pandemia
Btu10 = []
for i in range(0, len(Beta2)):
    Betau10 = Bhu2.iloc[i, 0] * (1 + (1 - T) * DE.iloc[i, 5])
    Btu10.append((Betau10))
Bhl2 = pd.DataFrame(Btu10, index = Stocks[::-1], columns = ['Beta l Hamada pan'])

# print('Los betas apalancados por Hamada son: {}' .format(Bhl2))

#Beta apalancado Miles - Ezzel pre - pandemia
Btu11 = []
for i in range(0, len(Beta1)):
    Betau11 = Bmu1.iloc[i, 0] + DE.iloc[i, 5] * (Bmu1.iloc[i, 0] * DE.iloc[i, 4]) * ((1 - (T * DE.iloc[i, 2])) / (1 + DE.iloc[i, 2])) 
    Btu11.append((Betau11))
Bml1 = pd.DataFrame(Btu11, index = Stocks[::-1], columns = ['Beta l Miles pre'])

# print('Los betas apalancados por Miles son: {}' .format(Bml1))

#Beta apalancado Miles - Ezzel pandemia
Btu12 = []
for i in range(0, len(Beta2)):
    Betau12 = Bmu2.iloc[i, 0] + DE.iloc[i, 5] * (Bmu2.iloc[i, 0] * DE.iloc[i, 4]) * ((1 - (T * DE.iloc[i, 2])) / (1 + DE.iloc[i, 2])) 
    Btu12.append((Betau12))
Bml2 = pd.DataFrame(Btu12, index = Stocks[::-1], columns = ['Beta l Miles pan'])

# print('Los betas apalancados por Miles son: {}' .format(Bml2))

#Beta apalancado Harris Pringle pre - pandemia
Btu13 = []
for i in range(0, len(Beta1)):
    Betau13 = Bhpu1.iloc[i, 0] + (Bhpu1.iloc[i, 0] - DE.iloc[i, 4]) * DE.iloc[i, 5]
    Btu13.append(Betau13)
Bhpl1 = pd.DataFrame(Btu13, index = Stocks[::-1], columns = ['Beta l Harris pre'])

# print('Los betas apalancados por Harris son: {}' .format(Bhpl1))

#Beta apalancado Harris Pringle pandemia
Btu14 = []
for i in range(0, len(Beta2)):
    Betau14 = Bhpu2.iloc[i, 0] + (Bhpu2.iloc[i, 0] - DE.iloc[i, 4]) * DE.iloc[i, 5]
    Btu14.append(Betau14)
Bhpl2 = pd.DataFrame(Btu14, index = Stocks[::-1], columns = ['Beta l Harris pan'])

# print('Los betas apalancados por Harris son: {}' .format(Bhpl2))

#Beta apalancado Practicioners Method pre - pandemia
Btu15 = []
for i in range(0, len(Beta1)):
    Betau15 = Bpu1.iloc[i, 0] * (1 + DE.iloc[i , 5])
    Btu15.append(Betau15)
Bpl1 = pd.DataFrame(Btu15, index = Stocks[::-1], columns = ['Beta l Practicioners pre'])

# print('Los betas apalancados por Practicioners son: {}' .format(Bpl1))

#Beta apalancado Practicioners Method pandemia
Btu16 = []
for i in range(0, len(Beta2)):
    Betau16 = Bpu2.iloc[i, 0] * (1 + DE.iloc[i , 5])
    Btu16.append(Betau16)
Bpl2 = pd.DataFrame(Btu16, index = Stocks[::-1], columns = ['Beta l Practicioners pan'])

# print('Los betas apalancados por Practicioners son: {}' .format(Bpl2))

#Data Frame de salida
Betaf = pd.DataFrame()
Betaf.loc[:, 'Beta apalancado pre - pandemia'] = Beta1.iloc[:, 0]
Betaf.loc[:, 'Beta apalancado pandemia'] = Beta2.iloc[:, 0]
Betaf.loc[:, 'Beta desapalancado por Hamada pre'] = Bhu1.iloc[:, 0]
Betaf.loc[:, 'Beta desapalancado por Hamada pan'] = Bhu2.iloc[:, 0]
Betaf.loc[:, 'Beta desapalancado por Miles pre'] = Bmu1.iloc[:, 0]
Betaf.loc[:, 'Beta desapalancado por Miles pan'] = Bmu2.iloc[:, 0]
Betaf.loc[:, 'Beta desapalancado por Harris pre'] = Bhpu1.iloc[:, 0]
Betaf.loc[:, 'Beta desapalancado por Harris pan'] = Bhpu2.iloc[:, 0]
Betaf.loc[:, 'Beta desapalancado por Practicioners pre'] = Bpu1.iloc[:, 0]
Betaf.loc[:, 'Beta desapalancado por Practicioners pan'] = Bpu2.iloc[:, 0]
Betaf.loc[:, 'Beta apalancado por Hamada pre'] = Bhl1.iloc[:, 0]
Betaf.loc[:, 'Beta apalancado por Hamada pan'] = Bhl2.iloc[:, 0]
Betaf.loc[:, 'Beta apalancado por Miles pre'] = Bml1.iloc[:, 0]
Betaf.loc[:, 'Beta apalancado por Miles pan'] = Bml2.iloc[:, 0]
Betaf.loc[:, 'Beta apalancado por Harris pre'] = Bhpl1.iloc[:, 0]
Betaf.loc[:, 'Beta apalancado por Harris pan'] = Bhpl2.iloc[:, 0]
Betaf.loc[:, 'Beta apalancado por Practicioners pre'] = Bpl1.iloc[:, 0]
Betaf.loc[:, 'Beta apalancado por Practicioners pan'] = Bpl2.iloc[:, 0]

#Salidas
Writer = pd.ExcelWriter('Betas.xlsx')
Betaf.to_excel(Writer, sheet_name = 'Betas')
Writer.save()