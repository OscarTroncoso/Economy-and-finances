# Tratamiento de datos
# ==============================================================================
import pandas as pd
import numpy as np
import os

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

# Preprocesado y modelado
# ==============================================================================
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from scipy import stats

# Configuración matplotlib
# ==============================================================================
plt.rcParams['image.cmap'] = "bwr"
#plt.rcParams['figure.dpi'] = "100"
plt.rcParams['savefig.bbox'] = "tight"
style.use('ggplot') or plt.style.use('ggplot')

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')
# ==============================================================================

#Variables
Columnas = ['x1']
Columna_exc = ['x1']
Alpha = 0.5

#Abrir Archivos
Dat = pd.read_csv('../Microeconometría/DataMLRM.csv')
Ans = open("../Microeconometría/AnswerMLRM.txt", 'w')

# Correlación entre columnas numéricas
X = Dat[Columnas]
y = Dat['y']

X_train, X_test, y_train, y_test = train_test_split(
                                        X,
                                        y.values.reshape(-1,1),
                                        train_size   = 0.8,
                                        random_state = 1234,
                                        shuffle      = True)
X_train = sm.add_constant(X_train, prepend=True)
modelo1 = sm.OLS(endog=y_train, exog=X_train,)
modelo1 = modelo1.fit()

# Se elimina la columna periodico del conjunto de train y test
X_train = X_train.drop(columns = Columna_exc)
X_test  = X_test.drop(columns = Columna_exc)

# A la matriz de predictores se le tiene que añadir una columna de 1s para el
# intercepto del modelo
X_train = sm.add_constant(X_train, prepend=True)
modelo2  = sm.OLS(endog=y_train, exog=X_train,)
modelo2  = modelo2.fit()

# Intervalos de confianza para los coeficientes del modelo
intervalos_ci = modelo2.conf_int(alpha=0.05)         #Distribución normal estandar a dos colas
intervalos_ci.columns = ['2.5%', '97.5%']

# Diagnóstico errores (residuos) de las predicciones de entrenamiento
y_train = y_train.flatten()
prediccion_train = modelo2.predict(exog = X_train)
residuos_train   = prediccion_train - y_train

# Normalidad de los residuos Shapiro-Wilk test
shapiro_test = stats.shapiro(residuos_train)

# Normalidad de los residuos D'Agostino's K-squared test
k2, p_value = stats.normaltest(residuos_train)

# Predicciones con intervalo de confianza 
predicciones = modelo2.get_prediction(exog = X_train).summary_frame(alpha=0.05)

# Error de test del modelo 
X_test = sm.add_constant(X_test, prepend=True)
predicciones = modelo2.predict(exog = X_test)
rmse = mean_squared_error(
        y_true  = y_test,
        y_pred  = predicciones,
        squared = False
       )

#Salidas
Ans.write('Regresión de minimos cuadrados ordinarios' + os.linesep)
Ans.write(str(modelo1.summary()) + os.linesep)
Ans.write('Regresión de minimos cuadrados ordinarios excluyendo una variable dado su p - value' + os.linesep)
Ans.write(str(modelo2.summary()) + os.linesep)
Ans.write('Predicciones con intervalo de confianza ' + os.linesep)
Ans.write(str(predicciones.head(5)) + os.linesep)
Ans.write('Intervalos de confianza del modelo' + os.linesep)
Ans.write(str(intervalos_ci) + os.linesep)
Ans.write('Normalidad de los residuos Shapiro-Wilk test' + os.linesep)
Ans.write(str(shapiro_test) + os.linesep)
Ans.write('Normalidad de los residuos DAgostino K-squared test' + os.linesep)
Ans.write(str(f"Estadítico= {k2}, p-value = {p_value}") + os.linesep)
Ans.write('Error de test del modelo' + os.linesep)
Ans.write(str(f"El error (rmse) de test es: {rmse}") + os.linesep)
Ans.close()


# Gráficos
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(9, 8))

axes[0, 0].scatter(y_train, prediccion_train, edgecolors=(0, 0, 0), alpha = 0.4)
axes[0, 0].plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()],
                'k--', color = 'black', lw=2)
axes[0, 0].set_title('Estimado vs Poblacional', fontsize = 10, fontweight = "bold")
axes[0, 0].set_xlabel('Datos Muestrales')
axes[0, 0].set_ylabel('Estimación')
axes[0, 0].tick_params(labelsize = 7)
############################################################################################
axes[0, 1].scatter(list(range(len(y_train))), residuos_train,
                   edgecolors=(0, 0, 0), alpha = 0.4)
axes[0, 1].axhline(y = 0, linestyle = '--', color = 'black', lw=2)
axes[0, 1].set_title('Residuos del modelo', fontsize = 10, fontweight = "bold")
axes[0, 1].set_xlabel('Media = 0')
axes[0, 1].set_ylabel('Residuos')
axes[0, 1].tick_params(labelsize = 7)
############################################################################################
sns.histplot(
    data    = residuos_train,
    stat    = "density",
    kde     = True,
    line_kws= {'linewidth': 1},
    color   = "firebrick",
    alpha   = 0.3,
    ax      = axes[1, 0]
)

axes[1, 0].set_title('Distribución de los residuos del modelo', fontsize = 10,
                     fontweight = "bold")
axes[1, 0].set_xlabel("Residuo")
axes[1, 0].tick_params(labelsize = 7)
############################################################################################
sm.qqplot(
    residuos_train,
    fit   = True,
    line  = 'q',
    ax    = axes[1, 1], 
    color = 'firebrick',
    alpha = 0.4,
    lw    = 2
)
axes[1, 1].set_title('Q-Q residuos del modelo', fontsize = 10, fontweight = "bold")
axes[1, 1].tick_params(labelsize = 7)

axes[2, 0].scatter(prediccion_train, residuos_train,
                   edgecolors=(0, 0, 0), alpha = 0.4)
axes[2, 0].axhline(y = 0, linestyle = '--', color = 'black', lw=2)
axes[2, 0].set_title('Residuos del modelo vs predicción', fontsize = 10, fontweight = "bold")
axes[2, 0].set_xlabel('Estimación')
axes[2, 0].set_ylabel('Residuos')
axes[2, 0].tick_params(labelsize = 7)
############################################################################################
# Se eliminan los ejes vacíos
fig.delaxes(axes[2,1])

fig.tight_layout()
plt.subplots_adjust(top=0.9)
fig.suptitle('Diagnóstico residuos', fontsize = 12, fontweight = "bold");
plt.show()
############################################################################################