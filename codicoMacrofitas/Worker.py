# coding:utf-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''
from floradobrasil import (requisicaoFB, urlFB, dadosFB, getSinonimosFB)
from OperacoesArquivo import (Reader, Writer)
from plantlist import (dadosPL, requisicaoPL, urlPL, getSinonimosPL)
from specieslink import (requisicaoSL, dadosSL)
from macrofita import Macrofita
import requests
import os.path
import sys

#-----------------------------------#
#   VALIDA A LISTA DE MACRÓFITAS    #
#-----------------------------------#
def release1(parametros):
    count = 1
    nomeArquivo = parametros['arquivoEntrada']
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
                if(jsonRespFloraBrasil and jsonRespFloraBrasil['result'] != None):
                    dadosFB(nomePlanta, jsonRespFloraBrasil, macrofita)
            except (Exception, requests.exceptions.ConnectionError) as ex:
                print('Flora do Brasil', nomePlanta + ' -> ' + str(ex))

            # Pesquisa Plantlist
            try:
                if(jsonRespFloraBrasil):
                    dadosPL(nomePlanta, macrofita, jsonRespPlantlist)
            except (Exception, requests.exceptions.ConnectionError) as ex:
                print('Plantlist: ' + nomePlanta + ' -> ' + str(ex))

            macrofita.comparaFloraPlantlist()
            escritorValidado.escreve(macrofita.saidaStringExcel())

    except AttributeError:
        arquivoSaida = escritorValidado.fim('VALIDADOS')            # fecha o arquivo de saida
        parametros['arquivoSaida'] = arquivoSaida
        arquivoSaida = os.path.relpath(arquivoSaida)                # caminho relativo
        mensagem = parametros['msgRetorno'].format(arquivoSaida)
        parametros['funcaoRetorno'](mensagem)

#-----------------------------------#
#   RECUPERA A LISTA DE SINÔNIMOS   #
#-----------------------------------#
def release2(parametros):
    count = 1
    nomeArquivo = parametros['arquivoEntrada']
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
        arquivoSaida = escritorSinonimos.fim('SINONIMOS')           # fecha o arquivo de saida
        parametros['arquivoSaida'] = arquivoSaida
        arquivoSaida = os.path.relpath(arquivoSaida)                # caminho relativo
        mensagem = parametros['msgRetorno'].format(arquivoSaida)
        parametros['funcaoRetorno'](mensagem)


def salvaSinonimos(nomePlanta, escritor, sinonimos):
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


#-----------------------------------#
#      RECUPERA AS COORDENADAS      #
#-----------------------------------#
def release4(parametros):
    count = 1
    nomeArquivo = parametros['arquivoEntrada']
    leitor = Reader(nomeArquivo)
    escritorCoordenadas = Writer(nomeArquivo, ['Nome das espécies', 'Latitude', 'Longitude', 'Localização'])

    try:
        while True:
            nomePlanta, nomeAutor = leitor.getNome()            # recupera o nome da planta
            print(count , ')- ', nomePlanta)
            count += 1
            ocorrencia = dadosSL(requisicaoSL(nomePlanta), nomePlanta, escritorCoordenadas)

    except AttributeError:
        arquivoSaida = escritorCoordenadas.fim('OCORRENCIAS')       # fecha o arquivo de saida
        parametros['arquivoSaida'] = arquivoSaida
        arquivoSaida = os.path.relpath(arquivoSaida)                # caminho relativo
        mensagem = parametros['msgRetorno'].format(arquivoSaida)
        parametros['funcaoRetorno'](mensagem)
