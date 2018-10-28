import unittest
from codicoMacrofitas.plantlist import urlPL, verificaEspecieIncorreta, dadosPL
from codicoMacrofitas.macrofita import Macrofita
from bs4 import BeautifulSoup

class TestPlantlist(unittest.TestCase):
    
    def testUrlPL(self):
        self.assertEqual(urlPL('Dicliptera ciliaris'), 'http://www.theplantlist.org/tpl1.1/search?q=Dicliptera+ciliaris')

    def testVerificaEspecieIncorreta(self):
        self.assertTrue(verificaEspecieIncorreta('ciliaris', 'ciliaris'))
        self.assertFalse(verificaEspecieIncorreta('ciliaris', 'Ciliaris'))

    def testDadosPLSubtitleAccepted(self, nomePlanta='Hygrophila costata Nees'):
        macrofita = Macrofita(nomePlanta)
        dadosPL(self.retornaNomeSemAutor(nomePlanta), macrofita, self.requisicaoData(nomePlanta))
                
        self.assertEqual(macrofita.statusPlantlist, 'Aceito')
        self.assertEqual(macrofita.nomePlantlist, nomePlanta)
        self.assertFalse(macrofita.obsPlantlist, '')

    def testDadosPLSubtitleSynonym(self, nomePlanta='Hygrophila guianensis Nees'):
        macrofita = Macrofita(nomePlanta)
        dadosPL(self.retornaNomeSemAutor(nomePlanta),macrofita, self.requisicaoData(nomePlanta))

        self.assertEqual(macrofita.statusPlantlist, 'Sinonimo')
        self.assertEqual(macrofita.nomePlantlist, 'Hygrophila costata Nees')
        self.assertFalse(macrofita.obsPlantlist, '')
    
    def testDadosPLUnresolvedName(self, nomePlanta='Isoetes ekmanii'):
        macrofita = Macrofita(nomePlanta)
        dadosPL(self.retornaNomeSemAutor(nomePlanta),macrofita, self.requisicaoData(nomePlanta))

        self.assertEqual(macrofita.statusPlantlist, '')
        self.assertEqual(macrofita.nomePlantlist, '')
        self.assertEqual(macrofita.obsPlantlist, 'Não Encontrado')

    def testDadosPLTabelaAccepted(self, nomePlanta='Juncus acutus L.'):
        macrofita = Macrofita(nomePlanta)
        dadosPL(self.retornaNomeSemAutor(nomePlanta),macrofita, self.requisicaoData(nomePlanta))

        self.assertEqual(macrofita.statusPlantlist, 'Aceito')
        self.assertEqual(macrofita.nomePlantlist, 'Juncus acutus L.')
        self.assertFalse(macrofita.obsPlantlist, '')

    def testDadosPLTabelaAcceptedEspecieInvalida(self, nomePlanta='Juncus acutusdd L.'):
        macrofita = Macrofita(nomePlanta)
        dadosPL(self.retornaNomeSemAutor(nomePlanta),macrofita, self.requisicaoData(nomePlanta))

        self.assertEqual(macrofita.statusPlantlist, '')
        self.assertEqual(macrofita.nomePlantlist, '')
        self.assertEqual(macrofita.obsPlantlist, 'Especie Invalida')

    def testDadosPLTabelaSinonimo(self, nomePlanta='Utricularia inflata L.'):
        macrofita = Macrofita(nomePlanta)
        dadosPL(self.retornaNomeSemAutor(nomePlanta),macrofita, self.requisicaoData(nomePlanta))

        self.assertEqual(macrofita.statusPlantlist, 'Sinonimo')
        self.assertEqual(macrofita.nomePlantlist, nomePlanta)
        self.assertFalse(macrofita.obsPlantlist, '')

    def testDadosPLGeneroIncorreto(self, nomePlanta='Diclipptera ciliaris Juss.'):
        macrofita = Macrofita(nomePlanta)
        dadosPL(self.retornaNomeSemAutor(nomePlanta), macrofita, self.requisicaoData(nomePlanta))

        self.assertFalse(macrofita.statusPlantlist)
        self.assertFalse(macrofita.nomePlantlist)
        self.assertEqual(macrofita.obsPlantlist, 'Genero Invalido')



    def retornaNomeSemAutor(self, nomePlanta):
        return  nomePlanta.split(' ')[0] + ' ' + nomePlanta.split(' ')[1]
        
    def requisicaoData(self,opt):
        if(opt == 'Hygrophila costata Nees'):
            return BeautifulSoup('<html><h1><span class="C-M"><img alt="M" src="/1.1/img/bM.png"/></span><span class="name"><i class="genus">Hygrophila</i> <i class="species">costata</i> <span class="authorship">Nees</span></span><span class="subtitle">is an <a href="/1.1/about/#accepted">accepted</a> name</span></h1><</html>>', "html.parser")
        elif(opt == 'Hygrophila guianensis Nees'):
            return BeautifulSoup('<h1><span class="C-M"><img src="/1.1/img/bM.png" alt="M"/></span><span class="name"><i class="genus">Hygrophila</i> <i class="species">guianensis</i> <span class="authorship">Nees</span></span><span class="subtitle">is a <a href="/1.1/about/#synonym">synonym</a> of <a href="kew-2856690"><span class="name"><i class="genus">Hygrophila</i> <i class="species">costata</i> <span class="authorship">Nees</span></span></a></span> </h1>', "html.parser")
        elif(opt == 'Isoetes ekmanii'):
            return BeautifulSoup('<h1> <span class="C-L"><img src="/1.1/img/bL.png" alt="L"/></span> <span class="name"><i class="genus">Isoetes</i> <i class="species">ekmanii</i> <span class="authorship">U. Weber</span></span> <span class="subtitle">is an <a href="/1.1/about/#unresolved">unresolved</a> name </span> </h1> ', "html.parser")
        elif(opt == 'Juncus acutus L.'):
            return BeautifulSoup('''<tr id="Juncus-A"><td class="name Accepted"><a href='/tpl1.1/record/kew-314275'><span class="name"><i class="genus">Juncus</i> <i class="species">acutus</i> <span class="authorship">L.</span></span></a></td> <td>Accepted</td> <td class="C-H"><img src="/1.1/img/H.png" alt="H"/></td> <td class="source"><a href="/1.1/about/#iopi">IOPI</a></td> <td class="dateExported"><time>2012-03-23</time></td> </tr>''', "html.parser")
        elif(opt == 'Juncus acutusdd L.'):
            return BeautifulSoup(
                '''
                    <tr>
                        <td class="name Accepted"><a href='/tpl1.1/record/kew-314237'><span class="name"><i class="genus">Juncus</i> <i class="species">acuminatus</i> <span class="authorship">Michx.</span></span></a></td>
                        <td>Accepted</td>
                        <td class="C-H"><img src="/1.1/img/H.png" alt="H"/></td>
                        <td class="source"><a href="/1.1/about/#iopi">IOPI</a></td>
                        <td class="dateExported"><time>2012-03-23</time></td>
                    </tr>
                    <tr>
                        <td class="name Synonym"><a href='/tpl1.1/record/kew-314238'><span class="name"><i class="genus">Juncus</i> <i class="species">acuminatus</i> <span class="authorship">Salzm. ex Kunth</span></span></a> [Invalid]</td>
                        <td>Synonym</td>
                        <td class="C-H"><img src="/1.1/img/H.png" alt="H"/></td>
                        <td class="source"><a href="/1.1/about/#iopi">IOPI</a></td>
                        <td class="dateExported"><time>2012-03-23</time></td>
                    </tr>
                ''', "html.parser")

        elif(opt == 'Utricularia inflata L.'):
            return BeautifulSoup(
                '''
                    <tr>
                        <td class="name Synonym"><a href='/tpl1.1/record/tro-18300093'><span class="name"><i class="genus">Utricularia</i> <i class="species">inflata</i> <span class="authorship">Walter</span></span></a></td>
                        <td>Synonym</td>
                        <td class="C-M"><img src="/1.1/img/M.png" alt="M"/></td>
                        <td class="source"><a href="/1.1/about/#tropicos">TRO</a></td>
                        <td class="dateExported"><time>2012-04-18</time></td>
                    </tr>
                    <tr>
                        <td class="name Synonym"><a href='/tpl1.1/record/tro-18300174'><span class="name"><i class="genus">Utricularia</i> <i class="species">inflata</i> <span class="infraspr">var.</span> <i class="infraspe">minor</i> <span class="authorship">Chapm.</span></span></a></td>
                        <td>Synonym</td>
                        <td class="C-L"><img src="/1.1/img/L.png" alt="L"/></td>
                        <td class="source"><a href="/1.1/about/#tropicos">TRO</a></td>
                        <td class="dateExported"><time>2012-04-18</time></td>
                    </tr>
                ''', "html.parser")

        elif(opt == 'Diclipptera ciliaris Juss.'):
            return BeautifulSoup(
                '''
                    <div id="container">
                        <div id="columns">
                    <section>
                        <h2>Results</h2>

                        <p>No plant name records match your search criteria <strong><i>Diclipptera</i></strong>.
                        </p>
                    <p>Please note that The Plant List contains only scientific plant names in Latin and does not contain common (vernacular) names in other languages.</p>

                        <h4>Help with searching scientific names</h4>
                        <p><kbd><kbd>?</kbd></kbd> will match a single character. <kbd><kbd>*</kbd></kbd> will match any number of characters.  Use at least three letters in the genus name if you include a <kbd><kbd>?</kbd></kbd> or <kbd><kbd>*</kbd></kbd>.</p>
                        
                        <h5>Examples of searches that will work</h5>
                        <ul>
                            <li>Use <kbd><kbd>Vicia faba</kbd></kbd> to locate this name (and any infraspecific names associated with it).</li>
                            <li>Use <kbd><kbd>Schusterella</kbd></kbd> to locate all names in this genus.</li>
                            <li>Use <kbd><kbd>Taxaceae</kbd></kbd> to see the <i class="family">Taxaceae</i> family page.</li>
                            <li>Use <kbd><kbd>Quercus a*</kbd></kbd> to locate all names in the genus <i class="genus">Quercus</i> that have a species name beginning with the letter "a".</li>
                            <li>Use <kbd><kbd>Psilo*</kbd></kbd> to locate all names in any genera which begin with the letters "Psilo".</li>
                            <li>Use <kbd><kbd>Orchis a?????</kbd></kbd> to locate all names in the genus <i class="genus">Orchis</i> which have a species name of exactly six letters, the first of which is the letter "a".</li>
                            <li>Use <kbd><kbd>M?cro*</kbd></kbd> to locate all names in any genera whose names begin with "Micro" or "Macro".</li>
                            <li>Use <kbd><kbd>http://ipni.org/urn:lsid:ipni.org:names:295763-1</kbd></kbd> or <kbd><kbd>295763-1</kbd></kbd> to go directly to the name with that IPNI identifier.</li>
                        </ul>

                        <h5>Examples of searches that will <em>not</em> work</h5>
                        <ul>
                            <li><kbd><kbd>La*</kbd></kbd> is not a valid search string, since at least three letters are required when a <kbd><kbd>?</kbd></kbd> or <kbd><kbd>*</kbd></kbd> is in the genus.</li>	
                            <li>Neither <kbd><kbd>*ubus</kbd></kbd> nor <kbd><kbd>?ubus</kbd></kbd> are valid search strings since each begins with a wildcard.</li>
                            <li>Using <kbd><kbd>Vicia sativa var. sativa</kbd></kbd> will return all names that would be found using <kbd><kbd>Vicia sativa</kbd></kbd> rather than just those infraspecific names matching the full string.</li>
                        </ul>
                ''', "html.parser")
        
        return ''



