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

def validador(nomePlanta, macrofita, jsonRespFloraBrasil, jsonRespPlantlist, escritorValidado, escritorSinonimos):
    # Pesquisa Flora do Brasil
            try:
                if jsonRespFloraBrasil['result'] != None:
                    dadosFB(nomePlanta, jsonRespFloraBrasil, macrofita, escritorSinonimos)
            except (Exception, requests.exceptions.ConnectionError) as ex:
                print('Flora do Brasil', nomePlanta + ' -> ' + str(ex))

            # Pesquisa Plantlist
            try:
                dadosPL(nomePlanta, macrofita, jsonRespPlantlist)
            except (Exception, requests.exceptions.ConnectionError) as ex:
                print('Plantlist: ' + nomePlanta + ' -> ' + str(ex))

            macrofita.comparaFloraPlantlist()
            escritorValidado.escreve(macrofita.saidaStringExcel())

def start(nomeArquivo):
    count = 1
    try:
        leitor = Reader(nomeArquivo)
        escritorValidado = Writer(nomeArquivo, ['Nome Especie', 'Status Flora', 'Nome Flora', 'Observacao', 'Status Plantlist', 'Nome Plantlist', 'Observacao', 'Flora x Plantlist'])
        escritorSinonimos = Writer(nomeArquivo, ['Nome das espécies - Status Flora = ACEITO', 'Sinônimos Relevantes'])
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
                jsonRespPlantlist = requisicaoPL(urlPL(nomePlanta))
            except (requests.exceptions.ConnectionError) as ex:
                print(nomePlanta + ' -> ' + str(ex))

            print(count , ')- ', nomePlanta)
            count += 1
            macrofita = Macrofita(nomePlanta + ' ' + nomeAutor)
            #'''
            # Pesquisa Flora do Brasil
            try:
                if jsonRespFloraBrasil['result'] != None:
                    dadosFB(nomePlanta, jsonRespFloraBrasil, macrofita, escritorSinonimos)
            except (requests.exceptions.ConnectionError) as ex:
                print('Flora do Brasil',nomePlanta + ' -> ' + str(ex))

            # Pesquisa Plantlist
            try:
                dadosPL(nomePlanta, macrofita, jsonRespPlantlist)
            except (requests.exceptions.ConnectionError) as ex:
                print('Plantlist: ' + nomePlanta + ' -> ' + str(ex))
            #'''
            macrofita.comparaFloraPlantlist()
            escritorValidado.escreve(macrofita.saidaStringExcel())

            validador(nomePlanta, macrofita, jsonRespFloraBrasil, jsonRespPlantlist, escritorValidado, escritorSinonimos) # Primeira tabela

    except AttributeError:
        escritorValidado.fim('VALIDADOS')           # fecha o arquivo de saida
        escritorSinonimos.fim('SINONIMOS')          # fecha o arquivo de sinônimos
        print("Fim dos trabalhos da Release 2")

# python3 Worker arquivo.xlsx
if sys.argv.__len__() == 2:
    start(sys.argv[1])
else:
    print("Erro. Use: python3 Worker.py arquivo.xlsx")
