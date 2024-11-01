from boletim import Boletim
from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: int, pais: str, serie: str, bolsa: bool, mensalidade: float):
        self.__nome = nome
        self.__matricula = matricula
        self.__pais = pais
        self.__serie = serie
        self.__bolsa = bolsa
        self.__mensalidade = mensalidade
        self.__boletim = []

    @property
    def boletim(self):
        return self.__boletim

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

    def media_ultimo_boletim(self):
        ultimo_boletim = self.__boletim[-1]
        if len(self.__boletim) == 0:
            return 0
        if len(ultimo_boletim) == 0:
            return 0
        media = sum(ultimo_boletim) / len(ultimo_boletim)
        return media