import requests
from bs4 import BeautifulSoup
import time

def urlFB(nomePlanta):
    return "http://servicos.jbrj.gov.br/flora/taxon/" + nomePlanta.replace(' ','%20')

def requisicaoFB(url):
    for i in range(3):
        try:
            req = requests.get(url, timeout = 3).json()
            return req
        except:  
            print('Tentativa:',i + 1)
    return False

# deve retornar uma tupla: return validado, nomeValidado
#                                 'SIM'|'NAO', 'NOME CIENTIFICO DO SITE'
def dadosFB(nomePlanta, jsonResp, macrofita):
    # para cada um dos resultados
    try:
        if(jsonResp['result']):
            for result in jsonResp['result']:
                if result['taxonomicstatus'].__eq__('NOME_ACEITO'):     # se for um nome aceito
                    macrofita.statusFlora = 'Aceito'
                    macrofita.nomeFlora = result['scientificname']
                    macrofita.comaparaNome('flora')
                    macrofita.floraID = result['taxonid']
                elif(result['NOME ACEITO']):
                    for nome in result['NOME ACEITO']:
                        if nome['taxonomicstatus'].__eq__('NOME_ACEITO'):
                            macrofita.statusFlora = 'Sinonimo'
                            macrofita.nomeFlora = nome['scientificname']
                            macrofita.floraID = result['taxonid']
            macrofita.statusFlora = 'Sinonimo'
            macrofita.nomeFlora = macrofita.nomeEspecie
        else:
            return True
    except Exception as ex:
        print("Erro Flora: {0} -- {1}".format(nomePlanta, ex))
        return True

def getSinonimosFB(nomePlanta, jsonResp):
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
        return 'http://reflora.jbrj.gov.br/reflora/listaBrasil/ConsultaPublicaUC/ResultadoDaConsultaCarregaTaxonGrupo.do?&idDadosListaBrasil=' + resp["result"][0]["references"].split('=FB')[1]
    return False

def getInfoFlora(nomePlanta, info, jsonResp):
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
# fInfo = FloraInfo(nomePlanta)
# getInfoFlora(nomePlanta, fInfo, requisicaoFB(getURLID(nomePlanta)))
