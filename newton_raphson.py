import math
import numpy as np

num_padron = 102145

k = np.longdouble(10)
Lo = np.longdouble(2 * 100000 / num_padron) 
a = np.longdouble(1)
m = np.longdouble(100000 / num_padron)
g = np.longdouble(0)

def funcion(y):
	return -2*k*y*(1-Lo/(math.sqrt(math.pow(y,2) + math.pow(a,2)))) - m*g

def derivada(y):
	return -2*k*(-Lo*(math.pow(a,2))/(math.pow(math.pow(y,2)+math.pow(a,2),1.5))+1)

def newton_raphson(funcion,derivada,semilla,error):
	max_iteraciones = 10000
	salida = []

	error_actual = np.longdouble(100)
	iteracion_anterior = np.longdouble(semilla)

	cant_iteraciones = 0 

	while error_actual > error and cant_iteraciones < max_iteraciones:
		cant_iteraciones += 1
		iteracion_actual = iteracion_anterior - funcion(iteracion_anterior)/derivada(iteracion_anterior)
		error_actual = abs(iteracion_actual - iteracion_anterior)
		iteracion_anterior = iteracion_actual
		salida.append((cant_iteraciones,iteracion_actual,error_actual,error_actual/iteracion_actual))


	
	return salida