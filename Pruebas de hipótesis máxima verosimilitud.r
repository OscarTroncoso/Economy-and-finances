#Llamando librerias
library(dplyr)
library(ggplot2)

#Importando archivo .csv
File = read.csv(file = ('../Microeconometría/ClasesCII/Base de datos CII.csv'), skip = 0, header = TRUE)

############################################################################################################################################

#Inputs
Test = '2t'                             #'1tl', '1tr', '2t'
alpha = 0.05

#Matriz Restricción
R1 = c(0, 1, 0, 0)                       #Cada restricción
R2 = c(0, 0, 1, 0)
R = c(R1, R2)                            #Matriz de restricciones
J = 2                                   #Número de restricciones
r = c(0, 0)

#Parámetros
Y = File$Ingreso
X1 = File$Educacion
X2 = File$Edad
X3 = File$Genero
T = length(Y)
K = ncol(File)

#Conformación matriz R
R = matrix(R, nrow = as.numeric(length(R1)), ncol = J)
R = t(R)

#Estimación de los betas
Y = cbind(Y)
X = cbind(1, X1, X2, X3)
Betasm = solve(t(X) %*% X) %*% (t(X) %*% Y)
RB = R %*% Betasm                                        
Betase = Betasm + solve(t(X) %*% X) %*% t(R) %*% solve(R %*% solve(t(X) %*% X) %*% t(R)) %*% (r - RB)

############################################################################################################################################

#Estimación sigma^2 (Beta moño)
Ym = X %*% Betasm
Em = Y - Ym
sigma2 = as.numeric((t(Em) %*% Em) / (T - K))

#Prueba Jarque Bera (Normalidad en el error)
# JB = jarque.bera.test(Em)                     #Forma rápida
VcJB = qchisq(alpha, df = 2, lower.tail = FALSE)
S = (sum((Em - mean(Em)) ** 3) / T) / (sqrt(as.numeric((t(Em) %*% Em) / T)) ** 3)
K = (sum((Em - mean(Em)) ** 4) / T) / (sqrt(as.numeric((t(Em) %*% Em) / T)) ** 4)
JB = T * ((S ** 2 / 6) + ((K - 3) ** 2 / 24))

#Matriz var - cov betas
vcB = sigma2 * solve(t(X) %*% X)

#Lambda 1 (Multiplicadores de Lagrange)
#Lambda 1 por una F - Fisher
L1F = as.numeric((t(RB - r) %*% solve(R %*% solve(t(X) %*% X) %*% t(R)) %*% (RB - r)) / (J * sigma2))
VCF = qf(p = alpha, df1 = J, df2 = (T - K), lower.tail = FALSE)
#Lambda 1 por el test de la raíz de Lambda 1 si J = 1
L1t = as.numeric(RB - r) / (sqrt(as.numeric(R %*% vcB %*% t(R))))
#Valor crítico de 1t o 2t
if(Test == '2t'){
    VCt = qt(p = (alpha/2), df = (T - K), lower.tail = FALSE)        # True = cola izquierda, False = cola derecha  
} else {
    VCt = qt(p = alpha, df = (T - K), lower.tail = FALSE) 
}        

#Lambda 2 (Razón de verosimilitud)
#Beta moño
Ym = X %*% Betasm
Em = Y - Ym
SRCnr = as.numeric(t(Em) %*% Em)
#Beta estrella
Ye = X %*% Betase
Ee = Y - Ye
SRCr = as.numeric(t(Ee) %*% Ee)
L2 = (SRCr - SRCnr) / (J * sigma2)

#Lambda 3 (Test de Wold)
L3 = as.numeric((t(Betase - Betasm) %*% (t(X) %*% X) %*% (Betase - Betasm)) / (J * sigma2))

