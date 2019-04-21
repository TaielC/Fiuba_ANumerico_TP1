import math
import numpy as np

k = np.longdouble(10)
Lo = np.longdouble(2 * 1e5/102145)
a = np.longdouble(1)
m = np.longdouble(1e5/102145)
g = np.longdouble(0)


def funcion(y):
	return -2*k*y*(1-Lo/(a**2+y**2)**0.5)-m*g

def calcular_cant_iteraciones(a, b, error):
	return int(math.log(abs(a-b)/error,2)+1)

def biseccion(funcion, a, b, error):

	lista = [('k','a','b','Fa','Fb',)]

	cant_iteraciones = calcular_cant_iteraciones(a, b, error)

	ai = a
	bi = b
	for i in range(cant_iteraciones+1):
		pi = (ai+bi)/2
		Fpi = funcion(pi)
		Fai = funcion(ai)
		Fbi = funcion(bi)

		print(Fpi)
		if(Fpi == 0):
			lista.append((i,ai,bi,Fai,Fbi,pi,Fpi,(abs(a-b)/2**i)))
			return lista

		if( Fpi*Fai < 0):
			bi = pi
		elif( Fpi*Fbi < 0):
			ai = pi
		else:
			raise ValueError
		lista.append((i,ai,bi,Fai,Fbi,pi,Fpi,(abs(a-b)/2**i)))

	return lista