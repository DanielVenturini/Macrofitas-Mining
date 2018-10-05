import urllib
import urllib.request
from bs4 import BeautifulSoup

def requisicaoPL(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage,"html.parser")
	return soupdata

def urlPL(genero, especie):
	return "http://www.theplantlist.org/tpl1.1/search?q="+genero+'+'+especie

def dadosPL(name):
	genero, especie = name.split(' ')
	response = {'checked': False, 'message': '', 'obj': [], 'nameAccepted':''}
	soup = requisicaoPL(urlPL(genero, especie))

	if(soup.findAll('tbody')):
		for record in soup.findAll('tr'):
			count = 0
			for data in record.findAll('td'):
				if(count > 3):
					count = 0
				if(data.text):
					if(count == 0):
						nome = data.text		
						esp = nome.split(' ')
						if (esp[1] != especie):
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
						if(status == 'Accepted'):
							response['nameAccepted'] = nome
					count+=1
		return response 
	response['message'] = 'genero inválido'
	return response