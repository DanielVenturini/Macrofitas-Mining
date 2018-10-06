import urllib
import urllib.request
from bs4 import BeautifulSoup

def requisicaoPL(url):
	try:
		thepage = urllib.request.urlopen(url)
		soupdata = BeautifulSoup(thepage,"html.parser")
		return soupdata
	except urllib.error.URLError:
		raise

def urlPL(genero, especie):
	return "http://www.theplantlist.org/tpl1.1/search?q="+genero+'+'+especie

def dadosPL(name):
	try:
		genero, especie = name.split(' ')
		response = {'checked': 'NAO', 'message': '', 'nameAccepted':'', 'trocado': 'NAO', 'obj': []}
		soup = requisicaoPL(urlPL(genero, especie))
	except (urllib.error.URLError, http.client.RemoteDisconnected):
		return response

	if(soup.findAll('tbody')):
		for record in soup.findAll('tr'):	#pega tr paginas
			count = 0
			for data in record.findAll('td'):  # pega td paginas
				if(count > 3):
					count = 0
				if(data.text):		
					if(count == 0):
						nome = data.text		
						esp = nome.split(' ')
						if (esp[1] != especie):	#descobre se foi retornado especies incorretas
							response['message'] = 'especie incorreta'
							return response
					elif(count == 1):	
						status = data.text
					elif(count == 2):
						source = data.text
					elif(count == 3):
						dataSupplied = data.text
						response['obj'].append({'nome': nome, 'status': status,'source': source, 'dataSupplied': dataSupplied})
						response['checked'] = True
						if(status == 'Accepted'): #verifica se eh o nome aceito
							response['nameAccepted'] = nome
							if(name.__contains__(nome)): #verifica se foi trocado nome de entrada
								response['trocado'] = 'SIM'
					count+=1
		return response 
	response['message'] = 'genero invalido'
	return response