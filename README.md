[![Build Status](https://travis-ci.org/DanielVenturini/Macrofitas-Mining.svg?branch=master)](https://travis-ci.org/DanielVenturini/Macrofitas-Mining)
[![Coverage Status](https://coveralls.io/repos/github/DanielVenturini/Macrofitas-Mining/badge.svg?branch=master)](https://coveralls.io/github/DanielVenturini/Macrofitas-Mining?branch=master)

# Macrofitas-Mining
Projeto desenvolvido para mineração em base de dados Web de plantas. Os sites são: ```Flora do Brasil```, ```PlantList```, ```GBIF``` e ```Species Link```. Para isto, é necessário um arquivo de entrada no formato ```Excel xlsx``` como uma entrada como o gênero, espécie e autor. Por exemplo:

```
Hyptis tetracephala Bordig.
Marsypianthes chamaedrys (Vahl) Kuntze.
Cassytha filiformis L.
.
.
.
```

## Tabelas resultados
No total, são gerados quatro tabelas:

 - Os nomes das plantas são extraídos do arquivo e são validados no ```Flora do Brasil``` e ```Plant List```. O resultado é salvo em um novo arquivo, informando se o nome é aceito em alguma das bases e o nome aceito, caso for um sinônimo. Este arquivo é usado nas próximas etapas.

 - Tabela somente com os sinônimos de cada nome aceito. Estes sinônimos são recuperados do ```Flora do Brasil``` e do ```Plant List```.
 
 - Tabela com informações mais detalhadas dos nomes validados, tal como Hierarquia, Forma de vida, Vida e Substrato, ... encontrados no ```Flora do Brasil```.
 
  - Tabela com as ocorrências de cada nome aceito, tal como latitude, longitude e localização. Esta tabela é gerada a partir do ```Species Link``` e do `````GBIF``.

## Execução
Para executar o ```Macrofitas Mining```, não é necessário instalação. Apenas baixe o arquivo e o execute:

```https://www.dropbox.com/s/i23ynnqdscbz289/main.exe?dl=0```

## Uso
A imagem a seguir, refere-se a interface principal do programa:

<p align="center">
  <img src="https://github.com/danielventurini/Macrofitas-Mining/raw/master/interface.JPG">
</p>

- O primeiro botão, ```Escolha um arquivo```, seleciona o arquivo que será usado nas operações.

- O segundo botão, ```Validar nomes```, valida os nomes das plantas do arquivo selecionado. Então o arquivo resultante é salvo com o mesmo nome do arquivo de entrada mais o ```_VALIDADOS.xlsx```. Por exemplo, o arquivo de entrada ```Lista.xlsx``` será validado e salvo no arquivo ```Lista.xlsx_VALIDADOS.xlsx```. ENTÃO O ARQUIVO VALIDADO DEVE SER USADO NAS DEMAIS OPERAÇÕES.

```SE FOR REALIZADO MAIS OPERAÇÕES, O ARQUIVO VALIDADO DEVE SER SELECIONADO NO PRIMEIRO BOTÃO. SE FOR USADO O BOTÃO Todas as operações ENTÃO NÃO SERÁ NECESSÁRIO ESTA TROCA DE ARQUIVOS.```

- O terceiro botão, ```Gerar lista de sinônimos```, gera a lista de sinônimos do arquivo VALIDADO. E o arquivo resultante é salvo com o mesmo nome do arquivo de entrada mais o ```_SINONIMOS```. Por exemplo, o arquivo de entrada ```Lista.xlsx_VALIDADOS.xlsx``` será gerado os sinônimos e salvo com o nome ```Lista.xlsx_VALIDADOS.xlsx_SINONIMOS```.

- O quarto botão, ```Gerar informações``` gera informações sobre cada planta. E o arquivo resultante é salvo com o mesmo nome do arquivo de entrada mais o ```_INFORMACOES```. Por exemplo, o arquivo de entrada ```Lista.xlsx_VALIDADOS.xlsx``` será gerado os sinônimos e salvo com o nome ```Lista.xlsx_VALIDADOS.xlsx_INFORMACOES```.

- O quinto botão, ```Gerar coordenadas geográficas```, gera a latitude, longitude a a localização. E o arquivo resultante é salvo com o mesmo nome do arquivo de entrada mais o ```_COORDENADAS```. Por exemplo, o arquivo de entrada ```Lista.xlsx_VALIDADOS.xlsx``` será gerado os sinônimos e salvo com o nome ```Lista.xlsx_VALIDADOS.xlsx_COORDENADAS```.

- O sexto botão, ```Todas as operações```, realiza todas as operações sobre um arquivo de entrada. As operações são as descritas anteriormente e de uma vez, ou seja, não é necessário ficar trocando o arquivo a cada operação.

Quando é terminada uma operação, é mostrado uma janela informando o nome do arquivo resultado. Então quando ```Todas as operações``` é usado, recomenda-se que use a flag ```AUTO-CONFIRMAR após executar```, assim, é como se já fosse clicado no botão ```OK``` a cada operação.

<p align="center">
  <img src="https://github.com/danielventurini/Macrofitas-Mining/raw/master/interface2.JPG">
</p>

## Desenvolver
Instale o Python 3.7:

```https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe```

Instale a dependência ```requests```:

```python -m pip install requests```

Instale a dependência ```openpyxl```:

```python -m pip install openpyxl```

Instale a dependência ```bs4```:

```python -m pip install bs4```

Instale a dependência ```coveralls```:

```python -m pip install coveralls```