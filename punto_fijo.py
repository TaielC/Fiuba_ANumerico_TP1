from Equation import Expression
import math


def wrapper_punto_fijo(funcion, derivada, semilla, semilla_b, error, valor_raiz, max_iteraciones):
	return punto_fijo(funcion, semilla, error, max_iteraciones)



def punto_fijo(funcion_pf,semilla,error,max_iteraciones = 10000):
	err = np.longdouble(math.inf)
	p = np.longdouble(semilla)
	Fp = funcion(p)

	i = 0 
	tabla = [['i','p','F(p)','err_rel','cota_err'],[i,p,Fp,'-','-']]
	while err > error and i < max_iteraciones:
		i += 1
		p = Fp
		Fp = funcion(p)
		err = abs(p - tabla[-1][1])
		tabla.append([i,p,Fp,err/p,err])

	return tabla