from pessoa import Pessoa
from boletim import Boletim

class Aluno(Pessoa):
    
    def __init__(self, nome: str, matricula: int, responsavel: str, serie: str, bolsa: bool, mensalidade: float, boletim: Boletim):
        super().__init__(nome)
        self.__matricula = matricula
        self.__responsavel = responsavel
        self.__serie = serie
        self.__bolsa = bolsa
        self.__mensalidade = mensalidade
        self.__boletim = None

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def responsavel(self):
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, responsavel):
        self.__responsavel = responsavel

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
        self.__boletim = boletim

    @property
    def mensalidade(self):
        return self.__mensalidade

    @mensalidade.setter
    def mensalidade(self, mensalidade):
        self.__mensalidade = mensalidade