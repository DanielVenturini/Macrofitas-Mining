import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage,"html.parser")
	return soupdata

def get_data(name):
	genero, especie = name.split(' ')
	response = {'checked': False,'message':'','obj':[]}
	soup = make_soup("http://www.theplantlist.org/tpl1.1/search?q="+genero+'+'+especie)

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
						response['checked'] = True
						response['obj'].append({'nome': nome, 'status': status,'source': source, 'dataSupplied': dataSupplied})
					count+=1
		return response 
	response['message'] = 'genero inválido'
	return response