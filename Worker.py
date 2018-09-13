# coding:UTF-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''

from OperacoesArquivo import (Reader, Writer)
import subprocess
import json
import sys

def getUrl(nomePlanta):
    return "curl -X GET --header 'Accept: text/html' 'http://servicos.jbrj.gov.br/flora/taxon/" + nomePlanta + "'"

def baixaArquivo(url):
    subprocess.getstatusoutput(url + ' -o arquivobaixado')

def start(nomeArquivo):

    leitor, escritor = None, None

    try:

        leitor, escritor = Reader().getLeitorEscritor(nomeArquivo)

    except FileNotFoundError:
        print("Arquivo nao existe")
        return

    try:
        while True:
            nomePlanta = leitor.getNome()
            baixaArquivo(getUrl(nomePlanta))            # baixando o arquivo JSON
            arquivo = json.load(open('arquivobaixado')) # convertendo para um objeto JSON

            if arquivo['result'] == None:
                print("Uma planta nao encontrada: " + nomePlanta)
                continue

            print(arquivo['result'][0]['genus'])
    except AttributeError:
        print("Fim do arquivo")
        escritor.fim()

# python3 Worker arquivo.csv
if sys.argv.__len__() == 2:
    start(sys.argv[1])
else:
    print("Erro. Use: python3 Worker.py arquivo.csv")

