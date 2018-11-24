from OperacoesArquivo import Reader
import gbif

def buscarOcorrenciaGbif(nomePlanta):
    gbif.buscar(nomePlanta,1)



nomeArquivo = 'ListaMacrofitas_RESULTADO.xlsx'

arq = Reader(nomeArquivo)
print(arq.getNomeOcorrencia())

statusFlora, nomeFlora,statusPlantlist,nomePlantilist = arq.getNomeOcorrencia()

buscarOcorrenciaGbif(nomeFlora)

