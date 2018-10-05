# coding:UTF-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''

from floradobrasil import (requisicaoFB, urlFB, dadosFB)
from OperacoesArquivo import (Reader, Writer)
import requests
import sys

def getUrl(nomePlanta, site):
    if site.__eq__('FB'):
        return "http://servicos.jbrj.gov.br/flora/taxon/" + nomePlanta.replace(' ','%20')
    elif site.__eq__('PL'):
        return "link"

def start(nomeArquivo):

    try:
        leitor = Reader(nomeArquivo)
        escritor = Writer(nomeArquivo)
    except FileNotFoundError:
        return

    try:
        while True:
            nomePlanta = leitor.getNome()                               # recupera o nome da planta
            jsonResp = requisicaoFB(requests, getUrl(nomePlanta, 'FB')) # baixando o arquivo JSON

            # Foi encontrado no Flora do Brasil
            try:
                if jsonResp['result'] != None:
                    validado, nomeValidado = dadosFB(nomePlanta, jsonResp)
                    #print(validado)
                    #print(nomeValidado)
                    escritor.escreve(nomePlanta, validado, 'Flora do Brasil', nomeValidado)
                    continue
            except Exception as ex:
                print(nomePlanta + ' -> ' + str(ex))

            #print(nomePlanta + ' -- ' + 'ERR!')
            #plResp = requisicaoPL(getUrl(nomePlanta, 'PL'))     # recuperando dados do PlantList
            
    except AttributeError:
        escritor.fim()          # fecha o arquivo de saida
        print("Fim do arquivo")

# python3 Worker arquivo.xlsx
if sys.argv.__len__() == 2:
    start(sys.argv[1])
else:
    print("Erro. Use: python3 Worker.py arquivo.xlsx")

