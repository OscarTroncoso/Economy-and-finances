#Llamando librerias
library(dplyr)
library(ggplot2)
library(tseries)

#Importando archivo .csv
File = read.csv(file = ('../Microeconometría/ClasesCII/Base de datos CII.csv'), skip = 0, header = TRUE)

############################################################################################################################################

#Inputs
#H0: B2 = 15000
#H1: B2 <> 15000
Test = '1tr'                             #'1tl', '1tr', '2t'
R = c(0, 1, 0, 0, 0)
r = c(40000)
alpha = 0.05

#Parámetros
Y = File$Ingreso
X1 = File$Educacion
X2 = File$Edad
X3 = File$Edad ** 2
X4 = File$Genero
T = length(Y)
K = ncol(File)

#Si hay transformación lineal
Y = Y
X1 = X1
X2 = X2
X3 = X3
X4 = X4

#Estimación de los betas
Y = cbind(Y)
X = cbind(1, X1, X2, X3, X4)
Betasm = solve(t(X) %*% X) %*% (t(X) %*% Y)

############################################################################################################################################

#Estimación sigma^2 (Beta moño)
Ym = X %*% Betasm
Em = Y - Ym
sigma2 = as.numeric((t(Em) %*% Em) / (T - K))

#Prueba Jarque Bera (Normalidad en el error)
# JB = jarque.bera.test(Em)                     #Forma rápida
S = (sum((Em - mean(Em)) ** 3) / T) / (sqrt(as.numeric((t(Em) %*% Em) / T)) ** 3)
K = (sum((Em - mean(Em)) ** 4) / T) / (sqrt(as.numeric((t(Em) %*% Em) / T)) ** 4)
JB = T * ((S ** 2 / 6) + ((K - 3) ** 2 / 24))
VcJB = qchisq(alpha, df = 2, lower.tail = FALSE)

#Matriz var - cov betas
vcB = sigma2 * solve(t(X) %*% X)

#Estimación intervalo de confianza
R = matrix(R, nrow = 1, ncol = ncol(vcB))                                 
RB = R %*% Betasm                                      #Se toman los betas de interés
Rvc = R %*% vcB %*% t(R)                           #Selección matriz var - cov de los Betasm
#Valor crítico de 1t o 2t
if(Test == '2t'){
    Vc = qt(p = (alpha/2), df = (T - K), lower.tail = FALSE)        # True = cola izquierda, False = cola derecha  
} else {
    Vc = qt(p = alpha, df = (T - K), lower.tail = FALSE) 
}        
ICp = round(RB + (Vc * sqrt(Rvc)), 4)
ICn = round(RB - (Vc * sqrt(Rvc)), 4)

#Salidas
print(Betasm)
#Jarque Bera
if(JB < VcJB){
    print(sprintf('No hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio del test de Jarque Bera sobre normalidad en los errores', alpha))
        #Int. Confianza
    if(Test == '2t'){               
        print(sprintf('El intervalo de confianza a %s es: [%s, %s]', alpha, ICn, ICp))
    } else { 
        print(sprintf('El intervalo de confianza a %s es: [%s, %s]', alpha, ICn, ICp))
    }
    #Condición de tails
    #Rechaza o no H0:
    if(Test == '1tl'){
        print(sprintf('El intervalo de confianza de 1tl es [%s, Inf]', ICn))
        if(r < ICn){
            print(sprintf('Hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s', alpha))
        }else{
            print(sprintf('No hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s', alpha))
        }
    }
    if(Test == '1tr'){
        print(sprintf('El intervalo de confianza de 1tr es [-Inf, %s]', ICp))
        if(r > ICp){
            print(sprintf('Hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s', alpha))
        }else{
            print(sprintf('No hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s', alpha))
        }
    }
    Check = between(r, ICn, ICp)
    if(Test == '2t'){
        print(sprintf('El intervalo de confianza de 2t es [%s, %s]', ICn, ICp))                
        if(Check == TRUE){
            print(sprintf('No hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s', alpha))
        }else{
            print(sprintf('Hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s', alpha))
        }
    }

    #Gráficas
    #Parámetros gráficas
    if(Test == '1tr'){
    #Int. Confianza 1tr
        t = dt(X, df = (T - K))
        Cord.x = c(Vc, seq(Vc, 5, 0.01), Inf)
        Cord.y = c(0, dt(seq(Vc, 5, 0.01), df = (T - K)), 0)
        #Int. Confianza 1tr
        plot(function(x) dt(x, df = (T-K)), xlim = c(-5, 5), ylim = c( 0, 0.4),
            main = sprintf("t - Student cola derecha (df = %s) con alpha %s", (T-K), alpha),
            xlab = 't - value', ylab = 'Probabilidad',
            col = "black", type = "l", lwd = 2)
        polygon(Cord.x, Cord.y,
                col = "slateblue1",
                border = 1)
    } 
    if(Test == '1tl'){
    #Int. Confianza 1tl
        t = dt(X, df = (T - K))
        Cord.x = c(-5, seq(-5, -Vc, 0.01), -Vc)
        Cord.y = c(0, dt(seq(-5, -Vc, 0.01), df = (T - K)), 0)
        #Int. Confianza 1tr
        plot(function(x) dt(x, df = (T-K)), xlim = c(-5, 5), ylim = c( 0, 0.4),
            main = sprintf("t - Student cola izquierda (df = %s) con alpha %s", (T-K), alpha),
            xlab = 't - value', ylab = 'Probabilidad',
            col = "black", type = "l", lwd = 2)
        polygon(Cord.x, Cord.y,
                col = "slateblue1",
                border = 1)
    }
    if(Test == '2t'){
        #Int. Confianza 2t
        t = dt(X, df = (T - K))
        Cord.x = c(Vc, seq(Vc, 5, 0.01), Inf)
        Cord.y = c(0, dt(seq(Vc, 5, 0.01), df = (T - K)), 0)
        #Int. Confianza 1tr
        plot(function(x) dt(x, df = (T-K)), xlim = c(-5, 5), ylim = c( 0, 0.4),
            main = sprintf("t - Student dos colas (df = %s) con alpha %s", (T-K), alpha),
            xlab = 't - value', ylab = 'Probabilidad',
            col = "black", type = "l", lwd = 2)
        polygon(Cord.x, Cord.y,
                col = "slateblue1",
                border = 1)
        Cord.x = c(-5, seq(-5, -Vc, 0.01), -Vc)
        Cord.y = c(0, dt(seq(-5, -Vc, 0.01), df = 100), 0)
        polygon(Cord.x, Cord.y,
                col = "slateblue1",
                border = 1)
    }
}else{
    print(sprintf('Hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio del test de Jarque Bera sobre normalidad en los errores, por lo que no es posible hacer inferencia', alpha))
}

