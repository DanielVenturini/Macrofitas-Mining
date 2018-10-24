import unittest
from codicoMacrofitas.floradobrasil import urlFB, dadosFB
from codicoMacrofitas.macrofita import Macrofita

class TestPlantlist(unittest.TestCase):

    def variavelEscolha(self,opt):
        if(opt == 1):
            return {'success': True, 'result': [{'family': 'Acanthaceae', 'genus': 'Dicliptera', 'scientificname': 'Dicliptera ciliaris Juss.', 'specificepithet': 'ciliaris', 'infraspecificepithet': None, 'scientificnameauthorship': 'Juss.', 'taxonomicstatus': 'NOME_ACEITO', 'acceptednameusage': None, 'higherclassification': 'Flora;Angiospermas;Acanthaceae Juss.;Dicliptera Juss.;Dicliptera ciliaris Juss.', 'acceptednameusageid': None, 'SINONIMO': []}]}
        
        return ''

    nomePlanta = 'Dicliptera ciliaris'
    macrofita = Macrofita(nomePlanta)

    def test_urlFB(self):
        self.assertEqual(urlFB(self.nomePlanta), 'http://servicos.jbrj.gov.br/flora/taxon/Dicliptera%20ciliaris')
    
    def teste_dadosFB(self):
        retornoReqFB = self.variavelEscolha(1)
        retorno = dadosFB(self.nomePlanta, retornoReqFB, self.macrofita)
        
        self.macrofita.statusFlora = 'Aceito'
        self.macrofita.nomeFlora = 'Dicliptera ciliaris Juss.'
        self.macrofita.obsFlora = ''

        self.assertEqual(retorno.statusFlora, self.macrofita.statusFlora)
        self.assertEqual(retorno.nomeFlora, self.macrofita.nomeFlora)
        self.assertEqual(retorno.obsFlora, self.macrofita.obsFlora)

        

        
