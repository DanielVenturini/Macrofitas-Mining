import urllib.parse
import urllib.error
import urllib.request
import socket
from bs4 import BeautifulSoup
import time
import re

# classe para guardar as informações das plantas
# e para ter melhor controle sobre as informações
class InfPlanta:

	def __init__(self):
		self.__hashmap = {}

	@property
	def hashmap(self):
		return self.__hashmap

	@hashmap.setter
	def hashmap(self, hashmap):
		self.__hashmap = hashmap

	# retorna o valor mapeado para a chave
	# ou retorna a string '' se não houver valor mapeado
	# last é a string que deve ser colocada no fim da chave. geralmente é ' ' ou ', '
	def getMapped(self, key, last=' '):
		try:
			return self.hashmap[str(key)] + last
		except KeyError:
			return ''

	# retorna uma string com o reino completo da planta
	# por exemplo: Plantae Pteridophyta Filicopsida Polypodiales Salviniaceae
	def getReino(self):
		reino = self.getMapped('tK')
		reino += self.getMapped('tP')
		reino += self.getMapped('tC')
		reino += self.getMapped('tO')
		reino += self.getMapped('tF', last='')

		return reino

	# retorna uma string com a localização da ocorrência da planta
	# por exemplo: 'Jargim Botânico Rio, Rio de Janeiro, RJ, Brasil'
	def getLocalizacao(self):
		localizacao = self.getMapped('lP', last=', ')
		localizacao += self.getMapped('lM', last=', ')
		localizacao += self.getMapped('lS', last=', ')
		localizacao += self.getMapped('lC', last=', ')

		return localizacao[:-2]				# remove o último ', '

	# retorna uma tupla com a coordenada da ocorrência da planta
	# por exemplo: (-19.0019, -57.51)
	def getCoordenada(self):
		try:
			latitude = self.getMapped('lA')
			longitude = self.getMapped('lO')

			latitude = re.search('[+|-]?[\d]+(.[\d]+)?', latitude).group(0)
			longitude = re.search('[+|-]?[\d]+(.[\d]+)?', longitude).group(0)

			return (latitude, longitude)
		except AttributeError:
			return ' ', ' '

	def getColeta(self):
		coleta = self.getMapped('cL')
		coleta += self.getMapped('cN')
		coleta += self.getMapped('cY')

		return coleta[:-1]				# remove o último ' '

	def getDet(self):
		det = self.getMapped('tI')
		det += self.getMapped('tY')

		return det[:-1]					# remove o último ' '

#############################################################################

# retorna se uma latitude e longitude está dentro da américa do súl
def americaSul(lat, longi):

	try:
		lat = float(lat)
		longi = float(longi)
	except :
		return False

	# Extremo norte e leste
	if lat > 12.458611:
		return False

	# Extremo sul
	if lat < -59.488889:
		return False

	# Extremo leste
	if longi < -71.668889:
		return False

	# Extremo oeste
	if longi < -92.009167:
		return False

	return True


# retorna a requisição já no formado do BeaultifulSoup
def requisicaoSL(planta):
	url = urlSL()
	for i in range(0, 20):
		try:
			data = urllib.parse.urlencode({'ts_any': planta}).encode('ascii')	# insere o nome da planta no body
			thepage = urllib.request.urlopen(url, data, timeout=8)				# recupera a página
			soupdata = BeautifulSoup(thepage,"html.parser")						# faz o parse
			return soupdata
		except (urllib.error.URLError, urllib.error.HTTPError, socket.timeout) as ex:
			print("ErroSPLINK : " + str(ex))
			if(i > 10):
				time.sleep(5)
			else:
				time.sleep(2)

		print("TentativaSPLINK {0}".format(i))

	return False

def urlSL():
	return "http://www.splink.org.br/mod_perl/searchHint"

# recupera cada uma das divs que contém as plantas
def nextPlanta(soup):
	i = 0
	while True:
		div = soup.find(id='record_{0}'.format(i))
		i += 1

		if div.__eq__(''):
			break
		else:
			yield div

# recupera todos os spans e guarda a chave e
# o valor deles já em um objeto InfPlanta
def trataDiv(div):
	spans = div.findAll('span')
	planta = InfPlanta()

	for span in spans:

		if span.has_attr('class'):
			key = 'class'
		elif span.has_attr('index'):
			key = 'index'
		else:
			continue

		key = span[key][0]				# lista com apenas um elemento
		mapped = span.get_text()

		hashmap = planta.hashmap		# recupera a hash da planta get
		hashmap[str(key)] = mapped
		planta.hashmap = hashmap		# adiciona a hash com o novo atributo set

	return planta
	#lls = div.findAll('ll')			# os dados sobre o sexo estão em ll
	#for ll in lls:


def dadosSL(soup, nomePlanta):  		# valida pelo subtitulo
	
	coordenadas = []

	if not soup:
		return coordenadas

	try:
		divPlanta = nextPlanta(soup)	# recupera o iterador dos div das plantas
		# para cada ocorrencia de uma determinada planta
		while True:
			div = next(divPlanta)				# recupera a próxima div

			planta = trataDiv(div)				# trata os elementos da div
			lat, longi = planta.getCoordenada()
			local = planta.getLocalizacao()

			if americaSul(lat, longi):
				coordenadas.append(str(lat) + '!#' + str(longi) + '!#' + local)

	except StopIteration:						# lança StopIteration quando não há mais div
		#escritor.escreve(['', '', '', ''])
		return coordenadas


#dados = requisicaoSL(urlSL(), 'victoria amazonica')
#dadosSL(dados)