#Salidas
#Jarque Bera
if(JB < VcJB){
    print(sprintf('No hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio del test de Jarque Bera sobre normalidad en los errores', alpha))
        #Test de Lambdas
    if(L1F < VCF){
        print(sprintf('No hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio del test de multiplicadores de lagrange', alpha))
    }else{
        print(sprintf('Hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio del test de multiplicadores de lagrange', alpha))
    }
    if(J == 1){                                             
        if(Test == '1tl'){
            if(L1t < -VCt){
                print(sprintf('Hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio de la raíz de Lambda 1 (test de multiplicadores de Lagrange)', alpha))
            }else{
                print(sprintf('No hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio de la raíz de Lambda 1 (test de multiplicadores de Lagrange)', alpha))
            }
        }
        if(Test == '1tr'){
            if(L1t > VCt){
                print(sprintf('Hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio de la raíz de Lambda 1 (test de multiplicadores de Lagrange)', alpha))
            }else{
                print(sprintf('No hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio de la raíz de Lambda 1 (test de multiplicadores de Lagrange)', alpha))
            }
        }
        Check = between(L1t, -VCt, VCt)
        if(Test == '2t'){               
            if(Check == TRUE){
                print(sprintf('No hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio de la raíz de Lambda 1 (test de multiplicadores de Lagrange)', alpha))
            }else{
                print(sprintf('Hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio de la raíz de Lambda 1 (test de multiplicadores de Lagrange)', alpha))
            }
        }
    } else {
        print('No se puede hacer por medio de la raíz de Lambda 1 (test de multiplicadores de Lagrange) porque la F no tiene (1, (T - K)) grados de libertad')
    }
    if(L2 < VCF){
        print(sprintf('No hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio del test de razón de verosimilitud', alpha))
    }else{
        print(sprintf('Hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio del test de razón de verosimilitud', alpha))
    }
    if(L3 < VCF){
        print(sprintf('No hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio del test de Wold', alpha))
    }else{
        print(sprintf('Hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio del test de Wold', alpha))
    }

    #Gráficas
    #Lambda 1 con t
    if(J == 1){
        if(Test == '1tr'){
        #Int. Confianza 1tr
            Cord.x = c(VCt, seq(VCt, 5, 0.01), Inf)
            Cord.y = c(0, dt(seq(VCt, 5, 0.01), df = (T - K)), 0)
            plot(function(x) dt(x, df = (T-K)), xlim = c(-5, 5), ylim = c( 0, 0.4),
                main = sprintf("t - Student cola derecha (df = %s) con alpha %s", (T-K), alpha),
                xlab = 't - value', ylab = 'Probabilidad',
                col = "black", type = "l", lwd = 2)
            polygon(Cord.x, Cord.y,
                    col = "slateblue1",
                    border = 1)
            points(x = L1t, y = dt(L1t, df = (T-K)), col = "red",pch = 19, lwd = 3)
        } 
        if(Test == '1tl'){
        #Int. Confianza 1tl
            Cord.x = c(-5, seq(-5, -VCt, 0.01), -VCt)
            Cord.y = c(0, dt(seq(-5, -VCt, 0.01), df = (T - K)), 0)
            plot(function(x) dt(x, df = (T-K)), xlim = c(-5, 5), ylim = c( 0, 0.4),
                main = sprintf("t - Student cola izquierda (df = %s) con alpha %s", (T-K), alpha),
                xlab = 't - value', ylab = 'Probabilidad',
                col = "black", type = "l", lwd = 2)
            polygon(Cord.x, Cord.y,
                    col = "slateblue1",
                    border = 1)
            points(x = L1t, y = dt(L1t, df = (T-K)), col = "red",pch = 19, lwd = 3)
        }
        if(Test == '2t'){
        #Int. Confianza 2t
            Cord.x = c(VCt, seq(VCt, 5, 0.01), Inf)
            Cord.y = c(0, dt(seq(VCt, 5, 0.01), df = (T - K)), 0)
            plot(function(x) dt(x, df = (T-K)), xlim = c(-5, 5), ylim = c( 0, 0.4),
                main = sprintf("t - Student dos colas (df = %s) con alpha %s", (T-K), alpha),
                xlab = 't - value', ylab = 'Probabilidad',
                col = "black", type = "l", lwd = 2)
            polygon(Cord.x, Cord.y,
                    col = "slateblue1",
                    border = 1)
            Cord.x = c(-5, seq(-5, -VCt, 0.01), -VCt)
            Cord.y = c(0, dt(seq(-5, -VCt, 0.01), df = 100), 0)
            polygon(Cord.x, Cord.y,
                    col = "slateblue1",
                    border = 1)
            points(x = L1t, y = dt(L1t, df = (T-K)), col = "red",pch = 19, lwd = 3)
        }
    }else{
        #Lambda 1,2 y 3 con F
        Cord.x = c(VCF, seq(VCF, 6, 0.01), Inf)
        Cord.y = c(0, df(seq(VCF, 6, 0.01), df1 = J, df2 = (T - K)), 0)
        plot(function(x) df(x, df1 = J, df2 = (T - K)), xlim = c(-0.1, 5), ylim = c( 0, 1),
            main = sprintf("F - Fisher para Lambda 1, 2 y 3 (df1 = %s, df2 = %s) con alpha %s", J, (T-K), alpha),
            xlab = 'F - value', ylab = 'Probabilidad',
            col = "black", type = "l", lwd = 2)
        polygon(Cord.x, Cord.y,
                col = "slateblue1",
                border = 1)
        points(x = L1F, y = df(L1F, df1 = J, df2 = (T - K)), col = "red",pch = 19, lwd = 7)
        points(x = L2, y = df(L2, df1 = J, df2 = (T - K)), col = "blue",pch = 19, lwd = 5)
        points(x = L3, y = df(L3, df1 = J, df2 = (T - K)), col = "green",pch = 19, lwd = 3)
    }
}else{
    print(sprintf('Hay suficiente evidencia para rechazar H0 a un nivel de significancia alpha de: %s, por medio del test de Jarque Bera sobre normalidad en los errores, por lo que no es posible hacer inferencia', alpha))
}


