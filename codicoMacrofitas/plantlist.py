import urllib
import urllib.request
from bs4 import BeautifulSoup
import time

def requisicaoPL(url):
	for i in range(3):
		try:
			thepage = urllib.request.urlopen(url, timeout=3)
			soupdata = BeautifulSoup(thepage,"html.parser")
			return soupdata
		except:
			print('Tentativa:',i)			
	return False

def urlPL(name):
	genero, especie = name.split(' ')[0:2]
	return "http://www.theplantlist.org/tpl1.1/search?q=" + genero +'+'+ especie

def verificaEspecieIncorreta(especieEntrada, especieSite):
	if especieEntrada != especieSite:
		return False
	return True

# parâmetro escrever diz se os sinônimos já foram escritos no arquivo na função dadosFB
# se ainda não foram, então escreve daqui
def dadosPL(name, macrofita, soup):  # valida pelo subtitulo
	especie = name.split(' ')[1]
	spanSubtitulo = soup.findAll("span", class_="subtitle")
	if spanSubtitulo:
		for data in spanSubtitulo:
			if data.text.__contains__('is an accepted name'):
				macrofita.nomePlantlist = name + ' ' + soup.find("span", class_="authorship").text #pega o nome + autor
				macrofita.statusPlantlist = 'Aceito'
				macrofita.comaparaNome('plantlist')
				return

			elif data.text.__contains__('is a synonym'):				
				a = data.text.split()
				nome = ''
				for char in a :
					if(char != 'is' and char != 'a' and char != 'synonym' and char != 'of'):
						nome = nome + char + ' '
				macrofita.nomePlantlist = nome.strip(' ')
				macrofita.statusPlantlist = 'Sinonimo'
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
				if verificaEspecieIncorreta(especie, data.text.split()[1]):
					macrofita.nomePlantlist = data.text
					macrofita.statusPlantlist = 'Aceito'
					macrofita.comaparaNome('plantlist')
					return
				else:
					macrofita.obsPlantlist = 'Especie Invalida'
					return
		elif(tdSynonym):
			for data in tdSynonym:
				if verificaEspecieIncorreta(especie, data.text.split()[1]):
					macrofita.nomePlantlist = macrofita.nomeEspecie
					macrofita.statusPlantlist = 'Sinonimo'
					return
				else:
					macrofita.obsPlantlist = 'Especie Invalida'
					return 
		else:
			macrofita.obsPlantlist = 'Genero Invalido'
			return


#recupera todos os sinonimos
def getSinonimosPL(nomePlanta, soup): 
	
	try:
		tdSynonym = soup.findAll("td", class_="name Synonym")
		sinonimo = []
	except urllib.error.URLError as er:
		print(er)
		return []

	try:
		for td in tdSynonym:	
			sin = BeautifulSoup(str(td), "html.parser")
			sinonimo.insert(0, str(sin.find("i", class_="genus").text +' '+ sin.find("i", class_="species").text +' '+sin.find("span", class_="authorship").text))
		return sinonimo
	except :
		return ['']

# nomePlanta = 'Sesuvium portulacastrum'
# jsonRespPlantlist = requisicaoPL(urlPL(nomePlanta))
# # print(jsonRespPlantlist)
# print(getSinonimosPL(nomePlanta, jsonRespPlantlist))
