#Llamando librerias
library(dplyr)
library(ggplot2)
library(lmtest)

#Importando archivo .csv
File = read.csv(file = '../ClasesCII/Basedatos.csv', skip = 0, header = TRUE)

############################################################################################################################################

#Inputs
Test = '2t'                             #'1tl', '1tr', '2t'
alpha = 0.05
Rho_i = 'No dado'                       #'No dado' si no lo tiene, diferente de cero cuál es el valor (Valor del Rho para Durbin - Watson)
Dl = 1.336
Du = 1.720

#Matriz Restricción
R1 = c(0, 1, 0, 0, 0)                       #Cada restricción
R2 = c(0, 0, 1, 0, 0)
R = c(R1, R2)                            #Matriz de restricciones
J = 2                                   #Número de restricciones
r = c(0, 0)

#Parámetros
Y = File$Cij
X1 = File$Yi
X2 = File$Yj
X3 = File$Dij
X4 = File$Acuerdo
T = length(Y)
K = ncol(File) - 4

#Si hay transformación lineal
Y = log(Y)
X1 = (X1)
X2 = (X2)
X3 = (X3)
X4 = X4

#Conformación matriz R
R = matrix(R, nrow = as.numeric(length(R1)), ncol = J)
R = t(R)

#Estimación de los betas
Y = cbind(Y)
X = cbind(1, X1, X2, X3, X4)
Betasm = solve(t(X) %*% X) %*% (t(X) %*% Y)
RB = R %*% Betasm                                        
Betase = Betasm + solve(t(X) %*% X) %*% t(R) %*% solve(R %*% solve(t(X) %*% X) %*% t(R)) %*% (r - RB)

############################################################################################################################################

#Estimación sigma^2 (Beta moño)
Ym = X %*% Betasm
Em = Y - Ym
sigma2 = as.numeric((t(Em) %*% Em) / (T - K))

# Durbin Watson----
Emt1 = Em[-1]
Emt = Em[-T]
# Emt2 = append(Emt2, 0)

if(Rho_i == 'No dado'){
    Dw = sum((Emt - Emt1) ** 2) / sum(Emt1 ** 2)
    print(sprintf('El valor del estádistico de Durbin - Watson es: %s', round(Dw, 3)))
} else {
    Dw = 2 * (1 - as.numeric(Rho_i))
    print(sprintf('El valor del estádistico de Durbin - Watson es: %s', round(Dw, 3)))
}


plot(NA, xlim = c(0, 4), ylim = c(0, 1),
    main = sprintf("Test de no autocorrelación de Durbin - Watson con un alpha %s", alpha))
    abline(v = Dl, col = "blue", lwd = 2)
    abline(v = Du, col = 'blue', lwd = 2)
    abline(v = 4 - Dl, col = 'blue', lwd = 2)
    abline(v = 4 - Du, col = 'blue', lwd = 2)
    points(x = Dw, y = 0.5, col = "red",pch = 19, lwd = 3)
    text(x = Dl/2, y = 0.5, 'Zona autocorrelación positiva', srt = 90)
    text(x = (4 - Dl) + (Dl / 2), y = 0.5, 'Zona autocorrelación negativa', srt = 90)
    text(x = (Dl) + ((Du - Dl) / 2), y = 0.5, 'Zona indecisión', srt = 90)
    text(x = (4 - Du) + ((Du - Dl) / 2), y = 0.5, 'Zona indecisión', srt = 90)
    text(x = (Du) + ((4 - 2 * Du) / 2), y = 0.5, 'Zona no rechazo', srt = 90)

