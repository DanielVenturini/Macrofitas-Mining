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


def dadosPL(name):  # valida pela tabela
	try:
		genero, especie = name.split(' ')
		response = {'checked': True, 'message': '', 'nameAccepted':'', 'trocado': 'NAO', 'obj': []}
		soup = requisicaoPL(urlPL(genero, especie))
	except (urllib.error.URLError):
		return response

	if(soup.findAll('tbody') and soup.findAll('tr')):
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
						# verifica se eh o nome aceito
						if(status == 'Accepted' and response['nameAccepted'].__len__ != 0):
							response['nameAccepted'] = nome
							if(name.__contains__(nome)): #verifica se foi trocado nome de entrada
								response['trocado'] = 'SIM'
					count+=1
		return response 
	response['message'] = 'Especie nao encontrada PlantList'
	return response


def dadosPL2(name): #valida pelo subtitulo
	try:
		genero, especie = name.split(' ')
		response = {'checked': True, 'message': '',
                    'nameAccepted': '', 'trocado': 'NAO', 'obj': []}
		soup = requisicaoPL(urlPL(genero, especie))
	except (urllib.error.URLError):
		return response

	if soup.findAll("span", class_="subtitle"):
		for data in soup.findAll("span", class_="subtitle"):
			if data.text.__contains__('is an accepted name'):
				response['checked'] = True
				response['nameAccepted'] = name
				return response
			
			elif data.text.__contains__('is a synonym'):
				a = data.text.split()
				nome = ''
				for char in a :
					if(char != 'is' and char != 'a' and char != 'synonym' and char != 'of'):
						nome = nome + char + ' '
				response['checked'] = True
				response['nameAccepted'] = nome
				response['trocado'] = 'SIM'
				return response
			elif data.text.__contains__('is an unresolved name'):
				response['checked'] = True
				response['nameAccepted'] = ''
				response['trocado'] = 'NAO'
				response['message'] = 'This name is unresolved -- Plantlist status'
				return response
			else:
				print('----------\n\n' + data.text + '----------\n\n')
	else:
		return dadosPL(name)

#print(dadosPL2('Salicornia ambigua'))
