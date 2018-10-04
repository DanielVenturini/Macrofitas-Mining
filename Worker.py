# coding:UTF-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''

from OperacoesArquivo import Reader
import requests
import sys

def getUrl(nomePlanta):
    return "http://servicos.jbrj.gov.br/flora/taxon/" + nomePlanta

def requisicao(url):
    return requests.get(url).json()

def start(nomeArquivo):

    leitor, escritor = None, None

    try:
        leitor = Reader(nomeArquivo)
    except FileNotFoundError:
        return

    try:
        while True:
            nomePlanta = leitor.getNome()               # recupera o nome da planta
            jsonResp = requisicao(getUrl(nomePlanta))   # baixando o arquivo JSON

            if jsonResp['result'] == None:
                print(nomePlanta.replace('%20', ' ') + ' -- ' + "ERR")
                continue

            print(nomePlanta.replace('%20', ' ') + ' -- ' + 'OK!')
    except AttributeError:
        print("Fim do arquivo")

# python3 Worker arquivo.xlsx
if sys.argv.__len__() == 2:
    start(sys.argv[1])
else:
    print("Erro. Use: python3 Worker.py arquivo.xlsx")

