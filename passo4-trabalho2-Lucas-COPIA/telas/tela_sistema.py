from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaSistema(TelaAbstrata):

    def __init__(self):
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('Bem vindo ao sistema da escola!', font=("Arial", 25))],
            [sg.Text('Escolha sua opção', font=("Arial", 15))],
            [sg.Radio('Alunos', "RD1", key='1')],
            [sg.Radio('Finanças', "RD1", key='2')],
            [sg.Radio('Funcionários', "RD1", key='3')],
            [sg.Radio('Professores', "RD1", key='4')],
            [sg.Radio('Finalizar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Sistema da escola').Layout(layout)
