# coding:utf-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''

from floradobrasil import (requisicaoFB, urlFB, dadosFB, getSinonimosFB)
from OperacoesArquivo import (Reader, Writer)
from plantlist import (dadosPL, requisicaoPL, urlPL, getSinonimosPL)
from macrofita import Macrofita
import requests
import sys

#-----------------------------------#
#   VALIDA A LISTA DE MACRÓFITAS    #
#-----------------------------------#
def release1(nomeArquivo):
    count = 1
    leitor = Reader(nomeArquivo)
    escritorValidado = Writer(nomeArquivo, ['Nome Especie', 'Status Flora', 'Nome Flora', 'Observacao', 'Status Plantlist', 'Nome Plantlist', 'Observacao', 'Flora x Plantlist'])

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

            # Pesquisa Flora do Brasil
            try:
                if jsonRespFloraBrasil['result'] != None:
                    escrever = dadosFB(nomePlanta, jsonRespFloraBrasil, macrofita)
                else:
                    escrever = True
            except (requests.exceptions.ConnectionError) as ex:
                print('Flora do Brasil',nomePlanta + ' -> ' + str(ex))
                escrever = True     # se os sinonimos ainda não foram escritos na função dadosFB

            # Pesquisa Plantlist
            try:
                dadosPL(nomePlanta, macrofita, jsonRespPlantlist)
            except (requests.exceptions.ConnectionError) as ex:
                print('Plantlist: ' + nomePlanta + ' -> ' + str(ex))

            validador(nomePlanta, macrofita, jsonRespFloraBrasil, jsonRespPlantlist, escritorValidado)

    except AttributeError:
        escritorValidado.fim('VALIDADOS')           # fecha o arquivo de saida


def validador(nomePlanta, macrofita, jsonRespFloraBrasil, jsonRespPlantlist, escritorValidado):
    # Pesquisa Flora do Brasil
    try:
        if jsonRespFloraBrasil['result'] != None:
            dadosFB(nomePlanta, jsonRespFloraBrasil, macrofita)
    except (Exception, requests.exceptions.ConnectionError) as ex:
        print('Flora do Brasil', nomePlanta + ' -> ' + str(ex))

    # Pesquisa Plantlist
    try:
        dadosPL(nomePlanta, macrofita, jsonRespPlantlist)
    except (Exception, requests.exceptions.ConnectionError) as ex:
        print('Plantlist: ' + nomePlanta + ' -> ' + str(ex))

    macrofita.comparaFloraPlantlist()
    escritorValidado.escreve(macrofita.saidaStringExcel())

#-----------------------------------#
#   RECUPERA A LISTA DE SINÔNIMOS   #
#-----------------------------------#
def release2(nomeArquivo):
    count = 1
    leitor = Reader(nomeArquivo)
    escritorSinonimos = Writer(nomeArquivo, ['Nome das espécies - Status Flora = ACEITO', 'Sinônimos Relevantes'])

    try:
        while True:

            nomePlanta, nomeAutor = leitor.getNome()            # recupera o nome da planta
            jsonRespFloraBrasil = requisicaoFB(urlFB(nomePlanta))

            sinonimos = getSinonimosFB(nomePlanta, jsonRespFloraBrasil)

            print(count , ')- ', nomePlanta)
            count += 1

            if sinonimos.__len__() > 0:
                salvaSinonimos(nomePlanta, escritorSinonimos, sinonimos)
                continue

            jsonRespPlantlist = requisicaoPL(urlPL(nomePlanta))
            sinonimos = getSinonimosPL(nomePlanta, jsonRespPlantlist)

            salvaSinonimos(nomePlanta, escritorSinonimos, sinonimos)
    except AttributeError:
        escritorSinonimos.fim('SINONIMOS')          # fecha o arquivo de sinônimos


def salvaSinonimos(nomePlanta, escritor, sinonimos):
    print(sinonimos)
    linha = [0, 1]                  # lista com duas posicoes
    primeiraColuna = nomePlanta     # apenas para escrever no arquivo no padrão requerido
    for sinonimo in sinonimos:
        linha[0] = primeiraColuna
        try:
            linha[1] = sinonimo['scientificname']
        except TypeError:
            linha[1] = sinonimo

        escritor.escreve(linha)
        primeiraColuna = ''         # assim, deixando no padrão

    escritor.escreve(['', ''])      # apenas quebrando uma linha



def valida(nomeArquivo):
    count = 1
    try:
        leitor = Reader(nomeArquivo)
        escritorValidado = Writer(nomeArquivo, ['Nome Especie', 'Status Flora', 'Nome Flora', 'Observacao', 'Status Plantlist', 'Nome Plantlist', 'Observacao', 'Flora x Plantlist'])
        escritorSinonimos = Writer(nomeArquivo, ['Nome das espécies - Status Flora = ACEITO', 'Sinônimos Relevantes'])
        #escritorCoordenadas = Writer(nomeArquivo, ['Nome das espécies', 'Latitude', 'Longitude', 'Localizacao'])
    except FileNotFoundError:
        return

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
            # try:
            #     if jsonRespFloraBrasil['result'] != None:
            #         escrever = dadosFB(nomePlanta, jsonRespFloraBrasil, macrofita, escritorSinonimos)
            #     else:
            #         escrever = True
            # except (requests.exceptions.ConnectionError) as ex:
            #     print('Flora do Brasil',nomePlanta + ' -> ' + str(ex))
            #     escrever = True     # se os sinonimos ainda não foram escritos na função dadosFB

            # # Pesquisa Plantlist
            # try:
            #     dadosPL(nomePlanta, macrofita, jsonRespPlantlist, escritorSinonimos, escrever)
            # except (requests.exceptions.ConnectionError) as ex:
            #     print('Plantlist: ' + nomePlanta + ' -> ' + str(ex))
            # #'''

            validador(nomePlanta, macrofita, jsonRespFloraBrasil, jsonRespPlantlist, escritorValidado) # Primeira tabela

            # macrofita.comparaFloraPlantlist()
            # escritorValidado.escreve(macrofita.saidaStringExcel())


    except AttributeError:
        escritorValidado.fim('VALIDADOS')           # fecha o arquivo de saida
        escritorSinonimos.fim('SINONIMOS')          # fecha o arquivo de sinônimos
        escritorCoordenadas.fim('COORDENADAS')      # fecha o arquivo das coordenadas
        print("Arquivos VALIDADOS, SINONIMOS e COORDENADAS prontos.")

def ocorrencias(nomeArquivo):
    nomeArquivo += '_VALIDADOS.xlsx'                # reabre o arquivo gerado na outra função