import unittest
from codicoMacrofitas.macrofita import Macrofita

class testClassMacrofita(unittest.TestCase):

    def setUpMacrofita(self, macrofita, nomeFlora, nomePlantlist):
        macrofita.nomeFlora = nomeFlora
        macrofita.nomePlantlist = nomePlantlist
        return

    def testComparaFloraPlantlistIgual(self, nomeFlora='Dicliptera ciliaris Juss.', nomePlantlist='Dicliptera ciliaris Juss.'):
        nomeEspecie = nomeFlora
        macrofita = Macrofita(nomeEspecie)
        self.setUpMacrofita(macrofita, nomeFlora, nomePlantlist)
        macrofita.comparaFloraPlantlist()
        
        self.assertFalse(macrofita.floraXplantlist)
        

    def testComparaFloraPlantlistDiferente(self, nomeFlora='Dicliptera cilias.', nomePlantlist='Dicliptera ciliaris Juss'):
        nomeEspecie = nomeFlora
        macrofita = Macrofita(nomeEspecie)
        self.setUpMacrofita(macrofita, nomeFlora, nomePlantlist)
        macrofita.comparaFloraPlantlist()

        self.assertEqual(macrofita.floraXplantlist, 'Diferente')

    def testComparaNome(self, nomeEspecie='Echinodorus grandiflorus(Cham. & Schltdl.) Micheli', nomeFlora='Echinodorus grandiflorus (Cham. & Schltr.) Micheli', nomePlantlist='Echinodorus grandiflorus (Cham. & Schltdr.) Micheli'):
        
        macrofita = Macrofita(nomeEspecie)
        
        macrofita.comaparaNome('flora')
        self.assertEqual(macrofita.obsFlora, 'Autor Incorreto')

        macrofita.comaparaNome('plantlist')
        self.assertEqual(macrofita.obsPlantlist, 'Autor Incorreto')