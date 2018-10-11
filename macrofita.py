class Macrofita:
    def __init__(self, nomeEspecie):
        self.__nomeEspecie = nomeEspecie
        self.__statusFlora = ''
        self.__nomeFlora = ''
        self.__statusPlantlist = ''
        self.__nomePlantlist = ''
        self.__floraXplantlist = ''
        self.__obs = ''
        self.__autorFloraBrasil = ''
        self.__autorPlantlist = ''
    
    def printMacrofita(self):
        print('\t',self.nomeEspecie, '|' + self.statusFlora + '|', self.nomeFlora,
              '|' + self.statusPlantlist + '|', self.nomePlantlist, '|' + self.floraXplantlist + '|', self.obs)
        
    def saidaStringExel(self):
        return self.nomeEspecie + ',' + self.statusFlora + ',' + self.nomeFlora + ',' + self.autorFloraBrasil + ',' + self.statusPlantlist + ',' + self.nomePlantlist + ',' + self.autorPlantlist + ',' + self.obs + ',' + self.floraXplantlist+'\n'

    @property
    def nomeEspecie(self):
        return self.__nomeEspecie

    @property
    def statusFlora(self):
        return self.__statusFlora

    @property
    def nomeFlora(self):
        return self.__nomeFlora
    
    @property
    def statusPlantlist(self):
        return self.__statusPlantlist

    @property
    def nomePlantlist(self):
        return self.__nomePlantlist

    @property
    def floraXplantlist(self):
        return self.__floraXplantlist
    
    @property
    def obs(self):
        return self.__obs
    
    @property
    def autorFloraBrasil(self):
        return self.__autorFloraBrasil

    @property
    def autorPlantlist(self):
        return self.__autorPlantlist

    @statusFlora.setter
    def statusFlora(self, status):
        self.__statusFlora = status

    @statusPlantlist.setter
    def statusPlantlist(self, status):
        self.__statusPlantlist = status

    @nomeFlora.setter
    def nomeFlora(self, nome):
        self.__nomeFlora = nome
        
    @nomePlantlist.setter
    def nomePlantlist(self, nome):
        self.__nomePlantlist = nome

    @obs.setter
    def obs(self, obs):
        if len(self.nomeFlora) == 0:
            self.__obs = obs
    
    @autorFloraBrasil.setter
    def autorFloraBrasil(self, autor):
        self.__autorFloraBrasil = autor

    @autorPlantlist.setter
    def autorPlantlist(self, autor):
        self.__autorPlantlist = autor

