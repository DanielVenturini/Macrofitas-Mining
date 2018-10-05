def urlFB(nomePlanta):
        return "http://servicos.jbrj.gov.br/flora/taxon/" + nomePlanta.replace(' ','%20')

def requisicaoFB(requests, url):
    return requests.get(url).json()

# deve retornar uma tupla: return validado, nomeValidado
#                                 'SIM'|'NAO', 'NOME CIENTIFICO DO SITE'
def dadosFB(nomePlanta, jsonResp):
    # para cada um dos resultados
    for result in jsonResp['result']:
        if result['taxonomicstatus'].__eq__('NOME_ACEITO'):     # se for um nome aceito
            print(nomePlanta + ' -- ' + '+')
            return 'SIM', result['scientificname']              # retorna 'SIM' e o nome completo do site
        else:
            for nome in result['NOME ACEITO']:                  # 
                if nome['taxonomicstatus'].__eq__('NOME_ACEITO'):
                    return 'NAO', nome['scientificname']

    raise Exception("PlantaNãoEncontradaErro: '{0}'".format(nomePlanta))