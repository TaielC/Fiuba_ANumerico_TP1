import argparse
import gspread 
import numpy as np 
import math
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
	parser.add_argument("metodo") # Opciones: 'biseccion', 'punto_fijo', 'newton_raphson'
	parser.add_argument("semilla_a", type = float)
	parser.add_argument("semilla_b", nargs = '?', const = None, type = float)
	return parser.parse_args()

def obtener_sheet(metodo):
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('planillas_numerico.json', scope)
	client = gspread.authorize(creds)

	return client.open(metodo).sheet1

FUNCIONES = {'biseccion':wrapper_biseccion, 'punto_fijo':wrapper_punto_fijo, 'newton_raphson':wrapper_newton_raphson}

def main():
	args = obtener_args()
	metodo = args.metodo
	semilla_a = args.semilla_a
	semilla_b = args.semilla_b

	sheet = obtener_sheet(metodo)

	tabla = FUNCIONES[metodo](funcion, derivada, semilla_a, semilla_b, error, valor_raiz, max_iteraciones)

	da_lo_mismo = []
	pos_valor = 2 if metodo == 'newton_raphson' else 3
	for k in range(1,len(tabla)):
		da_lo_mismo.append((k,abs(tabla[k][pos_valor] - tabla[k-1][pos_valor])))

	print(tabla)
	for fila in tabla:
		for i in range(len(fila)):
			if type(fila[i]) == np.longfloat:
				fila[i] = recortar_numero(str(fila[i]))

	for fila in tabla:
		sheet.append_row(fila)

	

main()