# coding:UTF-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''

from OperacoesArquivo import Reader
import requests
import sys

def getUrl(nomePlanta, site):
    if site.__eq__('FB'):
        return "http://servicos.jbrj.gov.br/flora/taxon/" + nomePlanta.replace(' ','%20')
    elif site.__eq__('PL'):
        return "link"

def requisicaoFB(url):
    return requests.get(url).json()

def requisicaoPL(url):
    return True

def start(nomeArquivo):

    try:
        leitor = Reader(nomeArquivo)
    except FileNotFoundError:
        return

    try:
        while True:
            nomePlanta = leitor.getNome()                           # recupera o nome da planta
            jsonResp = requisicaoFB(getUrl(nomePlanta, 'FB'))   # baixando o arquivo JSON

            if jsonResp['result'] != None:
                print(nomePlanta + ' -- ' + 'OK!')
                continue

            print(nomePlanta + ' -- ' + 'ERR!')
            plResp = requisicaoPL(getUrl(nomePlanta, 'PL'))     # recuperando dados do PlantList
            
    except AttributeError:
        print("Fim do arquivo")

# python3 Worker arquivo.xlsx
if sys.argv.__len__() == 2:
    start(sys.argv[1])
else:
    print("Erro. Use: python3 Worker.py arquivo.xlsx")

