from Equation import Expression
import math

num_padron = 102145

k = 10
Lo = 2 * 100000 / num_padron 
a = 1
m = 100000 / num_padron
g = 0

def funcion(y):
	return y + 2*k*y*(1-Lo/(math.sqrt(math.pow(y,2) + math.pow(a,2)))) + m*g

def punto_fijo(funcion_pf,semilla,error):
	max_iteraciones = 100
	error_actual = math.inf

	iteracion_anterior = semilla

	cant_iteraciones = 0

	while error_actual > error and cant_iteraciones <= max_iteraciones:
		cant_iteraciones += 1

		iteracion_actual = funcion_pf(iteracion_anterior)
		error_actual = abs(iteracion_anterior - iteracion_actual)
		iteracion_anterior = iteracion_actual

	print(cant_iteraciones)
	return iteracion_anterior