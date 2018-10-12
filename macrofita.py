class Macrofita:
    def __init__(self, nomeEspecie):
        self.__nomeEspecie = nomeEspecie
        self.__statusFlora = ''
        self.__nomeFlora = ''
        self.__statusPlantlist = ''
        self.__nomePlantlist = ''
        self.__floraXplantlist = ''
        self.__obsFlora = ''
        self.__obsPlantlist = ''
        

    def printMacrofita(self):
        print('\t',self.nomeEspecie, '|' + self.statusFlora + '|', self.nomeFlora, '|' + self.obsFlora ,'|' + self.statusPlantlist + '|', self.nomePlantlist, '|' + self.obsPlantlist ,'|' + self.floraXplantlist + '|')
    
    def saidaStringExel(self):
        return self.nomeEspecie + ',' + self.statusFlora + ',' + self.nomeFlora + ',' + self.obsFlora + ',' + self.statusPlantlist + ',' + self.nomePlantlist + ',' + self.obsPlantlist + ',' + self.floraXplantlist+'\n'

    def comaparaNome(self,site):
        if(site == 'flora'):
            if(self.nomeEspecie.replace(' ', '') != self.nomeFlora.replace(' ', '')):
                self.obsFlora = 'Autor Incorreto'
        elif(site == 'plantlist'):
            if(self.nomeEspecie.replace(' ', '') != self.nomePlantlist.replace(' ', '')):
                self.__obsPlantlist = 'Autor Incorreto'
        else:
            print('comparaNome--error' + site)
            
    def comparaFloraPlantlist(self):
        if(self.nomeFlora and self.nomePlantlist and self.nomeFlora != self.nomePlantlist):
            self.floraXplantlist = 'Diferente'

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
    def obsFlora(self):
        return self.__obsFlora

    @property
    def obsPlantlist(self):
        return self.__obsPlantlist

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

    @obsFlora.setter
    def obsFlora(self, obs):
        self.__obsFlora = obs

    @obsPlantlist.setter
    def obsPlantlist(self, obs):
        if(self.nomeFlora.__len__() == 0):
            self.__obsPlantlist = obs
    
    @floraXplantlist.setter
    def floraXplantlist(self, data):
        self.__floraXplantlist = data
