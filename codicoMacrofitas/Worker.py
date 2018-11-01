# coding:utf-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''

from floradobrasil import (requisicaoFB, urlFB, dadosFB)
from OperacoesArquivo import (Reader, Writer)
from plantlist import dadosPL, requisicaoPL, urlPL
from macrofita import Macrofita
import requests
import sys

def start(nomeArquivo):
    cont = 1
    try:
        leitor = Reader(nomeArquivo)
        escritor = Writer(nomeArquivo, ['Nome Especie', 'Status Flora', 'Nome Flora', 'Observacao', 'Status Plantlist', 'Nome Plantlist', 'Observacao', 'Flora x Plantlist'])
    except FileNotFoundError:
        return

    '''
    Release 2
    '''
    try:
        while True:
            
            try:
                nomePlanta, nomeAutor = leitor.getNome()            # recupera o nome da planta
                jsonRespFloraBrasil = requisicaoFB(urlFB(nomePlanta))     
                jasonRespPlantlist = requisicaoPL(urlPL(nomePlanta))
            except (Exception, requests.exceptions.ConnectionError) as ex:
                print(nomePlanta + ' -> ' + str(ex))

            print(cont , ')- ', nomePlanta)
            cont += 1
            macrofita = Macrofita(nomePlanta + ' ' + nomeAutor)

            # Pesquisa Flora do Brasil
            try:
                if jsonRespFloraBrasil['result'] != None:
                    dadosFB(nomePlanta, jsonRespFloraBrasil, macrofita)
            except (Exception, requests.exceptions.ConnectionError) as ex:
                print('Flora do Brasil',nomePlanta + ' -> ' + str(ex))

            # Pesquisa Plantlist
            try:
                dadosPL(nomePlanta, macrofita, jasonRespPlantlist)
            except (Exception, requests.exceptions.ConnectionError) as ex:
                print('Plantlist: ' + nomePlanta + ' -> ' + str(ex))
            
            macrofita.comparaFloraPlantlist()
            escritor.escreve(macrofita.saidaStringExcel())

    except AttributeError:
        escritor.fim(nomeArquivo + '_VALIDADOS')       # fecha o arquivo de saida
        print("Fim dos trabalhos da Release 2")

# python3 Worker arquivo.xlsx
if sys.argv.__len__() == 2:
    start(sys.argv[1])
else:
    print("Erro. Use: python3 Worker.py arquivo.xlsx")
