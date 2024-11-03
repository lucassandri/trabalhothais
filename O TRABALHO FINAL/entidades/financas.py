class Financas():

    def __init__(self, despesas_agua: float, despesas_luz: float, despesas_internet: float, despesas_estrutura: float):
        self.__despesas_agua = despesas_agua
        self.__despesas_luz = despesas_luz
        self.__despesas_internet = despesas_internet
        self.__despesas_estrutura = despesas_estrutura

    @property
    def despesas_agua(self):
        return self.__despesas_agua
    
    @despesas_agua.setter
    def despesas_agua(self, despesas_agua):
        self.__despesas_agua = despesas_agua
    
    @property
    def despesas_luz(self):
        return self.__despesas_luz
    
    @despesas_luz.setter
    def despesas_luz(self, despesas_luz):
        self.__despesas_luz = despesas_luz
    
    @property
    def despesas_internet(self):
        return self.__despesas_internet
    
    @despesas_internet.setter
    def despesas_internet(self, despesas_internet):
        self.__despesas_internet = despesas_internet
    
    @property
    def despesas_estrutura(self):
        return self.__despesas_estrutura
    
    @despesas_estrutura.setter
    def despesas_estrutura(self, despesas_estrutura):
        self.__despesas_estrutura = despesas_estrutura
