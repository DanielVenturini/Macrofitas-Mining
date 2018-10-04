# coding:UTF-8

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

import openpyxl

class Reader:

    def __init__(self, nomeArquivo):
        try:
            book = openpyxl.load_workbook(nomeArquivo)      # abrindo o arquivo para o leitor
            self.leitor = book.active                       # ativando o leitor
        except FileNotFoundError:
            self.leitor = None
            raise

        self.linha = 1          # começa em 1 porque na posição 0 é outra coisa

    # Esta funçao retorna nome a nome.
    # O valor retornado é 'genero%20especie', pois está no padrão para enviar o GET
    # Gera a exceção AttributeError quando não houver mais linhas
    def getNome(self):
        if not self.leitor:     # se o leitor for inválido
            raise Exception     # lança uma exceção

        try:
            linha = self.leitor['A{0}'.format(str(self.linha))].internal_value.split(' ')   # recupera o objeto da linha e desta, os valores da linha
            self.linha += 1                     # atualiza o valor da linha
            return linha[0] + '%20' + linha[1]  # Primeira coluna é o genero, segunda é o nome da espécie.
        except AttributeError:                  # quando chegar no fim do arquivo
            self.leitor = None                  # atribui None ao leitor, para, se chamar novamente, gere a exceção no bloco if
            raise                               # Re-lança a exceção


'''
Esta classe contera as implementaçoes das funçoes responsaveis por escrever no arquivo.
O que sera escrito sera o nome da planta, se é sinonimo, o nome alterado e a coordenada.
Na primeira etapa, não será usado o campo coordenada.
'''

class Writer:

    def __init__(self, nomeArquivo):
        self.file = open(nomeArquivo+'pt1.csv', 'w')                                # abrindo o arquivo para escrita
        nomeCampos = ['nome original', 'sinonimo', 'nome alterado']                 # os campos que terao o arquivo csv
        self.escritor = csvWriter = csv.DictWriter(self.file, fieldnames=nomeCampos)# abrindo como csv
        self.escritor.writeheader()                                                 # escreve os campos

    def fim(self):
        self.file.close()   # fecha o arquivo e salva o conteudo