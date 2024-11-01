from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome: str, salario: float, leciona: str, email: str):
        super.__init__(nome)
        self.__salario = salario
        self.__leciona = leciona
        self.__email = email

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def leciona(self):
        return self.__leciona

    @leciona.setter
    def leciona(self, leciona):
        self.__leciona = leciona

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email