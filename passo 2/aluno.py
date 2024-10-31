from boletim import Boletim
lista_alunos = []
class Aluno:
    def __init__(self, nome: str, matricula: int, pais: str, serie: str, bolsa: bool, boletim: 'Boletim', mensalidade: float):
        self.__nome = nome
        self.__matricula = matricula
        self.__pais = pais
        self.__serie = serie
        self.__bolsa = bolsa
        if isinstance(boletim, Boletim):
            self.__boletim = boletim
        self.__mensalidade = mensalidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @property
    def serie(self):
        return self.__serie

    @serie.setter
    def serie(self, serie):
        self.__serie = serie

    @property
    def bolsa(self):
        return self.__bolsa

    @bolsa.setter
    def bolsa(self, bolsa):
        self.__bolsa = bolsa

    @property
    def boletim(self):
        return self.__boletim

    @boletim.setter
    def boletim(self, boletim):
        if isinstance(boletim, Boletim):
            self.__boletim = boletim

    @property
    def mensalidade(self):
        return self.__mensalidade

    @mensalidade.setter
    def mensalidade(self, mensalidade):
        self.__mensalidade = mensalidade
