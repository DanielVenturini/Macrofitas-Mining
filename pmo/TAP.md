## Sumário
 
1. [Introdução](#1-introdu%C3%A7%C3%A3o)
2. [Justificativa](#2-justificativa)
3. [Objetivo do Projeto (SMART)](#3-objetivo-do-projeto-smart)
4. [Requisitos](#4-requisitos)
5. [Riscos](#5-riscos)
6. [Cronograma e Marcos](#6-cronograma-e-marcos)
7. [Custo Estimado do Projeto](#7-custo-estimado-do-projeto)    
  7.1. [Nota](#71-nota)    
8. [Stakeholders (Partes interessadas)](#8-stakeholders-partes-interessadas)           
  8.1. [Cliente](#81-cliente)    
  8.2. [Equipe de Gerência](#82-equipe-de-gerencia)
9. [Referência Bibliográfica](#9-refer%C3%AAncia-bibliogr%C3%A1fica)

# 1. Introdução

<p align = "justify"> O sistema em questão é aplicado à pesquisas em Ecologia de ambientes aquáticos continentais, as quais têm o objetivo de investigar padrões biogeográficos de Macrófitas aquáticas (plantas que vivem permanentemente ou por alguns períodos do ano, com a parte fotossintetizante em contato com a água) na América do Sul. Com base em dados sobre a ocorrência dessas plantas, pretendemos identificar áreas de maior diversidade, famílias e táxons amplamente distribuídas, famílias e táxons com áreas restritas de ocorrência, entre outros. Em adição, dados de ocorrência das espécies serão correlacionados à variáveis ambientais para a predição da área de distribuição geográfica das espécies no presente e no futuro, considerando o efeito das mudanças climáticas. </p>

# 2. Justificativa

<p align = "justify"> Atualmente os dados eram coletados e análisados individualmente e manualmente. Com isso, o tempo perdido somente nestas etapas, eram demasiados. Por isso, se torna inviável a realização da pesquisa de forma manual. </p>

# 3. Objetivo do Projeto (SMART)

 <p align = "justify"> - Validar os nomes das espécies de macrófitas em online databases, trazendo também informações acerca da
taxonomia/ecologia/biologia referentes aos nomes aceitos. </p>
 
 <p align = "justify"> - Congregar informações de registros ocorrências dessas espécies de macrófitas no continente, corrigindo erros e indicando padrões e tendências considerando as bacias hidrográficas Sul-Americanas. </p>

# 4. Requisitos

<p align = "justify"> 1. O sistema deve validar o nome das espécies da lista de entrada (1900 espécies) com base nas informações disponibilizadas em online databases (Flora do Brasil e PlantList), fornecendo o nome atualmente aceito e autor, bem como a lista de sinonímias para cada nome válido ou aceito; </p>

<p align = "justify"> 2. Para cada espécie válida o sistema deve buscar e extrair das online databases os seguintes informações: ordem, classe, família, tribo, forma de vida, substrato, origem, endemismo e distribuição geográfica; </p>

<p align = "justify"> 3. O sistema deve buscar os dados de ocorrência de cada espécie (para o nome aceito e suas sinonímias) nas plataformas Specieslink e GBIF; </p>

<p align = "justify"> 4. O sistema deve executar um processo de triagem dos dados de ocorrências disponibilizados pelo GBIF e Specieslink de modo a corrigir nomes duplicados, erros de digitação, coordenadas ausentes, registros de grupos não plantas (ex. peixes, insetos, répteis, etc), entre outras inconsistências; e </p>

<p align = "justify"> 5. O sistema deverá fornecer gráficos/tabelas/mapas com as principais tendências dos dados entre as 14 grandes bacias Sul-Americanas e do continente como um todo, como por exemplo, número de espécies de macrófitas por bacia, família mais especiosa, família mais amplamente distribuída. </p>

# 5. Riscos

<p align = "justify"> O principal risco é a limitação de tempo. Visto que o projeto será desenvolvido até meados de dezembro de 2018. Outro risco, será a extração das bases de dados. Que demandará tempo e análise para uma implementação que venha ser conveniente com as bases. </p>

# 6. Cronograma e Marcos

<p align = "justify"> O projeto será dividido em quatro entregas, sendo estas a seguir: </p>

 **Entregas**     | **Data**           
------------|-----------------|
Release 01                   | 21/09/2018 |
Release 02                   | 05/10/2018 |
Release 03                   | 19/10/2018 |
Release 04                   | 07/11/2018 |

<br />

<p>Na Figura abaixo esta o EOP referente a cada entrega das release:</p>
<kbd>
 <img src="https://github.com/DanielVenturini/Macrofitas-Mining/blob/master/pmo/teste.png"/>
</kbd>

<br />

Na tabela abaixo vemos os valores da estimativa PERT:

| Atividade | Otimista | Média | Pessimista | Final |
|---|---|---|---|---|
| 2.1.1 | 1/4h | 1h | 2h | 1h |
| 2.1.2 | 3h | 5h | 10h | 6h |
| 2.1.3 | 1h | 2h | 3h | 2h |
| 2.1.4 | 1/4h | 1h | 2h | 1h |
| 3.1.1 | 4h | 5h | 12h | 6h |
| 3.1.2 | 2h | 2h | 4h | 3h |
| 4.1.1 | 13h | 14h | 18h | 8h |
| 4.1.2 | 10h | 12h | 13h | 11h |
| Duração |||| 36h |

<br />

<p>Na Figura abaixo esta o Grafico de Gantt, referente ao EAP:</p>
<kbd>
 <img src="https://github.com/DanielVenturini/Macrofitas-Mining/blob/master/pmo/gantt.png"/>
</kbd>

<br />

# 7. Custo estimado do projeto
## 7.1. Nota

<p align = "justify"> O custo será a nota requerida para o exito na disciplina com o mínimo de 9,5. </p>

# 8. Stakeholders (Partes interessadas)

## 8.1. Cliente

<p align = "justify"> Aluna de doutorado em Biológia Comparada e suas orientadoras. </p>

| Nome | E-mail | Lattes |  
|---|---|--- |
|Tânia Camila Crivelari|taniacrivelari@hotmail.com|http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4400924P9|   
|Karina Fidanza Rodrigues|karina.fidanza@gmail.com|http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4775416E9|  
|Dayani Bailly|dayanibailly@gmail.com|http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4762458J6|

## 8.2.  Equipe de Gerência

<p align = "justify"> Os seguintes desenvolvedores têm o objetivo de planejar, controlar e tomar decisões para que o projeto seja concluído com êxito. </p>

| Nome | E-mail |   GitHub |  
|---|---|--- |
|Daniel Venturini|danielventurini021@gmail.com|https://github.com/danielventurini|   
|Douglas Vinicius de Abreu|douglasabrel97@gmail.com|https://github.com/doouglasabreu|  
|Luiz Augusto da Silva Silveira|luiz_ssilveira@hotmail.com|https://github.com/LuizASSilveira|

# 9. Referência Bibliográfica

* PMI. *Um guia do conhecimento em gerenciamento de projetos. * Guia PMBOK® 5a. ed. - EUA: Project Management Institute, 2013

* **¹** MONTES, Eduardo. **TERMO DE ABERTURA DO PROJETO**. Disponível em <[https://escritoriodeprojetos.com.br/termo-de-abertura-do-projeto](https://escritoriodeprojetos.com.br/termo-de-abertura-do-projeto)> Acesso em 18/08/2018
