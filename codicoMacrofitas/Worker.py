# coding:utf-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''
from floradobrasil import (requisicaoFB, urlFB, dadosFB,getSinonimosFB, getInfoFlora, getURLID)
from plantlist import (dadosPL, requisicaoPL, urlPL, getSinonimosPL)
from specieslink import (requisicaoSL, dadosSL)
from OperacoesArquivo import (Reader, Writer)
from gbif import (requisicaoGB, dadosGB)
from macrofita import Macrofita
from floraInfo import FloraInfo
from tkinter import END
import requests
import os.path
import sys

#-----------------------------------#
#   VALIDA A LISTA DE MACRÓFITAS    #
#-----------------------------------#
def release1(parametros):
    count = 1
    lista = parametros['lista']
    nomeArquivo = parametros['arquivoEntrada']
    leitor = Reader(nomeArquivo)
    escritorValidado = Writer(nomeArquivo, ['Nome Especie', 'Status Flora', 'Nome Flora', 'Observacao', 'Status Plantlist', 'Nome Plantlist', 'Observacao', 'Flora x Plantlist'])

    lista.insert(END, 'VALIDANDO OS NOMES')
    try:
        while True:
            try:
                nomePlanta, nomeAutor = leitor.getNome()            # recupera o nome da planta
                if nomePlanta.lower().__contains__('nome especie'):
                    continue

                jsonRespFloraBrasil = requisicaoFB(urlFB(nomePlanta))
                jsonRespPlantlist = requisicaoPL(urlPL(nomePlanta))
            except (requests.exceptions.ConnectionError) as ex:
                print(nomePlanta + ' -> ' + str(ex))

            lista.insert(END, '{0} -> {1}'.format(count, nomePlanta))
            lista.yview(END)
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
    lista = parametros['lista']
    nomeArquivo = parametros['arquivoEntrada']
    leitor = Reader(nomeArquivo)
    escritorFlora = Writer(nomeArquivo, ['Nome Especie', 'Sinônimos Relevantes'])

    lista.insert(END, 'RECUPERANDO OS SINÔNIMOS')
    try:
        while True:

            nomePlanta, statusFlora, nomeFlora, statusPlantlist, nomePlantlist, comparacao = leitor.getLinha()
            if statusFlora == None or statusPlantlist == None or statusFlora.lower().__contains__('status flora'):
                continue

            # printa o nome da planta
            lista.insert(END, '{0} -> {1}'.format(count, nomePlanta))
            lista.yview(END)
            count += 1

            apagar = False
            try:
                verificaStatus(nomePlanta, statusFlora, nomeFlora)  # verifica se possúi um nome aceito

                jsonRespFloraBrasil = requisicaoFB(urlFB(nomeFlora))
                sinonimos = getSinonimosFB(nomeFlora, jsonRespFloraBrasil)

                salvaSinonimos(nomeFlora, escritorFlora, sinonimos)
                continue

            except Exception:
                apagar = True   # diz para apagar a linha se no plant list também não tiver

            try:
                verificaStatus(nomePlanta, statusPlantlist, nomePlantlist)      # se não tiver nome aceito, então gera exceção

                jsonRespPlantlist = requisicaoPL(urlPL(nomePlantlist))
                sinonimos = getSinonimosPL(nomePlantlist, jsonRespPlantlist)

                salvaSinonimos(nomePlantlist, escritorFlora, sinonimos)
            except Exception as ex:
                if apagar:
                    count -= 1
                    lista.delete(0, END) # clear

    except AttributeError as ex:
        # salva os arquivos
        arquivoSaidaFB = escritorFlora.fim('SINONIMOS')
        # recupera o caminho relativo
        arquivoSaidaFB = os.path.relpath(arquivoSaidaFB)
        # printa a mensagem de erro
        mensagem = parametros['msgRetorno'].format(arquivoSaidaFB)
        parametros['funcaoRetorno'](mensagem)


