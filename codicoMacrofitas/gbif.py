import requests

def urlGB(nomePlanta,offset):
    return "http://api.gbif.org/v1/occurrence/search?limit=1&offset="+str(offset)+"&continent=SOUTH_AMERICA"
    +"scientificName=" + nomePlanta.replace(' ','%20')
   

def requisicaoGB(url):
    try:
        return requests.get(url).json()
    except Exception as ex:
        print("Err: " + str(ex))
        return requisicaoGB(url)

def dadosGB(jsonResp):
    try:
        if(jsonResp['results']):
            for result in jsonResp['results']:
                print(result['stateProvince'])

    except Exception as ex:
        print("Erro")
url = urlGB("justicia pectoralis",10)

dadosGB(requisicaoGB(url))
