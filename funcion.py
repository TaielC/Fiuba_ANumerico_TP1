import math
import numpy as np

NP = 102145 # Padrón utilizado

# Raiz con g = 0 : +-1.6833787452620399
valor_raiz = 1.6833787452620399
error = 0.5e-15

k = np.longdouble(10)
Lo = np.longdouble(2 * 100000 / NP) 
a = np.longdouble(1)
m = np.longdouble(100000 / NP)
g = np.longdouble(0)

def funcion(y):
	return -2*k*y*(1-Lo/(math.sqrt(math.pow(y,2) + math.pow(a,2)))) - m*g

def funcion_pf(y):
	return y + 2*k*y*(1-Lo/(math.sqrt(math.pow(y,2)+ math.pow(a,2)))) + m*g

def derivada(y):
	return -2*k*(-Lo*(math.pow(a,2))/(math.pow(math.pow(y,2)+math.pow(a,2),1.5))+1)