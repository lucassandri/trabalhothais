from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, cargo: str, salario: float, email: str):
        super().__init__(nome)
        self.__cargo = cargo
        self.__salario = salario
        self.__email = email

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
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
