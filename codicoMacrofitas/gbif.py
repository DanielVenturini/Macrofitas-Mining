import requests

def urlGB(nomePlanta,offset):
    return "http://api.gbif.org/v1/occurrence/search?limit=1&offset="+str(offset)+"&continent=SOUTH_AMERICA&scientificName=" +nomePlanta.replace(' ','%20')

def requisicaoGB(url):
    try:
        return requests.get(url,timeout=2).json()
    except requests.exceptions.RequestException as ex:
        print("Err: " + str(ex))
        return requisicaoGB(url)

def getCoordenadas(latitude, longitude):
    try:
        latitude = re.match(['[+|-]?[\d]+(.[\d]+)?', latitude)
        longitude = re.match(['[+|-]?[\d]+(.[\d]+)?', longitude)

        return latitude, longitude
    except AttributeError:
        return ' ', ' '

def dadosGB(jsonResp):
    try:
        for result in jsonResp['results']:
            print(result['decimalLatitude'], result['decimalLongitude'], result['country'] + ' ' + result['stateProvince'] + ' ' + result['locality'])
    except Exception as ex:
        print("Err dadosGB: " + ex)

url = urlGB("Victoria amazonica", 10)
print(url)
dadosGB(requisicaoGB(url))
