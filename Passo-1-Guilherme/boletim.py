class Boletim:
    def __init__(self, notas: list, frequencia_suficiente: bool):
        self.__notas = notas
        self.__frequencia_suficiente = frequencia_suficiente

    @property
    def notas(self):
        if isinstance(self.__notas, list):
            return self.__notas

    @notas.setter
    def notas(self, notas):
        if isinstance(self.__notas, list):
            self.__notas = notas

    @property
    def frequencia_suficiente(self):
        if isinstance(self.__frequencia_suficiente, bool):
            return self.__frequencia_suficiente

    @frequencia_suficiente.setter
    def frequencia_suficiente(self, frequencia_suficiente):
        if isinstance(self.__frequencia_suficiente, bool):
            self.__frequencia_suficiente = frequencia_suficiente

    def media_final(self):
        return sum(self.__notas) / len(self.__notas)

    def aprovado(self):
        if (sum(self.__notas) / len(self.__notas)) >= 7 and self.__frequencia_suficiente == True:
            return True
        else:
            return False