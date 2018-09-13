# coding:UTF-8

'''
Esta classe contera as implementaçoes das funçoes responsaveis por ler o arquivo
com os nomes das macrofitas e retornar nome a nome
'''

import openpyxl

class Reader:

    def __init__(self):
        pass

    def getLeitorEscritor(self, nomeArquivo):
        try:
            book = openpyxl.load_workbook(nomeArquivo)
            self.leitor = book.active
        except FileNotFoundError:
            self.leitor = None
            print("ARQUIVO {0} NAO EXISTE.".format(nomeArquivo))
            raise

        self.linha = 1
        return self, None#, Writer(nomeArquivo)


    # Esta funçao retorna nome a nome.
    # Estes nomes ja foram previamente lidos do arquivo
    def getNome(self):
        if not self.leitor:
            raise Exception

        linha = self.leitor['A{0}'.format(str(self.linha))].internal_value.split(' ')
        self.linha += 1
        return linha[0] + '%20' + linha[1]        # Primeira coluna e o genero, segunda o nome da especie.


'''
Esta classe contera as implementaçoes das funçoes responsaveis por escrever o arquivo.
O que sera escrito sera o nome da planta, se e sinonimo, o nome alterado e a coordenada.
Na primeira etapa, nao sera usado o campo coordenada.
'''

class Writer:

    def __init__(self, nomeArquivo):
        self.file = open(nomeArquivo+'pt1.csv', 'w')                                # abrindo o arquivo para escrita
        nomeCampos = ['nome original', 'sinonimo', 'nome alterado']                 # os campos que terao o arquivo csv
        self.escritor = csvWriter = csv.DictWriter(self.file, fieldnames=nomeCampos)# abrindo como csv
        self.escritor.writeheader()                                                 # escreve os campos

    def fim(self):
        self.file.close()   # fecha o arquivo e salva o conteudo


leitor = Reader().getLeitorEscritor('ListaMacrofitas.xlsx')