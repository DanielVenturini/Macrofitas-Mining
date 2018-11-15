import requests

def urlFB(nomePlanta):
        return "http://servicos.jbrj.gov.br/flora/taxon/" + nomePlanta.replace(' ','%20')

def requisicaoFB(url):
    return requests.get(url).json()

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

def getSinonimosFlora(nomePlanta, jsonResp):
    sinonimos = []
    resp =  jsonResp['result']
    try:
        if(resp): 
            sinonimos = resp[0]["SINONIMO"]
        return sinonimos

    except Exception as ex:
        print("Erro: {0} -- {1}".format(nomePlanta, ex))
        return []
    
# nomePlanta = 'Sesuvium portulacastrum'
# getSinonimosFlora(nomePlanta, requisicaoFB(urlFB(nomePlanta)))
