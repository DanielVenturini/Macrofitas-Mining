import requests
from bs4 import BeautifulSoup

def urlFB(nomePlanta):
    return "http://servicos.jbrj.gov.br/flora/taxon/" + nomePlanta.replace(' ','%20')

def requisicaoFB(url, i=5):
    try:
        req = requests.get(url).json()
        return req
        if(i <= 0):
            return False
    except:
        requisicaoFB(url, i-1)

# deve retornar uma tupla: return validado, nomeValidado
#                                 'SIM'|'NAO', 'NOME CIENTIFICO DO SITE'
def dadosFB(nomePlanta, jsonResp, macrofita):
    # para cada um dos resultados
    if(not jsonResp):
        return
    try:
        if(jsonResp['result']):
            for result in jsonResp['result']:
                if result['taxonomicstatus'].__eq__('NOME_ACEITO'):     # se for um nome aceito
                    macrofita.statusFlora = 'Aceito'
                    macrofita.nomeFlora = result['scientificname']
                    macrofita.comaparaNome('flora')
                    macrofita.floraID = result['taxonid']

                    return False        # como já foi escrito os sinonimos aqui, não escrever para o Plantlist
                elif(result['NOME ACEITO']):
                    for nome in result['NOME ACEITO']:
                        if nome['taxonomicstatus'].__eq__('NOME_ACEITO'):
                            macrofita.statusFlora = 'Sinonimo'
                            macrofita.nomeFlora = nome['scientificname']
                            macrofita.floraID = result['taxonid']
                            return True #dadosFB(nome['scientificname'], requisicaoFB(urlFB(nome['scientificname'])), macrofita, escritor)      # provavelmente tem que fazer uma chamada recursiva para recuperar os dados da planta com o nome certo
            macrofita.statusFlora = 'Sinonimo'
            macrofita.nomeFlora = macrofita.nomeEspecie
            return True                 # não escreveu os sinônimos, então escreve no Plantlist
        else:
            return True
    except Exception as ex:
        print("Erro: {0} -- {1}".format(nomePlanta, ex))
        return True

def getSinonimosFB(nomePlanta, jsonResp):
    if(not jsonResp):
        return []
    sinonimos = []
    resp =  jsonResp['result']
    try:
        if(resp): 
            sinonimos = resp[0]["SINONIMO"]
        return sinonimos

    except Exception as ex:
        print("Erro: {0} -- {1}".format(nomePlanta, ex))
        return []

from floraInfo import FloraInfo

def getURLID(nomePlanta):
    resp = requisicaoFB('http://servicos.jbrj.gov.br/flora/url/' + nomePlanta.replace(' ', '%20'))
    if(not resp):
        return False

    return 'http://reflora.jbrj.gov.br/reflora/listaBrasil/ConsultaPublicaUC/ResultadoDaConsultaCarregaTaxonGrupo.do?&idDadosListaBrasil=' + resp["result"][0]["references"].split('=FB')[1]
    
def getInfoFlora(nomePlanta, info, jsonResp):
    if(not jsonResp):
        return []
    siteFlora = jsonResp
    
    soup = BeautifulSoup(siteFlora['hierarquia'], "html.parser")
    info.familia = soup.find("div", class_="taxon").text + soup.find("div", class_="nomeAutorSupraGenerico").text
    info.taxonomica = soup.findAll("div", class_="grupo")[1].text
    
    info.substrato = siteFlora['substrato']
    info.formaVida = siteFlora['formaVida']
    info.endemismo = siteFlora['endemismo']
    info.origem = siteFlora['origem']
    info.vegetacao = siteFlora['tipoVegetacao']
    info.fitogeografico = siteFlora['dominioFitogeografico']

    DGC = ['distribuicaoGeografica-Nordeste', 'distribuicaoGeografica-CentroOeste', 'distribuicaoGeografica-Norte', 'distribuicaoGeografica-Sul', 'distribuicaoGeografica-Sudeste']
   
    for local in DGC:
        certeza = local.replace('-', 'Certeza')
        if(siteFlora[certeza]):
            pos1 = siteFlora[certeza].index('(') + 1
            pos2 = siteFlora[certeza].index(')')
            info.ocorenciaConfirmada = (siteFlora[certeza][pos1:pos2].split(', '))
        
        duvida = local.replace('-', 'Duvida')
        if(siteFlora[duvida]):
            pos1 = siteFlora[duvida].index('(') + 1
            pos2 = siteFlora[duvida].index(')')
            info.possiveisOcorrencias = (siteFlora[duvida][pos1:pos2].split(', '))
    info.printInfo()

# nomePlanta = 'Microlicia fasciculata'
# nomePlanta = 'limnobium laevigatum'
# fInfo = FloraInfo(nomePlanta)
# getInfoFlora(nomePlanta, fInfo, requisicaoFB(getURLID(nomePlanta)))
