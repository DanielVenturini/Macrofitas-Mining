# -*- coding: utf-8 -*-
import subprocess as sp

'''
    Arquivo com um menu para selecionar qual as operações a serem usadas
'''

# printa o menu com as opções
def principal():

    print()
    print('Digite a opção escolhida:')
    print('1 - Validar nomes.')
    print('2 - Gerar lista de sinônimos.')
    print('3 - Gerar informações.')
    print('4 - Gerar coordenadas geográficas.')
    print('5 - Todas as operações, começando da 1 até a 4.')
    print('6 - SAIR.')
    print()

    while True:
        try:
            opc = input('> ')
            if int(opc) < 1 or int(opc) > 6:    # se digitou um número inválido
                continue
            else:
                return int(opc)
        except ValueError:      # se digitou um não-número
            continue

def getArquivo():
    print()
    print('Digite 0 para sair')
    print('Digite o nome do arquivo de entrada.')
    
    while True:
        arq = input('> ')
        try:
            if arq.__eq__('0'):
                return None

            file = open(arq)
        except FileNotFoundError:
            print('Arquivo não existe: ' + arq)
            print('Digite 0 para sair.')
            print('Digite um arquivo válido.')
            continue
        else:
            return file


################################EXECUTÁVEL###########################################

opc = principal()

if opc == 6:
    exit(0)

file = getArquivo()
if not file:
    exit(0)

print("Arquivo aberto:", file.readlines())