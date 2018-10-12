# coding:utf-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''

from floradobrasil import (requisicaoFB, urlFB, dadosFB)
from OperacoesArquivo import (Reader, Writer)
from plantlist import dadosPL
from macrofita import Macrofita
import requests
import sys

def start(nomeArquivo):
    cont = 1
    try:
        leitor = Reader(nomeArquivo)
        escritor = Writer(nomeArquivo)
    except FileNotFoundError:
        return

    try:
        while True:
            
            nomePlanta, nomeAutor = leitor.getNome()            # recupera o nome da planta
            jsonResp = requisicaoFB(urlFB(nomePlanta))          # baixando o arquivo JSON
            print(cont , ')- ', nomePlanta)
            cont += 1
            macrofita = Macrofita(nomePlanta)

            # Foi encontrado no Flora do Brasil
            try:
                if jsonResp['result'] != None:
                    dadosFB(nomePlanta, nomeAutor, jsonResp, macrofita)
            except (Exception, requests.exceptions.ConnectionError) as ex:
                print(nomePlanta + ' -> ' + str(ex))

            # se não foi encontrada no Flora do Brasil
            try:
                dadosPL(nomePlanta, macrofita)
            except (Exception, requests.exceptions.ConnectionError) as ex:
                print('\n\n' + nomePlanta + ' -> ' + str(ex) + '\n\n')
            
            macrofita.printMacrofita()
            escritor.escreve(macrofita.saidaStringExel())

    except AttributeError:
        escritor.fim()          # fecha o arquivo de saida
        print("Fim do arquivo")

# python3 Worker arquivo.xlsx
if sys.argv.__len__() == 2:
    start(sys.argv[1])
else:
    print("Erro. Use: python3 Worker.py arquivo.xlsx")