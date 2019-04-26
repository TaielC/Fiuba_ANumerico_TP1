import argparse
import numpy as np 
import math
import matplotlib.pylab as plt 
from scipy.optimize import brentq

import gspread 
from oauth2client.service_account import ServiceAccountCredentials

from biseccion import *
from newton_raphson import *
from punto_fijo import *

derivada = None
valor_raiz = None
error = 0.1
max_iteraciones = 10000
from funcion import *

def recortar_numero(string):
	retorno = string[:16]
	encontro_e = False
	for caracter in string:
		if caracter == 'e':
			encontro_e = True
		if encontro_e:
			retorno += caracter
	return retorno

def obtener_args():
	'''
	Parsea los argumentos pasados por consola.
	'''
	parser = argparse.ArgumentParser()
	parser.add_argument("metodo") # Opciones: 'biseccion', 'newton_raphson'. Opición adicional: 'graph_diferencias'
	parser.add_argument("semilla_a", type = float)
	parser.add_argument("semilla_b", nargs = '?', const = None, type = float)
	return parser.parse_args()

def obtener_sheet(metodo):
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('planillas_numerico.json', scope)
	client = gspread.authorize(creds)

	return client.open(metodo).sheet1


def imprimir_tabla_en_sheet(sheet, tabla):
	for fila in tabla:
		for i in range(len(fila)):
			if type(fila[i]) == np.longfloat:
				fila[i] = recortar_numero(str(fila[i]))

	for fila in tabla:
		sheet.append_row(fila)

def calcular_diferencias(tabla, metodo):
	diferencias = []
	pos_valor = 2 if metodo == 'newton_raphson' else 3

	valor_ant = tabla[1][pos_valor]
	for k in range(2,len(tabla)):
		valor = tabla[k][pos_valor]
		if valor == valor_ant:
			valor = tabla[k][pos_valor+1]
			print(k,abs(valor-valor_ant),valor,valor_ant)

		diferencias.append(abs(valor-valor_ant))
		valor_ant = valor
	return diferencias

FUNCIONES = {'biseccion':wrapper_biseccion, 'newton_raphson':wrapper_newton_raphson}

def grafico_diferencias(semilla_a, semilla_b):
	tablas = []
	dif_entre_iteraciones = []

	plt.figure(figsize=(10,7))
	for func in FUNCIONES:
		print(func)
		tablas.append(FUNCIONES[func](funcion, derivada, semilla_a, semilla_b, error, valor_raiz, max_iteraciones))
		dif_entre_iteraciones.append(calcular_diferencias(tablas[-1],func))
		plt.plot(np.arange(len(dif_entre_iteraciones[-1])), dif_entre_iteraciones[-1], '.--', lw=1, ms=8, label=func)

	plt.legend(loc='best')
	plt.yscale('log')
	plt.xlabel('k')
	plt.ylabel('delta_k')
	plt.title('Comparacion Métodos')
	plt.grid(True)
	plt.savefig('Tabla Comparativa-P1.png')
	# plt.show()

def encontrar_rango_convergencia_nr(direccion):
	
	diverge_con_actual = False
	busqueda_binaria = False
	intervalo = np.longfloat(0.01)

	anterior = 0
	actual = error+1
	ultima_linea = []
	while(True):
		if not busqueda_binaria and diverge_con_actual:
				actual = valor_raiz+ (intervalo if direccion > 0 else -intervalo)
		else:
			actual = (anterior+actual)/2

		ultima_linea = newton_raphson(funcion, derivada, actual, error,500)[-1][:]

		if ultima_linea[4] > error or abs(ultima_linea[1]-valor_raiz) > error:
			diverge_con_actual = True
			if not busqueda_binaria:
				busqueda_binaria = True
			continue
		else:
			if not busqueda_binaria:
				intervalo *= 2
			actual = anterior
			continue

		if actual-anterior < error:
			break

	if abs(ultima_linea[1]-valor_raiz) < error:
		return actual,'La convergencia es desde la raiz hasta el valor, llendo en direccion'
	else:
		return actual,'Es probable que hubiera otra raíz a donde convergió el Método'
def main():
	args = obtener_args()
	metodo = args.metodo
	semilla_a = args.semilla_a
	semilla_b = args.semilla_b

	if metodo == 'graph_diferencias':
		grafico_diferencias(semilla_a, semilla_b)
		return 
	elif metodo == 'buscar_rango_convergencia':
		print(encontrar_rango_convergencia_nr(semilla_a))
		return

	tabla = FUNCIONES[metodo](funcion, derivada, semilla_a, semilla_b, error, valor_raiz, max_iteraciones)

	# sheet = obtener_sheet(metodo)
	# imprimir_tabla_en_sheet(sheet, tabla)
	

main()