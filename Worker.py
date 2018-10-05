# coding:UTF-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''

from floradobrasil import (requisicaoFB, urlFB, dadosFB)
from OperacoesArquivo import (Reader, Writer)
from plantlist import dadosPL
import sys

def start(nomeArquivo):

    try:
        leitor = Reader(nomeArquivo)
        escritor = Writer(nomeArquivo)
    except FileNotFoundError:
        return

    try:
        while True:
            nomePlanta = leitor.getNome()                       # recupera o nome da planta
            jsonResp = requisicaoFB(urlFB(nomePlanta))          # baixando o arquivo JSON

            # Foi encontrado no Flora do Brasil
            try:
                if jsonResp['result'] != None:
                    trocado, nomeAceito = dadosFB(nomePlanta, jsonResp)
                    if trocado.__eq__('SIM'):
                        print("Planta trocada: " + nomePlanta)
                    escritor.escreve(nomePlanta, 'SIM', 'Flora do Brasil', trocado, nomeAceito)
                    continue                                            # se acho no Flora do Brasil, vai para a próxima planta
            except Exception as ex:
                print(nomePlanta + ' -> ' + str(ex))

            print(nomePlanta + ' -> NAO ENCONTARADA NO FLORA DO BRASIL')
    except AttributeError:
        escritor.fim()          # fecha o arquivo de saida
        print("Fim do arquivo")

# python3 Worker arquivo.xlsx
if sys.argv.__len__() == 2:
    start(sys.argv[1])
else:
    print("Erro. Use: python3 Worker.py arquivo.xlsx")

