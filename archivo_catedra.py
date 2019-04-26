#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TP1 ANALISIS NUMERICO
Problemas de busqueda de raices
Comparacion de metodos

1 Cuatrimestre 2019

Por:
Ignacio

"""

#Imports
from scipy.optimize import brentq
import timeit #Para calcular tiempo de corrida
import numpy as np #Manejo de arrays
import matplotlib.pylab as plt #Rutinas gráficas


#Constantes
NP = 81714
L0 = 2*100000 / NP #m
k = 10 #N/m
m0 = 100000/NP #kg
m = 1*m0
a = 1 #m
g = 9.81 #m/s**2

#Funciones f y derivadas
def f(y): 
    """
    funcion para buscar raices del tp
    devuelve fuerza resultante en y del sistema de masa y dos resortes
    
    OJO: Definida con constantes de afuera
    """
    return -2*k*y * ((1 - L0) / np.sqrt(y**2+a**2)) - m * g

def df1(x): 
    """
    derivada de f
    """
    return None #Usar Wolfram y calcular derivada


#Funciones busqueda de raices
def bisec(f, a, b, a_tol, n_max):
    """
    Devolver (x0, delta), raiz y cota de error por metodo de la biseccion
    Datos deben cumplir f(a)*f(b) > 0
    """
    x = a+(b-a)/2    #mejor que (a+b)/2 segun Burden
    delta = (b-a)/2
    
    delta_abs_graph = [] #Solo para el tp
    
    print('{0:^4} {1:^17} {2:^17} {3:^17}'.format('i', 'x', 'a', 'b'))
    print('{0:4} {1: .14f} {2: .14f} {3: .14f}'.format(0, x, a, b))
    
    for i in range(n_max):
        if f(a) * f(x) > 0:
            a = x
        else:
            b = x
        x_old = x
        x = a+(b-a)/2 #(a+b)/2
        delta = np.abs(x - x_old)
        
        delta_abs_graph.append(delta) #Solo para el tp
        
        print('{0:4} {1: .14f} {2: .14f} {3: .14f}'.format(i+1, x, a, b))
        
        if delta <= a_tol: #Hubo convergencia
            print('Hubo convergencia, n_iter = ' + str(i+1))
            return x, delta, i+1, delta_abs_graph
    
    #Si todavia no salio es que no hubo convergencia:
    raise ValueError('No hubo convergencia')
    return x, delta, i+1, delta_abs_graph

def secante(f, x0, x1, a_tol, n_max):
    """
    Devolver (x, delta), raiz y cota de error por metodo de la secante
    """
    delta = 0
    
    delta_abs_graph = [] #Solo para el tp

    print('{0:^4} {1:^17} {2:^17} {3:^17}'.format('i', 'x', 'x_-1', 'delta'))
    print('{0:4} {1: .14f} {2: .14f} {3: .14f}'.format(0, x1, x0, delta))

    for i in range(n_max):
        x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        delta = np.abs(x - x1)
        
        delta_abs_graph.append(delta) #Solo para el tp
        
        x0 = x1
        x1 = x
        
        print('{0:4} {1: .14f} {2: .14f} {3: .14f}'.format(i+1, x1, x0, delta))
        
        #Chequear convergencia
        if delta <= a_tol: #Hubo convergencia
            print('Hubo convergencia, n_iter = ' + str(i+1))
            return x, delta, i+1, delta_abs_graph

    #Si todavia no salio es que no hubo convergencia:
    raise ValueError('No hubo convergencia')
    return x. delta, i+1, delta_abs_graph

#Intervalo para buscar raiz
l_izq = 0.0
l_der = 2.0

#Parametros para el algoritmo
a_tol = 1e-15
n_max = 200

#Grafica de las funciones
#Ver https://matplotlib.org
print('----------------')
print('Graficando f')
print('----------------')
print('')
xx = np.linspace(l_izq, l_der, 256+1)
yy = f(xx)
nombre = 'f'
plt.figure(figsize=(10,7))
plt.plot(xx, yy, lw=2)
#plt.legend(loc=best)
plt.xlabel('x')
plt.ylabel(nombre +'(x)')
plt.title('Funcion '+ nombre)
plt.grid(True)
plt.savefig(nombre + '.png')
plt.show()

print('----------------')
print('Metodo biseccion')
print('----------------')
print('')
print('Funcion f, a_tol = '+str(a_tol))
r, delta, n_iter, delta_abs_graph_bisec = bisec(f, l_izq, l_der, a_tol, n_max)
print('raiz = ' +str(r))
print('delta= ' +str(delta))
print('n_ite= ' +str(n_iter))
print('')

print('----------------')
print('Metodo secante')
print('----------------')
print('')
print('Funcion f, a_tol = '+str(a_tol))
r, delta, n_iter, delta_abs_graph_secante = secante(f, l_izq, l_der, a_tol, n_max)
print('raiz = ' +str(r))
print('delta= ' +str(delta))
print('n_ite= ' +str(n_iter))
print('')

print('----------------')
print('Metodo brent')
print('----------------')
print('')
print('Funcion f1, a_tol por defecto para la funcion')
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html
r, results = brentq(f, l_izq, l_der, full_output=True)
print('raiz = ' +str(r))
print('Resultados: ')
print(results)

print('----------------')
print('Graficando comparacion de metodos')
print('----------------')
print('')
nombre = 'Comparacion_metodos'
plt.figure(figsize=(10,7))
plt.plot(np.arange(len(delta_abs_graph_bisec)),
         delta_abs_graph_bisec, '.--', lw=1, ms=8, label='Biseccion')
plt.plot(np.arange(len(delta_abs_graph_secante)),
         delta_abs_graph_secante, '.--', lw=1, ms=8, label='Secante')
plt.legend(loc='best')
plt.yscale('log')
plt.xlabel('k')
plt.ylabel('delta_k')
plt.title(nombre)
plt.grid(True)
plt.savefig(nombre + '.png')
plt.show()
