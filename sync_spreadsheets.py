import gspread 
from oauth2client.service_account import ServiceAccountCredentials

# scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('planillas_numerico.json', scope)
# client = gspread.authorize(creds)

# sheet = client.open('datos').sheet1






def nformat(n):
	'''Devuelve un número formateado como X.XXXXXEYY'''
	n = str('%.80f' % n)

	string = ""
	i 		= 0
	ceros 	= 0
	pos 	= 0
	for caracter in n:
		pos +=1
		if caracter == '0':
			ceros +=1
			continue
		elif caracter == '.':
			continue
		elif caracter == '-':
			string += '-'
			continue

		if i == 1:
			string += '.'
		elif i == 4: #Acá se define la cantidad de cifras significativas después de la coma
			if int(n[pos+1]) >= 5:
				string+= str(int(caracter)+1)
			else:
				string+= caracter
			break
		i+=1
		string += caracter

	if i == 0:
		return '0*'
	return string+' E-'+str(ceros)


