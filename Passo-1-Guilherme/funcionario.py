from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, cargo: str, salario: float):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario