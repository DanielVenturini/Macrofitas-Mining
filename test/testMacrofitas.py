import unittest
from codicoMacrofitas.plantlist import urlPL

class TestMacrofitas(unittest.TestCase):
    
    def test_urlPL(self):
        self.assertEqual(
            urlPL('Dicliptera', 'ciliaris'), 'http://www.theplantlist.org/tpl1.1/search?q=Dicliptera+ciliaris')

