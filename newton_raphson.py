import math
import numpy as np

def wrapper_newton_raphson(funcion, derivada, semilla, semilla_b, error, valor_raiz, max_iteraciones):
	return newton_raphson(funcion, derivada, semilla, error, max_iteraciones)


def newton_raphson(funcion,derivada,semilla,error, max_iteraciones = 10000):

	err = np.longdouble(math.inf)
	p = np.longdouble(semilla)
	Fp = funcion(p)

	i = 0 
	tabla = [['i','p','F(p)','err_rel','cota_err'],[i,p,Fp,'-','-']]
	while err > error and i < max_iteraciones:
		i += 1
		p = p - Fp/derivada(p)
		Fp = funcion(p)
		err = abs(p - tabla[-1][1])
		tabla.append([i,p,Fp,err/p,err])


	
	return tabla