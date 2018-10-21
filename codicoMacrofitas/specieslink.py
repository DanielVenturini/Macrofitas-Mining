import urllib
from bs4 import BeautifulSoup

# classe para guardar as informações das plantas
# e para ter melhor controle sobre as informações
class InfPlanta:

	def __init__(self):
		self.hashmap = {}

	def getNome1(self):
		nome1 = ''

		try:
			# montando o nome de trás para frente
			nome1 = self.hashmap['tF'] + nome1
			nome1 = self.hashmap['tO'] + ' ' + nome1
			nome1 = self.hashmap['tC'] + ' ' + nome1
			nome1 = self.hashmap['tP'] + ' ' + nome1
			nome1 = self.hashmap['tK'] + ' ' + nome1
		except KeyError:
			return nome1
		else:
			return nome1










# retorna a requisição já no formado do BeaultifulSoup
def requisicaoSL(url, planta):
	try:
		data = urllib.parse.urlencode({'ts_any': planta}).encode('ascii')
		thepage = urllib.request.urlopen(url, data)
		soupdata = BeautifulSoup(thepage,"html.parser")
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

# recupera as seguintes informações:
# nome1				tO + tF
# espécie			tGa + tEa
# autores			tA
# coleta, data		cL, cY
# local				lP + lM + lS + lC
# coordenadas		lA + lO
# sexo
def trataDiv(div):
	spans = div.findAll('span')
	planta = InfPlanta()

	for span in spans:
		# <span class='tO'>Anactinotrichida</span>
		key = span['class']			# tO
		mapped = span.get_text()	# Anactinotrichida

		planta.hashmap[key] = mapped

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

				trataDiv(div)				# trata os elementos da div

		except StopIteration:				# lança StopIteration quando não há mais div
			print('Acabou')

	except urllib.error.URLError:
		print(urllib.error.URLError)
		raise
