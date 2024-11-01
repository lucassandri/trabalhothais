class Professor:
    def __init__(self, nome: str, salario: float, leciona: str, email: str):
        self.__nome = nome
        self.__salario = salario
        self.__leciona = leciona
        self.__email = email
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

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