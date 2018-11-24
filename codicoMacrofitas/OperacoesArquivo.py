# coding:utf-8

'''
Esta classe contém as implementações das funções responsáveis por ler o árquivo
com os nomes das macrofitas e retornar nome a nome
'''

'''
Use:
    from OperacoesArquivo import (Reader, Writer)
    leitor = Reader('ListaMacrofitas.xlsx')     # inicializa o leitor e abre o arquivo
    leitor.getNome()                            # recupera um nome por linha já no padrão GET: 'genero%20especie'
'''

import csv
import openpyxl

class Reader:

    def __init__(self, nomeArquivo):
        try:
            book = openpyxl.load_workbook(nomeArquivo)      # abrindo o arquivo para o leitor
            self.leitor = book.active                       # ativando o leitor
        except FileNotFoundError:
            self.leitor = None
            raise

        self.linha = 1              # começa em 1 porque na posição 0 é outra coisa


    #Esta função retorna os nomes para serem procuradas as ocorrências das espécies
    def getNomeOcorrencia(self):
        if not self.leitor:
            raise Exception
        try:
            statusFlora = self.leitor['B'+str(self.linha)].internal_value
            nomeFlora = self.leitor['C'+str(self.linha)].internal_value
            statusPlantlist = self.leitor['E'+str(self.linha)].internal_value
            nomePlantlist = self.leitor['F'+str(self.linha)].internal_value
            self.linha += 1 
            return statusFlora , nomeFlora , statusPlantlist , nomePlantlist

        except AttributeError:
            self.leitor = None
            raise  

    # Esta funçao retorna nome a nome.
    # O valor retornado é 'genero especie', pois está no padrão para enviar o GET
    # Gera a exceção AttributeError quando não houver mais linhas
    def getNome(self):
        if not self.leitor:     # se o leitor for inválido
            raise Exception     # lança uma exceção

        try:
            linha = self.leitor['A{0}'.format(str(self.linha))].internal_value.replace('\xa0', ' ')     # recupera o objeto da linha e desta, os valores da linha
            self.linha += 1                                     # atualiza o valor da linha
            nomePlanta = linha.split(' ')
            nomePlanta = nomePlanta[0] + ' ' + nomePlanta[1]    # recupera o nome da planta
            nomeAutor = linha.replace(nomePlanta, '')[1:]      # recupera o nome do autor
            return nomePlanta, nomeAutor
        except AttributeError:                  # quando chegar no fim do arquivo
            self.leitor = None                  # atribui None ao leitor, para, se chamar novamente, gere a exceção no bloco if
            raise                               # Re-lança a exceção


'''
Esta classe contera as implementaçoes das funçoes responsaveis por escrever no arquivo.
O que sera escrito sera o nome da planta, se é sinonimo, o nome alterado e a coordenada.
Na primeira etapa, não será usado o campo coordenada.
'''

class Writer:

    def __init__(self, nomeArquivo, cabecalho):
        self.nomeArquivo = nomeArquivo

        self.workbook = openpyxl.Workbook()
        self.worksheet = self.workbook.active
        self.linhaNum = 1

        # as linhas com 8 colunas são linhas de arquivos VALIDADOS
        # as linhas com 2 colunas são linhas de arquivos SINÔNIMOS
        # as linhas com 4 colunas são linhas de arquivos COORDENADAS
        if len(cabecalho) == 8:
            self.coluna = 'H'
        elif len(cabecalho) == 2:
            self.coluna = 'B'
        elif len(cabecalho) == 4:
            self.coluna = 'D'

        self.escreve(cabecalho)

    def escreve(self, linha):
        for pos, celula in enumerate(self.worksheet['A{0}'.format(str(self.linhaNum)):'{0}{1}'.format(self.coluna, str(self.linhaNum))][0]):
            celula.set_explicit_value(linha[pos])

        self.linhaNum += 1

    # tipoArquivo será VALIDADOS|SINONIMOS|OCORRENCIAS
    def fim(self, tipoArquivo):
        print()
        self.workbook.save(self.nomeArquivo + '_' + tipoArquivo + '.xlsx')
        return self.nomeArquivo + '_' + tipoArquivo + '.xlsx'
