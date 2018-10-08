# coding:UTF-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''

from floradobrasil import (requisicaoFB, urlFB, dadosFB)
from OperacoesArquivo import (Reader, Writer)
from plantlist import dadosPL2
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
            nomePlanta = leitor.getNome()                       # recupera o nome da planta
            jsonResp = requisicaoFB(urlFB(nomePlanta))          # baixando o arquivo JSON
            print(cont , ')- ', nomePlanta)
            cont += 1

            # Foi encontrado no Flora do Brasil
            try:
                if jsonResp['result'] != None:
                    trocado, nomeAceito = dadosFB(nomePlanta, jsonResp)
                    #escritor.escreve(nomePlanta, 'SIM', 'Flora do Brasil', trocado, nomeAceito)                    
                    continue                                            # se acho no Flora do Brasil, vai para a próxima planta
            except (Exception, requests.exceptions.ConnectionError) as ex:
                print(nomePlanta + ' -> ' + str(ex))

            # se não foi encontrada no Flora do Brasil
            resp = dadosPL2(nomePlanta)
            if resp['checked']:
                if resp['nameAccepted'].__len__():
                    escritor.escreve(nomePlanta, resp['checked'], 'Plant List',
                                     resp['trocado'], resp['nameAccepted'], resp['message'])
                elif not resp['message'].__len__():
                    escritor.escreve(nomePlanta, resp['checked'], 'Plant List',
                                     resp['trocado'], nomePlanta , 'So possui sinonimos')
                else:
                    escritor.escreve(
                        nomePlanta, resp['checked'], 'Plant List', resp['trocado'], ' ', resp['message'])
            else:
                escritor.escreve(
                    nomePlanta, resp['checked'], ' ', ' ', ' ', 'Dados Incorretos')

    except AttributeError:
        escritor.fim()          # fecha o arquivo de saida
        print("Fim do arquivo")

# python3 Worker arquivo.xlsx
if sys.argv.__len__() == 2:
    start(sys.argv[1])
else:
    print("Erro. Use: python3 Worker.py arquivo.xlsx")

