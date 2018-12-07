import unittest
import types
import codicoMacrofitas.specieslink as specieslink
from bs4 import BeautifulSoup


class TestSpecieslink(unittest.TestCase):

    def testNextPlanta(self):
        resp = specieslink.nextPlanta(self.entrada())
        self.assertTrue(isinstance(resp, types.GeneratorType))

    def testDadosSL(self):
        self.assertTrue(specieslink.dadosSL(self.entrada(), 'victoria amazonica'))

        
    def entrada(self):
        return BeautifulSoup('''
            <div class="record" id="record_x"><table border="0" width="100%"><tr align="right" valign="top">
            <td><b>Atenção!</b><br/>Os nomes das espécies e gêneros ao lado<br/>são comparados com alguns dicionários de acordo com o grupo biológico.<br/> Em <span class="tAcc">negrito verde</span> aparecem os <span class="tAcc">aceitos</span>,<br/>em <span class="tSyn">negrito cinza</span> os <span class="tSyn">sinônimos</span> e<br/> em <span class="tUnk">laranja</span> os <span class="tUnk">não encontrados</span>.<br/> Nomes em <span class="tAmb">magenta</span> aparecem nos dicionários com mais de um status por diferentes motivos.<br/> Nomes de <b>famílias</b> são apenas checados quanto a constarem ou não dos dicionários.<br/> No inventário de espécies, o nome aparece em <span class="tnoId">azul</span> quando o espécime com <span class="tnoId">identificação só até gênero</span>.<br/> Veja <a href="javascript:getTips()"><b>dicas de uso</b></a> para informações mais detalhadas.</td>
            </tr></table></div>
            <div class="record" id="record_0"><table border="0" width="100%"><tr id="detail_0" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=MBM" target="manager"><img align="right" src="logos/institutions/MBM.png" width="50px"/></a></td>
            <td><span onclick="top.getDetail(823583026,0)">
            <span class="tK">Plantae</span> <span class="tF">Amaranthaceae</span> <br/> <span class="tGa"> <u>Salicornia</u> </span> <span class="tEa"> <u>ambigua</u> </span> <span class="tA">Michx.</span>. <ll>Det: </ll> <span class="tI">Schinini, A</span> <span class="tY">2000</span><br/> <span class="tN">MBM 249431</span> <ll>Coleta: </ll> <span class="cL">Pedersen, TM</span> <span class="cN">14101</span> <br/> <ll>Loc: </ll> <span class="lP">About 5 km S of Arauco, on the shore of the Pacific. VIII Región del Bio-Bio.</span> <span class="lS">Arauco</span>, <span class="lC">Chile</span> <ll>Cód. barras: </ll> <span class="bC">MBM249431.</span> <br/> <ll>Notas:</ll> <no>Salt-march.</no><br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Herbário do Museu Botânico Municipal (MBM)</span></td></tr></table>
            </td></tr></table></div></div>
            <br/><div class="record" id="record_1"><table border="0" width="100%"><tr id="detail_1" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=MBM" target="manager"><img align="right" src="logos/institutions/MBM.png" width="50px"/></a></td>
            <td><span onclick="top.getDetail(823583025,1)">
            <span class="tK">Plantae</span> <span class="tF">Amaranthaceae</span> <br/> <span class="tGa"> <u>Salicornia</u> </span> <span class="tEa"> <u>ambigua</u> </span> <span class="tA">Michx.</span>. <ll>Det: </ll> <span class="tI">Seijo, G</span><br/> <span class="tN">MBM 242786</span> <ll>Coleta: </ll> <span class="cL">Seijo, G</span> <span class="cN">1452</span> <span class="cY">14/01/1999</span>. <br/> <ll>Loc: </ll> <span class="lP">Viedma. Caleta de los Loros.</span>, <span class="lM">Adolfo Alsina</span>, <span class="lS">Rio Negro</span>, <span class="lC">Argentina</span> <ll>Cód. barras: </ll> <span class="bC">MBM242786.</span> <br/> <ll>Notas:</ll> <no>Orillas del mar.</no><br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Herbário do Museu Botânico Municipal (MBM)</span></td></tr></table>
            </td></tr></table></div>
            <br/><div class="record" id="record_2"><table border="0" width="100%"><tr id="detail_2" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=MBM" target="manager"><img align="right" src="logos/institutions/MBM.png" width="50px"/></a></td>
            <td><span onclick="top.getDetail(823583022,2)">
            <span class="tK">Plantae</span> <span class="tF">Amaranthaceae</span> <br/> <span class="tGa"> <u>Salicornia</u> </span> <span class="tEa"> <u>ambigua</u> </span> <span class="tA">Michx.</span>. <ll>Det: </ll> <span class="tI">Pedersen, TM</span><br/> <span class="tN">MBM 127396</span> <ll>Coleta: </ll> <span class="cL">Pedersen, TM</span> <span class="cN">14425</span> <span class="cY">14/02/1986</span>. <br/> <ll>Loc: </ll> <span class="lM">Puerto Deseado</span>, <span class="lS">Santa Cruz</span>, <span class="lC">Argentina</span> <ll>Cód. barras: </ll> <span class="bC">MBM127396.</span> <br/> <ll>Notas:</ll> <no>Brackish mud-flats.</no><br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Herbário do Museu Botânico Municipal (MBM)</span></td></tr></table>
            </td></tr></table></div>
            <br/><div class="record" id="record_3"><table border="0" width="100%"><tr id="detail_3" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=MBM" target="manager"><img align="right" src="logos/institutions/MBM.png" width="50px"/></a></td>
            <td><span onclick="top.getDetail(823583024,3)">
            <span class="tK">Plantae</span> <span class="tF">Amaranthaceae</span> <br/> <span class="tGa"> <u>Salicornia</u> </span> <span class="tEa"> <u>ambigua</u> </span> <span class="tA">Michx.</span>. <ll>Det: </ll> <span class="tI">Schinini, A</span> <span class="tY">1996</span><br/> <span class="tN">MBM 202174</span> <ll>Coleta: </ll> <span class="cL">Schinini, A; Cuadrado, G</span> <span class="cN">30542</span> <span class="cY">29/02/1996</span>. <br/> <ll>Loc: </ll> <span class="lP">Ruta 86, alrededores de Laguna Blanca.</span>, <span class="lM">Pilcomayo</span>, <span class="lS">Formosa</span>, <span class="lC">Argentina</span> <ll>Cód. barras: </ll> <span class="bC">MBM202174.</span> <br/> <ll>Notas:</ll> <no>Gemifera; ramosa, ramas suberectas, verde-olivaceas.; En suelos degradados con acumulacion de sales.</no><br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Herbário do Museu Botânico Municipal (MBM)</span></td></tr></table>
            </td></tr></table></div>
            <br/><div class="record" id="record_4"><table border="0" width="100%"><tr id="detail_4" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=MBM" target="manager"><img align="right" src="logos/institutions/MBM.png" width="50px"/></a></td>
            <td><span onclick="top.getDetail(823583029,4)">
            <span class="tK">Plantae</span> <span class="tF">Amaranthaceae</span> <br/> <span class="tGa"> <u>Salicornia</u> </span> <span class="tEa"> <u>ambigua</u> </span> <span class="tA">Michx.</span><br/> <span class="tN">MBM 95818</span> <ll>Coleta: </ll> <span class="cL">Cristóbal, CL</span> <span class="cN">2017</span> <span class="cY">23/09/1983</span>. <br/> <ll>Loc: </ll> <span class="lP">5 km E de ayo. Golondrinas, camino a Fortín Olmos.</span>, <span class="lM">Vera</span>, <span class="lS">Santa Fe</span>, <span class="lC">Argentina</span> <ll>Cód. barras: </ll> <span class="bC">MBM095818.</span> <br/> <ll>Coord. orig.:  </ll> <span class="lA">[<i>lat: </i>-29.666667</span> <span class="lO"> <i>long: </i>-60.5</span> WGS84]<br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Herbário do Museu Botânico Municipal (MBM)</span></td></tr></table>
            </td></tr></table></div>
            <br/><div class="record" id="record_5"><table border="0" width="100%"><tr id="detail_5" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=MBM" target="manager"><img align="right" src="logos/institutions/MBM.png" width="50px"/></a></td>
            <td><span onclick="top.getDetail(823583028,5)">
            <span class="tK">Plantae</span> <span class="tF">Amaranthaceae</span> <br/> <span class="tGa"> <u>Salicornia</u> </span> <span class="tEa"> <u>ambigua</u> </span> <span class="tA">Michx.</span><br/> <span class="tN">MBM 66977</span> <ll>Coleta: </ll> <span class="cL">Schinini, A; Bordas, E</span> <span class="cN">16576</span> <span class="cY">14/03/1979</span>. <br/> <ll>Loc: </ll> <span class="lP">Ruta Trans-Chaco.</span> <span class="lS">Presidente Hayes</span>, <span class="lC">Paraguay</span> <ll>Cód. barras: </ll> <span class="bC">MBM066977.</span> <br/> <ll>Coord. orig.:  </ll> <span class="lA">[<i>lat: </i>-22.916667</span> <span class="lO"> <i>long: </i>-59.416667</span> WGS84]<br/> <ll>Notas:</ll> <no>Tallos expuestos al sol, rojizos. Sufrútice. 0.5m de altura. Apoyante.</no><br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Herbário do Museu Botânico Municipal (MBM)</span></td></tr></table>
            </td></tr></table></div>
            <br/><div class="record" id="record_6"><table border="0" width="100%"><tr id="detail_6" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=SP" target="manager"><img align="right" src="logos/institutions/IBT.gif" width="50px"/></a></td>
            <td><span onclick="top.getDetail(887476652,6)">
            <span class="tK">Plantae</span> <span class="tF">Amaranthaceae</span> <br/> <span class="tGa"> <u>Salicornia</u> </span> <span class="tEa"> <u>ambigua</u> </span> <span class="tA">Michx.</span>. <ll>Det: </ll> <span class="tI">Soriano, A</span><br/> <span class="tN">SP 54084</span> <ll>Coleta: </ll> <span class="cL">Krapovickas, A</span> <span class="cN">806</span> <span class="cY">30/12/1944</span>. <br/> <ll>Loc: </ll> <span class="lP">Estância "Las Marias"</span> <span class="lS">Santa Fé</span>, <span class="lC">Argentina</span> <ll>Cód. barras: </ll> <span class="bC">SP011110.</span><br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Herbário do Estado "Maria Eneyda P. Kaufmann Fidalgo" - Coleção de Fanerógamas (SP)</span></td></tr></table>
            </td></tr></table></div>
            <td align="right"><table><tr><td valign="top" width="50px"><a class="highslide" href="http://reflora.cria.org.br/inct/exsiccatae/image/imagecode/SP011110/size/huge/format/jpeg/foo/17370" onclick="return top.hs.expand(this, { slideshowGroup: 6 }, { bc: 'SP011110' })"><img align="right" alt='&lt;table width="100%"&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;Herbário Maria Eneyda P. Kauffmann Fidalgo, Instituto de Botânica, São Paulo [&lt;a href="downImage?imagecode=SP011110"&gt;SP011110&lt;/a&gt;]&lt;/b&gt;&lt;/td&gt;&lt;td
            align="right"&gt;&lt;a href="http://reflora.cria.org.br/inct/exsiccatae/viewer/imagecode//SP011110/format/slide/initialimagecode/SP011110/foo/17370"
            target="other" class="oV"&gt;&lt;big&gt;abrir no &lt;/big&gt;  &lt;img src="imgs/eh.png" height="15px"&gt;&lt;/a&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;
            #CCCCCC; border-radius: 5px; visibility: hidden" title="Herbário Maria Eneyda P. Kauffmann Fidalgo, Instituto de Botânica, São Paulo [SP011110]"/></a>
            ' onload="this.style.visibility='visible'" src="http://reflora.cria.org.br/inct/exsiccatae/image/imagecode/SP011110/size/thumb/format/jpeg/foo/17370" style="box-shadow: 3px 3px 3px
            <div class="highslide-caption"><small><span class="tK">Plantae</span> <span class="tF">Amaranthaceae</span> <br/> <span class="tGa"> <u>Salicornia</u> </span> <span class="tEa"> <u>ambigua</u> </span> <span class="tA">Michx.</span>. <ll>Det: </ll> <span class="tI">Soriano, A</span></small></div>
            </td>
            <td rowspan="2" valign="top" width="21px"><a href="http://reflora.cria.org.br/inct/exsiccatae/viewer/imagecode//SP011110/format/slide/foo/17370" target="other" title="abrir no visualizador exsiccatae"><img align="right" height="50px" src="imgs/e.png"/></a></td>
            </tr></table></td><br/><div class="record" id="record_7"><table border="0" width="100%"><tr id="detail_7" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=MBM" target="manager"><img align="right" src="logos/institutions/MBM.png" width="50px"/></a></td>
            <td><span onclick="top.getDetail(823583027,7)">
            <span class="tK">Plantae</span> <span class="tF">Amaranthaceae</span> <br/> <span class="tGa"> <u>Salicornia</u> </span> <span class="tEa"> <u>ambigua</u> </span> <span class="tA">Michx.</span><br/> <span class="tN">MBM 55881</span> <ll>Coleta: </ll> <span class="cL">Krapovickas, A; Schinini, A</span> <span class="cN">30454</span> <span class="cY">23/03/1977</span>. <br/> <ll>Loc: </ll> <span class="lP">Copo Quille</span>, <span class="lM">Dep. Rosario de la Frontera</span>, <span class="lS">Salta</span>, <span class="lC">Argentina</span> <ll>Cód. barras: </ll> <span class="bC">MBM055881.</span> <br/> <ll>Notas:</ll> <no>1 a 1,5m de altura.</no><br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Herbário do Museu Botânico Municipal (MBM)</span></td></tr></table>
            </td></tr></table></div>
            <br/><div class="record" id="record_8"><table border="0" width="100%"><tr id="detail_8" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=MBM" target="manager"><img align="right" src="logos/institutions/MBM.png" width="50px"/></a></td>
            <td><span onclick="top.getDetail(823583023,8)">
            <span class="tK">Plantae</span> <span class="tF">Amaranthaceae</span> <br/> <span class="tGa"> <u>Salicornia</u> </span> <span class="tEa"> <u>ambigua</u> </span> <span class="tA">Michx.</span><br/> <span class="tN">MBM 17699</span> <ll>Coleta: </ll> <span class="cL">Krapovickas, A; Irigoyen, J</span> <span class="cN">17798</span> <span class="cY">27/01/1971</span>. <br/> <ll>Loc: </ll> <span class="lP">Ayo. Colastiné, 15 km S de Coronda, Ruta Nacional 11.</span>, <span class="lM">San Jerónimo</span>, <span class="lS">Santa Fé</span>, <span class="lC">Argentina</span> <ll>Cód. barras: </ll> <span class="bC">MBM017699.</span> <br/> <ll>Notas:</ll> <no>Suelo salino.</no><br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Herbário do Museu Botânico Municipal (MBM)</span></td></tr></table>
            </td></tr></table></div>
            <br/>
            <div id="div_hint_action"><table border="0" cellpadding="0" cellspacing="0" width="100%">
            <tr>
            <td align="right"><table><tr valign="top">
            <th><img align="left" height="20px" src="imgs/summary_icon.png"/><select onchange="top.getStats(this[this.selectedIndex].value,0);this.selectedIndex=0;" style="width: 100px">
            <option value="">resumo</option>
            <option value="tables">… tabelas</option>
            <option value="maps">… mapas</option>
            <option value="graphs">… gráficos</option>
            </select></th>
            <th> </th>
            <th><img align="left" height="20px" src="imgs/picture_icon.png"/><select onchange="top.getImages(this[this.selectedIndex].value,top.RecsOffset);this.selectedIndex=0;" style="width: 100px">
            <option value="">imagens</option>
            <option title="ver imagens numa tabela" value="thumb">… mosaico</option>
            <option title="comparar as imagens lado a lado" value="compare">… comparar</option>
            <option title="ver as imagens como catálogo" value="book">… catálogo</option>
            </select>
            </th>
            <th> </th>
            <th><img align="left" height="20px" src="imgs/map_icon.png"/><select onchange="top.getMap(this[this.selectedIndex].value);this.selectedIndex=0;" style="width: 100px">
            <option value="">mapa</option>
            <option value="global">… global</option>
            <option value="collectioncode">… por coleção</option>
            <option value="genus">… por gênero</option>
            <option value="norm_yearcollected">… por ano de coleta</option>
            <option value="density">… por densidade</option>
            </select>
            </th>
            <th> </th>
            <th><img align="left" height="20px" src="imgs/graph_icon.png"/><select onchange="top.getGraph(this[this.selectedIndex].value,1);this.selectedIndex=0;" style="width: 100px">
            <option value="">gráfico</option>
            <option value="collection.column.1">… por coleção</option>
            <option value="family.column.1">… por família</option>
            <option value="genus.column.1">… por gênero (máx 100)</option>
            <option value="stateprovince.column.1">… por estado</option>
            <option value="typestatus.column.1">… por typus</option>
            <option value="yearcollected.column.1">… por ano de coleta</option>
            <option value="monthcollected.column.1">… por mês de coleta</option>
            <option value="yearidentified.column.1">… por ano de identificação</option>
            </select></th>
            <th> </th>
            <th><img align="left" height="20px" src="imgs/down_icon.png"/><select onchange="top.preDownLoad(this[this.selectedIndex].value);this.selectedIndex=0;" style="width: 100px">
            <option value="">download</option>
            <option value="dwc_csv">… dados completos</option>
            <option value="openModeller">… openModeller</option>
            <option value="Maxent">… Maxent</option>
            </select>
            </th>
            <th> </th>
            </tr></table></td></tr>
            </table></div>
            ''', features="html.parser")

        
