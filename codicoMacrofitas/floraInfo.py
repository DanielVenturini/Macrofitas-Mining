class FloraInfo:
    def __init__(self,nome):
        self.nome = nome
        self.__taxonomica = ''
        self.__familia = ''
        self.__formaVida = ''
        self.__substrato = ''
        self.__origem = ''
        self.__endemismo = ''
        self.__ocorenciaConfirmada = []
        self.__possiveisOcorrencias = []
        self.__fitogeografico = ''
        self.__vegetacao = ''

    def printInfo(self):
        print(
        self.nome,
        ':\n----',
        self.taxonomica,
        '\n----',
        self.familia,
        '\n----',
        self.formaVida,
        '\n----',
        self.substrato,
        '\n----',
        self.origem,
        '\n----',
        self.endemismo,
        '\n----',
        self.ocorenciaConfirmada, 
        '\n----',
        self.possiveisOcorrencias,
        '\n----',
            self.fitogeografico,
        '\n----',
        self.vegetacao,
        '\n\n\n',
        )

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.strip()

    @property
    def taxonomica(self):
        return self.__taxonomica
        
    @taxonomica.setter
    def taxonomica(self, taxonomica):
        self.__taxonomica = taxonomica.strip()

    @property
    def familia(self):
        return self.__familia

    @familia.setter
    def familia(self, familia):
        self.__familia = familia.strip()

    @property
    def formaVida(self):
        return self.__formaVida

    @formaVida.setter
    def formaVida(self, formaVida):
        self.__formaVida = formaVida

    @property
    def substrato(self):
        return self.__substrato

    @substrato.setter
    def substrato(self, substrato):
        self.__substrato = substrato

    @property
    def origem(self):
        return self.__origem

    @origem.setter
    def origem(self, origem):
        self.__origem = origem.strip()

    @property
    def endemismo(self):
        return self.__endemismo

    @endemismo.setter
    def endemismo(self, endemismo):
        self.__endemismo = endemismo.strip()

    @property
    def ocorenciaConfirmada(self):
        return self.__ocorenciaConfirmada
    
    @ocorenciaConfirmada.setter
    def ocorenciaConfirmada(self, ocorenciaConfirmada):
        for pOcorencia in ocorenciaConfirmada:
            self.__ocorenciaConfirmada.append(pOcorencia)

    @property
    def possiveisOcorrencias(self):
        return self.__possiveisOcorrencias

    @possiveisOcorrencias.setter
    def possiveisOcorrencias(self, possiveisOcorrencias):
        for pOcorencia in possiveisOcorrencias:
            self.__possiveisOcorrencias.append(pOcorencia)

    @property
    def fitogeografico(self):
        return self.__fitogeografico

    @fitogeografico.setter
    def fitogeografico(self, fitogeografico):        
        self.__fitogeografico = fitogeografico

    @property
    def vegetacao(self):
        return self.__vegetacao

    @vegetacao.setter
    def vegetacao(self, vegetacao):
        self.__vegetacao = vegetacao
