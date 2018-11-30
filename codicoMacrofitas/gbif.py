import requests
import math

def urlGB(nomePlanta,offset,limit = 300):
    return "http://api.gbif.org/v1/occurrence/search?limit="+str(limit)+"&offset="+str(offset)+"&continent=SOUTH_AMERICA&scientificName=" +nomePlanta.replace(' ','%20')

def requisicaoGB(url):
        cont = 0; 
        while True:
                if cont < 5 :
                        try:
                                return requests.get(url,timeout=2).json()
                        except requests.exceptions.RequestException as ex:
                                print("Erro : " + str(ex))
                                cont+=1
        

# def getCoordenadas(latitude, longitude):
#     try:
#         latitude = re.match(['[+|-]?[\d]+(.[\d]+)?', latitude)
#         longitude = re.match(['[+|-]?[\d]+(.[\d]+)?', longitude)
#         return latitude, longitude
#     except AttributeError:
#         return ' ', ' '

def dadosGB1(jsonResp, nomedaPlanta, escritor):
        print(jsonResp)
        linha = []
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
                                print(localidade)
                                #escritor.escreve([nomedaPlanta, latitude, longitude, localidade])
                                nomedaPlanta = ''
        except Exception as ex:
                print("Erro Ao capturar os dados GBIF : " + ex)

def dadosGB(nomePlanta, escritor):
        numReg = numeroRegistro(nomePlanta)
        numReg = math.ceil(numReg/300)

        for offset in range(0, numReg):
                url = urlGB(nomePlanta, offset*300)
                print(url)
                dadosGB1(requisicaoGB(url), nomePlanta, escritor)

        print('FIMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')

def numeroRegistro(nomePlanta):
        url = urlGB(nomePlanta, 0,1)
        print('url numero'+ url)
        jsonResp = requisicaoGB(url)
        return(jsonResp['count'])
