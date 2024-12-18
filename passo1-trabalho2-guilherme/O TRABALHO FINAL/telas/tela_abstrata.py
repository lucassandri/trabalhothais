import PySimpleGUI as sg
from abc import ABC, abstractmethod

class TelaAbstrata(ABC):
    def __init__(self):
        self.__window = None
        self.init_components()

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window
    
    @abstractmethod
    def tela_opcoes(self):
        pass

    @abstractmethod
    def init_components(self):
        pass

    def le_num_inteiro(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos or valor_int < 0:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)
    
    def le_float(self, mensagem=" "):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_float = float(valor_lido)
                if valor_float < 0:
                    raise ValueError
                return valor_float
            except ValueError:
                print("Valor incorreto!")
    
    
    def le_string(self, mensagem=" "):
        while True:
            valor_lido = input(mensagem)
            try:
                for caractere in valor_lido:
                    if caractere.isdigit():
                        raise ValueError
                return valor_lido
            except ValueError:
                print("Não é possível adicionar números nesse campo!")
    
    def le_email(self, mensagem=" "):
        while True:
            valor_lido = input(mensagem)
            try:
                for caractere in valor_lido:
                    if caractere in ["'", '"','+',',','`','[',']',';','{','}','(',')','','/','*','#','!','?', '|', "\"", "=" ,":", ' ', '<', '>']:
                        raise ValueError
                return valor_lido
            except ValueError:
                print("Só é possivel adicionar caracteres nesse campo!")

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
