import requests
import math
import time

def urlGB(nomePlanta,offset,limit = 300):
    return "http://api.gbif.org/v1/occurrence/search?limit="+str(limit)+"&offset="+str(offset)+"&continent=SOUTH_AMERICA&scientificName=" +nomePlanta.replace(' ','%20')

def requisicaoGB(url):
        for i in range(0, 20):
                resultado = None
                try:
                        resultado = requests.get(url,timeout=1).json()
                        return resultado
                except requests.exceptions.RequestException as ex:
                        print("ErroGBIF : " + str(ex))
                        time.sleep(0.1)    
                except:
                        time.sleep(0.1)

                print("Tentativa {0}".format(i))

        print("Terminado as tentativas")
        return False

# def getCoordenadas(latitude, longitude):
#     try:
#         latitude = re.match(['[+|-]?[\d]+(.[\d]+)?', latitude)
#         longitude = re.match(['[+|-]?[\d]+(.[\d]+)?', longitude)
#         return latitude, longitude
#     except AttributeError:
#         return ' ', ' '

def dadosGB1(jsonResp, nomedaPlanta, escritor):
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
                                escritor.escreve([nomedaPlanta, str(latitude), str(longitude), localidade])
                                nomedaPlanta = ''
        except Exception as ex:
                print("Erro Ao capturar os dados GBIF : " + ex)

def dadosGB(nomePlanta, escritor):
        numReg = numeroRegistro(nomePlanta)
        numReg = math.ceil(numReg/300)

        try:
                for offset in range(0, numReg):
                        url = urlGB(nomePlanta, offset*300)
                        dadosGB1(requisicaoGB(url), nomePlanta, escritor)

        except Exception:
                return

def numeroRegistro(nomePlanta):
        url = urlGB(nomePlanta, 0,1)
        jsonResp = requisicaoGB(url)
        if jsonResp['results']:
                return(jsonResp['count'])
        else:
                return 0
