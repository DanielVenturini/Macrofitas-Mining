import requests

def urlGB(nomePlanta,offset):
    return "http://api.gbif.org/v1/occurrence/search?limit=300&offset="+str(offset)+"&continent=SOUTH_AMERICA&scientificName=" +nomePlanta.replace(' ','%20')

def requisicaoGB(url):
    try:
        return requests.get(url,timeout=2).json()
    except requests.exceptions.RequestException as ex:
        print("Err: " + str(ex))
        return requisicaoGB(url)

# def getCoordenadas(latitude, longitude):
#     try:
#         latitude = re.match(['[+|-]?[\d]+(.[\d]+)?', latitude)
#         longitude = re.match(['[+|-]?[\d]+(.[\d]+)?', longitude)
#         return latitude, longitude
#     except AttributeError:
#         return ' ', ' '

def dadosGB(jsonResp):
        lista = []
        try:
                for result in jsonResp['results']:
                                print(result['key'])
        except Exception as ex:
                print("Err dadosGB: " + ex)

def buscar(nomePlanta,offset):
        url = urlGB(nomePlanta, offset)
        print(url)
        dadosGB(requisicaoGB(url))
