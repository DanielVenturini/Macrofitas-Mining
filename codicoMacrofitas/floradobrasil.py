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
        for result in jsonResp['result']:
            if result['taxonomicstatus'].__eq__('NOME_ACEITO'):     # se for um nome aceito
                macrofita.statusFlora = 'Aceito'
                macrofita.nomeFlora = result['scientificname']
                macrofita.comaparaNome('flora')
                return macrofita
            else:
                for nome in result['NOME ACEITO']:
                    if nome['taxonomicstatus'].__eq__('NOME_ACEITO'):
                        macrofita.statusFlora = 'Sinonimo'
                        macrofita.nomeFlora = nome['scientificname']
                        return macrofita
                macrofita.statusFlora = 'Sinonimo'
                macrofita.nomeFlora = nomePlanta
                return macrofita
    except Exception as ex:
        print("PlantaNãoEncontradaErro: {0} -- {1}".format(nomePlanta, ex))