def verificaStatus(nomePlanta, status, nomePlataforma):

    if status.__eq__('Aceito'):
        return

    # se for um sinônimos e estes nomes forem iguais
    # então é porque não foi encontrado um nome aceito
    if nomePlanta.__eq__(nomePlataforma):
        raise Exception

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
#      RECUPERA INFORMAÇÔES FLORA   #
#-----------------------------------#
def release3(parametros):
    i = 0
    
    lista = parametros['lista']
    nomeArquivo = parametros['arquivoEntrada']
    leitor = Reader(nomeArquivo)
    count = 0
    escritorFloraInfo = Writer(nomeArquivo, ['Nome das espécies - Status Flora = ACEITO', 'Sinônimos Hierarquia Taxonômica', '', 'Forma de Vida e Substrato', '', 'Origem', 'Endemismo', 'Distribuição','','',''])
    escritorFloraInfo.escreve(['', 'Grupo taxonômico', 'Família', 'Forma de Vida', 'Substrato', '', '', 'Ocorrências confirmadas', 'Possíveis ocorrências', 'Domínios Fitogeográficos', 'Tipo de Vegetação'])

    try:
        leitor.getLinha()
        while(True):
            nomePlanta, statusFlora, nomeFlora, statusPlantlist, nomePlantlist, comparacao = leitor.getLinha()   
            if(nomeFlora and (statusFlora == 'Aceito' or nomePlanta != nomeFlora)):
                nomeP = nomeFlora.split(' ')
                nomeP = str(nomeP[0] + ' ' + nomeP[1])
                fInfo = FloraInfo(nomeP)
                resp = requisicaoFB(getURLID(nomeP))

                lista.insert(END, '{0} -> {1}'.format(count, nomePlanta))
                lista.yview(END)
                count += 1

                if(resp):
                    getInfoFlora(nomeP, fInfo, resp)
                    #fInfo.printInfo()
                    linha = [nomePlanta, fInfo.taxonomica, fInfo.familia, fInfo.formaVida, fInfo.substrato, fInfo.origem, fInfo.endemismo, fInfo.ocorenciaConfirmada,fInfo.possiveisOcorrencias,fInfo.fitogeografico,fInfo.vegetacao]
                    for pos, value in enumerate(linha):
                        linha[pos] = str(value).replace("[", '').replace("]", '').replace("'", '')

                    escritorFloraInfo.escreve(linha)
    
    except AttributeError as ex:
        print("FIM", ex)
        arquivoSaida = escritorFloraInfo.fim('INFORMACOES')       # fecha o arquivo de saida
        parametros['arquivoSaida'] = arquivoSaida
        arquivoSaida = os.path.relpath(arquivoSaida)                # caminho relativo
        mensagem = parametros['msgRetorno'].format(arquivoSaida)
        parametros['funcaoRetorno'](mensagem)

#-----------------------------------#
#      RECUPERA AS COORDENADAS      #
#-----------------------------------#
def release4(parametros):
    count = 1
    nomeArquivo = parametros['arquivoEntrada']
    lista = parametros['lista']
    leitor = Reader(nomeArquivo)
    escritorCoordenadasGB = Writer(nomeArquivo, ['Nome Especie', 'Latitude', 'Longitude', 'Localização'])
    escritorCoordenadasSL = Writer(nomeArquivo, ['Nome Especie', 'Latitude', 'Longitude', 'Localização'])

    lista.insert(END, 'RECUPERANDO AS COORDENADAS')
    try:
        while True:
            nomePlanta, nomeAutor = leitor.getNome()            # recupera o nome da planta

            if nomePlanta.lower().__contains__('nome especie'):
                continue

            lista.insert(END, '{0} -> {1}'.format(count, nomePlanta))
            lista.yview(END)
            count += 1

            dadosSL(requisicaoSL(nomePlanta), nomePlanta, escritorCoordenadasSL)
            dadosGB(nomePlanta, escritorCoordenadasGB)

    except AttributeError as ex:
        arquivoSaidaSL = escritorCoordenadasSL.fim('OCORRENCIAS_SPLINK')# fecha o arquivo de saida
        arquivoSaidaGB = escritorCoordenadasGB.fim('OCORRENCIAS_GBIF')    # fecha o arquivo de saida

        arquivoSaidaSL = os.path.relpath(arquivoSaidaSL)                # caminho relativo
        arquivoSaidaGB = os.path.relpath(arquivoSaidaGB)                # caminho relativo

        mensagem = parametros['msgRetorno'].format(arquivoSaidaSL)
        parametros['funcaoRetorno'](mensagem)

        mensagem = parametros['msgRetorno'].format(arquivoSaidaGB)
        parametros['funcaoRetorno'](mensagem)
