import math
import numpy as np



def wrapper_biseccion(funcion, derivada, a, b, error, valor_raiz, max_iteraciones):
	if b == None:
		raise ValueError('No se dio un valor de b')
	return biseccion(funcion, a, b, error, valor_raiz, max_iteraciones)

def calcular_cant_iteraciones(a, b, error):
	return int(math.log(abs(a-b)/error,2)+1)

def biseccion(funcion, a, b, error, valor_raiz = None, max_iteraciones = 10000):

	tabla = [['k','a','b','F(a)','F(b)','p','err_rel','cota_err','err_absoluto']]

	cant_iteraciones = calcular_cant_iteraciones(a, b, error)

	ai = np.longfloat(a)
	bi = np.longfloat(b)
	Fai = funcion(ai)
	Fbi = funcion(bi)
	err = '-'
	err_rel = '-'
	for i in range(cant_iteraciones+1):

		if tabla[-1][3] == 0:
			break

		p = (ai+bi)/2

		tabla.append([i,ai,bi,Fai,Fbi,p,err_rel,abs(ai-bi),err])

		Fp = funcion(p)
		if valor_raiz:
			err = abs(p-valor_raiz)
			err_rel = err/valor_raiz

		if( Fp*Fai < 0):
			bi = p
			Fbi = Fp
		else:
			ai = p
			Fai = Fp

	return tabla