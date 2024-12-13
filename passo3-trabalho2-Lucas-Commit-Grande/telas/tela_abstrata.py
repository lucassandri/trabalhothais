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

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values