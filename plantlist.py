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
	return "http://www.theplantlist.org/tpl1.1/search?q=" + genero +'+'+ especie

def verificaEspecieIncorreta(especieEntrada, especieSite):
	if especieEntrada != especieSite:
		return True

def dadosPL(name, macrofita):  # valida pelo subtitulo
	try:
		genero, especie = name.split(' ')
		soup = requisicaoPL(urlPL(genero, especie))
	except urllib.error.URLError:
		print(urllib.error.URLError)
		raise

	spanSubtitulo = soup.findAll("span", class_="subtitle")
	if spanSubtitulo:
		for data in spanSubtitulo:
			if data.text.__contains__('is an accepted name'):
				macrofita.nomePlantlist = name + ' ' +soup.find("span", class_="authorship").text #pega o nome + autor
				macrofita.statusPlantlist = 'Aceito'
				macrofita.comaparaNome('plantlist')
				return
			
			elif data.text.__contains__('is a synonym'):
				a = data.text.split()
				nome = ''
				for char in a :
					if(char != 'is' and char != 'a' and char != 'synonym' and char != 'of'):
						nome = nome + char + ' '
				macrofita.nomePlantlist = nome
				macrofita.statusPlantlist = 'Aceito'
				return

			elif data.text.__contains__('is an unresolved name'):
				macrofita.obsPlantlist = 'Não Encontrado'
				return
			else:
				print('----------\n\n' + data.text + '----------\n\n')
				return

	else: # não possui subtitulo
		tdAceito = soup.findAll("td", class_="name Accepted")
		tdSynonym = soup.findAll("td", class_="name Synonym")

		if(tdAceito):
			for data in tdAceito:
				if not verificaEspecieIncorreta(especie, data.text.split()[1]):
					macrofita.nomePlantlist = data.text
					macrofita.statusPlantlist = 'Aceito'
					macrofita.comaparaNome('plantlist')
					return
				else:
					macrofita.obsPlantlist = 'Especie Invalida'
					return
		elif(tdSynonym):
			for data in tdSynonym:
				if not verificaEspecieIncorreta(especie, data.text.split()[1]):
					macrofita.nomePlantlist = data.text
					macrofita.statusPlantlist = 'Sinonimo'
					return
				else:
					macrofita.obsPlantlist = 'Especie Invalida'
					return 
		else:
			macrofita.obsPlantlist = 'Genero Invalido'
			return
		

# dadosPL()
