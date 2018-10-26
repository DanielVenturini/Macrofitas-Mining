import unittest
from codicoMacrofitas.plantlist import urlPL

class TestPlantlist(unittest.TestCase):
    
    def testUrlPL(self):
        self.assertEqual(urlPL('Dicliptera', 'ciliaris'), 'http://www.theplantlist.org/tpl1.1/search?q=Dicliptera+ciliaris')