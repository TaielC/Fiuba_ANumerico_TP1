import gspread 
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('planillas_numerico.json', scope)
client = gspread.authorize(creds)

sheet = client.open('datos').sheet1

sheet.append_row([1,2,3,4,'Hello World!'])