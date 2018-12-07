import requests
import math
import time

def urlGB(nomePlanta,offset,limit = 300):
    return "http://api.gbif.org/v1/occurrence/search?limit="+str(limit)+"&offset="+str(offset)+"&continent=SOUTH_AMERICA&scientificName=" +nomePlanta.replace(' ','%20')

def requisicaoGB(url):
    for i in range(0, 50):
        resultado = None
        try:
            resultado = requests.get(url,timeout=15).json()
            return resultado
        except requests.exceptions.RequestException as ex:
            print("ErroGBIF : " + str(ex), url)
            if(i>10):
                time.sleep(5)    
            else:
                time.sleep(2)    

        except:
            time.sleep(5)

        print("TentativaGBIF {0}".format(i))

    print("Terminado as tentativas")
    return False

def dadosGB1(jsonResp, coordenadas):
    if not jsonResp:
        raise Exception

    try:
        for result in jsonResp['results']:
            localidade = ''
            latitude = 0
            longitude = 0
            try:
                localidade = result['locality']
            except Exception as ex:
                localidade = ''
            try: 
                latitude = result['decimalLatitude']
                longitude = result['decimalLongitude']
            except Exception as notLatitude:
                latitude = 0
                longitude = 0
            if(latitude != 0 and longitude != 0):
                coordenadas.append(str(latitude) + '!#' + str(longitude) + '!#' + localidade)

    except Exception as ex:
        print("Erro Ao capturar os dados GBIF : " + ex)

def dadosGB(nomePlanta):
    numReg = numeroRegistro(nomePlanta)
    numReg = math.ceil(numReg/300)

    coordenadas = []
    try:
        for offset in range(0, numReg):
            url = urlGB(nomePlanta, offset*300)
            dadosGB1(requisicaoGB(url), coordenadas)

        return coordenadas
    except Exception:
        return coordenadas

def numeroRegistro(nomePlanta):
    url = urlGB(nomePlanta, 0,1)
    jsonResp = requisicaoGB(url)
    if jsonResp['results']:
        return(jsonResp['count'])
    else:
        return 0