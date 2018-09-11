# coding:UTF-8

'''
Este arquivo chamara as funçoes reponsaveis por cada parte do projeto
'''

from OperacoesArquivo import (Reader, Writer)
import sys

def start(nomeArquivo):

    try:

        leitor, escritor = Reader().getLeitorEscritor(nomeArquivo)

    except Exception as ex:
        print("Exception aqui: " + str(ex))
        return

    try:
        while True:
            # Primeira coluna e o genero, segundo o nome da especie.
            genero, especie = leitor.getNome()
            print("Genero: " + genero)
            print("Especie: " + especie)

    except StopIteration:       # quando nao ha mais o que ler do arquivo
        escritor.fim()










# python3 Worker arquivo.csv
if sys.argv.__len__() == 2:
    start(sys.argv[1])
else:
    print("Erro. Use: python3 Worker.py arquivo.csv")

