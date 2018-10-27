import urllib
from bs4 import BeautifulSoup

# classe para guardar as informações das plantas
# e para ter melhor controle sobre as informações
class InfPlanta:

	def __init__(self):
		self.hashmap = {}

	# retorna o valor mapeado para a chave
	# ou retorna a string '' se não houver valor mapeado
	def getMapped(self, key):
		try:
			return self.hashmap[str(key)] + ' '
		except KeyError:
			return ''

	# retorna uma string com o reino completo da planta
	# por exemplo: Plantae Pteridophyta Filicopsida Polypodiales Salviniaceae
	def getReino(self):
		reino = self.getMapped('tK')
		reino += self.getMapped('tP')
		reino += self.getMapped('tC')
		reino += self.getMapped('tO')
		reino += self.getMapped('tF')

		return reino[:-1]				# remove o último espaço

	# retorna uma string com a localização da ocorrência da planta
	# por exemplo: 'Jargim Botânico Rio, Rio de Janeiro, RJ, Brasil'
	def getLocalizacao(self):
		localizacao = self.getMapped('lP')
		localizacao += self.getMapped('lM')
		localizacao += self.getMapped('lS')
		localizacao += self.getMapped('lC')

		localizacao.replace(' ', ', ')		# substitui todos ' ' por ', ' para separar os nomes

		return localizacao[:-2]				# remove o último ', '

	# retorna uma string com a coordenada da ocorrência da planta
	# por exemplo: 'lat: -19.0019... long: -57.51... err: ± 15163'
	# vários casos não contém o 'err'
	def getCoordenada(self):
		latitude = self.getMapped('lA')
		longitude = self.getMapped('lO')
		err = self.getMapped('eR')

		coordenada = latitude + longitude + err

		return coordenada[1:-1]			# retorna a coordenada sem o '[' e o ']' da string


#############################################################################

# retorna a requisição já no formado do BeaultifulSoup
def requisicaoSL(url, planta):
	try:
		data = urllib.parse.urlencode({'ts_any': planta}).encode('ascii')	# insere o nome da planta no body
		thepage = urllib.request.urlopen(url, data)							# recupera a página
		soupdata = BeautifulSoup(thepage,"html.parser")						# faz o parse
		return soupdata
	except (urllib.error.URLError, urllib.error.HTTPError):
		raise

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
		planta.hashmap[str(key)] = mapped

	return planta
	#lls = div.findAll('ll')			# os dados sobre o sexo estão em ll
	#for ll in lls:


def dadosSL(macrofita):  # valida pelo subtitulo
	try:
		soup = requisicaoSL(urlSL(), macrofita)

		try:
			divPlanta = nextPlanta(soup)	# recupera o iterador dos div das plantas

			# para cada ocorrencia de uma determinada planta
			while True:
				div = next(divPlanta)		# recupera a próxima div

				planta = trataDiv(div)				# trata os elementos da div
				#print(planta.getCoordenada())

		except StopIteration:				# lança StopIteration quando não há mais div
			print('Acabou')

	except urllib.error.URLError:
		print(urllib.error.URLError)
		raise

#dadosSL('Victoria amazonica')