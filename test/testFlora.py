import unittest
from codicoMacrofitas.floradobrasil import urlFB, requisicaoFB

class TestPlantlist(unittest.TestCase):

    def test_urlFB(self):
        self.assertEqual(urlFB('Dicliptera ciliaris'),'http://servicos.jbrj.gov.br/flora/taxon/Dicliptera%20ciliaris')
    


