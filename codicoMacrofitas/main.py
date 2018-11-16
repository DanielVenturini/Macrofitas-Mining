# -*- coding: utf-8 -*-
import subprocess as sp
import Worker as wk

'''
    Arquivo com um menu para selecionar qual as operações a serem usadas
'''

# printa o menu com as opções
def principal():

    print()
    print('Digite a opção escolhida:')
    print('0 - SAIR.')
    print('1 - Validar nomes.')
    print('2 - Gerar lista de sinônimos.')
    print('3 - Gerar informações.')
    print('4 - Gerar coordenadas geográficas.')
    print('5 - Todas as operações, começando da 1 até a 4.')
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
    print('Digite 0 para SAIR.')
    print('Digite o nome do arquivo de entrada.')

    while True:
        arq = input('> ')
        try:
            if arq.__eq__('0'):
                return None

            open(arq)           # tenta abrir
        except FileNotFoundError:
            print('Arquivo não existe: ' + arq)
            print('Digite 0 para sair.')
            print('Digite um arquivo válido.')
            continue
        else:
            return arq

################################EXECUTÁVEL###########################################

opc = principal()

if opc == 6:
    exit(0)

nomeArquivo = getArquivo()
if not nomeArquivo:
    exit(0)

if opc == 1:
    wk.release1(nomeArquivo)
if opc == 2:
    pass
if opc == 3:
    pass
if opc == 4:
    pass